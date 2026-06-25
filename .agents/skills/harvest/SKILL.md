---
name: harvest
description: Produce a digest of recent garden activity — entries sown, fertilized, tended, pruned, or grafted over a given period — for review or changelog purposes. Use when the user says "harvest the garden", "what's changed recently", or asks for a summary/digest of recent garden activity.
metadata:
  interactive: no
---

# Harvest

Use this skill to gather a digest of what's happened in the garden recently — new entries, expansions, repairs, merges, splits — without re-scanning the whole repository the way [tend](../tend/SKILL.md) or [prune](../prune/SKILL.md) would.

Do NOT use this skill to make any changes to the garden — it only reports. Do NOT use it as a substitute for [tend](../tend/SKILL.md) — harvest summarizes *what changed*, not *what's currently broken*.

**Input**: OPTIONAL — a time window or commit range (eg. "harvest the last 2 weeks", "harvest since v1.4"). Defaults to commits since the last harvest digest was produced, or the last 30 days if no prior digest exists.

**Output**: A digest, grouped by activity type (sown / fertilized / tended / pruned / grafted / other), printed to the chat. If the user asks for it to be saved, write it to a dated entry, newest first, rather than overwriting prior digests.

## Instructions

1.  **Determine the window.**

    If the user gave a range or date, use it. Otherwise, find the most recent digest file (if any) and use commits since its date; if none exists, default to the last 30 days.

2.  **Pull the commit log for the window.**

    ```sh
    git log --since="<window-start>" --name-status --pretty=format:'%h %s'
    ```

    This repo's commit messages are prefixed by type (eg. `add:`, `edit:`, `maintenance:`) — use these prefixes as a first signal, but verify against the actual file changes, since a commit message doesn't always say which garden skill produced it.

3.  **Classify each change.**

    For each commit, inspect the files touched and classify the activity:

    - **Sown**: a new `.adoc` page added under `pages/`, plus a corresponding `index.adoc` addition.
    - **Fertilized**: an existing page's content grew substantially (significant line additions to a file that already existed).
    - **Tended**: fixes to `xref:` targets, pseudo-links, or index listings with no new concept introduced.
    - **Pruned**: a page deleted along with repointed references elsewhere.
    - **Grafted**: one page's content shrank while one or more new pages appeared in the same change, with cross-links between them.
    - **Other**: anything that doesn't fit the above (eg. CI config, README changes) — list briefly, don't force a category.

4.  **Build the digest.**

    Group entries by category. For each entry, give the page title, a one-line description of what changed, and the commit short-hash. Keep descriptions terse — this is a scan-able digest, not a narrative.

5.  **Present the digest.**

    Print it in the chat by default. Only write it to a file if the user asks — and if so, append a new dated section rather than overwriting any existing digest history.

## Rules

-   **Classify by actual file changes, not commit message alone.** Commit prefixes are a hint, not ground truth — a commit titled `edit: ...` might really be a fertilize (substantial growth) or a tend (a one-line link fix); check the diff.

-   **Keep it a report, not an action.** If the digest surfaces something that looks broken or undone (eg. a half-finished graft, a page added but never linked from the index), name it as a finding for the user to send to [tend](../tend/SKILL.md) — don't fix it inline.

-   **Default to the chat, not a file.** Most uses of this skill are a quick check-in, not a permanent changelog entry — only persist to disk on explicit request.

-   **Committing is out of scope.** Even when the user asks for the digest to be saved to a file, this skill only writes that file — it never stages, commits, or pushes it.

## Success criteria

- **Every commit in the window is classified** into one of the categories, with no commit silently dropped.

- **The digest is grouped by activity type**, not presented as a flat chronological list.

- **Classification is checked against the actual diff**, not assumed from the commit message prefix alone.

- **No garden file was modified** by running this skill, unless the user explicitly asked for the digest to be saved.
