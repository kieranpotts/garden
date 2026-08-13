---
name: forage
description: >-
  Find topics referenced or implied in one target entry that have no entry of
  their own, and rank them as candidates worth planting. Use this skill when the
  user says something like "forage event-sourcing.adoc", "what topics are
  missing from this page?", or asks to forage around a particular entry. Do not
  use it to create or edit anything — it is read-only.
compatibility: requires Read, Glob, Grep
license: CC0-1.0
---

# Forage

Find topics that are referenced or implied in a single target entry but have no
entry of their own, and produce a ranked list of candidates worth planting.
Foraging is read-only: it presents its findings and plants nothing.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename. Foraging searches this entry only.

## Success criteria

- Every candidate listed MUST be drawn from the target entry — a topic it
  names or clearly implies — and MUST have no matching entry, checked against
  the actual file inventory under `src/modules/ROOT/pages/` rather than
  assumed.

- Each candidate's mention count and the passages that surfaced it MUST be
  accurate, and reproducible by re-running the same search against the
  target entry.

- The list MUST be ranked by the strength of the signal in the target entry
  (how central the topic is to the entry's subject, then how often it is
  named), not presented as an unordered dump.

- Every candidate whose scope is doubtful — too narrow, too broad, or
  possibly covered under another name — MUST be flagged as such rather than
  ranked as though frequency settled it.

- No file in the repository MUST have been created, edited, or deleted.

## Instructions

1.  Read the target entry in full. Understand its subject and the concepts it
    names, so the candidates you surface are things the entry genuinely
    relies on rather than passing mentions of no consequence.

2.  Inventory the garden. List every `.adoc` file under
    `src/modules/ROOT/pages/`, with its `=` title. This is the ground truth
    for deciding what already has an entry, and the target entry is one of
    them.

3.  Collect bracketed markers from the target entry. Search it for the
    `*[text]*` pattern, ignoring lines inside `//` comments. This is the
    garden's convention for naming a topic that has no entry yet. Discard any
    whose term matches an entry in the inventory — including an obvious
    synonym or singular/plural variant — since those are broken markup for a
    structural pass to convert, not gaps. Keep the rest.

4.  Collect plain mentions from the target entry. Some topics are named in
    prose with no markup at all, which makes them easy to miss. Search the
    entry for technical multi-word phrases that have neither a matching entry
    nor an `xref:`. This step is fuzzier than step 3, so favor precision and
    do not force a match to pad the list.

5.  Aggregate and count. Group the candidates from both steps by normalized
    name, treating variants such as "CI/CD" and "CI/CD pipelines" as one
    candidate where they clearly mean the same thing. For each, record the
    passages in the target entry that surfaced it.

6.  Rank by the strength of the signal in the target entry. A topic central
    to the entry's subject, or named several times within it, is a stronger
    candidate than one mentioned once in passing.

7.  Present the ranked candidates with their supporting passages from the
    target entry, with the doubtful ones marked. Say which look worth
    planting, and leave the decision to the user.

## Rules

- Frequency and centrality MUST be treated as a signal, not a verdict. A
  topic named many times in the entry may still be too narrow, too broad, or
  already covered under another name. Flag the ambiguous cases rather than
  letting the ranking imply a decision the count cannot support.

- A bracketed marker with a matching entry MUST NOT be listed as a
  candidate. That is broken markup for a structural pass to convert into a
  real `xref:`. Foraging is specifically about the gaps where nothing exists
  yet, and mixing the two makes both lists less useful.

- You MUST search only the target entry for candidates. Foraging across the
  whole garden produces a diff of findings too large to act on and loses the
  single-entry focus every skill keeps. To forage several entries, run the
  skill once per entry, or delegate each to a sub-agent.

- You MUST NOT create, edit, or delete any file. Foraging is pure discovery.
  Even a candidate you are certain about is reported for the user to act on,
  never planted inline.

## Edge cases

- No candidates are found. Report an empty list and say so. An entry with no
  bracketed markers and no recurring unlinked mentions has no detectable
  gaps — either it is thorough, or its references are too thinly marked for
  plain mentions to surface, which is itself a finding worth reporting.

- The target entry is a stub with too little content to forage from. Say so
  and stop. Foraging a nearly empty entry produces noise; the entry wants
  fertilizing first.