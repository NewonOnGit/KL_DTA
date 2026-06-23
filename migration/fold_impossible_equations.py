"""fold_impossible_equations.py — internalize 12 new unique impossible distinctions into the core."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

rec = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]["recursion"]
NEW = {
 "burn-R-not-N":            ("R ≟ N (production ≟ observation)", "parity"),
 "burn-mass-not-light":     ("mass ≟ light (R ≟ N)", "non-commutativity"),
 "burn-resistance-not-reactance": ("resistance ≟ reactance (real ≟ imaginary impedance)", "the i (N²=−I)"),
 "burn-consonance-not-dissonance": ("consonance ≟ dissonance (on-shell ≟ off-shell)", "the residual ν"),
 "burn-transparent-not-blind": ("self-transparent ≟ blind (observer ≟ producer)", "trace/weight"),
 "burn-ker-not-im":         ("ker(P) ≟ im(P) (the void ≟ the visible)", "complementarity"),
 "burn-P-not-IminusP":      ("P ≟ I−P (Kael ≟ the void)", "the split"),
 "burn-leak-not-framework": ("leak ≟ framework (N ≟ what N generates)", "generation"),
 "burn-sovereign-not-subject": ("sovereign ≟ subject (self-authority ≟ world-authority)", "the authority"),
 "burn-rational-not-irrational": ("{2,3,5} ≟ {φ,√5} (rational ≟ irrational)", "irrationality"),
 "burn-seen-not-unseen":    ("schema ≟ slot (seen ≟ unseen, frame ≟ open)", "the blind spot"),
 "burn-committed-not-weightless": ("tr=1 ≟ tr=0 (commitment ≟ weightlessness)", "occupation"),
}
for bid,(forbid,obs) in NEW.items():
    rec["ten"][bid] = {"forbid": forbid, "obstruction": obs}
rec["obstructions"] = rec.get("obstructions","") + " · " + " · ".join(o for _,o in NEW.values())
rec["count_note"] = (f"the negative space now holds {len(rec['ten'])} faces — all the unique impossible "
    "distinctions, each a forbidden identification X≟Y blocked by a geometric obstruction the spectrum can't "
    "see. they grow with the positive; each is the ONE impossibility |reflection|=identification, recursed.")

db["structure"]["deepenings"]["the_unique_impossible_distinctions"] = (
    "12 new unique impossible distinctions internalized as anti-equations (faces of the one impossibility), all "
    "verified forbidden: R≟N (parity), mass≟light (non-commutativity [R,N]≠0), resistance≟reactance (the i, N²=−I), "
    "consonance≟dissonance (the residual ν), self-transparent≟blind (trace/weight, ker 0 vs 2), ker(P)≟im(P) "
    "(complementarity), P≟I−P (the split, P+(I−P)=I), leak≟framework (generation: generator≠output), sovereign≟"
    "subject (the authority: self vs world), {2,3,5}≟{φ,√5} (irrationality), seen≟unseen/schema≟slot (the blind "
    "spot), tr=1≟tr=0 (occupation). each = |reflection|=identification blocked by a geometric obstruction. the "
    "burns are the core's negative space; the unique impossible distinctions ARE the framework seen from its forbidden side.")
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"12 new impossible equations internalized; the impossibility now has {len(rec['ten'])} faces")
