---
name: entwine
description: Find existing garden pages that are related but not cross-referenced, and add the missing xref links between them. Use when the user says "entwine related topics in the garden", "find missing cross-references", or asks whether related entries are properly linked together.
metadata:
  interactive: no
---

# Entwine

**Input**: OPTIONAL — a page or topic to focus on (eg. "entwine event-sourcing.adoc with its neighbors"). If none given, scan the whole garden for unlinked-but-related pairs and propose a batch of candidates. Do not block to ask the user questions. Make your proposed edits and leave them in the Git working tree for the user to decide what to do with them.

**Output**: New `xref:` links added to existing pages, connecting concepts that are related but were previously isolated from each other. No new pages, no content rewrites beyond inserting a link (and, where natural, a short clause introducing it).

##  Instructions

1.  **Build a map of existing concepts.**

    List every page under `src/modules/ROOT/pages/`, using its title and opening paragraph as a summary of what it covers.

2.  **Find related-but-unlinked pairs.**

    For each page (or just the one named by the user), look for other pages that:

    - Share a category or parent in `index.adoc` (eg. both filed under the same "tent pole" topic).

    - Mention the same concept by name in prose without an `xref:` (this overlaps with what [tend](../tend/SKILL.md) catches as a *fake* pseudo-link — if the mention is already bracketed as `*[text]*`, that's tend's job; entwine looks for plain, unbracketed mentions and genuinely missing connections that neither page currently gestures at).

    - Are natural neighbors by domain knowledge even without a textual hint (eg. `circuit-breaker.adoc` and `retry.adoc` both belong to resilience patterns, and a reader of one likely wants the other).

    Favor precision over volume — a wrong or strained link is worse than a missing one.

3.  **Propose the batch.**

    Present candidate pairs to the user before editing: which two pages, and a one-line reason they're related. Confirm before making changes, especially for less obvious pairs.

4.  **Add the links.**

    For each confirmed pair, add an `xref:` in at least one direction — ideally both, where the relationship reads naturally in each page's context. Insert it where it fits the existing prose; don't bolt on an orphaned "see also" line if a more natural spot exists in an existing sentence.

5.  **Report back.**

    List every link added, with the two files and a one-line reason for the connection.

##  Rules

-   **Precision over volume.**

    A handful of well-justified links is better than dozens of tenuous ones. If the relationship needs a paragraph to justify, it's too thin to link.

-   **Don't link everything to everything.**

    Hub pages (eg. `architecture-and-design.adoc`, `computer-science.adoc`) already aggregate many topics by design — entwine is about finding missing *sibling* connections, not adding redundant links back to a hub that already lists both pages.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing are the user's call.

##  Success criteria

-   **Every link added has a one-line justification** the user can sanity-check.

-   **No link was added without the user confirming the batch** it belonged to.

-   **No new pages were created** and no existing page's scope changed — only links were added.

-   **All new `xref:` targets resolve** to real files in `src/modules/ROOT/pages/`.
