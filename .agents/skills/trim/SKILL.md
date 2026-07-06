---
name: trim
description: Everyday gardening. Follow this skill when you're requested to do a freeform, judgment-driven trim over one discrete entry in the garden. This is about making small trimmings while walking the garden with secateurs in hand: trim waffle, smooth awkward phrasing, move a paragraph to a better home, merge stray sentences, drop redundancy. Use when the user says "trim this", "tidy this up", "give this a once-over", "move this bit somewhere better", "trim agent.adoc" or "trim the section on AI agents".
metadata:
  interactive: no
---

# Trim

**Input**: A single target entry in the garden. Do not block to ask the user
questions. Make your proposed edits and leave them in the Git working tree for
the user to decide what to do with them.

**Output**: The target edits in place, but not committed. Plus a short report,
outputted to the conversation thread, listing the changes made and their
rationale.

##  Instructions

1.  **Read the target in full.**

    Understand what the page is about, before touching it.

2.  **Make small improvements inline.**

    Work through the page applying your edits. Keep each change small.

3.  **Report what you did.**

    List the edits you made. OPTIONALLY, group them, eg. trimmed, moved,
    dead-headed, etc.

##  Rules

-   **In-scope changes:**

    Make only small changes that are self-evidently improvements, without
    requiring clarification from the user.

    Trim waffle. Cut filler and padding. Say the same thing in fewer words.

    Smooth awkward phrasing. Fix clumsy sentences, bad transitions, tangled
    clauses.

    Drop redundancy. Remove sentences or clauses that repeat something said
    elsewhere in the page.

    Reorder content for better flow. Shuffle paragraphs, pull a stray point into
    a section where it sits more comfortably, merge two half-empty bullets, etc.

    Tighten bullets and lists. Fix over-long headings, collapse one-item lists,
    split run-on bullets, etc.

-   **Out-of-scope changes:**

    Do NOT fix broken xrefs, pseudo-links, orphaned pages, or stale maturity
    labels.

    Do NOT apply changes for style guide conformance, eg. dashes, colons,
    casing, bold text.

    Do NOT expand with new content — even if the existing content is just a
    stub.

-   **Do NOT change meaning.**

    Do not make any edits that could change the perceived meaning of the
    content.

    If tightening a sentence could alter its meaning, leave it as-is.

-   **Preserve voice.**

    Match the existing tone and phrasing conventions.

-   **Stay within the target page.**

    Do not edit anything except the target topic page.

    Do not create, delete, or merge pages here.

-   **Do NOT commit your changes.**

    Make your edits in the working tree only. Staging, committing, and pushing
    are the user's call.

##  Success criteria

-   **The page is tighter and better-ordered than before.**

    There's no waffle or local redundancy left that a quick read would catch.

-   **The meaning and voice are unchanged.**

    Only the expression and arrangement are improved.

-   **No content moved between pages.**

    And no page was created, merged, or deleted.
