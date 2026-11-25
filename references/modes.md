# Operating modes

| Mode | Scope and stage order |
| --- | --- |
| init | Run 1 through 9. Inventory existing deliverables first. Create shared context, safe demo, README, static site, social image, metadata, sitemap, validation and draft Pages workflow. Stage 10 runs only when launch material is requested. |
| refresh | Calculate stage status. Reopen stages whose inputs or declared outputs changed. Use field-level comparisons and preserve existing decisions and unchanged media. Validate affected surfaces. |
| audit | Inventory and inspect existing surfaces using relevant parts of 1 and 4 through 9. Run validators read-only. Pass audit-only constraints to each dependency. Keep browser recordings, diagnostics and baselines in temporary storage. End with severity, evidence, affected path and remediation. |
| prepare-release | Resolve the requested release with manifests, tag/ref and changelog. If the ref differs from the working tree, inspect or test it in an isolated checkout. Update verified versions, install commands, compatibility, release links and examples. Refresh demo only when its inputs or displayed version changed. Run affected gates, draft release notes if applicable and report the tested ref. |
| launch | Run readiness checks and stage 10. Use the latest verified facts, approved media and canonical links. Draft a channel schedule, directory shortlist and submission tracker, tailored outreach and posts in `.agents/showcase/launch/` or the existing release-planning location. Keep status at draft. |

With no explicit mode, infer from the desired outcome. Use audit for a request framed as review. Complete independent stages when a creative decision, missing tooling, unavailable evidence or a public URL blocks another stage. Report unresolved dependencies and leave the affected stage unrecorded.

## Existing repositories

Respect existing public documentation, licenses, links and deployment workflows. Scope monorepo facts and fingerprints to the selected package. Put the showcase at the repo root under `docs/` by default. If the destination already serves a site, agree with existing architecture and reconcile manually, or use a dedicated showcase subdirectory within `docs/` with matching asset references and publish paths. The starter generator targets a single homepage in `docs/`. Never create a competing workflow for a site already deployed by the repo.
