#!/usr/bin/env python3
"""Project a flow workspace into board.md, append transitions, and compute flow metrics.

Deterministic: same inputs, same board. Card frontmatter is the state; this is the
projection. Rollup items are collapsed by default — expand them deliberately.

Usage:
  python3 flow_board.py <flow-workspace> [options]

  --today YYYY-MM-DD   pin "today" for reproducible ages and flags
  --expand SLUG        expand this rollup's children (repeatable; --expand all for every one)
  --export json|csv    also write exports/flow-export.{json,csv} for an integration adapter
  --quiet              suppress the summary line

Exit codes: 0 = board written, 2 = workspace unusable (run flow_lint.py for the why).
"""

import csv
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import flow_defs as fd  # noqa: E402

TERMINAL_HOLDERS = ("blocked", "waiting-decision")


def flag_items(data):
    cfg, steps, today = data["config"], data["steps"], data["today"]
    for item in data["items"]:
        if not fd.in_flow(cfg, item):
            continue
        step = steps.get(item["step"])
        rung = fd.effective_rung(steps, item)
        threshold = cfg["aging_thresholds"].get(item["step"])
        if threshold and item["age"] is not None and item["age"] > threshold:
            item["flags"].append(f"aging {item['age']}d > {threshold}d")
        nd = item["next_decision"]
        nd_date = fd.parse_iso(nd[:10]) if nd else None
        if nd_date and nd_date < today:
            item["flags"].append(f"decision overdue since {nd_date.isoformat()}")
        if item["blocked_by"]:
            item["flags"].append(f"blocked: {item['blocked_by']}")
        if rung is not None:
            if item["holder"] == "agent" and rung <= 1:
                item["flags"].append(f"agent holding a rung-{rung} step")
            if item["holder"] == "human" and rung >= 4:
                item["flags"].append(f"human holding a rung-{rung} step — leverage leak")
        if item["override"] is not None and step and step["rung"] is not None \
                and item["override"] != step["rung"]:
            item["flags"].append(f"delegate override {item['override']} (step default {step['rung']})")
        if item["step"] != cfg["entry"] and not item["fm"].get("outcome_hypothesis") \
                and item["kind"] != "rollup":
            item["flags"].append("no outcome hypothesis past intake")
        for row in fd.transitions_for(data["log_rows"], item["slug"]):
            if row[2] in cfg["evidence_exits"] and row[2] not in item["evidence_met"]:
                item["flags"].append(f"unevidenced exit from `{row[2]}`")


