# Record the guided walkthrough

Create a disposable Git repository on `main`, copy [task_counter.py](task_counter.py) to its root, and add a README that identifies it as a synthetic CLI. Install OSS Showcase into that project using the [installation instructions](../../../README.md#quickstart). To record a development commit, use a checkout of that commit as the installation source.

Open the project in the client being recorded. Use read-only permissions or plan mode. In Codex, start the prompt with `$oss-showcase`. In Claude Code, select `/oss-showcase`. Ask for a guided plan for the synthetic Task Counter, the first confirmation, and a pause. Request no file changes or remote probes.

Record the prompt and confirm that each client loads the skill, identifies the fixture, and offers the first decision. Leave the decision unanswered. The current video contains real Codex CLI and Claude Code CLI executions and a review of the completed plan in the Claude desktop app. The terminal clips filter the clients' JSON output to keep the response visible without exposing raw traces. Versions used for the terminal clips were Codex CLI 0.172.0, Claude Code 2.1.326, and VHS 0.12.1.

Use `sh run.sh` from this directory for the independent generator smoke test.
