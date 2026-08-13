---
name: divide
description: >-
  Break up an overgrown entry that has drifted into covering two or more
  distinct concepts, narrowing the original and planting a new cross-linked
  entry for each concept extracted. Use this skill when the user says something
  like "divide event-driven-architecture.adoc — it's covering both event
  sourcing and CQRS", "this entry has grown to cover two ideas, divide it", or
  asks to break an overgrown entry up into separate pages. Do not use it to
  extract a concept that only the original entry would ever link to.
compatibility: >-
  requires Read, Glob, Grep, Write, Edit
license: CC0-1.0
---

# Divide

Divide an overgrown garden entry that has drifted into covering two or more
distinct concepts back into separate atomic entries, cross-linked together. The
original is narrowed to its core concept, and each concept extracted gets its
own entry.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename.

- **Concepts to extract — OPTIONAL.** The concept(s) the user wants lifted out,
  eg. "it's covering both event sourcing and CQRS". Where none are given,
  analyse the page's content and identify the multiple concepts yourself.

## Success criteria

- The target entry MUST cover exactly one concept once the divide is done.

- Each new entry MUST exist at
  `src/modules/ROOT/pages/<title-kebab-case>.adoc` and MUST read
  self-containedly, without the original for context.

- Each new entry MUST be listed under the correct alphabetical sub-section of
  "All topics" in `src/modules/ROOT/pages/index.adoc`, carrying the 🌱 emoji,
  and at the matching alphabetical position in `src/modules/ROOT/nav.adoc`.

- The target and each new entry MUST be cross-linked, and every `xref:` you
  add MUST name a file that exists under `src/modules/ROOT/pages/`.

- No new entry MAY duplicate a topic the garden already covers, checked
  against the file inventory before creation.

- No maturity emoji on an entry that already existed MUST have changed.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the target entry in full.

    Identify the distinct concepts it currently covers. A genuine divide
    candidate has sections that could each stand alone; sub-points of a
    single idea are not concepts.

2.  Plan the divide.

    Name what stays under the original title and what becomes a new entry
    for each concept extracted. Record this plan; it goes in your report,
    and it is what the user checks the diff against.

3.  Apply the atomicity criterion to each concept extracted.

    A concept earns its own file only where it will be cross-referenced from
    *multiple* other entries. One that only the original would ever link to
    is a section of the original. Drop it from the plan and leave it inline.
    Dividing should reduce an entry to one concept by extracting genuinely
    shared ones, not fragment it into single-link stubs.

4.  Check for collisions.

    Before creating anything, search `src/modules/ROOT/pages/` for an entry
    already covering each concept, including obvious synonyms and
    singular/plural variants. Where one exists, fold the extracted content
    into that entry instead of creating a near-duplicate.

5.  Create the new entries.

    For each concept extracted, create
    `src/modules/ROOT/pages/<title-kebab-case>.adoc`, following the garden's
    conventions for an atomic entry: a single `=` title, a focused body,
    `xref:` outward rather than re-explaining. Carry over the relevant
    content from the original, rewritten to stand alone. Follow
    `docs/style-guide.md`, wrapping every `xref:` in `*...*`.

6.  Narrow the original.

    Remove the extracted sections, leaving the entry on its core concept,
    and add an `xref:` to each new entry where the relationship reads
    naturally.

7.  Cross-link the new entries to one another, where they relate to each
    other and not only to the original.

8.  Update the index and nav.

    Add each new entry to `src/modules/ROOT/pages/index.adoc` in its correct
    alphabetical sub-section, marked 🌱 — it is a new entry, whatever the
    age of the material in it — and to `src/modules/ROOT/nav.adoc` at the
    matching alphabetical position. Without the nav listing an entry has no
    ancestry and renders with no breadcrumb trail.

9.  Report the files created, what moved from the original into each, and
    every cross-link added.

## Rules

- A concept MUST NOT be extracted unless it will be cross-referenced from at
  least two other entries.

  This is the gate for dividing, and it is the same criterion that governs
  planting a new entry. Without it, a divide trades one overgrown entry for
  several stubs nothing links to.

- You MUST check for an existing entry before creating one.

  A concept lifted out of an overgrown entry has often already been planted
  elsewhere. Creating the duplicate makes work for a later drop.

- You MUST rewrite extracted content to read standalone.

  Content lifted out of an entry usually refers back to it implicitly, with
  phrases like "as mentioned above". Turn those into explicit `xref:` links
  or remove them, so the new entry is self-contained.

- A newly created entry MUST be marked 🌱 Seedling in the index, and you
  MUST NOT change the maturity emoji of the entry you divide.

  Maturity is an editorial judgment the user reserves. Where narrowing the
  original leaves its label overstated, recommend a change in your report.

- The index and the nav MUST be kept in step.

  An entry added to one is added to the other, at the same alphabetical
  position. An entry listed in only one of them is half-published.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- Every candidate concept fails the atomicity criterion.

  Do not divide. Report that the entry is long but singular, and suggest
  tightening its prose instead.

- The original is left thinner than the entries extracted from it.

  That is expected where the overgrowth was the main event, and it is not a
  reason to keep the concepts inline. Say so in the report, and note the
  narrowed entry as a candidate for a later research-and-extend pass.
