# Reproducibility

Finite representation claims should be reproducible exhaustively, not statistically.

Required artifacts:

- exhaustive 16-nibble table;
- exhaustive 256-byte table;
- codec/decoder source SHA;
- exact test command;
- target language/runtime version;
- integration upstream SHAs for DirectK/DirectV tests.

Hardware experiments additionally record GPU, driver, CUDA/toolchain, compiler, dtype/accumulation policy, raw outputs, and analysis path.

Negative results are retained when they constrain which exact representation is actually useful.