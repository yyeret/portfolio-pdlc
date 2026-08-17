#!/usr/bin/env python3
"""Deterministic portfolio board generator.

Projects card frontmatter (initiatives/ + improvements/) into board.md, appends stage
transitions to flow-log.csv, and computes flow metrics. Stdlib only; no harness assumptions.

Usage:
  python3 portfolio_board.py <portfolio-workspace> [--check] [--quiet] [--today YYYY-MM-DD]

Exit codes: 0 = ok, 1 = contract violations found (use --check to gate a loop cycle),
2 = workspace unusable.
"""

import csv
import re
import sys
from datetime import date, datetime
from pathlib import Path

DEFAULT_CONFIG = {
    "stages": ["explore", "discovery", "plan-commit", "execute", "rollout", "bau"],
    "optional_stages": ["discovery", "rollout"],
    "wip_limits": {"plan-commit": 3, "execute": 4},
    "aging_thresholds": {
        "explore": 30, "discovery": 45, "plan-commit": 30, "execute": 120, "rollout": 45,
    },
    "decision_boundaries": ["plan-commit", "execute"],
}
TERMINAL_STAGES = ["done", "frozen"]
REQUIRED_FIELDS = ["title", "type", "tier", "stage", "stage_entered", "owner"]
EXPLORATION_STAGES = ["explore", "discovery"]
COMMITTED_STAGES = ["plan-commit", "execute", "rollout"]


def parse_frontmatter(text):
    """Tolerant parser for the workspace-contract YAML subset (flat keys, scalar lists)."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None, ["no frontmatter block"]
    data, problems, current_list_key = {}, [], None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        list_item = re.match(r"\s+-\s+(.*)$", raw)
        if list_item and current_list_key:
            data[current_list_key].append(_unquote(list_item.group(1)))
            continue
        kv = re.match(r"([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", raw)
        if not kv:
            problems.append(f"unparsed line: {raw.strip()!r}")
            current_list_key = None
            continue
        key, value = kv.group(1), kv.group(2).strip()
        value = re.sub(r"\s+#.*$", "", value)  # trailing comments
        if value == "":
            data[key], current_list_key = [], key
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [_unquote(v.strip()) for v in inner.split(",") if v.strip()] if inner else []
            current_list_key = None
        else:
            data[key], current_list_key = _unquote(value), None
    return data, problems


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def parse_board_config(pdlc_path):
    config = {k: (dict(v) if isinstance(v, dict) else list(v)) for k, v in DEFAULT_CONFIG.items()}
    if not pdlc_path.exists():
        return config, False
    m = re.search(r"<!--\s*board-config\s*(.*?)-->", pdlc_path.read_text(encoding="utf-8"), re.DOTALL)
    if not m:
        return config, False
    for line in m.group(1).splitlines():
        line = line.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key in ("stages", "optional_stages", "decision_boundaries"):
            config[key] = [v.strip() for v in val.split(",") if v.strip()]
        elif key in ("wip_limits", "aging_thresholds"):
            entries = {}
            for pair in val.split(","):
                if "=" in pair:
                    k2, _, v2 = pair.partition("=")
                    try:
                        entries[k2.strip()] = int(v2.strip())
                    except ValueError:
                        pass
            config[key] = entries
    return config, True


def parse_iso(s):
    try:
        return datetime.strptime(str(s).strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def load_cards(ws, config, today):
    cards, violations = [], []
    for lane, folder in (("initiative", "initiatives"), ("improvement", "improvements")):
        base = ws / folder
        if not base.is_dir():
            continue
        for card_dir in sorted(p for p in base.iterdir() if p.is_dir()):
            path = card_dir / f"{lane}.md"
            if not path.exists():
                violations.append(f"{card_dir.name}: missing {lane}.md")
                continue
            text = path.read_text(encoding="utf-8")
            fm, problems = parse_frontmatter(text)
            if fm is None:
                violations.append(f"{card_dir.name}: {problems[0]}")
                continue
            card = {
                "slug": card_dir.name, "lane": lane, "path": path, "body": text,
                "fm": fm, "flags": [], "parse_problems": problems,
            }
            for field in REQUIRED_FIELDS:
                if not fm.get(field):
                    card["flags"].append(f"missing `{field}`")
            stage = str(fm.get("stage", "")).strip()
            card["stage"] = stage
            if stage and stage not in config["stages"] + TERMINAL_STAGES:
                card["flags"].append(f"unknown stage `{stage}`")
            entered = parse_iso(fm.get("stage_entered"))
            card["age"] = (today - entered).days if entered else None
            if fm.get("stage_entered") and entered is None:
                card["flags"].append("unparsable `stage_entered`")
            try:
                card["tier"] = int(str(fm.get("tier", "")).strip())
            except ValueError:
                card["tier"] = None
            try:
                card["score"] = int(str(fm.get("portfolio_score", "")).strip())
            except ValueError:
                card["score"] = None
            cards.append(card)
    return cards, violations


def update_flow_log(ws, cards, today):
    """Append a row whenever a card's current stage differs from its last logged stage."""
    log_path = ws / "flow-log.csv"
    last = {}
    rows = []
    if log_path.exists():
        with log_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.reader(fh):
                if len(row) >= 4 and row[0] != "date":
                    rows.append(row)
                    last[row[1]] = row[3]
    appended = []
    for card in cards:
        if not card["stage"]:
            continue
        prev = last.get(card["slug"])
        if prev != card["stage"]:
            when = card["fm"].get("stage_entered") or today.isoformat()
            appended.append([str(when), card["slug"], prev or "none", card["stage"]])
    if appended or not log_path.exists():
        with log_path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["date", "slug", "from_stage", "to_stage"])
            w.writerows(rows + appended)
    return rows + appended, appended


