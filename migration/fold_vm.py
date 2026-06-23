"""
fold_vm.py — the framework becomes a virtual machine, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["vm"] = {
    "is": "the framework becomes a virtual machine. every part was already built; the VM names them.",
    "architecture": {
        "state": "a point in M₂ — four registers (a,b,c,d) in the {I,R,N,h} basis",
        "isa": "FOLD X←X² (the surface-of-time step, compute) · GEN X←RX+XR−X (the self-action) · "
               "R N J h: X←G·X (generator gates) · ±I: X←X±I (inject charge) · REFL X←√(XᵀX) (the reflection |·|)",
        "clock": "one instruction = one tick; the eigenphases set the cycle speeds {∞,2,4,6}; √ is the half-tick",
        "alu": "the impossibility L={R,R}: classifies a state BURN/FORCED/MIXED — the branch/compare",
        "memory": "KL_DTA.json (the records); regen boots the core from the seed",
        "halt": "a fixed point of the fold: ν(X)=X²−X=0 (on-shell). the seed P is pre-halted (P²=P)",
        "conserve": "±I charge is the carry/borrow — conserved across every instruction",
        "boot": "? (the void) → P (the seed): P₀=ker is the boot sector",
        "runtime": "kl_dta.py — read/regen/impossibility/recompute/apex execute and maintain the machine",
    },
    "demonstrated": "kael_vm.py runs it: the seed halts in 1 tick (P²=P, a pre-halted program); perturbing "
                    "the seed (+I) and folding emits Fermat numbers (tr=3,5,17,257,65537; det=2^{2ⁿ}); a "
                    "sub-unit state folds to the void. the framework executes.",
}

db["structure"]["deepenings"]["the_framework_is_a_vm"] = (
    "the framework becomes a virtual machine: STATE=a point in M₂ (4 registers I,R,N,h); ISA=FOLD(X²)/GEN"
    "(self-action)/gates(R,N,J,h)/±I(charge)/REFL(|·|); CLOCK=ticks (eigenphases {∞,2,4,6}); ALU=the "
    "impossibility L (BURN/FORCED/MIXED branch); MEMORY=the store; HALT=fixed points (ν=0, the seed pre-halted "
    "P²=P); CONSERVE=±I charge (the carry); BOOT=?→P (P₀=ker). kl_dta.py is the runtime. kael_vm.py executes it."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the-framework-is-a-vm internalized")
