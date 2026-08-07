---
name: trim
description: >-
  Make small, self-evident improvements to how one entry reads — cutting
  waffle, smoothing awkward phrasing, dropping repetition, and moving a
  paragraph to a better home — without changing what it says. Use when the
  user says "trim this", "tidy this up", "give this a once-over", "move this bit
  somewhere better", or "trim agent.adoc". Do not use it to add content, fix
  links, or apply style-guide rules.
compatibility: requires Read, Edit
license: CC0-1.0
---

# Trim

Everyday gardening: a freeform, judgment-driven pass over one entry, made with
secateurs in hand. Cut waffle, smooth awkward phrasing, move a paragraph to a
better home, merge stray sentences, drop repetition. Change how the entry
reads, never what it says.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single existing file under
  `src/modules/ROOT/pages/`, named by the user, eg. "trim agent.adoc".
  Accept a topic name too, and resolve it to the file whose `=` title
  matches.

- **Focus — OPTIONAL.** A section of the entry the user wants trimmed, eg.
  "trim the section on AI agents". Defaults to the whole entry.

## Success criteria

- The entry MUST read tighter and better ordered than before, with no waffle
  or local repetition a careful read would still catch.

- The entry's meaning and voice MUST be unchanged. Only the expression and
  the arrangement move.

- No content MAY have moved to or from another entry, and no entry MAY have
  been created, merged, or deleted.

- No `xref:` target, bracketed term, or maturity emoji MAY have changed.
  These belong to structural and style passes, and mixing them into a
  freeform diff makes the trim impossible to review.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the target entry in full, and understand what it is about before
    touching it.

2.  Work through the entry applying small improvements in place. Keep each
    change small enough that its merit is self-evident on reading the diff.

3.  Report the edits you made and why. Group them where it helps, eg.
    trimmed, smoothed, moved, de-duplicated.

## Rules

- You SHOULD make only changes that are self-evidently improvements.

  A trim is approved by reading the diff, so every edit must justify itself
  at a glance. Anything needing an argument is too big for this pass.

- In scope: you MAY cut filler and padding, fix clumsy sentences and tangled
  clauses, remove a sentence that repeats something said elsewhere in the
  entry, reorder paragraphs for flow, pull a stray point into a section it
  sits better in, merge two half-empty bullets, and split a run-on bullet.

- Out of scope: you MUST NOT repair cross-references, pseudo-links, orphans,
  or maturity emoji; you MUST NOT apply style-guide conventions such as dash,
  colon, casing, or bold rules; and you MUST NOT add new content, even where
  the entry is plainly a stub.

  Each of those is a separate pass, and each produces a differently shaped
  diff. Keeping them apart is what makes any of them reviewable.

- You MUST NOT change meaning.

  Where tightening a sentence could shift what it asserts, leave the
  sentence alone. A slightly baggy true statement beats a crisp wrong one.

- You SHOULD preserve the author's voice.

  Match the existing tone and phrasing conventions rather than imposing your
  own register.

- You MUST stay within the target entry.

  Do not edit any other file, and do not create, delete, or merge entries.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- The entry is too thin to trim.

  Say so and stop. A stub has no waffle to cut, and padding it out is a
  different job with a different scope.

- A paragraph would sit better on a different entry entirely.

  Do not move it. Report it as a candidate for a linking or restructuring
  pass — moving content between entries changes both, which is outside this
  skill's single-entry boundary.
