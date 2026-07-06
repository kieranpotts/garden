---
name: sow
description: Research a new topic and plant it as a new entry in the digital garden, cross-referenced to relevant adjacent topics. Use when the user says "sow a new entry for X", "plant a page on X", or asks to add a new topic to the garden.
metadata:
  interactive: no
---

# Sow

**Input**: REQUIRED — a topic name or short description, supplied by the user (eg. "sow an entry for event sourcing"). If the topic is ambiguous or could collide with an existing entry, confirm scope and exact title before writing. Do not block to ask the user questions. Make your proposed edits and leave them in the Git working tree for the user to decide what to do with them.

**Output**: A new `.adoc` file under `src/modules/ROOT/pages/`, self-contained and focused on a single idea, cross-referenced from and to relevant adjacent entries, and listed on `src/modules/ROOT/pages/index.adoc` under the correct alphabetical section (and "Hot topics" if applicable).

##  Instructions

1.  **Check for an existing entry first.**

    Search `src/modules/ROOT/pages/` for a file already covering this topic (by filename and by grepping page titles). If one exists, stop and tell the user — point them to [fertilize](../fertilize/SKILL.md) instead of creating a duplicate.

2.  **Research the topic.**

    Gather enough understanding to write an accurate, concise explanation — what the concept is, why it matters, and how it relates to neighboring concepts already in the garden. Prefer a small number of reliable sources over breadth. This is a knowledgebase entry, not a survey paper.

3.  **Find adjacent topics already in the garden.**

    Search existing pages for related concepts (eg. broader categories, sibling techniques, prerequisites). These become the entry's outbound `xref:` links. Note their exact filenames — AsciiDoc `xref:` targets must match real files.

4.  **Write the entry.**

    Create `src/modules/ROOT/pages/<topic-kebab-case>.adoc`, named after the topic in kebab-case (eg. `event-sourcing.adoc`). Follow the structure of existing entries:

    - A single `=` title line matching the topic name.

    - A short, focused explanation — self-contained, but linking out via `xref:` rather than re-explaining concepts that already have their own page.

    - A "See also" line or section if there are related topics that don't fit naturally inline.

    Keep it atomic: one idea or concept per file. If the research surfaces a second distinct concept, that's a separate entry, not a section of this one.

5.  **Link it back in.**

    For each adjacent topic identified in step 3, check whether that page already references the new topic. If it's a natural fit, add an inbound `xref:` from that page too — the garden is most useful when paths run in both directions, not just outward from the new page.

6.  **List it on the index.**

    Add a line to `src/modules/ROOT/pages/index.adoc`, in the correct alphabetical sub-section under "All topics", following the existing `*xref:<file>.adoc[Title]* <emoji>` pattern. Mark new entries 🌱 (Seedling). If the topic is something the user is actively researching right now, also add it under "Hot topics".

7.  **Report back.**

    Tell the user the file path created, the entries it links to/from, and where it landed in the index.

##  Rules

-   **Prefer linking over duplicating.**

    If a concept is already explained on another page, link to it with `xref:` instead of re-explaining it. The value of the garden comes from connections between atomic notes, not self-contained essays.

-   **One file, one concept.**

    If a topic naturally splits into two or more distinct ideas, sow separate entries and cross-link them, rather than producing one long page.

-   **New entries start as 🌱 Seedling.**

    Don't mark a freshly sown entry 🌳 Evergreen — maturity is earned through later tending and fertilizing, not assigned at creation.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing are the user's call.

##  Success criteria

-   **The new file exists** at `src/modules/ROOT/pages/<topic>.adoc`, with a single `=` title and a non-empty body.

-   **It is listed in `index.adoc`** under the correct alphabetical section, with the 🌱 emoji.

-   **All `xref:` targets resolve** — every `xref:foo.adoc[...]` added (in the new page or in pages linking back to it) corresponds to a real file in `src/modules/ROOT/pages/`.

-   **At least one adjacent topic is linked**, unless research genuinely turns up no related entries in the garden yet.
