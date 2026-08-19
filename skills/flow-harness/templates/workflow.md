# Definition of Workflow — <Stream Name>

This is OUR workflow for <the value stream>. It started from an archetype and we own it
from here: try, inspect, adapt. It is a **common language and a set of pull policies, not
a set of gates** — work moves on evidence and capacity, not on ceremony.

## What this stream is for

- **Value delivered**: <what changes in the world when an item finishes>
- **Customer / consumer**: <who receives it>
- **Trigger**: <what makes an item exist>
- **Definition of "in this stream"**: <what belongs here, and what deliberately does not>

## Flow boundaries

- **Start**: <the moment an item becomes ours to track — request received? idea captured?>
- **End**: <the moment it stops being ours — outcome measured? handed to operations?>

Everything before the start and after the end is somebody else's flow. Say who.

## Demand

| Class of service | What it is | Arrival rate | Pull policy |
|---|---|---|---|
| standard | the normal case | <n/week> | pull when the step has capacity, oldest first |
| expedite | <the genuine emergency> | <rare> | jumps the queue; costs a WIP slot; needs a named human |
| fixed-date | <externally dated work> | <n/quarter> | scheduled backwards from the date |
| derisk-first | <high blast radius / novel> | <n/quarter> | must pass a discovery step before commitment |

If every item is expedite, none is. If nothing is ever derisk-first, either the work is
simple or the risks are invisible; check which.

## Steps

| Step | Intent | What you can rely on when an item leaves | Delegate rung | Run |
|---|---|---|---|---|
| <step-id> | <why this step exists> | <exit evidence, in one line> | <0–5> | <skill/prompt/script/tool/human> |

Full contracts live in `steps/<step-id>.md`. This table is the read-in-one-minute version;
the step files are the truth.

## The graph

<Describe the shape in a sentence or two: the happy path, the branches that matter, and
the back-edges that are normal rather than shameful. The machine-readable graph is the
`flow-config` block at the bottom.>

## Policies

1. **Pull, don't push.** A step takes new work when it has capacity, not when upstream
   wants to hand it over.
2. **Right-to-left.** Walk the board from the last step backwards. Finishing outranks
   starting.
3. **Evidence exits.** At the steps listed in `evidence_exits`, an item leaves only when
   its exit evidence is recorded on the item. Not "we reviewed it" — the recorded finding.
4. **Decision points are human.** Entering the steps listed in `decision_points` needs a
   dated Decision-log entry naming a person.
5. **Skipping an optional step is a decision.** Record who skipped it and on what basis.
6. **One move per cycle.** The loop advances one item through one step, then records.
7. **Escalation is normal.** An agent that stops and asks has done its job correctly.
8. <your policy — the one you argue about most is usually the one worth writing down>

## Cadences

- **Loop cycle**: <how often the run loop fires, and who/what triggers it>
- **Meta-loop**: <how often the workflow inspects itself — weekly? every 20 items?>
- **Decision forum**: <where the human decisions actually get made>

## Delegation stance

Where we are on the ladder today, and what would move us:

| Rung | Steps here today | What would promote the next one |
|---|---|---|
| 0–1 human-led | <steps> | <the context artifact or check that is missing> |
| 2–3 agent-drafts / agent-runs | <steps> | <the evidence bar: N clean items, escape rate under X> |
| 4–5 checked / automated | <steps> | <the independent check that makes it safe> |

Rungs are per step and per evidence, never per workflow. Reversibility caps the rung: the
harder a step is to undo, the more human it stays regardless of how good the agent looks.

## Measures

We steer on the measures in `measures.md`. Each step names the ones it feeds.

## System of record

Bindings, field ownership, and sync rules live in `integrations.md`.

## Change log

Every change to this file or to a step contract gets a dated line here. Anything beyond a
typo should trace back to an improvement card in `improvements/`.

| Date | Change | Why | Bet |
|---|---|---|---|
| <YYYY-MM-DD> | workflow defined | first version | — |

<!-- flow-config
id: <stream-id>
kind: <development | operational | content | ai-use-case | custom>
steps: <step-a>, <step-b>, <step-c>
optional_steps:
entry: <step-a>
terminal: done, dropped
edges:
  <step-a> -> <step-b>
  <step-b> -> <step-c>
  <step-c> -> <step-b>          [rework]
  <step-c> -> done
  <step-b> -> dropped           [when: the item stops being worth doing]
wip_limits: <step-b>=2
aging_thresholds: <step-a>=14, <step-b>=7, <step-c>=5
decision_points:
evidence_exits: <step-b>
cadence: <daily loop, weekly meta-loop>
-->
