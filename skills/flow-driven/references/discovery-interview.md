# Discovery by Interview — surfacing the workflow that already exists

Almost nobody has no workflow. They have one nobody has written down, running on folklore,
habit, and one person who notices when things stall. This is how to get it out of people's
heads and onto the page — without leading the witness, and without proposing anything yet.

## Which path are you on

| What exists | Path | Where |
|---|---|---|
| A formal artefact: spec-kit, Kiro, a bespoke harness, a tracker with states | **Adapt** | `ingest-recipes.md`, then come back here for the parts the artefact does not cover |
| A real workflow living in people's heads and habits | **Discover** | this document |
| Genuinely nothing — a new stream, a new team, a new capability | **Derive** | `first-principles.md` |

The common case is a mix: a tracker that describes a third of it, a folder of prompts that
describes another third, and folklore for the rest. Ingest what is written, interview for
the rest, and be explicit about which parts came from where — the folklore parts are the
ones most likely to be wrong, and most likely to matter.

## Before you interview

1. **Read what exists first.** Ten minutes with the tracker or the folder buys much better
   questions. Never spend an interview asking what a file could have told you.
2. **Pick three people, not one**: the person who does the work, the person who receives the
   output, and the person who gets nagged when it stalls. The third one knows where the
   waiting is.
3. **The one rule**: ask about **the last real item**, not about "the process". People
   describe the process they wish they had; they remember the thing they actually did last
   Tuesday. Every question below is anchored to a real item on purpose.

## The interview ladder

Twelve questions, in this order. Roughly 45 minutes. Follow the tangents — the tangents are
usually the back-edges.

| # | Ask | Listen for | Follow up with |
|---|---|---|---|
| 1 | "Walk me through the last one you finished. Start from when it showed up." | the actual sequence, in their verbs | "and then what happened?" until they stop |
| 2 | "What made it exist? What was happening just before?" | the trigger, the entry boundary | "does it always arrive that way?" |
| 3 | "Who asked for it, and what did they want to be *different* afterwards?" | **the unit of value and its outcome** | "how would they know it worked?" |
| 4 | "When did you know it was done? Who agreed?" | the end boundary, the real exit | "what would have made you say not yet?" |
| 5 | "Where did it sit and wait? For how long?" | queues — usually the biggest number in the room | "what was it waiting *for*?" |
| 6 | "What came back? What had to be redone?" | back-edges, and the weak exit upstream of them | "what would have caught that earlier?" |
| 7 | "What did you have to go and find out or dig up?" | repeated context assembly — the highest-yield agentic target | "where did you find it? was it written down?" |
| 8 | "What decisions got made along the way, and who made them?" | decision points and who genuinely owns them | "what happens if that person is away?" |
| 9 | "What would have made you stop or drop it?" | branch conditions, kill criteria, derisking | "has that ever actually happened?" |
| 10 | "What do you always have to explain to someone new?" | context packs, in their own words | "is that written anywhere?" |
| 11 | "What was different about the last hard one?" | classes of service, variability | "how often is it like that?" |
| 12 | "Which one are you least proud of? What went wrong?" | failure modes and the exits that did not hold | "would anything have caught it?" |

Question 3 is the one to slow down on. If the answer is about producing an artefact rather
than changing something for someone, you have found the stream's central confusion, and
`unit-of-value.md` is the next conversation.

## What to listen for

- **Passive voice.** "It gets reviewed", "it goes to legal". Somebody or something specific
  is doing that. An unnamed actor is an unnamed step, and unnamed steps have no exits.
- **"Usually" and "normally".** Variability, announced. Ask what the other case looks like —
  that is your branch, or your second class of service.
- **The nag.** "I chase them", "I ping the channel on Fridays". This is the human glue and
  it *is* the current control system. It appears in no tool and it is often the single most
  valuable thing flow-driven replaces.
- **Waiting described as working.** "It was with design for two weeks" is a queue, not a
  step, unless someone was doing something for two weeks. Ask which.
- **Numbers stated with confidence and no source.** Note them as opinion. They are often
  wrong by a factor, and the flow log will settle it later.
- **Disagreement between interviewees.** Do not resolve it. Record both versions with names.
  Two people describing different workflows *is a finding*, usually about a handoff.

## From transcript to draft graph

1. **Step candidates from the verbs.** What did somebody *do* to the item. Verbs that change
   the item's state are steps; verbs that describe waiting are queues.
2. **Queues become one of two things**: a step with `type: wait` when the waiting is real and
   outside your control, or a handoff to remove. Naming it as a wait makes it visible; that
   alone often ends the debate about where the time goes.
3. **Exits from question 4 and 6.** "When did you know it was done" gives the exit evidence;
   "what came back" tells you which exits are currently too weak to hold.
