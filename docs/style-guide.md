# Style guide

Conventions specific to writing and formatting garden entries (`.adoc` files under `src/modules/ROOT/pages/`).

This document covers only what's specific to *this* garden — its atomic-entry format, its skills-driven maintenance
conventions, and its site-structure requirements. General prose style is governed by
[TS-26: Technical writing style guide](https://kieranpotts.com/standards/026), general AsciiDoc syntax by
[TS-28: AsciiDoc](https://kieranpotts.com/standards/028), and single-topic document scope by
[TS-25 §Scope](https://kieranpotts.com/standards/025). Those are normative for garden entries the same as this
document is. Where this document doesn't cover something, defer to them; where it does, it's usually because the
garden's format calls for something more specific than the general rule.

## File naming

- File names are kebab-case with the `.adoc` extension. The file name is derived from the document title (`= H1
  heading`) but does not necessarily match it exactly. For example, `event-sourcing.adoc` for "Event sourcing," or
  `domain-driven-design.adoc` for "Domain-driven design (DDD)."

- File names are singular and atomic.

## Atomicity

Keep each page focused on exactly one topic — see [TS-25 §Scope](https://kieranpotts.com/standards/025) for the
general single-topic rule this follows, including its "does the title contain 'and'/'or'" test for a page that has
outgrown its scope. If any paragraph covers a different (but related) concept at length, extract it to its own topic
page and cross-reference it with `xref:`.

It's fine for an entry to be short. Even a single-paragraph entry is acceptable, if that's sufficient to explain a
concept and cross-reference it to neighbouring topics. That is a complete, atomic entry. Pages don't need to be padded
to feel "finished."

## Bold text

Beyond the general emphasis rules in [TS-26 §Emphasis](https://kieranpotts.com/standards/026), the garden uses bold
for one thing of its own:

- **A technical term that doesn't yet have a dedicated topic page, but could warrant one in the future**, eg
  `*event-carried state transfer*`. This is a deliberate signal marking a candidate for a future `sow`. The `forage`
  skill teaches agents to uncover these terms.

## Cross-references

Link to other garden pages with `xref:target.adoc[*link text*]` — bold, per
[TS-28 §Links](https://kieranpotts.com/standards/028). In each page, do this only for the first mention of a concept
that has its own page; subsequent references to the same concept are plain text. This is a garden-specific economy
rule — most content isn't dense enough with cross-references for it to matter, but a garden entry often is.

Cross-reference link text MUST match the natural reading of the sentence. It follows normal sentence-case rules, so it
starts with a capital letter only if opening a sentence. The link text does not necessarily need to match exactly the
page's title, eg `... xref:asynchronous-communication.adoc[*asynchronously interacts*] with ...`.

## External links

Define every external link as a document attribute, immediately after the `= Title` line, one per line, aligned so
the URLs start at a common column:

```asciidoc
= Title

:link-example-source: https://example.com/some/long-path
:link-wikipedia:      https://en.wikipedia.org/wiki/Example
```

This is the same attribute mechanism as [TS-28 §Attributes](https://kieranpotts.com/standards/028); the garden adds
two refinements of its own:

- Align the URLs to a common column, for readability of the page header as a block.
- Order the attribute definitions in the order the links first appear in the body.

Attribute names are short, kebab-case, mnemonic labels for the source (the publication, organization, or topic), not
derived mechanically from the URL, eg `link-wikipedia`, `link-nist`, `link-rfc-2119`. Keep them unique within the
page.

## See also and references sections

An entry may end with one or both of two standard sections, in the following order.

- `== See also`. Cross-references to other garden pages, one bullet per line, in the inner-bold xref form
  `* xref:target.adoc[*Link text*]`. List only pages genuinely related to the entry's topic, and only those not
  already linked in the body prose above. A page already cross-referenced in the body text MUST NOT be repeated in
  `See also`. Not every entry needs this section — omit it entirely if there are no genuinely relevant related pages
  left to list once the body's own cross-references are excluded. Don't pad the list just to have one, and don't keep
  a stale entry that's now covered in the body.

- `== References`. External citations (books, papers, articles), following
  [TS-26 §Referencing](https://kieranpotts.com/standards/026) — one `*` bullet per entry, separated by a blank line.
  Break each entry over three lines — author, title, publication — regardless of the 120-character soft wrap used
  elsewhere. This is a deliberate garden-specific exception to the general line-wrap rule. For example:

  ```asciidoc
  * Lieberman, Paternò, Klann, and Wulf (2006).
    {link-lieberman}[_End User Development: An Emerging Paradigm_].
    Springer.

  * {link-wikipedia}[_End-user development_].
    Wikipedia.
  ```

  The second line is indented two spaces to align under the bullet's text, not under the `*` marker. If a reference
  has no separate publication (eg an undated web page whose title and site are the same source), the entry may
  collapse to two lines — author and title — rather than inventing a third.

An entry that has neither section simply ends on its last content paragraph. Do not invent other closing-section names
like "Further reading" or "External links."

## Open questions and TODOs

- A `// TODO: <url or note>` comment at the top of a file is the convention for flagging un-researched or unfinished
  content.

- TODOs are resolved by writing the content they point to, not by deleting the TODO comment!

## The index

- Every page MUST be listed in `index.adoc`, in its correct alphabetical section, as
  `* xref:<file>.adoc[*Page title*] <maturity emoji>`.

- A page that exists but isn't listed in `index.adoc` is an orphan — undiscoverable from the site — and is a defect
  to fix. The `tend` skill looks for these.

## Maturity labels

- Every entry carries one of four maturity markers, applied on its `index.adoc` listing line: 🌱 seedling, 🌿 budding,
  🌳 evergreen, or 🍂 decaying.

- New entries are always sown as seedlings 🌱.

- Maturity is an editorial judgment, not a mechanical one. It's changed only with explicit confirmation from the
  user, never inferred or auto-applied by agents.
