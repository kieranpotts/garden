# Harvest

Produces a digest of recent garden activity — what's been sown, fertilized, tended, pruned, or grafted — without re-scanning the whole repo.

## What it does

The agent reads the `git log` for a given window (or since the last harvest), classifies each change by inspecting the actual diff against the file-change patterns of the other garden skills, and reports a grouped digest. It's read-only by default; it only writes a saved digest file if asked.

## How to invoke

> Harvest the garden.

> What's changed in the garden over the last two weeks?

> Harvest since v1.4.
