# Release operations

After successful verification on `main`, Release Please can propose a release PR. It generates `CHANGELOG.md`, updates `version.txt` and records the version in its manifest. Subsequent `fix` commits increment the patch, `feat` commits increment the minor and breaking changes increment the major. Other types can be used for repository maintenance.

## GitHub setup

- Automatic release PRs require **Allow GitHub Actions to create and approve pull requests** in **Settings → Actions → General**. This also grants approval capability. If the setting is disabled, use the manual release path below.
- Protect `main` with a PR requirement and the `verify` check. Use squash merges and the PR title and description for the squash message. Keep the generated release PR title and description intact.
- Enable private vulnerability reporting and GitHub secret scanning and push protection where available. The PR workflow uses no repository secrets.

## Publish and recover

1. Review the proposed changelog and version. If GitHub marks bot-triggered CI as approval required, select **Approve workflows to run** on the release PR.
2. Wait for `verify` to pass, then squash merge the release PR. The release workflow verifies `main` and publishes the GitHub Release with the matching `v` tag and GitHub source archives.
3. Verify the release tag points to the merged release commit and the source archive includes the skill, references, scripts and templates.
4. For a transient failure, rerun the failed workflow after checking whether the release already exists. For a bad release, revert or fix the change and publish a new version. Consumers can reinstall the previous tagged release while the fix is prepared.

## Manual release

Open a normal release PR with the changelog, version and manifest updated together. Wait for the required check and squash merge it. Create the GitHub Release and matching tag at the verified merge commit, then verify the archive as above. The first release, `v0.1.0`, followed this path.

## Publish a target project's showcase

Review the target landing's [copy and discovery checks](../references/publishing.md#discovery), then stage the exact Pages artifact. Confirm the deployment, verify the live URL and assets, and use that verified page in the [launch calendar](../references/distribution.md). Confirm each channel submission separately.

See the [Pages publication procedure](../references/publishing.md#publish-to-github-pages) for target project settings and verification.

[Release Please setup](https://github.com/googleapis/release-please-action#workflow-permissions) · [GitHub workflow approval for automated PRs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow)
