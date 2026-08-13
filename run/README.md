# Run scripts

Bash scripts that drive the `.agents/skills/` agent skills headlessly,
via the Pi coding agent's CLI. If changes are made, the script commits them
to a temporary branch and opens a GitHub PR. The `forage` script is the
exception: foraging is read-only, so it opens a GitHub issue suggesting
entries to sow rather than a PR.

The `pi` CLI is restricted to `read,edit,grep,find,ls`, so it never runs Bash
or Git — those operations are done by the wrapper scripts.

| Breadth | Scripts | Output |
| --- | --- | --- |
| Iterate every page, one PR per page that changed | [`divide`](./divide), [`entwine`](./entwine), [`fertilize`](./fertilize), [`prune`](./prune), [`tend`](./tend), [`tidy`](./tidy), [`uproot`](./uproot) | One PR per page that needed work. Pages with nothing to do are skipped with no branch or PR. |
| Whole-garden pass, single output | [`cultivate`](./cultivate), [`forage`](./forage) | One PR refreshing `TODO.md` (`cultivate`) or one GitHub issue (`forage`), aggregating every page's findings. |
| Single target, argument-driven | [`graft`](./graft), [`sow`](./sow) | One PR for the entry or topic given on the command line. No iteration. |
