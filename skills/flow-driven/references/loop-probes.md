# Loop Probes — the meta-loop's diagnostic library

Probes for `flow-driven-evolve`. Each names a signal in real workspace data, a reading, and
the cheapest way to find out more. A probe either **fires with a citation** or is recorded
**checked, quiet** — "the team should consider…" with no signal is consulting prose.

Run 3–5 probes per meta-loop pass, chosen by what the data is already pointing at. Every
fired probe that is worth acting on becomes an improvement card with a benefit hypothesis
and kill criteria. **Nothing gets changed on the spot.**

## Family A — flow

| # | Probe | Signal | Reading | Cheapest discovery |
|---|---|---|---|---|
| A1 | **Constraint drift** | the step with the longest median time in step, vs where the team says the bottleneck is | the constraint moved and the attention did not | recompute per month over the last 60 items |
| A2 | **Rework hotspot** | back-edge traversals concentrated on one step | the *upstream* step's exit evidence is too weak — fix the exit, not the reworker | read the last five back-edges and what triggered each |
| A3 | **WIP theatre** | limits declared, routinely exceeded, never enforced | limits nobody pulls against are decoration; either enforce or delete | replay the flow log under the declared limit |
| A4 | **Decision starvation** | items sitting at decision points past their date | the loop is fast enough that people are now the constraint | count decision-wait days as a share of cycle time |
| A5 | **Intake shaping** | arrival rate vs finish rate; entry-step age | the stream is filling faster than it drains, or starving | compare intake and terminal counts by month |
| A6 | **Blocked-by-human** | waiting share dominated by `blocked` on handoffs | the handoff, not the work, is the cost | list blocks by who they wait on |
| A7 | **Ghost step** | a step with no items and no transitions for a long stretch | it is aspiration, or it happens elsewhere without being recorded | ask two people what happens there |
| A8 | **Class-of-service inflation** | most items are `expedite` | the classes have stopped meaning anything | count by class over the last quarter |

## Family B — evidence and quality

| # | Probe | Signal | Reading | Cheapest discovery |
|---|---|---|---|---|
| B1 | **Watermelon step** | evidence coverage high, escape rate also high | evidence is being recorded, not produced | read the actual evidence on three "clean" items |
| B2 | **Evidence theatre** | exit evidence recorded but never read downstream | the exit is paperwork; either wire it into the next step or delete it | ask the next step what it reads |
| B3 | **Check that always passes** | a `verify_with` with zero findings across many items | it is calibrated to pass, or it is not running | seed a known defect and see if it catches it |
| B4 | **Self-graded step** | `verify_with` empty, or equal to `run_ref`, at rung 3+ | the runner grades its own work | the linter already flags it; ask why it persists |
| B5 | **Rubber-stamp step** | a human verify step whose cycle time is near zero | the check is a click | compare its findings rate to its history |
| B6 | **Late discovery** | defects found at the last step or after terminal | an earlier exit is missing | trace three escapes to the step that should have caught them |

## Family C — delegation and leverage

| # | Probe | Signal | Reading | Cheapest discovery |
|---|---|---|---|---|
| C1 | **Rung mismatch (too high)** | escapes or overrides concentrated on one high-rung step | promoted on capability, not on evidence | check whether demotion criteria were ever written |
| C2 | **Rung mismatch (too low)** | a human holding items in a rung-4 step | the promotion is on paper, not in the habit | ask what stopped them trusting it |
| C3 | **Human-touch concentration** | one person's minutes dominate the stream | the leverage question is entirely about that step | estimate minutes per step for ten items |
| C4 | **Escalation drought** | zero escalations at rung 3+ over many items | the agent is not noticing when it should stop | plant an ambiguous item and see if it asks |
| C5 | **Escalation loop** | the same escalation recurring | a missing context pack, precisely identified | read the last five and write the pack |
| C6 | **Cost drift** | cost per item rising without cycle-time or quality gains | inner loops are grinding | check inner-loop iteration counts against caps |
| C7 | **Context rot** | a pack past its review date, or a `learn` result contradicting it | confident wrongness is being manufactured upstream | diff the pack against the last three outcomes |
| C8 | **Platform stall** | questions-to-human flat over months | answers are landing in chat, not in packs | count how many packs changed last month |

## Family D — the definition of workflow itself

| # | Probe | Signal | Reading | Cheapest discovery |
|---|---|---|---|---|
| D1 | **Policy contradiction** | two policies that cannot both be followed, and a recorded exception | the definition drifted from practice | find every item that hit the contradiction |
| D2 | **Silent drift** | step files edited with no change-log line or bet | the workflow is changing by accident | diff the definition against three months ago |
| D3 | **Unused optionality** | an optional step never skipped, or never taken | it is mandatory, or dead — either way the graph lies | count the branch traversals |
| D4 | **Measure without steering** | a declared measure no bet or decision has ever cited | decoration | check which measures appear in improvement cards |
| D5 | **Bet graveyard** | improvement cards stuck at `proposed` | improvement WIP exceeds appetite; or the bets are too big | count open bets and their ages |
| D6 | **Adopted but unwatched** | an adopted bet with an empty Watch table | nobody can revert with confidence | fill in the measure now and see |
| D7 | **Exit-evidence inflation** | steps accumulating exit-evidence lines over time | ceremony creeping in one incident at a time | ask which line last caught something |

## Running a pass

1. **Gather the data first**: board, flow log, loop log, learnings, escalations across
   items, the improvement lane, the context packs' review dates. Probes read data.
2. **Pick 3–5** the data already points at. Do not run the whole library; a pass that fires
   nine probes produces a report nobody acts on.
3. **Cite or stay quiet.** Every fired probe names the rows, items, or dates behind it.
4. **Respect improvement WIP.** If the lane already holds more open bets than the team
   digests, strengthen or kill existing ones before minting new cards.
5. **Write the pass** to `reviews/YYYY-MM-DD-meta-loop.md`: probes run, fired vs quiet, cards
   created, bets strengthened or killed.

## The meta-meta question

Once a quarter, ask the loop about itself: **is the loop still worth running?** If cycles
keep firing rule 8 ("in flow, unrun") and nothing is aging, the stream may not need this
much machinery. Shrinking the machinery is a legitimate improvement bet — and one nobody
proposes unless it is explicitly allowed.
