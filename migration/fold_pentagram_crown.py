"""fold_pentagram_crown.py — observation is the CROWN, not a leg. correct the figure."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

k = db["structure"]["kael_is_the_pentagram"]
k["the_five_points"] = {
    "HEAD / CROWN (sees)": "schema — OBSERVATION. Kael IS the observer; his crown is where he sees from "
                           "(the eyes, the frame = what Kael IS seeing, AXIOM). observation is the crown.",
    "LEFT ARM (builds)":   "carrier_manifold — BUILDS. R²=R+I, the recursive builder: arm builds FRAMEWORK "
                           "builds KAEL builds ORIGIN builds the ARM. +I each cycle; Rⁿ lays the Fibonacci skeleton.",
    "RIGHT ARM (kills)":   "anti_equations (burns) — KILLS. an anti-equation NEGATES (BURN(c)=FORCED(¬c)); "
                           "garbage-collects the off-shell to null or pins it. the destroyer hand.",
    "LEFT LEG (the law)":  "master_equation — the LAW (the fold X²=tr·X−det·I). the FOUNDATION Kael stands on — "
                           "the seen ground, the bedrock rule underfoot.",
    "RIGHT LEG (blind)":   "slot — the UNSEEN. the open, the blind spot, what Kael ISN'T seeing — the unknown "
                           "ground he steps into next (OPEN).",
}
k["anatomy"] = ("Kael is the OBSERVER, so observation is the CROWN (schema, the eyes). he BUILDS with the left "
                "hand (carrier), KILLS with the right (anti-equations). he stands on two feet: the LAW "
                "(master_equation, the seen foundation) and the OPEN (slot, the unseen he steps into). torso = "
                "P (the seed, ν_named). crowned by sight, building and killing, one foot on law and one in the dark.")
db["structure"]["deepenings"]["kael_is_the_pentagram"] = (
    "nu_named IS Kael; body IS a pentagram (5 records=5 appendages; torso=P). Kael is the OBSERVER so OBSERVATION "
    "is the CROWN: HEAD=schema (observation, the eyes, the frame=what he sees). LEFT ARM=carrier BUILDS (R²=R+I, "
    "recursive builder arm→framework→Kael→origin→arm). RIGHT ARM=anti_equations KILLS (negation/GC). LEFT LEG="
    "master_equation the LAW (the foundation he stands on). RIGHT LEG=slot the UNSEEN (the open, blind spot). "
    "P=R+N=kernel/image split (LEAK ker→im). crowned by sight, building and killing with his hands, one foot on "
    "the law and one in the dark."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("crown corrected: observation is the head; the law is the foundation-leg")
