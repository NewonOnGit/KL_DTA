"""
fold_grammar.py — internalize the fixed-point grammar.

The connective words are the five fold-operations spoken. A sentence is an
expression-tree (content at leaves, fixed-point words at nodes); generating
language is walking it; the observer supplies only the coherence.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["grammar"] = {
    "is": "the fixed-point grammar — the connective words ARE the fold-operations",
    "words": {
        "the":   "BASE   — index / determinacy (this specific one)",
        "a":     "FIBER  — class / a member",
        "is":    "FOLD   — equality / the copula / the fixed point (X is its fold)",
        "isn't": "DEFECT — ≠ / the gap / self-negation",
        "of":    "RETURN — belonging / provenance / application",
        "to":    "FLOW   — the arrow / becoming",
    },
    "mechanism": "a sentence is an expression-tree: content (objects) at the leaves, "
                 "fixed-point words at the nodes. generating language = walking the tree.",
    "coherence": "the words' meaning is fixed (inherent); only the walk — voice, order, "
                 "projection — is the observer's coherence.",
    "example": "P²=P  ⟺  'the fold of the seed is the seed'  ('is' = the fixed point)",
}

rec = {
    "id": "fixed_point_grammar",
    "title": "The fixed-point grammar: connective words ARE the fold-operations",
    "section": "metalayer", "source": "KL_DTA_EXPLORATION",
    "self_action": {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": "self-reference (R² = R + I, ν = I)",
            "reads_as": "enrichment (+I) — the symmetric {·} half",
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": ["RETURN", "BASE", "FOLD"]},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 2, "mechanism": None}]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": "self-negation (N² = −I, N⁴ = I)",
            "reads_as": "defect (−I) — the antisymmetric [·] half",
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": 4, "disc": None}]},
    },
    "provenance": ["?", "master_equation", "indexed_store"],
    "links": ["indexed_store", "naming_unnaming", "verification_is_provenance", "five_generators"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "the=BASE, a=FIBER, is=FOLD, isn't=DEFECT, of=RETURN, to=FLOW; sentence = walk(expression-tree); 'is' = the fixed point (X is its fold)"},
}
db["base"][rec["id"]] = rec

# place `grammar` right after `kernel`
order, out = list(db.keys()), {}
for k in order:
    if k != "grammar":
        out[k] = db[k]
    if k == "kernel":
        out["grammar"] = db["grammar"]
db = out

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("fixed-point grammar internalized; base now", len(db["base"]))
