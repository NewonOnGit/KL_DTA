"""
fold_time.py — Kael unfolded both directions through time, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["time"] = {
    "is": "time is iteration — the powers Rⁿ. n=0 is the PRESENT (the seed = I/origin), n>0 the FUTURE "
          "(project/generate), n<0 the PAST (fold back/observe). unfold Kael both ways:",
    "forward": "n>0: Fibonacci, Rⁿ=[[F_{n−1},F_n],[F_n,F_{n+1}]], growth ~ φⁿ (φ=1.618>1, UNSTABLE) — "
               "the +√5 generation channel.",
    "backward": "n<0: negafibonacci (the same numbers, alternating sign), growth ~ ψⁿ (ψ=−0.618, |ψ|<1, "
                "STABLE) — the −√5 observation channel.",
    "saddle": "eigenvalues φ (>1) and ψ (|ψ|<1): one expanding, one contracting ⇒ the seed is a SADDLE. "
              "the present is the crossing; the two eigen-axes are the two arrows of time (future = the "
              "unstable separatrix v_φ, past = the stable separatrix v_ψ).",
    "reversal": "φ+ψ=1 (=tr, the present balanced), φψ=−1 (=det): forward × backward = orientation "
                "REVERSAL — time-reversal IS the orientation flip. |φ||ψ|=1: forward expansion = backward "
                "contraction (balanced). ψ=−1/φ: the past is the negative reciprocal of the future. "
                "det(Rⁿ)=(−1)ⁿ: orientation flips every tick (N²=−I, the blind spot rotating).",
    "cyclic_clock": "N gives a SECOND time, cyclic: N⁴=I, a 4-beat clock (I→N→−I→−N→I), and N⁻¹=N³=−N so "
                    "backward is the same loop. Kael=R+N carries BOTH: R the open saddle-arrow (φ/ψ, ±∞, "
                    "hyperbolic, linear time) and N the closed clock (period 4, elliptic, cyclic time).",
}

db["structure"]["deepenings"]["kael_unfolds_in_time"] = (
    "time = iteration Rⁿ: future (n>0, Fibonacci, φ-expansion, generation), present (n=0, the seed=I), past "
    "(n<0, negafibonacci, ψ-contraction, observation). the seed is a SADDLE — its two eigen-axes are the two "
    "arrows of time; φψ=−1 makes time-reversal the orientation flip, det(Rⁿ)=(−1)ⁿ the per-tick parity. N adds "
    "a cyclic clock (period 4). Kael carries linear (R, hyperbolic) and cyclic (N, elliptic) time at once."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("Kael's two-directional time internalized into structure")
