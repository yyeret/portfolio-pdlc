# Spec — Flow-Driven (the meta-framework)

**Status**: draft v0.1 · **Realised as**: `skills/flow-driven*` in this repo ·
**Intended end state**: a standalone meta-framework, extracted from this repo, of which
`portfolio-pdlc` becomes one instance.

This is the specification for **Flow-Driven**: a flow-driven agentic loop engineering
framework that takes any value stream — a PDLC, an SDLC, a content pipeline, an AI use-case
pipeline, an operational request stream — and turns it into an engineered agentic loop with
an explicit definition of workflow, an explicit unit of value, evidence-based steering,
per-step delegation and run models, measurement inside the workflow, and a meta-loop that
adapts the loop.

The name states the claim: work is steered by **where it sits and how long it has sat in a
flow**, not by a task list — and the loop is driven by evidence at the exits, not by
activity.

The implementation in `skills/flow-driven/` is the first, opinionated instantiation.
This spec is what gets extracted, generalised, and built as its own thing.

---

## 1. Framing

**The claim.** An agentic workflow is not a prompt chain; it is a flow system with two
nested control loops — an outer loop moving items through a graph of steps, and an inner
loop getting one step done. Both need a trigger, a bounded move, an evidence-based exit,
and a recorded trace. Most harnesses specify only the move.

**The bet.** In complex knowledge work, the constraint is not model capability. It is
(a) undetected wrongness, (b) human attention spent in the wrong places, and (c) workflows
nobody has written down. A framework that makes flow visible, exits evidential, delegation
explicit, and adaptation routine beats one that makes generation faster.

**The unit of value**: a value stream, run as a loop, that leaves the organisation with more
leverage every cycle — including leverage over the loop itself.

## 2. Scope

**In scope**: choosing the stream · defining the workflow · ingesting existing workflow
machinery · scaffolding it as plain markdown · orchestrating it agentically · measuring it ·
integrating it with the system of record · evolving it · the delegation and platform path.

**Out of scope (deliberate non-goals)**:

- A runtime, daemon, scheduler, or DAG engine. Orchestration is a deterministic selector
  plus whatever agent is reading; the framework must run by hand when tooling is absent.
- A hosted product, a database, or a UI.
- Model- or vendor-specific behaviour. The framework must work from any agent harness that
  can read files and run `python3`.
- Replacing working automation. The framework wraps; it does not rewrite.
- Deciding for humans. It prepares decisions and refuses to make the ones reserved to people.

## 3. Domain model

| Entity | Definition | Key relationships |
|---|---|---|
| **Stream** | one value stream run as a loop | has one Workflow, many Items, one Platform |
| **Workflow** | the definition: graph + policies + cadences | has a UnitOfValue, Steps, Edges, terminal States |
| **UnitOfValue** | what one Item *is*, named as an outcome rather than an artefact | declared on the Workflow; every Step, limit, and Measure is defined relative to it |
| **Step** | a node with a contract | has ExitEvidence, DelegateModel, RunModel, Measures, optional InnerGraph |
| **Edge** | a permitted transition, optionally conditional or rework | connects Steps and terminal States |
| **InnerGraph** | a bounded mini-graph private to a Step | has Nodes, a stop rule; never holds Items |
| **Item** | one unit of work flowing through the graph | sits on a Step; may have a parent Rollup |
| **Rollup** | an Item that aggregates children | position derived from its least-advanced child |
| **ExitEvidence** | what you can rely on when an Item leaves a Step | recorded on the Item, verified independently |
| **DelegateModel** | the rung (0–5) plus the reason and the promotion/demotion criteria | per Step, overridable per Item |
| **RunModel** | how the Step executes: mechanism, context, tools, guardrails, budget, stop rule | per Step |
| **Measure** | a number that changes a named decision | declared once, referenced by Steps |
| **Integration** | a binding to a system of record | owns specific fields, one writer each |
| **ContextPack** | reusable knowledge a Step runs against | the platform's compounding unit |
| **Check** | verification independent of the runner | what makes a rung promotion safe |
| **Bet** | a proposed change to the Workflow, with kill criteria | rides the same lifecycle it manages |
| **Projection** | board, flow log, export — all derived | never a source of truth |

**Invariant set** (these are the framework, everything else is convenience):

