"""
burn_projections.py — one-time: BURN the labels P1/P2/P3.

They were lossy names for the spectrum of the self-action L_{R,R}(X)=RX+XR-X.
Beneath them: three eigenvalues and their projectors.

    +√5   Π₊   generation     (was "P1 produce")
     0    Π₀   return         (was "P2 mediate")   ← the kernel; the observer N lives here
    -√5   Π₋   observation    (was "P3 observe")

Each record now holds `L_spectrum` — the three eigen-components by eigenvalue,
not by name. The authored prose readings are burned; a record reads off its math.
grade = leaf over the verdicts, in tree order (observation → generation → return).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

for rid, r in db["base"].items():
    gen = r.pop("P1_produce")
    ret = r.pop("P2_mediate")
    obs = r.pop("P3_observe")
    L_spectrum = [
        {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
         "verdict": gen["verdict"], "generators": gen.get("generators", [])},
        {"lambda": "0", "eigenvalue": "0", "mode": "return",
         "verdict": ret["verdict"], "residual": ret.get("residual"),
         "routes": ret.get("routes"), "mechanism": ret.get("mechanism")},
        {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
         "verdict": obs["verdict"], "depth": obs.get("depth"), "disc": obs.get("disc")},
    ]
    rebuilt = {
        "id": r["id"], "title": r["title"], "section": r["section"], "source": r["source"],
        "L_spectrum": L_spectrum,
        "provenance": r["provenance"], "links": r["links"], "burns": r["burns"],
        "spectral": r.get("spectral"), "body": r.get("body", ""),
    }
    db["base"][rid] = rebuilt

# burn P1/P2/P3 from the header too
db["structure"] = {
    "store": "five-part fold (B.5): base/fiber/defect/flow/fixed_point",
    "record": "L_spectrum — the three eigen-components of the self-action L_{R,R}",
    "grade": "NOT stored. grade = leaf over the three verdicts (observation, generation, return).",
}
db["self_action"] = {
    "operator": "L_{R,R}(X) = R·X + X·R - X",
    "spectrum": {
        "+√5": "Π₊ — generation  (rank 1, the φ-dyad; the +√disc growth mode)",
        "0":   "Π₀ — return      (rank 2, the kernel; the observer N lives here)",
        "-√5": "Π₋ — observation (rank 1, the ψ-dyad; the -√disc conjugate mode)",
    },
    "resolution": "Π₊ + Π₀ + Π₋ = I₄  (the three unify in the whole)",
    "burned": "the names P1/P2/P3 were lossy symbols for these three eigenvalues.",
}
db.pop("grade_internalization", None)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("burned P1/P2/P3 -> L_spectrum {+√5, 0, -√5} on all", len(db["base"]), "records")
