# Package distribution

Run this stage in launch mode for applications and CLIs. In prepare-release mode validate release assets and prepare or refresh package definitions. In audit mode inspect and report only. Treat `launch --submit-packages <release> <channels>` as authorization to submit eligible requests or pull requests for the named release and channels. Example: `launch --submit-packages v1.2.0 homebrew,winget`. The plain `launch` mode prepares drafts. Never infer additional publishing permissions from the flag. Use the active client's approval flow when a tool requires one.

## Select channels

Confirm supported operating systems and CPU architectures from CI, release assets and documentation. Verify submission policy, access, ownership and package type on the official channel at execution time. Select appropriate package managers for the supported systems.

| Platform | Channels and submission path |
| --- | --- |
| macOS | Homebrew Core formula for eligible software under Core rules. Evaluate Homebrew Cask for eligible prebuilt macOS apps or binaries. Search both collections for duplicates. If upstream eligibility is unmet, prepare a project tap. Publishing the tap or its repo requires separate authorization. |
| Windows | Prepare and validate a WinGet manifest for a supported installer or portable artifact. Submit to `microsoft/winget-pkgs` using WinGet Create or the official PR flow. Consider Scoop for portable tools and Chocolatey for eligible releases when those channels are selected. |
| Linux | Select by supported distribution and packaging format. Consider Flathub for desktop apps, Snap Store for compatible apps or CLIs, and distro-specific routes such as a Debian RFP or Arch AUR package where appropriate. Distinguish an intake request, maintainer contribution and direct registry publication. AUR upload, Snap channel release and other direct publication need separate authorization. Use the distro's actual maintainer process when no external submission route exists. |
| Ecosystem | Validate existing npm, PyPI, crates.io or other package metadata when relevant to installation. Each registry upload requires separate authorization. |

[Homebrew submission guide](https://docs.brew.sh/Adding-Software-to-Homebrew) · [WinGet submission guide](https://learn.microsoft.com/en-us/windows/package-manager/package/) · [Debian WNPP](https://www.debian.org/devel/wnpp/) · [Flathub submission](https://docs.flathub.org/docs/for-app-authors/submission/)

## Verify and submit

1. Resolve the exact public release and upstream origin. Verify license, package ownership, version, architectures, fixed artifact URLs, publisher-required signing and SHA-256 hashes from actual artifacts. Never submit placeholder manifests. For a previously listed product, follow the existing package's update path.
2. Search the destination registry and open requests or PRs for equivalent package identifiers, release versions and submission scope. Reuse an existing open request. Record its URL. Avoid duplicates when rerunning or resuming after a timeout.
3. Draft the manifest, submission text, test commands and declared destination in `.agents/showcase/launch/packages/`. Invoke the destination's official validator. Test installation and a version or startup smoke check on a representative clean supported environment. Test upgrade or uninstall where the destination requires it. Report unverified architectures and skip submission where required validation is missing.
4. For the explicitly authorized channels, submit only where the release is eligible, tests are adequate and the active client exposes a supported write route. Prefer the GitHub integration or an authenticated official CLI. If an upstream PR requires a public fork or branch, check what the tooling would create. Use an existing dedicated fork and submit only the reviewed packaging files. If no appropriate fork or tool exists or there is an account, policy or maintainer blocker, keep the draft and report the exact dependency. Never include repository secrets or unrelated files. Do not push or tag the product repository or publish a release as part of the request.
5. Query the resulting URL or request ID. Update the tracker with manager, target, package ID, release, validation, status and blocker. Mark submission and upstream acceptance as separate states. HTTP success or a local CLI exit code alone does not establish acceptance. Keep this workflow outside routine CI.

Verify live eligibility and tool availability for each run. Requests are subject to upstream review. Report a draft, pending request, already listed package or verified accepted listing accurately.
