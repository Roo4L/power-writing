#!/usr/bin/env python3
"""Strip invisible characters and confusable punctuation from prose.

Rule 11 (cut the machine texture) has one clause a reader cannot verify by
eye: zero-width joiners, bidi controls, exotic spaces, and confusable
punctuation are invisible or near-invisible, survive copy-paste, and are a
genuine machine fingerprint. This is the deterministic check behind that
clause -- the rest of Rule 11 is judgment, this part is not.

Code fences, inline backtick spans, and leading YAML/TOML frontmatter are
protected: a zero-width character inside a code sample may be the point.

    python3 scripts/strip-invisibles.py --check < text.md   # report, exit 1 if found
    python3 scripts/strip-invisibles.py < text.md > out.md  # fix
    python3 scripts/strip-invisibles.py --in-place text.md  # fix in place

Character classes ported from DeSlop's src/util/postCheck.ts
(https://github.com/AUAggy/deslop). Curly quotes and em/en dashes are
deliberately left alone -- they are legitimate typography, and em-dash
*overuse* is a judgment call for the prose sweep, not a byte-level one.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata

# Zero-width characters, joiners, bidi controls, soft hyphen: deleted outright.
DELETE = frozenset(
    [
        0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF,  # zero-width + joiners
        0x202A, 0x202B, 0x202C, 0x202D, 0x202E,  # bidi embedding/override
        0x2066, 0x2067, 0x2068, 0x2069,          # bidi isolates
        0x00AD,                                  # soft hyphen
    ]
)

# Exotic spaces: replaced with a plain space, never deleted -- deleting fuses words.
SPACES = frozenset(
    [
        0x00A0, 0x1680,
        0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007,
        0x2008, 0x2009, 0x200A,
        0x202F, 0x205F, 0x3000,
    ]
)

# Line and paragraph separators: replaced with a newline.
NEWLINES = frozenset([0x2028, 0x2029])

# Confusable punctuation -> ASCII. Closed list on purpose.
CONFUSABLES = {
    0x02BC: "'", 0x02B9: "'", 0x2032: "'", 0x055A: "'", 0xFF07: "'",
    0x2033: '"', 0xFF02: '"',
    0x2010: "-", 0x2011: "-", 0x2043: "-", 0x2212: "-", 0xFF0D: "-",
}

FRONTMATTER_RE = re.compile(r"\A(---|\+\+\+)\r?\n.*?\r?\n\1(?:\r?\n|\Z)", re.DOTALL)
FENCE_LINE_RE = re.compile(r"^```.*(?:\r?\n|$)", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\r\n]+`")


def is_tag_character(cp: int) -> bool:
    """Unicode tag characters (U+E0001, U+E0020-U+E007F) -- an invisible channel."""
    return 0xE0001 <= cp <= 0xE007F


def _fence_ranges(text: str) -> list[tuple[int, int]]:
    """Ranges covering each ``` fence pair, opening fence line to closing fence line."""
    ranges = []
    pos = 0
    while True:
        opening = FENCE_LINE_RE.search(text, pos)
        if opening is None:
            break
        closing = FENCE_LINE_RE.search(text, opening.end())
        end = closing.end() if closing else len(text)
        ranges.append((opening.start(), end))
        pos = end
    return ranges


def protected_ranges(text: str) -> list[tuple[int, int]]:
    """Half-open ranges that must be reproduced byte-for-byte."""
    ranges: list[tuple[int, int]] = []

    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter:
        ranges.append((0, frontmatter.end()))

    ranges.extend(_fence_ranges(text))

    # Search for inline code with the ranges above blanked out, so a backtick
    # inside a fence cannot open a spurious inline span.
    masked = list(text)
    for start, end in ranges:
        for i in range(start, end):
            masked[i] = " "
    for match in INLINE_CODE_RE.finditer("".join(masked)):
        ranges.append((match.start(), match.end()))

    return sorted(ranges)


def _in_protected(index: int, ranges: list[tuple[int, int]], cursor: int) -> tuple[bool, int]:
    while cursor < len(ranges) and index >= ranges[cursor][1]:
        cursor += 1
    inside = cursor < len(ranges) and ranges[cursor][0] <= index < ranges[cursor][1]
    return inside, cursor


def scan(text: str) -> tuple[str, list[tuple[int, int, str]]]:
    """Return the cleaned text and a list of (line, codepoint, action) findings."""
    ranges = protected_ranges(text)
    out: list[str] = []
    findings: list[tuple[int, int, str]] = []
    index = 0
    cursor = 0
    line = 1

    for ch in text:
        inside, cursor = _in_protected(index, ranges, cursor)
        index += len(ch)

        if inside:
            out.append(ch)
            if ch == "\n":
                line += 1
            continue

        cp = ord(ch)
        if cp in DELETE or is_tag_character(cp):
            findings.append((line, cp, "deleted"))
        elif cp in SPACES:
            findings.append((line, cp, "-> space"))
            out.append(" ")
        elif cp in NEWLINES:
            findings.append((line, cp, "-> newline"))
            out.append("\n")
            line += 1
        elif cp in CONFUSABLES:
            findings.append((line, cp, "-> %s" % CONFUSABLES[cp]))
            out.append(CONFUSABLES[cp])
        else:
            out.append(ch)
            if ch == "\n":
                line += 1

    return "".join(out), findings


def describe(cp: int) -> str:
    try:
        return unicodedata.name(chr(cp))
    except ValueError:
        return "UNNAMED"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Strip invisible characters and confusable punctuation from prose."
    )
    parser.add_argument("file", nargs="?", help="input file (default: stdin)")
    parser.add_argument(
        "--check",
        action="store_true",
        help="report findings without writing output; exit 1 if any are found",
    )
    parser.add_argument(
        "--in-place", action="store_true", help="rewrite the input file in place"
    )
    args = parser.parse_args()

    if args.in_place and not args.file:
        parser.error("--in-place needs a file argument")

    if args.file:
        with open(args.file, encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()

    cleaned, findings = scan(text)

    if args.check:
        if not findings:
            print("clean: no invisible or confusable characters outside protected regions")
            return 0
        print("%d finding(s):" % len(findings), file=sys.stderr)
        for line, cp, action in findings:
            print(
                "  line %d: U+%04X %s (%s)" % (line, cp, describe(cp), action),
                file=sys.stderr,
            )
        return 1

    if args.in_place:
        with open(args.file, "w", encoding="utf-8") as handle:
            handle.write(cleaned)
        print("%d character(s) fixed in %s" % (len(findings), args.file), file=sys.stderr)
        return 0

    sys.stdout.write(cleaned)
    return 0


if __name__ == "__main__":
    sys.exit(main())
