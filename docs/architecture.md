# Architecture

OSS Showcase helps maintainers get a working repository ready to share. The installed skill coordinates market research, branding, public assets and launch planning. Its Python scripts handle deterministic generation, state and validation.

- `SKILL.md` and `references/` describe how the host agent inspects a project, selects a mode and uses optional integrations.
- `scripts/showcase.py` reads the selected profile and shared facts, applies templates and tracks generated files and stage fingerprints. It vendors the standalone validator into the target project.
- `scripts/validate.py` checks the generated site and stages the public manifest and its files for Pages. `templates/pages.yml` is the deployment template for a target project.
- Templates, CLI behavior, shared facts consumed by the generator and generated public paths form the user-facing contract for releases.

## Project artifacts

| Artifact | Role |
| --- | --- |
| `.agents/showcase/research.md` | Dated audience evidence, alternatives, and observed or unmeasured demand. It informs brand and launch decisions. |
| `.agents/product-marketing.md` and `.agents/product-facts.json` | Positioning and evidence-backed facts. The generator consumes the JSON and checks its source references. |
| `.agents/showcase/public.json` | The allowlist and hashes for reviewed Pages files. The validator stages the matching public files. |
| `.agents/showcase/launch/` and `docs/HANDOFF.md` | Channel choices, calendar, drafts, and the approval and progress record. Keep these out of the Pages artifact. |

[Stage fingerprints](../references/state.md#refresh-plan) detect reviewed input changes. A changed research memo prompts brand and launch review. A changed landing prompts launch review. The agent resolves those decisions through the [guided workflow](../references/execution.md#guided-workflow).

See [contributing checks](../CONTRIBUTING.md#verification), the [threat model](security/threat-model.md) and [release operations](deployment.md).
