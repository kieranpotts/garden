# Run scripts

Bash scripts that drive the `.agents/skills/` agent skills headlessly,
via the Pi coding agent's CLI. If changes are made, the script commits them
to a temporary branch and opens a GitHub PR. The `forage` script is the
exception: foraging is read-only, so it opens a GitHub issue suggesting
entries to sow rather than a PR.

The `pi` CLI is restricted to `read,edit,grep,find,ls`, so it never runs Bash
or Git — those operations are done by the wrapper scripts.

| Script | Skill | Scope | Description |
| --- | --- | --- | --- |
| [`divide`](./divide) | [divide](../.agents/skills/divide/SKILL.md) | Per-page | Break a page into separate atomic pages, only if it unambiguously covers multiple concepts. |
| [`entwine`](./entwine) | [entwine](../.agents/skills/entwine/SKILL.md) | Per-page | Add missing cross-references between one page and its related-but-unlinked neighbours. |
| [`fertilize`](./fertilize) | [fertilize](../.agents/skills/fertilize/SKILL.md) | Per-page | Expand a page into a fuller entry, only if it genuinely qualifies as a thin stub. |
| [`forage`](./forage) | [forage](../.agents/skills/forage/SKILL.md) | Per-page | Open a GitHub issue suggesting entries to sow, foraging each page for topics with no entry yet. |
| [`graft`](./graft) | [graft](../.agents/skills/graft/SKILL.md) | Two entries (arguments) | Absorb one dead-head entry into a target entry, repointing references and removing the dead-head. |
| [`prune`](./prune) | [prune](../.agents/skills/prune/SKILL.md) | Per-page | Make small, self-evidently-good trims and phrasing fixes within a page. |
| [`sow`](./sow) | [sow](../.agents/skills/sow/SKILL.md) | Single topic (argument) | Plant a brand-new entry for the topic given on the command line. |
| [`tend`](./tend) | [tend](../.agents/skills/tend/SKILL.md) | Per-page | Fix broken cross-references, fake pseudo-links, and orphaned pages, one page at a time. |
| [`tidy`](./tidy) | [tidy](../.agents/skills/tidy/SKILL.md) | Per-page | Fix unambiguous style-guide violations (dashes, colons, casing, bold usage) on a page. |
| [`uproot`](./uproot) | [uproot](../.agents/skills/uproot/SKILL.md) | Per-page | Drop one redundant entry whose topic another entry already covers. |