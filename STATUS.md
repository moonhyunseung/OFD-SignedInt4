# Status

## Current phase

**T2 — Exact codec / operator algebra verified; hardware lowering open**

No performance claim exists yet.

| Stage | Requirement | Status |
|---|---|---|
| T0 Representation | Exact offset/signed code mapping specified | PASS |
| T1 Finite verification | Exhaustive nibble/byte equivalence tests | PASS |
| T2 Operator compatibility | DirectK/DirectV equations rewritten in signed form | PASS (real algebra) |
| T3 Symmetry classification | Exact code/coordinate automorphisms classified | PARTIAL (permutation conditions / negation obstruction only) |
| T4 Lowering | Native signed consumption/recode path inspected | NOT STARTED |
| T5 Boundary | Inline/materialized/native crossover measured | NOT STARTED |
| T6 Integration | Locked upstream DirectK/DirectV integrations | VERIFIED CPU REFERENCES (hardware open) |
| T7 Freeze | Claims/results/manifests frozen | NOT STARTED |

## Original bootstrap questions (see checkpoint below for resolved items)

1. Exhaustively verify all 16 nibble states and 256 packed-byte states.
2. Prove that offset-to-signed recoding is a representation bijection under the frozen decoder.
3. Determine which downstream correction terms disappear under signed consumption.
4. Separate exact automorphisms from transforms that change quantization semantics.

## Verified CPU reference checkpoint — 2026-10-17

Source `39bb5a64f1c1fdb7a44b789186d3499501254f5f`; [8-test formal run and raw evidence](results/20261017T045047Z_83706194/FINDINGS.md). Exact dependencies are pinned where used. These are CPU reference results only.
