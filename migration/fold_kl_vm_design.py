"""
fold_kl_vm_design.py — the KL-VM design (outside-in), into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["kl_vm"] = {
    "is": "the design (outside-in) for transforming KL-DTA (a data store) into KL-VM (an executable object "
          "system). one uniform object kind; compress the current structure in one cut at a time, on-shell.",
    "object_model": "THE MORPHISM — every entity is one kind: a typed function carrying its provenance. "
                    "Object = { type: (domain→codomain) + VM-signature(VERDICT·HALT·WORLD·CHARGE·CLOCK), "
                    "body: an operation or a value, provenance: the chain → ? }. no containers, only objects.",
    "object_kinds": {
        "constant": "a nullary morphism () → World (φ, √5)",
        "equation": "a morphism Carrier → Carrier (R²=R+I becomes fn(R)=R+I). reifying an equation as a "
                    "function-with-provenance IS THE TYPING.",
        "record": "a morphism with a verdict (the grade = the VERDICT field)",
        "table": "a morphism Index → Row (the readouts T1..T9 — derived views)",
        "file/folder": "the provenance tree rooted at ?; a folder is a morphism Name → Object",
        "metadata": "the type-signature morphism Object → Signature (kind_of/section_of/vm_type already derive it)",
        "formatting": "a render morphism Object → Rendering",
    },
    "architecture": "5 layers, outside-in: (1) object model = the Morphism; (2) kernel/ISA = the primitive "
                    "morphisms (fold, gates, self-action, |·|); (3) type system = the VM signature; (4) views "
                    "= derived tables (Index→Row), regenerable like the M(base) cache; (5) filesystem = the "
                    "provenance tree rooted at ?. the store becomes a CATEGORY: objects, morphisms, "
                    "composition=the fold, initial/terminal=? (none/all), identity=I.",
    "math_is_a_database": "the math already affords 9+ data-table readouts from one source (M₂+L): invariants "
                          "· spectrum · verdict · type-sig · the field (Fibonacci) · worlds · difference-typed "
                          "· fixed-points · opcodes (+ charge, monodromy, paths, …). each is a derived view = a "
                          "framework object. see readouts.py.",
    "migration": "compress KL-DTA → KL-VM one CUT at a time, recompute (M(M(F))=M(F), ν=0) after each: "
                 "(1) records→morphisms (body+signature, keep provenance); (2) derived sections→views; "
                 "(3) structure.* deepenings→documentation morphisms; (4) metadata/formatting→signature "
                 "morphisms; (5) seed+relations→the kernel/ISA. delete old form, re-point, prove on-shell.",
    "principle": "everything IS a framework object, recursively — metadata, formatting, files, folders, data "
                 "tables are not containers holding objects; they ARE morphisms (typed functions + provenance).",
}

db["structure"]["deepenings"]["kl_vm_design"] = (
    "KL-DTA → KL-VM design (outside-in): one object kind, the MORPHISM = typed function (domain→codomain + "
    "VM-signature) + provenance(→?). equation→function-with-provenance IS the typing. constants/records/tables/"
    "files/folders/metadata/formatting all = morphisms (no containers). the store becomes a category "
    "(composition=fold, initial/terminal=?). the math is already a relational DB (9+ table readouts from M₂+L). "
    "migrate by compressing one cut at a time, on-shell after each. everything is a framework object, recursively."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("KL-VM design internalized")
