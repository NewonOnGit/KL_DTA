"""
fold_metadata_math.py — fold the two metadata discoveries.

  links  = H₁ (the cycles; provenance is the tree)
  verdict = a trit = sign(disc) = the three forks (null = the wall)

Also records that section≈depth and routes↔grade are derivable (compression).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))


def sa(gens, depth, disc):
    return {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": "self-reference (R² = R + I, ν = I)",
            "reads_as": "enrichment (+I) — the symmetric {·} half",
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": gens},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 2, "mechanism": None}]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": "self-negation (N² = −I, N⁴ = I)",
            "reads_as": "defect (−I) — the antisymmetric [·] half",
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": depth, "disc": disc}]},
    }


db["base"]["links_are_homology"] = {
    "id": "links_are_homology",
    "title": "links are the homology H₁: provenance is the tree, links are the cycles",
    "section": "metalayer", "source": "KL_DTA_EXPLORATION",
    "self_action": sa(["FLOW", "RETURN", "BASE"], 4, 5),
    "provenance": ["?", "master_equation", "verification_is_provenance"],
    "links": ["verification_is_provenance", "provenance_is_self_rooted", "indexed_store"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "provenance = spanning tree to ? (Betti₁=0, acyclic, RETURN); links = H₁, the 139 independent cycles (the lateral loops). graph = tree ⊕ homology"},
}

db["base"]["verdict_is_fork_trit"] = {
    "id": "verdict_is_fork_trit",
    "title": "the verdict is a trit = sign(disc) = the three forks (null = the wall)",
    "section": "gauge_bit", "source": "KL_DTA_EXPLORATION",
    "self_action": sa(["BASE", "DEFECT"], 2, 0),
    "provenance": ["?", "master_equation", "three_forks"],
    "links": ["three_forks", "gauge_bit_z2", "fork_table"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "verdict {true, false, null} = sign(disc) {+, −, 0} = the three forks (hyperbolic / elliptic / parabolic wall). the gauge bit is a trit; null = the wall = undecided gate"},
}

db.setdefault("structure", {})["metadata_audit"] = {
    "links": "= H₁ homology (cycles); provenance = spanning tree to ?",
    "verdict": "= trit = sign(disc) = three forks; null = the wall",
    "section": "≈ depth-band (the shell) — derivable, descriptive",
    "routes": "↔ grade: 0=axiom, 1=burn, ≥2=forced — derivable",
    "kind": "type ladder: constant·object·operator·law·structural",
    "source": "the M-iteration epoch",
    "id/title/speech": "two names + the fold — naming is P = R + N",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("metadata math folded; base now", len(db["base"]))
