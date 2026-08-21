# Portfolio PDLC — Agent Instructions

This repo holds **operating systems for coding agents, built on flow**: plain-markdown
skills, deterministic scripts, templates, and practice workspaces. Everything works the
same from Claude Code, Codex, Gemini CLI / Antigravity, or any agent that can read files
and run `python3`.

Two families live here:

- **`portfolio-pdlc`** — a portfolio-level product development lifecycle: significant
  investments, evidence-verified stages, human investment decisions.
- **`flow-driven`** — agentic loop engineering for any single value stream (PDLC, SDLC,
  content pipeline, AI use cases, operational request streams): definition of workflow,
  per-step delegate and run models, evidence exits, orchestration, and a meta-loop.

## How to work here

1. **Entry point**: read `skills/portfolio-pdlc.md` for portfolio work, or
   `skills/flow-driven.md` for a single value stream — each carries its operating loop,
   its leverage table, and the routing to member skills. Load member skills
   (`skills/<name>.md`) only when the loop routes you there; each references companion
   material in `skills/<name>/` (load only what you need).
2. **State lives in card frontmatter.** `board.md` and `flow-log.csv` inside a workspace
   are generated projections — regenerate them with
   `skills/portfolio-pdlc/scripts/portfolio_board.py` (portfolio) or
   `skills/flow-driven/scripts/flow_board.py` (flow), never hand-edit.
3. **Humans keep the decisions**: invest, commit, pivot, kill, reorganize. You prepare
   decision briefs; a dated Decision-log entry naming a human is required before any card
   crosses a decision boundary.
4. **One loop cycle = one move.** Resist fan-out; capture everything else as improvement
   cards or loop-log lines.
5. **Improvement ideas are captured, not implemented.** They become cards in the
   workspace's `improvements/` lane and ride the same lifecycle (simulation is their
   Discovery).

## Practice safely

`skills/portfolio-pdlc/example/fiy-portfolio/` is a fictional scale-up portfolio with
deliberately seeded smells (see its README). Run the loop there before wiring a real
portfolio with `skills/portfolio-pdlc-wire.md`.

`skills/flow-driven/example/fiy-content-engine/` is the same fictional company's content
value stream, wired as a flow workspace with its own seeded smells. Run cycles there before
defining a real stream with `skills/flow-driven-define.md`.

## Conventions

- Skills: entry file at `skills/<name>.md`; companions in `skills/<name>/`
  (`references/`, `templates/`, `scripts/`, `example/`).
- Scripts are `python3` stdlib only; no network, no harness assumptions.
- Sponsor-facing language is confidence and "what you can rely on" — never gates or
  compliance.
- A step or stage is finished when its **evidence** exists, not when a run completes.
- Changes to a definition of workflow are captured as bets with kill criteria, never edited
  in passing.

## Shipping changes here

Changes reach `main` through a pull request, and the PR is reviewed against
`docs/quality-bar.md` by an **independent reviewer** — a fresh context that did not write
the change — before it merges. Review is a bounded loop: review → fix the blocking findings
→ re-review, at most three rounds, then merge on a clean verdict (rebase, so history stays
linear). Anything on the escalation list in §4 of that file leaves the loop and goes to a
human instead, whatever the round.

That is this repo running its own delegation ladder on itself: merging sits at rung 4 —
the agent runs it, the quality bar is the independent check that makes it safe, and the
escalation list is the `escalate_when`. The verifier is never the doer.

## Specs

`docs/specs/flow-driven.md` is the requirement-level spec for the flow-driven
meta-framework — the thing to be extracted from this repo later, of which `portfolio-pdlc`
is one instance. Keep it in step with what `skills/flow-driven*` actually does; requirement
ids (`R1`…`R27`) are stable and referenced by the extraction plan.
