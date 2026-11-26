# OSS Showcase on Product Hunt

Review copy prepared on 2026-11-26 (Europe/Rome). Draft for the maintainer’s approval.

## Listing

**Name**

OSS Showcase

**Tagline**

Ship a README, real demo, and GitHub Pages site

**Description**

Your code runs. Show people how. OSS Showcase reads your repo and plans a README, real demo, and GitHub Pages site. You choose what the agent edits. A static generator and validator prepare the files you review before publishing.

**Product URL**

https://ifthenelse.github.io/oss-showcase/

**Additional link**

https://github.com/ifthenelse/oss-showcase

**Suggested launch tags**

Developer Tools, GitHub. Confirm available tags in the editor.

## First Maker comment

👋 I maintain OSS Showcase. If you’ve ever opened a repo and wondered what to run first, that’s the problem this skill is meant to help with.

I tested it on Task Counter, a tiny Python CLI that counts task names. Codex and Claude read the fixture and proposed what to show. The clip ends at the first decision: do you want the agent to edit the README?

The rest follows the same plan. The README, demo, and Pages site draw on the same repo evidence. The Python generator and validator prepare a reviewable site artifact. Publishing has its own confirmation.

Try it from your project folder with `npx skills add ifthenelse/oss-showcase --skill oss-showcase`. Which part of getting a repo ready for strangers takes you longest: the first-run instructions, a real demo, or the project page?

## Upload assets

| Slot | File | Suggested alt text |
| --- | --- | --- |
| Logo | [Otto S](otto-s-240.png) | Lime angular S inside an octagonal frame on a graphite background. |
| Gallery 1 | [Claude Desktop approval](01-claude-desktop-approval.png) | Claude Desktop shows the first confirmation and choices for a synthetic Task Counter project. |
| Gallery 2 | [Codex CLI plan](02-codex-cli-plan.png) | Codex CLI loads OSS Showcase, proposes a guided plan for Task Counter, and requests a decision. |
| Gallery 3 | [Claude Code CLI plan](03-claude-code-cli-plan.png) | Claude Code CLI shows the Task Counter plan and asks whether to start the README step. |

The public [58-second demo](https://ifthenelse.github.io/oss-showcase/#demo) is available on the product page. The gallery was extracted from that recording. Its button labels reflect the recorded run.

## Publication handoff

- Select the Maker role only after confirming who will submit the launch. Check the personal account, posting access, available tags, and duplicate or relaunch status in the editor.
- The [latest tagged release](https://github.com/ifthenelse/oss-showcase/releases/tag/v0.1.0) predates the guided workflow. The copy directs readers to install from the default branch. The public repository reports no license, so leave the Open Source listing flag unset.
- Confirm the listing preview, exact date and posting account before scheduling. The current demo covers Codex CLI, Claude Code CLI, and Claude Desktop. Codex Desktop has a pending clip.

[Product Hunt listing guide](https://help.producthunt.com/en/articles/17834537-4-build-your-product-page) · [Product Hunt posting requirements](https://help.producthunt.com/en/articles/479557-how-to-post-a-product)
