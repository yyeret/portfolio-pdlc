# Portfolio PDLC — Agent Instructions

This repo is a **portfolio-level product development lifecycle (PDLC) operating system
for coding agents**: a set of plain-markdown skills, deterministic scripts, templates,
and a practice portfolio. It works the same from Claude Code, Codex, Gemini CLI /
Antigravity, or any agent that can read files and run `python3`.

## How to work here

1. **Entry point**: read `skills/portfolio-pdlc.md` — the operating loop, the leverage
   table, and the routing to member skills. Load member skills (`skills/<name>.md`) only
   when the loop routes you there; each references companion material in
   `skills/<name>/` (load only what you need).
2. **State lives in card frontmatter.** `board.md` and `flow-log.csv` inside a portfolio
   workspace are generated projections — regenerate them with
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
portfolio with `skills/portfolio-pdlc-wire.md`.

## Conventions

- Skills: entry file at `skills/<name>.md`; companions in `skills/<name>/`
  (`references/`, `templates/`, `scripts/`, `example/`).
- Scripts are `python3` stdlib only; no network, no harness assumptions.
- Sponsor-facing language is confidence and "what you can rely on" — never gates or
  compliance.
