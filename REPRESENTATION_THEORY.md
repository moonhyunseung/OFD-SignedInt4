# Representation theory

## Frozen state

For each quantization group, the stored state consists of integer codes plus a group scale. The representation change studied here is exact only when it preserves the decoded quantized value under the frozen scale/group contract.

Signed integer:

```text
q in [-8, 7]
```

Offset-binary nibble:

```text
c = q + 8
```

Two's-complement nibble is obtained by flipping the high bit:

```text
s = c XOR 0x8
```

For a byte containing low/high nibbles independently:

```text
B_signed = B_offset XOR 0x88
```

## Exactness criterion

For representation maps `phi` and decoders `D_offset`, `D_signed`, exact recoding requires

```text
D_signed(phi(code), scale) = D_offset(code, scale)
```

for every admissible code and scale.

This is stronger than numerical closeness and can be exhaustively verified over the finite code space.

## Scope of representation symmetries

Candidate exact symmetries may include code recodings and coordinate/group permutations only when the associated decoder/downstream map is transformed compatibly. Any action that changes scale selection, rounding, clipping, or group partition changes the quantized state and is outside the exact automorphism set.

## Downstream relevance

A representation is useful only relative to an operator. Signed recoding is interesting because DirectK/DirectV can consume signed `q` without an explicit `-8` offset correction. This is an operator-level simplification, not a change in quantization quality.