1. Item frontmatter is the state; everything else is a projection.
2. A Step is finished when its ExitEvidence exists.
3. Exactly one writer per field, across all Integrations.
4. Decision points require a dated human decision.
5. Every inner loop is bounded.
6. The verifier is not the doer.
7. Changes to the Workflow are Bets with kill criteria, not edits.
8. The UnitOfValue is declared, and stated as a change for someone rather than an artefact.

## 4. Requirements

Each requirement: the ask, why it exists, how you know it is met, and where it is realised
today. `R#` ids are stable and should be referenced by the extracted framework's tests.

### R1 — Adapts to any workflow

The framework must fit a PDLC, an SDLC, a content pipeline, an AI use-case pipeline, and an
operational request stream without special-casing any of them.

- **Accept**: the same schema, scripts, and loop run all five archetypes; archetypes are
  *starting points* (steps, exits, rungs, measures, failure modes), never fixed templates;
  `kind:` is a hint, not a constraint; adapting to a stream is primarily a **discovery**
  activity (R25), with archetype selection as an optional shortcut and "custom" a
  first-class outcome.
- **Realised**: `references/workflow-archetypes.md`; `flow-config.kind`; R25.

### R2 — Guides choosing which workflow to make agentic

Identify operational and development value streams and choose one, on evidence.

- **Accept**: a repeatable identification method that starts from outcomes and finds streams
  by handoffs and waiting, not by org chart; a seven-dimension score with reversibility and
  human appetite as vetoes; a ranked first move; the not-chosen streams recorded with reasons.
- **Realised**: `flow-driven-choose`, `references/value-streams.md`.

### R3 — Helps define the workflow

Produce a definition of workflow the team recognises as theirs.

- **Accept**: three explicit entry paths — **Adapt** (an artefact exists), **Discover** (an
  unwritten workflow exists, R25), **Derive** (nothing exists, R26) — and a nine-move systems
  read producing the unit of value (R27), steps, graph, exits, policies, classes of service,
  WIP limits, cadences, and the delegation stance; output is machine-readable and lintable;
  the first version describes what exists rather than proposing what should.
- **Realised**: `flow-driven-define`, `templates/workflow.md`, `references/workflow-definition.md`.

### R4 — A point of view on loop engineering, end to end and within a step

The framework must be opinionated, and its opinions must be inspectable and arguable.

- **Accept**: a stated model (two nested loops), named principles, the six beats of the outer
  loop, the criteria for when a step deserves an inner graph, and a catalogue of failure
  modes each mapped to a countermeasure the framework actually implements.
- **Realised**: `references/loop-engineering.md`.

### R5 — Ingests existing workflows

Adopt spec-kit, Kiro, bespoke harnesses, agent skill libraries, trackers, and workflow engines.

- **Accept**: per-tool mapping recipes; existing assets bound as run refs, checks, and
  context packs rather than rewritten; tracker transition history mined for the *actual*
  workflow; output includes a delta report separating observed, documented, and automated;
  existing automation still runs unchanged afterwards.
- **Realised**: `flow-driven-ingest`, `references/ingest-recipes.md`.

### R6 — Guides what to measure, inside the workflow

Measurement is part of the workflow definition, not a separate dashboard project.

- **Accept**: four families (flow, evidence, leverage, outcome); every measure names the
  decision it changes; measures declared once and referenced per step, with a lint check that
  the reference resolves; explicit refusals (agent activity, volume as a goal); baselines
  before changes; a watermelon check on the cadence.
- **Realised**: `flow-driven-instrument`, `references/measurement.md`, `templates/measures.md`,
  the `measure-set` island, `flow_lint.py`.

### R7 — Integrates with wherever the workflow is managed

GitHub, Jira/Linear, an internal Kanban dashboard, a spreadsheet, chat.

- **Accept**: four modes (files-only, mirror, adopt, split) chosen explicitly; a field map
  with exactly one writer per field, machine-checked; idempotent sync keyed on a stable slug;
  a neutral export the harness pushes with its own tools; the framework's own scripts never
  touch the network.
- **Realised**: `flow-driven-integrate`, `references/integration-adapters.md`,
  `flow_board.py --export`, the `integration-map` island.

### R8 — A delegate model for each step

- **Accept**: a six-rung ladder with named accountability and check type per rung; the rung
  set per step by reversibility, blast radius, check quality, and accountability — not by
  model capability; promotion requires a baseline, an evidence bar, and a shadow run;
  demotion criteria written at promotion time; items may override for one pass; the board
  reports the delegate mix and flags mismatches in both directions.
