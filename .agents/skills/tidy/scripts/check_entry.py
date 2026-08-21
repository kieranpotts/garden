#!/usr/bin/env python3

"""
Mechanical style checks for one garden entry.

- Out-bold xref form, *xref:foo.adoc[Text]* (should be xref:foo.adoc[*Text*]).

- A soft line-wrap landing inside an xref/link/bold/italic/code span.

- A prose line over the style guide's line-wrap ceiling (120 chars),
  when the overrun isn't explained by one unbreakable inline span.

- A bare external https?://...[...] link not using the {link-name}[...]
  attribute form.

This script is read-only. It reports findings, it never edits the file.
Fixing is the calling agent's job. This script just gives it precise line numbers
and a clear description of each finding.

Usage:
    python3 check_entry.py <path/to/entry.adoc> [more paths...]

Exit status is 0 if no findings, 1 if any findings were reported.
"""

import re
import sys
import pathlib

LINE_WRAP_CEILING = 120

FENCE_DELIMS = {"----", "....", "****", "====", "++++"}
QUOTE_DELIM = "____"

# NOTE: every fence-tracking loop below tests `stripped in FENCE_DELIMS or
# stripped == QUOTE_DELIM` in ONE condition, then toggles `in_fence` in one
# place. Splitting the quote check into a separate `if` after an
# `if in_fence is not None: continue` guard is a real bug that was hit
# during garden-wide editing. The guard fires first on every line already
# inside the block, so the closing `____` is treated as ordinary fenced
# content instead of closing it — and everything after silently stops being
# checked/rewrapped for the rest of the file.

# A constrained inline span: xref:, link:/http(s) with [label], or
# AsciiDoc bold/italic/code, matched the same way Asciidoctor treats them
# as a single unbreakable unit for word-wrap purposes.
ATOMIC = re.compile(
    r"xref:\S+?\[[^\]]*\]"
    r"|(?:https?://\S+?|link:\S+?)\[[^\]]*\]"
    r"|(?<![\w*])\*(?!\s)[^*\n]+?(?<!\s)\*(?![\w*])"
    r"|(?<![\w_])_(?!\s)[^_\n]+?(?<!\s)_(?![\w_])"
    r"|`[^`\n]+?`"
)

# The old, wrong "outer bold" xref form: *xref:target[Text]*
OUTER_BOLD_XREF = re.compile(r"\*xref:([a-z0-9-]+\.adoc(?:#\S+?)?)\[([^\]]*)\]\*")

# A bare external link not yet using the {link-name}[...] attribute form.
BARE_EXTERNAL_LINK = re.compile(r"(?<!\{)https?://[^\[\s]+\[")


def iter_blocks(lines):
    """Yield (line_no, line, in_fence) for every line, tracking whether we're
    inside a fenced/quote block (code, example, sidebar, literal, quote)."""
    in_fence = None
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped in FENCE_DELIMS or stripped == QUOTE_DELIM:
            if in_fence == stripped:
                in_fence = None
            elif in_fence is None:
                in_fence = stripped
            yield i, line, True
            continue
        yield i, line, in_fence is not None


def check_outer_bold_xref(text, lines):
    findings = []
    for m in OUTER_BOLD_XREF.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        findings.append(
            (line_no, "outer-bold-xref",
             f"`{m.group(0)}` uses the outer *xref:...[...]* form — "
             f"should be `xref:{m.group(1)}[*{m.group(2)}*]`.")
        )
    return findings


