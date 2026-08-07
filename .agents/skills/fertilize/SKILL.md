---
name: fertilize
description: >-
  Bring a thin stub entry up to strength — deepening its explanation,
  resolving its flagged gaps, and adding cross-references — without changing
  what it is about. Use when the user says "fertilize X", "this needs growth",
  "expand the stub on X", or asks to flesh out a short or underdeveloped page.
  Do not use it on an entry that is already established.
compatibility: >-
  requires Read, Glob, Grep, Edit, WebSearch, WebFetch
license: CC0-1.0
---

# Fertilize

Bring a thin stub entry in the garden up to strength, without changing its
scope. Fertilizing deepens the entry's explanation, resolves the gaps its
author flagged, and adds cross-references — it does not widen the entry into a
different concept.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — OPTIONAL.** A single existing file under
  `src/modules/ROOT/pages/`, named by the user, eg. "fertilize
  abstraction.adoc". Where none is given, pick the weakest stub yourself, by
  the ranking in step 1.

## Success criteria

- The target entry MUST still carry the same title, filename, and scope as
  before, only fuller.

- Every `// TODO` marker in the target entry MUST be either resolved and
  removed, or left in place with the reason given in your report.

- Every `xref:` you add, in the target entry and in entries linking back to
  it, MUST name a file that exists under `src/modules/ROOT/pages/`.

- The entry SHOULD gain at least one cross-reference, unless research turns
  up no adjacent topic worth linking.

- No maturity emoji in `src/modules/ROOT/pages/index.adoc` MUST have
  changed.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Pick the target.

    Where the user named an entry, use it. Otherwise scan
    `src/modules/ROOT/pages/` and rank candidates by weakness: short body,
    `// TODO` markers present, few outbound `xref:` links, 🌱 or 🌿 maturity
    in the index. Take the top-ranked entry, and name your runners-up in the
    report so the user can redirect you.

2.  Read the target entry in full.

    Understand its current scope and claims before adding anything.
    Fertilizing deepens the existing idea; it does not widen it into a
    different one.

3.  Research to fill the gaps.

    Identify what is missing: a clearer definition, examples, trade-offs,
    common pitfalls, or context on when and why the concept matters. Address
    each `// TODO` marker in the file — these are the gaps the original
    author knew about.

4.  Find adjacent topics already in the garden.

    Deepening usually surfaces new cross-reference opportunities — related
    patterns, prerequisites, contrasting approaches. Search existing entries
    for concepts that should now be linked, outbound from this entry and
    inbound from those. Note their exact filenames — an AsciiDoc `xref:`
    target must match a real file.

5.  Rewrite the entry.

    Expand the body in place, keeping the original title and filename.
    Remove each `// TODO` marker you resolved. Follow `docs/style-guide.md`,
    wrapping every `xref:` in `*...*`.

6.  Add the cross-references from step 4, in both directions where each
    reads naturally in its host entry's context.

7.  Report what was added, which `// TODO` markers were resolved, which
    links were made, and whether the entry's maturity emoji now looks
    understated.

## Rules

- You MUST NOT change the entry's scope.

  If research reveals the topic really covers two ideas, report that and
  leave the second one out. Smuggling a second concept into a stub trades
  one problem for a worse one.

- You SHOULD resolve `// TODO` markers rather than delete them.

  They are the clearest signal of what the entry's author knew was missing.
  Where a marker cannot be resolved with confidence, leave it in place — an
  unanswered gap is better recorded than silently erased.

- You MUST link rather than duplicate.

  Where a concept is already explained elsewhere, `xref:` to it instead of
  re-explaining it. The value of the garden is in the connections between
  atomic notes, not in self-contained essays.

- You MUST NOT change an entry's maturity emoji in the index.

  Maturity is an editorial judgment the user reserves. Recommend a promotion
  in your report and leave the label as it stands.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- The entry is a redirect stub whose whole body points at another entry.

  Do not fertilize it into a second entry on the same topic. Report it as a
  redundancy to be dropped, with the covering entry named.

- The named target turns out to be substantial already.

  Say so and stop. An established entry wants researching and extending, not
  rescuing, and the two produce noticeably different diffs.
