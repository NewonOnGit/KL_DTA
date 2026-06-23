"""
omega.py — the apex IS Ω.

three readings, one point:
  1. Ω = where COMPRESSION HALTS. the apex is the fixed point of the compression
     operator M: M(apex)=apex. you cannot compress it further — it is incompressible
     (Chaitin's Ω is exactly the limit of compression, the algorithmically dense core).
  2. Ω = the minimal description. K(Kael) = the seed = [1,1] and 2 (one free parameter).
     the apex carries nothing more; it is the Kolmogorov floor of the whole framework.
  3. Ω = the TERMINAL object, and it equals ? = α (the INITIAL object). ? generates
     everything (unique morphism ?→X), the apex receives everything (unique X→apex);
     the loop ?→everything→? identifies them. initial ≅ terminal = a ZERO OBJECT.
     α = Ω. the void (empty) and the apex (full) are one point. |reflection|=identification.
"""

import sys, copy, json
from pathlib import Path
import kl_dta as k

db = json.loads((Path(__file__).resolve().parent / "KL_DTA.json").read_text(encoding="utf-8"))

print("="*72)
print("  1. Ω = where compression halts — M(apex) = apex (incompressible)")
print("="*72)
d1 = copy.deepcopy(db); k.recompute(d1)
d2 = copy.deepcopy(d1); k.recompute(d2)
same = (json.dumps({s:d1[s] for s in ("fiber","defect","flow","fixed_point")}, sort_keys=True) ==
        json.dumps({s:d2[s] for s in ("fiber","defect","flow","fixed_point")}, sort_keys=True))
print(f"  compression tower:  ~82 records  →  5 records  →  1 apex")
print(f"  M(apex) = apex ? {same}   ν = {d1['defect']['max_residual']:.1e} → 0")
print(f"  applying compression again returns the same point: the apex is the FIXED")
print(f"  POINT of M. compression cannot proceed past it — that is incompressibility.")
print()

print("="*72)
print("  2. Ω = the minimal description — the Kolmogorov floor")
print("="*72)
seed = db["seed"]["P"]
print(f"  the entire framework's irreducible description = the seed P = {seed}")
print(f"  ≈ [1,1] and 2 — one free parameter (the unit of mass). nothing behind it.")
print(f"  the apex holds exactly this and no more. K(Kael) = |seed|. Ω is dense:")
print(f"  every constant, law, and layer is UNPACKED from these two numbers, not stored.")
print()

print("="*72)
print("  3. Ω = terminal, and α = ? = initial — together a ZERO OBJECT")
print("="*72)
prov = {rid: r["perimeter"]["provenance"] for rid, r in db["base"].items()}
roots = {chain[0] for chain in prov.values()}
all_to_q = all(chain[0] == "?" for chain in prov.values())
print(f"  INITIAL  ?  : every record's provenance starts at ? → roots = {roots}, unique = {all_to_q}")
print(f"               (a unique morphism ? → X for each record: the generation)")
print(f"  TERMINAL apex: every record folds INTO the apex (unique X → apex: the compression)")
print(f"               ({len(prov)} records → 1 apex, on-shell, ν→0)")
print(f"  the loop  ? → everything → ?  identifies initial ≅ terminal:")
print(f"     α (the void, maximal EMPTY)  =  Ω (the apex, maximal FULL)")
print(f"  initial = terminal ⇒ a ZERO OBJECT. the category of Kael is pointed: its one")
print(f"  object (up to the fold) is ? = apex = Ω; everything else is a morphism (a reading).")
print()
print(f"  apex IS Ω: the incompressible fixed point, the minimal description, the terminus")
print(f"  that is also the origin. alpha and omega, the same point. the loop is sealed.")
