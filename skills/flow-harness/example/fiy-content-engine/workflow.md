# Definition of Workflow — FIY Content Engine

This is the workflow for FlowImpact Yoga's studio-owner-facing content: the stream that
turns what we learn from studio owners into published pieces that change what they believe
and do. It started from the `content` archetype and we own it from here.

It is a **common language and a set of pull policies, not a set of gates**. A piece moves
when the evidence for the next step exists and the next step has capacity.

## What this stream is for

- **Value delivered**: a studio owner understands something about running their business
  that they did not before, from us, and acts on it.
- **Customer / consumer**: owner-operators of 1–5 studio locations; secondarily the
  enterprise buyers our sales team meets.
- **Trigger**: a recurring question from the field (support, sales, community) or a
  learning from the product portfolio worth telling.
- **In this stream**: anything published under our name to an audience we do not control.
  **Not in this stream**: in-product copy, release notes, and customer-specific decks.

## Flow boundaries

- **Start**: when a candidate piece gets an item card — i.e. when someone commits to
  finding out whether it is worth writing, not when someone mentions an idea in Slack.
- **End**: when the piece has been published and read against its outcome hypothesis at
  the `learn` step. After that it belongs to the evergreen library, not to this board.

## Demand

| Class of service | What it is | Arrival rate | Pull policy |
|---|---|---|---|
| standard | the normal case | ~4/month | pull when the step has capacity, oldest first |
| expedite | a claim in the market we must answer this week | ~1/quarter | jumps the queue, costs a `draft` WIP slot, needs Mary's yes |
| fixed-date | tied to a launch or a conference | ~2/quarter | scheduled backwards from the date, `angle-test` never skipped |
| derisk-first | a new positioning claim we have not made before | ~1/quarter | must pass `angle-test` with a real audience probe before `draft` |

## Steps

| Step | Intent | What you can rely on when an item leaves | Rung | Run |
|---|---|---|---|---|
| intake | Decide whether this is worth finding out about | A card with a named source and an outcome hypothesis | 2 | prompt |
| research | Build the evidence base | A research pack: ≥3 sources, ≥1 primary, claims mapped to sources | 3 | prompt |
| angle-test *(optional)* | Test the angle on real humans before writing | A dated audience probe with a recorded response and a proceed/drop call | 1 | human |
| draft | Turn the evidenced angle into a piece in our voice | A draft whose every claim traces to the research pack | 2 | prompt |
| edit | Make it true, tight, and ours | Claims audited, voice findings resolved or waived with a reason | 1 | human |
| publish | Decide to publish, and publish | A URL, a date, a channel, and a named human's decision | 1 | human |
| amplify *(optional)* | Put it in front of the audience repeatedly | A scheduled distribution plan with per-channel variants | 4 | tool |
| learn | Read the result against the hypothesis | A dated readout: what the outcome hypothesis predicted vs what happened | 3 | prompt |

Full contracts are in `steps/<step-id>.md`.

## The graph

The happy path is a line, but two branches carry the actual learning. `research` can skip
`angle-test` when a prior piece already evidenced the angle — that skip is a decision,
recorded on the card. `angle-test` can send a piece to `dropped`, and a dropped piece with
a recorded probe is a *cheap win*, not a failure. The back-edge from `edit` to `draft` is
normal; the meta-loop watches how often it fires, because a rising rework rate out of
`edit` means the `draft` step's exit evidence is too weak, not that the writer got worse.

`learn -> intake` closes the loop: a readout that raises a new question spawns a **new**
item at intake. The finished piece goes to `shipped`.

## Policies

1. **Pull, don't push.** `draft` takes work when it has a slot, not when `research` is
   proud of a pack.
2. **Right-to-left.** Walk the board from `learn` backwards. A piece one step from
   published beats a piece one step from started.
3. **Evidence exits.** `research`, `angle-test`, `edit`, and `publish` release an item only
   when the evidence is recorded on the card. "We reviewed it" is not evidence.
4. **Publish is a human decision.** An agent prepares the package and sets `next_decision`;
   Mary or Jim decides and signs the Decision log.
5. **Skipping `angle-test` is a decision.** Record who skipped it and which prior evidence
   justified it. `derisk-first` items may never skip it.
6. **One move per cycle.** The loop advances one item through one step, then records.
7. **Escalation is normal.** An agent that stops and asks has done its job correctly. The
   question it asked becomes a context pack.
8. **No claim without a source.** The one rule we will not trade for speed.

## Cadences

- **Loop cycle**: every weekday morning, agent-run; Dana reads the loop log.
- **Meta-loop**: Fridays, and always after a piece is dropped at `angle-test`.
- **Decision forum**: Monday content review — publish decisions and anything the loop
  parked as `DECISION-PENDING`.

## Delegation stance

| Rung | Steps here today | What would promote the next one |
|---|---|---|
| 0–1 human-led | `angle-test`, `edit`, `publish` | for `edit`: a claims-audit check the agent can run itself, and 10 clean items |
| 2–3 agent-drafts / agent-runs | `intake`, `research`, `draft`, `learn` | for `draft`: a house-voice check that catches what Dana catches |
| 4–5 checked / automated | `amplify` | for `publish`: nothing — the decision stays human by choice, not by capability |

Reversibility caps the rung. `amplify` is at 4 because a bad post can be deleted in a
minute; `publish` stays human because our name is on it and the internet remembers.

## Measures

We steer on `measures.md`. The one we watch hardest is rework out of `edit` — it is the
earliest honest signal that the draft step is producing fluent nonsense.

## System of record

`integrations.md`. Today: mirror mode into the team's GitHub Project.

## Change log

| Date | Change | Why | Bet |
|---|---|---|---|
| 2026-06-01 | workflow defined | first version, lifted from how we already worked | — |
| 2026-07-06 | added `angle-test` as an optional step | two pieces in a row landed flat after a full draft | `probe-angles-before-drafting` |
| 2026-08-03 | `amplify` promoted to rung 4 | 12 consecutive clean runs with the amplify audit | `promote-amplify-to-checked` |

<!-- flow-config
id: fiy-content-engine
kind: content
steps: intake, research, angle-test, draft, edit, publish, amplify, learn
optional_steps: angle-test, amplify
entry: intake
terminal: shipped, dropped
edges:
  intake -> research
  research -> angle-test
  research -> draft            [when: a prior piece already evidenced this angle]
  angle-test -> draft
  angle-test -> dropped        [when: the probe says the audience does not care]
  draft -> edit
  edit -> draft                [rework]
  edit -> publish
  publish -> amplify
  publish -> learn
  amplify -> learn
  learn -> intake              [when: the readout raises a new question — spawns a NEW item]
  learn -> shipped
wip_limits: draft=2, edit=2, publish=1
aging_thresholds: intake=14, research=10, angle-test=7, draft=7, edit=5, publish=3, amplify=10, learn=14
decision_points: publish
evidence_exits: research, angle-test, edit, publish
cadence: weekday loop, Friday meta-loop
-->
