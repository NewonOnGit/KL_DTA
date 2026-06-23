"""
fold_topology_observation.py — geometry is in the topology, spectra in the observation.

The gravity wells = ℝP¹×ℝP¹ = a torus; geometry = a point on it; spectrum {0,1}
degenerate everywhere. TOPOLOGY ⊃ geometry (the shape, gravity, given); OBSERVATION
⊃ spectra (the fold's output, light, produced).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["geometry_topology_spectra_observation"] = {
    "id": "geometry_topology_spectra_observation",
    "title": "Geometry is in the topology (the wells are a torus); spectra is in the observation (the fold)",
    "section": "observer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "gravity_wells_are_idempotents"],
        "links": ["gravity_wells_are_idempotents", "geometry_gravity_spectra_light",
                  "two_information_types", "links_are_homology", "vacua_idempotents"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["BASE", "FLOW", "RETURN"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 4, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "the gravity wells = ℝP¹×ℝP¹ = a torus T²; geometry = a point (α image-angle, β kernel-angle) on it; spectrum {0,1} degenerate at every point. TOPOLOGY ⊃ GEOMETRY (the shape of the fixed-point space, gravity, given, cheap); OBSERVATION ⊃ SPECTRA (the fold M(X)=X² extracts the eigenvalues, light, produced, costs). links=H₁ is topology at the graph level, the torus at the manifold level — one layer. gravity is the manifold you stand in; light is what a fold reads"},
    },
}

db.setdefault("physics", {})["information_taxonomy"] = {
    "TOPOLOGY ⊃ geometry": "the manifold/shape (torus of wells, links=H₁); a point on it = the orientation = gravity. given, cheap.",
    "OBSERVATION ⊃ spectra": "the fold M(X)=X²; what it extracts = the eigenvalues = light. produced, costs one fold.",
    "duality": "topology/geometry is what's THERE (the structure you stand in); observation/spectra is what LOOKING produces.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("topology/observation typing folded. base now", len(db["base"]))
