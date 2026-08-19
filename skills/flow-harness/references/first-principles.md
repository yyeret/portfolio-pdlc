# Why Work This Way — deriving a workflow from first principles

For when nothing formal exists, and for anyone who asks "why are we doing this at all?" —
which is a fair question and deserves a real answer rather than a framework diagram.

Do not start from a template. Start from the value, and let the workflow fall out of it.
A workflow derived this way is one people can defend; a workflow copied from a template is
one they abandon the first time it costs them something.

## Start from the value

Three questions, before any mention of steps:

1. **Who is worse off if this stream stops?** Name people, not departments.
2. **What do they get, that they would notice?** Not what you produce — what changes for them.
3. **How would you know it got better?** If nobody can answer, the stream is currently
   steering on faith, which is worth knowing before you design anything.

If question 1 has no answer, stop. You have found something more useful than a workflow.

## The derivation — seven questions

Each question produces a piece of the definition. Answer them in order; the order matters,
because each one constrains the next.

### 1. What flows? → the unit of value

One item is *what*? Apply the five tests in `unit-of-value.md`. Name it as an outcome, not
as an artefact. Everything below is defined relative to this answer, so spend the time here.

### 2. What has to become true before one item is valuable? → the steps

This is the derivation's core move. Not "what work do we do" — **what has to become true**.
Each distinct truth that has to be established is a candidate step:

- *We understand the problem well enough to be worth solving* → a framing step.
- *The riskiest assumption has been tested* → a discovery step.
- *The thing exists and behaves as intended* → a build step.
- *It is true, safe, and ours* → a verification step.
- *The people who need it have it* → a delivery step.
- *We know whether it worked* → a learning step.

A step exists to **retire a distinct kind of doubt** or **add a distinct kind of value**.
Two steps that retire the same doubt are one step. A step that retires no doubt is a habit.

### 3. How would you know each one is true? → exit evidence

For each step: what would convince a sceptical colleague, who did not do the work? Write
that down; it is the exit evidence, and it is where quality is actually decided. If the only
honest answer is "you'd have to trust the person who did it", write *that* — an honest
weak exit is fixable, an invented strong one is not.

### 4. Which of those could be wrong in an expensive way? → derisking and decision points

Two different things fall out here:

- Truths that are **expensive to get wrong** need testing *before* the commitment they
  justify. That is a discovery or probe step, placed before the point of last return.
- Choices that are **expensive to reverse** need a person's name on them. That is a decision
  point, and the person is named, not a role.

In complex knowledge work the costly failure is confidently executing the wrong thing. This
question is where you buy protection from it, and it is the question templates skip.

### 5. What happens when a truth turns out not to hold? → back-edges

Work comes back. Draw the edge. A graph without back-edges is a graph that has never met a
real item, and rework you cannot see is rework you cannot reduce.

### 6. How many can we hold at once? → WIP limits and pull

Not "how many can we start" — how many can be *in progress* without everything slowing down.
Start looser than feels right, tighten on evidence. The limit's job is not efficiency; it is
to force the finishing conversation before the starting one.

### 7. Who does what, and how? → delegate and run models

For each step: who holds it today, what would have to be true for an agent to hold it, and
how is it actually run. Start from what happens *now*, not from the ambition — the ladder in
`step-contracts.md` is a path, and paths need a starting point that is true.

## Why each mechanism exists

The honest version, including what you lose by skipping it.

| Mechanism | The claim | Without it | Smallest version |
|---|---|---|---|
| **An explicit workflow** | you cannot improve what you cannot see; a shared language ends the same argument recurring | every conversation restarts from first principles; improvement is opinion vs opinion | the step names, on one page |
| **Steps** | different doubts need different work and different checks | one undifferentiated blob where quality is decided by whoever is tired | three steps |
| **Exit evidence** | fluent output reads as finished work | watermelon items — green until they are not | one sentence per step |
| **Pull + WIP limits** | starting is free, finishing is not | everything in progress, nothing done, and no slack to absorb surprise | one limit, on the busiest step |
| **Decision points** | some choices need a person's name on them | decisions happen by default, late, and nobody owns the consequence | one, at the point of last return |
| **A graph with back-edges** | rework is normal and worth seeing | rework hides inside "in progress" | draw the one loop everyone knows about |
| **Measures** | steering on anecdote favours whoever spoke last | improvement is fashion | age in step, and one outcome measure |
| **The meta-loop** | the workflow will be wrong, and being wrong slowly is the expensive part | the definition rots into decoration | one 30-minute review a month |
| **Delegate model per step** | autonomy that ignores blast radius fails loudly | either nothing is delegated, or the wrong thing is | write the current rung down |
| **Context packs** | most agent quality comes from what it can see | the same question answered forever | one file, from the last question someone asked |

## The objections, answered

**"This is bureaucracy."** Bureaucracy is process that serves the process. Every mechanism
above earns its place by changing a decision — and the meta-loop's job includes deleting the
ones that stop doing so. If a step cannot say what it retires, delete it today.

**"Our work is too creative for steps."** The steps are not a method for doing the work; they
are the points at which doubt gets retired. Creative work has *more* doubt, not less — which
is why the exits matter more here, not less. Nothing in a definition of workflow says how to
think.

**"We already know how we work."** Then it costs an hour to write down, and the disagreement
you find in that hour is the return. The reliable outcome of a first mapping is not the map —
it is discovering that three people described three different workflows.

**"We tried Kanban and it died."** Usually because the board was maintained by hand and
drifted, or because limits were imposed rather than derived. Here the board is generated
from the items, and the limits come out of question 6 with the people who live with them.

**"The agent can just figure it out."** It will figure out *something*, fluently, every time,
with no way for you to tell a good run from a bad one. The workflow is what makes the
difference visible — and what lets you delegate more next month with evidence rather than
hope.

## When not to formalise

Say this plainly rather than selling a harness into a place that does not need one:

- **Low volume.** A handful of items a quarter needs a conversation, not an operating system.
- **One person, one head.** No handoffs means no queues means little to see. Revisit when a
  second person joins.
- **Genuinely one-off work.** A workflow is for things that recur.
- **The real problem is an unmade decision.** No amount of flow design fixes a stream waiting
  on a choice nobody will make. Name that instead; it is more useful and less work.

## The smallest honest starting workflow

If you have nothing and want to start today:

```
<!-- flow-config
id: <stream>
kind: custom
unit: <one item is …>
unit_outcome: <what changes for whom when one finishes>
steps: intake, do, verify
entry: intake
terminal: done, dropped
edges:
  intake -> do
  do -> verify
  verify -> do        [rework]
  verify -> done
  intake -> dropped   [when: it stops being worth doing]
wip_limits: do=2
aging_thresholds: intake=14, do=7, verify=3
decision_points:
evidence_exits: verify
cadence: weekly loop, monthly meta-loop
-->
```

Three steps, one exit that must hold, one limit, one back-edge, one honest terminal state for
things that should stop. Run it for a fortnight. The board will tell you what to add — and
what you were wrong about — faster than any further design will.

Then grow **only on evidence**: a step because a doubt keeps surviving to the end, a limit
because work keeps piling up, an exit because something keeps coming back. Every addition is
a bet in `improvements/`, with kill criteria, like everything else.
