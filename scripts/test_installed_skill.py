#!/usr/bin/env python3
"""Check the packaged skill and run its offline showcase walkthrough."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

PACKAGE = Path(__file__).resolve().parent.parent


def main():
    with tempfile.TemporaryDirectory() as temporary:
        home = Path(temporary).resolve()
        env = {**os.environ, "HOME": str(home), "PYTHONDONTWRITEBYTECODE": "1"}
        subprocess.run(["sh", str(PACKAGE / "scripts/install.sh")], env=env, check=True)
        installed = home / ".agents/skills/oss-showcase"
        claude = home / ".claude/skills/oss-showcase"
        if claude.resolve() != installed:
            raise SystemExit("The Claude Code install does not resolve to the packaged skill.")

        entry = installed / "SKILL.md"
        references = sorted((installed / "references").glob("*.md"))
        for document in [entry, *references]:
            links = re.findall(r"\]\(([^)\s]+)\)", document.read_text(encoding="utf-8"))
            for link in links:
                url = urlsplit(link)
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (document.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(installed) or not target.is_file():
                    raise SystemExit(f"{document.relative_to(installed)}: broken bundled link {link}")

        env["SHOWCASE_SOURCE"] = str(installed)
        subprocess.run(
            ["sh", str(PACKAGE / ".agents/showcase/demo/run.sh")],
            env=env,
            check=True,
        )


if __name__ == "__main__":
    main()
