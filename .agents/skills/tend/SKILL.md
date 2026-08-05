---
name: tend
description: >-
  Inspect the digital garden for withering content — broken cross-references,
  fake pseudo-links, orphaned pages missing from the index, and stale maturity
  labels — and report or fix what's found. Use when the user says "tend the
  garden", "check for broken links", or asks for general garden
  maintenance/health checks.
compatibility: requires Read, Grep, Edit
license: CC0-1.0
---

# Tend

Inspect the digital garden for withering content — broken cross-references,
fake pseudo-links, orphaned pages missing from the index, and stale maturity
labels — and report or fix what's found. General garden maintenance and health
checks.

## Input

OPTIONAL — the user may scope it to a single page or section (eg. "tend the
AI topics"); otherwise scan the whole garden. Do not block to ask the user
questions. Make your proposed edits and leave them in the Git working tree
for the user to decide what to do with them.

## Output

A report of findings (broken xrefs, fake links, orphaned pages, stale
labels), followed by fixes applied directly to the affected `.adoc` files
for anything unambiguous. Ambiguous cases are listed for the user to
resolve manually.

This task runs non-interactively to completion. It does not block for user
input. If in doubt about any of the requirements of this task, stop and
print an error message.

## Instructions

1.  Inventory the garden.

    List every `.adoc` file under `src/modules/ROOT/pages/`. This is the
    ground truth for steps 2–4.

2.  Find broken cross-references.

    Grep all pages for `xref:` targets (pattern
    `xref:([a-z0-9-]+\.adoc)`). For each target, confirm the file exists
    in the inventory from step 1. Report any that don't — these are dead
    links pointing to a page that was renamed, removed, or never
    created.

3.  Find fake pseudo-links.

    Some pages contain bracketed bold text that looks like a
    cross-reference but isn't real AsciiDoc xref syntax — eg.
    `*[modular design]*` instead of
    `xref:modular-design.adoc[Modular design]`. Search for this pattern
    (`*[...]*` or `[...]` not preceded by `xref:` or a URL scheme). For
    each match, check whether a real page exists for that topic:

    - If a matching page exists, convert it to a proper `xref:`.

    - If no matching page exists, flag it to the user as a candidate for
      [sow](../sow/SKILL.md) — don't silently create new pages from
      inside tend.

4.  Find orphaned pages.

    Cross-check the inventory from step 1 against every `xref:` target
    listed in `index.adoc`. Any page not listed in the index is orphaned
    — it exists but has no discoverable path from the front page. Report
    orphans for the user to slot into the index (you may propose the
    section, but confirm before editing the index, since placement is a
    judgment call about taxonomy).

5.  Find stale maturity labels.

    Maturity emoji (🌱 Seedling, 🌿 Budding, 🌳 Evergreen, 🍂 Decaying)
    are a judgment call, not something to bulk-rewrite automatically.
    Flag candidates rather than changing labels outright:

    - A 🌱 Seedling page that is substantial, well-linked, and has no
      `// TODO` markers — candidate for promotion to 🌳 Evergreen.

    - A page with a `// TODO` comment, or noticeably thinner than its
      peers, still marked 🌳 Evergreen or 🌿 Budding — candidate for
      demotion to 🌱 Seedling, or a 🍂 Decaying flag if it looks
      abandoned.

    Present these as suggestions; only change the label in `index.adoc`
    if the user confirms.

6.  Apply unambiguous fixes.

    Fix broken xrefs only when the intended target is obvious (eg. an
    exact rename, a clear typo). Convert fake pseudo-links to real
    `xref:` only when a matching page genuinely exists. Leave everything
    else — orphan placement, maturity relabeling, dead links with no
    obvious target — for the user to decide.

7.  Report a summary.

    List what was found, what was fixed automatically, and what needs
    the user's decision, grouped by category (broken xrefs / fake links
    / orphans / stale labels).

## Rules

- Don't invent destinations for dead links.

  If a broken `xref:` has no obvious correct target, report it — don't
  guess and silently repoint it to the wrong page.

- Maturity labels are an editorial judgment, not a mechanical one.

  Surface evidence (TODO markers, length, link density) but let the
  user make the final call.

- Tend doesn't grow content.

  If a fix would mean writing new prose (eg. an orphan needs a
  one-line description in the index, or a fake link needs a target page
  that doesn't exist yet), do the minimum mechanical fix and hand the
  rest to [sow](../sow/SKILL.md) or [fertilize](../fertilize/SKILL.md).

- Do NOT commit your changes.

  Make your edits in the working tree only. Staging, committing, and
  pushing are the user's call.

## Success criteria

- Every `xref:` target in the garden has been checked against the
  actual file inventory, with all mismatches reported.

- Every bracketed pseudo-link has been checked for a matching real
  page, and converted to `xref:` where one exists.

- Every page under `pages/` has been checked against `index.adoc` for
  orphan status.

- No maturity label was changed without explicit user confirmation.

- The final report distinguishes fixes already applied from items
  still needing the user's decision.

## References

None.
