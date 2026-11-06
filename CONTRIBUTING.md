# Contributing

Help readers discover useful cmus resources and understand what each one adds.

## Adding a resource

Add the entry to the closest README category in alphabetical order. Use the canonical project or author URL and one concise sentence describing a concrete feature. For a general utility, explain its cmus connection. Prefer an author's repository, documentation, or original article over a mirror or aggregator.

Use this format:

```markdown
- [Project name](https://example.com/project) - Concrete description of what it adds to a cmus setup.
```

Do not add a duplicate entry simply because a project fits multiple categories. Link to a relevant guide section for a longer explanation. Separate platform support, author-declared experimental status, archival state, and observed availability from personal preference.

## Configurations and screenshots

Add substantial examples to `docs/setups.md`. Link directly to the relevant config or script when possible, describe the behavior worth borrowing, and label historical or screenshot-only references. Avoid attributing features to commented code or inferring a running application from appearance alone.

## Historical projects

Older resources can be valuable. Put explicitly archived, superseded, or historically interesting implementations in `docs/historical.md`. Explain the qualification rather than silently deleting a useful reference. An old push date alone is not evidence that a project is broken.

## Local validation

Run:

```sh
python3 scripts/check_catalog.py
```

This checks local Markdown links, anchors, duplicate README entries, the setup count, source inventory coverage, and formatting conventions. It does not install linked tools or make network requests. Include relevant manual link checks in the pull request description.

## Writing and licensing

Use plain English, concise descriptions, and standard GitHub Markdown. Avoid Obsidian-only links, em dashes, and triple-hyphen separators. Contributions to this list and its original descriptions are offered under CC0 1.0. Linked projects retain their own licenses.
