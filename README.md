<div align="center">

# Power Writing

**A Claude skill for writing any text that respects the reader's time.**

Pin the goal, the reader, and the form first — then write the leanest text that does the job.

</div>

---

## What it is

`power-writing` is a Claude Code skill for drafting and reviewing prose — emails, Slack messages, Jira issues, docs, reports, landing pages, essays. It fixes the two things AI writing usually skips: it works out *what the text is for and who reads it* before writing a word, and it holds the words to a fixed set of rules — so drafts come back sharp instead of bloated.

It runs two ways: **draft** new text from a short brief, or **review** an existing draft and hand it back tightened, with each change tied to the rule behind it.

## How it works — two pillars

**1. The Brief** — settled before writing, scaled to the task (a one-liner asks nothing; a report earns a real interview):

| Element | What it pins down |
|---|---|
| **Goal** | the single job: convey · inform · sell · advertise · document |
| **Audience** | mapped by what they *know vs. don't* — that gap sets detail **and** vocabulary |
| **Form** | style + format (storytelling blog ↔ sharp report) |
| **Constraints** | length cap, deadline, must-include, must-avoid |

Two dials govern it: **proportionality** (the Brief never costs more than writing the text yourself would) and **confirmable defaults** (infer from context; when a question is unavoidable, offer an answer to nod at, not a blank prompt).

**2. The Text** — four rules for the words:

- **Show, don't tell** — a diagram, table, or example over paragraphs of description
- **Progressive disclosure** — gist first; detail optional or linked
- **Less is more** — the reader's time is the scarcest resource in the document
- **Start lean, build up** — ship the smallest draft that works; expand on request

The full rulebook — rationale, citations, and worked examples — lives in **[`principles/writing-principles.md`](principles/writing-principles.md)**.

## Install

```bash
git clone https://github.com/Roo4L/power-writing.git ~/.claude/skills/power-writing
```

Then ask Claude to write, draft, tighten, or review any text — or call `/power-writing` directly.

## Files

- **[`SKILL.md`](SKILL.md)** — the procedure: Brief → Draft / Critique, plus a 10-point pre-delivery checklist.
- **[`principles/writing-principles.md`](principles/writing-principles.md)** — the ten rules. The source of truth.

## License

MIT © 2026 Nikita Ivanov — see [LICENSE](LICENSE).
