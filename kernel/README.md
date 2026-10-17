# Kernel gate

Kernel work is allowed only after exact recoding and decoder equivalence are closed.

Candidate implementations may include:

- materialized bytewise XOR recode;
- inline XOR during load/unpack;
- direct signed packed consumption;
- offset-binary correction baseline.

Every implementation must preserve the frozen quantized integer exactly. Any change to scale selection, clipping, rounding, or group boundaries is outside this repository's exact path.