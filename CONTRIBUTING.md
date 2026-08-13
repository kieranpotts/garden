# Contributing

<!-- Agents MUST read ./AGENTS.md. This document is for humans. -->

> [!NOTE]
> This repo is not open to external contributions.

## Adding or editing an entry

This repo is an Antora content module (component `garden`). It has no build of
its own. It's aggregated and built by the
[`website`](https://github.com/kieranpotts/website) repo.

See the [style guide](./docs/style-guide.md) for writing and formatting
conventions.

To add a new entry:

1. Add a new `.adoc` file under `src/modules/ROOT/pages/`, named after the topic
   in kebab-case, eg. `event-sourcing.adoc`.

2. Keep each file atomic — focused on a single idea or concept. Cross-reference
   related topics with `xref:` rather than repeating content.

3. Mark the entry's maturity with one of the legend emoji (🌱 Seedling, 🌿
   Budding, 🌳 Evergreen, 🍂 Decaying), matching the existing pages.

4. List the page on `src/modules/ROOT/pages/index.adoc`, under the relevant
   section, following the existing `xref:` + emoji pattern. The index is the
   primary way pages are discovered on the site.

5. Commit and push the changes. Merge into `latest/dev`, eg. via a PR. This
   queues the change for publication, which is scheduled to happen overnight
   unless a fresh deployment is manually triggered beforehand (via the `website`
   repo's GitHub workflows).

6. To preview the changes, rebuild the `website` repo. (The `website` repo
   fetches content sources from the `latest/dev` branch of the remote `garden`
   repository – it is not currently possible to preview local changes.)

Alternatively, to preview a draft entry *before* merging its PR: push the draft
to a branch in this repo, then manually run the `website` repo's
`Netlify Preview` GitHub Actions workflow with that branch name. This builds the
aggregated site against the draft branch, instead of `latest/dev`, and posts a
real preview URL.

## Commit messages

Commit messages MUST follow the format `<type>: <description>`, where
`<description>` is lowercase, imperative mood, and has no trailing period. This
is enforced both locally (a pre-commit hook at
`.hooks/validate_commit_message.py`) and in CI
(`.github/workflows/validate-commit-messages.yaml`) — keep the two in sync if
the allowed types ever change.

`<type>` MUST be one of:

- `sow`: Plant a new entry.
- `tend`: Fix broken links, fake links, orphaned documents, etc.
- `water`: Research and extend an existing entry.
- `fertilize`: Expand a thin stub entry.
- `prune`: Freeform trim — trim, smooth, reorder within a document.
- `graft`: Merge related-but-distinct entries into one document.
- `divide`: Split an overgrown entry into separate documents.
- `entwine`: Add missing cross-references between existing entries.
- `tidy`: Bring an entry into conformance with the style guide.
- `uproot`: Drop an entry already covered by another document.
- `fix`: Correct a factual error in an entry (standard TS-9 type).
- `chore`, `maintenance`, `style`: Standard types, for changes that aren't
  about garden content (eg. CI config, dependency bumps, whitespace).

Examples:

```
sow: add entry for event sourcing
water: research and extend event-sourcing with recent developments
fertilize: expand abstraction with examples and modular design xref
tend: fix broken xref in agent.adoc
prune: trim waffle and reorder sections in agent
graft: merge retry, backoff and jitter into retry-strategies
divide: break event-driven-architecture into event-sourcing and cqrs
entwine: link circuit-breaker and retry as related resilience patterns
tidy: fix dash and colon usage in resilience
fix: correct factual error in acid-principles
uproot: drop adaptive-software-development, covered by adaptive-software-development
maintenance: update pre-commit hook versions
```

## Agent skills

This repo has a set of [agent skills](./.agents/skills/README.md) for
maintaining the garden — sowing new entries, watering established entries,
tending broken links, fertilizing stubs, pruning duplicates, grafting related
entries into one, splitting overgrown pages, entwining related entries, foraging
for missing topics, cultivating style-guide conformance, trimming loose ends,
and harvesting a digest of recent growth.
