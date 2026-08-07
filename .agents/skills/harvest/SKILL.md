---
name: harvest
description: >-
  Summarize recent garden activity from the Git history — entries sown,
  watered, fertilized, tended, pruned, grafted, split, entwined, cultivated,
  trimmed, weeded, or uprooted — as a digest grouped by activity type. Use
  when the user says "harvest the garden", "what's changed recently", or asks
  for a summary of recent activity. Do not use it to fix what the digest finds.
compatibility: >-
  requires Read, Glob, Write, Bash (git log)
license: CC0-1.0
---

# Harvest

Produce a digest of recent garden activity, grouped by activity type, for
review or changelog purposes. Harvesting reads the Git history and reports.
It never repairs what it finds.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Window — OPTIONAL.** A time period or commit range, eg. "harvest the last
  2 weeks", "harvest since v1.4". Where none is given, run from the date of
  the most recent saved digest, or the last 30 days where no digest exists.

- **Digest store — OPTIONAL.** Where a saved digest is written, and where
  step 1 looks for the previous one. This repository does not prescribe a
  location, so resolve it from the user's request, then from the surrounding
  context, then from any existing digest file in the workspace. Where no
  store can be resolved, print the digest to the chat and say so — do not
  invent a path.

## Success criteria

- Every commit in the window MUST appear in the digest under one activity
  type, with none silently dropped.

- The digest MUST be grouped by activity type, not presented as a flat
  chronological list.

- Every commit whose type prefix is missing, legacy, or mismatched against
  the files it touched MUST have been classified from its diff instead.

- Each entry in the digest MUST carry the entry title, a one-line description
  of what changed, and the commit's short hash.

- No file in the repository MUST have been modified, unless the user asked
  for the digest to be saved, in which case only the digest file MUST have
  been written.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Determine the window.

    Where the user gave a range or a date, use it. Otherwise look for the
    most recent saved digest in the resolved digest store and start from its
    date. Where neither is available, use the last 30 days.

2.  Pull the commit log for the window.

    ```sh
    git log --since="<window-start>" --name-status --pretty=format:'%h %s'
    ```

3.  Classify each commit by its type prefix.

    This repository's commit types map onto garden activity directly:
    `sow:` sown, `water:` watered, `fertilize:` fertilized, `tend:` tended,
    `prune:` pruned, `graft:` grafted, `split:` split, `entwine:` entwined,
    `cultivate:` cultivated, `trim:` trimmed, `weed:` weeded, `uproot:`
    uprooted. The standard types `chore:`, `format:`, `maintenance:`, and
    `landscape:` all fall under "other".

    Older history predates this convention and carries prefixes that no
    longer exist. Map them by intent, checking the diff before you trust
    them: `add:` is usually sown, `tidy:` trimmed, `style:` cultivated,
    `fix:` weeded, `refactor:` other. `edit:` covers several activities and
    MUST always be classified from its diff.

4.  Classify from the diff wherever the prefix is missing, legacy, or does
    not match the files touched. The signatures are distinctive: a new file
    under `pages/` plus index and nav additions is a sow; a file deleted with
    inbound links repointed is a prune; one file shrinking as new ones appear
    is a split; several files deleted into one growing file is a graft;
    `xref:` additions with no other change is an entwine.

5.  Build the digest.

    Group by activity type. Give each entry its entry title, a one-line
    description of what changed, and the commit's short hash. Keep the
    descriptions terse — this is a scannable digest, not a narrative.

6.  Present the digest in the chat. Only write it to the digest store where
    the user asked for it to be saved, and then as a new dated section,
    newest first, leaving prior digests intact.

## Rules

- You MUST verify a commit's type prefix against its diff whenever the two
  could disagree.

  A prefix is a claim by the commit's author, not evidence. Most of this
  repository's history predates the current types, so a run that trusts
  prefixes blindly will miscount the older half of any long window.

- You MUST report rather than repair.

  Where the digest surfaces something broken or half-finished — an entry
  added but never listed in the index, a graft that left dangling links —
  name it as a finding for a structural pass. Fixing it here would put
  unrelated content changes into what is meant to be a read-only survey.

- You SHOULD default to the chat rather than a file.

  Most runs are a quick check-in, not a permanent changelog entry. Persist
  to the digest store only on an explicit request.

- You MUST NOT stage, commit, or push, even when saving a digest.

  Leave the digest file in the Git working tree. Reviewing the diff is how
  the user approves the work.

## Edge cases

- The window contains a merge commit with no meaningful diff of its own.

  Classify it under "other" and keep it in the count. Dropping it silently
  breaks the guarantee that every commit is accounted for.

- One commit spans several activities.

  File it under the dominant one and note the rest in its one-line
  description. Listing it twice would inflate the counts the digest is read
  for.
