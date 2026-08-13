---
name: entwine
description: >-
  Find entries related to one target entry but not yet cross-referenced from
  it, and add the missing links in both directions. Use this skill when the user 
  says something like "entwine event-sourcing.adoc with its neighbors", "link 
  this page to related entries", or asks whether an entry is properly connected. 
  Do not use it to create entries or to repair links that are already broken.
compatibility: requires Read, Glob, Grep, Edit
license: CC0-1.0
---

# Entwine

Given a single garden entry, find other entries related to it but not yet
cross-referenced, and add the missing `xref:` links. Entwining connects
concepts that were growing in isolation. It creates no entries and rewrites no
prose beyond the clause that carries a link.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename.

## Success criteria

- Every link added MUST carry a one-line justification in the report, so the
  user can sanity-check the connection without reading both entries.

- Every `xref:` added MUST name a file that exists under
  `src/modules/ROOT/pages/`.

- Each linked pair SHOULD be connected in both directions, unless the
  relationship only reads naturally one way.

- No entry MAY have been created or deleted, and no entry's scope MAY have
  changed. Only links, and the clauses introducing them, are added.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Build a map of the garden's concepts.

    List every file under `src/modules/ROOT/pages/`, taking its `=` title
    and opening paragraph as a summary of what it covers. This is the field
    the target is compared against.

2.  Find entries related to the target but not linked to it.

    Look for entries that:

    - Share a section or a parent with the target in
      `src/modules/ROOT/pages/index.adoc`.

    - Name the target's concept in plain prose, with no `xref:` and no
      bracketed marker. A bracketed marker means the term is already
      accounted for by a structural pass, so leave those alone.

    - Are natural neighbors by domain knowledge, with no textual hint at
      all. A reader of `circuit-breaker.adoc` likely wants `retry.adoc`,
      whether or not either mentions the other.

3.  Assess each candidate pair, and keep only those where the connection is
    obvious enough to state in one line. Favor precision over volume: a
    strained link is worse than a missing one.

4.  Add the links.

    For each pair kept, add an `xref:` in both directions where the
    relationship reads naturally in each entry's context, and in one
    direction otherwise. Place each link where it fits the existing prose
    rather than bolting on a "See also" line when a natural spot exists in
    a sentence already there. Follow `docs/style-guide.md`, wrapping every
    `xref:` in `*...*`.

5.  Report every link added, naming both files and giving the one-line
    reason for the connection, along with the candidates you rejected and
    why.

## Rules

- You MUST entwine one entry at a time.

  Entwining links a single target into its neighborhood. A garden-wide
  link-everything pass produces a diff too large to review, which defeats
  the working tree as a review gate.

- You MUST favor precision over volume.

  A handful of well-justified links beats dozens of tenuous ones. Where a
  relationship needs a paragraph to justify, it is too thin to link.

- You MUST NOT link to a hub entry that already aggregates the target.

  Hub entries such as `architecture-and-design.adoc` and
  `computer-science.adoc` aggregate many topics by design. Entwining is
  about missing sibling connections, not a redundant link back up to a hub
  that already lists the target.

- You MUST NOT repair existing links.

  A broken `xref:` or a bracketed pseudo-link belongs to a structural pass.
  Report any you notice and leave them.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- The target is already densely linked.

  Say so and add nothing. A well-connected entry is the goal, and forcing
  further links onto it only adds noise.

- A related concept has no entry at all.

  Do not create one. Report it as a candidate worth planting, and leave any
  bracketed marker for that term as it stands.

## Examples

- Given `event-sourcing.adoc`, a good result reads: linked to `cqrs.adoc`,
  commonly paired and already linking back; linked both ways with
  `event-driven-architecture.adoc`, the parent pattern, which neither
  previously referenced.
