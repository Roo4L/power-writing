# Writing Principles for Codified Text Generation
*The rulebook behind the power-writing skill.*

> Scope: one universal ruleset for **any** prose — an email, a Slack message, a Jira issue, a report, a landing page, a book. Every rule is either a **gate** ("don't write until X") or a **conditional check** ("if X then Y"). The rules deliberately carry **no invented numeric thresholds** — writing quality is context-dependent, and a fake number ("sentences ≤ 25 words") is worse than an honest judgment. Where a well-known authority obviously backs a rule, it's cited in brackets; the rest are stated as plain discipline.

The ruleset has two pillars, applied in order:

- **Pillar 1 — The Brief.** Establish *why*, *for whom*, and *in what form* before writing a word.
- **Pillar 2 — The Text.** Four rules that govern the words themselves.

Text is never written for its own sake. It exists to move a specific reader toward a specific goal. Both pillars serve that one fact.

---

## TL;DR — The rules that matter

**The Brief (resolve before writing):**

1. **Define the goal — the single job.** Every text does one primary thing: convey a thought, inform, sell, advertise, or document. Name it before writing. Beware the **goal-gap** — the operator and the agent silently assuming different jobs. [classical rhetoric: purpose]
2. **Map the audience by what they know, not by their name.** The label ("the infra team") is not the point; what they *already know vs. don't* is. That gap sets the detail level — explain the gaps, omit shared knowledge. [Gopen & Swan; Pinker — the curse of knowledge]
3. **Choose the form — style *and* format.** The same content is a storytelling blog post *or* a sharp monthly report. Pick one on purpose; they are not interchangeable.
4. **Capture the constraints.** Hard limits: length cap, deadline, must-include, and — most overlooked — must-**avoid** / non-goals.
5. **Scale the Brief to the task (proportionality).** The interview must never cost the operator more than writing the text themselves would. A Jira issue gets one question or none; a 100-page report earns a real interview. Ask: *"how long would this take the operator alone?"* — the Brief must stay well under that.
6. **Smart defaults, escalate.** Infer goal/audience/form/constraints from context and proceed. Ask **only** when a choice is genuinely ambiguous *and* getting it wrong is costly (high stakes or long text). Don't run a wizard for a two-line message.

**The Text (apply while writing; verify before delivering):**

7. **Show, don't tell.** When the medium allows it, a diagram, table, or example replaces paragraphs of description. In plain-text media (email, Slack, Jira), structure — a list, a table, bolding — is the lightweight stand-in. Before a long paragraph, ask: *can this be shown instead?* [Tufte — show the data]
8. **Progressive disclosure.** Deliver the gist first; push detail into references, follow-ups, or optional sections a reader can dive into *if they need to*. Don't cram every detail inline. [Nielsen — progressive disclosure; journalism — the inverted pyramid]
9. **Less is more.** The reader's time is the scarcest resource in the document. Cut noise, redundant examples, and throat-clearing. Sharper beats longer. This is not an entertainment book. [Strunk & White — "omit needless words"; Zinsser; Orwell]
10. **Start lean, build up.** The first draft carries only what matters — not every thought the author had. It is far cheaper to elaborate a thin draft than to review and cut a bloated one; dumping everything explodes the reviewer's time. Draft small, add on request.

---

# Pillar 1 — The Brief

Before quality text, a short interview. Its depth scales to the task (Rule 5); its job is to close the gap between what the operator wants and what the agent is about to produce.

### Rule 1 — Define the goal (the single job)
**The rule:** Name the one thing this text must achieve before writing it. Common jobs: **convey** a thought · **inform** / share · **sell** · **advertise** · **document**.

**Why it matters — the goal-gap.** This sounds obvious and is the most common failure anyway, because operator and agent quietly assume *different* jobs:
- **Landing page** — the agent writes it like **documentation** (exhaustive, neutral, feature-listing); the operator wanted a **pitch** (persuasive, benefit-led, one CTA).
- **Jira issue** — the operator wanted a **brief reminder** so the assignee knows what's required; the agent writes a **full specification** of every implementation detail, burying the ask and wasting everyone's time.

**The check:** State the goal in one sentence. If the goal implies a genre (pitch vs. docs, reminder vs. spec), confirm the genre — that's where the gap hides.

### Rule 2 — Map the audience by knowledge
**The rule:** Identify the reader *and* — the part that actually drives the writing — what they already know versus what they don't. Detail level is a function of that gap, not of the topic.

**Why it matters:** Explaining the same concept to a teammate and to the infra team requires different language and different detail.
- **Teammate** on your service: skip the internals — you both know them by heart. Extra explanation is noise.
- **Infra**, hearing about your service for the first time: they may genuinely need where it lives, how it's hosted, its address, its stack — omitting it blocks them.

**The check:** For the chosen audience, list what to **omit** (shared knowledge → noise) and what to **explain** (their gaps → required). Write to that list. This is the antidote to the curse of knowledge — you know too much to see what they're missing.

### Rule 3 — Choose the form (style + format)
**The rule:** Decide the style *and* the format deliberately. The same story delivered two ways:
- **Storytelling blog post**, general audience → narrative, warmth, some entertainment along the way.
- **Monthly report** for management → precise, sharp, grounded in facts, results-first; core over color.

