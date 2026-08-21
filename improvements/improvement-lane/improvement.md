---
title: This repo's own process changes ride a lane instead of landing as direct edits
type: improvement-convention
stage: watching
owner: Yuval
opened: 2026-08-21
benefit_hypothesis: "If changes to how this repo works are filed as cards with kill criteria before they land, we can tell later which conventions were bets and which were assumptions — because the reasoning and the falsifier are written down while they are still cheap to write"
measures: [process-changes-riding-the-lane, direct-process-edits-merged, cards-reverted]
baseline: "Two process changes shipped before the lane existed — agent-merge-authority and bounded-review-loop — both as direct edits; C4 fired on the first one in review"
kill_criteria: "If a process change merges as a direct edit anyway, the lane is not load-bearing and belongs in the quality bar as a check instead. And if three consecutive cards are opened, probed and adopted inside the same pull request that raised them, the lane is ceremony around a decision already made — delete it and say so."
probe: "This pull request: the lane's first act is to file the two changes already in flight, and itself, as cards"
---

# This repo's own process changes ride a lane instead of landing as direct edits

## The signal

`AGENTS.md` has told every workspace since the first commit that changes to a definition of
workflow are captured as bets with kill criteria, never edited in passing. This repo then
changed its own operating model twice — merge authority, then the bounded review loop — by
editing `AGENTS.md` and `docs/quality-bar.md` directly. The independent review of the first
one flagged it under C4. The convention pointed at an improvement lane that did not exist.

## Benefit hypothesis

If process changes here are filed as cards before they land, then a year from now we can
separate the conventions we bet on from the ones we assumed, **because** a card forces the
mechanism and the kill criteria to be written while they are still cheap — after adoption,
nobody can reconstruct what would have counted as evidence against.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | C4 stays a rule this repo breaks in public | — |
| a checklist item in the quality bar | reviewer asks "was this captured?" | xs | catches the omission at review time, records no reasoning | yes |
| an improvements lane | `improvements/`, one folder per bet | s | ceremony if process changes here are rare | yes |
| a full flow workspace for the repo | steps, WIP limits, board | m | far more machinery than a handful of process changes a year needs | yes |

The checklist option is the real alternative and it is cheaper. It loses the thing that
matters: a check confirms a card exists, it does not make anyone write down what would
falsify the change.

## Probe

This pull request. The lane's first act is to file `agent-merge-authority` and
`bounded-review-loop` — both already in flight — as cards, plus this one. Filing a bet you
have already made is the honest test of whether the card format captures anything the
commit message did not. Where it only restated the commit, the lane is paperwork; where it
forced a kill criterion nobody had written, it earned its place.

Read: both existing cards gained falsifiers that were not in their commits. The merge-
authority bet had no stated escape condition until it was carded; now it has one, and it is
a revert rather than a warning.

## Adoption

Adopted on the request that raised it — the lane exists as of this pull request. The
bootstrap is unavoidably a direct edit: a lane cannot be created by riding itself. It is
meant to be the last one.

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|
| 2026-08-21 | process-changes-riding-the-lane | 3 of 3 | the two in-flight bets and this one were filed as cards; no process change is currently un-carded |

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
| 2026-08-21 | Build the lane | Yuval | "C4 cobblers kids etc. add a simple improvements agentic lane" |
