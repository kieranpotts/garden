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

## Agent skills

This repo has a set of [agent skills](./.agents/skills/README.md) for maintaining the garden — sowing new entries, tending broken links, fertilizing stubs, pruning duplicates, grafting overgrown pages, and harvesting a digest of recent growth.
