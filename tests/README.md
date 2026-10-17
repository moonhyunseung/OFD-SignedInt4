# Tests

The first verification layer is exhaustive because the local code space is finite.

Required suites:

1. all 16 nibble states;
2. all 256 packed-byte states;
3. decoder equality before/after recoding;
4. random tensor packing/unpacking consistency;
5. locked DirectK/DirectV composition tests once upstream SHAs are frozen.

Statistical random tests supplement but never replace finite exhaustive verification.