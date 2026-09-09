# Style guide

This style guide defines the conventions specific to writing and formatting garden entries (`.adoc` files under
`src/modules/ROOT/pages/`).

This document covers only what's specific to the digital garden. General prose style is governed by
[TS-26: Technical Writing Style Guide](https://kieranpotts.com/standards/026), and general AsciiDoc syntax by
[TS-28: AsciiDoc](https://kieranpotts.com/standards/028).

[`template/example-entry.adoc`](../template/example-entry.adoc) is a complete, compliant worked example, only with
placeholder body text standing in for a real topic. Treat it as the canonical demonstration of every mechanical rule
of this style guide.

## File naming

- File names MUST be kebab-case, with the `.adoc` extension.

- A file name SHOULD be derived from the document title (`= H1 heading`), but MAY diverge from it where the exact
  title makes for an awkward file name, eg `event-sourcing.adoc` for "Event sourcing," or
  `domain-driven-design.adoc` for "Domain-driven design (DDD)."

- A file name MUST be singular and atomic.

## Atomicity

- Each page MUST be focused on exactly one topic.

- A paragraph that covers a different, but related, concept at length SHOULD be extracted to its own topic page and
  cross-referenced with `xref:`, rather than absorbed into the current one.

- An entry MAY be as short as a single paragraph, provided that's sufficient to explain the concept and
  cross-reference it to neighboring topics; a page MUST NOT be padded just to feel "finished."

## Bold text

- Beyond the general emphasis rules in TS-26, a technical term that doesn't yet have a dedicated topic page, but could
  warrant one in the future, SHOULD be set in bold. This is a deliberate signal marking a candidate for a future `sow`,
  which the `forage` skill relies on to find such terms.

## Cross-references

- A link to another garden page MUST use a bold `xref:`, per TS-28, and only for the first mention of a concept that has
  its own page.

- A later mention of the same concept, within the same page, MUST be left as plain text rather than linked again.

- Cross-reference link text MUST follow the natural reading of the sentence and the normal sentence-case rules
  (capitalized only where it opens a sentence), and need not match the target page's title exactly.

## See also and references sections

- An entry MAY end with a `== See also` section, a `== References` section, or both, in that order.

- `== See also` MUST list only cross-references to other garden pages that are genuinely related to the entry's
  topic, one bullet per line in the inner-bold xref form, but SHOULD NOT repeat a page already cross-referenced in the
  body prose above.

- `== See also` MUST be omitted entirely where no genuinely relevant related page is left to list once the body's
  own cross-references are excluded.

- Each `== References` entry MUST follow TS-26's style rules for referencing.

## Images and diagrams

- A hand-drawn (non-text-based) diagram MUST be drafted in draw.io, exported as SVG, and hand-edited to the
  `light-dark()`/font-inheritance/`opts=inline` conventions documented in the website repo.

- Every `image::` macro referencing one of these SVGs MUST include the `opts=inline` attribute, or the diagram will
  ignore the reader's dark mode preference.

## TODOs

- Un-researched or unfinished content MUST be flagged with a `// TODO: <url or note>` comment at the top of the
  file.

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical section, as
  `* xref:<file>.adoc[*Page title*] <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` MUST be treated as an orphan — undiscoverable from the site,
  and a defect to fix. The `tend` skill looks for these.

## Maturity labels

- Every entry MUST carry one of four maturity markers on its `index.adoc` listing line: 🌱 seedling, 🌿 budding,
  🌳 evergreen, or 🍂 decaying.

- A new entry MUST be sown as a seedling 🌱.

- Maturity MUST NOT be promoted, demoted, or otherwise changed without explicit confirmation from the user — it's
  an editorial judgment, never inferred or auto-applied by agents.
