#!/usr/bin/env python3
"""Validate a flow workspace against the workspace contract.

Checks the graph in workflow.md, the step contracts in steps/, the items in items/, and
the system-of-record bindings in integrations.md. Run it before every loop cycle: a loop
steered by a broken definition of workflow produces confident nonsense.

Usage:
  python3 flow_lint.py <flow-workspace> [--strict] [--quiet] [--today YYYY-MM-DD]

  --strict   treat warnings as violations
  --quiet    print only the verdict line

Exit codes: 0 = clean, 1 = violations found, 2 = workspace unusable.
"""

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import flow_defs as fd  # noqa: E402


def lint_graph(cfg, steps):
    v, w = [], []
    declared = set(cfg["steps"])
    terminal = set(cfg["terminal"])
    if not cfg["steps"]:
        v.append("flow-config declares no `steps`")
    if not cfg["unit"]:
        v.append("flow-config declares no `unit` — nobody has said what one item is, so nothing else "
                 "in the definition can be checked against it (see references/unit-of-value.md)")
    if not cfg["unit_outcome"]:
        w.append("flow-config declares no `unit_outcome` — say what changes, and for whom, when one "
                 "item finishes; a unit with no stated change legitimises activity-shaped work")
    if not cfg["entry"]:
        v.append("flow-config declares no `entry`")
    elif cfg["entry"] not in declared:
        v.append(f"entry `{cfg['entry']}` is not in `steps`")
    if not terminal:
        w.append("flow-config declares no `terminal` states — items have nowhere to land")
    for key in ("optional_steps", "decision_points", "evidence_exits"):
        for sid in cfg[key]:
            if sid not in declared:
                v.append(f"`{key}` names unknown step `{sid}`")
    for key in ("wip_limits", "aging_thresholds"):
        for sid in cfg[key]:
            if sid not in declared:
                w.append(f"`{key}` names unknown step `{sid}`")
    for sid in declared:
        if sid not in steps:
            v.append(f"step `{sid}` is declared in the graph but has no `steps/{sid}.md` contract")
    for sid in steps:
        if sid not in declared:
            v.append(f"`steps/{sid}.md` exists but `{sid}` is not in the graph's `steps` list")
    known = declared | terminal
    for e in cfg["edges"]:
        if e["from"] not in known:
            v.append(f"edge `{e['from']} -> {e['to']}` starts at unknown step `{e['from']}`")
        if e["to"] not in known:
            v.append(f"edge `{e['from']} -> {e['to']}` targets unknown step `{e['to']}`")
        if e["from"] in terminal:
            w.append(f"edge leaves terminal state `{e['from']}` — terminal states absorb")
    for sid in declared:
        if not fd.next_steps(cfg, sid):
            v.append(f"step `{sid}` has no outgoing edge — work arrives and cannot leave")
    if cfg["entry"] in declared:
        seen, frontier = {cfg["entry"]}, [cfg["entry"]]
        while frontier:
            cur = frontier.pop()
            for e in fd.next_steps(cfg, cur):
                if e["to"] not in seen:
                    seen.add(e["to"])
                    frontier.append(e["to"])
        for sid in declared - seen:
            v.append(f"step `{sid}` is unreachable from `{cfg['entry']}`")
        for t in terminal - seen:
            w.append(f"terminal state `{t}` is unreachable — nothing can finish there")
    return v, w


