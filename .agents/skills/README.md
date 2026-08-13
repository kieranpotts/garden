# Garden skills

Agent skills for maintaining this digital garden. Each does one gardening task.

| Skill                                  | Summary                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------- |
| [**divide**](./divide/README.md)       | Break up an overgrown entry that's drifted into covering several concepts.              |
| [**entwine**](./entwine/README.md)     | Given one entry, find related entries and intertwine them with cross-references.        |
| [**fertilize**](./fertilize/README.md) | Boost a struggling young plant (a thin stub entry) to strength.                         |
| [**forage**](./forage/README.md)       | Find topics referenced or implied across the digital garden that have no entry yet.     |
| [**graft**](./graft/README.md)         | Merge two or more related-but-distinct entries into one broader entry.                  |
| [**prune**](./prune/README.md)         | Clip waffle, smooth phrasing, drop repetition, and reorder within one entry.            |
| [**sow**](./sow/README.md)             | Research a new topic and plant it as a new seedling entry.                              |
| [**tend**](./tend/README.md)           | General upkeep. Fix broken xrefs, fake pseudo-links, orphans, and stale maturity emoji. |
| [**tidy**](./tidy/README.md)           | Review one entry against the style guide and fix mechanical violations.                 |
| [**uproot**](./uproot/README.md)       | Drop one entry whose topic another entry already covers.                                |
| [**water**](./water/README.md)         | Help grow an established entry by researching its topic afresh.                         |

Every skill instructs the agent to work on a single target entry in the digital
garden. To work across multiple entries, write a prompt that lists the entries
to work on, then instruct the agent to delegate each one to a sub-agent.

Every skill instructs the agent to run non-interactively and to leave its 
changes uncommitted in the Git working tree.
