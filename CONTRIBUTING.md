# Contributing

Use Python 3.12, Git and [Lefthook](https://lefthook.dev/installation/). Install the hooks once per clone with `lefthook install`.

## Verification

Run `scripts/verify` before opening a PR. The commit-message hook checks the header, and the pre-push hook and CI run the same suite. Temporary repositories and synthetic fixtures cover profile generation, read-only planning, fingerprints, file preservation, site URLs, public artifact scope, installer safety and commit headers. Verify hosted Pages, recording and optional integrations separately when relevant.

## Commits and review

- Branch from `main`. Explain the reason for the change, its scope and how to verify it in the PR.
- Use [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commit headers and PR titles. Use `type(scope)!: description` with an optional scope and breaking-change marker. Run `git config commit.template .gitmessage.txt` to enable the optional template.
- Squash merge with the PR title and description as the commit message. For a breaking change, use `!` in the title or add a `BREAKING CHANGE: ...` footer after a blank line at the end of the description. Review the final squash message before merging.
- Review the diff and wait for CI. Check dependency updates and permission changes explicitly. The repository maintainer reviews the sensitive paths listed in [CODEOWNERS](.github/CODEOWNERS).
- See [release operations](docs/deployment.md) for versioning and [SECURITY.md](SECURITY.md) for vulnerability reports.
