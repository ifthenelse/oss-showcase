# OSS Showcase

An Agent Skill for creating and maintaining the public presentation of open source projects. It includes profile templates, a deterministic static site generator and a standalone Pages validator.

## Installation

Place this entire directory at `~/.agents/skills/oss-showcase/`. For Claude Code, link the same directory from `~/.claude/skills/oss-showcase`. From the unpacked directory, run:

```sh
sh scripts/install.sh
```

Run the installer only when both destinations are available for a new install. It refuses to replace an existing copy or link. Install dependencies separately only when a run requires them.

## Invocation

Open a session in the target repository. In Codex, select the skill with `$oss-showcase`. In Claude Code, use `/oss-showcase`.

| Mode | Codex | Claude Code |
| --- | --- | --- |
| Create | `$oss-showcase init` | `/oss-showcase init` |
| Update | `$oss-showcase refresh` | `/oss-showcase refresh` |
| Inspect | `$oss-showcase audit` | `/oss-showcase audit` |
| Release | `$oss-showcase prepare-release v1.2.0` | `/oss-showcase prepare-release v1.2.0` |
| Draft launch | `$oss-showcase launch` | `/oss-showcase launch` |

Supply a package path in a monorepo and a public site URL if known. The skill resolves supporting skills at the relevant stage and reports fallbacks. See the [main workflow](SKILL.md) and [generation reference](references/state.md) for direct script commands.

[Codex skill locations](https://developers.openai.com/api/reference/cli) · [Claude Code skills](https://code.claude.com/docs/en/skills)

For an app or CLI, plain launch prepares package requests. To submit eligible requests for a specific release and selected channels, use `$oss-showcase launch --submit-packages v1.2.0 homebrew,winget` in Codex or `/oss-showcase launch --submit-packages v1.2.0 homebrew,winget` in Claude Code. See [package distribution](references/packages.md).

## Optional integrations

[GitHub, Ahrefs, Product Hunt and Cloudflare](references/integrations.md) support research, discovery, deployment checks and [launch planning](references/distribution.md) when the active host exposes the relevant tools.

## Checks

Run `python3 scripts/test_showcase.py` for fixture coverage across all six profiles. The tests exercise repeat generation, read-only planning, stage fingerprints, protection for existing files, shared media references, base paths and public artifact scope. Recording tools and hosted deployment are exercised separately in the target project.

## Portable execution

Install this repository with the skills CLI:

```sh
npx skills add ifthenelse/oss-showcase --skill oss-showcase
```

Select the installed agents interactively, including Codex, Claude Code or GitHub Copilot. Other skills CLI targets can use the same Agent Skills directory and supporting files. Capabilities depend on the active client, its tools and credentials. In a client without a dedicated invocation shortcut, write "Use the oss-showcase skill in research mode for this repository."

| Mode | Example prompt |
| --- | --- |
| Research | Use oss-showcase research for this project and shortlist domains. |
| Build | Use oss-showcase build to generate the assets and documentation locally. |
| Plan | Use oss-showcase plan for v1.2.0 and draft the launch and package requests. |
| Publish | Use oss-showcase publish to execute the approved v1.2.0 plan for the explicitly authorized destinations. |

See the [execution contract](references/execution.md) and [research procedure](references/research.md).
