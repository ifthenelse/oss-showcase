# Architecture

OSS Showcase helps open source maintainers create and maintain a README, demo, static site and launch drafts using evidence from the target repository. The installed skill coordinates the work. Its Python scripts handle deterministic generation, state and validation.

- `SKILL.md` and `references/` describe how the host agent inspects a project, selects a mode and uses optional integrations.
- `scripts/showcase.py` reads the selected profile and shared facts, applies templates and tracks generated files and stage fingerprints. It vendors the standalone validator into the target project.
- `scripts/validate.py` checks the generated site and stages the public manifest and its files for Pages. `templates/pages.yml` is the deployment template for a target project.
- Templates, CLI behavior, shared facts consumed by the generator and generated public paths form the user-facing contract for releases.

See [contributing checks](../CONTRIBUTING.md#verification), the [threat model](security/threat-model.md) and [release operations](deployment.md).
