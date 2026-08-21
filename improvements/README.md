# Improvements — how this repo changes how it works

This repo tells agents that changes to an operating model are **captured as bets with kill
criteria, never edited in passing**. This lane is where it does that to itself.

It exists because a review found we weren't: the first quality-bar PR added a process rule
to `AGENTS.md` as a direct edit, and the reviewer flagged it — the convention said "ride the
improvement lane", and there was no lane to ride. Cobbler's children.

## What belongs here

Changes to **how this repo operates**: conventions in `AGENTS.md`, the quality bar, the
review loop, repo layout, what agents are allowed to decide.

What does *not*: ordinary content work on the frameworks themselves — a new reference, a
sharper skill, a fixed script. Those are just pull requests. The test is whether the change
alters *how the next change gets made*.

## The card

One folder per bet, `improvements/<slug>/improvement.md`, using the same schema as
`skills/flow-driven/templates/improvement.md` — this repo should be legible to the
framework it ships. `type` here is `improvement-process`, `improvement-convention`, or
`improvement-tooling`.

Every card carries, at birth:

- a **benefit hypothesis with a mechanism** — *if we change X, measure Y moves, because Z*;
  the mechanism is what makes it falsifiable rather than hopeful,
- the **measures** it claims to move, and a **baseline** taken before anything changed,
- **kill criteria** — what we would see that means we revert. A change we cannot falsify is
  a mandate, not a bet; say which it is and who mandated it,
- the **cheapest probe** that would move our confidence.

## The lane, as an agent runs it

1. **Capture.** Noticed that a convention no longer fits, or that something needs changing
   in how we work? File a card. Do not edit the convention in passing — that is the whole
   point of the lane.
2. **Probe.** Run the cheapest thing that tests the hypothesis: one PR under the proposed
   rule, a replay of recent history, a shadow run. Record what happened on the card.
3. **Propose adoption.** A dated entry in the card's Decision log, naming a human. Adoption
   is a human decision here, the same as it is everywhere else in this repo.
4. **Watch.** After adoption, watch the measures for a stated number of changes and record
   them. A change nobody watched cannot be reverted with confidence, and a card that reaches
   `adopted` with an empty Watch table is itself a finding.

Stages: `proposed` → `probing` → `adopted` → `watching` → `kept` | `reverted`. A bet may also
be `rejected` — that is a result, not a failure, and the card stays as the record of why.

## Rules

- **The folder is the list.** No generated index to drift out of date.
- **Adoption edits the real file** — `AGENTS.md`, the quality bar, whatever the bet named —
  and the card records the date and the decision.
- **Kill criteria are written before the probe**, not after the result is known.
- **Respect improvement WIP.** More open bets than this repo digests means strengthening or
  killing existing ones before minting new cards.
