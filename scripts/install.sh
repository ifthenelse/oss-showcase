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

cd "$source_dir"
for directory in agents docs docs/assets references scripts templates templates/profiles; do
    if [ -L "$directory" ] || [ ! -d "$directory" ]; then
        printf 'Expected a real resource directory: %s\n' "$directory" >&2
        exit 1
    fi
done

set -- LICENSE README.md agents/openai.yaml docs/assets/oss-showcase-lockup.svg \
    docs/assets/otto-s.svg docs/assets/otto-s-favicon.svg references/*.md scripts/*.py scripts/install.sh scripts/verify \
    templates/*.cjs templates/*.css templates/*.html templates/*.in templates/*.json \
    templates/*.md templates/*.tape templates/*.yml templates/profiles/*.json SKILL.md
for file do
    if [ -L "$file" ] || [ ! -f "$file" ]; then
        printf 'Expected a regular skill file: %s\n' "$file" >&2
        exit 1
    fi
done

mkdir -p "$(dirname "$codex_dir")" "$(dirname "$claude_dir")"
mkdir "$codex_dir"
mkdir "$codex_dir/references" "$codex_dir/scripts" "$codex_dir/templates"
mkdir "$codex_dir/templates/profiles" "$codex_dir/agents" "$codex_dir/docs"
mkdir "$codex_dir/docs/assets"
for file do
    cp "$file" "$codex_dir/$file"
done
ln -s "$codex_dir" "$claude_dir"
printf '%s\n' "Installed at $codex_dir"
