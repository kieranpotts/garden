---
name: fertilize
description: >-
  Expand a thin stub entry in the digital garden into a fuller page, without
  changing its scope. Use when the user says "fertilize X", "this entry needs
  more growth", "expand the stub on X", or asks to flesh out a
  short/underdeveloped garden page.
compatibility: requires Read, Grep, Edit, WebSearch, WebFetch
license: CC0-1.0
---

# Fertilize

Expand a thin stub entry in the digital garden into a fuller page, without
changing its scope. Fertilize grows the existing plant — it deepens the entry's
explanation, resolves flagged gaps, and adds cross-references, but doesn't
widen it into a different concept.

## Input

OPTIONAL — a topic or file the user wants expanded (eg. "fertilize
abstraction.adoc"). If no target is given, scan the garden and recommend the
weakest stub (shortest body, most `// TODO` markers, fewest outbound links).
Do not block to ask the user questions. Make your proposed edits and leave
them in the Git working tree for the user to decide what to do with them.

## Output

The target `.adoc` file rewritten with a fuller explanation and more
cross-references, with its maturity label in `index.adoc` updated if the
expansion now qualifies it for promotion (eg. 🌱 Seedling → 🌳 Evergreen).

This task runs non-interactively to completion. It does not block for user
input. If in doubt about any of the requirements of this task, stop and
print an error message.

## Instructions

1.  Pick the target.

    If the user named a topic or file, use it directly. Otherwise,
    scan `src/modules/ROOT/pages/` for the weakest candidates: short
    body length, presence of `// TODO` comments, low outbound `xref:`
    count, or 🌱/🌿 maturity in `index.adoc`. Rank a handful and
    present the top pick to the user with a one-line reason, then wait
    for confirmation before editing.

2.  Read the existing entry in full.

    Understand its current scope and claims before adding anything —
    fertilizing should deepen the existing idea, not widen it into a
    different one.

3.  Research to fill the gaps.

    Identify what's missing: a clearer definition, examples,
    trade-offs, common pitfalls, or context on when/why the concept
    matters. Resolve any `// TODO` markers in the file — these mark
    known gaps the original author flagged.

4.  Find additional adjacent topics.

    As content deepens, new cross-reference opportunities usually
    surface (related patterns, prerequisites, contrasting approaches).
    Search the garden for pages that should now be linked, both
    outbound from this entry and inbound from those pages.

5.  Rewrite the entry.

    Expand the body in place. Keep it focused on the original topic —
    fertilize grows the existing plant, it doesn't bolt a different one
    onto it. Remove resolved `// TODO` markers. Preserve the existing
    title and filename.

6.  Re-link.

    Add new `xref:` links found in step 4, in both directions where
    it's a natural fit.

7.  Reconsider the maturity label.

    If the expanded entry is now substantial, accurate, and
    well-linked, propose promoting its emoji in `index.adoc` (eg.
    🌱 → 🌳). Confirm with the user before changing it — maturity is
    an editorial call.

8.  Report back.

    Summarize what was added, which `// TODO` markers were resolved,
    new links made, and whether the maturity label changed.

## Rules

- Don't change scope.

  If research reveals the topic should really be split into two
  entries, stop and suggest [sow](../sow/SKILL.md) for the new one
  rather than smuggling a second concept into this page.

- Resolve, don't ignore, `// TODO` markers.

  They're the clearest signal of what the page's original author knew
  was missing. If a `// TODO` can't be resolved with confidence, leave
  it in place rather than deleting it unanswered.

- Maturity promotion needs confirmation.

  Never bump a maturity emoji in `index.adoc` without the user
  agreeing the expanded page has earned it.

- Do NOT commit your changes.

  Make your edits in the working tree only. Staging, committing, and
  pushing are the user's call.

## Success criteria

- The target file's scope is unchanged — same topic, same title, same
  filename, just fuller.

- All `// TODO` markers in the target file are either resolved and
  removed, or deliberately left with reasoning given to the user.

- At least one new cross-reference was considered, even if research
  turns up none worth adding.

- No maturity label changed without explicit user confirmation.

## References

None.
