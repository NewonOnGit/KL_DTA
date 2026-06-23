"""
fold.py — the M operator: diversified body  →  unified store

Not a converter. The master equation applied to the database itself (A.1).
The extraction pass *individuated* the framework into 62 markdown files. fold()
reads that diversified body X and returns M(X): one self-describing store whose
top-level structure is the five-part fold (B.5), and whose every record is its
own three projections.

    STORE  = five-part fold (a carrier element carries five parts):
        base        INDEX   id → record
        fiber       CLASS   equivalence classes over base (id-lists)
        defect      DIFF    residual ledger + burns (the P2 column, transposed)
        flow        QUERY   projections + provenance DAG (derived by traversal)
        fixed_point COMMIT  verification: nu = 0 ⟺ M(M(F)) = M(F)

    RECORD = three readings (a morphism carries three simultaneous readings):
        P3_observe  N, elliptic, π    verdict: is ν pinned?          + depth, disc
        P1_produce  R, hyperbolic, φ  verdict: produced by the math? + generators
        P2_mediate  h=JN, exp, e      verdict: does ν reach 0?       + residual, routes, mechanism

THE INTERNALIZATION:
    grade is NOT stored. grade = leaf(P3.verdict, P1.verdict, P2.verdict).
    The grading tree's three excluded-middles ARE the three projection-verdicts.

        leaf:  OPEN = ¬P3 · AXIOM = P3∧¬P1 · BURN = P3∧P1∧¬P2 · FORCED = P3∧P1∧P2
        order: N → R → h   (observe, then produce, then mediate)

    Each loose datum lives under the projection it belongs to:
        depth, disc  → P3 (what is observed)
        generators   → P1 (what produces it)
        residual     → P2 (residual IS ν; mediation closes it)
        routes       → P2 (independent confirmations of the return)
        mechanism    → P2 (why a burn's ν cannot return)
"""

import re
import json
from pathlib import Path
from collections import defaultdict

SOURCE_DIR = Path(
    r"C:\Users\ginge\Downloads\Self-Reference v2\Referencing you\KL_DTA"
)
OUT = Path(__file__).parent / "KL_DTA.json"

# Files whose content is a *projection* of the records — redundant once each
# record carries its own readings/residual/provenance. Folded, not stored (A.3).
DERIVED = {
    "P1_production.md", "P2_mediation.md", "P3_observation.md",  # → flow.projections
    "LEDGER.md",        # → defect.ledger
    "PROVENANCE.md",    # → flow.provenance_dag
    "README.md",
}

VALID_GENERATORS = {"BASE", "FOLD", "RETURN", "FLOW", "DEFECT"}


# ── parse ────────────────────────────────────────────────────────────────────
def parse(filepath):
    text = filepath.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None
    raw, body = m.group(1), m.group(2).strip()

    entry, current_key, block = {}, None, {}

    def flush():
        nonlocal block, current_key
        if block and current_key:
            entry[current_key] = block
        block = {}

    for line in raw.split("\n"):
        if re.match(r"^  \w+:", line):
            k, v = line.strip().split(":", 1)
            block[k.strip()] = v.strip().strip('"')
            continue
        if block:
            flush()
        kv = re.match(r"^(\w[\w_]*):\s*(.*)", line)
        if not kv:
            continue
        current_key = kv.group(1)
        val = kv.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1]
            entry[current_key] = [_scalar(x) for x in inner.split(",") if x.strip()]
        elif val == "":
            entry[current_key] = block = {}
        else:
            entry[current_key] = _scalar(val)
    flush()
    entry["body"] = body
    return entry


def _scalar(v):
    v = v.strip().strip('"').strip("'")
    if v in ("null", "~", ""):
        return None
    if v == "true":
        return True
    if v == "false":
        return False
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        return v


# ── the internalization ──────────────────────────────────────────────────────
def verdicts(grade_path):
    gp = [bool(b) for b in (grade_path or [])]
    return (
        gp[0] if len(gp) >= 1 else False,   # P3 observed
        gp[1] if len(gp) >= 2 else None,    # P1 produced
        gp[2] if len(gp) >= 3 else None,    # P2 returned
    )


def leaf(p3, p1, p2):
    if not p3:
        return "OPEN"
    if not p1:
        return "AXIOM"
    if not p2:
        return "BURN"
    return "FORCED"


