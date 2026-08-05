# Sow

Plants a brand-new entry in the digital garden — researching a topic, writing an
atomic AsciiDoc page, and cross-referencing it to relevant adjacent entries
already in the garden.

## What it does

Given a topic, the agent checks it doesn't already exist, researches it, writes
a focused `.adoc` page under `src/modules/ROOT/pages/`, links it to and from
related entries, and adds it to `index.adoc` (marked as a seedling 🌱) and
`nav.adoc`, in matching alphabetical positions.

## How to invoke

> Sow a new entry for event sourcing.

> Plant a page on the circuit breaker pattern.
