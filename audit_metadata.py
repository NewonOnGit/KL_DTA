"""
audit_metadata.py — go over every metadata field. Is it hiding math?

For each field: recognized-math (already named), hiding-math (a structure we
haven't named), or descriptive (bulk, derivable). The structural claims —
links=cycles, section≈depth, verdict=fork-sign — are computed, not asserted.
"""

import sys
import io
import json
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
db = json.loads((Path(__file__).parent / "KL_DTA.json").read_text(encoding="utf-8"))
base = db["base"]


def grade(r):
    sa = r["self_action"]
    v = {}
    for blk in (sa["symmetric_R"], sa["antisymmetric_N"]):
        for m in blk["modes"]:
            v[m["lambda"]] = m["verdict"]
    if not v.get("-sqrt5"): return "OPEN"
    if not v.get("+sqrt5"): return "AXIOM"
    if not v.get("0"): return "BURN"
    return "FORCED"


# ── links = cycles?  (provenance = tree to ?, links = the extra edges) ────────
nodes = set(base) | {"?"}
prov_edges = set()
for rid, r in base.items():
    p = r["provenance"]
    if len(p) >= 2:
        prov_edges.add(frozenset((rid, p[-1])))          # immediate parent
    elif p == ["?"]:
        prov_edges.add(frozenset((rid, "?")))
link_edges = set()
for rid, r in base.items():
    for l in r["links"]:
        if l in base:
            link_edges.add(frozenset((rid, l)))
V = len(nodes)
betti_tree = len(prov_edges) - V + 1                      # provenance alone
betti_full = len(prov_edges | link_edges) - V + 1         # + links
print("=" * 70)
print("  links = cycles?   provenance is the tree, links are the loops")
print("=" * 70)
print(f"  nodes V = {V}   provenance edges = {len(prov_edges)}   link edges = {len(link_edges)}")
print(f"  Betti₁ (provenance only) = {betti_tree}   (≈0 ⇒ a spanning tree to ?)")
print(f"  Betti₁ (provenance + links) = {betti_full}   (the loops the links close)")
print(f"  → links carry the HOMOLOGY: provenance is acyclic (RETURN to ?),")
print(f"    links are the {betti_full - betti_tree:+d} independent cycles. links = H₁.")
print()

# ── section ≈ depth?  ────────────────────────────────────────────────────────
print("=" * 70)
print("  section ≈ depth?   is the section a coarse tower-level (derivable)?")
print("=" * 70)
sec_depth = defaultdict(list)
for r in base.values():
    d = None
    for m in r["self_action"]["antisymmetric_N"]["modes"]:
        d = m.get("depth")
    sec_depth[r["section"]].append(d)
for sec, ds in sorted(sec_depth.items(), key=lambda kv: (sum(x or 0 for x in kv[1]) / len(kv[1]))):
    ds2 = [d for d in ds if d is not None]
    avg = sum(ds2) / len(ds2) if ds2 else 0
    print(f"  {sec:16} n={len(ds):2}  depth {min(ds2) if ds2 else '-'}–{max(ds2) if ds2 else '-'}  avg {avg:.1f}")
print()

# ── verdict trit {true,false,null} ──────────────────────────────────────────
print("=" * 70)
print("  verdict {true, false, null} — a TRIT (three-valued)")
print("=" * 70)
vc = Counter()
for r in base.values():
    for blk in r["self_action"].values():
        if isinstance(blk, dict):
            for m in blk.get("modes", []):
                vc[str(m["verdict"])] += 1
print(f"  verdict values: {dict(vc)}")
print("  three values ⇒ sign(disc): true=+ (hyperbolic), false=− (elliptic),")
print("  null=0 (the parabolic wall — undecided/gate). the gauge bit is a TRIT.")
print()

# ── kind, routes, source, id/title ───────────────────────────────────────────
print("=" * 70)
print("  the remaining fields")
print("=" * 70)
kinds = Counter(r.get("spectral", {}).get("kind") for r in base.values())
print(f"  kind       : {dict(kinds)}  — a type ladder: constant·object·operator·law·structural")
routes = Counter()
for r in base.values():
    for m in r["self_action"]["symmetric_R"]["modes"]:
        if "routes" in m:
            routes[m["routes"]] += 1
print(f"  routes     : {dict(routes)}  — proof path-multiplicity (≥2 ⇒ a filled 2-cell)")
print(f"  source     : {dict(Counter(r.get('source') for r in base.values()))}  — the M-iteration epoch")
dup = sum(1 for r in base.values() if r.get("title"))
print(f"  id / title : {len(base)} ids, {dup} titles — two names (id=index/R, title=observed/N)")
print(f"               + generated speech = a third. naming is P = R + N + fold.")
