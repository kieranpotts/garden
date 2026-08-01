---
name: graft
description: >-
  Merge two or more related-but-distinct garden entries into a single broader
  page, cross-links repointed and the absorbed pages removed. Use when the user
  says "graft these entries", "merge X and Y into one page", or notices several
  thin pages that would read better as one concept.
metadata:
  interactive: no
  preferred_model: ollama/PROSE_DEEP
---

# Graft

Merge two or more related-but-distinct garden entries into a single broader
page, with cross-links repointed and the absorbed pages removed. The survivor
carries the distinct content from each source, arranged as coherent sections
rather than concatenated verbatim.

## Input

REQUIRED — two or more target pages named by the user (eg. "graft
retry.adoc, backoff.adoc and jitter.adoc into one retry-strategies page").
Do not block to ask the user questions. Make your proposed edits and leave
them in the Git working tree for the user to decide what to do with them.

## Output

One surviving page covering the combined concept, its sections carrying over
the distinct content from each source page; the absorbed pages removed;
every `xref:` and `index.adoc` entry that pointed at a removed page
repointed to the survivor.

This task runs non-interactively to completion. It does not block for user
input. If in doubt about any of the requirements of this task, stop and
print an error message.

## Instructions

1.  Read all the target pages in full.

    Confirm they're related-but-distinct, each contributing content the
    others don't. If one is already fully covered by another and adds
    nothing, don't graft it — hand that page off to
    [prune](../prune/SKILL.md) to be dropped instead. Graft is for
    combining distinct content, not clearing out redundancy.

2.  Propose the merge.

    Decide the survivor: either promote one existing page to the
    broader title, or create a new page that absorbs all the sources.
    Name the resulting title and sketch how each source page's content
    maps onto sections of the merged page. Present this to the user
    before editing — a graft changes the title and scope of existing
    content, and should be agreed before anything moves.

3.  Build the merged page.

    Carry the distinct content from each source into the survivor,
    arranged as coherent sections rather than concatenated verbatim.
    Rewrite transitions so it reads as one entry, not stitched
    fragments. Follow the garden's atomic-entry conventions (single `=`
    title, focused body, `xref:` outward). If the survivor is a newly
    created page, create `src/modules/ROOT/pages/<topic>.adoc`; if it's
    a promoted existing page, edit it in place and retitle as agreed.

4.  Repoint every reference.

    Grep the whole garden for `xref:<absorbed-file>.adoc` for each
    removed page and replace with `xref:<survivor-file>.adoc`, keeping
    the link text sensible in context. Where several old links now
    point at the same survivor from one page, collapse duplicates.

5.  Remove the absorbed pages.

    Delete each source page that was folded into the survivor, once
    nothing references it. If the survivor is a promoted existing page,
    only the other sources are deleted.

6.  Update the index.

    Remove the absorbed pages' entries from `index.adoc`. Ensure the
    survivor is listed once under its final title, in the correct
    alphabetical section. Propose a maturity label that reflects the
    merged page's completeness rather than silently keeping the highest
    or lowest of the sources.

7.  Report back.

    State which page survived (or was created), what content came from
    each source, every reference repointed, and every page deleted.

## Rules

- Confirm the merge before editing.

  A graft changes the meaning and boundaries of existing content and
  deletes pages — get the user's agreement on the survivor, title, and
  structure before moving any text.

- Graft is not prune.

  If a page's topic is already covered by another and adds nothing,
  this is the wrong skill — [prune](../prune/SKILL.md) drops the
  redundant page and redirects its links. Graft only combines pages
  that each contribute distinct content to the broader concept.

- Don't discard distinct content.

  Every source page contributes something the others don't — that's
  why it's a graft and not a prune. Confirm with the user before
  dropping any section, don't lose it silently in the merge.

- Never delete a page before every reference to it has been repointed.

  A dangling `xref:` after a graft is worse than the fragmentation it
  replaced.

- Do NOT commit your changes.

  Make your edits in the working tree only. Staging, committing, and
  pushing are the user's call.

## Success criteria

- One surviving page covers the combined concept, reading as a single
  coherent entry rather than stitched fragments.

- No `xref:` anywhere in the garden still points to a removed source
  page.

- `index.adoc` lists the survivor once under its final title, with
  the absorbed pages' entries removed.

- Distinct content from every source is present in the survivor, or
  was confirmed by the user as not worth keeping.

- The user confirmed the merge plan before any content was moved or
  any page deleted.

## References

None.
