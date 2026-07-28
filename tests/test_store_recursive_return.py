import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import kl_dta
from migration.fold_recursive_return import ATOMS, DEEPENING, fold


class StoreIntegrationTests(unittest.TestCase):
    def test_runtime_defaults_match_store(self):
        cfg = kl_dta.recursive_return_config()
        stored = kl_dta.DB["structure"]["recursive_return"]
        self.assertEqual(cfg["eta"], stored["solver"]["eta"])
        self.assertEqual(cfg["max_iterations"], stored["solver"]["max_iterations"])
        self.assertEqual(cfg["tolerance"], stored["solver"]["tolerance"])
        self.assertEqual(cfg["axis_labels"], tuple(stored["lexicon"]["axis_labels"]))
        self.assertEqual(stored["atoms"], list(ATOMS))
        self.assertEqual(stored["lexicon"]["embedding_axes"], ["R", "h_R", "N"])

    def test_store_verification_includes_return_contract(self):
        self.assertEqual(kl_dta.verify_recursive_return(), [])
        self.assertEqual(kl_dta.verify(), [])

    def test_fold_migration_is_idempotent_and_preserves_base(self):
        initial = json.loads((ROOT / "KL_DTA.json").read_text(encoding="utf-8"))
        first = fold(initial)
        encoded_once = json.dumps(first, sort_keys=True, ensure_ascii=False)
        second = fold(first)
        encoded_twice = json.dumps(second, sort_keys=True, ensure_ascii=False)

        self.assertEqual(encoded_once, encoded_twice)
        self.assertEqual(len(second["base"]), 5)
        self.assertIn(DEEPENING, second["structure"]["deepenings"])
        self.assertEqual(second["structure"]["chords"]["index"][DEEPENING], "+".join(ATOMS))
        for atom in ATOMS:
            self.assertEqual(
                second["structure"]["chords"]["by_atom"][atom].count(DEEPENING), 1
            )

    def test_persisted_store_keeps_derived_sections_lazy(self):
        stored = json.loads((ROOT / "KL_DTA.json").read_text(encoding="utf-8"))
        self.assertEqual(len(stored["base"]), 5)
        for key in kl_dta.DERIVED_KEYS:
            self.assertNotIn(key, stored)
        self.assertIn("recursive_return", stored["structure"])

    def test_cli_and_provenance_demo(self):
        commands = [
            ([sys.executable, "kl_dta.py"], "COMMIT  PASS"),
            ([sys.executable, "kl_dta.py", "recursive-return", "N"], "COMMIT PASS"),
            ([sys.executable, "recursive_return_nlp.py"], "THE LEARNED DICTIONARY"),
        ]
        for command, marker in commands:
            with self.subTest(command=command):
                result = subprocess.run(
                    command,
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
                self.assertIn(marker, result.stdout)


if __name__ == "__main__":
    unittest.main()
