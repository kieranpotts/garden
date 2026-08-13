---
name: water
description: >-
  Research an established entry's topic afresh and extend the page with new
  depth, detail, and developments, without widening its scope. Use this skill
  when the user says something like "water event-sourcing.adoc", "research
  and extend the resilience entry", or asks to grow an established page with
  more depth. Do not use it to rescue a thin stub or to plant a topic that has
  no entry yet.
compatibility: >-
  requires Read, Glob, Grep, Edit, WebSearch, WebFetch
license: CC0-1.0
---

# Water

Research an existing entry's topic afresh and extend the entry with new depth,
detail, and developments. Watering grows the plant that is already there — it
must not graft a different one onto it.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename.

- **Emphasis — OPTIONAL.** A particular angle the user wants grown, eg.
  recent developments, worked examples, trade-offs. If not specified, default 
  to whichever facets the entry is thinnest on.

## Success criteria

- The target entry MUST still carry the same title, filename, and core
  concept as before, now with more depth or breadth.

- The added material MUST be genuinely additive, not a restatement of what
  the entry already said.

- Every `xref:` you add, in the target entry and in entries linking back to
  it, MUST name a file that exists under `src/modules/ROOT/pages/`.

- Additional concepts SHOULD NOT have been folded in. Separate concepts are 
  separate entries.

- No maturity emoji in `src/modules/ROOT/pages/index.adoc` MUST have
  changed.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Read the target entry in full. Understand its current scope and claims, so 
    new material extends the entry rather than repeating it.

2.  Check the entry is already well established, not a stub/seedling. A body of 
    a few sentences, with unresolved `// TODO` markers, or almost no outbound 
    links, means the entry needs rescuing rather than growing. Stop
    and suggest the user invoke the `fertilize` skill instead.

3.  Research the topic. Gather understanding beyond what the entry already 
    carries: deeper detail, recent developments, additional facets, worked 
    examples, trade-offs, common pitfalls. Prefer a small number of reliable 
    sources over breadth.

4.  Find adjacent topics already in the garden. Growth usually surfaces new 
    cross-reference opportunities: related patterns, prerequisites, contrasting 
    approaches. Search existing entries for concepts that should now be linked, 
    outbound from this entry and inbound from those. Note their exact filenames. 
    An AsciiDoc `xref:` target must match a real file.

5.  Extend the entry. Weave the new material into the existing structure, in 
    place. Link out via `xref:` rather than re-explaining a concept that has its 
    own entry. Follow the [style guide](../../../docs/style-guide.md), wrapping 
    every `xref:` in `*...*`.

6.  Add the cross-references from step 4, in both directions where each
    reads naturally in its host entry's context.

7.  Report what was added, which links were made, and whether the entry's
    maturity emoji now looks understated.

## Rules

- You MUST keep the entry on its existing concept.

  Watering grows the established plant. If research surfaces a genuinely
  distinct concept, it belongs in a separate entry, cross-linked — or the
  entry has outgrown itself and should be broken up. Either way, report it
  rather than smuggling a second concept in here.

- You MUST link rather than duplicate.

  Where a concept is already explained elsewhere, `xref:` to it instead of
  re-explaining it. The value of the garden is in the connections between
  atomic notes, not in self-contained essays.

- You MUST NOT change an entry's maturity emoji in the index.

  Maturity is an editorial judgment the user reserves. Recommend a promotion
  in your report and leave the label as it stands.

- You MUST NOT stage, commit, or push.

  Leave every change in the Git working tree. Reviewing the diff is how the
  user approves the work, so it stands in for any mid-flow prompt.

## Edge cases

- Research contradicts something the entry already asserts.

  Do not quietly overwrite the claim. Correct it, and call the correction
  out explicitly in your report, naming the source — a factual fix is a
  different kind of change from growth, and the user will want to see it.

- The entry is already long and well-developed.

  Prefer depth over volume. Sharpen and extend the weakest facets rather
  than padding an entry that is already at the limit of one concept, and say
  in your report if the entry looks ready to be broken up instead.
