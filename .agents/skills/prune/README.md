# Prune

Drops an entry whose topic is already well-covered by another page, deleting it
and redirecting its links to the covering page.

## What it does

Given one target entry, the agent finds the page that already covers its topic,
confirms the target is genuinely redundant (nothing unique would be lost),
repoints every reference to the covering page, and deletes the target. If the
target actually carries distinct content, it's not a prune — the agent reports
it as a `graft` (combine) or `entwine` (link) candidate instead.

## How to invoke

> Prune acid.adoc — it's already covered by acid-principles.adoc.

> This entry is redundant, drop it.

> Is circuit-breaker.adoc made redundant by resilience.adoc?
