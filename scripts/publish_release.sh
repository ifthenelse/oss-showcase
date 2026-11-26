#!/usr/bin/env bash
set -euo pipefail

version=$(<version.txt)
if [[ ! "$version" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]]; then
  echo 'version.txt must contain a stable SemVer version.' >&2
  exit 1
fi
tag="v$version"
ref="refs/tags/$tag"

notes=$(mktemp)
trap 'rm -f "$notes"' EXIT
if ! awk -v version="$version" '
  /^## / {
    if (section) exit
    section = ($2 == version)
    next
  }
  section { print; if (NF) content = 1 }
  END { if (!content) exit 1 }
' CHANGELOG.md > "$notes"; then
  echo "CHANGELOG.md must have release notes for $version." >&2
  exit 1
fi

tag_refs=$(git ls-remote --tags "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY.git" "$ref" "$ref^{}")
tag_commit=$(awk -v peeled="$ref^{}" '
  $2 == peeled { annotated = $1 }
  NR == 1 { direct = $1 }
  END { print annotated ? annotated : direct }
' <<< "$tag_refs")
if [[ -z "$tag_commit" ]]; then
  gh api --method POST "repos/$GITHUB_REPOSITORY/git/refs" -f "ref=$ref" -f "sha=$GITHUB_SHA" >/dev/null
elif [[ "$tag_commit" != "$GITHUB_SHA" ]]; then
  echo "$tag already points to a different commit ($tag_commit)." >&2
  exit 1
fi

gh release create "$tag" --repo "$GITHUB_REPOSITORY" --verify-tag --title "$tag" --notes-file "$notes"
