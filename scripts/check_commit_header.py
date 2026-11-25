#!/usr/bin/env python3
"""Check the Conventional Commits header from Git or standard input."""

from pathlib import Path
import re
import sys


HEADER = re.compile(r"[a-zA-Z][a-zA-Z0-9-]*(?:\([^()\s]+\))?!?: \S.*")


if __name__ == "__main__":
    message = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    header, _, _ = message.partition("\n")
    if not HEADER.fullmatch(header.removesuffix("\r")):
        sys.exit("Expected a Conventional Commit header, for example: fix(validator): check public paths")
