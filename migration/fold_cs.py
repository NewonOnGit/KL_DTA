"""
fold_cs.py — the computer science beneath the math, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["computer_science"] = {
    "is": "beneath the math: a self-hosting, memoized, fixed-point computation whose verdict is a proof "
          "system and whose asymmetry is irreversible. each structure was already running.",
    "y_combinator": "FIXED-POINT COMBINATOR: P²=P (the seed is its own fixed point), M(M(F))=M(F) "
                    "(self-hosting). self-application reaching a fixed point is Y.",
    "power_iteration": "POWER ITERATION / PageRank: the burn IS the dominant-eigenvector fixed point — "
                       "'impossibility confirming itself' is v ← Lv/√5, which fixes the eigenvector (the "
                       "power method finding a principal direction).",
    "memoization": "IDEMPOTENCE = MEMOIZATION/CACHING: P²=P (apply twice = once, cacheable); the derived "
                   "sections M(base) are a regenerable cache; M(M(F))=M(F) means the cache is sound.",
    "hashing": "HASHING: (tr,det) is a lossy hash — hash(P)=hash(Pᵀ)=(1,0) is a COLLISION (P≠Pᵀ). computing "
               "the hash is cheap (forward); recovering the matrix (preimage) needs the eigenvectors — the "
               "hard inverse. hash vs preimage = compute vs search = P vs NP.",
    "landauer": "LANDAUER / IRREVERSIBILITY: det(P)=0, dim ker=1 — the fold ERASES a bit (ker→0, "
                "one-directional). erasing a bit raises entropy; the +I surplus is that bit; irreversibility "
                "(the LEAK ker→im) is the arrow of time. computation that forgets has a direction.",
    "curry_howard": "CURRY–HOWARD: witness = proof = program. FORCED = the type is INHABITED (a proof/term "
                    "exists, ν→0); BURN = the type is EMPTY (refuted, pinned); AXIOM = assumed; OPEN = goal. "
                    "the verdict (ALU) is a proof checker; the GRADE is provability. propositions are types.",
    "quine": "QUINE: recompute reproduces the store exactly — a program whose output is its own source. "
             "M(M(F))=M(F) is the quine equation.",
}

db["structure"]["deepenings"]["computer_science_beneath"] = (
    "the CS beneath the math: Y-combinator (P²=P, M(M(F))=M(F), self-hosting) · power iteration/PageRank (the "
    "burn = dominant-eigenvector fixed point, v←Lv/√5) · memoization (idempotence P²=P = caching) · hashing "
    "((tr,det) lossy, P/Pᵀ collision, preimage=hard=P vs NP) · Landauer (det P=0 erases a bit = arrow of time) "
    "· Curry–Howard (witness=proof, grade=provability, FORCED=inhabited/BURN=empty) · quine (output=source). "
    "the framework was doing computer science the whole time."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("computer-science-beneath internalized")
