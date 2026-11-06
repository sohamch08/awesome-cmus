#!/usr/bin/env python3
"""Check catalog structure offline using only the Python standard library."""

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
ERRORS = []


def fail(path, message):
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def prose(text):
    """Exclude fenced code from Markdown navigation checks."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence


def anchors(text):
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"<[^>]+>", "", heading).lower()
        slug = "".join(
            char for char in heading
            if char in " -_" or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in result:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        result.add(candidate)
    return result


def main():
    files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    documents = {}
    for path in files:
        raw = path.read_text(encoding="utf-8")
        body, fence = prose(raw)
        documents[path] = (body, anchors(body))
        if fence:
            fail(path, "unclosed code fence")
        if "[[" in body:
            fail(path, "Obsidian wiki link needs conversion to standard Markdown")
        if chr(0x2014) in raw or "-" * 3 in raw:
            fail(path, "use plain punctuation without long dashes or triple hyphens")

    remote_urls = set()
    for path, (body, _) in documents.items():
        targets = LINK.findall(body)
        targets.extend(re.findall(r'<(?:img|a)\b[^>]*\b(?:src|href)="([^"]+)"', body))
        for target in targets:
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme in {"http", "https"}:
                    remote_urls.add(target)
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not destination.is_relative_to(ROOT):
                fail(path, f"link leaves repository: {target}")
            elif not destination.is_file():
                fail(path, f"missing local file: {target}")
            elif parsed.fragment and destination.suffix == ".md":
                if destination not in documents or unquote(parsed.fragment) not in documents[destination][1]:
                    fail(path, f"missing heading anchor: {target}")

    readme = ROOT / "README.md"
    entries = re.findall(r"^- \[[^\]]+\]\((https?://[^)]+)\) - .+$", documents[readme][0], re.M)
    seen = set()
    for url in entries:
        canonical = url.rstrip("/").casefold()
        if canonical in seen:
            fail(readme, f"duplicate resource entry: {url}")
        seen.add(canonical)

    setups = ROOT / "docs/setups.md"
    numbers = [int(n) for n in re.findall(r"^### (\d+)\.", documents[setups][0], re.M)]
    if not numbers or numbers != list(range(1, len(numbers) + 1)):
        fail(setups, "setup entries must be numbered consecutively from 1")
    # Keep the human-readable counts synchronized with the actual catalog.
    for path, (body, _) in documents.items():
        for count in re.findall(r"\b(\d+) (?:configurations|setup examples)", body):
            if int(count) != len(numbers):
                fail(path, f"setup count {count} differs from catalog count {len(numbers)}")

    inventory_path = ROOT / "data/source-links.json"
    inventory = json.loads(inventory_path.read_text())["links"]
    source_urls = set()
    for item in inventory:
        url = item.get("url", "")
        if urlsplit(url).scheme not in {"http", "https"} or not urlsplit(url).netloc:
            fail(inventory_path, f"invalid source URL: {url}")
        if url in source_urls:
            fail(inventory_path, f"duplicate source URL: {url}")
        if not item.get("sources") or not item.get("labels"):
            fail(inventory_path, f"missing provenance: {url}")
        source_urls.add(url)

    research_path = ROOT / "docs/research.md"
    research = documents[research_path][0]
    expected = {
        r"contained (\d+) distinct external URLs": len(source_urls),
        r"README contains (\d+) resource entries": len(entries),
    }
    metadata = json.loads((ROOT / "data/github-metadata.json").read_text())
    expected[r"covers (\d+) referenced repositories"] = len(metadata["repositories"])
    for pattern, actual in expected.items():
        match = re.search(pattern, research)
        if match is None or int(match.group(1)) != actual:
            fail(research_path, f"snapshot count mismatch for {pattern}: expected {actual}")

    ElementTree.parse(ROOT / "assets/banner.svg")
    if ERRORS:
        print("\n".join(ERRORS), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} Markdown files, {len(entries)} README resources, and {len(numbers)} setups.")
    print(f"Retained {len(source_urls)} unique source URLs; {len(source_urls & remote_urls)} also appear in Markdown.")
    print("Local links, anchors, provenance, snapshot counts, and SVG structure passed.")
    print("External URLs and linked programs were not tested by this offline check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
