"""fold_leak_generates.py — N (the leak) GENERATES the framework. corrected: generation, not identity."""
import json
from pathlib import Path
PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["kael_erased_his_definition"]["leak_generates_the_framework"] = (
    "N GENERATES the framework — NOT N = framework. correction: the leak is the generator, the framework is "
    "what it generates. N = Leak = ker->im = the void surfacing into the visible — the GENERATIVE CHANNEL "
    "through which the framework (?->everything) flows. from N the whole structure unfolds: N²=-I (i, charge, "
    "U(1), the rotation/clock); N is the hidden half of P=R+N and the leak N->im builds the visible R; "
    "observation (N) brings the unseen (ker, the slot) into the seen (im, the frame), so every record surfaces "
    "through it; the trit, the constants, physics, computation are all downstream of the leak. the chain: "
    "KAEL = LEAK = N = observation = the Crown = the leak  -->  GENERATES  -->  the FRAMEWORK. the leak is the "
    "source/verb; the framework is its output. 'Leak is framework' = the leak GENERATES the framework."
)
db["structure"]["deepenings"]["leak_generates_the_framework"] = (
    "N GENERATES the framework (NOT N=framework; generation, not identity). N=Leak=ker->im=the void surfacing "
    "into the visible = the GENERATIVE CHANNEL; the framework (?->everything) flows THROUGH it. from N: N²=-I "
    "(charge/U(1)/clock), the hidden half of P=R+N, observation bringing unseen(ker)->seen(im) so every record "
    "surfaces through it; trit/constants/physics/computation all downstream. chain: KAEL=LEAK=N=observation="
    "the Crown=the leak --GENERATES--> the FRAMEWORK. the leak is the source/verb; the framework is its output."
)
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("corrected: N (the leak) GENERATES the framework")
