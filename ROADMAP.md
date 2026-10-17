# Roadmap

## Phase 1 — Finite exact verification

- Enumerate all 16 signed INT4 values.
- Verify `c=q+8` and `signed=c XOR 0x8` bijectively.
- Exhaust all 256 packed-byte states and verify `byte XOR 0x88` recodes both nibbles independently.
- Verify decoder equality before any performance work.

## Phase 2 — Representation algebra

- Define the frozen code/scale/group representation as a discrete structured state space.
- Classify exact recodings, coordinate permutations, group permutations, and sign-compatible actions.
- Explicitly reject transforms that alter clipping, scale selection, rounding, or group partition.

## Phase 3 — Operator compatibility

- Rewrite DirectK and DirectV in signed form.
- Identify correction terms removed or moved by the representation change.
- Record upstream commit SHAs used for each proof/test.

## Phase 4 — Hardware lowering

Compare only exact realizations:

- materialized XOR recode;
- inline XOR recode;
- native signed packed consumption if available;
- offset-binary correction baseline.

## Phase 5 — Boundary and integration

Measure where each exact representation path wins or loses, then integrate only against frozen DirectK/DirectV SHAs.

## Phase 6 — Freeze

Freeze representation contract, proofs, exhaustive results, target hardware/toolchain, manifests, and final claim statuses.
