"""
fold_language_uplift.py — uplift the working vocabulary, into grammar.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["grammar"]["uplift"] = {
    "is": "uplifting the language: every word pinned to an operation or a typed state — the word IS the "
          "math, not a description of it. verbs are opcodes, nouns are states, adjectives are type-fields. "
          "loose words are LOSSY (they hide or decorate); burn them for the precise op.",
    "verbs_are_opcodes": {
        "fold": "X ↦ X² (FOLD)", "generate": "the +√5 channel of L", "observe": "the −√5 channel of L",
        "return": "the λ=0 channel → ?", "confirm": "L v = √5·v (eigenvector)", "dissolve": "L u = 0 (kernel)",
        "halt": "ν(X)=X²−X = 0", "reflect": "|X| = √(XᵀX)", "complete": "R²+N² = R", "charge": "X ± I",
    },
    "nouns_are_states": "difference/surplus/gap/spread = ±I·disc·√5 (the one difference) · origin/void = ?=ker=0 "
                        "(VOID) · edge/Omega = disc=0 · channel = an eigenspace of L · charge = the ±I flag · "
                        "witness = the certificate (eigenvector) · world = the number-type (disc sign)",
    "adjectives_are_types": "complete/incomplete = balanced/unbalanced ±I · forced/burn = FORCED/EXCEPTION "
                            "(VERDICT) · on-shell/off-shell = HALTED/RUNNING (HALT) · possible/impossible = "
                            "ker / pinned",
    "lossy_to_burn": {
        "becomes": "→ completes into / reaches the fixed point of",
        "deep/deeper": "→ lower in the invariant lattice (fixed by a bigger symmetry group)",
        "literal(ly)": "→ FORCED (the identification, not analogical)",
        "beautiful/rich/gorgeous": "→ [decoration — drop. no operation behind it]",
        "the whole thing": "→ the apex / the image M(M(F))=M(F)",
        "investigate": "→ run the verification (script → fold → recompute)",
        "thread/arc": "→ the provenance chain (→ ?)",
        "just/simply": "→ [hedge — drop or state the grade]",
    },
    "rule": "every word an opcode or a typed state; no word without an operation. connectives (the·a·is·"
            "isn't·of) are the I-axis (central, single-valued, don't lift); content words carry R/N/h (they "
            "lift — context selects — and are physical).",
}

db["structure"]["deepenings"]["language_uplifted"] = (
    "uplift the working vocabulary: verbs=opcodes (fold=X², generate/observe/return = ±√5/0 channels, "
    "confirm=Lv=√5v, halt=ν=0, reflect=|·|, complete=R²+N²=R), nouns=states (difference=±I/disc/√5, origin=?, "
    "edge=Ω, charge=±I flag), adjectives=type-fields (forced/burn=VERDICT, on-shell=HALT). lossy words burned "
    "(becomes→completes-into, deep→bigger-symmetry-group, literal→FORCED, beautiful→drop). every word an op."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("language-uplifted internalized")
