---
title: Drafting runs to a verified exit instead of stopping at a human
type: improvement-delegation
stage: probing
owner: Dana
opened: 2026-08-10
benefit_hypothesis: "If the house-voice check catches what Dana catches, draft can move to rung 3 and edit becomes a judgement step rather than a cleanup step"
measures: [rework-rate, human-minutes-per-item, escape-rate]
baseline: "rework-rate out of edit = 22% (2 of 9) as of 2026-07-31; house-voice check agreement with Dana's findings = 4 of 10 items"
kill_criteria: "Agreement below 8 of 10 items after 10 more pieces, or any untraced claim reaching publish — then stay at rung 2 and say so"
probe: "Score the house-voice check against Dana's edit findings on the next 10 items, rule by rule; no change to the flow while probing"
---

# Drafting runs to a verified exit instead of stopping at a human

## The signal

`edit` is the human-heaviest step in the stream and much of it is not judgement: on the
last 10 items, over half of Dana's findings were rule 1 and rule 3 violations that
`platform/checks/house-voice.md` also flagged. Meanwhile rework out of `edit` sits at 22%,
which says the `draft` exit evidence is not yet load-bearing.

## Benefit hypothesis

If the house-voice check reliably catches the mechanical findings, then `draft` can exit at
rung 3 with a verified exit, `edit` becomes a judgement-only step, and
human-minutes-per-item falls toward the 120-minute target — because Dana stops doing what a
check can do.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | the target stays out of reach; Dana stays the bottleneck | — |
| strengthen the check, keep rung 2 | check improves, human still edits everything | s | slow, but safe | yes |
| promote `draft` to rung 3 now | agent exits on its own check | s | fluent-but-wrong drafts reach `edit` with a green tick | yes |
| strengthen, measure agreement, then promote | probe first | m | slower by three weeks | yes |

## Probe

Score the check against Dana's findings on the next 10 items, rule by rule. Nothing about
the flow changes while probing — this is measurement, not a pilot.

- **Timebox**: 2026-08-10 → 2026-09-15
- **Proceed if**: agreement ≥8 of 10 items, and rule 4 (concede the counter-argument)
  agreement ≥6 of 10
- **Stop if**: agreement below 8 of 10, or any untraced claim reaches `publish`

## Adoption

If it proceeds: `steps/draft.md` to `delegate_rung: 3`, `edit` intent rewritten as judgement
only, and both changes logged in `workflow.md`.

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|
| 2026-08-19 | check agreement | 4 of 10 | probing — rule 4 is where it misses |

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
| 2026-08-10 | Start the agreement probe; no flow change | Dana | edit findings analysis |
