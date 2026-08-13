---
name: graft
description: >-
  Merge two or more related-but-distinct entries into one broader entry,
  repointing every cross-reference and removing the absorbed files. Use this
  skill when the user says something like "graft retry.adoc, backoff.adoc and
  jitter.adoc into one retry-strategies page", "these three entries really
  cover one theme — merge them", or asks to merge one entry into another. Do
  not use it when one entry adds nothing the others lack, which calls for a
  drop instead.
compatibility: >-
  requires Read, Glob, Grep, Write, Edit, Bash (git rm)
license: CC0-1.0
---

# Graft

Merge two or more related-but-distinct garden entries into a single broader
entry, with cross-references repointed and the absorbed files removed. The
survivor carries the distinct content of each source, arranged as coherent
sections rather than concatenated verbatim.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Source entries — REQUIRED.** Two or more existing files under
  `src/modules/ROOT/pages/`, named by the user, eg. "graft retry.adoc,
  backoff.adoc and jitter.adoc".

- **Survivor — OPTIONAL.** The entry the merged content lands in, either one
  of the sources promoted to a broader title or a new file. Where the user
  names a title, eg. "into one retry-strategies page", use it; otherwise
  promote whichever source already covers the broadest ground.

## Success criteria

- One surviving entry MUST cover the combined concept, reading as a single
  coherent entry rather than stitched fragments.

- The distinct content of every source MUST be present in the survivor.

- No `xref:` anywhere under `src/modules/ROOT/pages/` MAY still name an
  absorbed file.

- `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc` MUST
  each list the survivor exactly once, under its final title and in the
  correct alphabetical position, with the absorbed entries' listings
  removed.

- No maturity emoji MUST have changed on an entry that survives.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read every source entry in full.

    Confirm they are related but distinct, each contributing content the
    others do not. Where one is already fully covered by another and adds
    nothing, exclude it from the graft and report it as a candidate to be
    dropped instead. Grafting combines distinct content; it is not a way to
    clear out redundancy.

2.  Plan the merge.

    Decide the survivor — an existing source promoted to the broader title,
    or a new file that absorbs them all — and map each source's content onto
    sections of it. Record this plan; it goes in your report, and it is what
    the user checks the diff against.

3.  Build the merged entry.

    Carry the distinct content of each source into the survivor as coherent
    sections, rewriting the transitions so it reads as one entry. Follow the
    garden's conventions for an atomic entry: a single `=` title, a focused
    body, `xref:` outward rather than re-explaining. Where the survivor is a
    new file, create `src/modules/ROOT/pages/<title-kebab-case>.adoc`; where
    it is a promoted source, edit it in place and retitle it.

4.  Repoint every reference.

    Grep the whole garden for `xref:<absorbed-file>.adoc`, for each absorbed
    entry, and replace with `xref:<survivor-file>.adoc`, adjusting the link
    text so it still reads sensibly in context. Where an entry ends up
    linking the survivor more than once, collapse the duplicates.

5.  Remove the absorbed entries, once nothing references them.

    ```sh
    git rm src/modules/ROOT/pages/<absorbed-file>.adoc
    git restore --staged src/modules/ROOT/pages/<absorbed-file>.adoc
    ```

    The second command puts the deletion back in the working tree, alongside
    your other changes, rather than leaving it in the index.

6.  Update the index and nav.

    Remove the absorbed entries' listings from
    `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc`, and
    list the survivor once in each, under its final title and in the correct
    alphabetical position.

7.  Report which entry survived or was created, what content came from each
    source, every reference repointed, and every file deleted.

## Rules

- You MUST NOT delete an entry before every reference to it has been
  repointed.

  A dangling `xref:` left behind by a graft is worse than the fragmentation
  it replaced, because nothing in the build catches it.

- You MUST NOT discard distinct content.

  Every source contributes something the others do not — that is what makes
  this a graft rather than a drop. Where a section genuinely does not belong
  in the survivor, leave its source entry out of the graft rather than
  losing the content in the merge.

- Grafting MUST NOT be used to clear redundancy.

  Where a source's topic is already covered by another and it adds nothing,
  that is a drop, not a merge. Keeping the two apart keeps the destructive
  remit narrow.

- You MUST NOT change the survivor's maturity emoji in the index.

  A merged entry usually deserves a new label, but maturity is an editorial
  judgment the user reserves. Recommend one in your report.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree, the deletions included, so the
  user can restore a file with `git restore` after reading the diff.
  Reviewing that diff is how the user approves the work.

## Edge cases

- The survivor is a new file rather than a promoted source.

  Every source is then absorbed and deleted, and the new entry needs a fresh
  listing in the index and the nav. Carry across the highest maturity emoji
  among the sources unchanged, and recommend a review of it in your report.

- Grafting would produce an entry covering more than one concept.

  Stop before building it. Entries that read better together are one
  concept; entries that merely sit near each other are not, and merging them
  only creates work for a later restructuring pass.
