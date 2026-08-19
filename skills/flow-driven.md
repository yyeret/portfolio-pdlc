---
name: flow-driven
description: Turn any value stream — a PDLC, an SDLC, a content pipeline, an AI use-case pipeline, an operational request stream — into a flow-driven agentic loop that runs on plain files. Use when choosing where to apply agentic workflow, defining or ingesting a definition of workflow (steps, graph, exit evidence, delegate model per step, run model per step, measures), scaffolding it as markdown, orchestrating it agentically one move per cycle, integrating it with GitHub or a Kanban board, or inspecting and adapting the loop itself. Entry point and operating loop for the flow-driven-* skill family; for portfolio-level investment management use portfolio-pdlc instead.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow-Driven — Agentic Loop Engineering

## Outcome

A value stream runs as an engineered loop on plain files: the workflow is defined rather
than assumed, every step declares what you can rely on when work leaves it, every step has
an explicit delegate model and run model, work advances one move per cycle on evidence, the
measures that matter ride inside the workflow rather than beside it — and a meta-loop
inspects and adapts the loop itself. Agents do the work the contracts allow; humans keep the
decisions that are actually theirs.

## Outcome Indicators

- Every step has exit evidence a stranger could check, a delegate rung with a reason, and a
  run contract with a stop rule.
- Evidence coverage at evidence exits stays at 100%: nothing leaves a checked step on assertion.
- Each cycle ends with exactly one move executed, a regenerated board, and a loop-log line.
- Human minutes per item trend down while escape rate does not move.
- The improvement lane holds live bets on the workflow itself, each with kill criteria.

## The Mental Model

**An agentic workflow is a flow system with two nested loops.** The outer loop moves items
through a graph of steps; the inner loop is how one step gets done. Both need a trigger, a
bounded move, an evidence-based exit, and a recorded trace. Most agentic harnesses specify
only the move, which is why they produce confident output and no visible flow.

Three commitments follow, and everything in this family is downstream of them:

1. **Flow-driven, not task-driven.** Steer on where items sit and how long they have sat,
   with pull policies and WIP limits — not on a to-do list.
2. **Evidence over status.** A step is finished when its evidence exists. Agents are fluent,
   and fluency reads as completion; exit evidence is the countermeasure.
3. **Delegation is per step and per evidence.** The rung is set by reversibility, blast
   radius, and check quality — never by how impressive the model looks this month.

The name is the first commitment, said out loud: **flow-driven**, not task-driven.

And one decision precedes all three: **what is the unit of value that flows?** Named as an
outcome, not an artefact or a task — because the steps are what happens to one, the limits
count them, and every measure inherits whatever confusion is in the unit.

Full argument: `skills/flow-driven/references/loop-engineering.md`.

## The Workspace

Any folder becomes a flow workspace when it follows
`skills/flow-driven/references/workflow-definition.md`:

```
workflow.md        definition of workflow: the unit of value + <!-- flow-config --> graph
steps/<id>.md      one contract per step: exit evidence, delegate, run, inner graph
items/<slug>/      the work, one card per item; frontmatter is the state
measures.md        what we steer on            integrations.md   system-of-record bindings
platform/          context packs, checks, prompts — the leverage that compounds
improvements/      bets on the workflow itself learnings/        one learning per file
board.md           GENERATED — never hand-edit flow-log.csv      GENERATED transitions
```

```bash
python3 <REPO>/skills/flow-driven/scripts/flow_lint.py  <ws>   # contract violations
python3 <REPO>/skills/flow-driven/scripts/flow_board.py <ws>   # regenerate the projection
python3 <REPO>/skills/flow-driven/scripts/flow_next.py  <ws>   # the run card for ONE move
```

No workspace yet? Load `flow-driven-choose` (which stream?) then `flow-driven-define`,
which discovers the workflow by interview, derives one from first principles when none
exists, or adapts an existing artefact. Existing spec-kit / Kiro / bespoke harness /
tracker? Load `flow-driven-ingest` first.

## The Run Loop (one cycle)

1. **Validate.** `flow_lint.py`. GATE: never steer with a broken definition of workflow —
   if it reports violations, fixing them IS this cycle's move.
2. **Project.** `flow_board.py`. The board is derived; never steer from memory.
3. **Select ONE move.** `flow_next.py` applies the leverage table below and prints the run
   card. One cycle, one move. Resist fan-out.
4. **Run the step** under its contract: context packs, tools, guardrails, budget, stop rule.
5. **Verify** against the step's exit evidence, using something other than what did the work.
6. **Record.** Update item frontmatter (`step`, `step_entered`, `holder`,
   `evidence_exits_met`, the Exit evidence log), re-run the board, append one line to
   `reviews/loop-log.md`, and capture at most one learning.

### Leverage table — how the one move gets picked

First matching rule wins; inside a rule, most downstream item first, then oldest.

