# Unified Physics Canon Integration

This branch promotes `KAEL_CANON_UNIFIED_PHYSICS_6726E7D6_20260730.py` as the repository integration target.

## Source artifact

- SHA-256: `6726e7d621dbe153b4ab4761314bc96a75de1ea324b402db8165239d990c8b97`
- Size: 378,146 bytes
- Lines: 7,969
- Theorems: 159 total, comprising 144 preserved source records and 15 proved closure records
- Standalone constraints: zero imports, zero duplicate top-level functions/classes, self-auditing

## Required repository migration

1. Install the source artifact as the active standalone canon.
2. Retarget the regression suite from the v3.15 kernel to the active canon.
3. Preserve the v3.15 public surface where it remains part of the current contract.
4. Add regression coverage for WD-31, FB-09, and UN-01 through UN-13.
5. Update repository documentation and CI entry points to name the active canon.
6. Keep historical kernels as references only, never as competing active canon files.

## Acceptance gates

- All 144 source theorem records remain exact and ordered.
- All 230 declared dependency edges remain represented; the 204-edge transitive reduction has identical reachability.
- All prior certificate outputs remain exact.
- The mathematical audit is valid with 31 of 31 direct checks.
- The unified-physics closure certificates pass.
- The active artifact hash matches the source hash above.
