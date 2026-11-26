# OSS Showcase

**Turn a repository into a README, a reproducible demo, and a static project site backed by evidence from the code.**

OSS Showcase is an Agent Skill for maintainers who want installation instructions, examples, and release materials to tell the same story. It starts with a plan you can review and uses a deterministic generator and validator for the static site.

[Project site](https://ifthenelse.github.io/oss-showcase/) · [GitHub release v0.1.0](https://github.com/ifthenelse/oss-showcase/releases/tag/v0.1.0) · [Operating modes](references/modes.md)

## Quickstart

From the folder of a project you want to showcase, run:

```sh
npx skills add ifthenelse/oss-showcase --skill oss-showcase
```

Select an agent such as Codex, Claude Code, or GitHub Copilot. Open an agent session in the target project and invoke `$oss-showcase` in Codex or `/oss-showcase` in Claude Code. In other hosts, ask the agent to use OSS Showcase for the current project. For a monorepo, specify the package. Include your site URL if you know it.

The skill shows the ordered plan in the client's task list when available. Before each uncovered step, it offers **Accept once**, **Always accept** for the remaining planned local steps, or **Cancel** to skip the step. Publication has its own confirmation. The skill records outstanding tasks in the target project's `docs/HANDOFF.md`. See the [guided workflow](references/execution.md#guided-workflow).

For the packaged release, download and unpack the source archive from the release page and run `sh scripts/install.sh`. The installer copies skill files to `~/.agents/skills/oss-showcase/` and creates a Claude Code link. Install from the default branch to use the guided workflow. The first tagged release predates it.

## Demo

[![Watch OSS Showcase in Codex and Claude Code](docs/assets/showcase-demo-poster.png)](docs/assets/showcase-demo.mp4)

The recording shows Codex CLI, Claude Code CLI, and Claude Code in the Claude desktop app using the skill on the same synthetic Task Counter project. Each run proposes a showcase plan and pauses at the first decision. You can approve the current step, approve the remaining eligible steps, skip, or pause. Public publishing has its own approval.

[Reproduce the guided walkthrough](.agents/showcase/demo/README.md).

## What you can do

| Goal | Start here |
| --- | --- |
| Review an existing README or site before editing | Run `oss-showcase audit` for a read-only review. |
| Build or refresh the public presentation | Use the guided plan or the [generation workflow](references/state.md) for the README, demo, project page and discovery checks. |
| Prepare a launch | Run `oss-showcase launch` for draft posts and a channel plan. See [launch distribution](references/distribution.md). |
| Publish a reviewed site | Use `oss-showcase publish` with an approved target and follow the [GitHub Pages procedure](references/publishing.md#publish-to-github-pages). |

See [optional integrations](references/integrations.md) for the connected tools available to each stage.

## Contribute

Use [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and PRs, [architecture](docs/architecture.md) for the package layout, and [SECURITY.md](SECURITY.md) for private vulnerability reporting.
