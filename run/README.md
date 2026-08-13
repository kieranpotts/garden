# Run scripts

Bash scripts that drive the `.agents/skills/` agent skills headlessly, via the Pi coding agent's CLI. If changes are made, the script commits them to a temporary branch and opens a GitHub PR.

The `pi` CLI is restricted to `read,edit,grep,find,ls`. so it never runs Bash or Git — those operations are done by the wrapper scripts.

| Script | Skill | Scope | Description |
| --- | --- | --- | --- |
| [`divide`](./divide) | [divide](../.agents/skills/divide/SKILL.md) | Per-page | Break a page into separate atomic pages, only if it unambiguously covers multiple concepts. |
| [`entwine`](./entwine) | [entwine](../.agents/skills/entwine/SKILL.md) | Whole garden | Add missing cross-references between existing, related-but-unlinked pages. |
| [`fertilize`](./fertilize) | [fertilize](../.agents/skills/fertilize/SKILL.md) | Per-page | Expand a page into a fuller entry, only if it genuinely qualifies as a thin stub. |
| [`forage`](./forage) | [forage](../.agents/skills/forage/SKILL.md) | Whole garden | Regenerate `TODO.md` with a ranked list of topics mentioned but not yet sown. |
| [`graft`](./graft) | [graft](../.agents/skills/graft/SKILL.md) | Whole garden | Merge related-but-distinct thin entries into a single broader page. |
| [`prune`](./prune) | [prune](../.agents/skills/prune/SKILL.md) | Per-page | Make small, self-evidently-good trims and phrasing fixes within a page. |
| [`sow`](./sow) | [sow](../.agents/skills/sow/SKILL.md) | Single topic (argument) | Plant a brand-new entry for the topic given on the command line. |
| [`tend`](./tend) | [tend](../.agents/skills/tend/SKILL.md) | Per-page | Fix broken cross-references, fake pseudo-links, and orphaned pages, one page at a time. |
| [`tidy`](./tidy) | [tidy](../.agents/skills/tidy/SKILL.md) | Per-page | Fix unambiguous style-guide violations (dashes, colons, casing, bold usage) on a page. |
| [`uproot`](./uproot) | [uproot](../.agents/skills/uproot/SKILL.md) | Per-page | Drop one redundant entry whose topic another entry already covers. |