def lint_step(step, cfg, ws, measure_ids):
    v, w = [], []
    sid, fm = step["id"], step["fm"]
    for field in fd.STEP_REQUIRED:
        if not fm.get(field):
            v.append(f"step `{sid}`: missing `{field}`")
    if fm.get("type") and fm["type"] not in fd.STEP_TYPES:
        w.append(f"step `{sid}`: unusual `type` `{fm['type']}` (expected one of {', '.join(fd.STEP_TYPES)})")
    run = str(fm.get("run", "")).strip()
    if run and run not in fd.RUN_MODELS:
        v.append(f"step `{sid}`: unknown run model `{run}` (expected one of {', '.join(fd.RUN_MODELS)})")
    rung = step["rung"]
    if rung is None or not 0 <= rung <= 5:
        v.append(f"step `{sid}`: `delegate_rung` must be an integer 0–5")
        rung = -1
    if run and run != "human" and not fm.get("run_ref"):
        v.append(f"step `{sid}`: run model `{run}` with no `run_ref` — nobody can tell how to run it")
    ref = str(fm.get("run_ref", "")).strip()
    if ref and not re.match(r"^(https?:|/|\w+:)", ref) and "/" in ref and not (ws / ref).exists():
        w.append(f"step `{sid}`: `run_ref` `{ref}` does not exist in the workspace")
    for pack in step["context_packs"]:
        if not (ws / "platform" / "context" / f"{pack}.md").exists():
            w.append(f"step `{sid}`: context pack `{pack}` has no `platform/context/{pack}.md`")
    verify = str(fm.get("verify_with", "")).strip()
    if rung >= 4 and not verify:
        v.append(f"step `{sid}`: rung {rung} needs a `verify_with` that is independent of the runner")
    elif rung == 3 and not verify:
        w.append(f"step `{sid}`: rung 3 with no `verify_with` — the runner is grading its own work")
    if verify and verify == ref:
        v.append(f"step `{sid}`: `verify_with` is the same artifact as `run_ref` — that is not verification")
    if sid in cfg["evidence_exits"] and not verify:
        w.append(f"step `{sid}` is an evidence exit with no `verify_with` recipe")
    if rung >= 3 and not fm.get("escalate_when"):
        w.append(f"step `{sid}`: rung {rung} with no `escalate_when` — the agent has no way to stop")
    for m in step["measures"]:
        if measure_ids is not None and m not in measure_ids:
            w.append(f"step `{sid}`: measure `{m}` is not declared in measures.md")
    if step["inner_graph"] and not step["graph_block"]:
        v.append(f"step `{sid}`: `inner_graph: true` but no `<!-- step-graph -->` block in the body")
    if step["graph_block"]:
        v2, w2 = lint_inner_graph(sid, step["graph_block"])
        v += v2
        w += w2
    return v, w


def lint_inner_graph(sid, block):
    v, w = [], []
    nodes, entry, max_iter = [], "", None
    for line in block.splitlines():
        if "->" in line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key == "nodes":
            nodes = [n.strip() for n in val.split(",") if n.strip()]
        elif key == "entry":
            entry = val
        elif key == "max_iterations":
            max_iter = fd.as_int(val)
    edges = fd.parse_edges(block)
    known = set(nodes) | {"exit"}
    if not nodes:
        v.append(f"step `{sid}` inner graph: no `nodes`")
    if entry and entry not in known:
        v.append(f"step `{sid}` inner graph: entry `{entry}` is not a node")
    for e in edges:
        for side in ("from", "to"):
            if e[side] not in known:
                v.append(f"step `{sid}` inner graph: edge `{e['from']} -> {e['to']}` names unknown node `{e[side]}`")
    order = {n: i for i, n in enumerate(nodes)}
    loops = [e for e in edges if "rework" in e["tag"]
             or (e["from"] in order and e["to"] in order and order[e["to"]] <= order[e["from"]])]
    if loops and max_iter is None:
        v.append(f"step `{sid}` inner graph: has a loop edge but no `max_iterations` — unbounded inner loops "
                 f"converge on plausibility, not truth")
    if not any(e["to"] == "exit" for e in edges):
        w.append(f"step `{sid}` inner graph: no edge to `exit` — where does the step finish?")
    return v, w


def lint_item(item, cfg, steps, log_rows):
    v, w = [], []
    slug, fm = item["slug"], item["fm"]
    for field in fd.ITEM_REQUIRED:
        if not fm.get(field):
            v.append(f"item `{slug}`: missing `{field}`")
    if item["step"] and item["step"] not in set(cfg["steps"]) | set(cfg["terminal"]):
        v.append(f"item `{slug}`: sits on unknown step `{item['step']}`")
    if item["holder"] and item["holder"] not in fd.HOLDERS:
        v.append(f"item `{slug}`: unknown holder `{item['holder']}` (expected one of {', '.join(fd.HOLDERS)})")
    if item["kind"] not in fd.ITEM_KINDS:
        w.append(f"item `{slug}`: unusual kind `{item['kind']}`")
    if item["klass"] not in fd.CLASSES:
        w.append(f"item `{slug}`: unusual class `{item['klass']}`")
    if item["blocked_by"] and item["holder"] != "blocked":
        w.append(f"item `{slug}`: has `blocked_by` but holder is `{item['holder']}` — the board will under-report waiting")
    if item["holder"] == "waiting-decision" and not item["next_decision"]:
        w.append(f"item `{slug}`: waiting on a decision that is not written down in `next_decision`")
    if item["kind"] == "rollup" and not item["children"]:
        w.append(f"item `{slug}`: kind `rollup` with no children")
    if item["kind"] != "rollup" and item["children"]:
        v.append(f"item `{slug}`: has children but kind is `{item['kind']}` — say `rollup` or drop the children")
    if item["step"] in cfg["decision_points"]:
        if not re.search(r"##\s*Decision log.*?\d{4}-\d{2}-\d{2}", item["body"], re.DOTALL | re.IGNORECASE):
            v.append(f"item `{slug}`: entered decision point `{item['step']}` with no dated Decision-log entry")
    left = {r[2] for r in fd.transitions_for(log_rows, slug)}
    for sid in left:
        if sid in cfg["evidence_exits"] and sid not in item["evidence_met"]:
            v.append(f"item `{slug}`: left evidence exit `{sid}` without recording it in `evidence_exits_met`")
    for sid in item["evidence_met"]:
        if sid not in cfg["steps"]:
            w.append(f"item `{slug}`: `evidence_exits_met` names unknown step `{sid}`")
    return v, w


