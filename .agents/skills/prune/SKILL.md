---
name: prune
description: Find duplicate or near-duplicate entries in the digital garden and merge them into one, redirecting or removing the redundant page. Use when the user says "prune the garden", "check for duplicates", or asks whether two entries cover the same ground.
metadata:
  interactive: yes
---

# Prune

Use this skill to cut back redundant growth: entries that cover the same concept as another entry, usually created by accident (a typo'd filename, a synonym, forgetting an entry already exists).

Do NOT use this skill for broken links, orphaned pages, or stale maturity labels — those are mechanical checks handled by [tend](../tend/SKILL.md). Prune is a semantic judgment call about whether two *different* pages are actually the *same* concept. Do NOT use this skill to split an overgrown entry that covers two concepts — that's the opposite operation, handled by [graft](../graft/SKILL.md).

**Input**: OPTIONAL — a pair of suspected duplicate topics or files named by the user (eg. "are acid.adoc and acid-principles.adoc duplicates?"). If none given, this skill scans the garden for likely duplicate pairs (similar filenames, similar titles, overlapping first paragraphs) and presents candidates for confirmation before merging anything.

**Output**: One surviving page per concept, retitled/expanded if the merge pulled in unique content from the removed page; the removed page deleted; every `xref:` and index entry that pointed at the removed page repointed to the survivor.

## Instructions

1.  **Find duplicate candidates.**

    If the user named a pair, use it directly. Otherwise scan `src/modules/ROOT/pages/` for likely duplicates:

    - Filenames that are near-anagrams or one-letter-off (eg. `adapative-software-development.adoc` vs `adaptive-software-development.adoc` — a typo'd duplicate).
    - Titles (the `=` line) that are synonyms or near-identical phrasing (eg. `acid.adoc` vs `acid-principles.adoc`).
    - Opening paragraphs that describe the same concept in different words.

    Present each candidate pair to the user with a one-line reason, and confirm before merging — false positives here (two genuinely distinct concepts with similar names) are costly to get wrong.

2.  **Read both pages in full.**

    Identify the better-written, more complete, or correctly-named page as the survivor. Prefer the page with the correctly spelled filename, more content, more inbound links, and no unresolved `// TODO` markers, in that order of priority.

3.  **Merge unique content into the survivor.**

    If the page being removed has any detail, example, or nuance the survivor lacks, fold it into the survivor before deleting anything. Don't silently discard content — a duplicate page often still has one sentence worth keeping.

4.  **Repoint every reference.**

    Grep the whole garden for `xref:<removed-file>.adoc` and replace each with `xref:<survivor-file>.adoc`, keeping the link text sensible in context. Check `index.adoc` too — remove the entry for the deleted page if present, and ensure the survivor's entry is still correctly listed.

5.  **Delete the redundant page.**

    Remove the file once nothing references it.

6.  **Report back.**

    State which page survived, what (if anything) was merged in from the removed page, and every file where a reference was repointed.

## Rules

-   **When in doubt, don't merge.** Two pages that look similar but address genuinely distinct concepts (eg. a general pattern vs. a specific implementation of it) should stay separate — link them with `xref:` instead. Prune removes accidental duplication, not legitimately related entries.

-   **The correctly spelled, more complete, or more-linked page wins** as survivor by default — don't let creation date or alphabetical order decide it.

-   **Never delete a file before every reference to it has been repointed.** A dangling `xref:` after a prune is worse than the duplicate it replaced.

-   **Committing is out of scope.** This skill edits and deletes files in the working tree only. Staging, committing, and pushing are the user's call — never run `git commit` or `git push` as part of pruning.

## Success criteria

- **No `xref:` anywhere in the garden still points to a deleted file.**

- **`index.adoc` lists exactly one entry per surviving concept**, not the removed duplicate.

- **Any unique content from the removed page is either present in the survivor or was confirmed by the user as not worth keeping.**

- **The user confirmed every merge before deletion** — no page was removed automatically without explicit sign-off.
