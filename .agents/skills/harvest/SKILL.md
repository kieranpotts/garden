---
name: harvest
description: >-
  Produce a digest of recent garden activity — entries sown, fertilized, tended,
  pruned, grafted, entwined, weeded, or uprooted over a given period — for
  review or changelog purposes. Use when the user says "harvest the garden",
  "what's changed recently", or asks for a summary/digest of recent garden
  activity.
compatibility: requires Bash (git log), Write
license: CC0-1.0
---

# Harvest

Produce a digest of recent garden activity — entries sown, fertilized,
tended, pruned, grafted, entwined, weeded, or uprooted over a given period —
for review or changelog purposes. The digest is grouped by activity type and
printed to the chat by default.

## Input

OPTIONAL — a time window or commit range (eg. "harvest the last 2 weeks",
"harvest since v1.4"). Defaults to commits since the last harvest digest was
produced, or the last 30 days if no prior digest exists. Do not block to ask
the user questions. This skill is read-only unless the user explicitly asks
for the digest to be saved.

## Output

A digest, grouped by activity type (sown / watered / fertilized / tended /
pruned / grafted / split / entwined / cultivated / trimmed / weeded /
uprooted / other), printed to the chat. If the user asks for it to be saved,
write it to a dated entry, newest first, rather than overwriting prior
digests.

This task runs non-interactively to completion. It does not block for user
input. If in doubt about any of the requirements of this task, stop and
print an error message.

## Instructions

1.  Determine the window.

    If the user gave a range or date, use it. Otherwise, find the most
    recent digest file (if any) and use commits since its date; if none
    exists, default to the last 30 days.

2.  Pull the commit log for the window.

    ```sh
    git log --since="<window-start>" --name-status --pretty=format:'%h %s'
    ```

    This repo's commit messages are prefixed by type, and the
    repository-specific types map directly onto garden activity: `sow:`,
    `water:`, `tend:`, `fertilize:`, `prune:`, `graft:`, `split:`,
    `entwine:`, `cultivate:`, `trim:`, `weed:`, `uproot:`. The `trim:`
    type was formerly named `tidy:`, so older commits carry the legacy
    `tidy:` prefix. Standard types (`chore:`, `format:`, `maintenance:`,
    `landscape:`) fall under "other". Use the prefix as the primary
    signal, but spot-check against the diff — a commit can be
    mislabeled, and history predating this commit-type convention won't
    have a matching prefix at all.

3.  Classify each change.

    For each commit, use the type prefix as the primary signal:

    - Sown (`sow:`): a new `.adoc` page added under `pages/`, plus a
      corresponding `index.adoc` addition.

    - Watered (`water:`): an existing page grown with freshly
      researched depth, detail, or developments, staying on its
      concept.

    - Fertilized (`fertilize:`): an existing page's content grew
      substantially.

    - Tended (`tend:`): fixes to `xref:` targets, pseudo-links, or
      index listings with no new concept introduced.

    - Pruned (`prune:`): a redundant page dropped — deleted because
      another page already covers its topic — with its inbound
      references repointed to that page.

    - Grafted (`graft:`): two or more pages were merged into one
      broader page — the survivor grew while the absorbed pages were
      deleted and their references repointed.

    - Split (`split:`): one page's content shrank while one or more
      new pages appeared in the same change, with cross-links between
      them.

    - Entwined (`entwine:`): new `xref:` links added between existing
      pages, with no content otherwise changed.

    - Cultivated (`cultivate:`): mechanical style-guide fixes (dashes,
      colons, casing, bold usage) with no change to meaning.

    - Trimmed (`trim:`, or legacy `tidy:` in older commits): freeform
      trim within a page — trimmed waffle, smoothed phrasing, reordered
      or de-duplicated content, with meaning left intact.

    - Weeded (`weed:`): a factual error or other harmful content
      corrected on an existing page.

    - Uprooted (`uproot:`): a change reverted.

    - Other: standard types (`chore:`, `format:`, `maintenance:`,
      `landscape:`), and any commit predating this convention with no
      matching prefix — list briefly, don't force a category.

    For commits with no recognizable prefix (older history), fall back
    to inspecting the files touched and classify by the same criteria
    above.

4.  Build the digest.

    Group entries by category. For each entry, give the page title, a
    one-line description of what changed, and the commit short-hash.
    Keep descriptions terse — this is a scan-able digest, not a
    narrative.

5.  Present the digest.

    Print it in the chat by default. Only write it to a file if the
    user asks — and if so, append a new dated section rather than
    overwriting any existing digest history.

## Rules

- Trust the commit type prefix, but spot-check.

  `sow:`/`water:`/`tend:`/`fertilize:`/`prune:`/`graft:`/`split:`/`entwine:`/`cultivate:`/`trim:`
  (and legacy `tidy:`) map directly onto these categories, but prefixes
  can be wrong or absent in older history — fall back to inspecting the
  diff when a prefix is missing or looks mismatched against the actual
  files touched.

- Keep it a report, not an action.

  If the digest surfaces something that looks broken or undone (eg. a
  half-finished graft, a page added but never linked from the index),
  name it as a finding for the user to send to [tend](../tend/SKILL.md)
  — don't fix it inline.

- Default to the chat, not a file.

  Most uses of this skill are a quick check-in, not a permanent
  changelog entry — only persist to disk on explicit request.

- Do NOT commit your changes.

  Even when the user asks for the digest to be saved to a file, this
  skill only writes that file — never stage, commit, or push it.

## Success criteria

- Every commit in the window is classified into one of the categories,
  with no commit silently dropped.

- The digest is grouped by activity type, not presented as a flat
  chronological list.

- Classification is checked against the actual diff whenever a commit's
  type prefix is missing or looks mismatched against the files it
  touched.

- No garden file was modified by running this skill, unless the user
  explicitly asked for the digest to be saved.

## References

None.