- **Realised**: `references/step-contracts.md`, `delegate_rung`, `delegate_override`,
  `flow_board.py` flags, `flow-driven-evolve`.

### R9 — A run model for each step

- **Accept**: mechanism (`skill | prompt | script | tool | human | external`) plus run ref,
  context packs, tools allowed, guardrails, budget (agent *and* human), stop rule, artifacts
  written, and an escalation contract; lint fails a non-human run model with no run ref;
  `run: human` is a first-class, honest answer.
- **Realised**: step frontmatter, `flow_lint.py`, `flow_next.py`'s run card.

### R10 — Full graph, not just a linear loop

- **Accept**: arbitrary directed graphs with branches, joins, conditional edges, back-edges,
  multiple terminal states, and a loop-closing edge; lint checks reachability, dangling
  endpoints, and dead ends; rework is detected from the graph and reported per step; a
  straight line remains the default and is legal.
- **Realised**: the `edges:` grammar, `flow_defs.is_rework`, `flow_lint.lint_graph`.

### R11 — Mini-graphs inside steps

- **Accept**: an optional inner graph per step with nodes, entry, edges, and a mandatory stop
  rule on any loop edge; inner nodes are private — items never sit on them, the board never
  projects them, the flow log never records them; work waiting on an inner node is a step
  that must be promoted.
- **Realised**: the `step-graph` island, `flow_lint.lint_inner_graph`.

### R12 — Markdown scaffolding with real stubs

- **Accept**: the definition generates a complete workspace where every stub is a starting
  point rather than a `TODO`; every named context pack and check exists with real seed
  content; live work is carded at its honest position; the workspace lints clean and produces
  a sensible first run card; a scaffold brief lists what was defaulted and who must confirm it.
- **Realised**: `flow-driven-scaffold`, `templates/`.

### R13 — Simple orchestration to advance the workflow agentically

- **Accept**: a deterministic leverage table, first match wins, right-to-left within a rule;
  output is a run card carrying everything needed to execute exactly one move and everything
  to record after; machine-readable mode and exit codes for headless loops; the selector has
  no side effects on state.
- **Realised**: `flow_next.py`, `flow-driven-run`.

### R14 — A meta-loop that inspects and adapts the main loop

- **Accept**: a probe library over four families (flow, evidence, delegation, definition);
  probes cite data or record "checked, quiet"; findings become bets with benefit hypotheses,
  baselines, and kill criteria; adoption is a separate act requiring a human decision, a
  change-log line, and a watch period; shrinking the machinery is an allowed bet.
- **Realised**: `flow-driven-evolve`, `references/loop-probes.md`, `templates/improvement.md`.

### R15 — Tree and scale patterns

- **Accept**: rollups with expand/collapse where a viewing choice never changes WIP; rollup
  position derived from the least-advanced child; explicit zoom levels with different units
  and audiences; split-and-join with a stated join condition; shared steps modelled as waits
  or as their own stream; replicated flows with one shared definition; collapse-to-promise at
  stream boundaries, expressed as a percentile range.
- **Realised**: `references/scaled-flow-patterns.md`, `parent`/`children`,
  `flow_defs.rollup_position`, `flow_board.py --expand`.

### R16 — A systems read inspired by, not copied from, the Kanban Method

- **Accept**: an original nine-move start-up sequence covering dissatisfaction, the unit of
  value, demand, capability and constraint, the graph, exits, delegation and run models,
  policies and cadences, measures and system of record; credits its inspiration; adds what
  STATIK never had to address — the agentic unit question, delegation, evidence, and context.
- **Realised**: `flow-driven-define` § The Systems Read.

### R17 — Assumes complex knowledge work: evidence-based steering, discovery-first

- **Accept**: exit evidence is a first-class, enforced concept; optional discovery/probe steps
  before points of last return, with skipping as a recorded decision; a "stop" result treated
  as a win; claims labelled evidence or opinion; verification independent of the doer;
  metrics that refuse to reward activity.
- **Realised**: `evidence_exits`/`evidence_exits_met` + linter, `derisk-first` class,
  `verify_with`, archetype exits, `references/measurement.md`.

### R18 — An evolutionary path for adoption and for human roles

