# OSS Showcase on Rizz Goblin Panic Button

Rizz Goblin Panic Button is a fictional Python CLI used to demonstrate the OSS Showcase skill. The CLI turns synthetic desk-chaos signals into a goblin alert. The GIFs replay the final text from real agent sessions and stop at the first decision in guided mode.

| Client | Capture |
| --- | --- |
| Codex CLI | [Recorded guided plan](../../../../docs/assets/codex-goblin.gif) |
| Claude Code CLI | [Recorded guided plan](../../../../docs/assets/claude-goblin.gif) |

## Repeat the walkthrough

Copy the [fixture instructions](FIXTURE.md) as `README.md` and the two Python files into a disposable Git repository. Run `python3 -m unittest` and the fixture quickstart. In an isolated client session with OSS Showcase installed, use read-only or plan mode with editing tools disabled.

Ask the client to load OSS Showcase and use the current synthetic project in guided mode. Ask it to identify the fixture, quote the quickstart from the README, outline the showcase, and pause at the first approval. Keep the initial run local and leave that decision unanswered.

The Codex response is its final agent message. The Claude Code response is its final result after invoking the skill. The text files contain those responses with terminal line wrapping. The VHS tapes replay these responses with client and fixture labels. From this directory, run `vhs codex.tape` and `vhs claude.tape` to reproduce the GIFs. The public captures contain neither raw agent events nor tool diagnostics.
