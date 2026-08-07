# Garden skills

Agent skills for maintaining this digital garden. Each does one gardening task.

| Skill                              | Summary                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------- |
| [cultivate](./cultivate/README.md) | Review one entry against the style guide and fix the mechanical violations.                  |
| [entwine](./entwine/README.md)     | Given one entry, find related entries and add the missing cross-references.                  |
| [fertilize](./fertilize/README.md) | Bring a thin stub entry up to strength, without changing its scope.                          |
| [forage](./forage/README.md)       | Find topics referenced or implied across the garden that have no entry yet.                  |
| [graft](./graft/README.md)         | Merge two or more related-but-distinct entries into one broader entry.                       |
| [harvest](./harvest/README.md)     | Produce a digest of recent garden activity, from the Git history.                            |
| [prune](./prune/README.md)         | Drop one entry whose topic another entry already covers.                                     |
| [sow](./sow/README.md)             | Research a new topic and plant it as a new entry.                                            |
| [split](./split/README.md)         | Break up an overgrown entry that's drifted into covering several concepts.                   |
| [tend](./tend/README.md)           | Fix broken cross-references, fake pseudo-links, orphans, and stale maturity emoji.           |
| [trim](./trim/README.md)           | Trim waffle, smooth phrasing, drop repetition, and reorder within one entry.                 |
| [water](./water/README.md)         | Research an established entry's topic afresh, and extend it with new depth.                  |

Every skill is non-interactive and leaves its changes uncommitted in the Git
working tree. Reviewing the diff is how you approve the work. No skill changes
an entry's maturity emoji: they recommend, you decide.

See each skill's own `SKILL.md` for the full instructions an agent follows, and
`README.md` for invocation examples.
