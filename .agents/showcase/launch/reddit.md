# Reddit launch draft

**Destination** [r/sideprojects](https://www.reddit.com/r/sideprojects/)

**Format** One text post with the `Feedback Request` flair if it is still available. Verify the current rules and whether the account has already posted this project before submitting.

## Title

I built an Agent Skill that plans a README and demo before editing the repo

## Body

I maintain OSS Showcase, an Agent Skill for the last stretch of shipping a project. I'm looking for feedback on the first approval screen: is there enough information there to decide what the agent should do?

The workflow reads the project and proposes a plan for the README, a demo, and a static GitHub Pages site. Each public claim can point to a file, example, or test in the repo. A Python script builds the site, and a separate validator stages only the reviewed files. The agent keeps unfinished work in a handoff so you can resume later.

The demo uses a synthetic Python CLI that counts task arguments. It shows the point where Codex or Claude has read the fixture and asks before editing the README. Publishing has a separate approval.

Try it from a project folder with `npx skills add ifthenelse/oss-showcase --skill oss-showcase`. [Project page and demo](https://ifthenelse.github.io/oss-showcase/)

Would you want to review the source evidence before the first edit, or is seeing the planned file changes enough?

[Community posting guidance](https://www.reddit.com/r/sideprojects/comments/1ld5xve/my_side_project_rsideprojects_new_rules_and_an/)
