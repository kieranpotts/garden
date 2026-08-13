---
name: graft
description: >-
  Absorb one related-but-distinct entry — the dead-head — into a target entry,
  combining their content in the survivor, repointing every cross-reference to
  the dead-head, and removing the dead-head file. Use this skill when the user
  says something like "graft backoff.adoc into retry.adoc", "absorb jitter.adoc
  into retry-strategies.adoc", or asks to merge one entry into another. Do not
  use it when the dead-head adds nothing the target lacks, which calls for a
  drop instead.
compatibility: >-
  requires Read, Glob, Grep, Write, Edit, Bash (git rm)
license: CC0-1.0
---

# Graft

Graft one garden entry — the dead-head — into a target entry, combining their
distinct content in the survivor. The target carries the merged content,
arranged as coherent sections rather than concatenated verbatim. The dead-head
is removed once every reference to it has been repointed at the target.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** The surviving entry the merged content lands
  in. A single file under `src/modules/ROOT/pages/`, named by the user, eg.
  "graft backoff.adoc into retry.adoc". The target keeps its filename and
  title unless the user asks for a retitle.

- **Dead-head entry — REQUIRED.** The entry to be absorbed into the target.
  A single existing file under `src/modules/ROOT/pages/`, named by the user.
  The dead-head contributes distinct content the target does not already
  carry, then is deleted. One dead-head per run — to absorb several entries
  into the same target, run the skill once per dead-head, or delegate each to
  a sub-agent.

## Success criteria

- The target entry MUST cover the combined concept, reading as a single
  coherent entry rather than stitched fragments.

- The distinct content of the dead-head MUST be present in the target.

- No `xref:` anywhere under `src/modules/ROOT/pages/` MAY still name the
  dead-head file.

- `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc` MUST no
  longer list the dead-head, and the target's listings in both MUST be intact
  (updated to the target's final title, where it was retitled).

- No maturity emoji MUST have changed on the target entry.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the target and the dead-head in full. Confirm they are related but
    distinct, each contributing content the other does not. Where the
    dead-head is already fully covered by the target and adds nothing, stop
    and report it as a candidate to be dropped instead. Grafting combines
    distinct content. It is not a way to clear out redundancy.

2.  Plan the merge. Map the dead-head's content onto sections of the target,
    deciding what stays as its own section and what weaves into existing
    prose. Record this plan. It goes in your report, and it is what the user
    checks the diff against.

3.  Build the merged entry. Carry the dead-head's distinct content into the
    target as coherent sections, rewriting the transitions so it reads as one
    entry. Follow the garden's conventions for an atomic entry: a single `=`
    title, a focused body, `xref:` outward rather than re-explaining. Retitle
    the target only where the user asked for it. Follow `docs/style-guide.md`,
    wrapping every `xref:` in `*...*`.

4.  Repoint every reference. Grep the whole garden for
    `xref:<dead-head-file>.adoc` and replace each with
    `xref:<target-file>.adoc`, adjusting the link text so it still reads
    sensibly in context. Where an entry ends up linking the target more than
    once, collapse the duplicates.

5.  Update the index and nav. Remove the dead-head's listing from
    `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc`. Where
    the target was retitled, update its listing in both to the final title,
    keeping it in the correct alphabetical position.

6.  Remove the dead-head, once nothing references it.

    ```sh
    git rm src/modules/ROOT/pages/<dead-head-file>.adoc
    git restore --staged src/modules/ROOT/pages/<dead-head-file>.adoc
    ```

    The second command puts the deletion back in the working tree, alongside
    your other changes, rather than leaving it in the index.

7.  Report what content came from the dead-head, every reference repointed,
    and the file deleted.

## Rules

- You MUST NOT delete the dead-head before every reference to it has been
  repointed. A dangling `xref:` left behind by a graft is worse than the
  fragmentation it replaced, because nothing in the build catches it.

- You MUST NOT discard distinct content. The dead-head contributes something
  the target does not — that is what makes this a graft rather than a drop.
  Where a section of the dead-head genuinely does not belong in the target,
  stop and report it: the dead-head is not a graft candidate after all, and
  losing the content in the merge is not an option.

- Grafting MUST NOT be used to clear redundancy. Where the dead-head's topic
  is already covered by the target and it adds nothing, that is a drop, not a
  merge. Keeping the two skills apart keeps the destructive remit narrow.

- You MUST graft one dead-head at a time. Absorbing several entries into one
  target in a single run produces a diff too large to review, which defeats
  the working tree as a review gate. Run the skill once per dead-head, or
  delegate each to a sub-agent.

- You MUST NOT change the target's maturity emoji in the index. A merged
  entry usually deserves a new label, but maturity is an editorial judgment
  the user reserves. Recommend one in your report.

- You MUST NOT stage, commit, or push. Leave every change in the Git working
  tree, the deletion included, so the user can restore the dead-head with
  `git restore` after reading the diff. Reviewing that diff is how the user
  approves the work.

## Edge cases

- Grafting would leave the target covering more than one concept. Stop before
  building the merge. Entries that read better together are one concept.
  Entries that merely sit near each other are not, and merging them only
  creates work for a later restructuring pass.

- The dead-head turns out to carry content the target already has, plus a
  distinct scrap. Fold the scrap into the target and treat the dead-head as
  redundant — the run becomes an uproot rather than a graft. Report it as
  such and let the user re-aim the skill.

- The user asks to retitle the target to a broader name. Honor it, and update
  the target's index and nav listings to the final title in its new
  alphabetical position. Where no retitle was requested, the target keeps its
  title and filename.