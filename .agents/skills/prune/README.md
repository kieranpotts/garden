# Prune

Checks whether a single garden entry duplicates an existing page, and if so merges them into one surviving page.

## What it does

Given one target entry, the agent scans for a page covering the same concept (typo'd filename, synonymous title, overlapping content), confirms the candidate with you, merges any unique content into the better page, repoints every reference, and deletes the redundant one. If nothing matches, it reports that the entry has no duplicate.

## How to invoke

> Is `acid.adoc` a duplicate of anything?

> Prune this entry.

> Does circuit-breaker.adoc repeat an existing page?
