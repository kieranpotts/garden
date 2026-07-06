---
name: water
description: Research an existing garden entry's topic afresh and extend the page with new depth, detail, and developments — like sow, but for an entry that already exists. Use when the user says "water event-sourcing.adoc", "research and extend this entry", or wants an established page grown further. For rescuing a thin stub, use fertilize instead.
metadata:
  interactive: no
---

# Water

**Input**: A single existing entry named by the user (eg. "water
event-sourcing.adoc"). Do not block to ask the user questions. Make your
proposed edits and leave them in the Git working tree for the user to decide
what to do with them.

**Output**: The target `.adoc` file extended with additional researched content
and new cross-references, staying on its existing concept, with its maturity
label in `index.adoc` reconsidered if the growth warrants it.

##  Instructions

1.  **Read the existing entry in full.**

    Understand its current scope, claims, and what it already covers, so new
    material extends the entry rather than repeating what's already there.

2.  **Research the topic.**

    Gather understanding beyond what's already on the page — deeper detail,
    recent developments, additional facets, worked examples, trade-offs, common
    pitfalls. Prefer a small number of reliable sources over breadth. This is a
    knowledgebase entry, not a survey paper.

3.  **Find adjacent topics already in the garden.**

    As the entry grows, new cross-reference opportunities usually surface
    (related patterns, prerequisites, contrasting approaches). Search existing
    pages for concepts that should now be linked, both outbound from this entry
    and inbound from those pages. Note their exact filenames — AsciiDoc `xref:`
    targets must match real files.

4.  **Extend the entry.**

    Weave the new material into the existing structure, in place. Keep it on the
    same concept — water grows the existing plant, it doesn't graft a different
    one on. Link out via `xref:` rather than re-explaining concepts that already
    have their own page. Keep it atomic: if the research surfaces a genuinely
    distinct concept, that's a new entry ([sow](../sow/SKILL.md)) cross-linked
    back, or a [split](../split/SKILL.md) — not a new section here.

5.  **Link it back in.**

    Add the new `xref:` links found in step 3, in both directions where it's a
    natural fit — the garden is most useful when paths run both ways.

6.  **Reconsider the maturity label.**

    If watering has grown the entry substantially, propose promoting its emoji
    in `index.adoc` (eg. 🌱 → 🌳). Confirm with the user before changing it —
    maturity is an editorial call.

7.  **Report back.**

    Summarize what was added, new links made, and whether the maturity label
    changed.

##  Rules

-   **Extend, don't rescue.**

    Water grows an already-established entry. If the target is a thin stub with
    known gaps or unresolved `// TODO` markers, that's
    [fertilize](../fertilize/SKILL.md)'s job — hand it off rather than doing a
    rescue here.

-   **Stay on the entry's concept.**

    If research surfaces a genuinely distinct concept, [sow](../sow/SKILL.md) a
    separate entry and cross-link it, or flag the page for
    [split](../split/SKILL.md) — don't smuggle a second concept into this page.

-   **Prefer linking over duplicating.**

    If a concept is already explained on another page, link to it with `xref:`
    instead of re-explaining it. The value of the garden comes from connections
    between atomic notes, not self-contained essays.

-   **Maturity promotion needs confirmation.**

    Never bump a maturity emoji in `index.adoc` without the user agreeing the
    grown page has earned it.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing
    are the user's call.

##  Success criteria

-   **The entry covers the same core concept as before**, now with more depth or
    breadth — same topic, same title, same filename.

-   **The new material is genuinely additive**, not a restatement of what the
    page already said.

-   **All `xref:` targets resolve** — every `xref:foo.adoc[...]` added (in this
    page or in pages linking back to it) corresponds to a real file in
    `src/modules/ROOT/pages/`.

-   **No genuinely distinct new concept was folded in** — anything that big
    became a sow or a split instead.

-   **No maturity label changed without explicit user confirmation.**
