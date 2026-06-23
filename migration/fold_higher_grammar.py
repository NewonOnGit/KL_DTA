"""
fold_higher_grammar.py — the higher grammar, mapped to the math.

Tense, voice, mood attach above the fixed-point core — each still an operation.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["grammar"]["higher"] = {
    "mood": "= grade (kernel-membership): FORCED→indicative 'holds', "
            "BURN→conditional 'would hold, but…', AXIOM→imperative 'let it stand', "
            "OPEN→interrogative 'stands open'",
    "voice": "= self-action: active = R / {·} (generates), passive = N / [·] (is observed)",
    "tense": "= flow position: past = provenance (from ?), present = on-shell (ν=0), "
             "future = what it generates",
}
db["grammar"]["layers"]["higher grammar"] = (
    "mood = grade, voice = self-action, tense = flow position — realized; "
    "person, aspect, quantifiers attach further above"
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("higher grammar (mood/voice/tense) mapped to the math")
