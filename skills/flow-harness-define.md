---
name: flow-harness-define
description: Define the workflow for a value stream by discovering it, deriving it, or adapting it — interview people about how work actually happens today and match it against archetypes; or, when no workflow exists, derive one from first principles and explain why working this way is worth it. Produces the unit of value, the steps and graph (branches, back-edges, sub-graphs), exit evidence per step, pull policies and WIP limits, classes of service, decision points, delegate and run model per step, and cadences. Use when standing up a new agentic workflow, surfacing an implicit one, or reworking a definition that no longer matches reality. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.1.0
---

# Flow Harness — Define

## Outcome

A definition of workflow the team recognises as *theirs*: a stated unit of value,
`workflow.md` with a machine-readable graph, and one contract per step — describing how work
actually moves rather than how someone wishes it did. Written to be argued with and changed.

## Three paths in

Establish which one you are on before asking anything else. Most streams are a mix; say
which parts came from where, because the folklore parts are the ones most likely to be wrong.

| What exists | Path | Do this |
|---|---|---|
| A formal artefact — spec-kit, Kiro, a bespoke harness, a tracker with states | **Adapt** | Load `flow-harness-ingest` first, then return here for what the artefact does not cover: exits, delegation, decisions, and the human glue |
| A real workflow living in habits and folklore | **Discover** | Interview it out — `references/discovery-interview.md`. Do not propose anything until the trace is on the page |
| Genuinely nothing — new stream, new team, new capability | **Derive** | Build it from the value — `references/first-principles.md`. Lead with *why* work this way, not with a template |

**Discover** is the common case and the one people skip. Almost nobody has no workflow; they
have one nobody has written down, running on habit and on one person who notices when things
stall. Ask about the last real item, never about "the process" — people describe the process
they wish they had and remember the thing they actually did last Tuesday.

**Derive** is a teaching path, not a form-filling one. If nobody has worked this way before,
the first deliverable is the rationale: why an explicit workflow, why steps, why evidence at
the exits, why limits, and what each buys you. A workflow people cannot defend is one they
abandon the first time it costs them something. `first-principles.md` carries that argument
and ends with the smallest honest starting workflow — three steps, one exit, one limit.

On the Discover path, once you have a trace, **match it against the archetypes** in
`workflow-archetypes.md` on *failure mode and evidence shape*, not vocabulary. Three or more
tells plus a recognised failure mode → propose that archetype as a starting point, naming
where their trace already differs. Two archetypes matching → probably two streams; split
them. None matching → custom is a perfectly good answer; build from the trace and steal exit
evidence from the nearest archetype. Always present a match as a proposal with an
alternative, never as a classification.

## The Systems Read — nine moves

A systems-thinking start-up sequence, in the spirit of the Kanban Method's approach to
introducing change, reworked for agentic flow: this version asks about the unit, delegation,
evidence, and context, which STATIK never had to. Ninety minutes with the people who do the
work gets a first draft.

1. **Dissatisfaction and aspiration.** What hurts today, for whom, in their words — and what
   "better" looks like. Capture both the pain and the leverage upside; a change justified
   only by upside gets abandoned when it costs something.
2. **The unit of value.** *What is one item?* Name it as an outcome, not an artefact or a
   task — "a piece that changes one operating decision", not "a blog post". Run the five
   tests in `references/unit-of-value.md`. Everything below is defined relative to this
   answer: the steps are what happens to one, the limits count them, cycle time is how long
   one takes. Get it wrong and the board cannot answer a single useful question. Write it
   into `flow-config` as `unit` (required) and `unit_outcome` (what changes, for whom).
3. **Demand.** What arrives, at what rate, in what varieties. Name the classes of service
   that genuinely behave differently — expedite, standard, fixed-date, derisk-first — and the
   pull policy for each. If everything is expedite, nothing is.
4. **Capability and constraint.** Where does work actually wait? What capability exists —
   human, agent, tool, context? The constraint is rarely the step everyone talks about, and
   finding it is often the whole value of the conversation.
5. **Draw the flow.** Steps, entry, terminal states, branches, back-edges. On the Derive
   path, get steps by asking *what has to become true before an item is valuable* — a step
   exists to retire a distinct kind of doubt, not to name an activity. Default to a straight
   line; add a branch when the work branches and a back-edge when rework is real.
