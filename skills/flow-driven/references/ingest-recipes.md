# Ingest Recipes — working with the workflow that already exists

Nobody starts empty. There is a spec-kit setup, a Kiro project, a bespoke harness of prompts
and cron jobs, a tracker with fifteen states, and — always — an undocumented layer of human
glue that is doing most of the real coordination.

Three rules before any recipe:

1. **Map, do not invent.** The first deliverable is the workflow they *have*, including the
   parts nobody wrote down. Proposals come after, and separately.
2. **Wrap, do not rewrite.** Existing prompts, scripts, templates, and CI become `run_ref`s
   and `verify_with`s. Rewriting working automation to fit a new frame is how adoption dies
   in week two.
3. **Retire only after the replacement has run twice.** Parallel running is cheap; a gap in
   an operational stream is not.

## The universal method

1. **Inventory the artefacts.** Every prompt, template, script, checklist, tracker state,
   CI job, doc, and recurring meeting that touches the stream.
2. **Trace one real item end to end.** Pick a recently finished one and follow it: what
   happened, in what order, who touched it, what waited. This always contradicts the
   documented process, and the contradiction is the finding.
3. **Find the human glue.** The nudges, the "can you look at this", the person who notices
   things. This is the workflow's real control system and it is invisible in every tool.
4. **Draw the graph from the trace**, not from the documentation.
5. **Name exit evidence from what already convinces people.** Someone already knows when a
   step is really done — usually the person who gets annoyed when it is not. Write down what
   they check.
6. **Bind existing assets** as `run_ref` / `verify_with` / context packs.
7. **Write the delta** — where the documented and the observed workflow differ — as findings,
   not as fixes. The org decides which one to change.

## Recipe: GitHub Spec Kit

**What it is**: `/specify`, `/plan`, `/tasks`, `/implement` slash commands over a `specs/`
directory, a `constitution.md`, and per-feature spec/plan/tasks files.

| Spec Kit | Maps to |
|---|---|
| `constitution.md` | a context pack (`platform/context/constitution.md`) loaded by most steps |
| `/specify` + `spec.md` | the `shape` step; `spec.md` is its exit evidence |
| `/plan` + `plan.md` | the `commit` step's decision brief; `plan.md` is evidence, the decision is human |
| `/tasks` + `tasks.md` | the inner graph of `build`, not a set of steps — tasks are how one item gets done |
| `/implement` | `build`'s run model: `run: skill`, `run_ref: /implement` |

Spec Kit is a strong **within-item** pipeline and has no opinion about the flow *between*
items — no WIP, no aging, no decision points, no measurement. That is exactly the gap
flow-driven fills, so keep spec-kit for the item and add the flow around it. Its
`spec.md`/`plan.md` files are unusually good exit evidence: specific, checkable, already
part of the team's habit.

## Recipe: Kiro

**What it is**: spec-driven IDE flow with `requirements.md` / `design.md` / `tasks.md`,
plus *steering files* and *agent hooks*.

| Kiro | Maps to |
|---|---|
| steering files | context packs — near one-to-one; keep the files, add provenance and a review date |
| `requirements.md` | `shape` exit evidence |
| `design.md` | `commit` decision brief input |
| `tasks.md` | `build`'s inner graph |
| agent hooks (on save, on commit) | rung-4/5 steps or automated `verify_with` |

Kiro's hooks are the most valuable thing to bring across: they are already automated checks
with a trigger, which is precisely what promotes a step up the ladder. Inventory them and
name each as the `verify_with` of the step it actually guards.

## Recipe: a bespoke harness (prompts, scripts, cron)

The common shape: a folder of prompts, a few scripts, a scheduled job, and a person who
knows which order to run them in.

1. List each automation as **trigger → action → artefact → who checks it**.
2. Anything with no "who checks it" is running at rung 3 with no verification. Note it; that
   is usually the first real finding.
3. Cron-triggered jobs are rung 5 candidates *if* they have a check, and unsupervised risk
   if they do not.
4. The order the person knows becomes the graph. Ask what they do when it fails — that is
   your back-edge and your escalation contract, and it is never documented.

## Recipe: Claude Code / Codex / agent assets

Skills, slash commands, subagents, `CLAUDE.md` / `AGENTS.md`, hooks, MCP servers.

| Asset | Maps to |
|---|---|
| skill or slash command | `run: skill`, `run_ref: <name>` |
| `CLAUDE.md` / `AGENTS.md` sections | context packs, split by what each step actually needs |
| hooks | automated checks (`verify_with`) or rung-5 steps |
| subagents | inner-graph nodes, or the independent verifier — the fresh context is the point |
| MCP tools | the `tools allowed` list in a run contract |

A monolithic `CLAUDE.md` loaded by everything is a context pack that has not been split yet.
Splitting it per step is usually a fast, visible quality win.

## Recipe: a tracker (Jira / Linear / Azure DevOps)

1. Export the workflow states — that is the *declared* workflow.
2. Export transition history for the last 100 items — that is the *actual* workflow.
3. Diff them. States never used, transitions that skip states, the state where everything
   waits, the loop nobody documented. This diff is the most useful artefact in the whole
   ingest, and it takes an afternoon.
4. Build the graph from the actual, then hold one conversation about each difference.
5. Then decide the integration mode (`adopt` / `mirror` / `split`) — see
   `integration-adapters.md`.

## Recipe: workflow engines (n8n, Zapier, Airflow, Temporal)

These are already rung-5 steps with real reliability engineering behind them. Do not port
them. Model each as one step with `run: external`, name the artefact it produces, and put
the check that guards it in `verify_with`. The value you add is the *flow* around them:
what waits, what decides, what nobody is measuring.

## The delta report

Ingest ends with a written delta, not a redesign:

- **What exists**, mapped into the definition of workflow.
- **What is undocumented but real** — the human glue, the informal escalations.
- **What is documented but dead** — states nobody uses, steps nobody runs.
- **Where evidence is missing** — steps that end on assertion.
- **Where autonomy is running unchecked** — automation with no verification.
- **Three candidate first moves**, each reversible.

Hand it over. Let the humans choose. An ingest that ends in a unilateral redesign is a
consultant's deliverable, not an operating system.
