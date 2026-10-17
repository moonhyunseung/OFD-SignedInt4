# Exact automorphism framework

This file classifies representation changes by whether they preserve the frozen quantized state and downstream operator semantics.

## Classes

### A. Pure code recoding

Bijections on stored codewords with a corresponding decoder change, e.g. offset-binary to two's-complement. These preserve the represented integer exactly.

### B. Coordinate permutation

A coordinate permutation is exact only if the same permutation is applied consistently to every downstream operand/operator that consumes that coordinate axis.

### C. Group permutation

A group permutation must move the corresponding group scale and coordinate block together. Permuting codes without scales changes the represented tensor.

### D. Signed coordinate actions

Sign changes may be exact only when code, scale/sign convention, and downstream dual action are transformed compatibly. These are not assumed valid by default.

### E. Non-automorphisms

The following are outside the frozen exact representation unless separately redefined as a new quantizer:

- regrouping coordinates;
- recomputing scales;
- changed clipping bounds;
- changed rounding;
- truncated/approximate transforms;
- any code map that is not bijective on the represented integer state.

## Required proof template

Every proposed automorphism must provide:

1. source representation state;
2. target representation state;
3. bijection/inverse;
4. decoder commutation identity;
5. downstream operator compatibility;
6. symbolic cost consequence;
7. remaining hardware question.
