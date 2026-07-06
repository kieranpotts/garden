# Tend

Walks the digital garden looking for withering content: broken cross-references, fake pseudo-links, pages missing from the index, and maturity labels that no longer match reality.

## What it does

The agent inventories every page, checks all `xref:` targets resolve, finds bracketed text that looks like a link but isn't real AsciiDoc syntax, finds pages absent from `index.adoc`, and flags maturity emoji that look out of date. Unambiguous fixes (a clear broken link, a fake link with an obvious real target) are applied directly. Everything else is reported for the user to decide.

## How to invoke

> Tend the garden.

> Check for broken links.

> Tend the AI topics.
