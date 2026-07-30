---
name: prune
description: >-
  Drop a garden entry whose topic is already well-covered by another page —
  deleting it and redirecting its inbound links to the covering page. Use when
  the user says "prune acid.adoc", "this entry is already covered by X, drop
  it", or suspects a page is redundant.
metadata:
  interactive: no
---

# Prune

Drop a garden entry whose topic is already well-covered by another page —
deleting it and redirecting its inbound links to the covering page. The
covering page survives; the redundant one goes.

## Input

A single target entry suspected of being redundant — its topic already
covered by another page. The user may also name the covering page (eg.
"acid.adoc is covered by acid-principles.adoc, drop it"). Do not block to
ask the user questions. Make your proposed edits and leave them in the Git
working tree for the user to decide what to do with them.

## Output

The redundant target page deleted, with every `xref:` and `index.adoc`
entry that pointed at it repointed to the covering page. If the target
turns out to carry content the covering page lacks, nothing is deleted —
it is reported as a graft or keep-and-link candidate instead.

This task runs non-interactively to completion. It does not block for
user input. If in doubt about any of the requirements of this task, stop
and print an error message.

## Instructions

1.  Identify the covering page.

    Confirm the target's topic is already well-covered by another
    existing page. If the user named that page, use it. Otherwise
    search `src/modules/ROOT/pages/` for the page that covers the same
    concept (similar title or filename, overlapping content). If no
    page covers it, stop — this isn't a prune; the topic is unique and
    should be kept.

2.  Confirm the target is genuinely redundant.

    Read both pages in full. The target is a prune candidate only if
    the covering page already says everything the target does. If the
    target carries substantial unique content — examples, nuance, a
    distinct angle — then it isn't really covered: stop and hand off
    to [graft](../graft/SKILL.md) (to combine the distinct content) or
    leave both and suggest [entwine](../entwine/SKILL.md) (to link
    them). Present the candidate to the user with a one-line reason
    and confirm before deleting anything — a wrong drop loses content.

3.  Salvage any stray detail (optional).

    If the target has only a small scrap the covering page lacks (a
    single sentence, one example), offer to fold it into the covering
    page before deletion. Anything larger than a scrap means the topic
    wasn't really covered — reclassify as a graft.

4.  Repoint every reference.

    Grep the whole garden for `xref:<target-file>.adoc` and replace
    each with `xref:<covering-file>.adoc`, keeping the link text
    sensible in context. Check `index.adoc` too — remove the target's
    entry and ensure the covering page's entry stays correct.

5.  Delete the redundant page.

    Remove the file once nothing references it.

6.  Report back.

    State which page was dropped, which page now covers it, any scrap
    salvaged, and every file where a reference was repointed.

## Rules

- One entry at a time.

  Prune drops a single redundant target. It is not a whole-garden
  duplicate sweep; run it once per entry of interest.

- Drop, don't merge.

  Prune removes a page whose topic another page already covers. If
  the two pages each carry distinct content that should be combined,
  that's [graft](../graft/SKILL.md), not prune — hand it off rather
  than merging here.

- The covering page survives, the redundant one goes.

  Prune keeps the page that already covers the topic and deletes the
  one that adds nothing. If the named target turns out to be the
  fuller page, don't prune it — flag that the other page is the
  redundant one and confirm the direction with the user.

- When in doubt, don't drop.

  If you're unsure the target is genuinely redundant, keep it and
  link the two with `xref:` ([entwine](../entwine/SKILL.md)) instead.
  Deleting a page that wasn't really covered loses content; a
  redundant page left in place is harmless by comparison.

- Never delete a file before every reference to it has been repointed.

  A dangling `xref:` after a prune is worse than the redundant page it
  replaced.

- Do NOT commit your changes.

  Make your edits in the working tree only. Staging, committing, and
  pushing are the user's call.

## Success criteria

- The dropped page's topic is genuinely covered by the surviving
  page — nothing unique was lost without the user's sign-off.

- No `xref:` anywhere in the garden still points to the deleted file.

- `index.adoc` no longer lists the dropped page, and the covering
  page's entry is intact.

- The user confirmed the drop before deletion — no page was removed
  automatically.

## References

None.
