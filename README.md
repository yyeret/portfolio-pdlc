# Portfolio PDLC

An AI-native, agentic approach to portfolio management: a product development lifecycle
(PDLC) your coding agents can actually run.

Plain-markdown skills + two small Python scripts turn any folder into a living portfolio
board: initiatives as cards with evidence-verified stages, a generated kanban and flow
metrics, decision briefs for the calls only humans should make, and an improvement lane
where the operating model itself gets treated as a product — with Monte Carlo simulation
as its discovery tool.

Alongside it, **flow-harness**: the same thinking one altitude down, for a single value
stream. Take any workflow — a PDLC, an SDLC, a content pipeline, an AI use-case pipeline, a
support queue — and engineer it into an agentic loop with an explicit definition of
workflow, evidence-based exits, a delegate model and run model per step, and a meta-loop
that adapts the loop itself.

Built by [Yuval Yeret](https://yuvalyeret.com), distilled from portfolio operating systems
developed with large enterprise product organizations, and built spec-driven so agents can
run it. The thinking behind it: [Scaling Product Orgs with Portfolio Agility](https://yuvalyeret.com/blog/scaling-product-organizations-with-portfolio-agility/).

**The story and the why**: [docs/the-ai-native-portfolio.md](docs/the-ai-native-portfolio.md)

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
| `skills/flow-harness.md` | Agentic loop engineering for one value stream: workspace contract, run loop, leverage table |
| `skills/flow-harness-choose.md` | Find the operational and development value streams; pick the one to make agentic first |
| `skills/flow-harness-define.md` | The systems read: steps, graph, exit evidence, delegate + run model per step, policies |
| `skills/flow-harness-ingest.md` | Absorb spec-kit, Kiro, a bespoke harness, or a tracker — wrap, don't rewrite |
| `skills/flow-harness-scaffold.md` | Turn the definition into a working markdown workspace with real stubs |
| `skills/flow-harness-instrument.md` | What to measure, wired into the steps that feed it |
| `skills/flow-harness-integrate.md` | Bind it to GitHub, a Kanban tool, or a dashboard — one writer per field |
| `skills/flow-harness-run.md` | Advance the flow: one move per cycle, under the step's contract |
| `skills/flow-harness-evolve.md` | The meta-loop: probe the loop itself, capture bets, change nothing on the spot |
| `skills/flow-harness/scripts/` | `flow_lint.py`, `flow_board.py`, `flow_next.py` (+ shared `flow_defs.py`) — python3 stdlib |
| `skills/flow-harness/example/fiy-content-engine/` | The same fictional company's content stream, wired as a flow workspace |
| `docs/specs/agentic-flow-harness.md` | The requirement-level spec for the flow-harness meta-framework |

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

## Quickstart: any workflow as an agentic loop

```bash
cd portfolio-pdlc/skills/flow-harness/example/fiy-content-engine
python3 ../../scripts/flow_lint.py  . --today 2026-08-19   # is the workflow definition sound?
python3 ../../scripts/flow_board.py . --today 2026-08-19   # project it
python3 ../../scripts/flow_next.py  . --today 2026-08-19   # what is the ONE next move?
```

`flow_next.py` prints a run card: the rule that fired, the item, the step's full run
contract (delegate rung, run ref, context packs, budget, escalation), the exit evidence to
produce, the edges it may take next, and what to record. Here it routes to a publish
decision that went overdue five days ago — and exits `DECISION-PENDING`, because agents
prepare decisions and humans make them.

Then point your agent at a workflow of your own:

> Load `skills/flow-harness-define.md` and help me define the workflow for <stream>.

Already have spec-kit, Kiro, a homegrown harness, or a tracker full of states? Start with
`skills/flow-harness-ingest.md` — it maps what exists before proposing anything.

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

And in `flow-harness`, three more that fall out of running a stream rather than a portfolio:

5. **Delegation is per step and per evidence.** A six-rung ladder from "human only" to
   "closed-loop automation", set by reversibility and blast radius — never by how impressive
   the model looks this month. Promotions need a shadow run; demotion criteria get written
   before you need them.
6. **A step is finished when its evidence exists.** Not when a run completes. Agents are
   fluent, and fluency reads as completion — exit evidence is the countermeasure.
7. **Every question an agent asks a human is a missing context artifact.** Capture it once
   in the platform and the next run doesn't need the human. That is how leverage compounds.

## Where this comes from

I'm [Yuval Yeret](https://yuvalyeret.com). I help scale-ups and enterprises get traction on
the investments that matter — usually at the portfolio level, where the gap between the
operating model on paper and the one people work in every day does the most damage.

This framework has a lineage. It started as the portfolio agility approach I wrote up in
[Scaling Product Orgs with Portfolio Agility](https://yuvalyeret.com/blog/scaling-product-organizations-with-portfolio-agility/) —
behaviors first, minimum viable process second. It got sharper through building
portfolio operating systems inside large product organizations: a real lifecycle, a real
Tier-1 board, real investment decisions, and the diagnostic habits (sniff tests,
watermelon hunts, evidence over opinion) that keep those decisions honest. Keeping it
honest always took a facilitator walking the board every week. This repo is what happened
when I handed that legwork to agents and kept the decisions with the humans. The story is
in [docs/the-ai-native-portfolio.md](docs/the-ai-native-portfolio.md).

It's open on purpose. Take it, fork it, make the lifecycle yours — that's the point of a
definition of workflow you own. If you're standing this up on a live portfolio and want a
thinking partner for the parts that are organizational rather than technical — altitude,
decision rights, descaling the dependency mess, getting leaders to steer on evidence — I
do that work: [yuvalyeret.com/contact](https://yuvalyeret.com/contact/). And if you run it
somewhere interesting, I'd genuinely like to hear what the first generated board told you.

## License

MIT — see [LICENSE](LICENSE).
