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

- [ ] `bottom-up-design.adoc` — bare `[term]` pseudo-links: `[decomposition]`
  and `[conceptual integrity]` have real target pages and should become real
  `xref:`; `[evolutionary design]` and `[reusability]` have no target page yet.
- [ ] `design-patterns.adoc` line 25 — malformed xref with a missing closing
  parenthesis in the link text
  (`xref:layered-architecture.adoc[Layered architecture (aka. multi-tiered or n-tier architecture]`).
- [ ] `kanban.adoc` line 9 — bare `[Scrum]` and `[Extreme Programming (XP)]`
  mentions, neither real xrefs nor forage-candidate markers.
- [ ] `makers-schedule.adoc` line 29 — plain-text "Deep work" See-also item;
  should link to `deep-work.adoc` if that page exists.
- [ ] `ontology.adoc` — bare `[Protégé]` and `[HybridMDSD]` bracket mentions,
  inconsistent with the `*[term]*` forage-candidate convention.
- [ ] `pert-chart.adoc` — bare `[Gantt charts]` bracket mention, same issue.
- [ ] Widespread `*[bracketed term]*` pseudo-links across many C/D-section pages
  (`cloud-computing`, `complexity`,
  `continuous-deployment/integration/delivery`, `cqrs`, `crash-only`,
  `cohesion`, `commit-early-commit-often`, `consistency`,
  `consensus-algorithms`, `containerization`, `cynefin-framework`, `coupling`,
  `crc-card`, `critical-path-analysis`, `cloud-service-providers`,
  `distributed-system`, `domain-driven-design`, `domain-model`, `durability`) —
  some targets already exist as real pages and could become genuine xrefs.
- [ ] Several bolded terms that already have a dedicated page elsewhere but
  aren't yet linked as `xref:` — eg. "coupling", "modular", "chaos engineering",
  "idempotent operations" (seen in
  `cohesion.adoc`/`coupling.adoc`/`consistency.adoc`).

## Naming / title inconsistencies (needs a decision, then tend or manual fix)

- [ ] `ports-and-adapters.adoc` — page title says "Ports-and-adapters"
  (hyphenated) but `index.adoc` lists it as "Ports and adapters" (no hyphens),
  and both forms are used interchangeably in the prose. Pick one and make
  consistent.
- [ ] `phased-commit.adoc` — filename is singular ("phased-commit") but the page
  title says "Phased commits (2PC, 3PC)" (plural) and `index.adoc` says "Phased
  commit (2PC, 3PC)" (singular). Pick one form.
- [ ] `adaptive-software-development.adoc` — body text says "Adaptive Software
  Development (ASD)" in Title Case mid-sentence, inconsistent with the page's
  own sentence-case title ("Adaptive software development (ASD)").
- [ ] `specification-by-example.adoc` — page title is correctly sentence case
  ("Specification by example") but `index.adoc` lists it as "Specification by
  Example" (Title Case). Pick one and make consistent.

## Maturity labels missing (editorial call, not cultivate's job)

- [ ] `raaml.adoc` — its `index.adoc` listing line has no maturity emoji
  (🌱/🌿/🌳/🍂), unlike every sibling entry.
- [ ] `robustness-principle.adoc` — same issue, no maturity emoji in its
  `index.adoc` listing line.

## Content defects (not style — needs a human edit)

- [ ] `archimate.adoc` — has a bare, unwrapped URL on its own line (not an
  `xref:` or AsciiDoc link).
- [ ] `metcalfes-law.adoc` line 3 — grammar typo: "the value is a network"
  should read "the value of a network".
- [ ] `modeling.adoc` line 71 — typo: "framworks" → "frameworks".
- [ ] `modeling.adoc` line 41 — the RAAML glossary entry has no description,
  unlike its sibling entries.
- [ ] `mythical-man-month.adoc` line 18 — `*blog post*` is bold with no link
  attached; looks like a forgotten link target.
- [ ] `processor-architectures.adoc` — "Related links" section lists the same
  Wikipedia IA-32 URL twice.
- [ ] `linux.adoc` line 9 — minor grammar slip: "It is core component" (missing
  article "a").
- [ ] Semicolons that are genuine "avoid semicolons" violations but need a
  sentence rewrite (not a mechanical fix) rather than a silent split:
  `rational-unified-process.adoc`, `replay-attack.adoc` (×2), `rest.adoc` (×4),
  `system-design.adoc` line 43 (semicolon inside a long, nested parenthetical
  aside about TCP vs UDP — risky to split mechanically without changing
  meaning).

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

- [ ] `feature-factory.adoc` line 33 — "See also" appears as plain bold-less
  text instead of a `== See also` heading, unlike its siblings (`ecmascript`,
  `event-sourcing`, `execution-orchestrator`, `file-storage`, `feature-flags`
  all use `== See also`).
- [ ] `inter-process-communication.adoc` line 5 —
  `*[shared memory] (eg. databases)*` has the parenthetical outside the `[...]`
  brackets but inside the bold wrapper, a minor formatting oddity in the
  forage-candidate convention.
