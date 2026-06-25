# Harvest

Produces a digest of recent garden activity — what's been sown, fertilized, tended, pruned, grafted, entwined, weeded, or uprooted — without re-scanning the whole repo.

## What it does

The agent reads the `git log` for a given window (or since the last harvest), classifies each change primarily by its commit type prefix (`sow:`, `tend:`, `fertilize:`, `prune:`, `graft:`, `entwine:`, `weed:`, `uproot:`), falling back to the diff when a prefix is missing or looks mismatched, and reports a grouped digest. It's read-only by default; it only writes a saved digest file if asked.

## How to invoke

> Harvest the garden.

> What's changed in the garden over the last two weeks?

> Harvest since v1.4.
