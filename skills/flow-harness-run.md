---
name: flow-harness-run
description: Advance a flow workspace agentically — validate the definition, regenerate the board, take the single highest-leverage move from the deterministic run card (overdue decision, broken contract, blocked item, missing exit evidence, ready-to-pull, over-WIP, aging, or intake), run that step under its contract, verify the exit evidence with something independent, and record the transition. Use to run a cycle, work the flow on a cadence, drive an item to its next decision, or operate the loop headlessly. Loop 1 of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Run

## Outcome

One move executed well: the right item advanced through the right step under its contract,
its exit evidence produced and independently verified, its state recorded, and the next
decision made visible to the human who owns it. One cycle, one move — the power is in
repetition, not in scope.

## Modes

- `mode:pair` (default) — ask when the run card is ambiguous; a human is present.
- `mode:loop` — headless. No blocking questions. When a cycle reaches a human decision,
  write the brief, set `next_decision`, log it, and end reporting `DECISION-PENDING <slug>`.
- `mode:brief <slug>` — skip selection; prepare the decision brief for this item.

## Workflow

1. **Validate.** `flow_lint.py <ws>`. GATE: violations mean the definition of workflow is
   lying to you — fixing them is this cycle's move, and nothing else is.
2. **Project.** `flow_board.py <ws>` — regenerate before reading. Never steer from memory,
   a stale board, or a summary of a board.
3. **Get the run card.** `flow_next.py <ws>` prints the rule that fired, why, the item, the
   step's full run contract, the exit evidence to produce, the candidate next edges, and
   what to record. Exit code 4 means the top move is a human decision.
4. **Sanity-check the selection, do not shop for a better one.** The rule ordering encodes
   the system's beliefs. If the card is genuinely wrong, that is a finding for
   `flow-harness-evolve`, not a licence to pick your favourite item.
5. **Run the step under its contract.** Load the named context packs. Use only the tools the
   contract allows. Respect the budget and the stop rule; if there is an inner graph, follow
   it and honour `max_iterations`. When the escalation condition fires, **stop and escalate**
   — that is the contract being satisfied, not a failure.
6. **Verify.** Run `verify_with` in a context independent of the run, with a sceptic's brief.
   Record its findings — including "none, and here is what I examined". If the step declares
   no verification and sits at rung 3+, verify anyway and open an improvement card.
7. **Decide the edge.** More than one edge out of the step means a branch condition to
   evaluate against evidence; record which edge you took and why in the item's `## Notes`.
   Entering a decision point without a dated Decision-log entry is forbidden — prepare the
   brief instead and set `next_decision` with a date and a name.
8. **Record.** Update `step`, `step_entered`, `holder`, `evidence_exits_met`, and add a dated
   row to the item's `## Exit evidence log`. Re-run `flow_board.py` (it appends the
   transition). Append one line to `reviews/loop-log.md`. Capture at most one learning.
9. **Report.** `CYCLE-COMPLETE <rule> <slug>` or `DECISION-PENDING <slug>`, plus the one
   thing the next cycle should know.

## Decision-brief mode

When the move is a human decision, the deliverable is a brief on the item (or in `reviews/`):
**what you can rely on** (evidence, with its receipts) · **what is still open** (and what it
would cost to close) · **evidence vs opinion**, labelled · **options with trade-offs**,
including doing nothing · **a recommendation with its reasoning** · **who decides and by
when**. Then stop. Agents prepare decisions; they do not make them, and a brief that argues
one option without the alternatives is advocacy wearing a brief's clothes.

## Rules

- **One move.** Everything else discovered goes to `improvements/`, `learnings/`, or the
  loop log — never into this cycle's scope.
- **Never fabricate exit evidence.** If the evidence cannot be produced, the honest move is
  the back-edge or an escalation. A recorded "we could not" beats an invented "we did".
- **Never advance across a decision point** without a dated entry naming a human.
- **Never edit `workflow.md` or a step contract** during a run cycle, however obvious the fix.
- **Escalate rather than improvise** when the contract does not cover the situation. Then log
  the escalation — repeated escalations are the meta-loop's best input.
- Respect WIP limits: over-limit means finish something, not start something.
- If the item is blocked, the move is to clear or escalate the block — not to work around it
  by pulling something easier.

## Quality Gates

- Lint clean before the move (or the move was fixing it); board regenerated after.
- Exactly one move executed.
- Exit evidence exists, is recorded on the item, and was verified by something other than
  what produced it.
- Any decision-point entry has its dated human decision.
- Loop-log line appended; at most one learning captured.

## References

- `skills/flow-harness/references/loop-engineering.md` — the six beats and why the leverage
  table is ordered the way it is.
- `skills/flow-harness/references/step-contracts.md` — running a step, escalation, verification.
- `skills/flow-harness/references/workflow-definition.md` — what to record and where.
- `flow-harness-evolve` — where a wrong run card, a missing check, or a recurring escalation goes.
