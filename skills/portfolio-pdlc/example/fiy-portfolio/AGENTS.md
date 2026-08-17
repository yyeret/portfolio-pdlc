# FlowImpact Yoga Portfolio — Agent Instructions

This folder is a **portfolio workspace** (and a practice instance — see README.md for the
seeded smells) run on the `portfolio-pdlc` operating system in this repo.

## Session start

1. Read `PORTFOLIO.md`, skim `board.md`.
2. Load `skills/portfolio-pdlc.md` from this repo's root and follow its operating loop.
3. Regenerate the board before acting (pass `--today 2026-08-17` for the canonical demo
   flags):

```bash
python3 ../../scripts/portfolio_board.py . --today 2026-08-17
```

## House rules

- One loop cycle = one move (the leverage table picks it).
- Humans decide invest / commit / pivot / kill / reorganize — here, "humans" are Mary, Jim,
  and the eng lead; in practice mode, write the decision brief and stop.
- `board.md` and `flow-log.csv` are generated — never hand-edit.
- Improvement ideas become cards in `improvements/`, not on-the-spot edits.
