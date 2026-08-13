---
name: sow
description: >-
  Create a new entry in this AsciiDoc knowledgebase — researching the topic,
  writing a single-concept page, and cross-referencing it to related entries.
  Use this skill when the user says something like "sow a new entry for event
  sourcing", "plant a page on the circuit breaker pattern", or asks to add a
  new topic to the garden. Do not use it when the topic already has an entry,
  which should be extended instead.
compatibility: >-
  requires Read, Glob, Grep, Write, Edit, WebSearch, WebFetch
license: CC0-1.0
---

# Sow

Research a topic and plant it as a new entry in the garden, cross-referenced
to adjacent entries. The result is self-contained, focused on a single idea,
and linked in both directions to what is already growing around it.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Topic — REQUIRED.** The subject of the new entry, as named by the user,
  eg. "sow an entry for event sourcing".

- **Title — OPTIONAL.** Defaults to the topic in sentence case. The filename
  is the title in kebab-case, so "Event sourcing" gives
  `event-sourcing.adoc`.

- **Hot topic — OPTIONAL.** Whether the topic is one the user is actively
  researching, in which case it is also listed under "Hot topics 🔥" in the
  index. Defaults to no.

## Success criteria

- A new entry MUST exist at `src/modules/ROOT/pages/<title-kebab-case>.adoc`,
  opening with a single `=` title line and carrying a non-empty body.

- The entry MUST be listed under the correct alphabetical sub-section of
  "All topics" in `src/modules/ROOT/pages/index.adoc`, carrying the 🌱
  emoji, and at the matching alphabetical position in
  `src/modules/ROOT/nav.adoc`.

- Every `xref:` you add, in the new entry and in entries linking back to it,
  MUST name a file that exists under `src/modules/ROOT/pages/`.

- The new entry SHOULD link to at least one adjacent entry, unless research
  genuinely turns up no related topic already in the garden.

- No existing entry MAY be changed beyond the insertion of an inbound `xref:`
  and any short clause introducing it. Sowing plants; it does not rewrite the
  neighbors.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Check for an existing entry.

    Search `src/modules/ROOT/pages/` by filename and by `=` title line for a
    topic already covering this ground, including obvious synonyms and
    singular/plural variants. If one exists, stop and report it — the topic
    should be extended rather than duplicated.

2.  Decide whether the topic warrants its own entry.

    A topic earns its own file when it will be cross-referenced from
    *multiple* other entries. That is the atomicity criterion. If the topic
    would only ever be linked from one place, it belongs as a section of that
    entry. Stop and report that instead of sowing.

3.  Research the topic.

    Gather enough understanding to write an accurate, concise explanation:
    what the concept is, why it matters, and how it relates to neighboring
    concepts already in the garden. Prefer a small number of reliable sources
    over breadth. This is a knowledgebase entry, not a survey paper.

4.  Find adjacent topics already in the garden.

    Search existing entries for broader categories, sibling techniques, and
    prerequisites. These become the new entry's outbound `xref:` links. Note
    their exact filenames — an AsciiDoc `xref:` target must match a real
    file.

5.  Write the entry.

    Create `src/modules/ROOT/pages/<title-kebab-case>.adoc`, following the
    structure of existing entries:

    - A single `=` title line matching the topic name.

    - A short, focused explanation, self-contained but linking out via
      `xref:` rather than re-explaining a concept that has its own entry.

    - A "See also" line or section for related topics that do not fit
      naturally inline.

    Follow `docs/style-guide.md` — in particular, every `xref:` is wrapped in
    `*...*`.

6.  Link the entry back in.

    For each adjacent topic from step 4, add an inbound `xref:` from that
    entry where it reads naturally. The garden is most useful when paths run
    in both directions, not just outward from the new entry.

7.  List the entry on the index.

    Add a line to `src/modules/ROOT/pages/index.adoc`, in the correct
    alphabetical sub-section under "All topics", following the existing
    `*xref:<file>.adoc[Title]* <emoji>` pattern, marked 🌱. Add it under
    "Hot topics 🔥" as well if the hot topic parameter says so.

8.  Update the nav.

    Add the entry to `src/modules/ROOT/nav.adoc` at the same alphabetical
    position it occupies in the index, following the existing
    `** xref:<file>.adoc[Title]` pattern, with no maturity emoji. Without
    this the entry has no ancestry and renders with no breadcrumb trail.

9.  Report the file created, the entries it links to and from, and where it
    landed in the index.

## Rules

- A new entry MUST be plausibly cross-referenceable from at least two other
  entries.

  This is the gate for sowing. A topic that would only be linked from one
  entry is a section of it, not an entry in its own right. When in doubt, prefer
  extending an existing entry over creating a new one.

- You MUST link rather than duplicate.

  Where a concept is already explained elsewhere, `xref:` to it instead of
  re-explaining it. The value of the garden is in the connections between
  atomic notes, not in self-contained essays.

- One file MUST cover one concept.

  If research surfaces a second distinct concept, that is a separate entry,
  cross-linked — not a second section here. Sow it separately only if it too
  meets the atomicity criterion above.

- A newly sown entry MUST be marked 🌱 Seedling in the index.

  Maturity is earned through later growth and maintenance, not assigned at
  creation.

- The index and the nav MUST be kept in step.

  An entry added to one is added to the other, at the same alphabetical
  position. An entry listed in only one of them is half-published.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- Research turns up no related entry anywhere in the garden.

  Sow the entry anyway, with no outbound `xref:`, and say so in the report.
  A genuinely novel topic in a young section of the garden is not a reason
  to refuse. Note it as a candidate for a later linking pass.

- The topic collides with an entry under a different name.

  Treat a synonym as an existing entry, not as a gap. Stop, name the entry
  you found, and report the collision rather than planting a near-duplicate
  that will later need dropping.