def apply_judgment_flags(cards, config, log_rows, today):
    discovered = {r[1] for r in log_rows if r[3] == "discovery"}
    for c in cards:
        fm, stage = c["fm"], c["stage"]
        in_flow = stage in config["stages"]
        if c["tier"] == 1 and in_flow:
            if not fm.get("outcome_hypothesis"):
                c["flags"].append("no outcome hypothesis")
            indicators = fm.get("leading_indicators") or []
            if not indicators:
                c["flags"].append("no leading indicators")
            orientation = str(fm.get("orientation", "")).strip()
            if orientation == "activity":
                c["flags"].append("activity-oriented")
            elif orientation not in ("outcome",):
                c["flags"].append("orientation not yet assessed as outcome")
        threshold = config["aging_thresholds"].get(stage)
        if threshold and c["age"] is not None and c["age"] > threshold:
            c["flags"].append(f"aging {c['age']}d > {threshold}d")
        nd = str(fm.get("next_decision", "")).strip()
        nd_date = parse_iso(nd[:10]) if nd else None
        if nd_date and nd_date < today:
            c["flags"].append(f"decision overdue since {nd_date.isoformat()}")
        if c["tier"] == 1 and c["score"] is not None and c["score"] <= 4:
            c["flags"].append(f"altitude: score {c['score']} on the Tier-1 board")
        if c["tier"] == 2 and c["score"] is not None and c["score"] >= 7:
            c["flags"].append(f"altitude: score {c['score']} sitting in the awareness lane")
        if stage in config["decision_boundaries"]:
            if not re.search(r"##\s*Decision log.*?\d{4}-\d{2}-\d{2}", c["body"], re.DOTALL | re.IGNORECASE):
                c["flags"].append(f"no dated Decision-log entry for `{stage}`")
        if (str(fm.get("risk_level", "")).strip() == "high"
                and stage in ("plan-commit", "execute")
                and c["slug"] not in discovered):
            c["flags"].append("high risk committed with no discovery record")