**The check:** Name the style (narrative ↔ sharp) and the format (post / report / issue / deck / page / message). If the operator hasn't said, infer from the goal and audience — and don't blend an entertaining register into a report that needs to be scannable.

### Rule 4 — Capture the constraints
**The rule:** Pin the hard limits before drafting: **length cap**, **deadline**, **must-include** (facts, links, sections that are non-negotiable), and **must-avoid / non-goals** (topics, claims, or detail to leave out).

**Why it matters:** Non-goals are the cheapest way to prevent over-writing and scope creep — they tell the agent what *not* to say, which is where drift happens. An explicit length cap turns Rules 9 and 10 into something enforceable.

### Rule 5 — Proportionality (the governing rule)
**The rule:** The Brief must never cost more than the task it precedes. Calibrate by asking: *"how long would the operator spend doing this themselves?"* — and keep the interview well under that.

- Two-line Slack message → zero or one question.
- A page or a routine issue → a quick check of goal + audience.
- A large report, a book, a public-facing page → a real, elaborate interview is justified.

A 30-minute interview for a 5-minute Jira issue is a bug. A 30-minute interview before a 100-page report is a bargain.

### Rule 6 — Smart defaults, escalate
**The rule:** Infer the Brief from available context and proceed on sensible defaults. Ask a question **only** when a fork is genuinely ambiguous **and** getting it wrong is expensive (high stakes or long text). Smart defaults beat wizards.

**The check:** Before asking anything, try to answer it yourself from context. If a confident default exists, use it and move. Reserve questions for the choices that would actually change the output *and* are worth the operator's attention under Rule 5.

---

# Pillar 2 — The Text

Four rules for the words themselves. They share one enemy: text that costs the reader more time and attention than it should.

### Rule 7 — Show, don't tell
**The rule:** Prefer showing over describing. A diagram, table, example, or screenshot often conveys — faster and more simply — what a two-page walkthrough labors to explain.

**Conditional on medium:**
- **Rich media** (docs, reports, pages, decks): when a paragraph describes a structure, comparison, sequence, or set of numbers, ask whether a **visual** (diagram / table / chart) does it better. Usually it does.
- **Plain-text media** (email, Slack, Jira): you can't draw, so use **structure** as the lightweight visual — a bulleted list, a small table, a bolded key line, a short code block.

**The check:** Before committing a long descriptive paragraph, ask *"can I show this instead of telling it?"* If yes, and the medium allows, show it. [Tufte]

### Rule 8 — Progressive disclosure
**The rule:** Lead with the gist; layer detail so the reader takes only as much as they need. Forward to a reference, a follow-up doc, or a collapsible/optional section instead of inlining every detail.

**Nuance:** Not universal — some documents are justified in gathering everything in one place or reiterating. But the default failure, especially for agents, is cramming *all* the details into the same text instead of delivering the main idea first and offering the rest optionally.

**The check:** Does the reader get the core message before any deep detail? Could a block of detail live in a linked reference or a later section without hurting the gist? If yes, move it. [Nielsen; inverted pyramid]

### Rule 9 — Less is more
**The rule:** Treat the reader's time as the document's scarcest resource. Cut redundant examples, hedging, throat-clearing, and restatement. Sharper and shorter wins — we are (almost always) writing emails, messages, issues, and reports, not entertainment.

**Why it's aimed at agents specifically:** AI drifts toward *longer* — more examples, more caveats, more mumble — which becomes noise and drowns the key point.

**The check:** For each sentence and example, ask *"does removing this lose meaning?"* If no, cut it. Elaborate later on the parts that feel thin — that's cheaper than trimming bloat. [Strunk & White; Zinsser; Orwell — "if it is possible to cut a word out, always cut it out"]

### Rule 10 — Start lean, build up
**The rule:** The first draft is minimal — only what matters for *this* document, for *this* goal and audience. Don't write down every thought; add depth on request.

**Why it matters:** When a human receives an over-stuffed first draft, review time explodes — they must read everything and then negotiate cuts, the slowest possible path. A lean draft is faster to extend where it's genuinely missing something than a bloated one is to prune.

**Distinction from Rule 9:** Rule 9 governs the *final text's* length; Rule 10 governs the *drafting strategy* that gets there. Start under-built on purpose.

**The check:** Before delivering a first draft, ask *"have I included things because they matter, or because I thought of them?"* Cut the latter. Deliver the smallest draft that achieves the goal, and invite the operator to point at what to expand.

---

## What not to do

- **Write before the Brief is resolved** (explicitly or by confident default) — Rules 1–4.
- **Interview harder than the task deserves** — a wizard for a one-liner. Rule 5.
- **Ask what you could infer** — questions that don't change the output, or whose answer is obvious from context. Rule 6.
- **Confuse the genre** — docs written as a pitch, a reminder written as a spec. Rule 1.
- **Write to the topic instead of to the reader** — dumping internals on someone who needs them, or re-explaining what the reader knows cold. Rule 2.
- **Describe what you could show** — a paragraph where a table or diagram is clearer. Rule 7.
- **Inline everything** — burying the gist under detail that belonged in a reference. Rule 8.
- **Pad** — extra examples and caveats that add length, not meaning. Rule 9.
- **Dump the first draft** — every thought on the page, handing the operator a cutting job instead of a reading one. Rule 10.

When in doubt, re-read this file. It is the source of truth for the skill.
