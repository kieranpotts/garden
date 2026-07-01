---
name: tidy
description: General gardening — a freeform, judgment-driven tidy-up pass over one or more entries. Trim waffle, smooth awkward phrasing, move a paragraph to a better home, merge stray sentences, drop redundancy. Small obvious improvements made inline, without the ceremony of the specific skills. Use when the user says "tidy this up", "give this a once-over", "trim this", or "move this bit somewhere better".
metadata:
  interactive: yes
---

# Tidy

Use this skill for the loose, everyday gardening that doesn't fit a single named operation: trimming waffle, smoothing an awkward sentence, moving a paragraph to where it belongs, deleting a line that repeats what's already been said, tightening a heading. It's the pass a gardener makes walking the beds with secateurs — lots of small, obvious improvements, no grand plan.

Tidy is deliberately low-ceremony. Unlike [graft](../graft/SKILL.md), [split](../split/SKILL.md), or [prune](../prune/SKILL.md) — which change the boundaries of entries and confirm a plan before acting — tidy makes small, self-evidently-good edits directly and reports what it did. It's meant for a human driving interactively, who can see each change and reel it back if they disagree.

**Input**: One or more target pages named by the user (eg. "tidy ai-agent.adoc"), or a selection/region the user points at. If nothing is named, ask what to tidy rather than roaming the whole garden — tidy is a focused pass, not a garden-wide sweep.

**Output**: The target edited in place — tighter, better-ordered, less repetitive — plus a short report of the changes made, so the user can scan and undo any they don't want.

## What counts as a tidy

Do these inline, no confirmation needed:

- **Trim waffle.** Cut filler, hedging, and throat-clearing. Say the same thing in fewer words.
- **Smooth awkward phrasing.** Fix clumsy sentences, bad transitions, tangled clauses — without changing the meaning.
- **Drop local redundancy.** Remove a sentence or clause that repeats something already said on the same page.
- **Move content to a better home *within the same page*.** Reorder paragraphs, pull a stray point into the section it belongs to, merge two half-empty bullets.
- **Tighten headings and lists.** Fix an over-long heading, collapse a one-item list, split a run-on bullet.

## What is NOT a tidy — hand off instead

Stop and point the user at the right skill when a change is bigger than a tidy:

- **Content spans two pages** (moving a section *out* to another entry, or merging entries) — that's [graft](../graft/SKILL.md) (merge related entries) or [split](../split/SKILL.md) (break one entry into several). Tidy stays within a page.
- **Two pages duplicate each other** — that's [prune](../prune/SKILL.md).
- **Broken xrefs, fake pseudo-links, orphaned pages, stale maturity labels** — that's [tend](../tend/SKILL.md)'s mechanical remit.
- **Systematic style-guide conformance** (dashes, colons, casing, bold usage per [docs/style-guide.md](../../../docs/style-guide.md)) — that's [cultivate](../cultivate/SKILL.md). Fixing one glaring style slip in passing is fine; a full style pass is not.
- **Expanding a thin stub with new material** — that's [fertilize](../fertilize/SKILL.md). Tidy tightens what's there, it doesn't grow new content.

If a tidy uncovers one of these, note it in the report as a suggestion — don't start doing it under the guise of tidying.

## Instructions

1.  **Read the target in full.** Understand what the page is for before touching it, so a "tidy" doesn't quietly change the meaning.

2.  **Make the small improvements inline.** Work through the page applying the tidy edits above. Keep each change small and self-evidently an improvement — if you're not sure a change is uncontroversially better, leave it and mention it instead.

3.  **Preserve meaning and voice.** Tidy tightens and reorders; it doesn't rewrite for content or impose a different tone. Match the surrounding style, don't replace it.

4.  **Note anything bigger.** If you spot something that needs graft, split, prune, tend, cultivate, or fertilize, collect it as a suggestion rather than acting on it.

5.  **Report what you did.** List the edits made (grouped loosely — trimmed / smoothed / moved / de-duplicated), and separately list any hand-off suggestions for the specific skills.

## Rules

- **Small and obvious only.** Tidy is for changes that are self-evidently improvements. Anything a reasonable person might disagree with — a rephrasing that shifts emphasis, a cut that loses a nuance — gets proposed, not applied.

- **Stay within the page.** The moment content needs to move *between* pages, it's a graft or a split, not a tidy. Don't create, delete, or merge pages here.

- **Don't change meaning.** Trimming and reordering must leave what the page asserts intact. If tightening a sentence would alter its claim, leave it.

- **Preserve voice.** Match the existing tone and phrasing conventions. Tidy is not a licence to rewrite the page in a different style.

- **Committing is out of scope.** This skill edits files in the working tree only. Staging, committing, and pushing are the user's call — never run `git commit` or `git push` as part of tidying.

## Success criteria

- **The page is tighter and better-ordered** than before, with no waffle or local redundancy left that a quick read would catch.

- **The meaning and voice are unchanged** — only the expression and arrangement improved.

- **No content moved between pages**, and no page was created, merged, or deleted.

- **Anything bigger than a tidy was reported as a hand-off suggestion**, not silently actioned.
