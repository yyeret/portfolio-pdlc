# Measurement Plan — FIY Content Engine

What we steer on, what we watch, and what we refuse to measure.

## Steering measures

| Id | Measure | Definition | Source | Steers what |
|---|---|---|---|---|
| item-age | Days in current step | today − `step_entered` | board | what to pull next |
| step-cycle-time | Median days in a step | flow-log | board | where the flow actually waits |
| throughput | Pieces reaching `shipped` per month | flow-log | board | what we can promise |
| rework-rate | `edit -> draft` traversals ÷ exits from `edit` | flow-log | board | whether `draft`'s exit evidence is real |
| evidence-coverage | Evidence-exit transitions with recorded evidence ÷ all | items + flow-log | board | whether exits are real or decorative |
| escalation-rate | Escalations per item | item `## Escalations` | manual | which context pack is missing |
| human-minutes-per-item | Dana-minutes per shipped piece | timesheet estimate at `learn` | manual | whether leverage is actually growing |
| hypothesis-confirm-rate | Readouts calling `confirmed` ÷ readouts | learn readouts | manual | whether we understand the audience |

## Watch measures

| Id | Measure | Why we watch it |
|---|---|---|
| wip-by-step | Items per step vs limit | earliest signal of strain |
| waiting-share | Blocked or waiting-decision ÷ in flow | how much of the flow queues on humans |
| delegate-mix | Items by rung | is the ladder moving |
| cost-per-item | Agent spend per shipped piece | is autonomy paying for itself |
| first-pass-yield | Shipped with no back-edge | quality at the source |
| escape-rate | Corrections needed after publication | whether the checks are real |

## What we refuse to measure

- **Publishing volume as a goal.** This stream can produce infinite plausible pieces; that
  is the failure mode, not the aspiration.
- **Words drafted, prompts run, tokens spent.** Costs, not outcomes.
- **Anything nobody would act on.** If a number moves and no decision changes, drop it.

## Watermelon check

Every Friday, take one piece that shipped green and read the evidence behind its `edit`
exit. If the honest answer is "the draft was fluent and the editor was tired", record it as
a learning — that is the real state of the system, and the board should say so.

## Baselines

| Measure | Baseline | As of | Target |
|---|---|---|---|
| step-cycle-time (`edit`) | 4d median | 2026-07-31 | watch only |
| rework-rate (`edit`) | 2 of 9 exits (22%) | 2026-07-31 | watch only — a *rising* rate is the signal |
| human-minutes-per-item | ~180 min | 2026-07-31 | 120 min by 2026-Q4 |
| evidence-coverage | 100% | 2026-08-19 | hold at 100% |
| hypothesis-confirm-rate | 3 of 7 | 2026-07-31 | watch only |

<!-- measure-set
steering: item-age, step-cycle-time, throughput, rework-rate, evidence-coverage, escalation-rate, human-minutes-per-item, hypothesis-confirm-rate
watch: wip-by-step, waiting-share, delegate-mix, cost-per-item, first-pass-yield, escape-rate
outcome:
-->
