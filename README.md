# OSS Showcase

An Agent Skill that turns repository evidence into a README, a reproducible demo, a static project site and launch materials. It includes a deterministic generator and a standalone GitHub Pages validator.

## Install

Select your agent when prompted. The skills CLI supports Codex, Claude Code, GitHub Copilot and other hosts.

```sh
npx skills add ifthenelse/oss-showcase --skill oss-showcase
```

From an unpacked source archive, `sh scripts/install.sh` is an alternative. It installs the skill under `~/.agents/skills/oss-showcase/` and links it from `~/.claude/skills/oss-showcase`. The installer preserves existing destinations.

## Run a showcase

Open the product folder or repository and invoke `$oss-showcase` in Codex or `/oss-showcase` in Claude Code. Supply a package path for a monorepo and a site URL if known. In other hosts, ask the agent to use OSS Showcase for that project.

By default, the skill presents a plan first. Choose **Proceed** for one step, **Proceed with this and remaining steps** for scoped autonomy, or **Skip** or **Pause**. It tracks outstanding work in the target project's `docs/HANDOFF.md`.

- [Operating modes](references/modes.md) lists explicit commands, including read-only audits and launch drafts.
- [Guided workflow](references/execution.md#guided-workflow) explains approvals, autonomy and resuming work.
- [Generation](references/state.md), [Pages publication](references/publishing.md#publish-to-github-pages) and [launch distribution](references/distribution.md) cover the main workflows.
- [Optional integrations](references/integrations.md) lists supported capabilities and fallbacks across hosts.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and the PR workflow, [architecture](docs/architecture.md) for the package layout and [SECURITY.md](SECURITY.md) for private vulnerability reporting.
