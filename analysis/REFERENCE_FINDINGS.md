# Reference evidence — OFD-SignedInt4

- Source commit: `39bb5a64f1c1fdb7a44b789186d3499501254f5f`.
- Recorded run: `results/20261017T045047Z_83706194`.
- Formal tests: 8 passed; see run.log. The source was committed and clean before execution.
- No GPU or performance measurement was performed. No original OFD E00–E14 result was modified.

## Direct observations

All16 nibbles and all256 bytes preserve both decoded integers under XOR recoding, in both inverse directions. The -8 endpoint is included; arbitrary negation is not closed on signed INT4. Rational scale fixtures preserve equality.

## Interpretation and limits

The case proof in theory/EXACT_RECODING.md establishes the representation bijection. Exhaustive tests verify this finite codec implementation. Downstream GPU instruction support and recoding cost remain unmeasured. Coordinate/group permutations require compatible operand/scale permutations; a complete symmetry classification is not claimed.

## Next justified work

Inspect native signed consumption and inline versus materialized recoding on the target GPU. Keep quantizer/layout fixed; inspect generated code before any crossover or model claim.
