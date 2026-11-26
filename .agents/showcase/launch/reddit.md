# Reddit launch draft

**Destination** [r/sideprojects](https://www.reddit.com/r/sideprojects/)

**Format** One text post with the `Feedback Request` flair if it is still available. Recheck community rules and prior posts before submitting.

## Title

What would you check before letting an agent rewrite your README?

## Body

I maintain OSS Showcase, an Agent Skill for people getting a GitHub repo ready to share. I’m trying to get one part right: what the agent shows you before it edits anything.

I tested it on Task Counter, a deliberately tiny Python CLI. Codex and Claude got far enough to propose a README, a demo, and a Pages site. The demo ends at the first decision. You can see which step is next and choose whether to run it.

The Pages build is a separate Python script. A validator stages only files in the reviewed manifest, and publishing needs its own approval. The handoff keeps track of steps you haven’t done.

[Here’s the run and the install command.](https://ifthenelse.github.io/oss-showcase/)

If this were your repo, would you want to see the files it plans to change or the source behind each claim first?

[Community posting guidance](https://www.reddit.com/r/sideprojects/comments/1ld5xve/my_side_project_rsideprojects_new_rules_and_an/)
