---
name: tend
description: >-
  Check one target entry's structural health — unresolvable cross-references,
  fake bracketed pseudo-links, a missing index or nav listing, and a maturity
  emoji that no longer matches the content — then fix what is mechanical and
  report the rest. Use this skill when the user says something like "tend
  event-sourcing.adoc", "check this entry for broken links", or asks to tend a
  particular page. Do not use it to write or reword an entry's prose.
compatibility: requires Read, Glob, Grep, Edit
license: CC0-1.0
---

# Tend

Inspect a single garden entry for withering content — broken cross-references,
fake pseudo-links, a missing index or nav listing, and a stale maturity emoji —
then apply the unambiguous fixes and report everything else. Tending repairs
structure. It never grows content.

## Parameters

Determine the following information from the surrounding context and
environment. You MUST NOT prompt the user for clarification on this task's
requirements. If you cannot determine the requirements, stop and alert the
user with an error message.

- **Target entry — REQUIRED.** A single file under `src/modules/ROOT/pages/`.
  The page may be referenced by its title, which you will need to resolve to
  its kebab-case filename. Tending inspects this entry only.

## Success criteria

- Every `xref:` target in the target entry MUST have been checked against the
  actual file inventory, and each unresolvable one reported.

- Every bracketed pseudo-link in the target entry MUST have been checked for
  a matching entry, and converted to a real `xref:` wherever one exists.

- The target entry MUST have been checked for a listing in both
  `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc`.

- No `xref:` MAY have been repointed to a target that was guessed rather than
  established.

- No maturity emoji in the index MUST have changed.

- The report MUST separate the fixes already applied from the items still
  needing the user's decision.

- Nothing MUST be staged, committed, or pushed.

## Instructions

1.  Inventory the garden. List every `.adoc` file under
    `src/modules/ROOT/pages/`. This is the ground truth for steps 2 and 3, and
    it confirms the target entry itself exists.

2.  Find unresolvable cross-references. Grep the target entry for `xref:`
    targets, pattern `xref:([a-z0-9-]+\.adoc)`, and confirm each names a file
    in the inventory. A target that does not is a dead link, left behind by a
    rename, a removal, or an entry that was never planted.

3.  Find fake pseudo-links. The target entry may carry bracketed text that
    looks like a cross-reference but is not AsciiDoc `xref:` syntax, eg.
    `*[modular design]*` where `*xref:modular-design.adoc[Modular design]*`
    was meant. Search for bracketed text not preceded by `xref:` or a URL
    scheme. Where the inventory holds a matching entry, convert it. Where it
    does not, the bracketed term is a deliberate marker for a topic not yet
    planted — report it as such and leave it alone.

4.  Check the entry's listings. Confirm the target entry appears in both
    `src/modules/ROOT/pages/index.adoc` and `src/modules/ROOT/nav.adoc`. An
    entry missing from the index has no discoverable path from the front page.
    An entry missing from the nav renders with no ancestry and no breadcrumb
    trail. Report each absence with the section you would file it under —
    placement is a taxonomy judgment, so propose it rather than applying it.

5.  Check the maturity emoji. Compare the target entry against its emoji in
    the index and flag any mismatch.

    - A 🌱 Seedling that is substantial, well-linked, and carries no
      `// TODO` marker — a candidate for 🌿 Budding or 🌳 Evergreen.

    - An entry carrying a `// TODO` marker, or noticeably thinner than its
      peers, still marked 🌿 Budding or 🌳 Evergreen — a candidate for
      demotion, or for 🍂 Decaying if it looks abandoned.

6.  Apply the unambiguous fixes. Repoint a broken `xref:` only where the
    intended target is beyond doubt, such as an exact rename or an obvious
    typo. Convert a pseudo-link only where a matching entry genuinely exists.
    Leave everything else for the user.

7.  Report what was found, what was fixed, and what needs a decision,
    grouped as broken cross-references, fake pseudo-links, listing problems,
    and stale maturity emoji.

## Rules

- You MUST NOT invent a destination for a dead link. A broken `xref:` with no
  obvious correct target is reported, never guessed at. Silently repointing a
  link at the wrong entry is harder to notice, and harder to undo, than
  leaving it dead.

- You MUST NOT change an entry's maturity emoji in the index. Maturity is an
  editorial judgment the user reserves. Surface the evidence — `// TODO`
  markers, body length, link density — and let the user decide.

- You MUST NOT write or reword an entry's prose. Where a repair would mean
  composing new content, such as an index description or an entry that does
  not exist yet, do the mechanical part and report the rest. Tending repairs
  structure, and mixing prose changes into a structural diff makes both
  harder to review.

- You MUST tend one entry at a time. A garden-wide structural sweep produces a
  diff too large to review, which defeats the working tree as a review gate.
  To tend several entries, run the skill once per entry, or delegate each to
  a sub-agent.

- You MUST NOT stage, commit, or push. Leave every change in the Git working
  tree. Reviewing the diff is how the user approves the work, so it stands in
  for any mid-flow prompt.

## Edge cases

- A bracketed term has no matching entry. This is the garden's convention for
  marking a topic worth planting later, not a defect. Report it as a
  candidate and leave the markup as it is.

- The target entry shares its topic with another entry under a different
  name. Tending does not resolve redundancy. Report the pair, with which
  looks fuller, and leave both in place for a dedicated merge or drop pass.