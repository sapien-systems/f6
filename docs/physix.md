# Physix

*A compact symbolic system for classifying any word, object or concept in several layers at once.*

The original Swedish specification is kept unchanged in [`physix.sv.md`](physix.sv.md). This page is an English summary, plus one change (marked **v0.2**).

## Layers

| Layer | Question | Values |
|-------|----------|--------|
| **Shape** | What category of thing is it? | ○ possibility/dream/self-model · △ information/claim/knowledge · □ spacetime/natural resource (always implied) · ⬠ human-made/constructed · ⬡ concentrated dangerous force · ⬢ orbit/free fall |
| **Perception** | Good or bad? | 🔴 bad · 🔵 good · — neutral (colour only when clearly positive or negative) |
| **Truth** | Affirmed or negated? | ⚫ true/yes · ⚪ false/no |
| **Chaos** | How is it structured? | **v0.2:** see below |

Operators: **⊂** nests one form in another, **→** marks change over time, **+** joins tags.

## v0.2: Chaos becomes a position

In v0.1, Chaos held three values: Α (ordered), Δ (chaotic), Λ (solo). That mixed *how orderly something is* with *how many are involved*, so a solo, chaotic thing had no valid tag.

In v0.2 the Chaos layer is replaced by a position in the [Svensk Army Knife](svensk-army-knife.md): three coordinates `(λ, δ, α)` summing to 1, plus an orthogonal **mass**. The old letters survive as a shorthand: write the nearest pole (`Λ`, `Δ` or `Α`) when a full position is not needed.

Examples (v0.1 shorthand kept; full positions live in the [lexicon](../lexicon/lexicon.json)):

```
sun       = ⬡ ⊂ □   — ⚫ Α
reactor   = ⬡ ⊂ ⬠   — ⚫ Α
satellite = ⬢ ⊂ ⬠   — ⚫ Α
human     = □ → ⬠   — ⚫ Α
dream     = ○       — ⚫ Λ
no        = △ 🔴 ⚪ Δ
yes       = △ 🔵 ⚫ Α
```

Physix is structure, not metaphor.

## Open questions

- What does Truth mean for a plain noun such as "sun"? (The convention appears to be "exists/affirmed".)
- ⬡ is defined as "dangerous", which overlaps with Perception.
- The nesting rule says constructed things nest in ⬠, but `human` uses → instead of ⊂.
- Abstract concepts (justice, love, time) have no guidance yet.
