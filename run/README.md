# Run scripts

Bash scripts that drive the `.agents/skills/` agent skills headlessly,
via the Pi coding agent's CLI. If changes are made, the script commits them
to a temporary branch and opens a GitHub PR.

The `pi` CLI is restricted to `read,edit,grep,find,ls`, so it never runs Bash
or Git — those operations are done by the wrapper scripts.
