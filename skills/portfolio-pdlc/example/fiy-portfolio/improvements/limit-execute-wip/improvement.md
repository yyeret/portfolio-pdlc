---
title: Committed work finishes faster under a tighter execute WIP limit
type: improvement-process
tier: 1
stage: discovery
stage_entered: 2026-08-10
owner: Noa
sponsor: Jim
outcome_hypothesis: "If execute WIP drops from 4 to 3, execute cycle time falls enough to raise annual throughput despite starting later"
leading_indicators:
  - "simulated P50 cycle time delta beyond noise band → yes/no (current: pending)"
  - "if piloted: execute-stage median age → -20% (current: baseline from flow-log)"
risk_level: medium
derisking_approach: discovery
orientation: outcome
portfolio_score: 5
dependencies: []
next_decision: "2026-08-30 — pilot the tighter limit for a quarter? (trio)"
---

# Committed work finishes faster under a tighter execute WIP limit

## Problem / Opportunity

Execute holds the two oldest cards; right-to-left reviews keep finding "everything moving,
nothing finishing."

## Benefit hypothesis

Fewer simultaneous committed bets → less multi-tasking on shared teams → faster finishes;
the classic stop-starting-start-finishing bet at portfolio altitude.

## Success / kill criteria

Keep if piloted quarter shows execute median age down ≥20% with throughput flat-or-up.
Kill if intake pressure just moves the queue upstream (plan-commit ages balloon) with no
finish-rate gain.

## Discovery approach

`portfolio-pdlc-simulate` scenario `reviews/scenarios/limit-execute-wip.txt` (WIP 4→3),
2000 runs; adopt-for-pilot decision only if the delta clears the noise band.

## Decision log

- 2026-08-10 — Jim: worth a simulation before we argue about it.

## Evidence log

- 2026-08-17 — simulation (500 runs, seed 7, multitask_alpha 0.25): P50 cycle time 217d
  baseline → 235d under WIP 3; throughput 14.4 → 12.9/yr. The bet does NOT clear the bar
  under current assumptions — execute runs at 2 of 4 slots today, so tightening the limit
  buys no multitasking relief while adding queue wait. Recommendation: de-risk further
  (revisit if execute fills up, or re-run with an evidence-based alpha), don't pilot yet.
