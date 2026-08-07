---
name: prune
description: >-
  Drop one redundant entry whose topic another entry already covers, repointing
  every reference to the covering entry and removing its index and nav
  listings. Use when the user says "prune acid.adoc", "this entry is already
  covered by X, drop it", or suspects an entry is redundant. Do not use it when
  each entry carries distinct content, which calls for a merge instead.
compatibility: >-
  requires Read, Glob, Grep, Edit, Bash (git rm)
license: CC0-1.0
---

# Prune

Drop a garden entry whose topic is already well covered by another, redirecting
its inbound links to the covering entry. The covering entry survives; the
redundant one goes. Where the target turns out to carry content of its own,
nothing is deleted.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** The single entry suspected of being
  redundant, named by the user, eg. "prune acid.adoc".

- **Covering entry — OPTIONAL.** The entry that already covers the target's
  topic, where the user names it, eg. "acid.adoc is covered by
  acid-principles.adoc". Where none is given, find it yourself in step 1.

## Success criteria

- The dropped entry's topic MUST be genuinely covered by the surviving
  entry, with nothing unique lost.

- No `xref:` anywhere under `src/modules/ROOT/pages/` MAY still name the
  deleted file.

- `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc` MUST no
  longer list the dropped entry, and the covering entry's listings in both
  MUST be intact.

- Exactly one entry MAY have been deleted. Pruning drops a single target; it
  is not a garden-wide duplicate sweep.

- Where the target proved to carry distinct content, no file MUST have been
  deleted, and the finding MUST be reported instead.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Identify the covering entry.

    Where the user named it, use it. Otherwise search
    `src/modules/ROOT/pages/` for the entry covering the same concept — a
    similar title or filename, or overlapping content. Where nothing covers
    it, stop and report: the topic is unique and should be kept.

2.  Confirm the target is genuinely redundant.

    Read both entries in full. The target is a prune candidate only where
    the covering entry already says everything the target does. Where the
    target carries substantial content of its own — examples, nuance, a
    distinct angle — it is not covered. Stop, delete nothing, and report the
    pair as a merge candidate, or as two entries that simply want linking.

3.  Salvage any stray detail.

    Where the target holds only a scrap the covering entry lacks — a single
    sentence, one example — fold it into the covering entry before deleting.
    Anything larger than a scrap means the topic was not really covered:
    return to step 2 and reclassify.

4.  Repoint every reference.

    Grep the whole garden for `xref:<target-file>.adoc` and replace each
    with `xref:<covering-file>.adoc`, adjusting the link text so it still
    reads sensibly in context. Where an entry ends up linking the covering
    entry twice, collapse the duplicate.

5.  Update the index and nav.

    Remove the target's listing from `src/modules/ROOT/pages/index.adoc` and
    `src/modules/ROOT/nav.adoc`, and confirm the covering entry's listings
    in both are still correct.

6.  Delete the redundant entry, once nothing references it.

    ```sh
    git rm src/modules/ROOT/pages/<target-file>.adoc
    ```

    Then unstage it, so the deletion sits in the working tree alongside your
    other changes rather than in the index.

    ```sh
    git restore --staged src/modules/ROOT/pages/<target-file>.adoc
    ```

7.  Report which entry was dropped, which one now covers it, any scrap
    salvaged, and every file where a reference was repointed.

## Rules

- You MUST NOT delete an entry before every reference to it has been
  repointed.

  A dangling `xref:` left behind by a prune is worse than the redundant
  entry it replaced, because nothing in the build catches it.

- You MUST drop rather than merge.

  Pruning removes an entry that adds nothing. Where two entries each carry
  distinct content that should be combined, that is a merge, and doing it
  here would silently widen this skill's remit into a destructive one.

- The covering entry MUST be the one that survives.

  Where the named target turns out to be the fuller of the two, do not
  delete it. Report that the other entry is the redundant one and let the
  user re-aim the skill.

- When in doubt, you MUST NOT drop.

  Keep both entries and report them as candidates for linking instead.
  Deleting an entry that was not really covered loses content; a redundant
  entry left standing is harmless by comparison.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree, the deletion included, so the
  user can restore the file with `git restore` after reading the diff.
  Reviewing that diff is how the user approves the work.

## Edge cases

- The target's body is nothing but a pointer to another entry.

  This is a redirect stub, and it is the cleanest possible prune. Repoint
  its inbound links and drop it, with no salvage step needed.

- Three or more entries all cover the same topic.

  Prune one target per run, against one covering entry, and report the
  others. Batching deletions produces a diff nobody can check.