def compute_metrics(cards, config, log_rows, today):
    in_flow = [c for c in cards if c["stage"] in config["stages"]]
    tier1 = [c for c in in_flow if c["tier"] == 1 and c["lane"] == "initiative"]
    wip = {}
    for stage in config["stages"]:
        wip[stage] = sum(1 for c in tier1 if c["stage"] == stage)
    explore_n = sum(wip[s] for s in EXPLORATION_STAGES if s in wip)
    committed_n = sum(wip[s] for s in COMMITTED_STAGES if s in wip)
    active = explore_n + committed_n
    balance = (round(100 * explore_n / active), round(100 * committed_n / active)) if active else None
    finished = [r for r in log_rows if r[3] in ("bau", "done")]
    throughput = {}
    for r in finished:
        d = parse_iso(r[0])
        if d:
            q = f"{d.year}-Q{(d.month - 1) // 3 + 1}"
            throughput[q] = throughput.get(q, 0) + 1
    entries = {}
    for r in log_rows:
        d = parse_iso(r[0])
        if d:
            entries.setdefault(r[1], []).append((d, r[3]))
    stage_durations = {}
    for slug, seq in entries.items():
        seq.sort()
        for (d1, s1), (d2, _s2) in zip(seq, seq[1:]):
            stage_durations.setdefault(s1, []).append((d2 - d1).days)
    cycle_times = {}
    for stage in config["stages"]:
        samples = stage_durations.get(stage, [])
        if len(samples) >= 3:
            samples = sorted(samples)
            cycle_times[stage] = (samples[len(samples) // 2], len(samples))
    return {"wip": wip, "balance": balance, "throughput": throughput,
            "cycle_times": cycle_times, "tier1": tier1}


def render(ws, cards, config, metrics, violations, today):
    lines = [f"# Portfolio Board — generated {today.isoformat()}", "",
             "> Generated by `portfolio_board.py`. Do not edit — regenerate.", ""]
    tier1 = metrics["tier1"]
    flagged = [c for c in cards if c["flags"]]
    overdue = [c for c in cards if any(f.startswith("decision overdue") for f in c["flags"])]
    lines += ["## Summary", ""]
    limits = ", ".join(f"{k}={v}" for k, v in config["wip_limits"].items()) or "none"
    lines.append(f"- Tier-1 initiatives in flow: **{len(tier1)}** (WIP limits: {limits})")
    for stage, limit in config["wip_limits"].items():
        if metrics["wip"].get(stage, 0) > limit:
            lines.append(f"- **WIP over limit**: `{stage}` at {metrics['wip'][stage]} / {limit}")
    if metrics["balance"]:
        lines.append(f"- Risk balance (Tier-1): **{metrics['balance'][0]}% explore+discovery / "
                     f"{metrics['balance'][1]}% committed**")
    orient = {"outcome": 0, "mixed": 0, "activity": 0, "unset": 0}
    for c in tier1:
        orient[str(c["fm"].get("orientation", "unset")).strip() or "unset"] = \
            orient.get(str(c["fm"].get("orientation", "unset")).strip() or "unset", 0) + 1
    lines.append(f"- Orientation (Tier-1): {orient.get('outcome', 0)} outcome / "
                 f"{orient.get('mixed', 0)} mixed / {orient.get('activity', 0)} activity")
    lines.append(f"- Cards with flags: **{len(flagged)}**; decisions overdue: **{len(overdue)}**; "
                 f"contract violations: **{len(violations)}**")
    lines.append("")

    def table(items):
        out = ["| Card | Title | Age (d) | Owner | Risk | Flags |",
               "|---|---|---|---|---|---|"]
        for c in sorted(items, key=lambda x: -(x["age"] if x["age"] is not None else -1)):
            age = c["age"] if c["age"] is not None else "?"
            flags = "; ".join(c["flags"]) or "—"
            out.append(f"| `{c['slug']}` | {c['fm'].get('title', '?')} | {age} | "
                       f"{c['fm'].get('owner', '?')} | {c['fm'].get('risk_level', '?')} | {flags} |")
        return out

    lines += ["## Flow (Tier-1 initiatives)", ""]
    for stage in config["stages"]:
        items = [c for c in tier1 if c["stage"] == stage]
        limit = config["wip_limits"].get(stage)
        suffix = f" (WIP {len(items)}" + (f" / limit {limit})" if limit else ")")
        lines.append(f"### {stage}{suffix}")
        lines += ([""] + table(items) + [""]) if items else ["", "_empty_", ""]
    terminal = [c for c in cards if c["lane"] == "initiative" and c["stage"] in TERMINAL_STAGES]
    if terminal:
        lines += ["### done / frozen", ""] + table(terminal) + [""]

    improvements = [c for c in cards if c["lane"] == "improvement"]
    lines += ["## Improvement lane (walk the talk)", ""]
    lines += (table(improvements) + [""]) if improvements else ["_empty — run portfolio-pdlc-improve_", ""]

    tier2 = [c for c in cards if c["tier"] == 2 and c["lane"] == "initiative"]
    lines += ["## Awareness lane (Tier-2 — visible, not managed here)", ""]
    lines += (table(tier2) + [""]) if tier2 else ["_empty_", ""]

    lines += ["## Flow metrics", ""]
    if metrics["throughput"]:
        lines.append("- Throughput (cards reaching bau/done): " +
                     ", ".join(f"{q}: {n}" for q, n in sorted(metrics["throughput"].items())))
    else:
        lines.append("- Throughput: insufficient history")
    if metrics["cycle_times"]:
        for stage, (median, n) in metrics["cycle_times"].items():
            lines.append(f"- Time in `{stage}`: median {median}d (n={n})")
    else:
        lines.append("- Stage cycle times: insufficient history (need ≥3 completed passages per stage)")
    lines.append("")

    if violations:
        lines += ["## Contract violations", ""] + [f"- {v}" for v in violations] + [""]
    problems = [(c["slug"], p) for c in cards for p in c["parse_problems"]]
    if problems:
        lines += ["## Data quality", ""] + [f"- `{s}`: {p}" for s, p in problems] + [""]
    (ws / "board.md").write_text("\n".join(lines), encoding="utf-8")
    return len(violations)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    opts = {a for a in argv[1:] if a.startswith("--")}
    today = date.today()
    for a in argv[1:]:
        if a.startswith("--today"):
            today = parse_iso(argv[argv.index(a) + 1] if a == "--today" else a.split("=", 1)[1]) or today
    if not args:
        print(__doc__)
        return 2
    ws = Path(args[0]).resolve()
    if not ws.is_dir():
        print(f"error: {ws} is not a directory")
        return 2
    config, had_config = parse_board_config(ws / "pdlc.md")
    cards, violations = load_cards(ws, config, today)
    if not cards:
        print(f"error: no cards found under {ws}/initiatives or {ws}/improvements")
        return 2
    log_rows, appended = update_flow_log(ws, cards, today)
    apply_judgment_flags(cards, config, log_rows, today)
    metrics = compute_metrics(cards, config, log_rows, today)
    n_violations = render(ws, cards, config, metrics, violations, today)
    if "--quiet" not in opts:
        flagged = sum(1 for c in cards if c["flags"])
        print(f"board.md regenerated: {len(cards)} cards, {flagged} flagged, "
              f"{len(appended)} transition(s) logged"
              + ("" if had_config else " (default board-config — none found in pdlc.md)"))
    if "--check" in opts and (violations or any(c["flags"] for c in cards)):
        return 1 if violations else 0
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
