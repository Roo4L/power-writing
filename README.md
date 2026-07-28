<div align="center">

# Power Writing

### A Claude skill for writing any text — that respects the reader's time.

**A proportional Brief × ten codified writing principles → prose that does one job well, and nothing more than it takes.**

</div>

---

## What it does

Power Writing is a Claude Code skill that helps write **any** prose — emails, Slack messages, Jira issues, docs, reports, landing pages, essays — by enforcing two things most AI writing skips:

1. **The Brief** — before a word is written, it establishes *why* you're writing, *for whom*, and *in what form*. This closes the **goal-gap**: the silent mismatch where the operator wanted a pitch and the agent wrote documentation, or wanted a one-line reminder and got a full spec.
2. **Codified writing principles** — ten rules, stated as gates and conditional checks (no fake numeric thresholds), that govern the words themselves.

The result: text that moves a specific reader toward a specific goal, written to *their* knowledge, in the right form, at the smallest length that does the job.

**One skill, two paths.** It asks *"generate or critique?"* — draft new text from a Brief, or run an existing draft against the same rules and hand back a tightened rewrite with each change tied to a rule.

---

## The two pillars

### Pillar 1 — The Brief
Resolve before writing (depth scaled to the task):

- **Goal** — the single job: convey · inform · sell · advertise · document. Confirm the *genre* when the goal implies one.
- **Audience** — mapped by what they **know vs. don't**, not by their label. That gap sets the detail level.
- **Form** — style *and* format (storytelling blog ↔ sharp report).
- **Constraints** — length cap, deadline, must-include, must-**avoid** / non-goals.

Governed by two dials:
- **Proportionality** — *the Brief must never cost more than writing the text yourself would.* A one-liner gets no questions; a 100-page report earns a real interview.
- **Smart defaults, escalate** — infer from context and proceed; ask only when a fork is genuinely ambiguous *and* costly to get wrong.

### Pillar 2 — The Text
Four rules for the words:

1. **Show, don't tell** — a diagram, table, or example beats paragraphs of description; in plain text, structure (lists, tables, bold) is the lightweight stand-in.
2. **Progressive disclosure** — gist first; push detail to references, follow-ups, or optional sections.
3. **Less is more** — the reader's time is the scarcest resource; cut noise, not meaning.
4. **Start lean, build up** — deliver the smallest draft that does the job; elaborate on request.

The full rulebook — with rationale, light citations (Strunk & White, Zinsser, Orwell, Tufte, Nielsen, Gopen, Pinker), and worked examples — lives in [`principles/writing-principles.md`](principles/writing-principles.md).

---

## Install

Copy this repo into your Claude Code skills directory:

```bash
git clone https://github.com/<your-username>/power-writing.git ~/.claude/skills/power-writing
```

Then invoke it by asking Claude to write, draft, rewrite, tighten, or review any piece of text — or call it directly with `/power-writing`.

---

## Files

- [`SKILL.md`](SKILL.md) — the operating procedure: Brief → Draft / Critique, with the 10-point pre-delivery checklist.
- [`principles/writing-principles.md`](principles/writing-principles.md) — the ten codified rules across both pillars. The source of truth.

---

## Why it exists

Most AI writing drifts long: more examples, more caveats, more mumble — and misses the reader entirely because it never asked who the reader is or what the text is *for*. Power Writing inverts that. It pins the goal, the audience, and the form first, then writes the leanest text that achieves them — because the most valuable thing in almost any document is the reader's time.

---

## License

MIT — see [LICENSE](LICENSE).
