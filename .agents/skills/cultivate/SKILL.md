---
name: cultivate
description: Review garden entries against docs/style-guide.md — sentence-case titles, prose style, dash/colon usage, bold-text rules, admonition usage — and report or fix violations. Use when the user says "cultivate the garden", "check style", or asks for a style-guide pass over one or more pages.
metadata:
  interactive: yes
---

# Cultivate

Use this skill to bring one or more entries into conformance with [docs/style-guide.md](../../../docs/style-guide.md): titles and headings, written style (sentence length, dashes, colons), bold-text usage, admonitions, and TODO conventions.

Do NOT use this skill for structural maintenance — broken `xref:` targets, fake pseudo-links to existing pages, orphaned pages, or maturity labels are [tend](../tend/SKILL.md)'s job, not cultivate's. Cultivate is about *how something is written*, not *whether it's linked or discoverable*.

**Input**: A page, a set of pages, or "the whole garden" (the user may scope it; default to recently-touched pages if no scope is given, since a full-garden pass can be large). The skill always re-reads [docs/style-guide.md](../../../docs/style-guide.md) first, since it's the source of truth and may have changed since the skill was last run.

**Output**: A report of style-guide violations found, with unambiguous mechanical fixes (eg. hyphen → en dash, colon-then-prose → split sentence, wrong-case heading) applied directly. Judgment calls (eg. whether a paragraph should be split into a new page, whether a term should be bolded as a forage candidate) are flagged for the user.

## Instructions

1.  **Read the style guide.**

    Read [docs/style-guide.md](../../../docs/style-guide.md) in full before reviewing anything. Don't rely on a remembered or cached understanding of its rules — it changes independently of any one page.

2.  **Determine scope.**

    If the user names specific pages or a topic area, scope to those. If they say "cultivate the garden" with no further scope, ask whether they want the whole garden or a more recent slice (eg. pages touched in recent commits), since a full sweep can surface a lot of findings at once.

3.  **Check each page against the style guide, section by section:**

    - **Title and headings** — sentence case, acronyms spelled out on first use, no over-structuring with headings on short entries. Formal proper nouns (named legal documents, standards, frameworks, methods — eg. "Developer Certificate of Origin", "Capability Maturity Model") keep their own established capitalization and are not forced into sentence case. If unsure whether a term is a formal proper noun, leave it and flag it rather than guessing.
    - **Written style** — prose paragraphs (not bullet-heavy where prose belongs), simple sentences, no semicolons, en dash (not hyphen or em dash) for sentence-level pauses, colons only before lists, colons (not hyphens) separating list terms from descriptions.
    - **Bold text** — only four things are ever bold (see [docs/style-guide.md](../../../docs/style-guide.md#bold-text)): `xref:` cross-references, not-yet-sown forage-candidate terms, glossary-style list-term lead-ins (`*Term*: Description.`), and a term being defined for the first time in running prose. Nothing else. Check both directions: every `xref:` must be bold, and nothing else is bold unless it fits one of the other three conventions.
    - **Admonitions** — used sparingly, only for genuinely secondary asides.
    - **Open questions and TODOs** — `// TODO` comments are fine as-is; don't flag them as violations.

4.  **Apply unambiguous mechanical fixes directly:**

    - Hyphen or em dash used as a sentence-level pause → en dash.
    - Hyphen/em dash separating a list term from its description → colon, with the description capitalized as its own sentence.
    - A colon followed by prose rather than a list → split into two sentences.
    - Wrong-case heading or title → sentence case, respecting the formal-proper-noun exception.
    - Bold markup that doesn't fit any of the four accepted conventions → unbold it (unless it's a genuine forage candidate, in which case leave it; if you can't tell, flag it instead of guessing).
    - An `xref:` that isn't bolded → bold it. Every `xref:` link must be wrapped in `*...*`, with no exceptions — check this on every single occurrence, not just the first per page.

5.  **Flag judgment calls for the user**, rather than fixing them automatically:

    - Long or complex sentences that need rewriting (not just dash/colon mechanics) — propose a rewrite, don't apply it silently, since rephrasing changes meaning more than punctuation fixes do.
    - A page that's grown past "a few short paragraphs" and might need restructuring or splitting — that's [split](../split/SKILL.md)'s job; flag it, don't act on it here.
    - Whether a bolded term is a genuine forage candidate, a first-use definition, or should just be unbolded.
    - Whether a heading or title is a genuine formal proper noun (exempt from sentence case) or just a capitalized-sounding descriptive phrase — if unsure, leave it and flag rather than guess.

6.  **Report a summary.**

    List what was checked, what was fixed automatically, and what's flagged for the user, grouped by style-guide section.

## Rules

-   **The style guide is the only source of truth for style.** Don't apply a personal preference that isn't written in [docs/style-guide.md](../../../docs/style-guide.md) — if you think the guide is missing a rule, say so, don't enforce an unwritten one.

-   **Don't fix structural issues.** Broken links, fake pseudo-links to existing pages, orphans, and maturity labels belong to [tend](../tend/SKILL.md). If you notice one while cultivating, mention it in the report but don't fix it here.

-   **Don't rewrite for content, only for style.** Cultivate doesn't expand thin stubs ([fertilize](../fertilize/SKILL.md)'s job) or split overgrown pages ([split](../split/SKILL.md)'s job). It only changes how existing prose is written.

-   **Committing is out of scope.** This skill edits files in the working tree only. Staging, committing, and pushing are the user's call — never run `git commit` or `git push` as part of cultivating.

## Success criteria

- **The current style guide was read before any page was reviewed.**

- **Every page in scope was checked against every section of the style guide.**

- **All unambiguous mechanical fixes (dash, colon, case, stray bold, unbolded `xref:`) were applied directly.**

- **Sentence-level rewrites and bolding judgment calls were flagged, not auto-applied.**

- **The final report distinguishes fixes already applied from items still needing the user's decision.**
