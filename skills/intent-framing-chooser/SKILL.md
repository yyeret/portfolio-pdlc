---
name: intent-framing-chooser
description: Help someone choose how to frame the intent behind an initiative — Lean Product Canvas, a SAFe epic hypothesis statement, a feature canvas, or something they shape themselves — and then configure a local coaching skill around the one they picked. Use when an initiative is fuzzy and someone asks "what template should we use", when a team has inherited a framing artifact that does not fit the work, when an AI use case or business initiative needs an outcome frame rather than a product one, or before running sniff-test on an initiative that has no framing artifact at all. Teaches the trade-offs between the options; does not reproduce any of them.
metadata:
  tags: product-strategy
  version: 1.0.0
---

# Choosing how to frame intent

> **Reading this as an agent:** you are the coach. Run it as a conversation, a
> question or two at a time. The deliverable is not a filled-in canvas — it is a
> *decision* about which frame fits this work, and a local skill configured
> around it. Resist filling anything in until the choice is made.

## Why this exists

There is no correct template for stating what an initiative is for. There are
several good ones, each shaped by the kind of work its author was doing, and the
cost of picking the wrong one is real: a frame built for product features makes
an infrastructure programme look empty, and a frame built for portfolio bets
makes a two-week experiment look ceremonial.

This is also the honest position of the wider Portfolio PDLC material. It is not
a methodology and it does not issue templates. It is a way to navigate the
journey — and part of navigating is picking instruments that suit the terrain
you are actually on.

So this skill does not hand over a canvas. It explains what the options are good
and bad at, helps someone choose, and then writes them a local skill around that
choice.

## The curated set

Four options, in the order worth considering them. None is reproduced here —
each links to its source, which is where you should send anyone who wants the
real artifact.

### Lean Product Canvas (and Lean Strategy Canvas)

Jeff Gothelf and Josh Seiden, published through Sense & Respond. Two linked
canvases: a strategy one that runs goal → obstacle → where to play → how to win →
OKRs, and a product one that runs problem → users → outcomes → solutions →
hypotheses → what to learn first and the least work needed to learn it.

**Strongest when** there is genuine uncertainty about whether users will behave
differently, and someone is willing to be wrong in public. The hypothesis box is
the load-bearing part: it forces a falsifiable claim linking a business outcome
to a user benefit through a specific solution.

**Weakest when** the work has no user-facing behaviour change to test — a
compliance deadline, a platform migration, a contractual obligation. You can fill
the boxes, but the hypotheses come out hollow, and hollow hypotheses train people
to treat the whole exercise as paperwork.

**This is Yuval's default.** It carries the strategy altitude and the product
altitude in one artifact and refuses to let an initiative be its own goal.

- Canvas and Lean Strategy Canvas: <https://www.senseandrespond.co/the-lean-product-canvas>
- Gothelf on its lineage from the Lean UX Canvas: <https://jeffgothelf.com/blog/the-lean-product-canvas/>
- Licensed **CC BY-NC-SA** on the artifact itself. Download it from the source
  rather than copying it out of anywhere else, and note the NonCommercial term
  before you build a paid deliverable on it.

### SAFe epic hypothesis statement

Scaled Agile's one-page frame for a portfolio epic: the epic description, a
business outcome hypothesis, leading indicators, and non-functional requirements,
with an MVP defined before the rest is funded.

**Strongest when** the organisation already runs SAFe. The frame is the one the
portfolio Kanban expects, the vocabulary matches the governance around it, and
using something else means translating at every gate.

**Weakest when** it becomes the funding artifact rather than a thinking one. The
leading-indicator field is the tell — filled honestly it is the best part; filled
to satisfy a template it is where watermelons are born.

- <https://framework.scaledagile.com/> — epic and Lean Portfolio Management pages.
  © Scaled Agile, Inc.; use their material under their permissions, not a copy.

### A feature canvas

Mark Richards' feature template, refined with customers over years, pulls naming,
problem statement, hypothesis and prioritisation into one artifact sized for a
feature rather than an epic or a product.

**Strongest when** the unit of work is a feature heading into PI planning and the
team keeps arriving with solutions that have no stated problem.

