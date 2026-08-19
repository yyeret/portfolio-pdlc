# The Evolutionary Path — how adoption grows and what happens to the humans

Nobody arrives at an agent-run workflow. They arrive at a visible one, then a
context-supported one, then a partly delegated one — and the human role changes at each
stage, in a direction most people find better once they are in it and threatening before
they are.

Two claims worth stating up front:

- **Every stage is a legitimate resting place.** A stream that stops at stage 2 with an
  honest board and one good context pack is in far better shape than one that jumped to
  stage 4 with unverified exits.
- **The path is per step, not per organisation.** A stream can be at stage 4 on three steps
  and stage 0 on the one that requires a person's name.

## The six stages

### Stage 0 — Make the flow explicit

The definition of workflow, the board, exit evidence written down. Humans do everything.

- **The move**: define, then run cycles by hand for a fortnight.
- **What changes**: people see their own flow for the first time. The constraint is almost
  never where they said it was.
- **Human role**: unchanged, plus one new one — a **flow steward** who runs the loop and
  keeps the board honest.
- **Ready for the next stage when**: the board matches reality without anyone tidying it.

### Stage 1 — Agents assemble context

Rung 1 on the steps where people re-derive the same context every time.

- **The move**: one context pack, one step, one week.
- **What changes**: the same work gets done with less setup. Nothing is delegated, so
  nothing is threatening — which is why this is the right beachhead.
- **Human role**: unchanged in authority; the prep disappears.
- **Ready when**: people start asking for a pack for another step.

### Stage 2 — Agents draft inside steps

Rung 2 where the exit evidence is clearest.

- **The move**: the agent produces, the human is editor of record.
- **What changes**: throughput rises before quality does. Watch rework, not volume.
- **Human role**: **doer → editor**. This is the stage people find hardest, because editing
  someone else's draft feels less like craft than writing your own. It gets easier when the
  drafts get better, and the drafts get better when the context packs do.
- **Ready when**: check agreement with the editor's findings is high on several items.

### Stage 3 — Agents run whole steps to a verified exit

Rung 3–4, starting with the most reversible step.

- **The move**: build the check *first*, then promote. Shadow-run before you switch.
- **What changes**: the loop starts to move without a human in every beat. Escalations
  become the main human interface — and their content tells you what to build next.
- **Human role**: **editor → verifier and exception handler**. Attention moves from
  every item to the ones that stopped.
- **Ready when**: escapes stay at zero across a meaningful number of items *and* the
  demotion criteria are written down.

### Stage 4 — The loop runs itself between decisions

Orchestration: the selector picks the move, agents run steps, work parks at decision points.

- **The move**: run the loop on a cadence; humans meet the board at decisions.
- **What changes**: decision latency becomes the dominant cycle-time component — the loop
  is now fast enough that the waiting is on people. That is a good problem and a real one.
- **Human role**: **verifier → decision-maker and steward of the workflow**. The job is
  deciding, and keeping the definition of workflow true.
- **Ready when**: the meta-loop is running and improvement bets are being made and killed
  on evidence.

### Stage 5 — The platform is the product

Context packs, checks, evals, adapters, and shared steps become the thing the team actually
builds. Steps get promoted because the platform made them safe.

- **The move**: treat `platform/` as a product with an owner, a backlog, and a review cadence.
- **What changes**: adding a new stream gets cheap, because most of what a new stream needs
  already exists.
- **Human role**: **steward → designer**. Curating context, designing checks, setting
  policy, owning taste and decision rights.
- **Ready when**: someone asks to reuse your packs and checks for a different stream.

## What never delegates

Not because agents cannot, but because delegating them breaks something:

- **Decision rights over irreversible or expensive moves.** Someone's name has to be on it.
- **Accountability.** It does not distribute; it stays with a person.
- **Relationships and trust.** The reply to a probe is the point of the probe.
- **Taste about the organisation's own voice and standards.** Delegate the application, never
  the definition.
- **Choosing what the flow is for.** The purpose is a human commitment, and every measure
  below it inherits its legitimacy.

Say these out loud in the workflow's delegation stance, so nobody treats them as a backlog
of steps waiting for a better model.

## The platform play, concretely

**Every question an agent has to ask a human is a missing context artifact.** That is the
entire mechanism, and it is why `questions-to-human` is the headline platform measure.

The loop:

1. An agent escalates or asks.
2. A human answers.
3. The answer goes into `platform/context/<pack>.md` with provenance and a rot signal —
   not into a chat log.
4. The next run does not need the human.
5. The escalation rate for that step falls; the step becomes promotable.

What belongs in the platform:

| Layer | What it is | Compounds because |
|---|---|---|
| **Context packs** | the knowledge steps run against | every step and every stream can use them |
| **Checks** | independent verification recipes | a check is what makes a promotion safe |
| **Run refs** | versioned prompts, scripts, skills | improvements land everywhere at once |
| **Adapters** | the bindings to where work lives | built once per system, not per stream |
| **Shared steps** | capabilities other streams pull on | the constraint gets managed instead of endured |

Two warnings. **Stale context is worse than missing context**: missing context makes an
agent ask; stale context makes it confident. Every pack carries provenance, a review date,
and the signal that would tell you it has rotted. And **a platform nobody uses is a
library**: the measure of a pack is that a step's escalations fell, not that it exists.

## Anti-patterns on the path

- **Jumping to stage 4** with unverified exits. Fast, confident, wrong.
- **Promoting on capability** rather than on check agreement.
- **Automating the human out of the step where the judgement was.** The tell: nobody can say
  what the step's judgement *was*.
- **Never demoting.** A ladder that only goes up is a ratchet, and ratchets break loudly.
- **Building the platform before the flow.** Context packs for steps nobody has defined are
  documentation with a folder name.
- **Telling people their role will "evolve" without saying into what.** Name the next role —
  editor, verifier, decision-maker, designer — and what it is worth.
