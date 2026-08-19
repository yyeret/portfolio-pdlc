---
name: flow-harness-scaffold
description: Materialise a definition of workflow as a working flow workspace — workflow.md with its graph, one step contract per step with real stubs, item cards, measures, integration bindings, platform context-pack and check stubs, and the first generated board — so a human or agent can take over from a running skeleton rather than a blank page. Use after defining or ingesting a workflow, when standing up a second stream, or when an existing workspace needs missing pieces filled in. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Scaffold

## Outcome

A folder that passes `flow_lint.py`, generates a board, and produces a sensible run card on
the first `flow_next.py` — with every stub carrying a *starting point* rather than a `TODO`.
The test: a person who was not in the definition workshop can read the workspace and run a
cycle.

## Inputs

A definition of workflow (from `flow-harness-define` or `flow-harness-ingest`), even a rough
one. Plus: where the work lives today, who owns the stream, and any items currently in flight.

## Workflow

1. **Create the skeleton** from `skills/flow-harness/templates/`:
   `workflow.md`, `steps/<id>.md` per step, `measures.md`, `integrations.md`, `AGENTS.md`,
   and the directories `items/`, `platform/{context,prompts,checks}/`, `improvements/`,
   `learnings/`, `reviews/`.
2. **Write the `flow-config` block first** — including `unit` and `unit_outcome` — and lint
   it before writing any prose. A graph that does not validate makes every downstream file a
   guess, and a workspace with no stated unit cannot be checked against anything.
3. **Fill every step contract with a real starting point**, not a placeholder:
   - exit evidence drafted from what already convinces the person who checks that step today;
   - a rung with its reason, defaulting to what people do *now* rather than to the ambition;
   - a run model — `run: human` with an empty `run_ref` is an honest, common answer;
   - escalation contract for anything at rung 2+.
4. **Stub the platform.** For every context pack a step names, create
   `platform/context/<pack>.md` from the template with the provenance section filled in and
   the knowledge section seeded from whatever exists — even three bullet points and a link.
   For every `verify_with`, create the check stub with its sceptic's brief. An unreferenced
   pack file is worse than none: it looks like coverage.
5. **Card the work in flight.** One `items/<slug>/item.md` per live item, at the step the
   evidence says it is on — not where anyone wishes. Missing hypotheses stay missing; that is
   a finding for the first cycles, not an embarrassment to paper over.
6. **Seed history if it exists** into `flow-log.csv` chronologically. This is the ONE
   sanctioned hand-touch of that file, done before the first board run, so cycle time and
   rework are computable from day one.
7. **Generate and read the first board.** `flow_lint.py` until clean, then `flow_board.py`,
   then `flow_next.py`. Read what the board says out loud — the first board is usually the
   most informative artefact the team has had in months.
8. **Write the scaffold brief** (`reviews/YYYY-MM-DD-scaffold.md`): what was created, what
   was defaulted and needs a human, the board's first three headlines, and the first cycle's
   likely move.

## Rules

- **Stubs are starting points, never `TODO`.** A stub that cannot be improved into something
  real in ten minutes is not a stub, it is a gap — say so in the brief.
- **Honest state.** Items go where the evidence puts them. Backdating `step_entered` to make
  ages look better breaks every metric that follows.
- **Do not fix while scaffolding.** Weak hypotheses, activity-framed titles, and missing
  evidence get recorded as-is. Improving them is a later cycle's move.
- **Scaffold only what the definition names.** Extra folders, extra steps, and speculative
  packs are how a workspace becomes a filing system.
- Nothing generated gets hand-edited: `board.md`, `flow-log.csv`, `exports/`.

## Quality Gates

- `flow_lint.py`: zero violations; every remaining warning is deliberate and named in the brief.
- `unit` and `unit_outcome` are stated, and the items carded actually match that unit.
- `flow_next.py` produces a sensible run card on the first run.
- Every step contract has exit evidence, a rung with a reason, and a run model.
- Every named context pack and check exists with real starting content.
- The brief lists what was defaulted and who needs to confirm it.

## References

- `skills/flow-harness/templates/` — every file this skill instantiates.
- `skills/flow-harness/references/workflow-definition.md` — the contract being satisfied.
- `skills/flow-harness/example/fiy-content-engine/` — what a filled-in workspace looks like.
- Next: `flow-harness-run` for the first cycle.
