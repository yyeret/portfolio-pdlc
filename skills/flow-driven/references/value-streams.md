# Choosing What to Make Agentic — value stream identification

Before you design a loop, pick the right thing to put in it. Most agentic programmes fail
here: they automate the workflow someone could describe rather than the one that carries
the value, and then wonder why nothing changed.

Two families of stream are worth running this way:

- **Development value streams** — build something that did not exist. Product delivery, a
  spec-driven SDLC, research, an AI use-case pipeline, a content engine. High variability,
  high knowledge content, evidence is *created* along the way.
- **Operational value streams** — run something repeatedly for someone waiting. Customer
  onboarding, support triage, contract review, month-end close, incident response. Higher
  volume, lower variance, evidence mostly *exists* and needs finding.

They both flow, they both benefit — but they fail differently. Development streams die of
undetected wrongness; operational streams die of queueing and handoffs. Design accordingly.

## Finding the streams (a working method)

Do this with the humans who do the work, not from an org chart.

1. **Start from an outcome someone outside your team notices.** "A studio owner changes how
   they handle week three." Not "the content team publishes."
2. **Walk it backwards to its trigger.** What made this item exist? Keep going until you hit
   something outside your control — that is the real entry point.
3. **List the handoffs, not the teams.** Every handoff is a queue, and queues are where time
   goes. Mark which handoffs involve *waiting for a person's attention* — those are the ones
   agents can most obviously change.
4. **Ask where work waits.** Not where work is hard. In knowledge work, waiting typically
   dwarfs touch time; the constraint is almost never the step everyone talks about.
5. **Ask what people re-derive every time.** Repeated context assembly is the highest-yield
   agentic target in any stream, and the easiest to prove.
6. **Ask what gets discovered late.** Rework tells you where an exit is too weak — that is
   where evidence, not automation, is the intervention.
7. **Name the stream by its outcome.** If you cannot name it without listing departments,
   you have found an org chart, not a value stream.

Two or three streams will emerge. Do **one**.

## Which stream first — scoring

Score each candidate 1–3. This is a conversation-forcing device, not a formula.

| Dimension | 1 | 2 | 3 |
|---|---|---|---|
| **Volume** | a handful a quarter | weekly | daily or more |
| **Pain** | mildly annoying | people complain | it is on a leadership slide |
| **Repeated context assembly** | every item is unique | some reusable context | the same context every time |
| **Evidence availability** | outcomes unknowable | proxies exist | outcomes observable within weeks |
| **Reversibility** | irreversible, high blast radius | recoverable with effort | undo in minutes |
| **Human appetite** | the team is threatened | curious | actively asking |
| **Decision clarity** | nobody knows who decides | decided by committee | one named human decides |

**12+ and reversible**: start here. **8–11**: a good second. **Below 8**: making it agentic
will produce a working demo and no change in outcomes.

Two dimensions are veto-shaped, not additive:

- **Reversibility at 1** caps how far the ladder can climb no matter how good the scores.
  You can still make the stream *visible* and *evidence-driven*; just do not promise autonomy.
- **Human appetite at 1** is not a technical problem and will not be solved by a better
  prompt. Pick another stream and let the result travel.

## Where to start inside the stream

Not everything at once. Ranked by yield per unit of risk:

1. **Make it visible.** The definition of workflow and the board, with humans doing every
   step. This alone routinely surfaces the constraint and costs nothing to reverse. Teams
   are consistently surprised by their own board.
2. **Assemble context.** Put an agent on the step where people re-derive the same context
   every time. Reversible, immediately felt, and it builds the platform.
3. **Draft inside a step.** Rung 2 on the step with the clearest exit evidence.
4. **Verify.** Automate a *check* before you automate the work it checks. A good check is
   what makes every later promotion safe.
5. **Run a whole step.** Rung 3+, on the most reversible step first.
6. **Orchestrate.** Only once several steps have contracts worth running.

Starting at 6 is the standard mistake. An orchestrator over steps with no exit evidence
just gets to the wrong answer faster and with better formatting.

## Anti-patterns

- **The demo stream.** Chosen because it is easy to show, not because anyone waits on it.
- **The org-chart stream.** "Marketing's workflow" is a department, not a flow.
- **The stream nobody owns.** No named decider means no decisions, and the loop parks.
- **Boiling the value stream.** Mapping fourteen steps across five teams before running one
  cycle. Map the part you will actually run this month.
- **Automating the handoff instead of removing it.** If two steps always run together for
  the same person, that is one step and you have automated a queue into existence.
- **Skipping the boring stream.** The unglamorous operational stream with daily volume and
  full reversibility usually beats the strategic one on every dimension that matters.

## Then what

Once you have picked: `flow-driven-define` runs the systems read that turns the stream
into a definition of workflow. If the org already has a workflow artefact — a spec-kit
setup, a Kiro spec dir, a bespoke harness, a tracker with states — start with
`flow-driven-ingest` instead, and map what exists before proposing anything.