| # | Signal | The move | Skill |
|---|---|---|---|
| 1 | A human decision is past its date | Surface it; stop piling work behind it | `flow-driven-run` (decision-brief mode) |
| 2 | Lint violations: broken graph, missing contract, unevidenced exit | Fix the definition | `flow-driven-define` / `flow-driven-scaffold` |
| 3 | An item is blocked | Clear it or escalate it to a named human with a date | `flow-driven-run` |
| 4 | An item left an evidence exit with no evidence recorded | Verify and record, or send it back | `flow-driven-run` |
| 5 | An item's exit evidence is recorded and it can move | Pull it downstream | `flow-driven-run` |
| 6 | A step is over its WIP limit | Finish, do not start | `flow-driven-run` |
| 7 | An item is aging past its step threshold | Run its step contract | `flow-driven-run` |
| 8 | Items in flow, nothing pressing | Run the most downstream unrun step | `flow-driven-run` |
| 9 | Intake is starved | Pull one new item, or report that demand dried up | `flow-driven-run` |
| 10 | Board clean and flowing | Inspect and adapt the loop | `flow-driven-evolve` |

The ordering is the system's belief: waiting decisions starve everything downstream; a
broken definition lies to every later cycle; blocked work never fixes itself; finishing
outranks starting; and only a clean board earns the luxury of self-improvement.

## The Human Decision Boundary

Agents **prepare** decisions; they never make them. What stays human: entering a decision
point, changing the definition of workflow, promoting or demoting a delegate rung, changing
WIP limits or classes of service, killing an item, and anything irreversible or
reputational. The agent's deliverable at each is a brief — what you can rely on, what is
still open, evidence vs opinion, options with trade-offs, a recommendation — plus the item's
`next_decision` set with a date and a name.

## Routing

| Situation | Load |
|---|---|
| "Which of our workflows should be agentic?" | `flow-driven-choose` |
| A workflow exists but nobody has written it down — interview it out | `flow-driven-define` (Discover) |
| Nobody has worked this way before / "why work this way at all?" | `flow-driven-define` (Derive) |
| "What actually flows here?" — the unit of value is fuzzy or artefact-shaped | `flow-driven-define` (move 2) |
| A spec-kit, Kiro, bespoke harness, or tracker already exists | `flow-driven-ingest` |
| Turn the definition into a working workspace with stubs | `flow-driven-scaffold` |
| "What should we measure, and where does it live?" | `flow-driven-instrument` |
| "Run it where we already work — GitHub, Jira, a dashboard" | `flow-driven-integrate` |
| Advance the flow; run a cycle; prepare a decision | `flow-driven-run` |
| "Is the loop itself any good?" / cadence review | `flow-driven-evolve` |
| Portfolio of investments rather than a single stream | `portfolio-pdlc` (in this repo) |
| Deep diagnostic of one initiative | `sniff-test` (in this repo) |

## Cross-Harness Rules

- Plain markdown plus `python3` stdlib. No runtime, no daemon, no network in the scripts —
  the harness pushes to external systems using whatever tools it has, which is what keeps
  this portable across Claude Code, Codex, Gemini CLI, and anything else that reads files.
- Headless / loop mode: no blocking questions. When a cycle hits a human decision, write the
  brief, set `next_decision`, log it, and end reporting `DECISION-PENDING <slug>` (that is
  also `flow_next.py`'s exit code 4). Otherwise end reporting `CYCLE-COMPLETE <rule> <slug>`.
- Never advance an item into a decision-point step without a dated Decision-log entry naming
  a human.
- Never edit `workflow.md` or a step contract in passing. Changes are bets in
  `improvements/`, adopted with a decision and a change-log line.

## Quality Gates

- Lint clean (or the cycle's move was fixing it), board regenerated before and after.
- Exactly one move executed; everything else discovered went to `improvements/` or the loop log.
- The step's exit evidence exists and was verified by something other than its runner.
- Any decision-boundary transition has a dated human decision recorded.
- At most one learning captured, and only if it changes how the next cycle behaves.

## References

- `skills/flow-driven/references/loop-engineering.md` — the POV: two loops, ten principles, failure modes.
- `skills/flow-driven/references/workflow-definition.md` — the contract: layout, flow-config, step/item schema.
- `skills/flow-driven/references/step-contracts.md` — delegation ladder and run models.
- `skills/flow-driven/references/discovery-interview.md` — surfacing an unwritten workflow by
  interview, and matching it to an archetype.
- `skills/flow-driven/references/first-principles.md` — why work this way, when nothing exists.
- `skills/flow-driven/references/unit-of-value.md` — choosing and sizing what flows.
- `skills/flow-driven/references/workflow-archetypes.md` · `value-streams.md` · `measurement.md` ·
  `integration-adapters.md` · `scaled-flow-patterns.md` · `ingest-recipes.md` · `evolution-path.md` ·
  `loop-probes.md`
- `skills/flow-driven/templates/` — workflow, step, item, measures, integrations, context pack, improvement, AGENTS.
- `skills/flow-driven/example/fiy-content-engine/` — a worked instance with seeded smells.
