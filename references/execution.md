# Execution and human checkpoints

## Service preflight

At the beginning of every invocation, identify only the services needed for the requested mode and target. Check whether each service has an MCP server or equivalent connector in the active host and whether it exposes the required tool. An installed connector alone is insufficient. Use the smallest read-only operation to confirm authentication, account or workspace, relevant subscription entitlement and target access. Confirm the needed scope for writes through permission metadata or a read-only probe when available. Mark write access unknown if it cannot be confirmed. Never test permissions by making a mutation. Never request or store raw tokens. Public sources need no account.

Record service, needed capability, expected and verified target, authentication and scope result, timestamp, and fallback in the handoff. Use statuses ready, public-only, unavailable, unauthorized and unverified. If MCP is missing, report it first, then use an authorized official CLI with a verified account or use public read-only sources. Do not install tools, authenticate a new account or start a paid service implicitly. Block only steps that require missing access. Recheck stale or changed scopes and confirm the account, destination and authorization immediately before external writes. For audit keep the handoff in memory or scratch.

## Separate modes

| Mode | Scope | Handoff |
| --- | --- | --- |
| research | Market, positioning and domain candidates | Research memo and decisions |
| build (init, refresh) | Assets, demos, README, site, local checks | Artifact paths, fingerprints and results |
| plan (launch) | Draft release, publication and channel plan, package requests | Exact targets, release ref, approved artifact hashes and validation |
| publish | Execute an explicitly approved plan for named targets only | URLs, job IDs, submission and acceptance status |

Keep legacy prepare-release and audit behavior. Keep the prior explicitly scoped package submission option for launch; treat it as authorization for that separate package request step only. Plain launch and build have no external writes. Before publishing compare release, files and destinations against the approved plan. Reuse verified work, and route changed content back for review. Authorization applies only to listed actions and targets. Stop affected writes on drift or uncertain results, confirm remote state before retry, and record successful actions so a rerun skips them.

## Keep model work small

Read existing facts, fingerprints and the handoff first. Open only the reference and supporting skill needed for the current stage. If the inputs and outputs match, skip generation. Use local scripts for hashing, rendering and tests. Save compact evidence summaries and artifact paths instead of replaying raw output. Group parallel read-only probes where possible. Batch consequential choices such as name, domain and launch scope into one review. Reuse prior decisions and explicit authorization when still current. Keep approved assets and plans portable across sessions as Markdown or JSON. Never require a host-specific orchestration feature, background agent or CI model call.
