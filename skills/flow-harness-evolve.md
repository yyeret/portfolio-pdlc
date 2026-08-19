---
name: flow-harness-evolve
description: Run the meta-loop — inspect and adapt the workflow itself. Probe the flow (constraint drift, rework hotspots, WIP theatre, decision starvation), the evidence (watermelon steps, checks that always pass, self-graded work), the delegation (rung mismatches, escalation droughts, context rot, platform stall), and the definition of workflow (policy contradictions, silent drift, measures nobody steers with) — then capture improvement bets with benefit hypotheses and kill criteria instead of changing anything on the spot. Use on the meta-loop cadence, after recurring findings, or when the board is clean enough to earn self-improvement. Loop 2 of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Evolve

## Outcome

The workflow gets treated as a product: probes run against real workspace data, each fired
probe becomes either an improvement card with a benefit hypothesis and kill criteria or an
explicit "checked, quiet" line — and **nothing changes on the spot**. The improvement lane is
where leverage accumulates; edits made in passing are how operating models rot.

## Focus argument

- `focus:flow` — Family A: constraint, rework, WIP, decisions, intake
- `focus:evidence` — Family B: watermelons, weak checks, self-graded steps
- `focus:delegation` — Family C: rungs, escalations, context packs, the platform
- `focus:definition` — Family D: policy contradictions, drift, measures nobody uses
- `focus:auto` (default) — read the board, flow log, and loop log, and run the 3–5 probes the
  data is already pointing at

## Workflow

1. **Load the probe library**: `skills/flow-harness/references/loop-probes.md`.
2. **Gather data first.** `board.md`, `flow-log.csv`, `reviews/loop-log.md`, `learnings/`,
   the items' `## Escalations` sections, `measures.md` baselines, the improvement lane, and
   the context packs' review dates. Probes read data; they do not free-associate.
3. **Run 3–5 probes.** For each: signal present? Cite the rows, items, or dates. No signal?
   One "checked, quiet" line. Three similar learnings count as a signal. A pass that fires
   nine probes produces a report nobody acts on.
4. **Read the delegation ladder deliberately**, every pass: which steps earned a promotion
   (check agreement met, escapes zero, demotion criteria written), which are running above
   their evidence, and which are promoted on paper but not in the habit — a human holding
   items in a rung-4 step is a leverage leak the board already flags.
5. **Read the platform.** Recurring escalations name the missing context pack. Packs past
   their review date, or contradicted by a `learn` result, are manufacturing confident
   wrongness upstream. `questions-to-human` flat over months means answers are landing in
   chat instead of in packs.
6. **Capture bets, not fixes.** Each fired probe worth acting on becomes
   `improvements/<slug>/improvement.md`: benefit hypothesis with a mechanism, the measures it
   claims to move, a baseline, kill criteria written *now*, and the cheapest discovery — a
   data probe, a shadow run, a one-item pilot, a replay of the flow log under a different
   limit. Delegation bets must include the shadow-run design and the demotion trigger.
7. **Right-size the ceremony.** A policy tweak needs a line and a decision. A rung promotion
   needs a shadow run. A change to the graph or to classes of service needs the option table
   with "do nothing" as a real row — most workflow changes lose to it.
8. **Report.** `reviews/YYYY-MM-DD-meta-loop.md`: probes run, fired vs quiet with citations,
   cards created, and which existing bets this evidence strengthens or kills.

## Adoption (a separate act)

When a bet's discovery says proceed and a human decides:

1. Record the decision on the improvement card, dated and named.
2. Make the change — `workflow.md`, a step contract, a limit, a policy, a pack.
3. Add a dated line to the **Change log** in `workflow.md` pointing at the bet.
4. Fill the card's **Watch** table for at least n items. A change nobody watched cannot be
   reverted with confidence, and a bet that reaches `adopted` with an empty Watch table is
   itself a finding.

## Rules

- **Capture, never implement.** Changes to the definition of workflow happen only when a
  card passes with a human decision. Walk the talk: the workflow rides its own lifecycle.
- **Every bet gets kill criteria at birth.** A change we cannot falsify or revert is a
  mandate — say which it is and who mandated it.
- **Probes cite data or stay silent.** "The team should consider…" without a signal is
  consulting prose; delete it.
- **Respect improvement WIP.** If the lane already holds more open bets than the team
  digests, strengthen or kill existing ones before minting new cards.
- **Shrinking the harness is a legitimate bet.** If cycles keep firing the low-priority rules
  and nothing ages, propose removing machinery — nobody proposes it unless it is allowed.
- Simulation, replay, and shadow runs are discovery evidence, never a substitute for the
  human decision to adopt.

## Quality Gates

- Every probe run is accounted for: fired-with-citation or checked-quiet.
- Every new card has a benefit hypothesis with a mechanism, a baseline, kill criteria, and a
  named, timeboxed discovery.
- Delegation bets include a shadow-run design and a demotion trigger.
- Graph and policy bets include the option table with "do nothing" as a row.
- Zero direct edits to `workflow.md` or step contracts in this invocation.

## References

- `skills/flow-harness/references/loop-probes.md` — the four probe families.
- `skills/flow-harness/references/evolution-path.md` — stages, human roles, the platform play.
- `skills/flow-harness/references/measurement.md` — reading the numbers honestly.
- `skills/flow-harness/templates/improvement.md` — the bet card.
