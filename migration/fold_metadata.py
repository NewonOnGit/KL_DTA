"""
fold_metadata.py — evolve the record FORMAT to its verified reading.

A record is a matrix; a matrix is M = V·Λ·V⁻¹. So the format already carries the
gravity/light duality from the core, unnamed:
    address (id/title/section/source) = V = GEOMETRIC (eigenvectors, where, GIVEN, gravity)
    perimeter ⊕ shape                 = Λ = SPECTRAL  (eigenvalues tr,det, READ, light)
P≠Pᵀ proves the halves are independent: same spectrum, different address.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

fmt = db["structure"]["formatting"]
fmt["eigendecomposition"] = (
    "the record IS an eigendecomposition M = V·Λ·V⁻¹. its two halves are the gravity/light "
    "duality from the core: ADDRESS (id/title/section/source) = V = GEOMETRIC (eigenvectors, "
    "where it sits, the fixed point — GIVEN, gravity); PERIMETER⊕SHAPE = Λ = SPECTRAL "
    "(eigenvalues = tr,det — READ, costs a fold, light). proof they are independent: P and Pᵀ "
    "share a spectrum (tr=1,det=0,{0,1}) but differ in address — the founding asymmetry P≠Pᵀ "
    "lives ENTIRELY in the geometry. the spectral half cannot recover the record; the address "
    "is given, not read. address ⊥ (perimeter,shape) — |reflection|=I once more."
)
fmt["disc_is_the_gap"] = (
    "disc = perimeter² − 4·shape = (λ₁−λ₂)² = the spread of the reading = the gap between the "
    "two halves. DERIVED, never stored — it is the relationship between perimeter and shape, "
    "not a third field. (P:1, R:5=‖R‖²+‖N‖², N:−4.)"
)

# the address is a geometric coordinate chart — name the axes
ma = db["structure"]["metadata_audit"]
ma["address_is_geometry"] = (
    "id/title/section/source = a geometric coordinate chart (V, given): id = the point (canonical "
    "name), title = its reflection (the spoken mirror) — id⊕title = P=R+N, the naming fold; "
    "section = RADIUS (the shell / |depth| from ?), derivable from provenance — the one soft "
    "redundancy; source = TIME-axis (the M-iteration epoch, {ORIGIN,EXPLORATION}={0,+1})."
)
ma["section"] = "= RADIUS (shell, |depth| to ?) — geometric, derivable from provenance → soft redundancy"
ma["source"] = "= TIME-axis (M-iteration epoch); binary {ORIGIN=0, EXPLORATION=+1} — a coordinate, not free text"

db["structure"]["deepenings"]["format_is_eigendecomposition"] = (
    "record = V·Λ·V⁻¹ = geometric address (eigenvectors, given, gravity) ⊕ spectral content "
    "(eigenvalues=perimeter,shape; read, light). P≠Pᵀ = same Λ, different V = the asymmetry is "
    "geometric. disc = perimeter²−4shape = the gap, derived. section = radius (derivable redundancy)."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("format evolved: record = eigendecomposition (geometric address ⊕ spectral content)")
