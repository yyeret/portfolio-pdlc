# System of Record & Integrations — FIY Content Engine

## Mode

**Our mode**: `mirror` — this workspace owns the flow state; the team's GitHub Project gets
a read-only projection so Mary and the wider team can see the pipeline where they already
look. Nobody edits the Project board expecting it to stick.

## Field ownership

| Field | Where it appears elsewhere | Owner | Sync direction |
|---|---|---|---|
| step | GitHub Project single-select "Stage" | workspace | push |
| title | Issue title | workspace | push |
| owner | Issue assignee | workspace | push |
| holder | Issue label `held:<holder>` | workspace | push |
| next_decision | Issue label `decision-due` + comment | workspace | push |
| evidence | Comment thread on the issue | workspace | push |
| discussion | Issue comments from humans | github | read-only, never pulled into state |

Human comments on the GitHub issue are conversation, not state. If a comment contains a
decision, a human copies it into the item's Decision log — the copy is the record, and the
sync never reads it back.

## Sync contract

1. **Idempotent** — re-running changes nothing the second time.
2. **Projection, not conversation** — the push writes; it never pulls flow state back.
3. **Conflict resolution** — the workspace wins on every field it owns; the loss is logged.
4. **Failure is loud** — a partial sync leaves a line below and a flag on the board.
5. **Traceable** — each pushed change names the loop cycle that caused it.

## How the sync runs

```bash
python3 <REPO>/skills/flow-driven/scripts/flow_board.py . --export json
```

Then the agent pushes `exports/flow-export.json` with whatever GitHub tooling the harness
has, following the adapter recipe in
`<REPO>/skills/flow-driven/references/integration-adapters.md`. The scripts never touch
the network — that stays the harness's job, which is what keeps this portable.

## Sync log

| Date | Direction | What moved | Conflicts | Cycle |
|---|---|---|---|---|
| 2026-08-18 | push | 9 items, 3 stage changes | none | 2026-08-18 loop |

<!-- integration-map
mode: mirror
system: github-projects
field: step -> Project single-select "Stage" (owner: workspace)
field: title -> Issue title (owner: workspace)
field: owner -> Issue assignee (owner: workspace)
field: holder -> Issue label held:<holder> (owner: workspace)
field: next_decision -> Issue label decision-due (owner: workspace)
field: evidence -> Issue comment thread (owner: workspace)
field: discussion -> Issue comments (owner: github)
-->
