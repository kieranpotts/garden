# Cultivate

Reviews a single entry against [docs/style-guide.md](../../../docs/style-guide.md) and fixes mechanical style violations directly.

## What it does

The agent re-reads the style guide, then checks titles and headings, written style (sentence length, dashes, colons), bold-text usage, and admonition usage on the target entry. Mechanical fixes — wrong dash character, hyphen-separated list terms, wrong-case headings, stray bold — are applied directly. Sentence-level rewrites and bolding judgment calls are flagged for the user to decide.

## How to invoke

> Cultivate resilience.adoc.

> Check style on this entry.

> Give agent.adoc a style-guide pass.
