---
name: forage
description: >-
  Find topics referenced or implied across the garden that have no entry of
  their own, and rank them as candidates worth planting. Use this skill when
  the user says something like "forage the garden", "what topics are missing?",
  or asks to forage around a particular subject area. Do not use it to create
  or edit anything — it is read-only.
compatibility: requires Read, Glob, Grep
license: CC0-1.0
---

# Forage

Find topics that are referenced or implied across the garden but have no entry
of their own, and produce a ranked list of candidates worth planting. Foraging
is read-only: it presents its findings and plants nothing.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Scope — OPTIONAL.** A subset of the garden to search, eg. "forage around
  the AI topics". Defaults to every file under `src/modules/ROOT/pages/`.

## Success criteria

- Every candidate listed MUST have no matching entry, checked against the
  actual file inventory under `src/modules/ROOT/pages/` rather than assumed.

- Each candidate's mention count and source files MUST be accurate, and
  reproducible by re-running the same search.

- The list MUST be ranked by mention count, not presented as an unordered
  dump.

- Every candidate whose scope is doubtful — too narrow, too broad, or
  possibly covered under another name — MUST be flagged as such rather than
  ranked as though frequency settled it.

- No file in the repository MUST have been created, edited, or deleted.

## Instructions

1.  Inventory the garden. List every `.adoc` file under `src/modules/ROOT/pages/`, 
    with its `=` title. This is the ground truth for deciding what already has 
    an entry.

2.  Collect bracketed markers. Search every entry for the `*[text]*` pattern,
    ignoring lines inside `//` comments. This is the garden's convention for 
    naming a topic that has no entry yet. Discard any whose term matches an 
    entry in the inventory — including an obvious synonym or singular/plural 
    variant — since those are broken markup for a structural pass to convert, 
    not gaps. Keep the rest.

3.  Collect plain mentions. Some topics are named in prose with no markup at all, 
    which makes them easy to miss. Search for technical multi-word phrases 
    repeated across several entries that have neither a matching entry nor an 
    `xref:`. This step is fuzzier than step 2, so favor precision and do not 
    force a match to pad the list.

4.  Aggregate and count. Group the candidates from both steps by normalized name, 
    treating variants such as "CI/CD" and "CI/CD pipelines" as one candidate 
    where they clearly mean the same thing. For each, count the distinct entries
    mentioning it and record which they are.

5.  Rank by mention count, descending. A topic named across ten entries is a
    stronger signal that the garden needs it than one named once in passing.

6.  Present the ranked candidates with their counts and source entries, with
    the doubtful ones marked. Say which look worth planting, and leave the
    decision to the user.

## Rules

- Frequency MUST be treated as a signal, not a verdict. A topic named many times 
  may still be too narrow, too broad, or already covered under another name. 
  Flag the ambiguous cases rather than letting the ranking imply a decision the 
  count cannot support.

- A bracketed marker with a matching entry MUST NOT be listed as a
  candidate. That is broken markup for a structural pass to convert into a real
  `xref:`. Foraging is specifically about the gaps where nothing exists yet,
  and mixing the two makes both lists less useful.

- You MUST NOT create, edit, or delete any file. Foraging is pure discovery. 
  Even a candidate you are certain about is reported for the user to act on, 
  never planted inline.

## Edge cases

- No candidates are found. Report an empty list and say so. A garden with no 
  bracketed markers and no recurring unlinked mentions has no detectable gaps — 
  either it is complete or its entries are too thinly cross-referenced for plain 
  mentions to surface, which is itself a finding worth reporting.
