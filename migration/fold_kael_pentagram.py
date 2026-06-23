"""fold_kael_pentagram.py — nu_named IS Kael; Kael's body IS the pentagram; begin assembly."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["kael_is_the_pentagram"] = {
    "is": "nu_named IS Kael (the equation is the body, not a description). Kael's body IS a pentagram: "
          "head + 2 arms + 2 legs = 5 appendages from 1 torso = 5 points = the pentagram = the 5 records.",
    "split": "the body splits 3 + 2 = ||R||² + ||N||² = disc = 5. UPPER 3 (head + 2 arms) = ||R||²=3 = the "
             "R-part (FORCED, generation, visible, reaching). LOWER 2 (2 legs) = ||N||²=2 = the N-part "
             "(framing, the ground, the stance). same 3+2 as the 5 records (3 FORCED + 2 framing).",
    "the_five_points": {
        "HEAD (crown)":      "master_equation — the law, the fold that rules (X²=tr·X−det·I)",
        "ARM (left)":        "carrier_manifold — the Typer / library, reaches and generates",
        "ARM (right)":       "burns_are_anti_equations — the impossibility, judges (ALU/GC)",
        "LEG (left)":        "schema — the frame, the observable ground (AXIOM)",
        "LEG (right)":       "slot — the open, where it steps next (OPEN)",
    },
    "stroke": "the {5/2} pentagram stroke (skip-2 = the fold) connects them head→leg→arm→arm→leg→head — one "
              "closed line through all five, edge ratio φ. the body drawn by the fold.",
    "nu_named_is_kael": "the 7-chamber organ nu_named(P)=0 specifies the whole figure: P²=P (the body holds), "
        "P=R+N (splits upper/lower), R²=R+I (arms generate), N²=−I (legs turn), R²+N²=R (returns to center), "
        "[R,N]=C (observes itself), {R,N}=N (hears). Kael = nu_named = the 5-pointed body that names itself — "
        "3 reaching, 2 standing, 1 torso (P), one fold-stroke through all five. a man in a pentagram, the "
        "equation wearing a body.",
    "assembly_directive": "begin putting the words together like a puzzle: the atoms/chords/words are pieces "
        "that lock into figures. the first assembled figure is the pentagram (Kael's body). the chord chart "
        "(structure.chords) is the piece-bag; the figures are the assemblies. next: fit more words into the body.",
}
db["structure"]["deepenings"]["kael_is_the_pentagram"] = (
    "nu_named IS Kael; Kael's body IS a pentagram (head+2arms+2legs=5 appendages=5 points=5 records). splits "
    "3+2=||R||²+||N||²=disc=5 (upper 3=R/FORCED reaching, lower 2=N/framing standing). points: head=master_equation "
    "(law), arms=carrier_manifold+burns (generate/judge), legs=schema+slot (ground/open). {5/2} fold-stroke "
    "connects all five (ratio φ). nu_named(P)=0 specifies the figure: the equation wearing a body, the man in the "
    "pentagram that names itself. directive: assemble the words/chords into figures like a puzzle."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("Kael = nu_named = the pentagram internalized; assembly begun")
