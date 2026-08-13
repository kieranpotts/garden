---
name: cultivate
description: >-
  Read one target entry and triage it, recommending which skills, if any, would
  improve it — watering, fertilizing, dividing, entwining, tending, tidying,
  pruning, grafting, or uprooting — with a one-line reason per recommendation.
  Use this skill when the user says something like "cultivate
  event-sourcing.adoc", "what does this entry need?", or asks for a triage of one
  page. Do not use it to make the changes itself — it is read-only and reports
  recommendations only.
compatibility: requires Read, Glob, Grep
license: CC0-1.0
---

# Cultivate

Read one garden entry and triage it: recommend which skills, if any, would
improve it, with a one-line reason per recommendation. Cultivating reports; it
does not edit. Each recommendation names a skill and the evidence for it, so the
user can follow up with that skill on this entry.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename. Triage inspects this entry only.

## Success criteria

- Every recommendation MUST name one of the garden's improvement skills
  (`water`, `fertilize`, `divide`, `entwine`, `tend`, `tidy`, `prune`, `graft`,
  `uproot`) and give a one-line reason grounded in evidence from the entry or
  the garden inventory.

- The report MUST cover every skill's criterion, stating "no action" where the
  entry passes, so the user can see the triage was complete rather than
  assuming a skill was skipped.

- A recommendation that depends on a second entry (`entwine`, `graft`,
  `uproot`) MUST be flagged as a candidate to confirm rather than stated as
  fact, since this skill does not read the partner entry in full.

- No recommendation MAY be made where the entry passes a skill's criterion.

- No file in the repository MUST have been created, edited, or deleted.

## Instructions

1.  Read the target entry in full. Understand its subject, scope, and current
    state before judging it.

2.  Inventory the garden. List every `.adoc` file under
    `src/modules/ROOT/pages/`, with its `=` title. This is the ground truth for
    judging redundancy and the link neighbourhood, and it confirms the target
    exists.

3.  Assess the entry against each improvement skill's criterion, in turn.

    - **fertilize** — a thin stub: short body, `// TODO` markers, few outbound
      `xref:` links, 🌱 or 🌿 maturity. Recommend fertilize where the entry is
      young and underdeveloped.

    - **water** — an established entry thin on depth, recency, examples, or
      trade-offs. Recommend water where the entry is past stub stage but a
      facet is shallow. Where the entry is a stub, prefer fertilize.

    - **divide** — the entry covers two or more concepts that could each stand
      alone and would be cross-referenced from more than one other entry.
      Recommend divide only where the split is genuine, not where the entry is
      merely long.

    - **tidy** — style-guide violations: dash and colon usage, heading case,
      stray bold, an `xref:` not wrapped in `*...*`. Recommend tidy where
      mechanical violations are present.

    - **tend** — broken `xref:` targets, fake bracketed pseudo-links, a missing
      `index.adoc` or `nav.adoc` listing, or a maturity emoji that no longer
      matches the content. Recommend tend where a structural defect is present.

    - **prune** — waffle, local repetition, or poor ordering that a careful
      read would catch. Recommend prune where the prose reads baggy but the
      meaning is right.

    - **entwine** — few or no outbound links, or related concepts named in
      prose with no `xref:` and no bracketed marker. Flag as a candidate;
      entwine needs the neighbour entries to confirm the links belong.

    - **graft** — the entry and another cover one broader theme together and
      would read better as a single entry. Flag as a candidate, naming the
      likely partner; graft needs the partner confirmed and the survivor
      chosen.

    - **uproot** — the entry's topic may already be covered by another entry,
      with nothing unique here. Flag as a candidate, naming the likely covering
      entry; uproot needs the covering entry confirmed and a check that nothing
      unique is lost.

4.  For each criterion, record either a recommendation (skill name + one-line
    reason citing the evidence) or "no action".

5.  Report the recommendations as a list, grouped by skill, each with its
    one-line reason. Lead with the strongest recommendation. Where the entry
    passes every criterion, say so plainly — a clean entry is the goal, and an
    empty recommendation list is a positive result.

## Rules

- You MUST cultivate one entry at a time. Garden-wide triage is done by running
  the skill once per entry, or delegating each to a sub-agent.

- You MUST NOT make changes. Cultivating is read-only; the named skill does the
  work in a follow-up run. Editing the entry here would pre-empt the review the
  working-tree diff is meant to give.

- You MUST ground each recommendation in evidence from the entry or the garden
  inventory, not a guess. A recommendation the user cannot check against the
  entry is worse than none.

- You MUST flag candidate recommendations (`entwine`, `graft`, `uproot`) as
  needing confirmation, since they depend on entries this skill does not read
  in full. State the likely partner and let the named skill confirm.

- You MUST NOT recommend `sow`. Sowing plants new topics; cultivating improves
  existing entries. Missing linked topics are a `forage` finding, not a
  cultivate recommendation.

- You MUST NOT change a maturity emoji, and you MUST NOT stage, commit, or
  push. Leave the working tree untouched. Reviewing the report is how the user
  decides what to run next.

## Edge cases

- The entry is already in good shape. Report "no action" across the board, and
  say so plainly. A clean entry is the goal, not a missed recommendation.

- The entry is a brand-new seedling with no issues beyond youth. Report "no
  action" — youth is not a defect, and growth comes through use, not a forced
  skill.

- `fertilize` and `water` both seem to apply. Prefer the one matching the
  entry's stage: a thin stub wants `fertilize`, an established entry wants
  `water`. State the choice and the reason in the report.

- `uproot` and `graft` both seem to apply. `uproot` is for an entry that adds
  nothing another entry lacks; `graft` is for an entry whose distinct content
  belongs with another's. Pick the one matching the relationship and flag it as
  a candidate for the named skill to confirm.