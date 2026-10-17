# Status

## Current phase

**T0 — Representation algebra**

No performance claim exists yet.

| Stage | Requirement | Status |
|---|---|---|
| T0 Representation | Exact offset/signed code mapping specified | PASS |
| T1 Finite verification | Exhaustive nibble/byte equivalence tests | NOT STARTED |
| T2 Operator compatibility | DirectK/DirectV equations rewritten in signed form | NOT STARTED |
| T3 Symmetry classification | Exact code/coordinate automorphisms classified | NOT STARTED |
| T4 Lowering | Native signed consumption/recode path inspected | NOT STARTED |
| T5 Boundary | Inline/materialized/native crossover measured | NOT STARTED |
| T6 Integration | Locked upstream DirectK/DirectV integrations | NOT STARTED |
| T7 Freeze | Claims/results/manifests frozen | NOT STARTED |

## Immediate questions

1. Exhaustively verify all 16 nibble states and 256 packed-byte states.
2. Prove that offset-to-signed recoding is a representation bijection under the frozen decoder.
3. Determine which downstream correction terms disappear under signed consumption.
4. Separate exact automorphisms from transforms that change quantization semantics.
