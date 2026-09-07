# Portfolio PDLC — Agent Instructions

This repo holds **Portfolio PDLC**: a portfolio-level product development lifecycle for
significant investments, evidence-verified stages, and human investment decisions. Its
plain-markdown skills, deterministic scripts, templates, and practice workspace run from
Claude Code, Codex, Gemini CLI / Antigravity, or any agent that can read files and run
`python3`.

The generic single-value-stream framework now lives in the separate
[`flow-driven`](https://github.com/yyeret/flow-driven) repository. It is private while it
is hardened against real workflows and will be public later. Portfolio PDLC is a domain
instance and neighbour of that framework, not its canonical owner.

## How to work here

1. **Entry point**: read `skills/portfolio-pdlc/SKILL.md`. It carries the operating loop,
   leverage table, and routing to member skills. Load member skills
   (`skills/<name>/SKILL.md`) only when the loop routes you there; each references
   companion material alongside it in `skills/<name>/` (load only what you need).
2. **State lives in card frontmatter.** `board.md` and `flow-log.csv` inside a workspace
   are generated projections — regenerate them with
   `skills/portfolio-pdlc/scripts/portfolio_board.py`, never hand-edit.
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
portfolio with `skills/portfolio-pdlc-wire/SKILL.md`.

For a single operational or development value stream, use the practice workspace and
definition skills in [`flow-driven`](https://github.com/yyeret/flow-driven).

## Conventions

- Skills: entry file at `skills/<name>/SKILL.md`; companions alongside it in `skills/<name>/`
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
linear). A failed check or a blocking convention finding is the loop's own material and
routes to a fix round; anything else on the escalation list in §4 of that file leaves the
loop and goes to a human, whatever the round.

Changes to **how this repo works** — conventions here, the quality bar, the review loop —
are captured as bets in `improvements/` with kill criteria, not edited in passing. Same rule
this repo gives everyone else; see `improvements/README.md` for the lane and how to run it.

That is this repo running its own delegation ladder on itself: merging sits at rung 4 —
the agent runs it, the quality bar is the independent check that makes it safe, and the
escalation list is the `escalate_when`. The verifier is never the doer.

## Framework relationship

The requirement-level Flow-Driven specification and generic contracts are canonical in
[`yyeret/flow-driven`](https://github.com/yyeret/flow-driven). Changes needed by Portfolio
PDLC should be raised there as evidence-backed framework improvements rather than copied
into this repository.
