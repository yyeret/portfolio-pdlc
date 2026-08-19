# System of Record & Integrations — <Stream Name>

Where the work actually lives, which system owns which field, and how the projection stays
honest. The rule that prevents every sync disaster: **exactly one writer per field.**

## Mode

<Pick one and say why.>

| Mode | Meaning | Choose when |
|---|---|---|
| files-only | this workspace is the whole system of record | small stream, agent-native team |
| mirror | workspace owns state; a tracker/dashboard gets a read-only projection | leadership needs a view they already use |
| adopt | the tracker owns flow state; the workspace projects it in and owns evidence | the org already lives in the tracker |
| split | tracker owns state and assignment; files own artifacts, evidence, and decisions | mixed reality, most common at scale |

**Our mode**: <mode> — because <reason>.

## Field ownership

Every mirrored field, and who writes it. Two writers is not a sync problem, it is a design
error — fix it here, not in the sync script.

| Field | Where it appears elsewhere | Owner | Sync direction |
|---|---|---|---|
| step | <Project board column / Jira status> | workspace | push |
| title | <Issue title> | workspace | push |
| owner | <Assignee> | <system> | pull |
| evidence | <PR body / comment> | workspace | push |
| decisions | <Issue comment> | workspace | push |

## Sync contract

1. **Idempotent.** Running the sync twice changes nothing the second time.
2. **Projection, not conversation.** The push writes; it never reads state back into the
   workspace except for fields the other system owns.
3. **Conflict resolution.** On disagreement, the declared owner wins and the loss is logged
   below. No silent merges.
4. **Failure is loud.** A sync that cannot complete leaves a line in the sync log and a
   flag on the board; it never half-writes.
5. **Human-readable trace.** Every pushed change names the loop cycle that caused it.

## How the sync runs

The board script writes a neutral export; the agent (or a CI job) pushes it with whatever
tools the harness has. The scripts themselves never touch the network.

```bash
python3 <REPO>/skills/flow-driven/scripts/flow_board.py . --export json
# → exports/flow-export.json, then the adapter recipe in
#   <REPO>/skills/flow-driven/references/integration-adapters.md
```

## Sync log

| Date | Direction | What moved | Conflicts | Cycle |
|---|---|---|---|---|

<!-- integration-map
mode: files-only
system: none
field: step -> workspace board.md (owner: workspace)
field: title -> workspace item.md (owner: workspace)
-->
