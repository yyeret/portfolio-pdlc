# Scaled Flow Patterns — trees, zoom levels, and many streams

One board works until it does not. These are the patterns for when a stream outgrows a
single flat list — and the discipline that keeps them from becoming a hierarchy of lies.

The governing rule: **a viewing choice must never change a physical fact.** Collapsing a
rollup hides rows; it does not reduce WIP. Any pattern here that makes work look smaller
than it is has been implemented wrong.

## 1. Expand / collapse (the rollup)

An item with `kind: rollup` and `children:` is a container: a series, an epic, a programme.

- **A rollup sits where its least-advanced child sits.** Flow is only as done as its
  laggard. Any other rule (furthest child, average) lets a board flatter itself.
- **Children count toward WIP**, always, whether displayed or not.
- **Collapsed by default**, with the child distribution shown inline
  (`intake: 1, draft: 1`) — the shape of the work without the rows.
- `flow_board.py --expand <slug>` (or `--expand all`) when you need the detail.
- **Never expand more than one level in a steering conversation.** If a conversation needs
  two levels at once, it is really two conversations.

Rollups exist so leadership can see "the series" while the loop works "the parts". They are
not a scheduling mechanism, and they carry the *outcome hypothesis* — the parts carry the
work.

## 2. Zoom levels

| Level | Unit | Board | Who steers | Cadence |
|---|---|---|---|---|
| Portfolio | investments | `portfolio-pdlc` | sponsors | monthly/quarterly |
| Stream | items | flow-driven | the stream's owner | daily/weekly |
| Item | steps | the item card | whoever holds it | per cycle |
| Step | inner-graph nodes | nothing — private to the step | the runner | per run |

Each level has a different unit, a different cadence, and a different audience. The most
common scaling mistake is one board trying to serve two levels: a portfolio board with task
detail, or a stream board with initiative-sized items nobody can finish. When a board starts
serving two audiences, split it — do not add columns.

Inner-graph nodes deliberately have no board. The moment work *waits* on an inner node, it
is a step you have not admitted to yet: promote it.

## 3. Split and join

An item that fans out into parallel work and reconverges:

- Create children with `parent:` set and let each flow independently.
- **State the join condition on the parent**: all children terminal? a quorum? the slowest
  by a date? Write it in the rollup's `## Notes`. An unstated join condition becomes "when
  someone notices", which is how parallel work quietly serialises.
- The parent's position is derived, so the join is visible: the rollup does not advance
  until its laggard does.

## 4. Shared step (a step that serves many streams)

Legal review, a design system team, a security check, the one person who knows the payments
code. Two options:

- **Model it as a wait** (`type: wait`, `run: external`) in each stream. Honest, cheap,
  makes the queue visible immediately, and does not pretend you control it.
- **Give it its own stream** with its own board and pull policy, and let other streams' items
  reference it. Correct when the shared capability has enough demand to be steered.

Either way, the meta-loop should count how many streams name it. A step that appears in
three streams' waits is your constraint, and no amount of local optimisation elsewhere will
move it.

## 5. Replicated flows (same workflow, many teams)

Keep **one definition of workflow** in a shared location; each team gets its own workspace
with its own items, WIP limits, and rungs. Divergence is fine and expected — but divergence
should be a recorded bet in that team's `improvements/`, not a quiet local edit.

What to compare across replicas: cycle time by step, rework rate, and delegate mix. Where
one team's rung is two higher than another's on the same step, the interesting question is
what they built that the others did not — usually a context pack or a check. That is how a
platform spreads: by evidence, not by mandate.

## 6. Stream of streams

A `portfolio-pdlc` initiative is an outer item; its delivery runs as an inner flow-driven
stream. Link them by slug in both directions and let each keep its own cadence. Do **not**
try to make the portfolio board show step-level state — that is the two-audiences mistake
again. The right coupling is thin: the initiative card carries the stream id and the
headline (WIP, oldest item, next decision); the stream carries the work.

## 7. Collapse to promise

At the boundary between an internal stream and its consumers, publish the *promise*, not the
internals: "items of this class typically finish in 9–14 days (85th percentile)". Consumers
should not steer on your steps, and you should not owe them a step-level view — that is what
turns an internal workflow into a compliance surface.

The promise comes from your own flow log, expressed as a range with a percentile. Never a
single number: a single number is a commitment nobody made.

## Anti-patterns

- **Hierarchy as status.** Rollups created so a leader has something to look at, with no
  join condition and no hypothesis.
- **Collapsing to hide WIP.** If the board looks calmer after collapsing, the implementation
  is lying.
- **Deep trees.** Beyond two levels, nobody can hold it. Three levels means the middle one
  is probably a department.
- **Splitting a step into a sub-board** because it feels big. Steps have inner graphs, not
  boards. If it needs a board, it is a stream.
- **One board for every team** at the wrong altitude: a portfolio board with 200 items is a
  spreadsheet, and a stream board with 4 items a quarter is a status doc.
