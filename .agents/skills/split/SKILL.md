---
name: split
description: >-
  Split an overgrown garden entry that has drifted into covering two or more
  distinct concepts back into separate atomic pages, cross-linked together. Use
  when the user says "split this entry", "split X into separate pages", or
  notices a page covering more than one idea.
metadata:
  interactive: no
---

# Split

**Input**: REQUIRED — a target page named by the user (eg. "split
event-driven-architecture.adoc — it's covering both event sourcing and CQRS").
Do not block to ask the user questions. Make your proposed edits and leave them
in the Git working tree for the user to decide what to do with them.

**Output**: The original page narrowed back to its core concept, one or more new
`.adoc` pages for the concepts that were split out, all of them cross-linked to
each other, and the new pages added to `index.adoc` and `nav.adoc`.

##  Instructions

1.  **Read the target page in full.**

    Identify the distinct concepts it currently covers. A genuine split
    candidate has sections that could each stand alone as a self-contained
    entry, not just sub-points of one idea.

2.  **Propose the split.**

    Name the resulting pages: what stays under the original title, and what
    becomes a new page for each split-out concept. Present this to the user
    before editing — splitting is a structural decision the original entry's
    title and scope depend on, and should be agreed before content moves.

3.  **Check for collisions.**

    Before creating any new page, check it doesn't already duplicate an existing
    entry elsewhere in the garden (the same failure mode
    [prune](../prune/SKILL.md) cleans up). If one already exists, merge the
    split-out content into that page instead of creating a new one.

4.  **Create the new page(s).**

    For each split-out concept, create `src/modules/ROOT/pages/<topic>.adoc`
    following the garden's atomic-entry conventions (single `=` title, focused
    body, `xref:` outward rather than re-explaining). Carry over the relevant
    content from the original, rewritten to stand alone rather than assuming the
    context of the rest of the original page.

5.  **Narrow the original.**

    Remove the split-out sections from the original page, leaving it focused on
    its core concept. Add an `xref:` from the original to each new page where
    the relationship is natural (eg. "see also").

6.  **Cross-link the new pages.**

    If the split-out concepts relate to each other as well as to the original,
    link them to one another too.

7.  **Update the index.**

    Add each new page to `index.adoc` in its correct alphabetical section,
    marked 🌱 Seedling (it's new content, even though it originated from older
    material). Leave the original's existing maturity label as-is unless the
    narrowing changes how complete it looks — propose a change rather than
    applying one silently.

8.  **Update the nav.**

    Add each new page to `src/modules/ROOT/nav.adoc`, in the same alphabetical
    position it occupies in `index.adoc`. Without this, the new page has no
    ancestry and renders with no breadcrumb trail.

9.  **Report back.**

    List the new files created, what moved from the original into each, and
    every cross-link added.

##  Rules

-   **Confirm the split before editing.**

    Unlike tend's mechanical fixes, a split changes the meaning and boundaries
    of existing content — get the user's agreement on the proposed split before
    moving any text.

-   **Check for an existing page first.**

    A split-out concept might already have its own entry elsewhere in the
    garden; don't create a duplicate that [prune](../prune/SKILL.md) will later
    have to clean up.

-   **Rewrite for standalone reading.**

    Content lifted out of the original page often refers back to it implicitly
    ("as mentioned above"). Rewrite those references as explicit `xref:` links
    or remove them — the new page must be self-contained.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing
    are the user's call.

##  Success criteria

-   **The original page covers exactly one concept** after the split.

-   **Each new page is self-contained** — readable without having read the
    original first.

-   **All new pages are listed in `index.adoc` and `nav.adoc`.**

-   **No new page duplicates an existing entry** — checked against the garden
    before creation.

-   **The user confirmed the split plan before any content was moved.**
