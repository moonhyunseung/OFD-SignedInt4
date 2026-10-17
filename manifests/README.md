# Manifests

Representation verification manifests should record:

- repository commit SHA;
- codec/test source path;
- runtime/toolchain version;
- exact exhaustive test command;
- generated nibble/byte table paths.

Integration/hardware manifests additionally record:

- DirectK/DirectV upstream SHAs;
- hardware/software stack;
- representation path (offset, materialized recode, inline recode, native signed);
- dtype/accumulation policy;
- raw result and analysis paths.
