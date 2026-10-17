# Reference implementations

This directory is for transparent codec and recoding references.

Planned files:

- `offset_codec.py` — frozen `q <-> q+8` nibble contract;
- `signed_codec.py` — two's-complement nibble interpretation;
- `recode.py` — exact nibble/byte recoding;
- `decode_equivalence.py` — reference decoder equality checks;
- `directk_adapter.py` / `directv_adapter.py` — later, locked upstream compatibility references.

Reference code favors clarity and exhaustive verifiability over performance.