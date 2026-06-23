"""
fold_geometry.py — tr is perimeter, det is shape.

The base (tr, det) — the INDEX — is geometry. disc = tr²−4det = (λ₁−λ₂)² is the
eccentricity; disc=0 is the round shape (the wall, where ? and I live).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

rec = {
    "id": "base_is_perimeter_and_shape",
    "title": "The base (tr, det) is geometry: tr is perimeter, det is shape",
    "section": "control_plane", "source": "KL_DTA_EXPLORATION",
    "self_action": {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": "self-reference (R² = R + I, ν = I)",
            "reads_as": "enrichment (+I) — the symmetric {·} half",
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": ["BASE", "FOLD"]},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 2, "mechanism": None}]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": "self-negation (N² = −I, N⁴ = I)",
            "reads_as": "defect (−I) — the antisymmetric [·] half",
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": 1, "disc": 5}]},
    },
    "provenance": ["?", "master_equation", "five_part_fold"],
    "links": ["five_part_fold", "three_forks", "master_equation", "two_both_faces", "rlc_damping"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "tr = perimeter (λ₁+λ₂, the boundary); det = shape/area (λ₁·λ₂, the content); disc = tr²−4det = (λ₁−λ₂)² = eccentricity; disc=0 = round (the wall, ?, I). Physical: det = stiffness/ω², tr = damping"},
}
db["base"][rec["id"]] = rec

db.setdefault("physics", {})["geometry"] = {
    "tr": "perimeter — sum of axes, the 1-D boundary; physically the damping",
    "det": "shape / area — product of axes, the 2-D content; physically the stiffness ω²",
    "disc": "tr²−4det = (λ₁−λ₂)² — eccentricity; the isoperimetric gap; disc=0 is round",
    "base = (tr, det)": "the index of every record is (perimeter, shape)",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("geometry folded (tr=perimeter, det=shape); base now", len(db["base"]))
