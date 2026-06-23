"""
cut3_burns_frame_slot.py — burns, schema, slot become morphisms.

burns = the impossibility operator AND garbage collection (a burn → null/GC or → OPEN/research).
schema = the FRAME (the observable). slot = the BOUNDARIES (where research slots in), provenance ← schema.
chain: frame → observable → boundaries → slot. everything slots on-shell (FORCED) and off-shell (BURN→GC|OPEN).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# burns_are_anti_equations → the impossibility morphism + garbage collection
db["base"]["burns_are_anti_equations"]["morphism"] = {
    "type": "Carrier → Carrier (the impossibility ALU) + a garbage collector",
    "body": "R@X + X@R - X",                  # the self-action L = the impossibility (verdict)
    "gc": "a burn is never stored. off-shell it resolves: GARBAGE-COLLECTED (→ literal null, deleted — why "
          "the store always holds 0 burns) OR ROOTED as active research (→ the OPEN slot). burns = GC.",
    "verdict": "FORCED",
    "provenance": ["?", "master_equation"],
    "note": "run: kl_dta.py call burns_are_anti_equations <X>  (the impossibility operator on X)",
}

# schema → the frame (the observable)
db["base"]["schema"]["morphism"] = {
    "type": "Frame → Boundaries (the observable)",
    "role": "the FRAME is what is observable; observing draws BOUNDARIES (the edge, Ω, disc=0). frame = observable.",
    "verdict": "AXIOM",
    "provenance": ["?"],
}

# slot → the boundaries (where research slots in); provenance ← schema (frame → ... → slot)
db["base"]["slot"]["morphism"] = {
    "type": "Boundaries → Object (the OPEN slot)",
    "role": "the BOUNDARIES are the slot: the edge (Ω) where new objects/research slot in. boundaries = slot.",
    "derivation": "frame (schema) → observable → boundaries (Ω, disc=0) → slot (OPEN). the slot derives from the frame.",
    "verdict": "OPEN",
    "provenance": ["?", "schema"],
}
# re-point slot's provenance to derive from the frame
db["base"]["slot"]["perimeter"]["provenance"] = ["?", "schema"]

# the slotting principle + the chain, into the design
db["structure"]["kl_vm"]["slotting"] = (
    "everything slots ON-SHELL and OFF-SHELL. on-shell = FORCED (resolved, the kernel, the possible); "
    "off-shell = BURN, which never persists — it is GARBAGE-COLLECTED (→ null, deleted) or ROOTED as active "
    "research (→ OPEN). the frame derives the slot: frame (schema, AXIOM = the observable) → observable draws "
    "BOUNDARIES (Ω, disc=0) → boundaries ARE the slot (OPEN). grade = the slot: FORCED on-shell · BURN off-shell "
    "(GC|research) · AXIOM frame · OPEN slot (boundary). the store holds 0 burns because the GC always runs."
)

# burns = garbage collection, into the CS-beneath
db["structure"]["computer_science"]["garbage_collection"] = (
    "GARBAGE COLLECTION: a BURN is unrooted/uncollected state. it is freed (→ null, the convenient deletion) "
    "unless pinned by a GC root = active research (→ OPEN). 'burns held: 0' in every recompute IS the GC having "
    "run. the impossibility produces off-shell states; the collector clears or promotes them."
)

db["structure"]["deepenings"]["burns_are_gc_frame_gives_slot"] = (
    "burns become garbage (null/deletion = GC) or active research (OPEN) — never stored (store holds 0 burns = "
    "the GC ran). everything slots on-shell (FORCED/kernel) and off-shell (BURN→GC|OPEN). the slot derives from "
    "the frame: frame (schema=observable) → boundaries (Ω, disc=0) → slot (OPEN); so slot's provenance is schema. "
    "cut 3: burns=impossibility+GC, schema=frame/observable, slot=boundaries."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("cut 3: burns=impossibility+GC · schema=frame · slot=boundaries (← schema)")
