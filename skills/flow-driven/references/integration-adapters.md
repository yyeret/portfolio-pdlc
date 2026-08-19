# Integration Adapters — putting the flow where people already look

The workspace is plain files. Most organisations steer from somewhere else: GitHub, Jira,
Linear, a Notion board, an internal dashboard, a Slack channel. Both can be true, as long as
one rule holds: **exactly one writer per field.**

## Pick a mode first

| Mode | State lives in | Good when | The cost |
|---|---|---|---|
| **files-only** | the workspace | small stream, agent-native team, or you are starting | leadership has to come and look |
| **mirror** | the workspace; tracker is a read-only projection | people need the view they already use | the tracker looks editable and is not — say so loudly |
| **adopt** | the tracker; the workspace projects it in and owns evidence | the org genuinely lives in the tracker | you inherit the tracker's model of your workflow |
| **split** | tracker owns state + assignment; files own artefacts, evidence, decisions | mixed reality at scale | two systems to keep honest — needs the field map most |

Write the mode in `integrations.md`, with the reason. A mode chosen by accident becomes a
sync bug six weeks later.

## The field map

Every mirrored field gets a row and exactly one owner. The linter fails on two owners for
one field, because that is a design error rather than a sync problem.

```
<!-- integration-map
mode: mirror
system: github-projects
field: step -> Project single-select "Stage" (owner: workspace)
field: owner -> Issue assignee (owner: workspace)
field: discussion -> Issue comments (owner: github)
-->
```

Human commentary in the other system is *conversation*, never state. If a comment contains a
decision, a human copies it into the item's Decision log — the copy is the record, and the
sync never reads it back. This one rule prevents most of the pain.

## How the sync actually runs

The scripts never touch the network. `flow_board.py --export json` writes a neutral payload;
the agent or a CI job pushes it using whatever tools the harness has (MCP connector, CLI,
API). That keeps flow-driven portable and keeps credentials out of the framework.

```bash
python3 <REPO>/skills/flow-driven/scripts/flow_board.py . --export json
# → exports/flow-export.json
```

Payload shape: `workflow` (id, kind, steps, terminal, generated), `wip` and `wip_limits`,
`evidence_coverage`, and `items` (slug, title, step, step_entered, age, owner, holder, rung,
class, kind, parent, blocked_by, next_decision, flags).

## Adapter recipes

### GitHub Issues + Projects (the common case)

| Workspace | GitHub |
|---|---|
| item | an Issue, one per item; the slug in the body as `flow-slug: <slug>` for idempotent matching |
| step | a Project **single-select field** ("Stage"), not a label — labels sort badly and lie about ordering |
| holder | label `held:human` / `held:agent` / `held:blocked` |
| next_decision | label `decision-due` + a comment naming the human and the date |
| exit evidence | a comment per exit, or a link to the artefact |
| flags | label `flag:aging`, `flag:over-wip` — cheap, and they make the tracker's filters useful |

Idempotence: match on `flow-slug` in the body, never on title. Titles change; slugs do not.
Create missing issues, update changed fields, and **never close an issue from a sync** —
closing is a human act with meaning attached.

### GitHub as the work surface (development streams)

For a development stream, artefacts already live in GitHub: a PR is `build`'s output, CI is
`verify`'s independent check, a review is a human exit. Bind those directly — `run: tool`
with `run_ref: gh-actions`, `verify_with: the CI workflow` — and let the item carry the
evidence pointers. Do not re-implement code review in markdown.

### Jira / Linear / a Kanban tool

Map steps to workflow states one-to-one, or do not map them at all. A partial mapping
("three of our steps are all `In Progress`") produces a board that cannot answer where work
waits, which was the entire point.

If the tracker's states cannot express your graph, that is a finding: either the tracker is
wrong for this stream, or your graph has steps the organisation does not believe in. Both
are worth a meta-loop conversation before writing any sync code.

### Internal dashboard / spreadsheet

Point it at `exports/flow-export.json` or `--export csv`. Refresh on a schedule; never write
back. A dashboard that writes state is a second source of truth wearing a chart.

### Chat (Slack/Teams)

Not a system of record. Excellent for two things: the `DECISION-PENDING` notification with a
named human, and the daily loop-log line. Both are pushes, both are one-way, and both should
link back to the item rather than restating it.

## Sync contract (same five rules, whatever the system)

1. **Idempotent** — running twice changes nothing the second time.
2. **Projection, not conversation** — the push writes; it does not pull state back.
3. **The declared owner wins** conflicts, and the loss gets logged.
4. **Failure is loud** — partial syncs leave a log line and a board flag; never half-write.
5. **Traceable** — every pushed change names the cycle that caused it.

## When to bother

Not on day one. Run files-only until the loop is real — a sync built around a workflow you
are still arguing about is rework with credentials attached. Add the mirror when someone
outside the loop starts asking where things are, which is the actual signal that it is
worth building.
