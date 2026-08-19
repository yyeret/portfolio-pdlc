---
name: flow-harness-ingest
description: Adopt a workflow that already exists — GitHub Spec Kit, Kiro, a bespoke prompt/script/cron harness, Claude Code or Codex skill libraries, a Jira/Linear tracker, or an n8n/Temporal automation — and map it into a definition of workflow without rewriting what works. Use when an organisation already has agentic or process machinery and wants it made flow-driven, when documented and actual process have drifted apart, or when deciding whether to wrap, extend, or retire an existing harness. Produces the mapped workflow plus a delta report. Part of the flow-harness family.
metadata:
  tags: flow-agile, agentic-workflow, loop-engineering
  version: 1.0.0
---

# Flow Harness — Ingest

## Outcome

The workflow they *have*, written down and machine-readable, with existing assets bound in
as run refs, checks, and context packs — plus a delta report naming where the documented
process, the actual process, and the automation disagree. Map first; propose second; never
in the same document.

## Inputs

Point at the material: a repo with `.specify/` or `.kiro/`, a folder of prompts and scripts,
skill and command definitions, `CLAUDE.md`/`AGENTS.md`, a tracker export (states plus
transition history for ~100 items), CI config, and the names of two people who run the
process by hand.

## Workflow

1. **Inventory the artefacts.** Every prompt, template, script, checklist, tracker state, CI
   job, hook, connector, doc, and recurring meeting that touches the stream. Do not judge
   them yet.
2. **Trace one real item end to end.** Take a recently finished one and follow it: what
   happened, in what order, who touched it, what waited, what came back. This always
   contradicts the documentation — the contradiction is the most valuable output of the day.
3. **Find the human glue.** The nudges, the "can you look at this", the person who notices
   when something stalls. This is the real control system and it appears in no tool. Write
   it down as steps and escalations; it is usually where the harness adds the most.
4. **Map assets onto the emerging graph** using the recipes in `ingest-recipes.md`:
   - spec-kit: `constitution.md` → context pack; `/specify`,`/plan` → steps with their
     artefacts as exit evidence; `tasks.md` → the inner graph of `build`, not steps.
   - Kiro: steering files → context packs (nearly one-to-one); hooks → automated checks or
     rung-4/5 steps; `requirements.md`/`design.md` → exit evidence.
   - bespoke harness: each automation as trigger → action → artefact → **who checks it**.
     Anything with no checker is running at rung 3 unverified; note it.
   - agent assets: skills and commands → `run_ref`; monolithic `CLAUDE.md` → context packs
     split per step; subagents → inner-graph nodes or the independent verifier.
   - tracker: states → steps, and **transition history → the workflow you actually have**.
   - workflow engines: one step, `run: external`, with the check that guards it.
5. **Diff declared against actual.** States never used, transitions that skip states, the
   state where everything waits, the loop nobody documented, the step that happens but is
   recorded nowhere.
6. **Write `workflow.md` and the step contracts** from the *actual*, and run `flow_lint.py`.
   Gaps stay visible: a step whose exit evidence is genuinely "somebody eyeballs it" gets
   written that way, not aspirationally.
7. **Write the delta report** (`reviews/YYYY-MM-DD-ingest-delta.md`): what exists and where
   it mapped; what is undocumented but real; what is documented but dead; where evidence is
   missing; where autonomy runs unchecked; and three candidate first moves, each reversible.

## Rules

- **Wrap, do not rewrite.** Working prompts, scripts, hooks, and CI become run refs and
  checks. Rewriting them to fit the frame is how adoption dies in week two.
- **Retire only after the replacement has run twice** in parallel.
- **Map, do not invent.** Every step traces to an artefact or a named person's statement.
- **The delta is a finding list, not a redesign.** The humans choose which side of each
  disagreement to change.
- Do not import a tracker's workflow states wholesale because they exist. If they cannot
  express the graph you traced, that is itself the headline finding.
- Automation with no checker gets named plainly, without drama: it is the most common and
  most consequential thing an ingest uncovers.

## Quality Gates

- One real item traced end to end, in writing.
- Every inventoried asset either mapped to a step, listed as unused, or named as out of scope.
- `flow_lint.py` clean on the produced definition.
- The delta report separates observed, documented, and automated — and does not merge them
  into a proposal.
- Existing automation still runs unchanged at the end of the ingest.

## References

- `skills/flow-harness/references/ingest-recipes.md` — the per-tool mappings.
- `skills/flow-harness/references/workflow-definition.md` — the target schema.
- `skills/flow-harness/references/integration-adapters.md` — choosing the system of record next.
- Next: `flow-harness-scaffold` to materialise, or `flow-harness-define` to rework the graph.
