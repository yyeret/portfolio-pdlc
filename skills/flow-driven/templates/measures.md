# Measurement Plan — <Stream Name>

What we steer on, what we watch, and what we refuse to measure. Every measure here answers
"what decision would change if this number moved?" — if nothing would, delete it.

## Steering measures

The short list leadership and the loop actually use.

| Id | Measure | Definition | Source | Steers what |
|---|---|---|---|---|
| item-age | Days in current step | today − `step_entered` | board | pull decisions, aging flags |
| step-cycle-time | Median days in a step | flow-log transitions | board | where the flow actually waits |
| throughput | Items reaching terminal per month | flow-log | board | capacity conversations |
| rework-rate | Back-edge traversals ÷ exits per step | flow-log | board | which step's exit is too weak |
| evidence-coverage | Evidence-exit transitions with recorded evidence ÷ all | items + flow-log | board | whether exits are real |
| escalation-rate | Escalations per item | item `## Escalations` | manual/agent | where context is missing |
| human-minutes-per-item | Human time per finished item | timing or estimate | manual | leverage, honestly |
| <outcome-measure> | <the thing this stream exists to move> | <source> | <where> | <the investment decision> |

## Watch measures

Diagnostics the meta-loop reads; not targets, and never reported as achievements.

| Id | Measure | Why we watch it |
|---|---|---|
| wip-by-step | Items per step vs limit | the earliest signal of a system under strain |
| waiting-share | Items blocked or waiting-decision ÷ items in flow | how much of the flow is queueing on humans |
| delegate-mix | Items by delegate rung | is leverage actually growing |
| cost-per-item | Agent spend per finished item | is autonomy paying for itself |
| first-pass-yield | Items reaching terminal with no back-edge | quality at the source |
| escape-rate | Defects found after the last evidence exit | whether the checks are real |

## What we refuse to measure

- **Agent activity** — prompts run, tokens spent, steps executed. These are costs, not
  outcomes; making them targets produces busy pipelines.
- **Individual throughput** — the system, not the person, sets the rate.
- **Anything nobody would act on.** A measure with no decision attached is a decoration.

## Watermelon check

Once a cadence, take one item that looks green and ask: what is the *evidence* behind its
last exit? If the honest answer is "the agent said so", the measure is reporting
compliance, not confidence. Record the finding as a learning.

## Baselines

| Measure | Baseline | As of | Target (if any) |
|---|---|---|---|
| <id> | <value> | <date> | <value, or "watch only"> |

Take the baseline before changing anything. A workflow improvement without a baseline is
a story, not a bet.

<!-- measure-set
steering: item-age, step-cycle-time, throughput, rework-rate, evidence-coverage, escalation-rate, human-minutes-per-item
watch: wip-by-step, waiting-share, delegate-mix, cost-per-item, first-pass-yield, escape-rate
outcome:
-->
