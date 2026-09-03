<div align="center">

# Power Writing

**A Claude skill for writing any text that respects the reader's time.**

Pin the goal, the reader, and the form first — then write the leanest text that does the job.

</div>

---

## What it is

`power-writing` is a Claude Code skill for drafting and reviewing prose — emails, Slack messages, Jira issues, docs, reports, landing pages, essays. It fixes the two things AI writing usually skips: it works out *what the text is for and who reads it* before writing a word, and it holds the words to a fixed set of rules — so drafts come back sharp instead of bloated.

It runs three ways: **draft** new text from a short brief, **review** an existing draft and hand it back tightened with each change tied to the rule behind it, or **deslop** a draft — strip the AI fingerprint without touching what it says.

## How it works — two pillars

**1. The Brief** — settled before writing, scaled to the task (a one-liner asks nothing; a report earns a real interview):

| Element | What it pins down |
|---|---|
| **Goal** | the single job: convey · inform · sell · advertise · document |
| **Audience** | mapped by what they *know vs. don't* — that gap sets detail **and** vocabulary |
| **Form** | style + format (storytelling blog ↔ sharp report) |
| **Constraints** | length cap, deadline, must-include, must-avoid |

Two dials govern it: **proportionality** (the Brief never costs more than writing the text yourself would) and **confirmable defaults** (infer from context; when a question is unavoidable, offer an answer to nod at, not a blank prompt).

**2. The Text** — five rules for the words:

- **Show, don't tell** — a diagram, table, or example over paragraphs of description
- **Progressive disclosure** — gist first; detail optional or linked
- **Less is more** — the reader's time is the scarcest resource in the document
- **Start lean, build up** — ship the smallest draft that works; expand on request
- **Cut the machine texture** — sweep the finished draft for the AI fingerprint

The full rulebook — rationale, citations, and worked examples — lives in **[`principles/writing-principles.md`](principles/writing-principles.md)**.

## Desloping

Rules 9 and 10 govern how *much* you write. Rule 11 governs how it *reads* — because a draft can be short, layered, and correctly aimed at its reader and still be unmistakably machine-written. Cutting words doesn't touch the fingerprint; the fingerprint is in the words that remain.

The sweep targets antithesis flips ("it's not X, it's Y"), throat-clearing ("let's dive in"), hype frames, engagement-bait closers ("I hope this helps"), padding phrases ("it's worth noting"), a known vocabulary (*delve*, *seamless*, *unlock*, *game-changer*), decorative emoji, and metronomic sentence rhythm. Two guards keep it from becoming a find-and-replace:

| Guard | What it prevents |
|---|---|
| **Classify before cutting** | Mangling terms of art — `critical section` and `public key` contain flagged words and are the right words |
| **Clean words aren't content** | Swapping out flagged vocabulary in a paragraph that says nothing, and calling it edited |

Both outrank every list, and neither licenses inventing a specific to prop up a weak sentence — vague claims get made *honest*, not *impressive*.

One clause has a deterministic check instead of a rule, because no reader can verify it by eye:

```bash
python3 scripts/strip-invisibles.py --check draft.md
# line 12: U+200B ZERO WIDTH SPACE (deleted)
# line 12: U+00A0 NO-BREAK SPACE (-> space)
```

Zero-width joiners, bidi controls, exotic spaces, and confusable punctuation survive copy-paste and are a real fingerprint. Code fences, inline spans, and frontmatter are protected; curly quotes and em-dashes are left alone as legitimate typography.

Pattern catalogue: **[`principles/slop-patterns.md`](principles/slop-patterns.md)**, adapted from **[DeSlop](https://github.com/AUAggy/deslop)** and reorganized to lead with the guards.

## Install

```bash
git clone https://github.com/Roo4L/power-writing.git ~/.claude/skills/power-writing
```

Then ask Claude to write, draft, tighten, review, or deslop any text — or call `/power-writing` directly. The invisible-character check needs Python 3.8+ and no packages; nothing else has dependencies.

## Files

- **[`SKILL.md`](SKILL.md)** — the procedure: Brief → Draft / Critique / Deslop, plus an 11-point pre-delivery checklist.
- **[`principles/writing-principles.md`](principles/writing-principles.md)** — the eleven rules. The source of truth.
- **[`principles/slop-patterns.md`](principles/slop-patterns.md)** — the Rule 11 catalogue: guards, intervention ladder, protected regions, pattern lists. Loaded on demand.
- **[`scripts/strip-invisibles.py`](scripts/strip-invisibles.py)** — the deterministic half of Rule 11.

## License

MIT © 2026 Nikita Ivanov — see [LICENSE](LICENSE).

The Rule 11 catalogue and the invisible-character check are adapted from [DeSlop](https://github.com/AUAggy/deslop) (MIT) — see [NOTICE](NOTICE).
