#!/usr/bin/env python3
"""Shared parsing and model for the flow-driven scripts.

Reads a flow workspace as defined in ../references/workflow-definition.md:
the flow-config graph in workflow.md, the step contracts in steps/, the items in
items/, and the generated flow-log.csv. Stdlib only; no network, no harness assumptions.

Not a CLI — used by flow_lint.py, flow_board.py, and flow_next.py, which live beside it.
"""

import csv
import re
from datetime import datetime
from pathlib import Path

STEP_TYPES = ["intake", "transform", "decision", "verify", "wait", "measure"]
RUN_MODELS = ["skill", "prompt", "script", "tool", "human", "external"]
HOLDERS = ["human", "agent", "pair", "blocked", "waiting-decision"]
ITEM_KINDS = ["item", "rollup", "spike"]
CLASSES = ["standard", "expedite", "fixed-date", "derisk-first"]
STEP_REQUIRED = ["id", "name", "type", "intent", "delegate_rung", "run", "exit_evidence"]
ITEM_REQUIRED = ["title", "kind", "step", "step_entered", "owner", "holder"]
RUNG_NAMES = {
    0: "human only",
    1: "agent assists",
    2: "agent drafts, human edits",
    3: "agent runs, human verifies exit",
    4: "agent runs, checked automatically, human on exception",
    5: "closed-loop automation",
}


# --------------------------------------------------------------------------- parsing

