---
name: flow-harness-define
description: Define the workflow for a value stream — the systems read that produces steps, a graph (branches, back-edges, sub-graphs), exit evidence per step, pull policies and WIP limits, classes of service, decision points, delegate model and run model per step, and the cadences that keep it honest. Use when standing up a new agentic workflow, replacing an implicit process with an explicit one, or reworking a definition of workflow that no longer matches how work actually happens. Produces workflow.md and the step contracts. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Define

## Outcome

A definition of workflow the team recognises as *theirs*: `workflow.md` with a
machine-readable graph, one contract per step, and policies that describe how work actually
moves rather than how someone wishes it did. Written to be argued with and changed.

## The Systems Read — eight moves

A systems-thinking start-up sequence, in the spirit of the Kanban Method's approach to
introducing change, reworked for agentic flow: this version asks about delegation, evidence,
and context, which STATIK never had to. Do it with the people who do the work — 90 minutes
gets you a first draft.

1. **Dissatisfaction and aspiration.** What hurts today, for whom, in their words — and what
   "better" would look like. Capture both the pain and the leverage upside; a change
   justified only by upside gets abandoned when it costs something.
2. **Demand.** What arrives, at what rate, in what varieties. Name the classes of service
   that genuinely behave differently (expedite, standard, fixed-date, derisk-first) and the
   pull policy for each. If everything is expedite, nothing is.
3. **Capability and constraint.** Where does work actually wait? What capability exists —
   human, agent, tool, context? The constraint is rarely the step everyone talks about, and
   finding it is often the whole value of this conversation.
4. **Draw the flow.** Steps, entry, terminal states, branches, back-edges. Default to a
   straight line; add a branch when the work branches and a back-edge when rework is real.
   Give each step an id you can live with — it appears in every edge, item, and log row.
5. **Name the exits.** For each step: *what can you rely on when an item leaves here?*
   Artefacts and observations, never activities. Mark the steps where this must be enforced
   (`evidence_exits`) and the steps a human must authorise entry to (`decision_points`).
   This move produces more argument than the other seven combined, which is the point.
6. **Set the delegate model and run model per step.** Rung 0–5 with a reason grounded in
   reversibility and blast radius; run model (`skill | prompt | script | tool | human |
   external`) with context packs, tools, guardrails, budget, and a stop rule. Decide which
   steps deserve an inner graph — more than one failure mode, or a separable verify.
7. **Policies, limits, and cadences.** Pull policies, WIP limits (start looser than feels
   right and tighten on evidence), escalation contracts, review cadence, and — separately —
   the meta-loop cadence.
8. **Measures and system of record.** Name what you steer on and where the work lives.
   Route to `flow-harness-instrument` and `flow-harness-integrate`; do not improvise either.

## Workflow

1. Pick the closest archetype from `workflow-archetypes.md` and say which one — it becomes
   `kind:` and saves an hour of blank-page work.
2. Run the eight moves. Write as you go; a definition assembled afterwards from notes loses
   the disagreements, and the disagreements are the content.
3. Draft `workflow.md` from `templates/workflow.md`, including the `flow-config` block.
4. Draft one `steps/<id>.md` per step from `templates/step.md`. Every step needs intent,
   exit evidence, rung, run, and escalation before you stop — a stub with `TBD` in
   `exit_evidence` is an unfinished step, and the linter will say so.
5. Add inner graphs only where move 6 said so, each with `max_iterations` or a falsifiable exit.
6. Run `flow_lint.py`. Fix the graph until it is clean — unreachable steps, dead ends, and
   steps with no contract are all real design problems, not linter pedantry.
7. Write the delegation stance table into `workflow.md`: where each step sits today and what
   would promote it. Include the steps that will never move, and say why.

## Rules

- **Describe, then propose.** The first version is the workflow they have. Improvements are
  bets, and they come after a fortnight of running it.
- **Every step must be able to fail.** If nothing goes wrong at a step and nothing would
  break if items skipped it, delete it.
- **Skipping an optional step is a decision**, recorded on the item — never a default.
- **No step without exit evidence.** "We'll work it out" means the step is undefined and the
  first ten items will define it by accident.
- **Set rungs by reversibility, not by ambition.** The delegation stance is a design output,
  not an aspiration list.
- Keep step ids short and stable. Renaming one later touches every log row.

## Quality Gates

- `flow_lint.py` reports zero violations against the definition.
- Every step: intent, exit evidence a stranger could check, a rung with a reason, a run model
  with a stop rule, and an escalation contract at rung 2+.
- Every inner graph is bounded.
- Flow boundaries (start and end), classes of service, and cadences are written down.
- The delegation stance names what stays human permanently — and says why it is a choice.

## References

- `skills/flow-harness/references/workflow-definition.md` — the schema this produces.
- `skills/flow-harness/references/step-contracts.md` — delegation ladder, run models, how to
  write exit evidence.
- `skills/flow-harness/references/loop-engineering.md` — when a step deserves an inner graph.
- `skills/flow-harness/references/workflow-archetypes.md` — starting points by workflow kind.
- Next: `flow-harness-scaffold` to materialise it; `flow-harness-instrument` for measures.
