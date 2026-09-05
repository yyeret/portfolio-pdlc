---
name: flow-driven-integrate
description: Bind a flow workspace to wherever the work is actually managed — GitHub Issues and Projects, Jira, Linear, an internal Kanban dashboard, a spreadsheet, or chat — by choosing a system-of-record mode (files-only, mirror, adopt, split), writing a field-ownership map with exactly one writer per field, and using the board export plus the harness's own tools to sync. Use when leadership needs the flow where they already look, when a tracker already holds the work, or when a sync has started fighting the workspace. Part of the flow-driven family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow-Driven — Integrate

## Outcome

`integrations.md` declares the mode, the field map, and the sync contract; the projection
runs idempotently; and everyone can say which system owns which field without a meeting.
Where the flow is *managed* becomes a decision rather than an accident.

## Workflow

1. **Ask who needs to see it and to do what.** A sponsor who wants to know what is coming
   needs a projection. A team that lives in a tracker needs their tracker to be authoritative
   for state. Those are different modes, and getting this wrong is what produces the
   two-sources-of-truth mess later.
2. **Choose the mode** — `files-only`, `mirror`, `adopt`, or `split` — and write the reason
   in `integrations.md`. A mode chosen by accident becomes a sync bug six weeks later.
3. **Write the field map.** Every mirrored field, one owner. Human commentary in the other
   system is conversation, never state — if a comment contains a decision, a human copies it
   into the item's Decision log and the sync never reads it back. `flow_lint.py` fails on two
   owners for one field.
4. **Pick the matching key.** A stable slug in the issue body (`flow-slug: <slug>`), never
   the title. Titles change; slugs do not, and title-matching is why syncs create duplicates.
5. **Map steps properly or not at all.** One step to one tracker state. A partial mapping —
   three steps collapsed into "In Progress" — produces a board that cannot answer where work
   waits, which was the point of having one.
6. **Export and push.** `flow_board.py --export json` writes a neutral payload; the agent or
   a CI job pushes it with the harness's own tools (MCP connectors, CLI, API). The scripts
   never touch the network, which is what keeps the framework portable and credential-free.
7. **Prove idempotence** before scheduling anything: run the sync twice against an unchanged
   board and confirm the second run changes nothing.
8. **Log every sync** in `integrations.md`: date, direction, what moved, conflicts, cycle.
9. **Wire the two notifications worth having**: `DECISION-PENDING` with the named human, and
   the daily loop-log line. Both one-way, both linking back to the item rather than restating it.

## Rules

- **Exactly one writer per field.** Two writers is a design error, not a sync problem.
- **Never close, delete, or reassign in the other system from a sync.** Those acts carry
  meaning; a projection has no business performing them.
- **Failure is loud.** A sync that cannot complete leaves a log line and a board flag; it
  never half-writes and then reports success.
- **Do not integrate on day one.** Run files-only until the loop is real — a sync built
  around a workflow still being argued about is rework with credentials attached.
- If the tracker cannot express the graph, raise it as a finding rather than degrading the
  graph to fit. Either the tracker is wrong for this stream, or the graph contains steps the
  organisation does not believe in.
- Dashboards read the export; they never write state.

## Quality Gates

- Mode declared with a reason; `integration-map` block present and lint-clean.
- Every mirrored field has exactly one owner and a direction.
- Idempotence demonstrated, not assumed.
- The matching key is a stable slug.
- Sync log started, with the first run recorded.

## References

- `skills/flow-driven/references/integration-adapters.md` — modes, the GitHub/Jira/dashboard
  recipes, the export payload, the five sync rules.
- `skills/flow-driven/templates/integrations.md` — the file this produces.
- `skills/flow-driven/example/fiy-content-engine/integrations.md` — a filled-in mirror-mode example.
