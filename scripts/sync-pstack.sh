#!/usr/bin/env bash
set -euo pipefail

# Rsync pstack from $PSTACK_DIR into this repo's local plugin copy,
# commit on lauren, optionally merge into main.

if [[ -z "${PSTACK_DIR:-}" ]]; then
  echo "error: PSTACK_DIR is not set" >&2
  exit 1
fi

if [[ ! -d "$PSTACK_DIR" ]]; then
  echo "error: PSTACK_DIR is not a directory: $PSTACK_DIR" >&2
  exit 1
fi

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$REPO/plugins/local/pstack"
BRANCH="lauren"

if [[ ! -d "$DEST/.git" ]]; then
  echo "error: not a git repo: $DEST" >&2
  exit 1
fi

if [[ -n "$(git -C "$DEST" status --porcelain)" ]]; then
  echo "error: target has uncommitted changes:" >&2
  git -C "$DEST" status --short >&2
  exit 1
fi

git -C "$DEST" checkout "$BRANCH"

rsync -a --delete \
  --exclude '.git/' \
  --exclude '.DS_Store' \
  "${PSTACK_DIR%/}/" \
  "${DEST}/"

msg="$(git -C "${PSTACK_DIR%/}" log -1 --format='%h - %s')"
echo "$msg"

if [[ -z "$(git -C "$DEST" status --porcelain)" ]]; then
  echo "no changes to commit"
else
  git -C "$DEST" add -A
  git -C "$DEST" commit -m "$msg"
fi

printf "Merge %s into main? [y/N] " "$BRANCH" > /dev/tty
read -r answer < /dev/tty
case "$answer" in
  y|Y|yes|YES)
    if git -C "$DEST" show-ref --verify --quiet refs/heads/main; then
      git -C "$DEST" checkout main
    elif git -C "$DEST" show-ref --verify --quiet refs/remotes/origin/main; then
      git -C "$DEST" checkout -B main origin/main
    else
      echo "error: main branch not found locally or on origin" >&2
      exit 1
    fi
    git -C "$DEST" merge -X ours "$BRANCH"
    echo "merged $BRANCH into main"
    ;;
  *)
    echo "skipped merge; left on $BRANCH"
    ;;
esac
