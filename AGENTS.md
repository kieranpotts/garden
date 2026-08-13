# Garden

A personal digital garden — a curated knowledgebase of atomic notes on
computer science topics, formatted in AsciiDoc. This repo has no build of its
own. It's an Antora content module aggregated and built by the
[`website`](https://github.com/kieranpotts/website) repo.

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Tech stack

- AsciiDoc, structured as an Antora component (`src/antora.yml`).
- No local build, test runner, or package manager — content only.

## Project structure

- [**`src/modules/ROOT/pages/`**](./src/modules/ROOT/pages/) \
  One `.adoc` file per topic. Each is atomic — focused on a single idea or
  concept — and cross-references related topics with `xref:` rather than
  repeating content.

- [**`src/modules/ROOT/pages/index.adoc`**](./src/modules/ROOT/pages/index.adoc) \
  The page listing — every entry MUST be listed here to be discoverable on the
  site.

- [**`src/modules/ROOT/nav.adoc`**](./src/modules/ROOT/nav.adoc) \
  The Antora navigation file, which declares the page hierarchy and drives
  each page's breadcrumb trail. Every entry MUST be listed here too — a page
  missing from `nav.adoc` renders with no ancestry.

- [**`src/antora.yml`**](./src/antora.yml) \
  Antora component descriptor.

- [**`.agents/skills/`**](./.agents/skills/README.md) \
  On-demand agent skills specific to maintaining this garden.

- [**`docs/style-guide.md`**](./docs/style-guide.md) \
  Writing and AsciiDoc formatting conventions for garden entries.

- [**`.github/workflows/`**](./.github/workflows/) \
  CI checks (stale-issue flagging, label sync, commit message validation).

## Tools

No build, lint, or test commands. Validity is structural. Every `xref:` target
must resolve to a real file, and every page must be listed in both `index.adoc`
and `nav.adoc`.

The [`Makefile`](./Makefile) wraps each `.agents/skills/` skill as a `make`
target (`divide`, `entwine`, `fertilize`, `forage`, `graft`, `prune`, `sow`,
`tend`, `tidy`, `uproot`), running it via the matching script in
[`run/`](./run/). Run `make help` for the full list.

## Rules

- Each `.adoc` file MUST cover exactly one topic. Use `xref:` to link rather
  than re-explaining a concept that already has its own page.

- Every page under `src/modules/ROOT/pages/` MUST be listed in both
  `index.adoc` (with its maturity emoji) and `nav.adoc` (the Antora navigation
  file), in the correct alphabetical section. The two files are kept in sync.
  A page added to one is added to the other, and a page removed from one is
  removed from the other.

- New entries MUST be marked 🌱 Seedling. Maturity (🌱 Seedling, 🌿 Budding,
  🌳 Evergreen, 🍂 Decaying) SHOULD only be promoted or demoted with explicit
  user confirmation — it's an editorial judgment, not a mechanical one.

- Filenames MUST be kebab-case and match the page title.

- New and edited entries MUST follow
  [`docs/style-guide.md`](./docs/style-guide.md).

- This repo MUST NOT accept external contributions — see
  [`CONTRIBUTING.md`](./CONTRIBUTING.md).

- Agent skills in `.agents/skills/` MUST NOT commit or push changes. They edit
  the working tree only. Staging, committing, and pushing are always the
  user's call.

## Skills

The [`.agents/skills/`](./.agents/skills/) directory provides on-demand skills
for managing this repository. See the [`README`](./.agents/skills/README.md) in
that directory for descriptions of the available skills and the situations
when you should use them.

`.claude/skills` is a symlink to `.agents/skills` for auto-discovery by
Claude Code.

## References

The following technical standards apply.

- [**TS-9: Version Control**](https://kieranpotts.com/standards/009)
- [**TS-26: Technical Writing Style Guide**](https://kieranpotts.com/standards/026)
- [**TS-28: AsciiDoc**](https://kieranpotts.com/standards/028)
- [**TS-61: AI Tools**](https://kieranpotts.com/standards/061)
