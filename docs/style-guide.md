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

- Prefer splitting a sentence in two over joining independent clauses with a
  semicolon. Reserve the semicolon for joining short items in an inline list,
  or the rare case where splitting would lose an explicit contrast or
  cause-and-effect that the semicolon itself is signaling.

- Colons may introduce short comma-separated lists within the same sentence, eg.
  `` The model supports three operations: create, read, and delete. `` Do not
  use a colon to join two independent clauses that could each stand as a
  sentence. Split them into two sentences instead. Do not use a colon to
  introduce a code block, list block, or an admonition.

- Where a sentence needs a dash to set off a parenthetical or a pause, use an en
  dash (–), not a hyphen (-) or an em dash (—). But use this syntax sparingly.
  Most of the time it will be better to split into multiple sentences.

- Use `eg.` (no full points, no comma) as the house abbreviation for "for
  example", and `ie.` for "that is". Do not "correct" these to `e.g.` / `i.e.`.

## Line wraps

- Soft line wraps at 100 characters, but don't break within cross-references,
  bold or italic text, or other inline styling — let those lines run longer,
  typically not past about 120, rather than breaking a span. Don't break
  titles and sub-headings over multiple lines.

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

The following content is rendered as bold text.

- **Cross-references.** Written in the form `` xref:target.adoc[*link text*] ``,
  eg. `` xref:resilience.adoc[*resilience*] ``. Use this for the first mention of a
  concept that has its own page. Subsequent mentions are plain text.

- **Technical terms** that don't yet have a dedicated topic page, but could
  warrant one in the future, eg. `` *event-carried state transfer* ``. This is a
  deliberate signal marking a candidate for a future `sow`. The `forage`
  skill teaches agents to uncover these terms.

- **A term being introduced for the first time** in running prose, eg.
  `` This phenomenon is known as *emergence*. `` Do not bold the same term
  again on subsequent mentions within the same page, except where it is used
  in `xref:` link text.

- **An acronym spelled out on first use**, with the short form in parentheses.
  The whole phrase is bold, eg. `` *event-driven architecture (EDA)* ``.

- **UI elements** that the reader interacts with, such as button labels, menu
  items, and field names.

- **Glossary-style lists** where each item is a term followed by its definition,
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

## Monospace

- Use monospace (backticks) for text a reader might type or that a system might
  output literally. File paths, commands, flags, environment variables, code
  identifiers, and configuration keys all take backticks, eg. `` `ItemShipped` ``
  or `` `LOG_LEVEL` ``.

- Do not apply monospace to concept names in prose. Use
  bold for those.

## Cross-references

- Link to other garden pages with `` xref:target.adoc[*link text*] ``. In each
  page, do this only for the first mention of a concept that has its own page.
  Subsequent references to the same concept are plain text.

- Bold every `xref:`. Apply the bold syntax to the inner link text, eg.
  `` xref:foo.adoc[*Foo*] ``. Do not use the outer `` *xref:foo.adoc[Foo]* `` form.

- Cross-reference link text MUST match the natural reading of the sentence.
  Cross-references follow the normal sentence case rules, so they start with a
  capital letter if opening a sentence, otherwise the link text can be lowercase.
  The link text does not necessarily need to match exactly the page's title,
  eg. `... xref:asynchronous-communication.adoc[*asynchronously interacts*] with ... `.

## Acronyms

- Acronyms are spelled out on first use, with the acronym in parentheses, and
  the whole in bold text, eg. `*event-driven architecture (EDA)*`. Subsequent
  headings/text may use the acronym alone, in plain text.

- The exception is an acronym so common in a software development context that
  spelling it out would be noise to the reader, eg. HTTP, URL, JSON. Use
  judgment based on the acronym's ubiquity among the digital garden's
  technical audience.

## See also and references sections

An entry may end with one or both of two standard sections, in the following
order.

- `` == See also ``. Cross-references to other garden pages, one bullet per line,
  in the inner-bold xref form `` * xref:target.adoc[*Link text*] ``. List only
  pages genuinely related to the entry's topic.

- `` == References ``. External citations (books, papers, articles). Follow the
  TS-26 referencing style (`<author> (<year>). _<title>_. <publication>`), one
  bullet per entry. Hyperlink the title in hypermedia renderings.

An entry that has neither section simply ends on its last content paragraph.
Do not invent other closing-section names like "Further reading" or "External
links".

## Block lists

- Bullet lists are for genuine enumerations (examples, steps, trade-offs), not a
  substitute for sentences.

- Numbered lists are for sequences where the order is significant, or where
  individual steps need to cross-reference each other.

- Where a sentence leads into a list, end the lead-in with a period. Never lead
  in with a colon or dash.

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
  the main flow of the page, not for core content that belongs in a regular
  paragraph.

- Garden entries are encyclopedic, not procedural, so choose the admonition
  type by how the aside relates to the reader's understanding of the
  concept, not to completing a task.

  - `` [NOTE] ``. Supplementary context that enriches the topic but isn't
    essential to the main explanation.

  - `` [TIP] ``. An optional pointer, eg. how to explore the concept further
    or apply it in practice.

  - `` [IMPORTANT] ``. A caveat or nuance whose omission would leave the
    reader with a wrong understanding of the concept.

  - `` [WARNING] ``. A common misconception or practice that could cause
    real harm if acted on, eg. a security anti-pattern.

  - `` [CAUTION] ``. A less severe pitfall, or a note that an approach is
    dated or superseded.

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical
  section, as `* xref:<file>.adoc[*Page title*] <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` is an orphan —
  undiscoverable from the site — and is a defect to fix. The `tend` skill looks
  for these.

## Maturity labels

- Every entry carries one of four maturity markers, applied on its `index.adoc`
  listing line: 🌱 seedling, 🌿 budding, 🌳 evergreen, or 🍂 decaying.

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
  AsciiDoc syntax and tooling conventions (file extensions, attributes,
  includes, links, admonition block form, line wrapping).

Where there is contradictory guidance between the various technical standards,
the style guide that's specific to the Digital Garden takes precedence.
