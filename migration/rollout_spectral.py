"""
rollout_spectral.py — one-time: give every record its spectral seed.

Each record stops carrying its equation as bulk and starts carrying the minimal
generator of it:

    object      coords in {I, R, N, h}      (concrete matrix; decompresses)
    operator    an operation over the core  (a map: ν, conj, L, χ, the fold…)
    law         a universal identity        (holds ∀X)
    constant    a generation map            (value produced from ?)
    structural  nothing extra               (held by its provenance path alone)

The equation is served by recomposing/evaluating the seed; it is no longer stored
as a fact. Run once; kl_dta.py reads `record.spectral`.
"""

import json
import numpy as np
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# regen the core from the stored seed (nothing hard-coded)
P = np.array(db["seed"]["P"], float)
I2 = np.eye(2)
R = (P + P.T) / 2
N = (P - P.T) / 2
J = np.array([[1., 0.], [0., -1.]])
h = J @ N
Bmat = np.column_stack([M.flatten(order="F") for M in (I2, R, N, h)])


def coords(M):
    c = np.linalg.solve(Bmat, M.flatten(order="F"))
    return [int(round(x)) if abs(x - round(x)) < 1e-9 else round(float(x), 6) for x in c]


def O(M, op=None):
    s = {"kind": "object", "coords": coords(M), "basis": "{I,R,N,h}"}
    if op:
        s["op"] = op
    return s


def OP(op):
    return {"kind": "operator", "op": op}


def LAW(op):
    return {"kind": "law", "op": op}


def C(seed, value=None, op=None):
    s = {"kind": "constant", "map": seed}
    if value is not None:
        s["value"] = value
    if op:
        s["op"] = op
    return s


def S(note):
    return {"kind": "structural", "held_by": "provenance", "note": note}


