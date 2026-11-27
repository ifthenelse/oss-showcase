# OSS Showcase launch plan

Reviewed on 2026-11-26 (Europe/Rome). **Decision: hold the public announcement until the readiness checks pass.** Keep the schedule relative until the maintainer confirms those checks and availability.

## Audience and angle

Lead with **“Your code runs. Show people how.”** The audience is solo maintainers and small teams with a working GitHub project. Show them an agent planning a README, a demo, and a Pages site, then pausing for review. The recording shows the first decision. The generator and its validator are separate evidence for the site build. See the [market and competitor memo](../research.md), the [reproducible walkthrough](../demo/README.md), and the [public demo](https://ifthenelse.github.io/oss-showcase/#demo).

## Readiness before choosing a date

| Check | State | Evidence or next action |
| --- | --- | --- |
| License and contribution terms | Blocked | GitHub reports no declared license. The maintainer must choose and approve a license, verify the rights to included assets and dependencies, and document applicable contribution terms before announcing the project as open source. |
| Name and launch accounts | Unverified | Confirm target markets and record the outcome of a name and similar-name review. Confirm the domains and handles actually needed for this launch and the accounts that control them. |
| Clean install and first use | Partial | The documented skills CLI command installed in a temporary Git project and home. The tagged archive installer and installed-skill smoke test also passed. Give a new reader the README and a clean sample project, record every point where they need help, and verify that the skill loads and proposes its first decision in the intended client. |
| Pages and share preview | Blocked | The public page responds, but the revised HTML, CSS, and social card still await deployment. Obtain approval for the reviewed artifact, then check HTTPS, canonical URL, sitemap, share preview, demo playback, and quickstart links on the live site. |
| Distribution and proof | Verified | The [latest release](https://github.com/ifthenelse/oss-showcase/releases/latest) and [quickstart](../../../README.md#quickstart) are available. The current footage covers Codex CLI, Claude Code CLI, and the Claude desktop app. Keep claims within that scope. A Codex Desktop clip is an optional improvement. |
| Repository hygiene | Unverified | Review public Git history and media for accidentally published secrets or internal data. Record the scanned refs, tooling, and any remaining coverage gaps without exposing findings. |
| Feedback and security | Partial | GitHub Issues and private vulnerability reporting are enabled. [Contributor guidance](../../../CONTRIBUTING.md) and [security policy](../../../SECURITY.md) exist. Confirm someone is watching both channels on launch day and the next day. |
| Channel eligibility and capacity | Unverified | Recheck maker role, duplicate eligibility, account access and current rules. Confirm who can post, reply and handle issues, and how many hours they can cover. |

## Channel sequence and launch day

Use one announcement window with Product Hunt as the proposed anchor. Use Reddit for a focused feedback question if the community rules and account history support it. Use X to share the actual demo and amplify the anchor if maintainer capacity permits. Drop secondary posts before reducing coverage of the main thread. Confirm final copy, account and timing separately for each publication.

| When | Action | Proposed owner |
| --- | --- | --- |
| Before scheduling | Close readiness checks, verify the deployed landing, and agree on the anchor, time zone and hours of coverage. | Maintainer |
| Before the anchor, only if eligible | Post the [Reddit feedback request](reddit.md). Address install or comprehension problems before the announcement. | Reddit account holder |
| Day before | Capture the baseline below. Reopen every public link and verify the exact listing preview and media. | Launch lead |
| At launch | Confirm the [Product Hunt listing](product-hunt/README.md) is visible, save its permalink, and post the prepared maker comment. | Confirmed maker |
| First few hours | Stay in the anchor thread. Log install and comprehension issues, assign fixes, and point security reports to the private reporting form. Share the [X demo post](x.md) when coverage and account access are confirmed. | Maker, support owner, and X account holder |
| Next day | Reply to remaining questions and check whether issues were resolved or assigned. | Named support owner |

If no one can cover the anchor thread and feedback channels, reschedule or reduce scope. A follow-up should contain an actual fix, result, or useful answer. [Product Hunt scheduling](https://help.producthunt.com/en/articles/17734355-3-set-your-goals-and-pick-your-launch-date) · [Reddit posting guidance](https://www.reddit.com/r/sideprojects/comments/1ld5xve/my_side_project_rsideprojects_new_rules_and_an/) · [X media limits](https://help.x.com/en/using-x/x-videos)

## Measurement

The goal is to learn whether a maintainer can get from installation to a first useful showcase. Record the measurement time, timezone, source, and window with every snapshot. Save post permalinks and keep any account-level reports private.

| When | Record | Decision |
| --- | --- | --- |
| Day before | GitHub stars, issues, unique visitors and cloners, available install counts and site referrals. Confirm which metrics are accessible and agree on a target relative to the baseline or an explicit goal when there is no usable baseline. | Set the comparison window before posting. |
| Day 1 | Anchor and amplifier reach, referrals, and install or quickstart issues. | Fix obvious friction in the first-run path. |
| Day 7 | Install or clone signals, substantive replies, and independently reported first runs. | Identify the step where people get stuck. |
| Day 30 | Independently reported completed showcases, repeat use, and meaningful issues or contributions. | Choose a product or onboarding improvement before planning another announcement. |

Keep counts of installs, reported first runs, and completed showcases separate. Mark unavailable metrics as unmeasured. Read search and AI discovery data separately when verified access exists.

This readiness and measurement sequence draws on the [OSS Launch checklist](https://github.com/samber/developer-relations-skills/blob/main/skills/oss-launch/references/readiness-checklist.md), [launch-day runbook](https://github.com/samber/developer-relations-skills/blob/main/skills/oss-launch/references/launch-day-runbook.md), and [measurement plan](https://github.com/samber/developer-relations-skills/blob/main/skills/oss-launch/references/measurement-plan.md).
