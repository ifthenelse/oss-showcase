<img src="docs/assets/oss-showcase-lockup.svg" width="520" alt="">

# OSS Showcase

**Turn a repository into a README, a reproducible demo, and a static project site backed by evidence from the code.**

OSS Showcase is an Agent Skill for maintainers who want installation instructions, examples, and release materials to tell the same story. It starts with a plan you can review and uses a deterministic generator and validator for the static site.

[Project site](https://ifthenelse.github.io/oss-showcase/) · [Latest release](https://github.com/ifthenelse/oss-showcase/releases/latest) · [Operating modes](references/modes.md)

## Quickstart

From the folder of a project you want to showcase, run:

```sh
npx skills add ifthenelse/oss-showcase --skill oss-showcase
```

Select an agent such as Codex, Claude Code, or GitHub Copilot. Open an agent session in the target project and invoke `$oss-showcase` in Codex or `/oss-showcase` in Claude Code. In other hosts, ask the agent to use OSS Showcase for the current project. For a monorepo, specify the package. Include your site URL if you know it.

For the packaged release, download and unpack the source archive from the latest release linked above and run `sh scripts/install.sh`. The installer copies skill files to `~/.agents/skills/oss-showcase/` and creates a Claude Code link.

## Guided showcase workflow

1. [Discover the market](references/research.md). Identify the audience, compare alternatives, and use dated evidence to choose a message the project can demonstrate.
2. [Plan the brand](references/branding.md), update the README, and record a real run of the project on a safe fixture.
3. Build or update the project page. [Review copy, SEO, GEO, and AEO](references/publishing.md#discovery) against the verified quickstart and demo.
4. [Plan distribution](references/distribution.md). Pick where to post, what to show, and when to launch. Put site verification and deployment before sending traffic.
5. Review each proposed deployment or post before it goes live.

The plan appears in the client's task list when available. Before each uncovered local step, **Accept once** runs that step, **Always accept** covers the remaining planned local steps, and **Cancel** skips the step. Outstanding work goes in the target project's `docs/HANDOFF.md`. See [execution and approvals](references/execution.md#guided-workflow).

## Demo

[![Watch OSS Showcase in Codex and Claude Code](docs/assets/showcase-demo-poster.png)](docs/assets/showcase-demo.mp4)

The recording shows Codex CLI, Claude Code CLI, and Claude Code in the Claude desktop app using the skill on the same synthetic Task Counter project. Each run proposes a showcase plan and pauses at the first decision.

[Reproduce the guided walkthrough](.agents/showcase/demo/README.md).

## What you can do

| Goal | Start here |
| --- | --- |
| Review an existing README or site before editing | Run `oss-showcase audit` for a read-only review. |
| Validate the audience and positioning | Run `oss-showcase research`. See [market discovery](references/research.md). |
| Build or refresh the public presentation | Use the guided plan or the [generation workflow](references/state.md). |
| Prepare a launch | Run `oss-showcase launch` for a [channel plan, calendar, and draft posts](references/distribution.md). |
| Publish a reviewed site | Use `oss-showcase publish` with an approved target and follow the [GitHub Pages procedure](references/publishing.md#publish-to-github-pages). |

See [optional integrations](references/integrations.md) for the connected tools available to each stage.

## Contribute

Use [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and PRs, [architecture](docs/architecture.md) for the package layout, and [SECURITY.md](SECURITY.md) for private vulnerability reporting.