4. **Back-edges from question 6.** Draw them. Rework that everyone knows about but nobody
   draws is how a graph flatters its owners.
5. **Decision points from question 8**, with the name of the person, not the role.
6. **Context packs from questions 7 and 10.** Each one is a `platform/context/` file waiting
   to be written, and you already have its first draft in their answer.
7. **Classes of service from question 11**, only where the *pull policy* would genuinely
   differ. Otherwise it is one class with variation.

Draft it, then read it back to them in their own words. The sentence you want is "yes, that
is what we do — except…". The exception is the real interview.

## Archetype matching

Once you have a draft trace, check it against the archetypes in `workflow-archetypes.md`.
Match on **failure mode and evidence shape**, not on vocabulary — every stream calls its
steps something different, and none of that matters.

| Archetype | Tells |
|---|---|
| **development** | there is a point of last return after which changing course is expensive · a commit or approval that resources the work · tests or review as the natural check · "we found out too late that…" |
| **operational** | somebody is waiting while it happens · volume measured per day or per week · classification early · "how long until someone gets back to them" is a real question |
| **content** | the output is published to people you do not control · claims that need sourcing · taste and voice are part of "done" · an editor or an equivalent gatekeeper |
| **ai-use-case** | you cannot say whether the output is good without a dataset · demos exist, production does not · "it works, mostly" · nobody has written down the pass bar |
| **research / analysis** | the deliverable is a decision, not a thing · sources and provenance matter · the risk is confident wrongness · a challenge or peer-review step exists, or should |

**The verdict rule**:

- **3+ tells and they recognise the failure mode** → propose that archetype as a starting
  point. Say what it would give them (steps, exits, starting rungs, measures) and where
  their trace already differs. It is a shortcut, not a verdict.
- **Two archetypes both match strongly** → you are probably looking at two streams sharing a
  team. Split them and pick one; a hybrid definition serves neither.
- **No archetype matches** → custom, and that is a perfectly good answer. Build the graph
  from the trace and steal exit evidence from the nearest archetype, which is where most of
  the reusable thinking lives anyway.
- **They recognise an archetype but not its failure mode** → be careful. Either it is not
  their archetype, or the failure has not bitten them yet. Ask question 12 again.

Present the match as a proposal with a named alternative, never as a classification. The
sentence to avoid is "you're a content pipeline"; the sentence to use is "this looks closest
to the content archetype — here is what that assumes, and here is where you already differ".

## Interview modes

- **Live** (best): 45 minutes, three people, separately. Separately matters — a group
  interview produces the official version.
- **Async**: send questions 1–6 and ask for the last real item. Weaker, but it still beats a
  process document.
- **Agent-led**: read every artefact, produce a draft definition plus **the five questions
  whose answers would most change it**, ranked. Then a human spends 20 minutes instead of
  two hours. In headless mode this is the default: draft, mark every inference as an
  assumption, and end with the question list rather than guessing.

Whichever mode: mark each element's provenance — observed in an artefact, stated by a named
person, or inferred. Inferred elements are the first things the first two cycles will
correct, and knowing which they are makes that fast instead of embarrassing.

## When you have enough

Stop when: two people describe the same trace, you can name the exit evidence for each step
without inventing it, and you can predict where the next item will wait. That is enough to
run cycles, and cycles will teach you more in a fortnight than a third interview will.

Signs of over-mapping: steps nobody could give an example of, a graph with more branches than
items per month, or a second week of interviews. Map the part you will actually run.

## Output

`reviews/YYYY-MM-DD-workflow-discovery.md`:

- **The trace** — the last real item, end to end, in their words.
- **Who said what**, including the disagreements, unresolved and attributed.
- **The draft graph** with provenance per element (observed / stated / inferred).
- **The archetype verdict** — matched, split, or custom, with the tells that decided it.
- **The waiting** — where time actually went, with the numbers if anyone had them.
- **The human glue** — the nagging, chasing, and noticing that is currently holding it up.
- **The five questions** that would most change the definition.

Then `flow-driven-define` turns it into `workflow.md`, and `flow-driven-scaffold` makes it
run.

## Anti-patterns

- **Leading the witness.** "So you do discovery first, right?" gets a yes and teaches you
  nothing. Ask about last Tuesday.
- **Interviewing only managers.** You will get the workflow as designed, not as run. Both
  are worth having; only one of them is what happens.
- **Mapping the ideal.** "We should really…" is a backlog item, not a step. Write it in the
  improvement lane and carry on mapping what is.
- **Resolving disagreements in the room.** Record them. They are the most valuable output of
  the interview and they belong to the team to settle.
- **Proposing during discovery.** The moment you propose, they stop describing. Keep the two
  conversations separate even if they are ten minutes apart.
