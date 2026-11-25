#!/bin/sh
set -eu

source_dir=$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)
codex_dir="$HOME/.agents/skills/oss-showcase"
claude_dir="$HOME/.claude/skills/oss-showcase"

if [ -e "$codex_dir" ] || [ -L "$codex_dir" ] || [ -e "$claude_dir" ] || [ -L "$claude_dir" ]; then
    if [ -f "$codex_dir/SKILL.md" ] && [ "$(readlink "$claude_dir" || true)" = "$codex_dir" ]; then
        printf '%s\n' "Already installed at $codex_dir"
        exit 0
    fi
    printf '%s\n' 'An install destination already exists. Inspect it before replacing it.' >&2
    exit 1
fi

mkdir -p "$(dirname "$codex_dir")" "$(dirname "$claude_dir")"
mkdir "$codex_dir"
cp -R "$source_dir"/. "$codex_dir"/
ln -s "$codex_dir" "$claude_dir"
printf '%s\n' "Installed at $codex_dir"
