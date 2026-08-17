<!-- DRAFT: for Yuval's edit before this repo goes public. -->

# The compounding portfolio

*What happens when your PDLC becomes something agents can run.*

By Yuval Yeret

Picture the monthly portfolio review. Forty slides. Every initiative green. And everyone
in the room knows that slide 23 — the big platform bet — has been green for five months
while the two teams building it quietly renegotiate what "done" means. Nobody's lying,
exactly. The deck is just the last place reality visits.

I've spent years helping scale-ups and enterprises with this. The pattern repeats: the
organization grows, throughput doesn't, and leadership responds by adding process. More
gates, more status reports, more steering committees. Full gas in neutral. The portfolio
runs on reported progress, and reported progress is a claim, not evidence. The evidence
lives somewhere else — in repos, in usage data, in the discovery findings nobody wrote
down — and no human has time to go collect it before every decision.

So decisions wait. And waiting decisions are the most expensive queue in your company.

## The idea I stole

Kieran Klaassen at Every describes [compound engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)
as building systems where each unit of work makes the next one easier: plans live in
files, agents do the work, learnings get captured where the next agent will find them,
and status is derived from what actually exists rather than what someone typed into a
tracker.

Engineers get to work this way now. I kept thinking: portfolio leaders need exactly this,
one level up. The lifecycle I've built with enterprise product organizations — a
product-oriented PDLC where initiatives move Explore → Discovery → Plan/Commit → Execute
→ Rollout → BAU as confidence grows — was always designed around evidence over ceremony.
"Common language, not gates" was the operating principle. But keeping it honest took a
facilitator (often me) walking the board, sniffing initiatives, chasing stale statuses,
prepping decision briefs.

That work is real. It's also exactly the kind of work agents are now good at.

## The portfolio as files

Portfolio PDLC turns a folder into the portfolio's system of record. Every significant
initiative is a card: a markdown file whose frontmatter carries the state (stage, owner,
outcome hypothesis, leading indicators, risk level, dependencies, the next decision and
who owns it) and whose body carries the story — riskiest assumptions tagged as evidence
or opinion, a derisking plan, a decision log with dates and names.

A small script projects those cards into a kanban board and flow metrics. Nobody updates
the board; you regenerate it. If the board disagrees with the cards, the script is wrong.
If the cards disagree with reality, that's a finding — the assess skill verifies every
stage label against what actually exists, because stale status is how portfolios lie to
themselves.

On top of that sit four loops, each one a skill an agent can run:

**Advance.** Take one initiative and grow its confidence toward the next decision. Finish
the canvas, drive the discovery timebox to a proceed-or-stop recommendation, build the
commit package. When it reaches a decision boundary, the agent writes the brief — what
you can rely on, what's still open, what would make us say no — and stops. Invest,
commit, pivot, kill: those calls stay human. The agent's job is making sure they're made
on evidence, on time.

**Compound.** Upgrade the cards themselves. Rewrite "Implement enterprise SSO" into an
outcome someone could steer by. Replace activity counters with leading indicators that
give feedback in weeks and plausibly correlate to the outcome. Tag every confident claim
as evidence or opinion, and put the opinions at the top of the discovery agenda.

**Improve the process.** Probe the operating model against a library of patterns from my
[portfolio agility work](https://yuvalyeret.com/blog/scaling-product-organizations-with-portfolio-agility/):
Do high-risk bets skip discovery by decision or by habit? Are commits rubber-stamped the
same day they're proposed? Does anything ever loop back from BAU, or do surprises hide
there? Fired probes become improvement bets in a backlog. Nothing gets changed on the spot.

**Improve the topology.** The same discipline, aimed at portfolio construction. When one
team's name shows up in most cards' dependency lists, that's your constraint. Options —
extract a platform, embed people, reorganize around the outcome — get compared against
the current state on how much work they'd localize, how big the change is, and what could
go wrong. Then the best one becomes a bet, not a reorg announcement.

One cycle of the operating loop is deliberately small: regenerate the board, pick the
single highest-leverage move, execute it, record what changed, capture at most one
learning. Waiting decisions outrank everything. Committed money outranks ideas. Finishing
outranks starting.

## The part I care most about

Improvement bets don't get implemented when someone has a clever idea in a review. They
get captured as cards — benefit hypothesis, leading indicators, success criteria, kill
criteria — and they ride the same lifecycle as everything else. The operating model is a
product. Its discovery stage has a tool the initiatives don't need: simulation.

The repo ships a small Monte Carlo simulator that learns stage durations from your own
flow history and runs what-ifs. In the bundled example portfolio, there's a bet that
tightening the execute WIP limit from four to three would speed things up. The simulation
says no — at current load the stage isn't full, so the limit buys nothing and adds queue
time. Bet parked, with the evidence attached. The platform-extraction bet, modeled as a
reduction in coordination tax, clears the bar convincingly and earns a real tracer.

A simulator that can tell you your favorite improvement isn't worth it yet is worth more
than one that always agrees with you. Learn before you burn.

## What this isn't

It isn't governance on autopilot. If you let agents advance cards past investment
decisions, you've automated the rubber stamp, which is worse than the manual version.
Every decision boundary in this system requires a dated entry naming a human.

It also isn't a framework to install. It's a minimally viable process around the
behaviors that matter: someone willing to ask "do we have the capacity and the attention
span for this, or should we finish what's in flight?" — and an operating system that puts
the evidence for that conversation on the table every single week, without anyone
building a deck.

## Try it

The [repo](https://github.com/yyeret/portfolio-pdlc) is self-contained: seven skills, the
sniff-test diagnostics, templates, both scripts, and a fictional scale-up portfolio with
deliberately seeded smells. Clone it, regenerate the example board, and point whatever
coding agent you use — Claude Code, Codex, Gemini/Antigravity — at the folder with one
instruction: *run one cycle of the operating loop.*

Watch which move it picks. Then wire your real portfolio and watch the first board it
generates tell you something your slides haven't.

If you try this on a live portfolio, I want to hear what happened —
[yuvalyeret.com/contact](https://yuvalyeret.com/contact/).