def compute_metrics(data):
    cfg, steps, items, log_rows = data["config"], data["steps"], data["items"], data["log_rows"]
    flowing = [i for i in items if fd.in_flow(cfg, i) and i["kind"] != "rollup"]
    wip = {sid: sum(1 for i in flowing if i["step"] == sid) for sid in cfg["steps"]}
    holders = {}
    for i in flowing:
        holders[i["holder"] or "unset"] = holders.get(i["holder"] or "unset", 0) + 1
    rungs = {}
    for i in flowing:
        r = fd.effective_rung(steps, i)
        key = r if r is not None else "unset"
        rungs[key] = rungs.get(key, 0) + 1
    step_rungs = {}
    for s in steps.values():
        key = s["rung"] if s["rung"] is not None else "unset"
        step_rungs[key] = step_rungs.get(key, 0) + 1

    throughput, entries, rework, total_moves = {}, {}, {}, {}
    for row in log_rows:
        d = fd.parse_iso(row[0])
        if not d:
            continue
        entries.setdefault(row[1], []).append((d, row[3]))
        if row[2] != "none":
            total_moves[row[2]] = total_moves.get(row[2], 0) + 1
            if fd.is_rework(cfg, row[2], row[3]):
                rework[row[2]] = rework.get(row[2], 0) + 1
        if row[3] in cfg["terminal"]:
            key = f"{d.year}-{d.month:02d}"
            throughput[key] = throughput.get(key, 0) + 1
    durations = {}
    for seq in entries.values():
        seq.sort()
        for (d1, s1), (d2, _s2) in zip(seq, seq[1:]):
            durations.setdefault(s1, []).append((d2 - d1).days)
    cycle_times = {}
    for sid in cfg["steps"]:
        samples = sorted(durations.get(sid, []))
        if len(samples) >= 3:
            cycle_times[sid] = (samples[len(samples) // 2], len(samples))

    exits, evidenced = 0, 0
    for row in log_rows:
        item = data["by_slug"].get(row[1])
        if item and row[2] in cfg["evidence_exits"]:   # history without a card predates the contract
            exits += 1
            if row[2] in item["evidence_met"]:
                evidenced += 1
    waiting = sum(1 for i in flowing if i["holder"] in TERMINAL_HOLDERS)
    return {
        "wip": wip, "flowing": flowing, "holders": holders, "rungs": rungs,
        "step_rungs": step_rungs, "throughput": throughput, "cycle_times": cycle_times,
        "rework": rework, "total_moves": total_moves,
        "evidence_coverage": (evidenced, exits),
        "waiting_share": (waiting, len(flowing)),
    }


def load_improvements(ws):
    out = []
    base = ws / "improvements"
    if not base.is_dir():
        return out
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        path = d / "improvement.md"
        if not path.exists():
            continue
        fm, _ = fd.parse_frontmatter(path.read_text(encoding="utf-8"))
        out.append({"slug": d.name, "fm": fm or {}})
    return out


def item_row(item, data, indent=""):
    rung = fd.effective_rung(data["steps"], item)
    rung_txt = "?" if rung is None else str(rung)
    age = item["age"] if item["age"] is not None else "?"
    flags = "; ".join(item["flags"]) or "—"
    return (f"| {indent}`{item['slug']}` | {item['fm'].get('title', '?')} | {age} | "
            f"{item['owner'] or '?'} | {item['holder'] or '?'} | {rung_txt} | {item['klass']} | {flags} |")


def render(data, expand, metrics):
    cfg, steps, today = data["config"], data["steps"], data["today"]
    by_slug = data["by_slug"]
    name = cfg["id"] or data["ws"].name
    lines = [f"# Flow Board — {name} — generated {today.isoformat()}", "",
             "> Generated by `flow_board.py`. Do not edit — regenerate.", ""]

    flowing = metrics["flowing"]
    flagged = [i for i in data["items"] if i["flags"]]
    overdue = [i for i in data["items"] if any(f.startswith("decision overdue") for f in i["flags"])]
    lines += ["## Summary", ""]
    limits = ", ".join(f"{k}={v}" for k, v in cfg["wip_limits"].items()) or "none declared"
    lines.append(f"- Items in flow: **{len(flowing)}** across {len(cfg['steps'])} steps (WIP limits: {limits})")
    over = [(sid, metrics["wip"][sid], cfg["wip_limits"][sid])
            for sid in cfg["wip_limits"] if metrics["wip"].get(sid, 0) > cfg["wip_limits"][sid]]
    for sid, n, limit in over:
        lines.append(f"- **WIP over limit**: `{sid}` at {n} / {limit} — finish before starting")
    holder_txt = ", ".join(f"{k}: {v}" for k, v in sorted(metrics["holders"].items())) or "—"
    lines.append(f"- Held by: {holder_txt}")
    waiting, total = metrics["waiting_share"]
    if total:
        lines.append(f"- Waiting (blocked or waiting-decision): **{waiting}/{total}** "
                     f"({round(100 * waiting / total)}% of items in flow)")
    rung_txt = ", ".join(f"rung {k}: {v}" for k, v in sorted(metrics["rungs"].items(), key=lambda x: str(x[0])))
    lines.append(f"- Delegation of items in flow: {rung_txt or '—'}")
    ev_ok, ev_total = metrics["evidence_coverage"]
    lines.append(f"- Evidence coverage at evidence exits: **{ev_ok}/{ev_total}**"
                 + (f" ({round(100 * ev_ok / ev_total)}%)" if ev_total else " (no exits logged yet)"))
    lines.append(f"- Items with flags: **{len(flagged)}**; decisions overdue: **{len(overdue)}**")
    lines.append("")

    header = ["| Item | Title | Age (d) | Owner | Holder | Rung | Class | Flags |",
              "|---|---|---|---|---|---|---|---|"]
    lines += ["## Flow", ""]
    for sid in cfg["steps"]:
        step = steps.get(sid, {})
        fm = step.get("fm", {})
        here = [i for i in data["items"] if i["step"] == sid and i["kind"] != "rollup"
                and not (i["parent"] and i["parent"] in by_slug)]
        rollups = [i for i in data["items"] if i["kind"] == "rollup"
                   and (fd.rollup_position(cfg, i, by_slug)[0] or {}).get("step") == sid]
        limit = cfg["wip_limits"].get(sid)
        # WIP counts every item at this step, including collapsed children — a viewing
        # choice must never change the physical fact of how much work is in progress.
        wip_txt = f"WIP {metrics['wip'].get(sid, 0)}" + (f" / {limit}" if limit else "")
        rung = step.get("rung")
        tags = []
        if sid in cfg["decision_points"]:
            tags.append("decision point")
        if sid in cfg["evidence_exits"]:
            tags.append("evidence exit")
        if sid in cfg["optional_steps"]:
            tags.append("optional")
        suffix = f" — {', '.join(tags)}" if tags else ""
        lines.append(f"### {sid} · {fm.get('name', sid)} ({wip_txt}, rung "
                     f"{rung if rung is not None else '?'}{suffix})")
        lines.append("")
        if not here and not rollups:
            lines += ["_empty_", ""]
            continue
        lines += header
        for item in sorted(here, key=lambda x: -(x["age"] if x["age"] is not None else -1)):
            lines.append(item_row(item, data))
        for rollup in rollups:
            _pos, kids = fd.rollup_position(cfg, rollup, by_slug)
            spread = {}
            for k in kids:
                spread[k["step"]] = spread.get(k["step"], 0) + 1
            dist = ", ".join(f"{k}: {v}" for k, v in sorted(spread.items(), key=lambda x: fd.step_index(cfg, x[0])))
            lines.append(item_row(rollup, data))
            if expand == "all" or rollup["slug"] in expand:
                for k in kids:
                    lines.append(item_row(k, data, indent="↳ "))
            else:
                lines.append(f"| ↳ _{len(kids)} children_ | _{dist}_ |  |  |  |  |  | _collapsed — "
                             f"`--expand {rollup['slug']}`_ |")
        lines.append("")

    terminal = [i for i in data["items"] if i["step"] in cfg["terminal"]]
    if terminal:
        lines += ["### terminal", ""] + header
        lines += [item_row(i, data) for i in terminal] + [""]

    improvements = load_improvements(data["ws"])
    lines += ["## Meta-loop bets (the workflow improving itself)", ""]
    if improvements:
        lines += ["| Bet | Title | Stage | Owner | Kill criteria |", "|---|---|---|---|---|"]
        for imp in improvements:
            fm = imp["fm"]
            kill = "yes" if fm.get("kill_criteria") else "**missing**"
            lines.append(f"| `{imp['slug']}` | {fm.get('title', '?')} | {fm.get('stage', '?')} | "
                         f"{fm.get('owner', '?')} | {kill} |")
        lines.append("")
    else:
        lines += ["_empty — run flow-harness-evolve_", ""]

    lines += ["## Metrics", ""]
    if metrics["throughput"]:
        lines.append("- Throughput (items reaching a terminal state): "
                     + ", ".join(f"{k}: {v}" for k, v in sorted(metrics["throughput"].items())))
    else:
        lines.append("- Throughput: nothing has finished yet")
    if metrics["cycle_times"]:
        for sid, (median, n) in metrics["cycle_times"].items():
            lines.append(f"- Time in `{sid}`: median {median}d (n={n})")
    else:
        lines.append("- Time in step: insufficient history (need ≥3 completed passages per step)")
    if metrics["rework"]:
        for sid, n in sorted(metrics["rework"].items(), key=lambda x: -x[1]):
            total_moves = metrics["total_moves"].get(sid, 0)
            share = f" ({round(100 * n / total_moves)}% of exits)" if total_moves else ""
            lines.append(f"- Rework out of `{sid}`: {n} back-edge traversal(s){share}")
    else:
        lines.append("- Rework: no back-edge traversals logged")
    autonomy = ", ".join(f"rung {k}: {v}" for k, v in sorted(metrics["step_rungs"].items(), key=lambda x: str(x[0])))
    lines.append(f"- Autonomy profile (steps by rung): {autonomy or '—'}")
    lines.append("")

    problems = data["problems"] + [f"`{i['slug']}`: {p}" for i in data["items"] for p in i["problems"]]
    if problems:
        lines += ["## Data quality", ""] + [f"- {p}" for p in problems] + [""]
    lines += ["---", "", "Run `flow_lint.py` for contract violations and `flow_next.py` for the next move.", ""]
    return "\n".join(lines)


def export(data, metrics, fmt):
    ws, cfg = data["ws"], data["config"]
    out_dir = ws / "exports"
    out_dir.mkdir(exist_ok=True)
    rows = []
    for item in data["items"]:
        rows.append({
            "slug": item["slug"], "title": item["fm"].get("title", ""), "step": item["step"],
            "step_entered": str(item["fm"].get("step_entered", "")), "age_days": item["age"],
            "owner": item["owner"], "holder": item["holder"],
            "rung": fd.effective_rung(data["steps"], item), "class": item["klass"],
            "kind": item["kind"], "parent": item["parent"], "blocked_by": item["blocked_by"],
            "next_decision": item["next_decision"], "flags": "; ".join(item["flags"]),
        })
    if fmt == "csv":
        path = out_dir / "flow-export.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["slug"])
            w.writeheader()
            w.writerows(rows)
        return path
    path = out_dir / "flow-export.json"
    payload = {
        "workflow": {"id": cfg["id"], "kind": cfg["kind"], "steps": cfg["steps"],
                     "terminal": cfg["terminal"], "generated": data["today"].isoformat()},
        "wip": metrics["wip"], "wip_limits": cfg["wip_limits"],
        "evidence_coverage": {"recorded": metrics["evidence_coverage"][0],
                              "exits": metrics["evidence_coverage"][1]},
        "items": rows,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def main(argv):
    positional, values, flags = fd.parse_cli(argv[1:], value_opts=("today", "export"),
                                             multi_opts=("expand",))
    today = fd.parse_iso(values.get("today")) or date.today()
    expand = set(values.get("expand", []))
    export_fmt = values.get("export")
    if not positional:
        print(__doc__)
        return 2
    ws = Path(positional[0]).resolve()
    if not ws.is_dir():
        print(f"error: {ws} is not a directory")
        return 2
    data = fd.load_workspace(ws, today)
    if data["fatal"]:
        for line in data["fatal"]:
            print(f"error: {line}")
        return 2
    flag_items(data)
    metrics = compute_metrics(data)
    expand_arg = "all" if "all" in expand else expand
    (ws / "board.md").write_text(render(data, expand_arg, metrics), encoding="utf-8")
    exported = export(data, metrics, export_fmt) if export_fmt in ("json", "csv") else None
    if "quiet" not in flags:
        flagged = sum(1 for i in data["items"] if i["flags"])
        msg = (f"board.md regenerated: {len(data['items'])} items, {flagged} flagged, "
               f"{len(data['appended'])} transition(s) logged")
        if exported:
            msg += f"; exported {exported.relative_to(ws)}"
        print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
