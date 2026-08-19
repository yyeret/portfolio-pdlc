---
name: flow-harness-instrument
description: Decide what a workflow should measure and wire it in — flow measures (WIP, age, cycle time, throughput, rework), evidence measures (coverage, first-pass yield, escape rate, check agreement), leverage measures (delegate mix, human minutes per item, escalation rate, cost per item), and the outcome measure the stream exists for — with each measure named on the steps that feed it and a baseline taken before anything changes. Use when defining a workflow, when a board has numbers nobody steers with, or before making any workflow-improvement bet. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Instrument

## Outcome

`measures.md` holds a short list of measures that each name the decision they change, wired
into the steps that feed them, with baselines taken and the refusals stated. The board
computes what it can compute; the rest has a named moment when someone records it.

## Workflow

1. **Start from decisions, not from data.** List the decisions this stream actually makes:
   what to pull next, whether to promote a step, whether to publish, where to invest. Then
   ask what number would change each one. Measures with no decision attached do not get
   written down — that is the whole filter.
2. **Cover the four families** (`measurement.md`): flow, evidence and quality, leverage,
   outcome. A plan missing *leverage* cannot tell you whether agents are helping; a plan
   missing *outcome* cannot tell you whether the stream should exist.
3. **Name the outcome measure explicitly.** If the stream genuinely has none available yet,
   write that down rather than substituting an activity count. An unmeasurable stream is a
   legitimate state; a stream measuring its own busyness is not.
4. **Split steering from watch.** Steering measures are read every cycle or review; watch
   measures are diagnostics for the meta-loop. Keeping the steering list short is what stops
   people optimising diagnostics.
5. **Wire them in.** Add ids to the `measure-set` island in `measures.md` and to each step's
   `measures:`. Run `flow_lint.py` — it fails on a step naming a measure nobody declared,
   which is the cheap mechanical guard against measurement drift.
6. **Say where each number comes from.** Board-computed (free, ungameable), recorded at a
   step (name the moment — human minutes at the terminal step, escalations when they
   happen), or external (analytics, CI, finance). Anything with no source is a wish.
7. **Take baselines before changing anything**, with dates and n. An improvement bet without
   a baseline is a story with a number in it.
8. **Write the refusals.** Agent activity counts, volume as a goal, individual throughput,
   anything nobody would act on. Writing them down stops them arriving later by default,
   because they are the easiest numbers to collect.
9. **Schedule the watermelon check** into the review cadence: one clean-looking item, read
   its actual evidence, record what you find.

## Rules

- Every measure names the decision it changes. No exceptions, including for the ones
  leadership asks for by name — for those, name the decision *they* would make with it.
- **Medians over averages, percentiles over medians, and n over both.** The scripts refuse a
  step median under three samples; hold yourself to the same bar in the prose.
- **Check agreement is the promotion currency.** If you plan to move any step up the ladder,
  start collecting it now, during a shadow run — it costs nothing extra and cannot be
  reconstructed later.
- **Human minutes per item is the honest headline.** Cycle time can improve while humans do
  more work; only this measure catches displacement dressed as leverage.
- Do not add a measure to fix a behaviour. Measures inform decisions; policies change
  behaviour.
- Never let a measure become a target without saying who set the target and why — and expect
  it to be gamed the moment it does.

## Quality Gates

- Every measure in `measures.md` has a definition, a source, and the decision it changes.
- All four families represented, or the absence is explained.
- Every step's `measures:` are declared; `flow_lint.py` clean.
- Baselines recorded with dates and n before any improvement bet starts.
- The refusal list exists.

## References

- `skills/flow-harness/references/measurement.md` — the four families, the anti-measures,
  leading vs lagging, the watermelon check.
- `skills/flow-harness/templates/measures.md` — the file this produces.
- `skills/flow-harness/references/loop-probes.md` — how the meta-loop reads these numbers.
