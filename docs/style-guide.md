# Style guide

Conventions for writing and editing garden entries (`.adoc` files under
`src/modules/ROOT/pages/`).

This guide covers writing style and AsciiDoc formatting. For the contribution
workflow, see [`CONTRIBUTING.md`](../CONTRIBUTING.md).

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
  throughout. Don't force sentence case onto a name that is conventionally title 
  case. If in doubt whether a term is a formal proper noun or just a descriptive 
  phrase, leave it as found and flag it rather than guessing.

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

- Avoid semicolons in sentences. Split into multiple sentences instead. (This
  is a sentence-level rule. It does not reach into bullet lists, where a semicolon
  chaining items into one flowing enumeration is fine.)

- Where a sentence needs a dash to set off a parenthetical or a pause, use an en
  dash (–), not a hyphen (-) or an em dash (—). Use this syntax sparingly. Most
  of the time it will be better to split into multiple sentences.

- A colon MUST only be followed by a list in the same sentence. For example:
  apples, bananas, oranges, and grapes.  Don't use a colon to join two clauses
  where a period or a new sentence would do.

- In a list with bold openers, prefer to terminate the bold opener with 
  a period before  writing its description as proper follow-on sentences.
  The house style is `` *`sow`.* Plant a new entry. `` rather than  
  `` *`sow`:* plant a new entry. `` or `` *`sow`* — plant a new entry. ``.
  Both the bold opener and the description are treated as separate sentences.
  Another example — `` *Abstraction.* Means to hide the details of a concept. ``
  Alternatively the bold text can cover an initial partial of the opening
  sentence, eg. `` *Abstraction* means to hide the details of a concept. ``

- Where a sentence leads into a list, prefer to use a period to terminate the 
  sentence before the list as normal. Do not use a colon or dash to set off 
  the list.

## Bold text

Only five things are ever bold in body text.

1.  **Cross-references.** `xref:target.adoc[*Link text*]`, eg.
    `xref:resilience.adoc[*resilience*]`. Use this for every mention of a 
    concept that has its own page.

2.  **Technical terms** that don't yet have a dedicated topic page, but could 
    warrant one in the future, eg. `*event-carried state transfer*`. This is a 
    deliberate signal marking a candidate for a future `sow`. The `forage`
    skill teaches agents to uncover these terms and create topic pages for 
    them.

3.  **A glossary-style list term** immediately followed by its description, eg.
    `` * *Atomicity.* Transactions are fully completed, or not at all. ``. The
    bold ends at the period. The description after it is plain text.

4.  **A term being introduced or defined for the first time** in running prose, 
    eg. `` This phenomenon is known as *emergence*. ``. Do not bold the same 
    term again on subsequent mentions within the same page (except where used in
    `xref:` link text).

5.  **A table-cell header label** in an AsciiDoc table, eg. `|*Granularity*`.

Don't bold anything else. Bold MUST NOT be used for general emphasis.

## Titles

- Book names and other publication titles are written in italics, eg.
  `_The Pragmatic Programmer_`, not `*The Pragmatic Programmer*` or plain text.
  This applies to books, papers, articles, and any other named publication
  mentioned in body prose.

- Italics are also used for foreign-word and pronunciation asides, eg.
  `_kuh-NEV-in_` and `_ad hoc_`.

## Cross-references

- Link to other garden pages with `xref:target.adoc[*Link text*]`. Use this for
  every mention of a concept that has its own page, even if it has been
  mentioned and linked already elsewhere on the same page.

- Bold every `xref:`. Apply the bold syntax to the inner link text, eg.
  `xref:foo.adoc[*Foo*]`.

- Cross-reference link text MUST match the natural reading of the sentence, not
  necessarily the target page's exact title, eg.
  `... xref:asynchronous-communication.adoc[*asynchronously interacts*] with ... `.

## Open questions and TODOs

- A `// TODO: <url or note>` comment at the top of a file is the convention for
  flagging un-researched or unfinished content. This is commonly used to plant
  seedlings 🌱 to `fertilize` later.

- TODOs are resolved by writing the content they point to, not by deleting the
  TODO comment!

## Admonitions

- Use AsciiDoc admonition blocks (`[NOTE]`, `[TIP]`, `[WARNING]`, `[IMPORTANT]`)
  sparingly. Use them for asides that are genuinely secondary to the main flow 
  of the page, not for core content that belongs in a regular paragraph.

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical
  section, as `* xref:<file>.adoc[*Page title*] <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` is an orphan —
  undiscoverable from the site — and is a defect to fix. The `tend` skill looks
  for these.

## Maturity labels

- Every entry carries one of four maturity markers, applied on its `index.adoc`
  listing line: 🌱 seedling, 🌿 budding, 🌳 evergreen, or 🍂 rotting.

- New entries are always sown as seedlings 🌱.

- Maturity is an editorial judgment, not a mechanical one. It's changed only
  with explicit confirmation from the user, never inferred or auto-applied
  by agents.
