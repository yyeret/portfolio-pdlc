# Portfolio PDLC

A portfolio-level product development lifecycle your coding agents can actually run.

Plain-markdown skills + two small Python scripts turn any folder into a living portfolio
board: initiatives as cards with evidence-verified stages, a generated kanban and flow
metrics, decision briefs for the calls only humans should make, and an improvement lane
where the operating model itself gets treated as a product — with Monte Carlo simulation
as its discovery tool.

Built by [Yuval Yeret](https://yuvalyeret.com), distilled from portfolio operating systems
developed with large enterprise product organizations, and built spec-driven so agents can
run it. The thinking behind it: [Scaling Product Orgs with Portfolio Agility](https://yuvalyeret.com/blog/scaling-product-organizations-with-portfolio-agility/).

**The story and the why**: [docs/the-portfolio-that-learns.md](docs/the-portfolio-that-learns.md)

## What's in the box

| Piece | What it does |
|---|---|
| `skills/portfolio-pdlc.md` | The operating system: workspace contract, one-move-per-cycle loop, leverage table |
| `skills/portfolio-pdlc-wire.md` | Turn whatever an org has (decks, exports, folders) into a wired portfolio workspace |
| `skills/portfolio-pdlc-assess.md` | Stale-status sweep, outcome-vs-activity x-ray, flow + risk-balance read, review brief |
| `skills/portfolio-pdlc-advance.md` | Move ONE initiative toward its next decision; prepare (never make) the human call |
| `skills/portfolio-pdlc-strengthen.md` | Upgrade a card into a steering instrument: outcome hypothesis, leading indicators, evidence-tagged risks |
| `skills/portfolio-pdlc-improve.md` | Probe the process AND the portfolio topology; capture improvement bets, never impulse-edit |
| `skills/portfolio-pdlc-simulate.md` | Deterministic Monte Carlo what-ifs: WIP limits, intake shaping, dependency-tax reduction |
| `skills/sniff-test.md` (+ portfolio add-on) | The diagnostic engine: clarity-vs-stage reads, watermelon hunting, derisking fit |
| `skills/lean-product-canvas-coach.md` | Coach an initiative from fuzzy ambition to testable hypotheses |
| `skills/portfolio-pdlc/scripts/` | `portfolio_board.py` (board/metrics/flow-log) and `portfolio_sim.py` (simulation) — python3 stdlib, no dependencies |
| `skills/portfolio-pdlc/example/fiy-portfolio/` | A fictional scale-up portfolio with deliberately seeded smells to practice on |

## Quickstart (five minutes, no setup)

```bash
git clone https://github.com/yyeret/portfolio-pdlc
cd portfolio-pdlc/skills/portfolio-pdlc/example/fiy-portfolio
python3 ../../scripts/portfolio_board.py . --today 2026-08-17
```

Open `board.md`. Six of ten cards carry flags — an overdue investment decision, a
rubber-stamped commit, an "experiment" that quietly became a rewrite. Then point your
agent at the folder and say:

> Read AGENTS.md and run one cycle of the portfolio-pdlc operating loop.

The leverage table should route it to the overdue decision first. That's the whole idea:
the agent does the clerical and analytical work, a human makes the invest/commit/kill
calls, and every cycle leaves the system a little sharper.

Try a what-if:

```bash
python3 ../../scripts/portfolio_sim.py . --scenario reviews/scenarios/extract-billing-platform.txt
```

## Wiring a real portfolio

1. Open your agent in a fresh folder (or point it at the folder where your initiative
   material already lives).
2. Ask it to load `skills/portfolio-pdlc-wire.md` from this repo and wire the portfolio.
3. It inventories what exists, drafts the charter and workflow definition with you,
   creates one card per significant investment, and generates the first board.
4. From then on, run loop cycles (`skills/portfolio-pdlc.md`) on whatever cadence you
   like — including via your harness's recurring/goal-loop mechanism.

Works from Claude Code, Codex, Gemini CLI / Antigravity, and anything else that reads
files and runs `python3`. Harness pointers: `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`.

## The operating principles

1. **Common language, not gates.** Confidence grows through Explore → Discovery
   (optional) → Plan/Commit → Execute → Rollout (optional) → BAU. The question is never
   "did the ceremony run" — it's "has confidence grown enough for this stage, on evidence."
2. **State is derived, not declared.** Cards carry frontmatter; the board is a
   deterministic projection; stage labels get verified against evidence, because stale
   status is how portfolios lie to themselves.
3. **Humans decide, agents prepare.** Invest, commit, pivot, kill, reorganize — those
   stay human. Everything that makes those decisions well-informed is agent work.
4. **The operating model is a product.** Process and topology improvements are captured
   as bets with kill criteria, derisked (probe, pilot, or simulation), and only then
   adopted. The portfolio manages its own improvement on its own board.

## License

MIT — see [LICENSE](LICENSE).
