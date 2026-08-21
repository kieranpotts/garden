---
name: tidy
description: >-
  Review one entry against the garden's style guide — sentence-case titles,
  prose style, dash and colon usage, bold-text rules, xref and external-link
  form, line wraps, admonition usage — then apply the mechanical fixes and
  flag the judgment calls. Use this skill when the user says something like
  "tidy resilience.adoc", "check style on this entry", or asks for a
  style-guide pass over one page. Do not use it to change what an entry says.
compatibility: requires Read, Edit, Bash
license: CC0-1.0
---

# Tidy

Review a single garden entry against `docs/style-guide.md` and bring it into
conformance. Unambiguous mechanical fixes are applied directly. Anything that
would change meaning is flagged for the user instead.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename.

## Success criteria

- The style guide MUST have been read in this session, before the entry was
  reviewed.

- The target entry MUST have been checked against every section of the style
  guide.

- Every unambiguous mechanical violation MUST have been fixed in place: dash
  character, colon usage, heading case, stray bold, unbolded `xref:`,
  outer-bold `xref:`, a bare external link, a line-wrap split inside an
  inline span.

- Every sentence-level rewrite and every bolding judgment call MUST have been
  reported rather than applied.

- No `xref:` target, entry title, filename, or index listing MAY have
  changed. Tidying changes how prose is written, never what it says or
  where it points.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the [style guide](../../../docs/style-guide.md) in full. Do not work
    from a remembered or cached understanding of its rules. The guide changes,
    and a pass run against a stale copy quietly enforces the wrong conventions.

2.  Run [`check_entry.py`](./scripts/check_entry.py) against the target entry:

    ```
    python3 .agents/skills/tidy/scripts/check_entry.py src/modules/ROOT/pages/<entry>.adoc
    ```

    This is a read-only checker for four specific, easy-to-miss-by-eye
    mistakes: the outer-bold `*xref:...[...]*` form, a soft line-wrap that
    lands inside an xref/link/bold/italic/code span, a plain prose line that
    runs past the line-wrap ceiling, and a bare external link not using the
    `{link-name}[...]` attribute form. Treat its findings as candidates for
    the mechanical-fix pass below — confirm each one against the entry before
    fixing, the same as any other check in this skill. A clean run doesn't
    mean the entry is fully tidy; it only clears those four checks. Everything
    else in this skill is still a manual read.

3.  Check the entry against the guide, section by section.

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

    - Cross-references — every `xref:` uses the inner-bold form,
      `xref:foo.adoc[*Text*]`, never the outer-bold form,
      `*xref:foo.adoc[Text]*`.

    - External links — every external `https?://` link in the body is
      defined as a `:link-name:` document attribute right after the title,
      and referenced inline as `{link-name}[link text]`. No bare
      `https://...[...]` in the body (except if in a `// TODO` comment).

    - Line wraps — soft-wrapped around 100 characters, running longer
      (typically not past 120) only where an xref, link, bold, italic, or
      code span can't otherwise be broken. A line-wrap MUST NOT land inside
      one of those spans.

    - Admonitions — used sparingly, and only for a genuinely secondary
      aside.

    - `// TODO` comments are legitimate, not style violations. They keep
      their bare URLs in place.

4.  Apply the mechanical fixes directly.

    - A hyphen or em dash used as a sentence-level pause becomes an en dash.

    - A hyphen or em dash separating a list term from its description
      becomes a colon, with the description capitalized as its own sentence.

    - A colon followed by prose rather than a list becomes two sentences.

    - A wrong-case heading or title becomes sentence case, respecting the
      formal proper noun exception.

    - An `xref:` that is not wrapped in `*...*` gets wrapped. Check every
      occurrence, not just the first in the entry.

    - An outer-bold `*xref:foo.adoc[Text]*` becomes the inner-bold
      `xref:foo.adoc[*Text*]`. If the link text was itself already bolded
      too (`*xref:foo.adoc[*Text*]*`), drop only the outer pair, keeping one
      bold, not zero.

    - A book or publication title set in bold becomes italics (`_Title_`).

    - Bold markup fitting none of the five accepted conventions is unbolded.

    - A bare external link becomes a `:link-name:` attribute reference. Add
      the attribute definition after the title, in the order links first
      appear in the body; pick a short, kebab-case, mnemonic name for the
      source (not derived mechanically from the URL); if the same URL
      already has an attribute elsewhere in the entry, reuse it rather than
      defining a duplicate. Re-align every attribute line in the block so
      the URLs start at a common column.

    - A soft line-wrap that splits an xref/link/bold/italic/code span across
      two lines gets un-split: join the span back onto one line. Don't
      reflow the rest of the paragraph while doing this — moving surrounding
      words to hit a target width is a bigger, riskier edit than this skill
      makes in one pass; leave that to a dedicated rewrap if the user asks
      for it.

5.  Report, rather than apply, the judgment calls.

    - A long or tangled sentence needing a rewrite. Propose the rewrite.
      Rephrasing moves meaning in a way punctuation does not.

    - An entry grown past a few short paragraphs and looking like it now
      covers more than one concept.

    - Whether a bolded term is a not-yet-planted topic marker, a first-use
      definition, or simply stray bold.

    - Whether a capitalized heading is a formal proper noun or just a
      descriptive phrase that reads like one.

    - A prose line past the line-wrap ceiling that isn't explained by one
      unbreakable span — this usually means the paragraph needs a proper
      rewrap, which is a judgment call about where to break, not a
      single-line mechanical fix.

6.  Report what was checked, what was fixed, and what is flagged, grouped by
    style-guide section.

## Rules

- You MUST tidy one entry at a time. A garden-wide style sweep produces a diff
  too large to review, which defeats the working tree as a review gate. Run the
  skill once per entry.

- `check_entry.py` is read-only and advisory. It never edits a file, and a
  finding is a candidate, not an automatic fix — apply the same judgment to
  its output as to anything else this skill catches by eye. It only covers
  four narrow, easy-to-miss mechanical checks; a clean run is not a
  substitute for the section-by-section read.

- The style guide MUST be the only source of style authority. Do not enforce a
  preference that is not written in `docs/style-guide.md`. Where you think the
  guide is missing a rule, say so in the report rather than applying an
  unwritten one.

- You MUST NOT repair structural defects. Broken cross-references, fake
  pseudo-links, orphans, and maturity emoji belong to a structural pass. Mention
  any you notice, and leave them.

- You MUST NOT change content. Tidying neither expands a thin entry nor breaks
  up an overgrown one. It changes only how the existing prose is written.

- You MUST NOT stage, commit, or push. Leave every change in the Git working
  tree. Reviewing the diff is how the user approves the work, so it stands in
  for any mid-flow prompt.

## Edge cases

- You cannot tell whether a term is a formal proper noun. Leave the
  capitalization as it stands and flag it. A wrongly de-capitalized standard or
  framework name is a factual error, which is worse than an inconsistent heading.

- A mechanical fix would change the sense of a sentence. It is then not
  mechanical. Move it to the flagged list, with the proposed wording, and leave
  the text alone.
