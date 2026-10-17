# OFD-SignedInt4

**Exact code-space recoding and representation algebra for groupwise INT4 attention states.**

This repository studies representation changes that preserve the decoded quantized state exactly, with special focus on converting the existing offset-binary nibble contract into signed two's-complement form for representation-native downstream operators.

## Frozen starting point

Signed quantized integer:

```text
q in [-8, 7]
```

Existing stored nibble:

```text
c = q + 8
```

Exact signed-nibble recoding:

```text
signed_nibble = c XOR 0x8
```

For a packed byte containing two nibbles:

```text
signed_byte = offset_byte XOR 0x88
```

This is a code-space bijection, not requantization.

## Research question

Which exact code/coordinate transformations preserve the quantized state or commute with downstream operators, and which representation minimizes auxiliary reconstruction/correction work for DirectK, DirectV, and DirectAttention?

## Scope

- offset-binary ↔ two's-complement recoding;
- exhaustive nibble/byte verification;
- exact code bijections;
- coordinate/group permutations and compatible symmetries;
- signed/unsigned radix and bit-plane forms;
- operator compatibility with DirectK/DirectV;
- machine-lowering questions only after representation algebra is fixed.

## Non-goals

No requantization, numerical low-rank approximation, changed quantization error, or quality-changing code transformation belongs in the exact path.