def lint_tree(items, by_slug):
    v = []
    for item in items:
        if item["parent"]:
            parent = by_slug.get(item["parent"])
            if not parent:
                v.append(f"item `{item['slug']}`: parent `{item['parent']}` does not exist")
            elif item["slug"] not in parent["children"]:
                v.append(f"item `{item['slug']}`: parent `{item['parent']}` does not list it as a child")
        for child in item["children"]:
            kid = by_slug.get(child)
            if not kid:
                v.append(f"item `{item['slug']}`: child `{child}` does not exist")
            elif kid["parent"] != item["slug"]:
                v.append(f"item `{item['slug']}`: child `{child}` does not point back to it as parent")
    return v


def lint_integrations(ws):
    v, w = [], []
    path = ws / "integrations.md"
    if not path.exists():
        return v, ["no integrations.md — the system of record is undeclared (files-only is a fine answer, "
                   "but say so)"]
    block = fd.read_block(path.read_text(encoding="utf-8"), "integration-map")
    if block is None:
        return v, ["integrations.md has no <!-- integration-map --> block — bindings are not checkable"]
    owners = {}
    for line in block.splitlines():
        m = re.match(r"\s*field:\s*([\w.-]+)\s*->\s*(.+?)\s*\(owner:\s*([\w-]+)\)\s*$", line)
        if not m:
            if line.strip().startswith("field:"):
                w.append(f"integration-map: unparsable field line {line.strip()!r} "
                         f"(expected `field: <name> -> <target> (owner: <system>)`)")
            continue
        field, owner = m.group(1), m.group(3)
        if field in owners and owners[field] != owner:
            v.append(f"integration-map: field `{field}` has two owners "
                     f"(`{owners[field]}` and `{owner}`) — exactly one writer per field")
        owners[field] = owner
    if not owners:
        w.append("integration-map declares no fields")
    return v, w


def run_checks(ws, data):
    """Every check, in one call. Returns (violations, warnings). Reused by flow_next.py."""
    cfg, steps, items = data["config"], data["steps"], data["items"]
    measure_ids = fd.find_measures(ws)
    violations, warnings = lint_graph(cfg, steps)
    for sid in sorted(steps):
        v, w = lint_step(steps[sid], cfg, ws, measure_ids)
        violations += v
        warnings += w
    for item in items:
        v, w = lint_item(item, cfg, steps, data["log_rows"])
        violations += v
        warnings += w
    violations += lint_tree(items, data["by_slug"])
    v, w = lint_integrations(ws)
    violations += v
    warnings += w
    if measure_ids is None:
        warnings.append("no measures.md with a <!-- measure-set --> block — the workflow has no declared measures")
    warnings += [f"data quality: {p}" for p in data["problems"]]
    if not items:
        warnings.append("no items in items/ — nothing is flowing yet")
    return violations, warnings


def main(argv):
    positional, values, flags = fd.parse_cli(argv[1:], value_opts=("today",))
    today = fd.parse_iso(values.get("today")) or date.today()
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
            print(f"FATAL  {line}")
        return 2
    cfg, steps, items = data["config"], data["steps"], data["items"]
    violations, warnings = run_checks(ws, data)

    quiet = "quiet" in flags
    if not quiet:
        if violations:
            print(f"\nVIOLATIONS ({len(violations)}) — fix these before running a loop cycle\n")
            for line in violations:
                print(f"  ✗ {line}")
        if warnings:
            print(f"\nWARNINGS ({len(warnings)})\n")
            for line in warnings:
                print(f"  ! {line}")
        print()
    strict = "strict" in flags
    verdict = "CLEAN" if not violations and not (strict and warnings) else "VIOLATIONS"
    print(f"{verdict}: {len(steps)} steps, {len(items)} items, {len(cfg['edges'])} edges, "
          f"{len(violations)} violations, {len(warnings)} warnings")
    return 1 if verdict == "VIOLATIONS" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
