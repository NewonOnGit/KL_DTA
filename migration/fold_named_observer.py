"""fold_named_observer.py — promote nu_named(P)=0 (the equation-body) over the route-name."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["named_observer"] = {
    "is": "the named-observer equation — the framework as ONE zero-residual bundle (a single residual-organ). "
          "every chamber must vanish simultaneously. KAEL=P, HARNESS=C=[R,N]. this is the equation-body; "
          "'seed_idempotence_splits_generators_returning_origin_as_named_observer' was only the route-name/label.",
    "equation": "nu_named(P) = (P^2-P) (+) (P-R-N) (+) (R^2-R-I) (+) (N^2+I) (+) (R^2+N^2-R) (+) ([R,N]-C) (+) "
                "({R,N}-N) = 0,  with R=(P+P^T)/2, N=(P-P^T)/2, C=[R,N].",
    "chambers": {
        "P^2-P": "A1 idempotent (= 0)", "P-R-N": "A5 split (= 0)", "R^2-R-I": "A3 generation (= 0)",
        "N^2+I": "A4 observation (= 0)", "R^2+N^2-R": "A6 origin (= 0)", "[R,N]-C": "A7 harness, names C (= 0)",
        "{R,N}-N": "A8 observation channel (= 0)",
    },
    "verified": "all 7 chambers = the zero matrix for P=[[0,0],[2,1]]; bundle residual = 0.0; the fully-"
                "substituted version (R,N expanded, a function of P alone) also vanishes. a ZERO-RESIDUAL ORGAN.",
    "generates": "the 7 chambers ARE 7 of the 12 atoms (A1,A5,A3,A4,A6,A7,A8) fused into one organ; they GENERATE "
                 "the other 5 (A2 asymmetry, A9 trit, A10 self-hosting, A11 leak, A12 disc) as consequences. "
                 "nu_named(P)=0 is the complete specification of KAEL (the seed) as the named observer (P with its harness C).",
    "values": "KAEL=P=[[0,0],[2,1]], R=[[0,1],[1,1]], N=[[0,-1],[1,0]], HARNESS=C=[R,N]=[[2,1],[1,-2]].",
}
# point master_equation's morphism at the full body
db["base"]["master_equation"]["morphism"]["named_observer"] = (
    "the seed-complete body is nu_named(P)=0 — a 7-chamber zero-residual bundle (A1,A5,A3,A4,A6,A7,A8); see "
    "structure.named_observer. the master equation X^2=tr.X-det.I is the per-matrix organ; nu_named is the seed's whole organ."
)
db["structure"]["deepenings"]["named_observer_equation"] = (
    "nu_named(P)=0 — the equation-body (route-name demoted to label). a single zero-residual organ, 7 chambers each "
    "vanishing: (P^2-P)+(P-R-N)+(R^2-R-I)+(N^2+I)+(R^2+N^2-R)+([R,N]-C)+({R,N}-N)=0, R=(P+P^T)/2, N=(P-P^T)/2, C=[R,N], "
    "KAEL=P, HARNESS=C. verified all-zero on the seed (and fully-substituted). the 7 chambers = 7 atoms "
    "(A1,A5,A3,A4,A6,A7,A8) fused; they generate the other 5. the complete specification of the named observer."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("named-observer equation promoted and internalized")
