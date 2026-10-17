# Claims

| ID | Claim | Type | Status | Evidence required |
|---|---|---|---|---|
| S-C0 | Offset-binary nibble `c=q+8` and signed two's-complement nibble are related by XOR with the sign bit. | Discrete algebra | PROVED + EXHAUSTIVELY VERIFIED | Exhaustive nibble check |
| S-C1 | Packed-byte recoding is exactly `byte XOR 0x88` for two independent nibbles. | Discrete algebra | PROVED + EXHAUSTIVELY VERIFIED | Exhaustive 256-byte check |
| S-C2 | Recoding changes representation only; it does not change the represented quantized integer. | Representation | PROVED + EXHAUSTIVELY VERIFIED | Decoder equality proof + exhaustive verification |
| S-C3 | Signed consumption removes explicit `-8` offset correction from DirectK/DirectV formulas. | Operator algebra | PROVED OVER REALS | Downstream composition proof |
| S-C4 | A larger family of exact code/coordinate automorphisms can be classified under the frozen groupwise representation contract. | Representation theory | OPEN | Formal classification |
| S-C5 | At least one signed representation path reduces auxiliary execution work versus offset-binary correction on target hardware. | Hardware/empirical | OPEN | Lowering + boundary experiment |
| S-C6 | Signed representation composes cleanly with frozen DirectK/DirectV semantics. | Integration | SUPPORTED IN LOCKED CPU REFERENCES | Locked upstream SHA tests |

## Guardrails

- `exact representation change` means decoded quantized values are unchanged.
- A transform that changes scale selection, rounding, clipping, or group boundaries is not an automorphism of the frozen representation.
- Hardware benefit is independent from algebraic validity and must be measured separately.

## Locked downstream reference evidence

- DirectK source `53efd65761a756d3e0ff059272eb57779e406d84`: tests/test_codec_interop.py and tests/test_signed_bytes.py.
- DirectV source `a02307c0bcc0bf5f8942b72ab8a9b0ecf4e4fe49`: tests/test_codec_interop.py and tests/test_reference.py.

Both pin this codec at `39bb5a64f1c1fdb7a44b789186d3499501254f5f`; this supports CPU representation/operator interoperability, not native GPU consumption.
