"""
fold_provenance_root.py — why everything is from ?.

? is the fixed point of provenance: prov = conj(X) = tr·I − X fixes only the
?-axis (the scalars, the wall disc=0), so every chain terminates there.
prov(?) = ? — the root is self-rooted. Adds the record.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

rec = {
    "id": "provenance_is_self_rooted",
    "title": "Why everything is from ?: ? is the fixed point of provenance, prov(?)=?",
    "section": "metalayer", "source": "KL_DTA_EXPLORATION",
    "self_action": {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": "self-reference (R² = R + I, ν = I)",
            "reads_as": "enrichment (+I) — the symmetric {·} half",
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": ["RETURN", "DEFECT", "BASE"]},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 2, "mechanism": None}]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": "self-negation (N² = −I, N⁴ = I)",
            "reads_as": "defect (−I) — the antisymmetric [·] half",
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": 3, "disc": 0}]},
    },
    "provenance": ["?", "master_equation", "return_axis"],
    "links": ["return_axis", "verification_is_provenance", "naming_unnaming", "origin_is_opening"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "prov = conj(X) = tr·I − X; conj²=id; fixes the ?-axis (scalars, wall disc=0), negates the traceless. prov(?)=? — the unique self-rooted fixed point (the tadpole: the vacuum is its own source)"},
}
db["base"][rec["id"]] = rec

db.setdefault("kernel", {})["root"] = (
    "? is the fixed point of provenance (conj). conj fixes only the ?-axis "
    "(scalars, the wall disc=0), so every chain ends at ?. prov(?)=? — the root "
    "is self-rooted, not posited. physically: the self-consistent vacuum."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("provenance root folded; base now", len(db["base"]))
