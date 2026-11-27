#!/bin/sh
set -eu
case "$1" in
  codex) client='Codex CLI'; invocation='$oss-showcase' ;;
  claude) client='Claude Code CLI'; invocation='Invoke the oss-showcase skill' ;;
  *) exit 2 ;;
esac
printf '%s\n%s\n\n' "$client · Recorded OSS Showcase run" 'Rizz Goblin Panic Button · Fictional example'
printf 'Invocation: %s\n\n' "$invocation"
while IFS= read -r line; do
  printf '%s\n' "$line"
  sleep 0.14
done < "$1.txt"
