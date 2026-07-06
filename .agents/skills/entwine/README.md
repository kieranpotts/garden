# Entwine

Given a single garden entry, finds other pages that are related to it but not cross-referenced, and adds the missing `xref:` links.

## What it does

The agent takes one target entry, scans the garden for pages related to it — by shared category, by name-dropping it without a link, or by domain knowledge — proposes the batch with a one-line reason per pair, and adds confirmed links in place. It never creates new pages; gaps that need new content go to `sow` instead.

## How to invoke

> Entwine event-sourcing.adoc with its neighbors.

> Link this page to related entries.

> Is retry.adoc properly connected to its siblings?

## Examples

**Input**: "Entwine event-sourcing.adoc with its neighbors."

**Output**: "Proposed links: `event-sourcing.adoc` → `cqrs.adoc` (commonly paired, cqrs.adoc already links back); `event-sourcing.adoc` ↔ `event-driven-architecture.adoc` (parent pattern, neither links the other). Add these?"
