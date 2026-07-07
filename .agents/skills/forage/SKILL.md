---
name: forage
description: >-
  Find topics that are referenced or implied across the garden but don't have
  their own page yet, and produce a prioritized list of candidates for sowing.
  Use when the user says "forage the garden", "what topics are missing?", or
  asks what new entries are worth creating.
metadata:
  interactive: no
---

# Forage

**Input**: OPTIONAL — the user may scope it to a section or topic (eg. "forage
around the AI topics"); otherwise scan the whole garden. Do not block to ask the
user questions. This skill is read-only: it presents its findings for the user
to decide what to act on, rather than sowing anything itself.

**Output**: A prioritized list of candidate topics with no existing page, each
with a frequency count (how many pages mention it) and the files where it
appears, ranked by mention frequency. No files are created or modified — this
skill is read-only.

##  Instructions

1.  **Collect fake pseudo-link mentions.**

    Search all pages under `src/modules/ROOT/pages/` for the `*[text]*`
    pseudo-link pattern (excluding lines inside `//` comments). For each, check
    whether a real page already exists for that topic (exact match or an obvious
    singular/plural or synonym variant). Discard any that do — those are
    [tend](../tend/SKILL.md)'s job to convert to a real `xref:`. Keep the ones
    with no matching page.

2.  **Collect plain unbracketed mentions.**

    Some topics are named in prose without any bracket at all (no fake link, no
    real xref) — eg. a page mentions "service mesh" in passing with no markup.
    These are easy to miss because they don't look like links. Search for
    capitalized or technical-sounding multi-word phrases repeated across
    multiple pages that don't already have a corresponding page or xref. This
    step is necessarily fuzzier than step 1 — favor precision, and don't force a
    match just to pad the list.

3.  **Aggregate and count.**

    Group all candidate topics (from both steps) by normalized name (eg. treat
    "CI/CD" and "CI/CD pipelines" as the same candidate if they clearly refer to
    the same concept). For each, count how many distinct pages mention it and
    list those pages.

4.  **Rank by frequency.**

    Sort candidates by mention count, descending. A topic mentioned across ten
    pages is a stronger signal that the garden needs it than one mentioned once
    in passing.

5.  **Present the list.**

    Show the ranked candidates with their mention counts and source pages. Ask
    the user which ones (if any) to send to [sow](../sow/SKILL.md). Don't sow
    anything automatically — this skill only forages, it doesn't plant.

##  Rules

-   **Frequency is a signal, not a verdict.**

    A topic mentioned many times might still be too narrow, too broad, or
    already covered under a different name — use judgment, and flag ambiguous
    cases rather than ranking them as if frequency settles it.

-   **Don't duplicate tend's job.**

    If a `*[text]*` pseudo-link actually does have a matching real page, that's
    a mechanical fix for [tend](../tend/SKILL.md), not a foraging find. Forage
    is specifically about the gaps where nothing exists yet.

-   **This skill never writes to the garden.**

    It's pure discovery — no file is created, edited, or deleted. Even confirmed
    candidates are only ever handed to [sow](../sow/SKILL.md) as a follow-up,
    not actioned inline.

##  Success criteria

-   **Every candidate listed has no existing matching page** — checked against
    the actual file inventory in `src/modules/ROOT/pages/`, not assumed.

-   **Each candidate's mention count and source pages are accurate** and
    verifiable by re-running the same grep.

-   **The list is ranked by frequency**, not presented as an unordered dump.

-   **No file in the garden was created, edited, or deleted** by running this
    skill.
