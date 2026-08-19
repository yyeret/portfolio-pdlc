#!/usr/bin/env python3
"""Pick the next move in the flow and print its run card.

Deterministic orchestration: a leverage table over the board state, first matching rule
wins, right-to-left inside a rule (most downstream item first, then oldest). The output is
a run card — everything an agent needs to execute exactly one move under the step's
contract, and everything it must record afterwards.

Usage:
  python3 flow_next.py <flow-workspace> [options]

  --today YYYY-MM-DD   pin "today"
  --top N              also list the N highest-ranked candidate moves (default 5)
  --json               machine-readable output for a harness loop
  --skip SLUG          exclude an item from selection (repeatable)

Exit codes: 0 = a move was selected, 3 = nothing to do, 4 = the top move is a human
decision (DECISION-PENDING), 2 = workspace unusable.
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import flow_defs as fd  # noqa: E402
import flow_lint  # noqa: E402
import flow_board  # noqa: E402

RULES = [
    (1, "human decision overdue", "Surface the decision — refresh the brief, notify the named human, "
        "and stop piling work behind it"),
    (2, "definition of workflow broken", "Fix the definition before steering with it — run flow_lint.py "
        "and repair the violations"),
    (3, "item blocked", "Clear the block or escalate it to a named human with a date"),
    (4, "exit evidence missing", "Run the step's verify recipe and record the evidence, or send the item "
        "back across the rework edge"),
    (5, "ready to pull downstream", "Advance it: evaluate the branch condition, move it to the next step, "
        "reset holder and step_entered"),
    (6, "step over WIP limit", "Finish, do not start — run the oldest item in the over-limit step"),
    (7, "item aging in step", "Run the step contract for this item"),
    (8, "item in flow, unrun", "Run the step contract for this item"),
    (9, "intake starved", "Pull one new item into the entry step, or say out loud that demand has dried up"),
    (10, "flowing clean", "Run the meta-loop: flow-driven-evolve"),
]
RULE_TEXT = {n: (name, action) for n, name, action in RULES}


def rank_key(cfg, item):
    """Right-to-left: most downstream first, then oldest."""
    return (-fd.step_index(cfg, item["step"]), -(item["age"] if item["age"] is not None else -1))


def candidates(ws, data, skip):
    cfg, steps = data["config"], data["steps"]
    items = [i for i in data["items"] if fd.in_flow(cfg, i) and i["slug"] not in skip
             and i["kind"] != "rollup"]
    out = []

    def add(rule, item, why):
        out.append({"rule": rule, "item": item, "why": why})

    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        for flag in item["flags"]:
            if flag.startswith("decision overdue"):
                add(1, item, flag)
    violations, _warnings = flow_lint.run_checks(ws, data)
    if violations:
        add(2, None, f"{len(violations)} contract violation(s): {violations[0]}")
    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        if item["blocked_by"]:
            add(3, item, f"blocked: {item['blocked_by']}")
    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        for flag in item["flags"]:
            if flag.startswith("unevidenced exit"):
                add(4, item, flag)
    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        if item["step"] in cfg["evidence_exits"] and item["step"] in item["evidence_met"] \
                and fd.next_steps(cfg, item["step"]):
            add(5, item, f"exit evidence for `{item['step']}` is recorded — it is ready to move")
    over = [sid for sid, limit in cfg["wip_limits"].items()
            if sum(1 for i in items if i["step"] == sid) > limit]
    for sid in sorted(over, key=lambda s: -fd.step_index(cfg, s)):
        here = sorted([i for i in items if i["step"] == sid], key=lambda i: rank_key(cfg, i))
        if here:
            add(6, here[0], f"`{sid}` is over its WIP limit of {cfg['wip_limits'][sid]}")
    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        for flag in item["flags"]:
            if flag.startswith("aging"):
                add(7, item, flag)
    for item in sorted(items, key=lambda i: rank_key(cfg, i)):
        if item["holder"] not in ("waiting-decision", "blocked"):
            add(8, item, f"in `{item['step']}`, held by {item['holder'] or 'nobody'}")
    entry_wip = sum(1 for i in items if i["step"] == cfg["entry"])
    if not items or entry_wip == 0:
        add(9, None, "nothing waiting in the entry step")
    add(10, None, "no rule above fired — the board is flowing")

    seen, deduped = set(), []
    for c in out:
        key = (c["rule"], c["item"]["slug"] if c["item"] else None)
        if key not in seen:
            seen.add(key)
            deduped.append(c)
    deduped.sort(key=lambda c: (c["rule"], rank_key(cfg, c["item"]) if c["item"] else (0, 0)))
    return deduped


def run_card(data, choice):
    cfg, steps = data["config"], data["steps"]
    rule, item, why = choice["rule"], choice["item"], choice["why"]
    name, action = RULE_TEXT[rule]
    lines = [f"## Next move — rule {rule}: {name}", "", f"**Do:** {action}", f"**Why now:** {why}", ""]
    if item is None:
        if rule == 2:
            lines += ["Run `flow_lint.py` on this workspace and fix every violation it prints. "
                      "A loop steered by a broken definition of workflow produces confident nonsense.", ""]
        elif rule == 9:
            lines += ["Check the intake source named in `workflow.md`. If demand is real, pull one item and "
                      "create `items/<slug>/item.md`. If it is not, say so — a starved stream is a finding, "
                      "not an idle moment.", ""]
        else:
            lines += ["Load `flow-driven-evolve` and run one meta-loop pass against the board, the flow log, "
                      "and the loop log.", ""]
        return "\n".join(lines)

    step = steps.get(item["step"], {})
    fm = step.get("fm", {})
    rung = fd.effective_rung(steps, item)
    rung_txt = f"{rung} — {fd.RUNG_NAMES.get(rung, '?')}" if rung is not None else "unset"
    verify = fm.get("verify_with") or "— none declared; grade it with something other than the runner"
    lines += [
        f"**Item:** `{item['slug']}` — {item['fm'].get('title', '?')}",
        f"**Step:** `{item['step']}` · {fm.get('name', '?')} (rung {rung_txt})",
        f"**Owner:** {item['owner'] or '?'} · **holder now:** {item['holder'] or '?'} · "
        f"**class:** {item['klass']} · **age:** {item['age'] if item['age'] is not None else '?'}d",
        "",
        "### Run contract", "",
        f"- **Intent:** {fm.get('intent', '—')}",
        f"- **Run:** `{fm.get('run', '?')}` → `{fm.get('run_ref', '—')}`",
        f"- **Context packs:** {', '.join(step.get('context_packs', [])) or '—'}",
        f"- **Verify with (independent of the runner):** {verify}",
        f"- **Budget:** {fm.get('budget', '— none declared')}",
        f"- **Escalate when:** {fm.get('escalate_when', '—')} → **to:** {fm.get('escalate_to', item['owner'] or '?')}",
        "",
        "### Exit evidence to produce", "",
    ]
    lines += [f"- [ ] {e}" for e in step.get("exit_evidence", [])] or ["- [ ] _step declares no exit evidence — "
                                                                      "that is the first thing to fix_"]
    nexts = fd.next_steps(cfg, item["step"])
    lines += ["", "### Where it can go next", ""]
    for e in nexts:
        tag = f" — {e['tag']}" if e["tag"] else ""
        lines.append(f"- `{item['step']}` → `{e['to']}`{tag}")
    if not nexts:
        lines.append("- _nowhere: this step has no outgoing edge (a contract violation)_")
    if len(nexts) > 1:
        lines.append("")
        lines.append("More than one edge leaves this step: evaluate the branch conditions against evidence "
                     "and record which one you took and why in the item's `## Notes`.")
    if item["step"] in cfg["decision_points"]:
        lines += ["", f"> `{item['step']}` is a decision point. An agent prepares the brief and sets "
                      f"`next_decision`; a named human decides and signs the Decision log."]
    lines += [
        "", "### Record before ending the cycle", "",
        "1. Update the item: `step`, `step_entered`, `holder`, `evidence_exits_met`, and the "
        "`## Exit evidence log` entry with today's date.",
        "2. Re-run `flow_board.py` (it appends the transition to `flow-log.csv`).",
        "3. Append one line to `reviews/loop-log.md`: date · rule fired · item · what changed · what is "
        "pending.",
        "4. Capture at most one learning, and only if it changes how the next cycle behaves.",
        "",
    ]
    return "\n".join(lines)


def main(argv):
    positional, values, flags = fd.parse_cli(argv[1:], value_opts=("today", "top"), multi_opts=("skip",))
    today = fd.parse_iso(values.get("today")) or date.today()
    top_n = fd.as_int(values.get("top"), 5)
    skip = set(values.get("skip", []))
    if not positional:
        print(__doc__)
        return 2
    ws = Path(positional[0]).resolve()
    if not ws.is_dir():
        print(f"error: {ws} is not a directory")
        return 2
    data = fd.load_workspace(ws, today, write_log=False)
    if data["fatal"]:
        for line in data["fatal"]:
            print(f"error: {line}")
        return 2
    flow_board.flag_items(data)
    ranked = candidates(ws, data, skip)
    choice = ranked[0]

    if "json" in flags:
        payload = {
            "rule": choice["rule"], "rule_name": RULE_TEXT[choice["rule"]][0],
            "action": RULE_TEXT[choice["rule"]][1], "why": choice["why"],
            "item": choice["item"]["slug"] if choice["item"] else None,
            "step": choice["item"]["step"] if choice["item"] else None,
            "queue": [{"rule": c["rule"], "rule_name": RULE_TEXT[c["rule"]][0],
                       "item": c["item"]["slug"] if c["item"] else None, "why": c["why"]}
                      for c in ranked[:top_n]],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(run_card(data, choice))
        if top_n and len(ranked) > 1:
            print("### Queue behind it\n")
            for c in ranked[1:top_n + 1]:
                slug = f"`{c['item']['slug']}`" if c["item"] else "—"
                print(f"- rule {c['rule']} ({RULE_TEXT[c['rule']][0]}): {slug} — {c['why']}")
            print("\nOne cycle, one move. Everything else here is the next cycle's problem, or an "
                  "improvement card.\n")

    if choice["rule"] == 1:
        print(f"DECISION-PENDING {choice['item']['slug']}")
        return 4
    if choice["rule"] == 10:
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
