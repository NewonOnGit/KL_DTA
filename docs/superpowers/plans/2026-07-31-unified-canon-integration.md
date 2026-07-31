# Unified Canon Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the 159-theorem unified-physics canon the authoritative exact-mathematics layer of KL_DTA while preserving the existing store, recursive-return API, historical investigations, and regression fixtures.

**Architecture:** Add the standalone zero-import canon unchanged as `kael_canon.py`. Convert `canon.py` into a compatibility/query surface, teach `kl_dta.py` to load and verify the canon lazily, persist a compact `structure.unified_canon` manifest in `KL_DTA.json`, and bind the layers with migration and regression tests.

**Tech Stack:** Python 3, standard library, existing NumPy runtime, unittest, JSON.

## Global Constraints

- Preserve all 144 source theorem records and the 15 added closure records exactly.
- Preserve all existing recursive-return behavior and the four-context to two-value fixture.
- Keep `kael_canon.py` standalone with zero imports.
- Do not rewrite or delete historical investigation scripts.
- Use a new branch and pull request; do not mutate `master` directly.
- Verify store, canon, JSON, CLI, and full tests before merge.

---

### Task 1: Add authoritative canon

- [ ] Add `kael_canon.py` byte-for-byte from the immutable unified artifact.
- [ ] Verify SHA-256 `6726e7d621dbe153b4ab4761314bc96a75de1ea324b402db8165239d990c8b97`.
- [ ] Run its standalone audit and require `VALID` with 31 direct checks.

### Task 2: Add store manifest and migration

- [ ] Add an idempotent `migration/fold_unified_canon.py`.
- [ ] Persist `structure.unified_canon` with artifact identity, theorem counts, graph counts, physical terminals, closure laws, frontier, and implementation paths.
- [ ] Verify the persisted object equals the migration result and leaves the five-record base unchanged.

### Task 3: Integrate runtime API

- [ ] Add lazy `load_unified_canon`, `unified_canon_summary`, `verify_unified_canon`, and CLI commands to `kl_dta.py`.
- [ ] Keep the default store verification fast while checking the manifest and exact canon identity.
- [ ] Add an explicit full-audit command for the 159-theorem canon.

### Task 4: Replace legacy canon surface

- [ ] Convert `canon.py` into a compatibility CLI over `kael_canon.py` and `kl_dta.py`.
- [ ] Support summary, theorem lookup, physics standing, frontier, and full audit.

### Task 5: Regression and documentation

- [ ] Add tests covering theorem identity, dependency graph, physical closure, manifest equality, runtime API, CLI, and unchanged recursive-return behavior.
- [ ] Add a GitHub Actions workflow for the full unittest suite and standalone canon audit.
- [ ] Update README with the new authority chain and commands.

### Task 6: Verification and pull request

- [ ] Run the full unittest suite.
- [ ] Run `python kl_dta.py`, recursive-return CLI, canon summary, canon audit, JSON validation, compileall, and diff checks.
- [ ] Compare branch against `master`, inspect every changed file, and open a pull request with exact evidence.
