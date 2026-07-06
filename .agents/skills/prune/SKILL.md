---
name: prune
description: Check whether a single garden entry duplicates an existing page, and if so merge them into one, repointing references and removing the redundant page. Use when the user says "is acid.adoc a duplicate of anything?", "prune this entry", or suspects a page repeats one that already exists.
metadata:
  interactive: no
---

# Prune

**Input**: A single target entry in the garden, to check for duplication against the rest of the garden (eg. "is acid.adoc a duplicate of anything?"). Do not block to ask the user questions. Make your proposed edits and leave them in the Git working tree for the user to decide what to do with them.

**Output**: If the target duplicates an existing page, one surviving page per concept — retitled/expanded if the merge pulled in unique content from the removed page — the removed page deleted, and every `xref:` and index entry that pointed at the removed page repointed to the survivor. If no duplicate is found, a report saying so, with nothing changed.

##  Instructions

1.  **Look for a duplicate of the target.**

    Scan `src/modules/ROOT/pages/` for a page covering the same concept as the target:

    - A filename that is a near-anagram or one-letter-off (eg. `adapative-software-development.adoc` vs `adaptive-software-development.adoc` — a typo'd duplicate).

    - A title (the `=` line) that is a synonym or near-identical phrasing (eg. `acid.adoc` vs `acid-principles.adoc`).

    - An opening paragraph that describes the same concept in different words.

    Present the candidate pair to the user with a one-line reason, and confirm before merging — false positives here (two genuinely distinct concepts with similar names) are costly to get wrong. If nothing matches, report that the target has no duplicate and stop.

2.  **Read both pages in full.**

    Identify the better-written, more complete, or correctly-named page as the survivor. Prefer the page with the correctly spelled filename, more content, more inbound links, and no unresolved `// TODO` markers, in that order of priority. The survivor may be the target or the page it duplicates.

3.  **Merge unique content into the survivor.**

    If the page being removed has any detail, example, or nuance the survivor lacks, fold it into the survivor before deleting anything. Don't silently discard content — a duplicate page often still has one sentence worth keeping.

4.  **Repoint every reference.**

    Grep the whole garden for `xref:<removed-file>.adoc` and replace each with `xref:<survivor-file>.adoc`, keeping the link text sensible in context. Check `index.adoc` too — remove the entry for the deleted page if present, and ensure the survivor's entry is still correctly listed.

5.  **Delete the redundant page.**

    Remove the file once nothing references it.

6.  **Report back.**

    State which page survived, what (if anything) was merged in from the removed page, and every file where a reference was repointed.

##  Rules

-   **One entry at a time.**

    Prune checks a single target entry for duplication. It is not a whole-garden duplicate sweep; run it once per entry of interest.

-   **When in doubt, don't merge.**

    Two pages that look similar but address genuinely distinct concepts (eg. a general pattern vs. a specific implementation of it) should stay separate — link them with `xref:` instead. Prune removes accidental duplication, not legitimately related entries.

-   **The correctly spelled, more complete, or more-linked page wins** as survivor by default.

    Don't let creation date or alphabetical order decide it.

-   **Never delete a file before every reference to it has been repointed.**

    A dangling `xref:` after a prune is worse than the duplicate it replaced.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing are the user's call.

##  Success criteria

-   **No `xref:` anywhere in the garden still points to a deleted file.**

-   **`index.adoc` lists exactly one entry per surviving concept**, not the removed duplicate.

-   **Any unique content from the removed page is either present in the survivor or was confirmed by the user as not worth keeping.**

-   **The user confirmed the merge before deletion** — no page was removed automatically without explicit sign-off.