def check_split_inline_spans(lines):
    """A soft line-wrap that lands inside an xref/link/bold/italic/code span,
    found by joining runs of contiguous plain-prose lines and looking for an
    ATOMIC match whose captured text contains a newline."""
    findings = []

    def is_para_line(s):
        s = s.strip()
        if not s:
            return False
        if s.startswith(("=", "//", "[", "|", ".", "*", "-", "+", ":",
                          "image:", "include:", "ifdef:", "ifndef:", "endif:")):
            return False
        if re.match(r"^\d+\.\s", s):
            return False
        return True

    in_fence = None
    i = 0
    n = len(lines)
    while i < n:
        stripped = lines[i].strip()
        if stripped in FENCE_DELIMS or stripped == QUOTE_DELIM:
            in_fence = None if in_fence == stripped else stripped
            i += 1
            continue
        if in_fence is not None:
            i += 1
            continue
        if is_para_line(lines[i]):
            start = i
            j = i + 1
            while j < n and is_para_line(lines[j]):
                j += 1
            para = "\n".join(lines[start:j])
            multiline_atomic = re.compile(
                r"xref:\S+?\[[^\]]*\]"
                r"|(?:https?://\S+?|link:\S+?)\[[^\]]*\]"
                r"|(?<![\w*])\*(?!\s)[^*]+?(?<!\s)\*(?![\w*])"
                r"|(?<![\w_])_(?!\s)[^_]+?(?<!\s)_(?![\w_])"
                r"|`[^`]+?`",
                re.DOTALL,
            )
            for m in multiline_atomic.finditer(para):
                if "\n" in m.group(0):
                    line_no = start + para.count("\n", 0, m.start()) + 1
                    snippet = re.sub(r"\s+", " ", m.group(0)).strip()
                    findings.append(
                        (line_no, "split-inline-span",
                         f"a line wrap lands inside an inline span: {snippet!r}")
                    )
            i = j
        else:
            i += 1
    return findings


def check_line_length(lines):
    """Flag a prose line over the ceiling, unless the overrun is explained by
    one atomic span that alone would exceed the ceiling on its own line —
    that's the accepted case per the style guide's line-wrap rule."""
    findings = []
    in_fence = None
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped in FENCE_DELIMS or stripped == QUOTE_DELIM:
            in_fence = None if in_fence == stripped else stripped
            continue
        if in_fence is not None:
            continue
        if stripped.startswith(("=", "//", "|", "image:", ":")):
            continue
        if len(line) <= LINE_WRAP_CEILING:
            continue
        # Does one atomic span, plus its glued punctuation, already exceed
        # the ceiling on its own? If so this line is expected to run long.
        widest = max((len(m.group(0)) for m in ATOMIC.finditer(line)), default=0)
        if widest >= LINE_WRAP_CEILING - 20:
            continue
        findings.append(
            (i, "line-too-long",
             f"line is {len(line)} chars (ceiling {LINE_WRAP_CEILING}), "
             f"and no single inline span explains the overrun — "
             f"likely needs a rewrap, not just a wide link/bold/italic term.")
        )
    return findings


def check_bare_external_links(lines):
    findings = []
    in_fence = None
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped in FENCE_DELIMS or stripped == QUOTE_DELIM:
            in_fence = None if in_fence == stripped else stripped
            continue
        if in_fence is not None:
            continue
        if stripped.startswith("// TODO"):
            continue  # TODO comments intentionally keep bare URLs — see style guide
        for m in BARE_EXTERNAL_LINK.finditer(line):
            findings.append(
                (i, "bare-external-link",
                 f"external link not using the {{link-name}}[...] attribute "
                 f"form: {line.strip()[:100]!r}")
            )
    return findings


def check_file(path):
    text = path.read_text()
    lines = text.split("\n")
    findings = []
    findings += check_outer_bold_xref(text, lines)
    findings += check_split_inline_spans(lines)
    findings += check_line_length(lines)
    findings += check_bare_external_links(lines)
    findings.sort(key=lambda f: f[0])
    return findings


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    any_findings = False
    for arg in argv:
        path = pathlib.Path(arg)
        if not path.exists():
            print(f"{path}: no such file")
            any_findings = True
            continue
        findings = check_file(path)
        if not findings:
            print(f"{path}: OK")
            continue
        any_findings = True
        print(f"{path}: {len(findings)} finding(s)")
        for line_no, category, message in findings:
            print(f"  {path}:{line_no}  [{category}]  {message}")
    return 1 if any_findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