- **Accept**: named stages from "make the flow explicit" to "the platform is the product",
  each with its move, its readiness signal, and the human role it produces (steward → editor
  → verifier → decision-maker → designer); an explicit list of what never delegates and why;
  every stage a legitimate resting place; the path applies per step, not per organisation.
- **Realised**: `references/evolution-path.md`, the delegation stance in `templates/workflow.md`.

### R19 — Encourages building platforms that scale human leverage

- **Accept**: a first-class `platform/` with context packs, checks, and run refs; the rule
  that every question an agent must ask a human is a missing context artifact; packs carry
  provenance, review dates, and a rot signal; `questions-to-human` and escalation rate as the
  platform's headline measures; the loop that feeds outcomes back into the packs.
- **Realised**: `platform/` in the contract, `templates/context-pack.md`,
  `references/evolution-path.md` § the platform play, the example's `learn` → `audience-map` loop.

### R25 — Discovery by interview, with archetype matching

Adapting to a workflow must begin by *finding* it, not by offering a menu.

- **Accept**: an interview protocol anchored to the last real item rather than to "the
  process"; a question ladder that yields the unit, boundaries, queues, back-edges, decision
  points, context packs, classes of service, and failure modes; listening rules (passive
  voice, "usually", the nag, waiting described as working); rules for turning a transcript
  into a draft graph with per-element provenance (observed / stated / inferred); archetype
  matching on **failure mode and evidence shape**, with three outcomes — propose an
  archetype, split into two streams, or go custom — always presented as a proposal with an
  alternative; agent-led mode produces a draft plus the five questions that would most change
  it; a written discovery record that preserves unresolved disagreements verbatim.
- **Realised**: `references/discovery-interview.md`, `flow-driven-define` (Discover path).

### R26 — First-principles derivation when no workflow exists

When nothing formal exists, the framework must teach *why* work this way before *how*.

- **Accept**: a derivation that starts from who is worse off if the stream stops; steps
  derived by asking what has to become **true** (a step retires a distinct kind of doubt),
  not by naming activities; a rationale table giving each mechanism its claim, the cost of
  omitting it, and its smallest starting version; the common objections answered honestly
  ("this is bureaucracy", "our work is too creative", "we already know how we work", "the
  agent can figure it out"); an explicit "when not to formalise"; and a smallest honest
  starting workflow that runs immediately and grows only on evidence.
- **Realised**: `references/first-principles.md`, `flow-driven-define` (Derive path).

### R27 — An explicit, outcome-oriented unit of value

The framework must force a decision about what flows, and push it toward an outcome.

- **Accept**: `unit` declared in the machine-readable config, with a **missing unit as a lint
  violation**, and `unit_outcome` (what changes, for whom) as a warning; five tests for a
  good unit; a catalogue of wrong units (task, artefact, batch, ticket, ceremony, person's
  work, project) each with its board-level tell; right-sizing guidance tied to the loop
  cadence, with rollups for containers; per-item outcome hypotheses flagged when missing; and
  changing the unit treated as a redefinition with a new baseline, not an edit.
- **Realised**: `references/unit-of-value.md`, `flow-config.unit` / `unit_outcome`,
  `flow_lint.py`, the board summary line, `templates/workflow.md`.

### Cross-cutting requirements

| Id | Requirement | Accept |
|---|---|---|
| **R20** | Harness-portable | plain markdown + `python3` stdlib; no network in scripts; runs from any file-reading agent; workspace remains usable by hand |
| **R21** | Deterministic projections | same inputs produce the same board; state derived, never reconciled; generated files declared and never hand-edited |
| **R22** | Human decision boundary | decision points enforced mechanically; agents prepare briefs and set `next_decision`; headless mode parks rather than decides |
| **R23** | Self-hosting | the framework's own changes ride its lifecycle: bets, kill criteria, decisions, change log |
| **R24** | Legible failure | violations, warnings, and gaps are surfaced rather than silently defaulted; a known gap on the board beats a clean board that lies |

## 5. Contracts to extract

These are the interfaces the meta-framework must publish and version:

1. **`flow-config`** — the workflow island: the unit of value (`unit`, `unit_outcome`) plus
   the graph (steps, edges, entry, terminal, limits, thresholds, decision points, evidence
   exits).
2. **Step frontmatter** — id, name, type, intent, delegate rung, run model + ref, context
   packs, inputs, exit evidence, verify, escalation, budget, measures, inner graph.
3. **`step-graph`** — inner graph island with a mandatory stop rule.
4. **Item frontmatter** — title, kind, step, step_entered, owner, holder, class, hypothesis,
   evidence_exits_met, parent/children, blocked_by, next_decision, delegate override.
5. **`measure-set`** — declared measures by family.
6. **`integration-map`** — mode, system, field ownership.
7. **`flow-log.csv`** — `date,slug,from_step,to_step`, append-only.
8. **Export payload** — the JSON an adapter consumes.
9. **Run card** — the orchestrator's output contract (rule, why, item, step, run contract,
   exit evidence, candidate edges, what to record) and its exit codes.