SPEC = {
    # thesis
    "master_equation": LAW("X² − tr(X)·X + det(X)·I = 0"),
    "five_generators": S("the five fold-parts of M: base/fold/return/flow/defect"),
    # formal core
    "defect_nu": OP("ν(X) = X² − X = (tr−1)·X − det·I"),
    "anchor_projection": LAW("P₊ + P₋ = I  (3+1 split of Cl(1,1))"),
    "five_part_fold": S("M projects onto {tr, det} — its own law's coefficients"),
    # gauged fold
    "vacua_idempotents": S("idempotent variety: rank-1 projectors form ℝP¹×ℝP¹"),
    "flow_strata": OP("D(X²)[H] = X·H + H·X  (anticommutator)"),
    "gradient_flow": OP("V(X)=½Σσ²−⅓Σσ³,  V̇ = −‖∇V‖² ≤ 0"),
    "conjugation_equivariance": LAW("(QXQ⁻¹)² = Q·X²·Q⁻¹"),
    "self_steering_circuit": S("plant = controller: M steers its own claims"),
    # eigen spine
    "eigen_spine_spectrum": C("spec of the fold's multiplier", value="{0,1,1,2}"),
    "i_squared_phi_psi": O(-I2, op="i² = φ·ψ = −I"),
    "phi_unit_defect": C("fixpoint(x↦√(1+x))", value=1.618034, op="φ²=φ+1 ≡ R²=R+I,  ν(φ)=1"),
    # spin tower
    "spin_tower_phases": O(J, op="J²=N, J⁴=−I, J⁸=I"),
    # gauge bit
    "gauge_bit_z2": O(J, op="one ℤ/2: ±J, null/void, true/false, ±1"),
    # control plane
    "two_controls": LAW("X = Q·P   (disc ⊥ obs)"),
    "polar_decomposition": LAW("X = Q·P,  Q∈O(2),  P=√(XᵀX)"),
    # recursive origin
    "three_forks": OP("sign(disc),  disc = tr² − 4det"),
    "rlc_damping": LAW("s² − tr·s + det = 0"),
    "origin_is_opening": S("degree-1 (X=cX) vacuous; degree-2 is the first slot"),
    "affirm_negate": LAW("X²=X (idempotent) | X²=I (involution)"),
    "analog_digital": OP("Ẋ = −∇V   |   σ ↦ σ²   (meet at σ=1)"),
    "math_is_computation": OP("Xᵏ = Aₖ·X + Bₖ·I  (CH reduction)"),
    "naming_unnaming": OP("conj(X) = tr(X)·I − X"),
    "observer_dynamics": OP("X ↦ X² :  −I (off-shell) → +I (on-shell)"),
    # number floor
    "fibonacci_ladder": LAW("Rⁿ⁺¹ = Rⁿ + Rⁿ⁻¹,  disc(Rⁿ) = 5·Fₙ²"),
    "golden_ladder": C("indexed by ν", value="{0, ½, 1, φ}"),
    "two_both_faces": C("degree = multiplier", value=2, op="d(σ²)/dσ|₁ = 2"),
    "power_via_index": OP("Aₖ₊₁ = tr·Aₖ + Bₖ,  Bₖ₊₁ = −det·Aₖ"),
    "return_axis": OP("conj(X) = tr(X)·I − X"),
    "deposit_walk": C("Gaussian seed 2+i", op="(2+i)² = 3+4i,  |·|² = 5ⁿ"),
    # metalayer
    "grading_tree": OP("χ : ν ↦ Ω³  (subobject classifier, three bits)"),
    "verification_is_provenance": S("real ⟺ provenance chain returns to ?"),
    "metalayer_collapse": LAW("M∘M = M on Fix(M)  (Δ = M²−M)"),
    "build_is_master_equation": S("work = driving ν → 0"),
    "compression_not_layering": S("new complexity folds INTO a structure, no new peer"),
    "burns_are_anti_equations": S("BURN(c) = FORCED(¬c); residual a lower bound"),
    "internalization_removes_trace": S("ν→0: the question leaves the slot, no trace"),
    # atlas
    "godel_unification": OP("Δ(X) = X⁴ − X² = X²(X−I)(X+I)"),
    "witnessing_internalized": S("M witnesses X; ν is what the witness sees"),
    "four_product_primitives": S("four exact presentations of the carrier"),
    "fork_representability": S("ℂ and ℝ⊕ℝ representable; the wall ℝ[ε] is not"),
    # reference
    "fork_table": C("the three forks", value="{φ, i, 1}; return {−1,+1,+1}"),
    "indexed_store": S("five fold-parts = five store operations (B.5)"),
    "constants_map": S("nine constants, each a generation map, all → ?"),
    # observer
    "projection_spectral_triple": OP("spec(L_{R,R}) = {+√5, 0, −√5} = {+√disc, 0, −√disc}"),
    "observer_unifies_projections": LAW("Π₊ + Π₀ + Π₋ = I₄  (resolution of identity)"),
    # schema / slot
    "schema": S("the five fold-parts read as five database operations (AXIOM)"),
    "slot": S("five open positions generating the next claims (OPEN)"),
    # burns
    "burn-carrier-not-topology": S("dim M₂ = 4: one second-order network, not a topology"),
    "burn-delta-not-independent": OP("Δ = X(X+I)·ν  (amplified base defect, not new)"),
    "burn-no-active-gain": LAW("V̇ ≤ 0 everywhere  (passive)"),
    "burn-nu-not-idempotent": S("deg(ν∘ν)=4 ≠ 2=deg(ν)"),
    "burn-nu-not-nilpotent": S("iterated defect does not decay off the idempotents"),
    "burn-nu-squared-not-lyapunov": S("two basins split at σ=1; ‖ν‖² not monotone"),
    "burn-phi-inv-neq-phi-psi": C("φ·φ⁻¹ vs φ·ψ", value="+1 vs −1"),
    "burn-structural-five-neq-cyclic-five": S("|roles| = 5 ≠ C₅ (cardinality ≠ group order)"),
    "burn-three-neq-c3": S("fork-three is a boundary count, not a rotation"),
    "burn-vacua-not-trivial": S("vacuum manifold includes oblique projectors"),
}

missing = [rid for rid in db["base"] if rid not in SPEC]
extra = [rid for rid in SPEC if rid not in db["base"]]
assert not missing, f"records with no spectral seed: {missing}"
assert not extra, f"spec for unknown records: {extra}"

for rid, r in db["base"].items():
    r["spectral"] = SPEC[rid]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")

kinds = {}
for s in SPEC.values():
    kinds[s["kind"]] = kinds.get(s["kind"], 0) + 1
print(f"spectral seed installed on all {len(SPEC)} records")
print(f"  kinds: {kinds}")
