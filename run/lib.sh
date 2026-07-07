#!/usr/bin/env bash

#
# Shared helpers for scripts in run/ that let `pi` edit the garden headlessly and open a PR
# per change-set. Source this from a run/ script; don't execute it directly.
#

: "${BASE_BRANCH:=latest/dev}"
: "${MODEL:=anthropic/claude-sonnet}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT" || exit

garden::check_clean() {
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "Working tree is not clean; commit or stash first." >&2
    exit 1
  fi
}

garden::sync_base() {
  git checkout "$BASE_BRANCH"
  git pull --ff-only
}

# garden::open_branch <slug> — checks out temp/<slug>-<timestamp> off BASE_BRANCH.
garden::open_branch() {
  local branch="temp/$1-$(date +%s)"
  git checkout -b "$branch" "$BASE_BRANCH" >&2
  echo "$branch"
}

# garden::commit_push_pr <commit-message> <pr-title> <pr-body> [paths...]
# With no paths, stages everything (for whole-repo passes). Returns 1 and discards the
# branch if there's nothing to commit.
garden::commit_push_pr() {
  local msg="$1" title="$2" body="$3"; shift 3
  local paths=("$@")
  local branch; branch="$(git branch --show-current)"

  if [[ ${#paths[@]} -eq 0 ]]; then
    if git diff --quiet && git diff --cached --quiet; then
      echo "No changes; skipping."
      git checkout "$BASE_BRANCH"; git branch -D "$branch"
      return 1
    fi
    git add -A
  else
    if git diff --quiet -- "${paths[@]}"; then
      echo "No changes; skipping."
      git checkout "$BASE_BRANCH"; git branch -D "$branch"
      return 1
    fi
    git add -- "${paths[@]}"
  fi

  git commit -m "$msg"
  git push -u origin "$branch"
  gh pr create --base "$BASE_BRANCH" --head "$branch" --title "$title" --body "$body"
  git checkout "$BASE_BRANCH"
}