10. **Improvement card** — hypothesis, measures, baseline, kill criteria, probe, watch.

Versioning: the islands carry no version today. The extracted framework should add a
`contract: <semver>` key to `flow-config` and refuse to run against a newer major.

## 6. Extraction plan

**What moves to the meta-framework** — `skills/flow-driven*`, `skills/flow-driven/`
(references, templates, scripts, example), and this spec.

**What stays here** — `portfolio-pdlc` and the diagnostic skills, which become *instances*
and *neighbours* of the framework rather than competitors to it.

**The insight to exploit during extraction**: `portfolio-pdlc` is already an instance of this
spec — a portfolio-level development value stream with a fixed archetype.

| portfolio-pdlc | flow-driven |
|---|---|
| `pdlc.md` + `board-config` | `workflow.md` + `flow-config` |
| stages (explore → bau) | steps, as the `development` archetype at portfolio altitude |
| `initiative.md` / `improvement.md` | items / improvement bets |
| decision boundaries | decision points |
| `orientation`, evidence logs | exit evidence + evidence exits |
| leverage table | the run-loop leverage table |
| probe library | loop probes (Families A–D) |
| `portfolio_board.py` | `flow_board.py` (superset: graph, rungs, holders, rollups) |
| — | delegate model, run model, inner graphs, integrations, platform |

**Sequence**:

1. Extract the contract, scripts, and references into the standalone repo; add contract
   versioning (§5) and a conformance test suite keyed to the R-ids.
2. Generalise the scripts where portfolio-pdlc needs them: multi-stream discovery, a stream
   registry, and cross-stream rollups (R15's stream-of-streams).
3. Re-express `portfolio-pdlc` as a flow-driven archetype plus a thin skill layer, keeping
   its language (sponsors, investment decisions, confidence) — the domain vocabulary is the
   product there, not the mechanics.
4. Keep both usable standalone. Nobody should have to adopt the meta-framework to run a
   portfolio, and nobody should have to care about portfolios to run a content pipeline.

**Compatibility**: `flow-log.csv` is shared in shape between both today; keep it that way, so
a portfolio workspace's history survives the migration.

## 7. Open questions

1. **Cross-stream dependencies.** Shared steps are modelled as waits. Should the framework
   model a first-class dependency edge between streams, or is that a portfolio concern?
2. **Contract versioning.** Semver on the islands, or a dated contract with a migration note?
3. **Time in the flow log.** Dates only, today. Do operational streams with sub-day cycle
   times need timestamps, and what does that do to the "editable by hand" property?
4. **Automated measure capture.** Human minutes and cost per item are recorded by hand.
   Worth a harness-side hook, or does that break portability?
5. **Multi-writer reality.** The single-writer rule is right and will be violated. Should the
   framework detect drift between a mirror and its projection, or stay silent by design?
6. **Eval integration.** For `ai-use-case` streams, the eval is the exit evidence. Should
   evals be a first-class entity rather than a check?
7. **How much orchestration is too much?** The selector is deliberately dumb. The moment it
   becomes a scheduler, the "run it by hand" property dies. Where is that line?

## 8. Success criteria for the extracted framework

- A team can go from "we have a process nobody wrote down" to a running loop in a day.
- Two different archetypes run on the same scripts with no forks.
- An existing spec-kit or Kiro setup is absorbed without rewriting anything that worked.
- The meta-loop kills at least one of its own bets within the first quarter — evidence that
  the improvement lane is real rather than a wish list.
- Someone reverts a rung promotion using the demotion criteria, without an argument.
- A user reads the definition of workflow and says "that is what we actually do" — and then
  changes one thing in it.
- A team can state their unit of value in one sentence, and it is a change for somebody
  rather than an artefact they produce.
- A stream with no prior process can explain, unprompted, why it has exit evidence at all.
