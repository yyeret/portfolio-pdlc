# Loop Engineering — the point of view

Most "agentic workflow" work specifies the move and nothing else: a prompt, a chain, maybe
a retry. That is not a workflow, it is a function call with ambition. A workflow is a **flow
system**, and a flow system needs a trigger, a bounded move, an evidence-based exit, and a
recorded trace — at two levels: the **outer loop** that moves items through the graph, and
the **inner loop** that gets one step done.

Everything else in this skill family is downstream of that claim.

## The two loops

```
OUTER (the flow)                          INNER (one step)
  project state                             frame the move
  sense the flow                            gather context
  select ONE move   ─────────────────►      act
  run the step under its contract           self-check
  verify against exit evidence      ◄────── verify independently
  record + hand off                         exit with evidence, or escalate
  (on cadence) adapt the loop itself
```

They fail differently, so they need different design. The outer loop fails by **drifting**:
work piles up invisibly, status detaches from reality, decisions go unmade, everything is
started and nothing finishes. The inner loop fails by **flattering**: fluent output, a
self-graded check, an unbounded revise cycle that converges on plausibility.

## Ten principles

**1. Steer on position and age, not on a task list.**
The unit of steering is "where is this item in the graph and how long has it been there",
not "what is everyone doing". A to-do list cannot tell you that a step is starving or that
the constraint has moved; a flow can.

**2. One move per cycle.**
Parallelism is a property of *many items*, not of one cycle. A cycle that advances five
things advances none of them traceably, and when it goes wrong you cannot say which move
caused it. Fan-out belongs in the item count, not in the cycle.

**3. Pull, don't push.**
A step takes work when it has capacity. WIP limits are the mechanism, and their real value
is not efficiency — it is that they force the finishing conversation to happen before the
starting one. In agentic systems the temptation is worse than in human ones, because
starting is nearly free and finishing is not.

**4. Exit evidence beats status.**
A step is finished when its evidence exists, not when a run completes without erroring.
Agents are fluent; fluency reads as completion. Write exit evidence as artifacts and
observations a stranger could check — "review findings recorded, unresolved ones listed",
never "reviewed".

**5. The verifier must not be the doer.**
Ranked by strength: a deterministic script, a different agent with a different context and
an adversarial brief, the same agent in a fresh context, the same agent in the same context
(worthless). Self-verification in the same context is not a weak check; it is theatre.

**6. Bound every inner loop.**
Max iterations, a budget, or a falsifiable exit. Critique-revise loops do not converge on
truth; they converge on prose that survives critique. Two passes then out to a human beats
six passes and a confident summary.

**7. Derisk before the point of last return.**
In complex knowledge work the expensive failure is confidently executing the wrong thing.
Put a cheap probe *before* commitment, make skipping it an explicit decision, and treat a
"stop" result as a win — a dropped item with a recorded probe saved a week.

**8. Reversibility governs autonomy.**
The delegate rung of a step is a function of blast radius and reversibility, not of how
impressive the model is this month. A reversible step with a mechanical failure mode can
run unattended today; an irreversible one with a reputational failure mode stays human even
when the agent could technically do it.

**9. Context is the product.**
Most step quality comes from what the runner can see, not from how the prompt is phrased.
Every question an agent has to ask a human is a missing context artifact. Capture it once,
and the next run does not need the human — that is the whole platform play, and it is what
compounds.

**10. Small state, big trace.**
Item frontmatter is the state; boards, logs, and trackers are projections. Regenerate,
never reconcile. And log every transition: the trace is what makes the meta-loop possible,
and a system that cannot see its own history cannot improve.

## Designing the outer loop

Six beats, in this order, every cycle:

| Beat | What it is | The failure it prevents |
|---|---|---|
| **Project** | regenerate the board from the items | steering from memory or a stale view |
| **Sense** | read the flow: aging, WIP, blocked, evidence gaps, waiting humans | reacting to whoever shouted |
| **Select** | one move, from a deterministic leverage table | picking the interesting move over the valuable one |
| **Run** | execute the step under its contract | improvised work with no budget or stop rule |
| **Verify** | check the exit evidence, independently | watermelon steps |
| **Record** | update item state, log the transition, one line in the loop log | a system with amnesia |

The leverage table matters more than it looks. Ordering the rules encodes what the system
believes: **waiting decisions starve everything downstream; a broken definition of workflow
lies to every later cycle; blocked work is a human handoff and never fixes itself; finishing
outranks starting; and only a clean, flowing board earns the luxury of self-improvement.**
Ship a table, argue about the order, and change it deliberately — that argument is more
valuable than any individual rule.

A cycle should be *small*. If one cycle can take an item from intake to published, the steps
are not steps; they are one step wearing a costume.

## Designing a step (the inner loop)

A step contract answers six questions. If you cannot answer them, you do not have a step —
you have an intention.

1. **Intent** — why this exists; what breaks if items skip it. If nothing breaks, delete it.
2. **Exit evidence** — what you can rely on when an item leaves.
3. **Delegate model** — which rung, and why *this* rung (see `step-contracts.md`).
4. **Run model** — skill, prompt, script, tool, human, or external system, plus the context
   packs, the tool set, the guardrails, the budget, and the stop rule.
5. **Verification** — what checks the work, and how it is independent of what did it.
6. **Escalation** — the condition under which the runner stops and asks, and who it asks.

### When a step deserves an inner graph

Add a mini-graph inside a step when at least one of these is true:

- it has **more than one distinct failure mode** (wrong structure *and* invented facts *and*
  wrong voice) — one long generation cannot be checked against three different standards;
- its **verify is separable** from its work, so the two should not share a context;
- it **repeats** with variation, so the sequence is worth naming rather than re-improvised;
- it has a **natural stop rule** that only makes sense inside the step (two revise passes).

Do *not* add one because the step feels big. A big step with one failure mode is a step.
And keep inner nodes private: items never sit on them, the board never shows them, the flow
log never records them. The moment work *waits* on an inner node, it is not an inner node —
it is a step you have not admitted to yet.

## Failure modes of agentic loops

| Failure | What it looks like | The countermeasure in this harness |
|---|---|---|
| **Watermelon step** | green board, no evidence behind an exit | `evidence_exits` + `evidence_exits_met`, enforced by the linter |
| **Fan-out** | a cycle that touches nine items and finishes none | one move per cycle; everything else is an improvement card |
| **Unbounded inner loop** | critique-revise until the budget dies | `max_iterations` required on any inner loop edge |
| **Self-graded work** | the runner passes its own check | `verify_with` must differ from `run_ref`; rung 4+ requires it |
| **Context rot** | confidently wrong because the pack is stale | context packs carry provenance, expiry, and a rot signal |
| **Decision starvation** | everything ready, nobody deciding | rule 1 of the leverage table; `next_decision` with a date and a name |
| **Silent scope drift** | the workflow changes by accident, one edit at a time | changes to the definition of workflow are bets with a change log |
| **Metric theatre** | dashboards nobody steers with | every measure names the decision it changes, or gets deleted |
| **Autonomy ratchet** | rungs only ever go up | demotion criteria written at promotion time |
| **Ghost step** | a step in the definition that never fires | the meta-loop's ghost-step probe |

## What this is not

It is not a workflow engine, and it deliberately does not try to be. There is no runtime,
no daemon, no DAG scheduler. The graph is markdown, the state is frontmatter, the
orchestration is a deterministic selector plus whatever agent happens to be reading. That
constraint is the feature: a workflow you can read, diff, argue with, and run by hand when
the tooling is missing will still be there in two years, and it works from any harness.
