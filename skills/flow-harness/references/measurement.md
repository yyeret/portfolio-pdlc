# Measurement — what to steer on, and how it rides inside the workflow

A measure earns its place by naming the decision it changes. If nothing would be decided
differently, it is decoration — and decoration in a measurement plan is worse than nothing,
because it teaches people that numbers here are for looking at.

Measures live in `measures.md` with a machine-readable `measure-set`; each step names the
measures it feeds. The linter checks that every measure a step claims is actually declared,
which is a small mechanical way of stopping measurement drift.

## Four families

### 1. Flow — how work moves

| Measure | Definition | The decision it changes |
|---|---|---|
| WIP by step vs limit | items in a step | whether to start or finish |
| Item age in step | today − `step_entered` | which item to pull next |
| Cycle time by step (median) | consecutive transitions | where the real constraint is |
| Throughput | items reaching terminal per period | what we can honestly promise |
| Waiting share | blocked + waiting-decision ÷ in flow | whether the loop is starved by human attention |
| Rework rate by step | back-edge traversals ÷ exits | which exit evidence is too weak |

Percentiles beat averages; medians beat means; **n beats both** — a median over two samples
is a rumour. The scripts refuse to compute a step median under three samples for that reason.

### 2. Evidence & quality — whether "done" means anything

| Measure | Definition | The decision it changes |
|---|---|---|
| Evidence coverage | evidence-exit transitions with recorded evidence ÷ all | whether to trust the board at all |
| First-pass yield | items reaching terminal with no back-edge | where to invest in upstream quality |
| Escape rate | defects found after the last evidence exit | whether a check is real or ceremonial |
| Check agreement | check findings vs human findings on the same item | whether a step can be promoted |

**Check agreement is the promotion currency.** It is the measure that converts "the model
seems good at this" into a decision you can defend, and it is the one most teams never
collect. Collect it during a shadow run; it costs nothing extra.

### 3. Leverage — whether agents are actually helping

| Measure | Definition | The decision it changes |
|---|---|---|
| Delegate mix | items by rung | is the ladder moving, or just the rhetoric |
| Human minutes per item | measured or estimated at a terminal step | whether leverage is real |
| Escalation rate | escalations per item, by step | which context pack to write next |
| Cost per item | agent spend ÷ items finished | whether autonomy pays for itself |
| Questions-to-human | times a runner had to ask | the platform's headline number, trending down |

Human minutes per item is the honest headline. Cycle time can improve while humans do more
work — that is not leverage, it is displacement, and only this measure catches it.

### 4. Outcome — what the stream exists for

Archetype-specific and non-negotiable: an outcome measure means the stream can be judged on
something other than its own activity. Content: hypothesis-confirm rate. Development:
adoption or the business measure the bet claimed. Operational: resolution quality and
reopen rate. AI use-case: eval pass rate by slice and human override rate.

If a stream has no outcome measure, say so on the board. An unmeasurable stream is a
legitimate state; an unmeasured stream pretending otherwise is not.

## What not to measure

- **Agent activity** — prompts run, tokens burned, steps executed. Costs, not outcomes.
  Making them targets produces busy pipelines, and they are the easiest numbers to collect,
  which is exactly why they end up on dashboards.
- **Volume as a goal** in any generative stream. The system can produce infinite plausible
  output; that is the failure mode, not the aspiration.
- **Individual throughput.** The system sets the rate.
- **Anything with no decision attached.**

## Wiring measures into the workflow

1. Declare them in `measures.md` (`measure-set` island: steering / watch / outcome).
2. Name them per step in the step contract's `measures:`.
3. Let the board compute what is computable from item state and the flow log — those
   measures cost nothing per cycle and cannot be gamed by anyone's memory.
4. Record the rest at a natural moment: human minutes at the terminal step, escalations when
   they happen, check agreement during a shadow run.
5. Baseline **before** changing anything. An improvement bet without a baseline is a story.
6. Read them in the meta-loop, not continuously. Measures reviewed daily become targets.

## The watermelon check

Green outside, red inside — the default failure mode of any system where the reporter and
the doer are the same. Once a cadence:

1. Take one item that looks clean.
2. Read the actual evidence behind its last exit.
3. Ask: would a stranger agree this step happened?

If the honest answer is "the agent said so", you have learned the state of your system. It
goes in `learnings/`, and if it recurs, into an improvement bet. Agents make this failure
more likely, not less: they are fluent, they never look tired, and their output has none of
the tells a rushed human's does.

## Leading vs lagging, honestly

Most useful measures here are lagging (cycle time, escape rate). The leading ones are:
**waiting share**, **evidence coverage**, and **questions-to-human**. They move first,
they are cheap, and they predict the lagging ones. Watch those three weekly and the rest
monthly.
