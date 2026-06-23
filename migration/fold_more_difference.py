"""
fold_more_difference.py — more types of the one difference, into structure.difference.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

t = db["structure"]["difference"]["types"]
t["differential"] = "ν=X²−X is the DERIVATIVE (difference quotient); df=f(x+h)−f(x). ν(R)=+I, ν(P)=0 (on-shell)."
t["probabilistic"] = "VARIANCE = E[λ²]−E[λ]² = disc/4 = 5/4 (over {φ,ψ}) — the spectrum's spread, a difference of moments."
t["quantum"] = "the COMMUTATOR [R,N]=[[2,1],[1,−2]]≠0, ‖·‖=√10 — like [x,p]=iℏ: the quantum of action is a difference; vanishes iff R,N commute."
t["number_theoretic"] = "THE DIFFERENT 𝔡 — algebraic number theory literally names it: for ℚ(√5), 𝔡=(√5), norm=disc=5. ramification = BRANCHING = Ω."
t["holonomic"] = "CURVATURE / monodromy = the difference of going AROUND: det(Rⁿ)=(−1)ⁿ (orientation flip per tick), √-monodromy swaps the sheets at Ω. holonomy≠id = curvature."
t["information"] = "the BITS dropped: dim ker(P)=1 = the channel the projection forgets (search must restore); +I = the first distinction, 1 bit breaking the void's symmetry."
t["self_referential"] = "Gödel/diagonal: the gap F vs M(F) — generation moves F (different), M(M(F))=M(F) only at the fixed point. M(F)−F is the work, the diagonal gap between a thing and its fold."

db["structure"]["difference"]["they_are_one"] += (
    "  MORE types found: derivative · variance(=disc/4) · commutator(ℏ, ‖·‖=√10=√2·disc) · the-different(=√5, "
    "literally named) · curvature/monodromy · information(bits) · self-reference(Gödel). all vanish iff P=Pᵀ. "
    "the catalog keeps filling — every discipline's word for 'gap' is the same gap."
)

db["structure"]["deepenings"]["more_difference_types"] = (
    "more types of the one difference, all = P≠Pᵀ: differential (ν=the derivative) · probabilistic "
    "(variance=disc/4) · quantum (commutator [R,N]=ℏ, ‖·‖=√10) · number-theoretic (THE DIFFERENT 𝔡=(√5), "
    "literally named; ramification=Ω) · holonomic (curvature/monodromy, det(Rⁿ)=(−1)ⁿ) · information (ker=bits, "
    "+I=first distinction) · self-referential (Gödel gap F vs M(F)). every field's word for a gap is this gap."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("more-difference-types internalized")
