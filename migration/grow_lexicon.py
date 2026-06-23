"""
grow_lexicon.py — the grammar is living: introduce new words to fill gaps.

Each new word still has inherent meaning — an operation — attaching above the
fixed-point core (the, a, is, isn't, of). The lexicon grows over time.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# core (already present) + the new connectives introduced for smoother speech
db["grammar"]["words"].update({
    "by":   "FLOW   — agency / generation (the generators act)",
    "from": "RETURN — provenance source (the chain back to ?)",
    "at":   "BASE   — position / index (depth, location)",
    "and":  "SUM    — conjunction / the enrichment join {·}",
    "not":  "DEFECT — negation of a term (within a clause)",
    "as":   "θ      — the duality reading (X read as Y)",
    "in":   "KER    — membership (∈ the kernel)",
})
db["grammar"]["living"] = (
    "the lexicon grows: new words are introduced to fill gaps, each one an "
    "operation. core five are fixed points; higher words attach above them."
)
db["grammar"]["layers"] = {
    "fixed-point core": "the · a · is · isn't · of  (the five fold-operations)",
    "connective layer": "by · from · at · and · not · as · in  (introduced as needed)",
    "higher grammar": "tense, voice, mood, quantifiers — attach above (future)",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("lexicon grown to", len(db["grammar"]["words"]), "words")
