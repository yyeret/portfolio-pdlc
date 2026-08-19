# FIY Content Engine — Example Flow Workspace

A safe practice instance of the flow-driven workspace contract: FlowImpact Yoga's
studio-owner-facing content stream. Same fictional scale-up as the portfolio example
(`skills/portfolio-pdlc/example/fiy-portfolio/`), a different value stream — deliberately
**not** software delivery, to show that flow-driven is about flow, not about code.

Dates assume "today" ≈ **2026-08-19**. Pass `--today 2026-08-19` for reproducible flags.

```bash
python3 ../../scripts/flow_lint.py  . --today 2026-08-19   # 0 violations, 2 seeded warnings
python3 ../../scripts/flow_board.py . --today 2026-08-19   # regenerate board.md
python3 ../../scripts/flow_next.py  . --today 2026-08-19   # the run card for one move
```

## What this instance demonstrates

| Aspect | Where to look |
|---|---|
| A graph, not a chain | `workflow.md` flow-config: two branches, a back-edge, and a loop-closing edge |
| Step contracts | `steps/*.md` — intent, exit evidence, delegate rung, run model, escalation |
| A mini-graph inside a step | `steps/draft.md` `## Inner graph`, bounded with `max_iterations: 2` |
| The delegation ladder in one flow | rungs 1 → 4 across eight steps, each justified by reversibility |
| Evidence exits that are enforced | `evidence_exits` + `evidence_exits_met` + the linter |
| Expand / collapse for scale | `instructor-retention-series` is a rollup; `--expand all` |
| The context platform | `platform/context/*.md` — and `learn` feeding `audience-map` back |
| Independent verification | `platform/checks/*.md`, never the same artifact as the runner |
| The meta-loop | `improvements/` — one adopted bet, one probing, one proposed |
| Integration | `integrations.md` mirror mode + `--export json` |

## Deliberately seeded smells

Don't "fix" the seed data casually — the loops should find these.

| Where | Seeded smell |
|---|---|
| `studio-owner-churn-teardown` | Publish decision overdue since 08-14 with everything ready — the loop's rule 1 |
| `agentic-flow-primer` | Aging in `edit` at 11d against a 5d threshold; the human-heaviest step is the bottleneck |
| `draft` step | WIP 3 against a limit of 2 — because `retention-part-one` is real work even though the board collapses it |
| `webinar-agentic-portfolio` | Blocked 8 days on a human handoff, aging past `research` threshold, `derisk-first` |
| `voice-of-studio-owner-digest` | Dana hand-holding a rung-4 step — a promotion adopted on paper but not in the habit |
| `steps/learn.md` | Rung 3 with no independent check: the linter warns, and `improvements/verify-learn-readouts` carries the bet |
| `steps/angle-test.md` | Uses the measure `audience-signal`, which nobody declared in `measures.md` |
| `sales-objection-library` | A recorded `angle-test` skip that the fixed-date policy forbids — see `learnings/fixed-date-skips-the-probe.md` |
| flow-log | Real history: 6 finished items (3 with no card — they predate the workspace), 2 rework traversals out of `edit` |

## Exercises

1. **Run one cycle.** `flow_next.py` should route to the overdue publish decision and exit
   `DECISION-PENDING`. Write the decision brief; do not decide.
2. **Break an evidence exit.** Move `agentic-flow-primer` from `edit` to `publish` without
   adding `edit` to `evidence_exits_met`. Re-run the board, then the linter: the violation
   appears, and rule 2 jumps to second in `flow_next`'s queue — behind only the overdue
   decision, because a waiting human starves more work than a broken contract does. Undo it.
3. **Zoom.** `flow_board.py . --expand instructor-retention-series` — note that WIP does not
   change when the view does.
4. **Meta-loop.** Load `flow-driven-evolve` and probe the workflow: the rework rate out of
   `edit`, the human-minute concentration, the policy contradiction in
   `learnings/fixed-date-skips-the-probe.md`. Capture bets; change nothing.
5. **Delegation.** Argue the case for promoting `edit` to rung 3, then read
   `improvements/promote-draft-to-run/` — the probe is running and the evidence is not there
   yet. Practise not promoting.
