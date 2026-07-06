# Forage

Finds topics that are referenced or implied across the garden but don't have
their own page yet, and produces a prioritized list of candidates for sowing.

## What it does

The agent scans all pages for fake pseudo-links (`*[text]*` with no matching
page) and plain unbracketed mentions of recurring topics, aggregates them by
concept, counts how many pages mention each one, and presents a ranked list.
It's read-only — it never creates pages itself; confirmed candidates get handed
to `sow`.

## How to invoke

> Forage the garden.

> What topics are missing?

> Forage around the AI topics.

## Examples

**Input**: "Forage the garden."

**Output**:
```
1. accidental complexity (9 mentions: microservices.adoc, distributed-system.adoc, ...)
2. distributed software (8 mentions: ...)
3. domain experts (5 mentions: ...)
```
Which of these should I sow?
