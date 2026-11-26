# OSS Showcase on Product Hunt

Review copy prepared on 2026-11-26 (Europe/Rome). Draft for the maintainer’s approval.

## Listing

**Name**

OSS Showcase

**Tagline**

Turn a repo into a README, demo, and project site

**Description**

OSS Showcase is an Agent Skill for maintainers. It inspects a repository, proposes a launch plan, and helps prepare a README, reproducible demo, and GitHub Pages site backed by project evidence. Review each step, and approve public publishing separately.

**Product URL**

https://ifthenelse.github.io/oss-showcase/

**Additional link**

https://github.com/ifthenelse/oss-showcase

**Suggested launch tags**

Developer Tools, GitHub. Confirm available tags in the editor.

## First Maker comment

Hi Product Hunt! I’m the maintainer of OSS Showcase. I built it to make the work around a release easier to review. The README, the demo, and the project page should all describe the same thing someone can actually try.

Point the skill at a repository and it starts with a plan. You can approve a step, skip it, or let the agent continue through the remaining local work. It uses the repository as evidence for the public copy, and a separate confirmation covers publishing. The static site generator and validator also run independently of the agent.

In the demo, the tool is a tiny Python task counter. The useful moment is when Claude or Codex has read enough to propose what to show and asks before changing anything.

Try it from a project directory with `npx skills add ifthenelse/oss-showcase --skill oss-showcase`. I’d love to know which part of preparing a release takes you the most time: explaining the project, making a demo, or getting the project page ready?

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