def parse_frontmatter(text):
    """Tolerant parser for the contract's YAML subset: flat keys, scalar lists."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None, ["no frontmatter block"]
    data, problems, current_list_key = {}, [], None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        list_item = re.match(r"\s+-\s+(.*)$", raw)
        if list_item and current_list_key:
            data[current_list_key].append(unquote(list_item.group(1)))
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
            data[key] = [unquote(v.strip()) for v in inner.split(",") if v.strip()] if inner else []
            current_list_key = None
        else:
            data[key], current_list_key = unquote(value), None
    return data, problems


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def parse_iso(s):
    try:
        return datetime.strptime(str(s).strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def as_int(value, default=None):
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def parse_cli(argv, value_opts=(), multi_opts=()):
    """Tiny CLI parser: returns (positional, values, flags).

    `--key value` and `--key=value` both work; options in `multi_opts` accumulate a list.
    """
    positional, values, flags = [], {}, set()
    multi_opts = set(multi_opts)
    value_opts = set(value_opts) | multi_opts
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg.startswith("--"):
            key, eq, inline = arg[2:].partition("=")
            if key in value_opts:
                val = inline if eq else (argv[i + 1] if i + 1 < len(argv) else "")
                if not eq:
                    i += 1
                if key in multi_opts:
                    values.setdefault(key, []).append(val)
                else:
                    values[key] = val
            else:
                flags.add(key)
        else:
            positional.append(arg)
        i += 1
    return positional, values, flags


def read_block(text, name):
    """Return the body of an <!-- name ... --> island, or None."""
    m = re.search(r"<!--\s*" + re.escape(name) + r"\s*\n(.*?)-->", text, re.DOTALL)
    return m.group(1) if m else None


def parse_edges(block_text):
    """`from -> to [tag: note]` lines anywhere inside a config block."""
    edges = []
    for line in block_text.splitlines():
        m = re.match(r"\s*([A-Za-z0-9][\w-]*)\s*->\s*([A-Za-z0-9][\w-]*)\s*(?:\[(.*?)\])?\s*$", line)
        if m:
            edges.append({"from": m.group(1), "to": m.group(2), "tag": (m.group(3) or "").strip()})
    return edges


# ------------------------------------------------------------------------ flow config

def load_config(ws):
    """Parse workflow.md's flow-config island. Returns (config, problems)."""
    problems = []
    path = ws / "workflow.md"
    if not path.exists():
        return None, ["workflow.md not found — this is not a flow workspace (run flow-driven-scaffold)"]
    text = path.read_text(encoding="utf-8")
    block = read_block(text, "flow-config")
    if block is None:
        return None, ["workflow.md has no <!-- flow-config --> block — the graph is not machine-readable"]
    cfg = {
        "id": "", "kind": "", "unit": "", "unit_outcome": "",
        "steps": [], "optional_steps": [], "entry": "", "terminal": [],
        "edges": parse_edges(block), "wip_limits": {}, "aging_thresholds": {},
        "decision_points": [], "evidence_exits": [], "cadence": "", "change_log": [],
    }
    for line in block.splitlines():
        if "->" in line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key in ("steps", "optional_steps", "terminal", "decision_points", "evidence_exits"):
            cfg[key] = [v.strip() for v in val.split(",") if v.strip()]
        elif key in ("wip_limits", "aging_thresholds"):
            for pair in val.split(","):
                if "=" in pair:
                    k2, _, v2 = pair.partition("=")
                    n = as_int(v2)
                    if n is None:
                        problems.append(f"flow-config {key}: `{pair.strip()}` is not step=<int>")
                    else:
                        cfg[key][k2.strip()] = n
        elif key in ("id", "kind", "entry", "cadence", "unit", "unit_outcome"):
            cfg[key] = val
        elif key == "edges":
            continue
    cfg["change_log"] = re.findall(r"^\s*[-|]\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    return cfg, problems


def step_index(cfg, step_id):
    return cfg["steps"].index(step_id) if step_id in cfg["steps"] else -1


def is_rework(cfg, from_step, to_step):
    """A back-edge: explicitly tagged, or landing earlier in the declared order."""
    for e in cfg["edges"]:
        if e["from"] == from_step and e["to"] == to_step and "rework" in e["tag"]:
            return True
    i, j = step_index(cfg, from_step), step_index(cfg, to_step)
    return i >= 0 and j >= 0 and j < i


def next_steps(cfg, step_id):
    return [e for e in cfg["edges"] if e["from"] == step_id]


# ------------------------------------------------------------------------------ steps

def load_steps(ws, cfg):
    """Load steps/<id>.md contracts. Returns ({id: step}, problems)."""
    steps, problems = {}, []
    base = ws / "steps"
    if not base.is_dir():
        return steps, ["steps/ directory not found"]
    for path in sorted(base.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, fm_problems = parse_frontmatter(text)
        if fm is None:
            problems.append(f"steps/{path.name}: {fm_problems[0]}")
            continue
        sid = str(fm.get("id", "")).strip() or path.stem
        if sid != path.stem:
            problems.append(f"steps/{path.name}: frontmatter id `{sid}` does not match the filename")
        step = {
            "id": sid, "path": path, "fm": fm, "body": text, "problems": fm_problems,
            "rung": as_int(fm.get("delegate_rung")),
            "exit_evidence": fm.get("exit_evidence") or [],
            "measures": fm.get("measures") or [],
            "context_packs": fm.get("context_packs") or [],
            "inner_graph": str(fm.get("inner_graph", "")).strip().lower() == "true",
            "graph_block": read_block(text, "step-graph"),
            "wip_limit": as_int(fm.get("wip_limit")),
            "aging_threshold": as_int(fm.get("aging_threshold")),
        }
        steps[sid] = step
    if cfg:
        for sid, step in steps.items():
            if step["wip_limit"] is not None:
                cfg["wip_limits"].setdefault(sid, step["wip_limit"])
            if step["aging_threshold"] is not None:
                cfg["aging_thresholds"].setdefault(sid, step["aging_threshold"])
    return steps, problems


# ------------------------------------------------------------------------------ items

def load_items(ws, cfg, today):
    """Load items/<slug>/item.md. Returns (items, problems)."""
    items, problems = [], []
    base = ws / "items"
    if not base.is_dir():
        return items, ["items/ directory not found"]
    for item_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        path = item_dir / "item.md"
        if not path.exists():
            problems.append(f"items/{item_dir.name}: missing item.md")
            continue
        text = path.read_text(encoding="utf-8")
        fm, fm_problems = parse_frontmatter(text)
        if fm is None:
            problems.append(f"items/{item_dir.name}: {fm_problems[0]}")
            continue
        entered = parse_iso(fm.get("step_entered"))
        item = {
            "slug": item_dir.name, "path": path, "fm": fm, "body": text,
            "problems": fm_problems, "flags": [],
            "step": str(fm.get("step", "")).strip(),
            "kind": str(fm.get("kind", "item")).strip() or "item",
            "holder": str(fm.get("holder", "")).strip(),
            "owner": str(fm.get("owner", "")).strip(),
            "klass": str(fm.get("class", "standard")).strip() or "standard",
            "parent": str(fm.get("parent", "")).strip(),
            "children": fm.get("children") or [],
            "blocked_by": str(fm.get("blocked_by", "")).strip(),
            "evidence_met": fm.get("evidence_exits_met") or [],
            "next_decision": str(fm.get("next_decision", "")).strip(),
            "override": as_int(fm.get("delegate_override")),
            "entered": entered,
            "age": (today - entered).days if entered else None,
        }
        if fm.get("step_entered") and entered is None:
            item["flags"].append("unparsable `step_entered`")
        items.append(item)
    return items, problems


def in_flow(cfg, item):
    return item["step"] in cfg["steps"]


def effective_rung(steps, item):
    if item["override"] is not None:
        return item["override"]
    step = steps.get(item["step"])
    return step["rung"] if step else None


def rollup_position(cfg, item, by_slug):
    """A rollup sits where its least-advanced child sits — flow is only as done as its laggard."""
    kids = [by_slug[c] for c in item["children"] if c in by_slug]
    live = [k for k in kids if in_flow(cfg, k)]
    if not live:
        return None, kids
    return min(live, key=lambda k: step_index(cfg, k["step"])), kids


# --------------------------------------------------------------------------- flow log

def update_flow_log(ws, items, today, write=True):
    """Append a row whenever an item's step differs from its last logged step."""
    log_path = ws / "flow-log.csv"
    last, rows = {}, []
    if log_path.exists():
        with log_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.reader(fh):
                if len(row) >= 4 and row[0] != "date":
                    rows.append(row)
                    last[row[1]] = row[3]
    appended = []
    for item in items:
        if not item["step"]:
            continue
        if last.get(item["slug"]) != item["step"]:
            when = item["fm"].get("step_entered") or today.isoformat()
            appended.append([str(when), item["slug"], last.get(item["slug"]) or "none", item["step"]])
    if write and (appended or not log_path.exists()):
        with log_path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["date", "slug", "from_step", "to_step"])
            w.writerows(rows + appended)
    return rows + appended, appended


def transitions_for(log_rows, slug):
    return [r for r in log_rows if r[1] == slug]


# ------------------------------------------------------------------------- workspace

def load_workspace(ws, today, write_log=True):
    """One call for the whole picture. Returns a dict; `fatal` non-empty means unusable."""
    cfg, cfg_problems = load_config(ws)
    if cfg is None:
        return {"fatal": cfg_problems, "config": None}
    steps, step_problems = load_steps(ws, cfg)
    items, item_problems = load_items(ws, cfg, today)
    log_rows, appended = update_flow_log(ws, items, today, write=write_log)
    return {
        "fatal": [], "ws": ws, "config": cfg, "steps": steps, "items": items,
        "by_slug": {i["slug"]: i for i in items}, "log_rows": log_rows, "appended": appended,
        "problems": cfg_problems + step_problems + item_problems, "today": today,
    }


def find_measures(ws):
    """Measure ids declared in measures.md's <!-- measure-set --> island."""
    path = ws / "measures.md"
    if not path.exists():
        return None
    block = read_block(path.read_text(encoding="utf-8"), "measure-set")
    if block is None:
        return None
    ids = set()
    for line in block.splitlines():
        if ":" in line:
            _, _, val = line.partition(":")
            ids.update(v.strip() for v in val.split(",") if v.strip())
    return ids
