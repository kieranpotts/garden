---
name: classify
description: >-
  Compare one target entry against its maturity emoji in the index and flag
  any mismatch — a substantial, well-linked 🌱 Seedling ready for promotion,
  or a 🌿 Budding or 🌳 Evergreen entry that has thinned or gone stale. Use
  this skill when the user says something like "classify event-sourcing.adoc",
  "is this entry still a seedling?", "check the maturity of this page", or
  asks whether an entry's maturity marker still fits. Do not use it to change
  the emoji itself — that is the user's editorial call.
compatibility: requires Read, Glob, Grep
license: CC0-1.0
---

# Classify

Compare one garden entry against its maturity emoji in the index and report
whether the two still agree. Classifying reports; it does not edit. Maturity
(🌱 Seedling, 🌿 Budding, 🌳 Evergreen, 🍂 Decaying) is an editorial judgment
the user reserves, so this skill surfaces evidence and a recommendation, never
a change.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename. Classifying inspects this entry only.

## Success criteria

- The target entry's current maturity emoji MUST have been read from
  `src/modules/ROOT/pages/index.adoc`.

- The entry MUST have been checked for the evidence that bears on maturity —
  `// TODO` markers, body length and depth, and outbound `xref:` link
  density — compared against its peers where useful.

- The report MUST state either that the current emoji still fits, or
  recommend a specific replacement, with the evidence for it.

- No maturity emoji in the index MUST have changed.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the target entry in full. Understand its scope, depth, and current
    state.

2.  Find the entry's current maturity emoji in
    `src/modules/ROOT/pages/index.adoc`.

3.  Gather the evidence:

    - Presence of any `// TODO` marker in the body.
    - Rough body length and depth of explanation, compared against a couple
      of peer entries of the same nominal maturity, if useful for context.
    - Count of outbound `xref:` links — a well-linked entry sits inside the
      garden's web; an isolated one does not.

4.  Judge the entry against its current emoji:

    - A 🌱 Seedling that is substantial, well-linked, and carries no `// TODO`
      marker is a candidate for promotion to 🌿 Budding or 🌳 Evergreen.

    - An entry carrying a `// TODO` marker, or noticeably thinner than its
      peers, still marked 🌿 Budding or 🌳 Evergreen is a candidate for
      demotion — to 🌱 Seedling, or to 🍂 Decaying if it looks abandoned
      rather than merely young.

    - An entry whose evidence matches its current emoji needs no change.
      Report this plainly — agreement is a valid, positive result.

5.  Report the current emoji, the evidence gathered, and either "no change"
    or the recommended emoji with the reasoning behind it.

## Rules

- You MUST classify one entry at a time. A garden-wide maturity sweep
  produces a report too large to act on in one sitting. To classify several
  entries, run the skill once per entry, or delegate each to a sub-agent.

- You MUST NOT change an entry's maturity emoji in the index. Maturity is an
  editorial judgment the user reserves. Surface the evidence — `// TODO`
  markers, body length, link density — and let the user decide.

- You MUST NOT write or reword an entry's prose. Classifying judges maturity;
  it does not improve the entry toward a higher tier.

- You MUST NOT stage, commit, or push. Leave the working tree untouched.
  Reviewing the report is how the user decides whether to act on it.

## Edge cases

- The entry is brand new and marked 🌱 Seedling with no issues beyond youth.
  Report "no change" — youth alone is not evidence of readiness for
  promotion.

- The entry looks thin but the topic itself is narrow and complete at that
  length. Do not recommend demotion on length alone — weigh it against
  `// TODO` markers and link density too, and say so in the reasoning.

- The entry's peers of the same nominal maturity vary widely in depth.
  Prefer the entry's own evidence — `// TODO` markers, link density,
  completeness — over a peer comparison that may itself be inconsistent.
