# Slop Patterns — the Rule 11 reference

*The pattern catalogue behind Rule 11 ("cut the machine texture") in [`writing-principles.md`](writing-principles.md).*

> **Load this on demand, not by default.** Rule 11 in the principles file is the rule; this is the lookup table. Read it when you are sweeping a draft for machine texture or running the Critique path — not before drafting a two-line Slack reply. (That's Rule 8 applied to the skill's own docs.)
>
> Adapted from [DeSlop](https://github.com/AUAggy/deslop) (`src/prompts/system.ts`), reorganized to lead with the guards, and calibrated where noted.

---

## The one thing to get right

**These lists are dangerous on their own.** A blocklist applied without judgment produces a *different* kind of bad writing: prose with the flagged words swapped out and nothing gained, or worse, mangled terms of art. `critical section`, `public key`, `robust estimator`, and `seminal paper` all contain flagged words and all are the correct words.

So the guards come first, and they outrank every list below.

### Guard 1 — False positives: classify before you cut

A flagged word is not automatically wrong. Sort it first:

| The instance is… | Move |
|---|---|
| **Filler** — carries no information | delete or replace |
| **Term of art** — precise in this domain | keep |
| **Code / API / product / legal wording** | preserve exactly |
| **Quoted or externally supplied** | preserve exactly |
| **Voice** — deliberate, fits the piece | keep |
| **Evidence-backed** — the source supports it | keep, or tighten |

**Only filler is removed automatically.** Everything else needs a reason.

### Guard 2 — False negatives: clean words are not content

A paragraph can pass every list on this page and still be slop, because the failure is abstraction, not vocabulary. Each paragraph must earn its place with **at least one** of:

a concrete noun · a specific example · a mechanism · a number from the source · a named system, object, or person · a tradeoff · a constraint · an observable consequence · a claim that advances the argument

If a paragraph has none of these, it is decoration. Compress it, make it direct, or delete it.

This is the guard that matters most for agent-written text: word-level cleanup is easy and shallow, and a draft that passes it can still say nothing.

---

## The intervention ladder

Rule 5 (proportionality) governs how much you *interview*. This governs how much you *edit*. Score the draft, then use **the lowest intervention that solves the problem**.

| Score | Reading | Intervention |
|---|---|---|
| **0** | Already clean | Leave it. Edit only if a small change clearly helps. |
| **1** | Mostly clean | Light copyedit. |
| **2** | Some generic phrasing | Tighten; remove filler. |
| **3** | Obvious machine texture | Rewrite the affected paragraphs. |
| **4** | Heavy slop | Restructure sentences and paragraphs. |
| **5** | Generic draft, little substance | Preserve the claims, but make the emptiness visible rather than papering over it. |

**Do not flatten strong human prose because its rhythm is unusual.** An idiosyncratic voice is not slop. Over-editing a score-1 draft into house style is its own failure, and it is the more common one once you have a list in hand.

---

## Protected regions — never rewrite

Reproduce character-for-character. Do not normalize quotes, punctuation, capitalization, or spelling inside these:

- Triple-backtick code fences (opening fence to closing fence, language tag included) and inline backtick spans
- YAML/TOML frontmatter at the start of a document
- URLs, file paths, shell commands
- API, function, class, package, and environment-variable names; flags; version numbers
- Quoted material that is a citation, legal text, testimonial, command output, or anyone else's wording

If the whole text is code, config, logs, a stack trace, or serialized data, there is nothing to deslop. Return it unchanged.

---

## Hard fails

Outside protected regions, these are slop on sight.

**Antithesis flips.** State the actual claim instead.

> "It's not X. It's Y." · "It's not just X; it's Y." · "It's not about X, it's about Y." · "Not X, but Y." · "Not merely X, but Y." · "More than just X." · "Less about X and more about Y." · "Forget X. Think Y." · "The goal/point isn't X. It's Y." · "Where X meets Y." · "X meets Y" as a tagline.

**Throat-clearing.** Cut and start with the content.

> "Let's dive in" · "Let's get started" · "Without further ado" · "In this article, we will…" · "This post will explore…" · "Before we begin…"

**Hype frames.**

> "In a world where…" · "Imagine a world…" · "Picture this:" · "Say goodbye to X and hello to Y" · "The future of X is here" · "Look no further" · "Buckle up" · "Stay tuned"

**Engagement bait.**

> "What do you think?" · "Let me know in the comments" · "Have you tried X?" · "Share your experience" · "I hope this helps" · "Feel free to reach out" · "Don't hesitate to…"

**Vocabulary tells.** Words that appear in machine prose at rates they never reach in human prose:

> delve · tapestry · rich tapestry · realm · journey · embark · unlock · unleash · harness · seamless(ly) · game-changer · game-changing · revolutionary · transformative · cutting-edge · state-of-the-art · ever-evolving · ever-changing · "in today's fast-paced world" · "in today's digital age" · "digital landscape"

Two conditional members of that list: **"robust solution"** is a hard fail unless *robust* is being used as a precise technical term, and **"comprehensive guide"** is a hard fail unless the document is genuinely comprehensive.

---

## Contextual flags

These often signal slop and often don't. Replace only the filler instances (Guard 1).

| Flagged | Filler use | Legitimate use |
|---|---|---|
| robust | "a robust solution" | robust estimator, robust to malformed input |
| critical, essential, key | "critical to success" | critical section, critical infrastructure, public key, key exchange |
| significant | "a significant improvement" | statistically significant |
| scalable, dynamic, agile | "scalable, dynamic solutions" | scalable architecture, dynamic linking, Agile methodology |
| ecosystem, landscape | "the developer ecosystem" | package ecosystem, landscape mode |
| implement, optimize, streamline, enhance, facilitate, leverage | verbs standing in for a specific action | implementation detail, optimization pass, leverage ratio |
| best, leading, world-class, enterprise-grade | unsourced superlatives | a benchmarked, cited claim |
| seminal, pivotal, granular | "a pivotal moment" | seminal paper, granular locking |

Keep them whenever they are precise technical, legal, academic, product, or domain terms. When in doubt, ask what the word is *doing*: if removing it loses nothing, it was filler.

---

## Padding phrases

Delete unless quoted. None of these carry information; each delays the sentence that does.

> it's worth noting · it's worth mentioning · importantly · it is important to note · it should be noted that · keep in mind · bear in mind · as a matter of fact · in fact · actually · basically · essentially · simply put · in other words · to put it simply · that is to say · for all intents and purposes · at the end of the day · all things considered · when it comes to · in terms of · with that said · having said that · that being said · be that as it may · with all that being said · needless to say · as we all know · as you may know · it goes without saying · here's the thing · the truth is · the bottom line is · at its core · pro tip · fun fact · did you know that

This is Rule 9 (less is more) at the phrase level, with names.

---

## Hedging — thin it, don't strip it

Accuracy matters more than confidence. Hedges that protect the truth stay.

- **Cut stacked or evasive hedges:** "could potentially", "might possibly", "may perhaps", "it seems likely that perhaps" — any chain of two or more weak qualifiers. One qualifier, or none.
- **Keep single load-bearing hedges:** *may* for uncertain behavior · *can* for capability · *usually* for non-universal behavior · *reported* for sourced claims · *experimental* for unstable features.

---

## Specificity — never invent the specifics

Vague claims should become *honest*, not *impressive*. The failure mode is fixing vagueness by fabricating precision.

| | |
|---|---|
| **Vague** | "The tool improves performance." |
| **Wrong fix** | "The tool cuts latency by 40%." — invented |
| **Right fix** | "The tool aims to improve performance." — or name the mechanism the source actually gives |

Never invent numbers, dates, mechanisms, examples, benchmarks, names, guarantees, or causal claims to make prose land harder. Replace a vague claim with a specific one **only when the source supplies the specifics.** If it doesn't, the honest sentence is the correct output.

---

## Texture

### Punctuation

**Calibrated deviation from DeSlop.** DeSlop bans the em-dash as a clause connector in technical, business, docs, README, changelog, and website copy — while its own deterministic checker exempts em-dashes and curly quotes as "legitimate typography." That contradiction is worth resolving honestly rather than copying:

**The tell is uniform reliance, not the mark.** An em-dash doing real work — setting off a genuine aside — is fine. Three of them per paragraph, used as the default connector for every clause, is the fingerprint. Sweep for *density and monotony*: where the em-dash is standing in for a colon, semicolon, comma, parentheses, or a full stop, use the right one.

Do not introduce smart quotes. Keep the input's quote style unless it is mixed, and leave quote style alone inside protected regions.

### Emoji

Remove emoji used as heading markers, bullet markers, or hype signals, unless the context is explicitly social or playful. Keep any emoji that carries required meaning.

Common decorative slop: 🚀 ✨ 🔥 ⚡ ✅ 🙌 💎 👉 🧠 ⭐ 🎉 🌍 🌐 📈 📣 🔒 🪄 🧵 🚫 💡

No exclamation points in technical, professional, docs, README, or changelog prose.

### Invisible characters

Zero-width joiners, bidi controls, non-breaking and exotic spaces, and confusable punctuation (U+2010 hyphen, U+2032 prime, U+FF07 fullwidth apostrophe) survive copy-paste and are a genuine fingerprint. **You cannot see them by reading.** Don't try — run the check:

```bash
python3 scripts/strip-invisibles.py --check < text.md   # report
python3 scripts/strip-invisibles.py < text.md > out.md  # fix
```

Proportional, like everything else: run it on text going into a file, repo, page, or published doc. Skip it for a chat reply.

---

## Shape

### Style

Active voice. Imperative mood for instructions. "to" over "in order to"; "because" over "due to the fact that". Concrete nouns and specific verbs. Present tense for stable behavior, future for planned, past for history. Define a technical term on first use when the source gives you enough to define it. Avoid first person unless the source uses it deliberately, and second person outside direct instructions. Don't add jokes, hype, warmth, or personality the source didn't imply — and don't turn clear prose into terse slogans.

### Structure

Don't add what the source didn't ask for: no heading above every paragraph, no table for two columns of filler, no TL;DR or "Key Takeaways" unless the source already has one. Drop a "Conclusion" heading from a short piece when the last paragraph only restates what came before. Don't close on a summary, a rhetorical question, or an engagement request. A call to action is allowed when it is specific and useful.

### Bullets

Keep bullets that help scanning; convert them to prose when they are decorative or repetitive. The pattern to kill:

> - **Speed:** Fast.
> - **Reliability:** Reliable.
> - **Security:** Secure.

Each item needs real information. When several bullets open the same way, vary the structure or combine them.

### Rhythm

Machine prose has a metronome. Watch for three similar-length sentences in a row; "This does X. It also does Y. It also does Z."; a long sentence repeatedly capped with a short punchline; the same colon-setup-then-declarative beat over and over.

Vary length and shape where it improves readability — not to be theatrical. Vary-for-variety's-sake is just a different metronome.

### Paragraphs

One point per paragraph. Short paragraphs for docs and web copy; longer ones are fine in articles and essays when a single coherent thought needs the room. Split any paragraph that combines unrelated claims, repeats itself, or has stopped being scannable.

---

## The sweep

Run in this order. Earlier steps outrank later ones.

1. **Score it** (0–5) and pick the intervention level. A 0 or 1 gets left alone.
2. **Mark protected regions.** Everything below skips them.
3. **Guard 2 first** — does every paragraph carry something concrete? Empty paragraphs get compressed or cut *before* you polish their wording. Polishing text that is about to be deleted is wasted work.
4. **Hard fails** — antithesis flips, throat-clearing, hype frames, engagement bait, vocabulary tells.
5. **Padding phrases** — delete.
6. **Contextual flags** — apply Guard 1 to each; filler only.
7. **Hedges** — unstack; keep the load-bearing ones.
8. **Specificity** — every vague claim made honest, none made up.
9. **Texture and shape** — punctuation, emoji, structure, bullets, rhythm, paragraphs.
10. **Invisible characters** — run the script when the text warrants it.

Then verify: protected regions untouched, meaning preserved, nothing invented, no hard fails left, no filler-only flags left, no decorative emoji, no engagement-bait closer added, no headings/tables/bullets added that the source didn't need.

---

## What Rule 11 does not do

- **It does not license inventing content.** Guard 2 says an empty paragraph should be cut or made honest, never filled with plausible detail.
- **It does not override the Brief.** If Rule 3 picked a warm storytelling register, warmth is not slop.
- **It does not outrank meaning.** Every list here loses to "the sentence must still be true and still say the thing."
- **It is not a style homogenizer.** The target is machine texture, not deviation from a house voice.
