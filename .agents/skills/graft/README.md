# Graft

Merges two or more related-but-distinct garden entries into a single broader
page, repointing cross-references and removing the absorbed pages.

## What it does

Given several pages that cover different-but-related ideas (not duplicates), the
agent proposes a merge, confirms the survivor and its structure with you, folds
each source's distinct content into one coherent page, repoints every `xref:`
and index entry, and deletes the absorbed pages. If one page is already fully
covered by another and adds nothing, that's a job for `prune` (drop it) instead;
splitting one page into many is `split`.

## How to invoke

> Graft retry.adoc, backoff.adoc and jitter.adoc into one retry-strategies page.

> These three entries really cover one theme — merge them.
