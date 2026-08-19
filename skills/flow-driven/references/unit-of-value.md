# The Unit of Value — deciding what flows

The most consequential decision in a definition of workflow, and the one most often made by
accident. Everything else is defined relative to it: the steps are what happens to *one*,
the WIP limits count *them*, cycle time is how long *one* takes, throughput is how many
finish, and every measure inherits whatever confusion is in the unit.

Get it wrong and the board cannot answer a single useful question — not because the board is
bad, but because nobody agreed what it is counting.

## What a good unit looks like

Five tests. A unit that fails one is usually still workable; one that fails three is why the
flow does not make sense.

1. **Finishing one produces value someone outside the stream would notice.** Not "a step was
   completed" — something changed for somebody who does not work here.
2. **It can actually finish.** It has an end, and the end is reachable in a number of loop
   cycles you can count on one hand.
3. **Its identity survives the whole graph.** The thing that entered is recognisably the
   thing that left. If it fragments halfway through, you picked a container, not a unit.
4. **You can hold several in your head.** If describing three items takes twenty minutes,
   they are too big or too vague to steer.
5. **Counting them says something true.** "We finished six" should mean roughly six times the
   value of one. If items vary by 50×, you have several units wearing one name.

## Orient it around the outcome

The default failure is naming the unit after the **artefact** or the **activity** rather
than the change it produces. Both feel concrete, and both quietly redefine "done" as
"something exists" rather than "something is different".

| Instead of | Say | Why it matters |
|---|---|---|
| "a blog post" | "a piece that changes one operating decision for a studio owner" | the exit is a change, not a URL |
| "a ticket" | "a change to how the product behaves for a user" | tickets close; behaviour is what shipped |
| "the Q3 report" | "a decision the leadership team can make with confidence" | reports get read or not; decisions are observable |
| "a model experiment" | "a use case running in front of real users at a stated quality bar" | experiments never end; use cases do |
| "a support ticket" | "a customer's problem resolved and not recurring" | reopen rate becomes meaningful |

Three practical consequences, all of them cheap:

- **Name items as outcomes.** `owners-stop-treating-churn-as-pricing` steers; `blog-post-14`
  does not. The slug is permanent, so this is worth ten seconds of thought.
- **Every item carries an outcome hypothesis**: *if we finish this, we expect <observable
  change> for <someone>, visible as <indicator>*. The board flags items past intake without
  one, because an item nobody can state a hypothesis for is an activity in a costume.
- **The stream's `unit_outcome` is the item hypothesis, generalised.** If you cannot write it
  for the stream, the items will not have one either.

## Candidate units by archetype

| Archetype | A good unit | A tempting bad one |
|---|---|---|
| development | a change that alters user-visible behaviour | a ticket, a PR, a sprint, a "feature" nobody has sized |
| operational | one request from one person who is waiting | a shift, a queue, a batch of tickets |
| content | one piece carrying one idea | a campaign, a channel, a content calendar |
| ai-use-case | one use case taken to a stated quality bar | a model, a prompt, an experiment |
| research | one question that a decision depends on | a document, a study, a "workstream" |

Notice the pattern: the good units are **countable, finishable, and attributable to
someone's change**. The bad ones are containers, tools, or time.

## The wrong units, and their tells

| Wrong unit | The tell on the board |
|---|---|
| **The task** ("write section 2") | the board reads as a to-do list; cycle time is meaningless; WIP limits do nothing |
| **The artefact** ("the report") | items finish when a file exists; nobody can say whether it worked |
| **The batch** ("Q3 campaign") | nothing finishes for a quarter; throughput is zero then five |
| **The ticket / PR** | the flow mirrors the tool; two "items" are the same change; closing is the goal |
| **The ceremony** ("the review") | steps named after meetings; the exit is that the meeting happened |
| **A person's work** ("Dana's stuff") | the board is an org chart; WIP limits become workload arguments |
| **The project** | one item, twelve months, no flow to speak of |

Each of these can be *rescued*: a batch becomes a rollup with real children; a project
becomes a portfolio item with an inner stream; a ticket becomes an item when the item is
named after the change rather than the record.

## Right-sizing

**Too big** — it cannot finish inside a few loop cycles, nobody can hold three of them, and
the board stops moving between reviews. Fixes: slice by the outcome (which part changes
something on its own?), not by the work (design / build / test are steps, not items); or
make it a `rollup` with children that each pass the five tests. The rollup carries the
hypothesis, the children carry the work.

**Too small** — coordination costs more than the work, the board is noise, and people batch
them informally to cope. Fix: raise the unit to the level someone outside would recognise,
and let the small things be inner-graph nodes or checklist lines inside a step.

Rule of thumb: **a unit should finish within a handful of loop cycles.** Daily loop, weekly
to fortnightly items. If your loop is daily and your items take a quarter, you are not
running a flow — you are watching a Gantt chart with better tooling.

Variation is fine; 50× variation is not. If your items differ that much, either split the
big ones or admit you have two streams with different units and different cadences.

## Declaring it

Two keys in the `flow-config` block, and a narrative section in `workflow.md`:

```
unit: one published piece carrying one idea, from question to measured outcome
unit_outcome: a studio owner changes one operating decision, and we can see they did
```

`flow_lint.py` treats a missing `unit` as a **violation** — a workflow whose definition does
not say what flows cannot be checked against anything — and a missing `unit_outcome` as a
warning, because a unit with no stated change is how activity-shaped work gets legitimised.
The board prints both at the top, every cycle, where they are hard to ignore.

## Changing the unit later

Changing the unit is a **redefinition, not an edit**. Cycle time, throughput, and every
historical comparison become incomparable across the change, and pretending otherwise
produces confident nonsense in the first review afterwards.

Do it deliberately: an improvement bet, a dated change-log line in `workflow.md`, and a
marker in the flow log's history so nobody averages across the boundary. It is often the
right move — realising six months in that you have been flowing tickets rather than changes
is a genuine insight — but it is a new baseline, not a tweak.
