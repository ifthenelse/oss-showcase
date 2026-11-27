# Release operations

The Release workflow runs on manual dispatch. A maintainer chooses the version and reviews the changelog before starting it. Use [SemVer 2.0.0](https://semver.org/) to choose a patch for compatible fixes, a minor version for compatible features and a major version for breaking changes. Assess the combined changes since the last published release. If an unpublished version already represents that scope, keep it and update its changelog entry.

## GitHub setup

- Protect `main` with a PR requirement and the `verify` check. Use squash merges and the PR title and description for the squash message.
- Enable private vulnerability reporting and GitHub secret scanning and push protection where available.
- Use an account with write access to [run the workflow manually](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow). The publish job uses GitHub's built-in token with `contents: write` and only publishes from `main` in the official repository.

## Publish and recover

1. Include `version.txt` and its matching dated `CHANGELOG.md` entry in the PR that prepares the next stable version. Wait for CI to pass, then merge.
2. In **Actions → Release → Run workflow**, select `main` and dispatch. The workflow verifies the selected commit, creates its matching `v` tag and publishes the GitHub Release with that version's changelog section and standard source archives.
3. Verify the release tag points to the commit shown in the workflow run and its archive includes the skill, references, scripts and templates.
4. If publishing fails after tagging, check whether the release exists and rerun the original workflow if needed. The workflow can reuse a tag at the same commit. For a bad published release, fix the change and publish a new version.

## Deploy the OSS Showcase site

In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. Then use **Actions → Deploy GitHub Pages → Run workflow**, select `main`, and dispatch. The workflow validates and publishes the allowlisted static bundle. The release workflow remains a separate manual operation.

## Publish a target project's showcase

Review the target landing's [copy and discovery checks](../references/publishing.md#discovery), then stage the exact Pages artifact. Confirm the deployment, verify the live URL and assets, and use that verified page in the [launch calendar](../references/distribution.md). Confirm each channel submission separately.

See the [Pages publication procedure](../references/publishing.md#publish-to-github-pages) for target project settings and verification.