6. **Name the exits.** For each step: *what can you rely on when an item leaves here?*
   Artefacts and observations, never activities. Mark which must be enforced
   (`evidence_exits`) and which steps a human must authorise entry to (`decision_points`).
   This move produces more argument than the other eight combined, which is the point.
7. **Set the delegate model and run model per step.** Rung 0–5 with a reason grounded in
   reversibility and blast radius; run model (`skill | prompt | script | tool | human |
   external`) with context packs, tools, guardrails, budget, and a stop rule. Decide which
   steps deserve an inner graph — more than one failure mode, or a separable verify.
8. **Policies, limits, and cadences.** Pull policies, WIP limits (start looser than feels
   right and tighten on evidence), escalation contracts, the loop cadence and — separately —
   the meta-loop cadence.
9. **Measures and system of record.** Name what you steer on and where the work lives. Route
   to `flow-harness-instrument` and `flow-harness-integrate`; do not improvise either.

## Workflow

1. Establish the path (Adapt / Discover / Derive) and say so out loud.
2. On Discover: run the interview ladder, then write
   `reviews/YYYY-MM-DD-workflow-discovery.md` — the trace, who said what including the
   unresolved disagreements, the draft graph with provenance per element (observed / stated
   / inferred), the archetype verdict, and the five questions that would most change it.
3. On Derive: work `first-principles.md` and record the rationale alongside the definition.
   The "why" is part of the deliverable — it is what survives the first inconvenience.
4. Run the nine moves. Write as you go; a definition assembled afterwards from notes loses
   the disagreements, and the disagreements are the content.
5. Draft `workflow.md` from `templates/workflow.md`, including the unit-of-value section and
   the `flow-config` block.
6. Draft one `steps/<id>.md` per step from `templates/step.md`. Every step needs intent, exit
   evidence, rung, run, and escalation before you stop — `TBD` in `exit_evidence` is an
   unfinished step, and the linter will say so.
7. Add inner graphs only where move 7 said so, each with `max_iterations` or a falsifiable exit.
8. Run `flow_lint.py`. Unreachable steps, dead ends, a missing unit, and steps with no
   contract are design problems, not linter pedantry.
9. Write the delegation stance table into `workflow.md`: where each step sits today and what
   would promote it — including the steps that will never move, and why that is a choice.

## Rules

- **Describe, then propose.** The first version is the workflow they have. Improvements are
  bets, and they come after a fortnight of running it. The moment you propose during
  discovery, people stop describing.
- **The unit is not optional.** A definition that cannot say what flows cannot be checked
  against anything; `flow_lint.py` treats a missing `unit` as a violation.
- **Every step must be able to fail.** If nothing goes wrong at a step and nothing would
  break if items skipped it, delete it.
- **Skipping an optional step is a decision**, recorded on the item — never a default.
- **No step without exit evidence.** "We'll work it out" means the step is undefined and the
  first ten items will define it by accident.
- **Record disagreements, do not resolve them.** Two people describing different workflows is
  a finding, usually about a handoff, and it belongs to the team to settle.
- **Set rungs by reversibility, not by ambition.** The delegation stance is a design output.
- Keep step ids short and stable. Renaming one later touches every log row.

## Quality Gates

- The path (Adapt / Discover / Derive) is stated, and each element's provenance is traceable
  to an artefact, a named person, or an explicit inference.
- `unit` and `unit_outcome` are written, and the unit passes the five tests.
- `flow_lint.py` reports zero violations.
- Every step: intent, exit evidence a stranger could check, a rung with a reason, a run model
  with a stop rule, and an escalation contract at rung 2+.
- Every inner graph is bounded.
- Flow boundaries, classes of service, and cadences are written down.
- On Derive, the rationale is recorded — not just the resulting steps.

## References

- `skills/flow-harness/references/discovery-interview.md` — the interview ladder, what to
  listen for, and archetype matching.
- `skills/flow-harness/references/first-principles.md` — why work this way, the seven-question
  derivation, the objections, and the smallest honest starting workflow.
- `skills/flow-harness/references/unit-of-value.md` — choosing and sizing what flows.
- `skills/flow-harness/references/workflow-definition.md` — the schema this produces.
- `skills/flow-harness/references/step-contracts.md` — delegation ladder, run models, exit evidence.
- `skills/flow-harness/references/workflow-archetypes.md` — starting points and their tells.
- Next: `flow-harness-scaffold` to materialise it; `flow-harness-instrument` for measures.
