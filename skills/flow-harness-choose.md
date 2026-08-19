---
name: flow-harness-choose
description: Identify the value streams an organisation actually runs — operational (a request stream with someone waiting) and development (building something that did not exist) — and choose which one to make agentic first, with a scored, reversible recommendation. Use before defining any workflow, when an org asks "where should we apply AI/agents", when an agentic programme has produced demos but no change in outcomes, or when picking the next stream after the first one is running. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Choose

## Outcome

A named value stream, its boundaries, its owner, and a first move — chosen on evidence
rather than on which workflow was easiest to describe. Plus an honest note on the streams
you are *not* doing yet and why, so the choice reads as a decision instead of an oversight.

## Inputs

Whatever exists: an org chart (useful only as a map of handoffs), a tracker, a description
of "how work gets done here", and — most valuable — thirty minutes with two people who
actually do the work.

## Workflow

1. **Find the streams from outcomes, not from teams.** For each candidate: name an outcome
   someone *outside* the team notices, walk it backwards to its trigger, and list the
   handoffs. Stop when you hit something outside their control — that is the entry point.
   A stream you cannot name without listing departments is an org chart.
2. **Classify each**: operational (volume, someone waiting, evidence mostly exists) or
   development (variability, high knowledge content, evidence is created along the way).
   They fail differently: operational streams die of queueing, development streams die of
   undetected wrongness.
3. **Ask the four questions that find the real system**, per stream:
   - Where does work *wait*? (not where it is hard)
   - What do people re-derive every single time? (the highest-yield agentic target)
   - What gets discovered late? (a weak exit, upstream of where it hurts)
   - Who decides, and how long does deciding take?
4. **Score** each candidate on the seven dimensions in `value-streams.md` (volume, pain,
   repeated context, evidence availability, reversibility, human appetite, decision clarity).
   Treat reversibility and appetite as vetoes, not as addends.
5. **Recommend one stream and one first move.** Rank the move by yield per unit of risk:
   make it visible → assemble context → draft in a step → automate a check → run a step →
   orchestrate. Starting at "orchestrate" is the standard, expensive mistake.
6. **Write the choice brief** (`reviews/YYYY-MM-DD-stream-choice.md`): the streams found,
   the scores with reasoning, the recommendation, what the first month looks like, what you
   deliberately are not doing yet, and the one thing that would change the recommendation.

## Rules

- **One stream.** Two streams in parallel means neither gets a second cycle.
- Score with the humans in the room, not afterwards. The argument about a score is worth
  more than the score.
- A low reversibility score is not a reason to skip the stream — it is a reason to cap the
  ambition at visibility and evidence. Say that explicitly rather than quietly aiming lower.
- Never recommend a stream whose decision-maker cannot be named. The loop will park at its
  first decision and stay parked.
- If the honest answer is "this stream does not need a harness", say so. A stream with four
  items a quarter needs a conversation, not an operating system.

## Quality Gates

- Every candidate stream named by its outcome, with a start and an end boundary.
- Scores recorded with one line of reasoning each, not just numbers.
- One recommended stream, one first move, and both are reversible within a month.
- The streams not chosen are listed with the reason, so nobody has to re-litigate.

## References

- `skills/flow-harness/references/value-streams.md` — the identification method, the scoring
  table, the anti-patterns.
- `skills/flow-harness/references/workflow-archetypes.md` — what the chosen stream will
  probably look like.
- Next: `flow-harness-define` (or `flow-harness-ingest` if a workflow artefact already exists).
