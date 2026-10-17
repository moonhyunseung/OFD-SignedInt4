# Claims

| ID | Claim | Type | Status | Evidence required |
|---|---|---|---|---|
| S-C0 | Offset-binary nibble `c=q+8` and signed two's-complement nibble are related by XOR with the sign bit. | Discrete algebra | PROVED AT FORMULA LEVEL | Exhaustive nibble check |
| S-C1 | Packed-byte recoding is exactly `byte XOR 0x88` for two independent nibbles. | Discrete algebra | PROVED AT FORMULA LEVEL | Exhaustive 256-byte check |
| S-C2 | Recoding changes representation only; it does not change the represented quantized integer. | Representation | OPEN | Decoder equality proof + exhaustive verification |
| S-C3 | Signed consumption removes explicit `-8` offset correction from DirectK/DirectV formulas. | Operator algebra | OPEN | Downstream composition proof |
| S-C4 | A larger family of exact code/coordinate automorphisms can be classified under the frozen groupwise representation contract. | Representation theory | OPEN | Formal classification |
| S-C5 | At least one signed representation path reduces auxiliary execution work versus offset-binary correction on target hardware. | Hardware/empirical | OPEN | Lowering + boundary experiment |
| S-C6 | Signed representation composes cleanly with frozen DirectK/DirectV semantics. | Integration | OPEN | Locked upstream SHA tests |

## Guardrails

- `exact representation change` means decoded quantized values are unchanged.
- A transform that changes scale selection, rounding, clipping, or group boundaries is not an automorphism of the frozen representation.
- Hardware benefit is independent from algebraic validity and must be measured separately.
