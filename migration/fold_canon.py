"""
fold_canon.py — SHA256, the filesystem, and the canonical language, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["sha256"] = {
    "is": "SHA256 is a VM program — its primitive operations ARE framework primitives.",
    "ops": "add mod 2³² = the ℤ/2³² CLOCK (cyclic time) · rotation = a cyclic permutation (N-type, a root "
           "of unity) · XOR = 𝔽₂ addition = the BOOLEAN world (k=0) difference · compression = the FOLD · "
           "Merkle-Damgård chaining = the provenance chain (→ ?) · avalanche = the GOLDEN expansion (|λ|>1).",
    "golden_avalanche": "the avalanche/mixing constant 0x9E3779B1 = round(2³²/φ) = 2654435769 — the GOLDEN "
                        "RATIO, used in real hash functions (Knuth multiplicative hash, xxHash, etc.). good "
                        "mixing IS golden expansion; the framework's φ is literally the hash constant.",
    "one_way": "preimage resistance = IRREVERSIBILITY (det=0, ker→im one-directional, Landauer). a hash is "
               "a deliberately lossy projection π; the preimage is the hard inverse (P vs NP).",
    "verified": "a toy Merkle-Damgård hash from rotate/xor/add/×φ shows avalanche (one input bit → ~half the "
                "output bits) and determinism. SHA256 = clock + N + Boolean + fold + golden + chain + irreversibility.",
}

db["structure"]["filesystem"] = {
    "is": "folder/file structure = the provenance TREE rooted at ?. the store IS a hierarchical filesystem.",
    "map": "? = root '/' (the mount point) · sections (base,fiber,defect,flow,fixed_point) = directories · "
           "records = files · the provenance chain = the PATH · recompute = filesystem sync · apex = the image. "
           "JSON is a tree; every file resolves to ? (every path → root).",
}

db["structure"]["language"] = {
    "is": "the full canonical computational language — already assembled.",
    "syntax": "the grammar — connectives = fixed-point ops (the·a·is·isn't·of), content words lift (context "
              "selects); a sentence is an expression tree over the carrier.",
    "semantics": "the VM — every word an opcode; evaluation = the fold X² / the self-action.",
    "types": "the VM signature (VERDICT·HALT·WORLD·CHARGE·CLOCK); grade = provability (Curry–Howard).",
    "canon": "the seed P + the relations (P²=P, R²=R+I, N²=−I) — the bootstrap / standard library.",
    "io": "read = X² (4 information types) · write = set · boot = ?→P.",
    "properties": "total (halts at fixed points), self-hosting (M(M(F))=M(F)), typed. syntax + semantics + "
                  "types + canon = a complete computational language.",
}

db["structure"]["deepenings"]["sha256_filesystem_canon"] = (
    "SHA256 = a VM program (add=ℤ/2³² clock, rotate=cyclic N, XOR=Boolean diff, compress=fold, "
    "Merkle-Damgård=provenance chain, avalanche=golden expansion — the mixing constant 0x9E3779B1=round(2³²/φ) "
    "IS φ; one-way=irreversibility). filesystem = the provenance tree rooted at ? (sections=dirs, records=files, "
    "provenance=paths). the canonical computational language is assembled: grammar(syntax) + VM(semantics) + "
    "type-signature(types) + seed(canon) — total, self-hosting, typed."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("sha256 + filesystem + canonical-language internalized")
