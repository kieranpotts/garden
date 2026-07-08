# Garden

A personal digital garden — a curated knowledgebase of atomic notes on computer
science topics, formatted in AsciiDoc. This repo has no build of its own; it's
an Antora content module aggregated and built by the
[`website`](https://github.com/kieranpotts/website) repo.

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Tech stack

- AsciiDoc, structured as an Antora component (`src/antora.yml`).
- No local build, test runner, or package manager — content only.

## Project structure

- **`src/modules/ROOT/pages/`**: One `.adoc` file per topic. Each is atomic —
  focused on a single idea or concept — and cross-references related topics with
  `xref:` rather than repeating content.

- **`src/modules/ROOT/pages/index.adoc`**: The only page listing — every entry MUST
  be listed here to be discoverable on the site.

- **`src/antora.yml`**: Antora component descriptor.

- **[`.agents/skills/`](./.agents/skills/README.md)**: On-demand agent skills
  specific to maintaining this garden.

- **[`docs/style-guide.md`](./docs/style-guide.md)**: Writing and AsciiDoc
  formatting conventions for garden entries..

- **`.github/workflows/`**: CI checks (stale-issue flagging, label sync, commit
  message validation).

## Tools

No build, lint, or test commands. Validity is structural: every `xref:` target
must resolve to a real file, and every page must be listed in `index.adoc`.

## Rules

- Each `.adoc` file MUST cover exactly one topic. Use `xref:` to link rather
  than re-explaining a concept that already has its own page.

- Every page under `src/modules/ROOT/pages/` MUST be listed in `index.adoc`, in
  the correct alphabetical section.

- New entries MUST be marked 🌱 Seedling. Maturity (🌱 Seedling, 🌿 Budding, 🌳
  Evergreen, 🍂 Decaying) SHOULD only be promoted or demoted with explicit user
  confirmation — it's an editorial judgment, not a mechanical one.

- Filenames MUST be kebab-case and match the page title.

- New and edited entries MUST follow
  [docs/style-guide.md](./docs/style-guide.md).

- This repo MUST NOT accept external contributions — see
  [CONTRIBUTING.md](./CONTRIBUTING.md).

- Agent skills in `.agents/skills/` MUST NOT commit or push changes. They edit
  the working tree only; staging, committing, and pushing are always the user's
  call.

## Skills

Skills specific to this project are installed in
[.agents/skills/](./.agents/skills/). They are named with gardening metaphors:
`sow`, `water`, `tend`, `fertilize`, `prune`, `graft`, `split`, `entwine`,
`forage`, `harvest`, `cultivate`, `trim`.
