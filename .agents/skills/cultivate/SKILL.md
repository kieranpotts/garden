---
name: cultivate
description: >-
  Review one entry against the garden's style guide — sentence-case titles,
  prose style, dash and colon usage, bold-text rules, admonition usage — then
  apply the mechanical fixes and flag the judgment calls. Use when the user says
  "cultivate agent.adoc", "check style on this entry", or asks for a
  style-guide pass over one page. Do not use it to change what an entry says.
compatibility: requires Read, Edit
license: CC0-1.0
---

# Cultivate

Review a single garden entry against `docs/style-guide.md` and bring it into
conformance. Unambiguous mechanical fixes are applied directly; anything that
would change meaning is flagged for the user instead.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single existing file under
  `src/modules/ROOT/pages/`, named by the user, eg. "cultivate
  resilience.adoc". Accept a topic name too, and resolve it to the file whose
  `=` title matches.

## Success criteria

- The style guide MUST have been read in this session, before the entry was
  reviewed.

- The target entry MUST have been checked against every section of the style
  guide.

- Every unambiguous mechanical violation MUST have been fixed in place: dash
  character, colon usage, heading case, stray bold, unbolded `xref:`.

- Every sentence-level rewrite and every bolding judgment call MUST have been
  reported rather than applied.

- No `xref:` target, entry title, filename, or index listing MAY have
  changed. Cultivating changes how prose is written, never what it says or
  where it points.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read [`docs/style-guide.md`](../../../docs/style-guide.md) in full.

    Do not work from a remembered or cached understanding of its rules. The
    guide changes, and a pass run against a stale copy quietly enforces the
    wrong conventions.

2.  Check the entry against the guide, section by section:

    - Titles and headings — sentence case, acronyms spelled out on first
      use, no over-structuring of a short entry. A formal proper noun keeps
      its established capitalization, eg. "Developer Certificate of Origin",
      "Capability Maturity Model".

    - Written style — prose paragraphs where prose belongs, simple
      sentences, no semicolons in sentences (semicolons within a bullet list
      chaining items are fine), en dash for a sentence-level pause, colons
      only before lists, colons rather than hyphens separating a list term
      from its description.

    - Bold text — only five things are ever bold: an `xref:`
      cross-reference, a bracketed term marking a topic not yet planted, a
      glossary-style list-term lead-in (`*Term*: Description.`), a term being
      defined for the first time in running prose, and a table-cell header label
      (`|*Term*`). Check both directions: every `xref:` is bold, and nothing else
      is bold unless it fits one of the other four.

    - Titles — book names and other publication titles are in italics
      (`_Title_`), not bold.

    - Admonitions — used sparingly, and only for a genuinely secondary
      aside.

    - `// TODO` comments are legitimate, not style violations.

3.  Apply the mechanical fixes directly:

    - A hyphen or em dash used as a sentence-level pause becomes an en dash.

    - A hyphen or em dash separating a list term from its description
      becomes a colon, with the description capitalized as its own sentence.

    - A colon followed by prose rather than a list becomes two sentences.

    - A wrong-case heading or title becomes sentence case, respecting the
      formal proper noun exception.

    - An `xref:` that is not wrapped in `*...*` gets wrapped. Check every
      occurrence, not just the first in the entry.

    - A book or publication title set in bold becomes italics (`_Title_`).

    - Bold markup fitting none of the five accepted conventions is unbolded.

4.  Report, rather than apply, the judgment calls:

    - A long or tangled sentence needing a rewrite. Propose the rewrite;
      rephrasing moves meaning in a way punctuation does not.

    - An entry grown past a few short paragraphs and looking like it now
      covers more than one concept.

    - Whether a bolded term is a not-yet-planted topic marker, a first-use
      definition, or simply stray bold.

    - Whether a capitalized heading is a formal proper noun or just a
      descriptive phrase that reads like one.

5.  Report what was checked, what was fixed, and what is flagged, grouped by
    style-guide section.

## Rules

- You MUST cultivate one entry at a time.

  A garden-wide style sweep produces a diff too large to review, which
  defeats the working tree as a review gate. Run the skill once per entry.

- The style guide MUST be the only source of style authority.

  Do not enforce a preference that is not written in `docs/style-guide.md`.
  Where you think the guide is missing a rule, say so in the report rather
  than applying an unwritten one.

- You MUST NOT repair structural defects.

  Broken cross-references, fake pseudo-links, orphans, and maturity emoji
  belong to a structural pass. Mention any you notice, and leave them.

- You MUST NOT change content.

  Cultivating neither expands a thin entry nor breaks up an overgrown one.
  It changes only how the existing prose is written.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- You cannot tell whether a term is a formal proper noun.

  Leave the capitalization as it stands and flag it. A wrongly
  de-capitalized standard or framework name is a factual error, which is
  worse than an inconsistent heading.

- A mechanical fix would change the sense of a sentence.

  It is then not mechanical. Move it to the flagged list, with the proposed
  wording, and leave the text alone.
