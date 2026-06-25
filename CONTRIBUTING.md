# Contributing

> [!NOTE]
> This repo is not open to external contributions.

## Adding or editing an entry

This repo is an Antora content module (component `garden`). It has no build of its own. It's aggregated and built by the [`website`](https://github.com/kieranpotts/website) repo.

To add a new entry:

1. Add a new `.adoc` file under `src/modules/ROOT/pages/`, named after the topic in kebab-case, eg. `event-sourcing.adoc`.

2. Keep each file atomic — focused on a single idea or concept. Cross-reference related topics with `xref:` rather than repeating content.

3. Mark the entry's maturity with one of the legend emoji (🌱 Seedling, 🌿 Budding, 🌳 Evergreen, 🍂 Decaying), matching the existing pages.

4. List the page on `src/modules/ROOT/pages/index.adoc`, under the relevant section, following the existing `xref:` + emoji pattern. The index is the primary way pages are discovered on the site.

5. Commit and push the changes. Merge into `latest/dev`, eg. via a PR. This queues the change for publication, which is scheduled to happen overnight unless a fresh deployment is manually triggered beforehand (via the `website` repo's GitHub workflows).

6. To preview the changes, rebuild the `website` repo. (The `website` repo fetches content sources from the `latest/dev` branch of the remote `garden` repository – it is not currently possible to preview local changes.)

Alternatively, to preview a draft entry *before* merging its PR: push the draft to a branch in this repo, then manually run the `website` repo's `Netlify Preview` GitHub Actions workflow with that branch name. This builds the aggregated site against the draft branch, instead of `latest/dev`, and posts a real preview URL.

## Commit messages

Commit messages MUST follow the format `<type>: <description>`, where `<description>` is lowercase, imperative mood, and has no trailing period. This is enforced both locally (a pre-commit hook at `.hooks/validate_commit_message.py`) and in CI (`.github/workflows/validate-commit-messages.yaml`) — keep the two in sync if the allowed types ever change.

`<type>` MUST be one of:

- `sow` — plant a new entry.
- `tend` — fix broken links, fake links, orphaned pages, etc.
- `fertilize` — expand a thin stub entry.
- `prune` — merge or remove a duplicate entry.
- `graft` — split an overgrown entry into separate pages.
- `entwine` — add missing cross-references between existing entries.
- `weed` — fix something incorrect or harmful (the gardening equivalent of `fix`).
- `uproot` — revert a change (the gardening equivalent of `revert`).
- `landscape` — restructure scripts/CI/tooling without changing behavior (the gardening equivalent of `refactor`).
- `chore`, `format`, `maintenance` — standard types, for changes that aren't about garden content (eg. CI config, dependency bumps, whitespace).

Examples:

```
sow: add entry for event sourcing
fertilize: expand abstraction with examples and modular design xref
tend: fix broken xref in ai-agent.adoc
prune: merge adapative-software-development into adaptive-software-development
entwine: link circuit-breaker and retry as related resilience patterns
weed: correct factual error in acid-principles
uproot: revert accidental merge of draft entry
landscape: restructure commit validation hook for clarity
maintenance: update pre-commit hook versions
```

## Agent skills

This repo has a set of [agent skills](./.agents/skills/README.md) for maintaining the garden — sowing new entries, tending broken links, fertilizing stubs, pruning duplicates, grafting overgrown pages, entwining related entries, and harvesting a digest of recent growth.
