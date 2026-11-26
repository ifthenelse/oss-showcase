# Operating modes

Invoke `$oss-showcase [mode]` in Codex or `/oss-showcase [mode]` in Claude Code. Use the guided default for a ready product and audit for an explicitly read-only review. Stage numbers refer to [stage routing](stages.md).

| Mode | Scope |
| --- | --- |
| Guided (default) | Follow the [guided workflow](execution.md#guided-workflow). Plan the showcase, execute the approved steps and track the remainder. |
| `research` | Produce the [market discovery and competitor memo](research.md) and positioning. Include a domain shortlist when it is in scope. |
| `build` or `init` | For a new showcase, run stages 1–9 using the [generation workflow](state.md). Add stage 10 if launch drafts are requested. Build writes locally. |
| `refresh` | Check [stage fingerprints](state.md#refresh-plan) and preview only stale or missing showcase work. Keep existing project behavior and hand-maintained content. |
| `audit` | Inspect existing surfaces using relevant parts of stages 1 and 4–9. Run read-only checks, use scratch for diagnostics and report severity, evidence, affected paths and fixes. |
| `prepare-release <ref>` | Verify the requested tag or ref and changelog. Inspect it in a scratch checkout if it differs from the working tree. Update release-specific showcase claims and examples. Keep working install commands and evergreen release links. Refresh the demo if its inputs or displayed version changed. Run affected checks and draft release notes when needed. |
| `plan [ref]` or `launch` | Review current market research, positioning, landing copy and discovery readiness first. Draft the [channel plan and calendar](distribution.md), tracker and posts in `.agents/showcase/launch/` or the project's existing planning location. Include eligible [package drafts](packages.md) for apps and CLIs. |
| `publish` | Execute the [approved plan](execution.md#publication) for the named destinations. Use the [Pages procedure](publishing.md#publish-to-github-pages) or [channel publication](distribution.md#publish-approved-channel-material) for the selected step. |

For apps and CLIs, `launch --submit-packages <release> <channels>` authorizes only the named [package requests or PRs](packages.md), such as `launch --submit-packages v1.2.0 homebrew,winget`. Review and approval for other distribution remain separate.

## Existing repositories

Scope monorepo facts and fingerprints to the selected package. Preserve existing public documentation, licenses, links and deployment workflows. The generator targets a single homepage under `docs/`. Reconcile with an existing site or stage a separately scoped showcase with matching asset and publish paths.