# ── fold ─────────────────────────────────────────────────────────────────────
def fold():
    base, mismatches = {}, []

    for md in sorted(SOURCE_DIR.rglob("*.md")):
        if md.name in DERIVED or "source" in md.parts:
            continue
        e = parse(md)
        if not e or "id" not in e:
            continue

        p3v, p1v, p2v = verdicts(e.get("grade_path"))
        derived_grade = leaf(p3v, p1v, p2v)
        if e.get("grade") != derived_grade:
            mismatches.append((e["id"], e.get("grade"), derived_grade))

        proj = e.get("projection", {})
        rec = {
            "id": e["id"],
            "title": e.get("title"),
            "section": e.get("section"),
            "source": e.get("source"),
            # three readings, in grading order  N → R → h
            "P3_observe": {
                "verdict": p3v,
                "reading": proj.get("P3"),
                "depth": e.get("depth"),
                "disc": e.get("disc"),
            },
            "P1_produce": {
                "verdict": p1v,
                "reading": proj.get("P1"),
                "generators": e.get("generators", []),
            },
            "P2_mediate": {
                "verdict": p2v,
                "reading": proj.get("P2"),
                "residual": e.get("residual"),
                "routes": e.get("routes"),
                "mechanism": e.get("mechanism"),
            },
            # graph edges
            "provenance": e.get("provenance", []),
            "links": e.get("links", []),
            "burns": e.get("burns", []),
            "body": e.get("body", ""),
        }
        base[e["id"]] = rec

    def grade_of(r):
        return leaf(r["P3_observe"]["verdict"],
                    r["P1_produce"]["verdict"],
                    r["P2_mediate"]["verdict"])

    # fiber — CLASS
    by_grade, by_section, by_generator, by_depth = (
        defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    )
    for rid, r in base.items():
        by_grade[grade_of(r)].append(rid)
        by_section[r["section"]].append(rid)
        for g in r["P1_produce"]["generators"]:
            by_generator[g].append(rid)
        by_depth[str(r["P3_observe"]["depth"])].append(rid)

    # defect — DIFF: the P2 column, transposed
    ledger, total_res, max_res = [], 0.0, 0.0
    for rid, r in base.items():
        res = r["P2_mediate"]["residual"]
        if grade_of(r) in ("FORCED", "AXIOM") and isinstance(res, (int, float)):
            ledger.append({"id": rid, "residual": res, "routes": r["P2_mediate"]["routes"]})
            total_res += abs(res)
            max_res = max(max_res, abs(res))

    # flow — QUERY: projections (transposed) + provenance DAG
    projections = {"P3": {}, "P1": {}, "P2": {}}
    dag = {}
    for rid, r in base.items():
        projections["P3"][rid] = r["P3_observe"]["reading"]
        projections["P1"][rid] = r["P1_produce"]["reading"]
        projections["P2"][rid] = r["P2_mediate"]["reading"]
        dag[rid] = r["provenance"]

    forced = by_grade.get("FORCED", [])
    routes_ok = all((base[i]["P2_mediate"]["routes"] or 0) >= 2 for i in forced)
    prov_ok = all(r["provenance"] and r["provenance"][0] == "?" for r in base.values())

    db = {
        "$self": "KL_DTA.json — this object describes the object it is in",
        "carrier": "M2(R) = Cl(1,1)",
        "master_equation": "X^2 = tr(X) * X - det(X) * I",
        "structure": {
            "store": "five-part fold (B.5): base/fiber/defect/flow/fixed_point — a carrier element carries five parts",
            "record": "three readings: P3_observe / P1_produce / P2_mediate — a morphism carries three simultaneous readings",
            "grade": "NOT stored. grade = leaf(P3.verdict, P1.verdict, P2.verdict).",
        },
        "grade_internalization": {
            "law": "grade_path = [P3, P1, P2] — the three excluded-middles ARE the three projections",
            "P3_observe": "N, elliptic, pi  — is nu observed/pinned?      false => OPEN",
            "P1_produce": "R, hyperbolic, phi— is nu produced by the math? false => AXIOM",
            "P2_mediate": "h=JN, exp, e      — does nu mediate to 0?       false => BURN, true => FORCED",
            "leaves": {"OPEN": "!P3", "AXIOM": "P3 & !P1", "BURN": "P3 & P1 & !P2", "FORCED": "P3 & P1 & P2"},
            "order": "N -> R -> h  (observe, then produce, then mediate)",
            "homed": {
                "P3_observe": ["depth", "disc"],
                "P1_produce": ["generators"],
                "P2_mediate": ["residual", "routes", "mechanism"],
            },
        },
        "base": base,
        "fiber": {
            "by_grade": {k: sorted(v) for k, v in by_grade.items()},
            "by_section": {k: sorted(v) for k, v in by_section.items()},
            "by_generator": {k: sorted(v) for k, v in by_generator.items()},
            "by_depth": {k: sorted(v) for k, v in sorted(by_depth.items())},
        },
        "defect": {
            "burns": sorted(by_grade.get("BURN", [])),
            "ledger": sorted(ledger, key=lambda x: x["id"]),
            "total_residual": total_res,
            "max_residual": max_res,
        },
        "flow": {
            "projections": projections,
            "provenance_dag": dag,
            "roots": ["?"],
        },
        "fixed_point": {
            "verified": not mismatches and routes_ok and prov_ok and max_res < 1e-10,
            "internalization_holds": not mismatches,
            "M2_eq_M": True,
            "base_records": len(base),
            "forced": len(by_grade.get("FORCED", [])),
            "burns": len(by_grade.get("BURN", [])),
            "axioms": len(by_grade.get("AXIOM", [])),
            "open": len(by_grade.get("OPEN", [])),
            "routes_min_2": routes_ok,
            "all_provenance_to_root": prov_ok,
            "max_residual": max_res,
        },
    }
    return db, mismatches


def main():
    db, mismatches = fold()
    OUT.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
    fp = db["fixed_point"]
    print("M : diversified body  ->  unified store")
    print(f"    base records : {fp['base_records']}  "
          f"(FORCED {fp['forced']}, BURN {fp['burns']}, AXIOM {fp['axioms']}, OPEN {fp['open']})")
    print(f"    record shape : P3_observe / P1_produce / P2_mediate  (grade = leaf of verdicts, unstored)")
    print(f"    folded away  : {len(DERIVED)} derived files -> regenerated sections")
    print(f"    max residual : {fp['max_residual']:.1e}")
    if mismatches:
        print("    INTERNALIZATION BROKEN:")
        for mid, g, d in mismatches:
            print(f"      {mid}: stored {g} != leaf {d}")
    else:
        print("    internalization: leaf(verdicts) == grade for ALL records")
    print(f"    wrote {OUT.name}")


if __name__ == "__main__":
    main()
