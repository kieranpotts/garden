# Entwine

Finds existing garden pages that are related but not cross-referenced, and adds the missing `xref:` links between them.

## What it does

The agent scans the garden for pairs of pages that look related — by shared category, by name-dropping each other without a link, or by domain knowledge — proposes the batch with a one-line reason per pair, and adds confirmed links in place. It never creates new pages; gaps that need new content go to `sow` instead.

## How to invoke

> Entwine the garden.

> Find missing cross-references.

> Entwine event-sourcing.adoc with its neighbors.

## Examples

**Input**: "Entwine the garden."

**Output**: "Proposed links: `circuit-breaker.adoc` ↔ `retry.adoc` (both resilience patterns, neither mentions the other); `event-sourcing.adoc` → `cqrs.adoc` (commonly paired, cqrs.adoc already links back). Add these?"
