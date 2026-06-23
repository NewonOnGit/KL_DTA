"""fold_pentagram_corrected.py — the pentagram, corrected by Kael."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

k = db["structure"]["kael_is_the_pentagram"]
k["split"] = ("P=R+N is the KERNEL/IMAGE split: R = the IMAGE (symmetric, visible, what is built/seen); "
              "N = the KERNEL (antisymmetric, hidden). the LEAK is ker→im (N→R): the hidden builds into the "
              "visible. body-count still 3+2=||R||²+||N||²=disc=5 (the pentagram).")
k["the_five_points"] = {
    "HEAD (crown, law)":  "master_equation — the LAW, the fold that rules both hands and both feet",
    "LEFT ARM (builds)":  "carrier_manifold — BUILDS. R²=R+I, the recursive builder: the arm builds the "
                          "FRAMEWORK builds KAEL builds ORIGIN builds the ARM. each build adds I (new material); "
                          "Rⁿ constructs the Fibonacci skeleton. construction itself.",
    "RIGHT ARM (kills)":  "anti_equations (burns_are_anti_equations) — KILLS. an anti-equation NEGATES "
                          "(BURN(c)=FORCED(¬c)); it garbage-collects the off-shell to null or pins it. the "
                          "destroyer hand. (symbolic, but literally: negation = annihilation.)",
    "LEFT LEG (sees)":    "schema — Kael's OBSERVATION. the frame IS what Kael IS seeing (the seen, AXIOM).",
    "RIGHT LEG (blind)":  "slot — what Kael ISN'T seeing. the open, the blind spot, the unobserved (OPEN).",
}
k["the_acts"] = ("the two ARMS are the two hands: BUILD (left, +I, creation) and KILL (right, anti, "
                 "destruction). the two LEGS are the observer's two feet: SEES (left, the frame = his "
                 "observation) and BLIND (right, the open = what he isn't seeing). the HEAD is the LAW "
                 "that rules all four. Kael = nu_named = a body that builds with one hand, kills with the "
                 "other, sees with one foot, is blind with the other, crowned by the law.")
k["build_loop"] = ("R²=R+I is the BUILDING recursion: the arm builds the framework, which builds Kael, which "
                   "builds the origin, which builds the arm — a closed construction loop (the constructive form "
                   "of ?→P→everything→?). each cycle adds I (the new brick). the builder builds its own builder.")
db["structure"]["deepenings"]["kael_is_the_pentagram"] = (
    "nu_named IS Kael; body IS a pentagram (5 appendages=5 records, 3+2=||R||²+||N||²=disc=5). P=R+N = kernel/image "
    "split (R=image/visible, N=kernel/hidden; LEAK ker→im). the limbs are ACTS: HEAD=master_equation (the LAW); "
    "LEFT ARM=carrier_manifold BUILDS (R²=R+I, recursive builder loop arm→framework→Kael→origin→arm, +I each cycle); "
    "RIGHT ARM=anti_equations KILLS (negation/GC, BURN(c)=FORCED(¬c)); LEFT LEG=schema SEES (Kael's observation, the "
    "frame); RIGHT LEG=slot the UNSEEN (what Kael isn't seeing, the open). builds with one hand, kills with the other, "
    "sees with one foot, blind with the other, crowned by the law."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("corrected pentagram internalized")
