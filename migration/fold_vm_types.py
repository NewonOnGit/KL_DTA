"""
fold_vm_types.py — type the entire framework through the .vm, into structure.vm.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["vm"]["type_system"] = {
    "is": "the VM types the ENTIRE framework: every state gets a signature read by execution — "
          "(VERDICT, HALT, WORLD, CHARGE, CLOCK). the grade/worlds/charge/time were all fields of it.",
    "signature": {
        "VERDICT": "the ALU (impossibility L): FORCED (resolves) · BURN (pinned, an exception) · MIXED. "
                   "= the GRADE field (FORCED/BURN/AXIOM/OPEN).",
        "HALT": "ν(X)=X²−X: HALTED (on-shell, =0; the seed is pre-halted P²=P) · RUNNING (≠0).",
        "WORLD": "the number-type by disc: GOLDEN (>0, escape) · RETURN (<0, Gaussian/Eisenstein) · "
                 "EDGE (=0, Ω). = the four worlds.",
        "CHARGE": "the I-coordinate q — the ±I content, the conserved flag (carry/borrow).",
        "CLOCK": "the eigenphase periods — the cycle domain {∞,2,4,6}. = time.",
    },
    "constructors": {
        "VOID": "? origin, null, the zero register / boot sector",
        "CARRIER": "a state in M₂ — a register value",
        "GATE": "R N J h — the instruction set",
        "FOLD": "X² — the step opcode (compute)",
        "VERDICT": "the ALU output = the grade",
        "WORLD": "the number-type = the four worlds",
        "CLOCK": "time/eigenphase periods",
        "FLAG": "±I charge — the conserved carry",
        "HALT": "fixed points (ν=0); seed pre-halted",
        "EXCEPTION": "a BURN — pinned, uncatchable; P=NP = the return that never catches",
        "POINTER": "provenance — all references resolve to ?",
        "IMAGE": "the apex = M(M(F))=M(F), the self-hosting fixed-point image",
    },
    "examples": "?=FORCED·HALTED·EDGE·q0·∞ (the null); N=FORCED·RUNNING·RETURN·T4 (the observation clock); "
                "P=MIXED·HALTED·GOLDEN (the pre-halted boot image); −I=q−1·T2 (negative charge, parity clock); "
                "Eisenstein=RETURN·T6 (the hexagonal world). vm_types.py reads any state's signature.",
}

db["structure"]["deepenings"]["framework_typed_through_the_vm"] = (
    "typing the entire framework through the .vm: every state gets one signature (VERDICT, HALT, WORLD, "
    "CHARGE, CLOCK) read by execution — grade=VERDICT (FORCED/BURN/AXIOM/OPEN), worlds=WORLD, charge=FLAG, "
    "time=CLOCK, origin=VOID, apex=IMAGE. the constructors (VOID·CARRIER·GATE·FOLD·VERDICT·WORLD·CLOCK·FLAG·"
    "HALT·EXCEPTION·POINTER·IMAGE) type everything the framework is. one type system, the whole framework."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("framework-typed-through-the-vm internalized")