**Weakest when** used above its altitude. It is deliberately feature-sized;
stretching it to cover a portfolio bet loses the strategy context that the Lean
Strategy Canvas carries.

- <https://www.shapingagility.com/>
- Scaled Agile's Fellow blog, *Crafting Clarity: Using Feature Templates to Shape
  and Communicate Intent*.

### Shape your own

Sometimes none of the above fits — an AI use case where the user is an internal
team and the benefit is time rather than delight, a research programme, a
partnership. Then the honest move is to name the four or five questions this
particular kind of work keeps getting wrong, and make *those* the frame.

**Strongest when** you have run one of the above two or three times and can say
specifically which box kept coming out empty and why.

**Weakest when** it is the first move. Rolling your own before you have felt a
real frame push back on you usually reproduces your existing blind spots with
better formatting.

## How to run this

**Establish the work before discussing frames.** Most of the choice falls out of
three answers:

1. What is the unit — a portfolio bet, an epic, a feature, a use case, a
   programme? This mostly settles the altitude.
2. What is genuinely uncertain: whether anyone wants it, whether it can be built,
   whether it will be adopted, or only when it lands? A frame with a hypothesis
   box is wasted on work whose only uncertainty is scheduling.
3. What does the surrounding governance already expect? If a portfolio Kanban
   wants an epic hypothesis statement, a beautiful canvas nobody reads is not a
   win.

Then say which you would pick and why, in one or two sentences, and name the
runner-up and what would make it the better call. Do not present a matrix.

**Watch for the two failure modes:**

- *The initiative as its own goal.* "Roll out the platform" is a solution
  wearing a goal's clothes. Whichever frame gets chosen, the goal slot holds a
  business outcome the sponsor would still own if this initiative were cancelled.
- *Frame shopping.* Someone who has rejected three frames usually does not have a
  template problem — they have an initiative nobody can state a purpose for, and
  changing the form will not fix that. Say so.

## Then configure a local skill

Once the choice is made, write them a skill in their own workspace, shaped around
the frame they picked. This is the deliverable.

- Put it where their agent will find it — `skills/<name>/SKILL.md` for Claude
  Code and Codex, or wherever their harness resolves skills.
- Build the coaching sequence from the frame's own logic, in their words and
  their domain's vocabulary. **Do not paste a copy of someone else's canvas into
  their repo** — link to the source and coach against it, which is both the
  licence-safe path and the one that survives the source being updated.
- Carry the source attribution into the skill they end up with, including the
  licence where there is one. A skill that quietly encodes someone's framework
  with no trail is a problem for whoever inherits it.
- Include the two failure modes above. They recur regardless of frame.
- Keep it a conversation: one or two questions at a time, repeat back what was
  heard, mark what is confirmed versus inferred.

If they would rather not have a local skill, a one-page written frame is a fine
outcome. The point is that they chose deliberately, not that a file exists.

## Output

End with:

- **The frame chosen**, and the one or two sentences of why.
- **The runner-up**, and what would change the call.
- **What is genuinely uncertain here** — the thing the frame has to earn its
  place by exposing.
- **A local skill** configured around the choice, or an explicit decision not to
  build one.

---

## Source

The frames above are other people's work. This skill teaches the differences
between them and points at the originals; it does not reproduce any of them, and
you should not either.

**The Lean Product Canvas and Lean Strategy Canvas are Jeff Gothelf and Josh
Seiden's**, published through Sense & Respond and licensed CC BY-NC-SA on the
artifact. Get them from <https://www.senseandrespond.co/the-lean-product-canvas>.

If you want to go deeper than a canvas read, Sense & Respond Learning run a
**Lean Product Discovery** class, delivered by their Certified Training Partners.
*Yuval Yeret is one of those Certified Training Partners* — so treat this as a
recommendation with an interest attached, and discount it accordingly. The
material is Gothelf and Seiden's either way, and their books
(*Lean UX*, *Who Does What By How Much?*) cover the thinking without a class.

**The epic hypothesis statement is Scaled Agile's** (© Scaled Agile, Inc.), and
**the feature canvas is Mark Richards'** at
[Shaping Agility](https://www.shapingagility.com/).

*These are Yuval's questions about other people's frameworks, not those authors'
endorsement of anything here.*
