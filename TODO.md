# TODO

Items raised during cultivate passes (A–R sections so far) that are outside
cultivate's scope (style only) and were flagged rather than fixed. Grouped
roughly by which skill would handle them.

## Duplicate / mergeable pages (prune)

- [x] `robustness-principle.adoc` substantially overlaps `postels-law.adoc`
  (which is already documented as "aka the Robustness Principle").
  `robustness-principle.adoc`'s entire body is just "See
  xref:postels-law.adoc[Postel's law]." — likely a redirect stub that could be
  merged/removed. **Decision: leaving this as-is.**

## Broken or fake cross-references (tend)

- [x] `bottom-up-design.adoc` — bare `[term]` pseudo-links: `[decomposition]`
  and `[conceptual integrity]` converted to real `xref:`; `[evolutionary design]`
  and `[reusability]` left as forage-candidate markers (`*[term]*`); also converted
  `[architectural patterns]` to `xref:architectural-pattern.adoc` and marked
  `[architectural style]` as a forage candidate.
- [x] `design-patterns.adoc` line 25 — malformed xref with a missing closing
  parenthesis in the link text
  (`xref:layered-architecture.adoc[Layered architecture (aka. multi-tiered or n-tier architecture]`).
  Fixed: added the missing `)`.
- [x] `kanban.adoc` line 9 — bare `[Scrum]` and `[Extreme Programming (XP)]`
  mentions converted to real `xref:` (`scrum.adoc`, `extreme-programming.adoc`).
- [x] `makers-schedule.adoc` line 29 — plain-text "Deep work" See-also item;
  `deep-work.adoc` does not exist, so marked as a forage candidate (`*[Deep work]*`).
  Plant a `deep-work.adoc` page to turn it into a real xref.
- [x] `ontology.adoc` — bare `[Protégé]` and `[HybridMDSD]` bracket mentions
  converted to forage-candidate markers (`*[term]*`), matching the convention.
- [x] `pert-chart.adoc` — bare `[Gantt charts]` bracket mention converted to a
  forage-candidate marker (`*[Gantt charts]*`).
- [x] Widespread `*[bracketed term]*` pseudo-links across the C/D-section
  pages — a pass has been run over all listed files. Markers whose topic has a
  matching page were converted to real `xref:`; the rest were left as forage
  candidates. Ambiguous cases (listed below) were left alone for a human decision.

  Conversions made:
  - `cloud-computing.adoc`: `*virtualization*`->`virtualization.adoc`,
    `*[time-sharing]*`->`time-share-computing.adoc`.
  - `complexity.adoc`: `*[monolithic software]*`->`monolith.adoc`.
  - `continuous-deployment.adoc`: `*[delivery pipeline]*`->`deployment-pipeline.adoc`.
  - `crash-only.adoc`: `*[fault-tolerant]*`->`fault-tolerance.adoc`.
  - `cohesion.adoc`: `*[business domain]*`->`domain.adoc`, `*modular*`->`modular-design.adoc`,
    `*coupling*`->`coupling.adoc`, `*domain modeling*`->`domain-model.adoc`.
  - `consistency.adoc`: `*[replicate]*`->`replication.adoc`, `*latency*`->`latency.adoc`,
    `*chaos engineering*`->`chaos-engineering.adoc`, `*idempotent operations*`->`idempotent.adoc`.
  - `containerization.adoc`: `*[stateful]*`->`stateful.adoc`.
  - `cynefin-framework.adoc`: `*[iterative and incremental]*`->`iterative-and-incremental-development.adoc`.
  - `cloud-service-providers.adoc`: table row labels converted where a page
    exists (container orchestration, block storage, file storage, DNS, load
    balancing, firewalls, machine learning, event bus, message queues,
    monitoring, infrastructure as code).
  - `distributed-system.adoc`: `*[peer-to-peer networks]*`->`peer-to-peer-architecture.adoc`,
    `*[client and server]*`->`client-server-architecture.adoc`, `*[scale]*`->`scalability.adoc`,
    `*[resilient]*`->`resilience.adoc`, `*[Asynchronous communication patterns]*`->`asynchronous-communication.adoc`,
    `*[replicate]*`->`replication.adoc`, `*[canary releases]*`->`canary-deployment.adoc`.
  - `domain-driven-design.adoc`: `*[discovery phase]*`->`discovery.adoc`,
    `*[iterative and incremental]*`->`iterative-and-incremental-development.adoc`,
    `*[composed]*`->`composition.adoc`, `*[layered architecture]*`->`layered-architecture.adoc`,
    `*inversion of control*`->`inversion-of-control.adoc`.
  - `domain-model.adoc`: `*[essential complexity]*`->`complexity.adoc`.
  - `durability.adoc`: `*[ACID properties]*`->`acid-principles.adoc`.

  Left as forage candidates (no matching page): `*[practice]*` (continuous-*),
  `*[pattern]*` (cqrs), `*[Erlang/OTP]*` (crash-only), `*[measure]*` (coupling),
  `*[race conditions]*` (consistency), `*[firmware]*` and product names (containerization),
  `*[problem]*` (complexity), and many DDD building-block terms in `domain-driven-design.adoc`.

  Ambiguous (left alone — related page exists but term does not clearly match):
  - `complexity.adoc` `*[qualities]*` — possibly `quality-attributes.adoc`.
  - `consensus-algorithms.adoc` `*[asynchrony]*` — three async pages exist, none clearly covers the general concept.
  - `cloud-service-providers.adoc` `*Serverless*`, `*Blob storage*`, `*RDBMS*`, `*NoSQL*` — synonyms/shorthand.
  - `distributed-system.adoc` `*[points of failure]*`, `*temporal coupling*`, `*[asynchronous]*`.
  - `domain-driven-design.adoc` `*[model-driven design]*`, `*bounded contexts*`, `*ubiquitous language*`, `*[adapters]*`.
- [x] Several bolded terms that already have a dedicated page elsewhere but
  weren't yet linked as `xref:` — converted: "coupling" and "modular"
  (`cohesion.adoc`), "chaos engineering" and "idempotent operations"
  (`consistency.adoc`).

## Naming / title inconsistencies (needs a decision, then tend or manual fix)

- [x] `ports-and-adapters.adoc` — title changed to "Ports and adapters" (no
  hyphens) to match `index.adoc` and `nav.adoc`. The filename
  `ports-and-adapters.adoc` is the kebab-case of "Ports and adapters" and so
  still matches. Hyphenated compound-adjective usage in the prose (eg. "the
  ports-and-adapters pattern") left as-is — it is grammatically correct as a
  modifier.
- [x] `phased-commit.adoc` — title changed to "Phased commit (2PC, 3PC)"
  (singular) to match the filename and `index.adoc`. Opening sentence adjusted
  to "A phased commit is a way to implement..." and "is completed successfully".
- [x] `adaptive-software-development.adoc` — body "Adaptive Software Development
  (ASD)" changed to sentence case to match the page's own title.
- [x] `specification-by-example.adoc` — `index.adoc` and `nav.adoc` link text
  changed from "Specification by Example" to "Specification by example" to match
  the sentence-case page title.

## Maturity labels missing (editorial call, not cultivate's job)

- [x] `raaml.adoc` — added 🌱 to its `index.adoc` line (it is a TODO stub, so
  seedling is the correct default).
- [x] `robustness-principle.adoc` — added 🌱 to its `index.adoc` line as the
  safe default (maturity cannot be inferred without editorial judgment). **The
  page is well-developed — the owner may want to promote it to 🌿 or 🌳.**

## Content defects (not style — needs a human edit)

- [x] `archimate.adoc` — had a bare, unwrapped URL on its own line. Wrapped as
  an AsciiDoc link (`https://www.opengroup.org/archimate-forum/archimate-overview[ArchiMate overview]`).
  Its placement (between title and body) is still awkward — a human may want to
  move it to a See-also or remove it.
- [x] `metcalfes-law.adoc` line 3 — grammar typo: "the value is a network"
  fixed to "the value of a network".
- [x] `modeling.adoc` line 71 — typo: "framworks" -> "frameworks" (actually at
  the IBM Rhapsody entry).
- [x] `modeling.adoc` — the RAAML glossary entry now has a description: "An OMG
  standard modeling language for representing safety and risk analysis concepts,
  built as an extension of UML."
- [ ] `mythical-man-month.adoc` line 36 — `*blog post*` is bold with no link
  attached ("See my *blog post* for a more detailed discussion..."). Still needs
  the actual blog post URL — cannot be fixed without it.
- [x] `processor-architectures.adoc` — "Related links" section listed the same
  Wikipedia IA-32 URL twice. Removed the duplicate.
- [x] `linux.adoc` line 9 — minor grammar slip: "It is core component"
  fixed to "It is a core component".
- [x] Semicolons that are genuine "avoid semicolons" violations, now rewritten:
  `rational-unified-process.adoc` (the three-amigos enumeration converted to a
  bullet list), `replay-attack.adoc` (the sentence-level semicolon on line 11
  split into two sentences), `rest.adoc` (all four split with periods, two in
  prose and two in table cells), `system-design.adoc` (the parenthetical TCP/UDP
  semicolon split with a period — meaning preserved).
  Note: `replay-attack.adoc` also has two list-chaining semicolons (bullets for
  nonces/timestamps/sequence numbers). Those are the "chain list items into one
  flowing enumeration" pattern covered by the style-guide-gap decision below,
  not sentence-level violations, so they were left as-is pending that decision.

## Style guide gaps worth deciding on (would feed back into docs/style-guide.md and the cultivate skill)

- [ ] A repeated, repo-wide `* https://url[Tool Name] — Description.`
  citation-list convention (em dash) appears dozens/hundreds of times across
  many files (seen heavily in A, D, and other sections). The style guide doesn't
  explicitly cover this list/citation idiom. Decide whether to codify it as an
  accepted pattern (and update the style guide + cultivate skill accordingly) or
  mechanically convert it.
- [ ] Bold table-cell header labels (eg. `microservices.adoc`'s comparison
  table: `|*Granularity*`, `|*Communication*`) — don't strictly match any of the
  four accepted bold conventions but mirror an established table-formatting
  pattern seen elsewhere. Decide whether this is a fifth accepted convention.
- [ ] `cynefin-framework.adoc` bolds its five domain names (*Clear*,
  *Complicated*, *Complex*, *Chaotic*, *Disorder*) as a glossary-style
  convention — borderline against "no general emphasis," left as-is pending a
  decision.
- [ ] Book titles in body prose (eg. `rubber-ducking.adoc` line 3 bolds
  `*The Pragmatic Programmer*`) — the style guide has no convention for
  book/publication titles at all (no italics rule, doesn't fit any of the four
  bold conventions). Decide on a convention (italics? bold? plain?) and codify
  it.
- [ ] Semicolons used to chain list items into one flowing enumeration (seen in
  `spoofing.adoc` and `stepwise-refinement.adoc`) — stylistic list structure,
  not flagged as a sentence-level violation, but worth deciding if the "avoid
  semicolons" rule is meant to reach list-item punctuation too.

## Judgment calls on formal-proper-noun exemption (flagged, not changed)

- [ ] `developer-certificate-of-origin.adoc` — title kept as Title Case
  ("Developer Certificate of Origin (DCO)"), treated as a formal legal-document
  proper noun. Confirm this is the intended reading.
- [ ] `iconix.adoc` — title kept as all-caps "ICONIX", treated as the
  methodology's own stylized name.
- [ ] `protocol-buffers.adoc` — title kept as Title Case ("Protocol Buffers",
  Google's named technology), but the page itself is only a TODO stub with no
  body text yet to corroborate the judgment once it's fertilized.
- [ ] `feature-factory.adoc` line 35 — links to `capability-maturity-model.adoc`
  with sentence-case link text ("Capability maturity model") even though the
  target's own title is Title Case under the proper-noun rule. Cross-reference
  link text is normally allowed to read naturally rather than match the target's
  exact title — decide if this specific case should match anyway.
- [ ] `rational-unified-process.adoc` — `*waterfall*` and `*OpenUP*` are bold
  but don't clearly fit a first-use-definition (they're proper nouns naming
  specific things, not generic technical terms like the style guide's own
  examples). Decide whether to keep, unbold, or treat as exempt.

## Structural inconsistency (minor, not yet actioned)

- [x] `feature-factory.adoc` line 33 — "See also" appears as plain bold-less
  text instead of a `== See also` heading, unlike its siblings (`ecmascript`,
  `event-sourcing`, `execution-orchestrator`, `file-storage`, `feature-flags`
  all use `== See also`). Converted to a `== See also` heading.
- [x] `inter-process-communication.adoc` line 5 —
  `*[shared memory] (eg. databases)*` parenthetical moved inside the brackets:
  `*[shared memory (eg. databases)]*`.
