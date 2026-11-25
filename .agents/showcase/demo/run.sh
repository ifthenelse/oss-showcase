#!/bin/sh
set -eu

demo_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
source_dir=${SHOWCASE_SOURCE:-"$demo_dir/../../.."}
scratch=$(mktemp -d)
trap 'rm -rf -- "$scratch"' EXIT
mkdir -p "$scratch/home" "$scratch/project/.agents" "$scratch/project/docs"
HOME=$scratch/home
PYTHONDONTWRITEBYTECODE=1
export HOME PYTHONDONTWRITEBYTECODE

cd "$scratch/project"
cp "$demo_dir/task_counter.py" .
cp "$demo_dir/product-facts.json" .agents/product-facts.json
printf 'Private fixture notes\n' > docs/internal-notes.txt

printf 'Example: python3 task_counter.py build release\n'
result=$(python3 task_counter.py build release)
test "$result" = "Tasks: 2"
printf '%s\n\n' "$result"
python3 "$source_dir/scripts/showcase.py" apply
python3 .agents/showcase/validate.py --stage public

test -f README.md
test -f public/index.html
test ! -e public/internal-notes.txt
printf '\nPublic artifact:\n'
(cd public && find . -type f | LC_ALL=C sort)
