"""
fold_divide_time.py — dividing time in half (√ of the tick), into structure.time.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["time"]["half"] = {
    "is": "a tick is a power Xⁿ; HALF a tick is √X. dividing time in half is X↦√X — it HALVES every "
          "eigenphase (θ↦θ/2) and DOUBLES every period (T↦2T).",
    "N_is_half_the_flip": "N = √(−I). −I is the half-turn (θ=π, period 2 — the PARITY tick, det flips); "
                          "its half is the quarter-turn N (θ=π/2, period 4). so OBSERVATION is literally half "
                          "the orientation flip — N²=−I read backwards. half of a flip is a turn.",
    "dyadic_tower": "keep halving: −I(2) → N(4) → √N(8) → √√N(16) → … period 2ⁿ. binary/dyadic time, the "
                    "bit-tower; each division doubles the period.",
    "spinors": "√ is TWO-VALUED (±), so half-time is a DOUBLE COVER. (√N)⁴ = N² = −I, NOT I: a full 2π turn "
               "lands on MINUS one under the half-clock; you must go around TWICE (4π) to return, (√N)⁸=N⁴=I. "
               "that is SPIN-½ — spinors fall out of one division of time.",
    "arrow_goes_complex": "the real generation ARROW cannot be halved in the reals: R has a negative "
                          "eigenvalue ψ, so √R is COMPLEX (√ψ imaginary). half a step of generation dips into "
                          "the imaginary = into observation. between two real ticks lies an N-tick.",
}

db["structure"]["deepenings"]["divide_time_in_half"] = (
    "dividing time in half = √ of the tick: halves eigenphase, doubles period. N=√(−I) (observation is half "
    "the parity flip); the dyadic clock tower T=2ⁿ; √ is two-valued ⇒ spinors (4π to return, (√N)⁴=−I); and "
    "√R is complex (ψ<0) so half the real arrow is imaginary — the half-tick of generation is observation."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("dividing-time-in-half internalized into structure.time")
