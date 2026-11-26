# Execution and approvals

## Service preflight

At the beginning of every invocation, identify only the services needed for the requested mode and target. Check whether each service has an MCP server or equivalent connector in the active host and whether it exposes the required tool. An installed connector alone is insufficient. Use the smallest read-only operation to confirm authentication, account or workspace, relevant subscription entitlement and target access. Confirm the needed scope for writes through permission metadata or a read-only probe when available. Mark write access unknown if it cannot be confirmed. Never test permissions by making a mutation. Never request or store raw tokens. Public sources need no account.

Record service, needed capability, expected and verified target, authentication and scope result, timestamp, and fallback in the handoff. Use statuses ready, public-only, unavailable, unauthorized and unverified. If MCP is missing, report it first, then use an authorized official CLI with a verified account or use public read-only sources. Do not install tools, authenticate a new account or start a paid service implicitly. Block only steps that require missing access. Recheck stale or changed scopes and confirm the account, destination and authorization immediately before external writes. For audit keep the handoff in memory or scratch.

## Guided workflow

1. Resolve the target folder or repository, ref or release, existing assets and `docs/HANDOFF.md`. Inspect read-only and present an ordered plan before acting, starting with the first step that needs work. Propose [market discovery and competitor research](research.md) first, followed by [branding and art direction](branding.md), the README glow-up, a real fixture-based demo, the project page, [SEO, GEO and AEO](publishing.md#discovery), and quality checks. Then propose the [launch strategy and calendar](distribution.md) and separate draft tasks for Product Hunt, X, and Reddit. Confirm GitHub Pages deployment before sending launch traffic. Offer each channel publication as a separate task. If research or site review is skipped, record the evidence gap and use provisional copy or dates where needed. Mark existing verified results as reusable and identify dependencies, unavailable tools and any release, license or account blockers. List planned file changes and public destinations. If only a remote repository is provided, keep the ledger in its local working copy or clone.
2. Create the [session task list](#session-tasks) from the ordered plan before the first decision. Record the plan and first decision in the handoff before starting a confirmed operation.
3. At the start of each ready step, ask [for a decision](#step-decisions) unless it is covered by the current approval. For external writes, use the separate [publication rules](#publication). Resume any still-authorized local steps after the external decision.
4. Update the task list and handoff after each attempt. Mark a step done only after its checks pass. If a prerequisite was skipped or failed, record the dependent step as blocked and continue with the next independent step. On resume, read the handoff first, check for drift, and reuse verified results. Ask before reopening a skipped step.

### Session tasks

Create one task per plan step in order, with a stable title and clear next action. Give each channel draft and publication its own task. Reuse the session's existing task IDs when updating a plan. Keep an awaiting-approval task pending. Mark it in progress when execution starts, then record the verified outcome. If the client has no skipped or blocked state, label the task accordingly and leave it unchecked. Use `docs/HANDOFF.md` to reconstruct the list across sessions.

| Client | Interactive question | Session tasks |
| --- | --- | --- |
| Codex | Use `request_user_input` or the host's equivalent choice control when the active mode exposes it and permits the question. | Use `update_plan` when available in the active mode. [Codex tool behavior](https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/plan.md) |
| Claude Code | Use `AskUserQuestion` when available. | Use `TaskCreate`, `TaskList` and `TaskUpdate`, or `TodoWrite` when that is the exposed tracker. [Claude Code tools](https://code.claude.com/docs/en/tools-reference) |
| GitHub Copilot | In VS Code use `vscode/askQuestions`. In interactive CLI sessions use the exposed `ask_user` tool if it accepts choices. | Use the client task list when exposed, such as `#todos` in VS Code. [VS Code tools](https://code.visualstudio.com/docs/agents/reference/tools-reference) · [Copilot CLI tools](https://docs.github.com/en/copilot/reference/hooks-reference#tool-names-for-hook-matching) |

Check the tools in the current session. Use a Markdown checklist in chat when the client lacks a task tracker. Use one concise text question if the client lacks a choice control or limits its use. In a noninteractive session, keep unanswered steps pending and return the handoff.

### Step decisions

Ask **Proceed with <step>?** Show what will change and where. Use the client's native single-choice prompt with these labels, localized to the user's language:

| Choice | Effect |
| --- | --- |
| **Accept once** | Run this step only. Ask again at the next uncovered step. |
| **Always accept** | Run this step and the remaining eligible local steps already shown in this run. End this scope when the run ends or the plan materially changes. |
| **Cancel** | Skip this step and ask about the next ready step. |

Wait for an explicit selection or an unambiguous user instruction. Dismissing the prompt, a timeout or no answer leaves the step pending. An explicit request to pause stops the run with unfinished tasks pending. These are workflow choices. Any tool or sandbox permission prompt follows the host's own rules. Do not change permission mode or trigger an unnecessary tool call to obtain a dialog.

## Handoff

Keep `docs/HANDOFF.md` in the target project as a concise ledger. Record the target ref, dated decisions and the latest verified state of each planned step using Pending, In progress, Done, Skipped or Blocked. Record whether the user chose step-by-step or autonomous execution, the approved scope, and any step needing a separate decision. Include the next action or blocker and link to existing drafts, artifacts, checks and remote results where relevant. Preserve unrelated content in an existing handoff. Keep credentials, private material and personal data out of the file. Exclude it from public artifacts, including deployments that serve `docs/`. If exclusion cannot be verified, pause publication.

When pausing, ending or transferring unfinished work, explicitly use `mattpocock-skills:handoff` if available. Follow its instructions to write the session handoff outside the repository in the operating system's temporary directory. Link back to `docs/HANDOFF.md` and existing artifacts instead of repeating them. If unavailable, use the project ledger as the handoff and report the fallback.

## Publication

Build and plain launch produce local artifacts. Audit is read-only. Require explicit authorization for commits, pushes, pull requests, submissions, deployments and external settings changes. For each external write, show the exact account, destination, final payload or artifact and settings that will change. Confirm the operation once all details are known. Ask for **Accept once** or **Cancel** after showing those details, using the native choice control where allowed. **Always accept** is limited to local steps. Use the host's required approval flow when applicable.

Compare the ref, files or artifact hashes and destination with the approved plan. Ask again for any material change. After an uncertain outcome, verify remote state before retrying. Record verified URLs, job IDs and submission status so a later run can reuse completed work. Follow the relevant [Pages](publishing.md#publish-to-github-pages) or [channel](distribution.md#publish-approved-channel-material) procedure.
