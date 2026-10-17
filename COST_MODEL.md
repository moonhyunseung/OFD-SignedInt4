# SignedInt4 symbolic cost model

This file compares auxiliary representation work only. It does not claim latency.

## Offset-binary path

For a downstream operator consuming integer code `c=q+8`, the algebra may require an explicit offset correction proportional to `8` unless that correction is absorbed elsewhere.

## Signed recoding path

Exact recoding maps each nibble by

```text
s = c XOR 0x8
```

or each packed byte by

```text
B_signed = B_offset XOR 0x88.
```

A signed consumer can then operate on `q` directly and may remove the explicit zero-point correction from DirectK/DirectV formulas.

## Candidate realization costs

Logical alternatives:

1. keep offset-binary codes and compute reduced correction;
2. materialize a signed-recoded packed buffer;
3. recode inline during load/unpack;
4. consume the stored bits directly with a native signed interpretation if the machine path permits.

The algebra alone does not rank these by runtime.

## What must be counted later

- extra XOR/recode instructions;
- additional memory traffic if recoding is materialized;
- unpack/conversion instructions;
- instruction support for signed low-bit operands;
- register pressure and scheduling;
- reuse across K/V or repeated consumers.

A signed representation is a core candidate only if exactness is already closed; hardware experiments locate the boundary where its reduced correction work outweighs recoding cost.