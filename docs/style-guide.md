# Style guide

Conventions for writing and formatting garden entries (`.adoc` files under
`src/modules/ROOT/pages/`).

## File naming

- File names are kebab-case with the `.adoc` extension. The file name is derived
  from the document title (`` = H1 heading ``) but does not necessarily match it 
  exactly. For example, `event-sourcing.adoc` for "Event sourcing", or 
  `domain-driven-design.adoc` for "Domain-driven design (DDD)".

- File names are singular and atomic.

## Atomicity

- Keep each page focused on exactly one topic. If any paragraph covers a 
  different (but related) concept at length, that should be extracted to its 
  own topic page and cross-referenced using `xref:`.

- It's fine for an entry to be short. Even a single-paragraph entry is
  acceptable, if that's sufficient to explain a concept and cross-reference it
  to neighbouring topics. That is a complete, atomic entry. Pages don't need 
  to be padded to feel "finished".

## General written style

- American English. 

- Full prose paragraphs.

- Authoritative, journalistic style. This is a thoroughly researched, 
  continuously-refined encyclopedia of knowledge about topics in software 
  development, and computer science more broadly.

- Simple sentences. Avoid compounding multiple clauses in a single sentence.
  If an existing sentence has multiple clauses, consider splitting it into two 
  or more simple sentences. If that reads better, make the change — no need to
  prompt the user to approve this kind of regular tidying.

- Avoid semicolons in sentences. Split into multiple sentences instead.

- Avoid colons everywhere. Do not use them to introduce code blocks or list
  blocks. Don't use colons to join two clauses that could be split into two
  sentences. The only valid use case for a colon is within a sentence that ends
  with a short comma-separated list. For example,
  `` The model supports three operations: create, read, and delete. ``

- Where a sentence needs a dash to set off a parenthetical or a pause, use an en
  dash (–), not a hyphen (-) or an em dash (—). But use this syntax sparingly. 
  Most of the time it will be better to split into multiple sentences.

## Line wraps

- Soft line wraps at 80 characters, but don't break within cross-references, 
  bold or italic text, or other inline styling. Don't break titles and 
  sub-headings over multiple lines.

## Title and headings

- The document title (`` = Title ``) should be sentence case in most cases. 
  Capitalize the first word and any proper nouns or acronyms. Lowercase 
  everything else. For example, `` = Event-driven architecture (EDA) ``, 
  not `` = Event-Driven Architecture ``.

- A formal proper noun — the official name of a named legal document, standard,
  framework, or method (eg. `` Developer Certificate of Origin ``,
  `` Capability Maturity Model ``) — keeps its own established capitalization
  throughout. Don't force sentence case onto a name that is conventionally title 
  case. If in doubt whether a term is a formal proper noun or just a descriptive 
  phrase, leave it as found and flag it rather than guessing. The user makes 
  these decisions.

- Avoid use of `and`/`&` in document titles, unless part of a proper noun. This
  suggests two topics entwined in a single entry.

- Section headings (`==`, `===`) follow the same rules as the document title.

- Don't over-structure a short entry with headings. Only add sections when a page
  has genuinely distinct sub-topics, eg. "Trade-offs", "Implementations".

## Bold text

Only the following content is rendered as bold text. 

- **Cross-references.** Written in the form `` xref:target.adoc[*link text*] ``, 
  eg. `` xref:resilience.adoc[*resilience*] ``. Use this for every mention of a 
  concept that has its own page.

- **Technical terms** that don't yet have a dedicated topic page, but could 
  warrant one in the future, eg. `` *event-carried state transfer* ``. This is a 
  deliberate signal marking a candidate for a future `sow`. The `forage`
  skill teaches agents to uncover these terms.

- **A term being introduced for the first time** in running prose,  eg. 
- `` This phenomenon is known as *emergence*. ``. Do not bold the same 
  term again on subsequent mentions within the same page, except where it
  is used in `xref:` link text.

- **UI elements** that the reader interacts with, such as button labels, menu
  items, and field names.

- **Glossary-style lists** where each item is a term is followed by its definition,
   eg. `` * *Atomicity.* Transactions are fully completed, or not at all. ``. 

- **A table-cell header label** in an AsciiDoc table, eg. `` |*Granularity* ``.

Bold MUST NOT be used for general emphasis.

## Italics

- Book names and other publication titles are written in italics, eg.
  `` _The Pragmatic Programmer_ ``, not `` *The Pragmatic Programmer* `` or 
  plain text. This applies to books, papers, articles, and any other named 
  publication mentioned in body prose.

- Italics are also used for foreign-word and pronunciation asides, eg.
  `` _kuh-NEV-in_ `` and `` _ad hoc_ ``.

## Cross-references

- Link to other garden pages with `` xref:target.adoc[*link text*] ``. In each
  page, do this only for the first mention of a concept that has its own page. 
  Subsequent references to the same concept are plain text. 

- Bold every `xref:`. Apply the bold syntax to the inner link text, eg.
  `xref:foo.adoc[*Foo*]`.

- Cross-reference link text MUST match the natural reading of the sentence. 
  Cross-references follow the normal sentence case rules, so they start with a 
  capital letter if opening a sentence, otherwise the link text can be lowercase.
  The link text does not necessarily need to match exactly the page's title,
  eg. `... xref:asynchronous-communication.adoc[*asynchronously interacts*] with ... `.

## Acronyms

- Acronyms are spelled out on first use, with the acronym in parentheses, and 
  the whole in bold text, eg. `*event-driven architecture (EDA)*`. Subsequent 
  headings/text may use the acronym alone, in plain text.

## Block lists

- Bullet lists are for genuine enumerations (examples, steps, trade-offs), not a
  substitute for sentences.

- Numbered lists are for sequences where the order is significant, or where 
  individual steps need to cross-reference each other.

- Where a sentence leads into a list, prefer to use a period to terminate the 
  sentence before the list. Do not use a colon or dash to set off  the list.

- Some lists may be used for glossary-style references, in which a term is 
  followed by its definition. The term should come first and be in bold text.
  The term is either delimited from the description by a period, or it rolls
  into the description in a single sentence. The following examples demonstrate
  the house style.

  - `` *Abstraction.* Means to hide the details of a concept. ``
  - `` *Abstraction* means to hide the details of a concept. ``

  Do not use colons or hyphens to delimit terms from their definitions in a 
  glossary list. The following examples are invalid. 

  - `` *`sow`:* plant a new entry. `` 
  - `` *`sow`* — plant a new entry. ``

  The correct format is `` *`sow`.* Plant a new entry. ``

## Open questions and TODOs

- A `// TODO: <url or note>` comment at the top of a file is the convention for
  flagging un-researched or unfinished content.

- TODOs are resolved by writing the content they point to, not by deleting the
  TODO comment!

## Admonitions

- Use AsciiDoc admonition blocks (`[NOTE]`, `[TIP]`, `[WARNING]`, `[IMPORTANT]`, 
  `[CAUTION]`) sparingly. Use them for asides that are genuinely secondary to 
  the main flow  of the page, not for core content that belongs in a regular 
  paragraph.

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

## References

See also the following technical standards, which apply.

- [TS-26: Technical Writing Style Guide](https://kieranpotts.com/standards/026) \
  Prose-level rules (voice, tense, emphasis, punctuation, lists, numbers) that
  apply to any technical document.

- [TS-28: AsciiDoc](https://kieranpotts.com/standards/028) \
  AsciiDoc syntax  and tooling conventions (file extensions, attributes, 
  includes, links, admonition block form, line wrapping).

Where there is contradictory guidance between the various technical standards,
the style guide that's specific to the Digital Garden takes precedence.
