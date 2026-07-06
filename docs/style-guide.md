# Style guide

Conventions for writing and editing garden entries (`.adoc` files under
`src/modules/ROOT/pages/`).

This guide covers writing style and AsciiDoc formatting. For the contribution
workflow, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## File naming

- Kebab-case, matching the page title, eg. `event-sourcing.adoc` for "Event
  sourcing".

- Singular and atomic. One topic per file. Don't use `and`/`&` in a filename to
  bundle two concepts into one page. Create separate pages and cross-reference
  them instead.

## Atomicity

- Keep each page focused on its own topic. If a paragraph is really explaining a
  different concept at length, that's a sign that concept needs (or already has)
  its own page. Cross-reference it with `xref:` instead.

- It's fine for an entry to be short. A few paragraphs that clearly state what a
  thing is, why it matters, and how it relates to neighboring topics, is a
  complete page. It doesn't need padding to feel "finished".

## Title and headings

- The document title (`= Title`) is sentence case. Capitalize the first word and
  any proper nouns or acronyms, lowercase everything else. Example:
  `= Event-driven architecture (EDA)`, not `= Event-Driven Architecture`.

- A formal proper noun — the official name of a named legal document, standard,
  framework, or method (eg. `Developer Certificate of Origin`,
  `Capability Maturity Model`) — keeps its own established capitalization
  throughout, even where that means multiple capitalized words. Don't force
  sentence case onto a name that is conventionally Title Case in its source. If
  in doubt whether a term is a formal proper noun or just a descriptive phrase,
  leave it as found and flag it rather than guessing.

- Acronyms are spelled out on first use, with the acronym in parentheses, eg.
  `Event-driven architecture (EDA)`. Subsequent headings/text may use the
  acronym alone.

- Section headings (`==`, `===`) follow the same sentence-case rule.

- Don't over-structure a short entry with headings. Many entries are just 2-4
  plain paragraphs with no `==` sections at all. Only add sections when a page
  has genuinely distinct sub-topics (eg. "Trade-offs", "Implementations").

## Written style

- Write in American English.

- Write in prose paragraphs.

- Bullet lists are for genuine enumerations (examples, steps, trade-offs), not a
  substitute for sentences.

- Prefer simple sentences to complex ones. If a sentence has multiple clauses,
  consider splitting it into two or more simple sentences.

- Avoid semicolons in sentences. Split into multiple sentences instead.

- Where a sentence needs a dash to set off a parenthetical or a pause, use an en
  dash (–), not a hyphen (-) or an em dash (—).

- A colon must only be followed by a list. Don't use a colon to join two clauses
  where a period or a new sentence would do.

- In a bullet list, prefer a colon to a hyphen/dash to separate a term from its
  description, eg.
  `` `sow`: Plant a new entry. `` rather than `` `sow` — plant a new entry. ``.
  Capitalize the description as its own sentence.

## Bold text

Only four things are ever bold in body text:

- Cross-references: `xref:target.adoc[Link text]`, eg.
  `xref:resilience.adoc[resilience]`. Use this for every mention of a concept
  that has its own page.

- Technical terms that don't yet have a dedicated topic page, but could warrant
  one in the future, eg. `*event-carried state transfer*`. This is a deliberate
  signal, not a placeholder error. It marks a candidate for a future `sow` (see
  the `forage` skill).

- A glossary-style list term immediately followed by its description, eg.
  `` * *Atomicity*: Transactions are fully completed, or not at all. ``. The
  bold ends at the colon; the description after it is plain text.

- A term being introduced or defined for the first time in running prose, eg.
  `` Base models are known as *emergence*. `` or `` *LoRA (Low-Rank Adaptation)* is a fine-tuning technique that... ``. This marks the moment a term is defined, not ongoing emphasis — don't bold the same term again on subsequent mentions within the same page unless it's also an `xref:`
  or forage candidate.

Don't bold anything else. Bold is not used for general emphasis.

## Cross-references

- Link to other garden pages with `xref:target.adoc[Link text]`. Use this for
  every mention of a concept that has its own page, even if it has been
  mentioned and linked already elsewhere on the same page.

- Bold every `xref:` (`*xref:foo.adoc[Foo]*`), per the [Bold text](#bold-text)
  rule above.

- Cross-reference link text matches the natural reading of the sentence, not
  necessarily the target page's exact title, eg.
  `xref:asynchronous-communication.adoc[asynchronously]`.

## Maturity labels

- Every entry carries one of four maturity markers, applied on its `index.adoc`
  listing line: 🌱 seedling, 🌿 budding, 🌳 evergreen, or 🍂 rotting.

- New entries are always sown as seedlings 🌱.

- Maturity is an editorial judgment, not a mechanical one. It's changed only
  with explicit confirmation from the repo owner, never inferred or auto-applied
  (including by agent skills).

## Open questions and TODOs

- A `// TODO: <url or note>` comment at the top of a file is the convention for
  flagging un-researched or unfinished content (a source to read, a section
  still to write). It's a normal, expected state for seedlings 🌱.

- TODOs are resolved by writing the content they point to, not by deleting the
  comment alone.

## Admonitions

- Use AsciiDoc admonition blocks (`[NOTE]`, `[TIP]`, `[WARNING]`, `[IMPORTANT]`)
  sparingly, for an aside that's genuinely secondary to the main flow of the
  page, not for core content that belongs in a regular paragraph.

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical
  section, as `* *xref:<file>.adoc[Title]* <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` is an orphan —
  undiscoverable from the site — and is a defect to fix (the `tend` skill looks
  for these).
