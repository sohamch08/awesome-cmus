# Research notes

[Back to the list](../README.md)

## Sources and coverage

This repository combines an existing cmus research note with a later ecosystem guide and a catalog of 48 configurations, workflow examples, creator demonstrations, and screenshot posts.

- The source material contained 305 distinct external URLs.
- The README contains 191 resource entries after editorial deduplication and separation of historical material.
- All original source URLs are retained in the [source-link inventory](../data/source-links.json), including links not promoted to the README.
- Longer explanations are in the [ecosystem guide](ecosystem-guide.md) and [setup catalog](setups.md).

## Verification scope

Research and repository metadata were reviewed on November 6, 2026. The [GitHub metadata snapshot](../data/github-metadata.json) covers 189 referenced repositories. It records repository availability, canonical names, archival state, default branches, and push timestamps.

This is not an installation or runtime compatibility test. Repository metadata does not validate every file path, article, screenshot, release artifact, or service API. HTTP access errors can also reflect rate limits or access controls. The structural checker validates this repository's Markdown navigation and files without treating remote availability as a permanent property.

## Corrections and qualifications

- `mzivic7/spectroterm` resolves to `sparklost/spectroterm`; the catalog uses the canonical owner.
- `ronno/scripts` was unavailable in the metadata check; its historical status script is not promoted as a current integration.
- `jboynyc/cmus_app`, `seriousben/cmus-droid-remote`, and the two `0x61nas/cmus-rpc` implementations are explicitly archived.
- Current inspected `fortes/dotfiles` files center on MPD/rmpc rather than the old cmus setup implied by discovery results.
- The original wiki-linked cmusCoversSDL repository was unavailable during earlier research; a surviving fork is listed.
- A screenshot of artwork beside cmus does not establish that cmus renders the image itself.
- Commented configuration examples are distinguished from enabled behavior in the setup notes.

## Attribution

The sectioned resource-list format was inspired by [rothgar/awesome-tmux](https://github.com/rothgar/awesome-tmux). Descriptions here were written for this cmus catalog. Project documentation, author posts, and the upstream cmus wiki are linked beside the relevant resources. This list is independent of the cmus project.

## Updating the catalog

Check the resource's own documentation and actual configuration where possible. Update the description or move the entry to historical resources when its purpose, canonical location, or compatibility changes. Do not infer maintenance quality solely from stars, tags, or a recent commit date.
