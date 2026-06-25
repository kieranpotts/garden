# Style guide

Conventions for writing and editing garden entries (`.adoc` files under `src/modules/ROOT/pages/`).

This guide covers writing style and AsciiDoc formatting. For the contribution workflow, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## File naming

- Kebab-case, matching the page title, eg. `event-sourcing.adoc` for "Event sourcing".

- Singular and atomic. One topic per file. Don't use `and`/`&` in a filename to bundle two concepts into one page. Create separate pages and cross-reference them instead.

## Title and headings

- The document title (`= Title`) is sentence case. Capitalize the first word and any proper nouns or acronyms, lowercase everything else. Example: `= Event-driven architecture (EDA)`, not `= Event-Driven Architecture`.

- Acronyms are spelled out on first use, with the acronym in parentheses, eg. `Event-driven architecture (EDA)`. Subsequent headings/text may use the acronym alone.

- Section headings (`==`, `===`) follow the same sentence-case rule.

- Don't over-structure a short entry with headings. Many entries are just 2-4 plain paragraphs with no `==` sections at all. Only add sections when a page has genuinely distinct sub-topics (eg. "Trade-offs", "Implementations").

## Written style

- Write in prose paragraphs.

- Bullet lists are for genuine enumerations (examples, steps, trade-offs), not a substitute for sentences.

- Keep each page focused on its own topic. If a paragraph is really explaining a different concept at length, that's a sign that concept needs (or already has) its own page. Cross-reference it with `xref:` instead.

- It's fine for an entry to be short. A few paragraphs that clearly state what a thing is, why it matters, and how it relates to neighboring topics, is a complete page. It doesn't need padding to feel "finished".

## Cross-references

- Link to other garden pages with `xref:target.adoc[Link text]`, eg. `xref:resilience.adoc[resilience]`. Use this for every mention of a concept that has its own page.

- Never write a fake link. Bracketed or bolded text that looks like a link but isn't (`*[some concept]*` or `*some concept*` where a real page exists). If a page exists for that concept, link it with `xref:`. If no page exists yet, write the term as plain text. Don't invent a fake-looking link as a placeholder for a future page.

- Don't double up `xref:` inside bold markup (`*xref:foo.adoc[Foo]*`). The link itself is sufficient signal. Bold is for genuine emphasis elsewhere in the text.

- Cross-reference link text matches the natural reading of the sentence, not necessarily the target page's exact title, eg. `xref:asynchronous-communication.adoc[asynchronously]`.

## Maturity labels

- Every entry carries one of four maturity markers, applied on its `index.adoc` listing line: 🌱 seedling, 🌿 budding, 🌳 evergreen, or 🍂 rotting.

- New entries are always sown as seedlings 🌱.

- Maturity is an editorial judgment, not a mechanical one. It's changed only with explicit confirmation from the repo owner, never inferred or auto-applied (including by agent skills).

## Open questions and TODOs

- A `// TODO: <url or note>` comment at the top of a file is the convention for flagging un-researched or unfinished content (a source to read, a section still to write). It's a normal, expected state for seedlings 🌱.

- TODOs are resolved by writing the content they point to, not by deleting the comment alone.

## Admonitions

- Use AsciiDoc admonition blocks (`[NOTE]`, `[TIP]`, `[WARNING]`, `[IMPORTANT]`) sparingly, for an aside that's genuinely secondary to the main flow of the page, not for core content that belongs in a regular paragraph.

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical section, as `* *xref:<file>.adoc[Title]* <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` is an orphan — undiscoverable from the site — and is a defect to fix (the `tend` skill looks for these).
