# Publishing

[Back to the list](../README.md)

## Validate locally

```sh
python3 scripts/check_catalog.py
git status
```

## Choose the GitHub account

Confirm the active GitHub CLI account before creating a repository:

```sh
gh api user --jq .login
```

If needed, switch to the intended account using `gh auth switch` before publishing.

## Create and push

From the repository root, after selecting the destination account and public visibility:

```sh
gh repo create awesome-cmus --public --source . --remote origin --push
```

If the remote repository already exists, add its URL as `origin` and push the local main branch instead. Set a short repository description and the topics `awesome`, `awesome-list`, `cmus`, `terminal`, and `music-player` on GitHub.

The validation workflow runs on pushes, pull requests, and manual dispatch. It does not schedule recurring work or check external network links.
