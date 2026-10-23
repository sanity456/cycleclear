# StudioNet release evidence

Corrected deployment verified on 2026-10-23 against the public source release commit `3a81bcfd6d341897bbb08a03ba3dd3400d5dc5ec`.

- Contract: `0x57AECF347f700dFEc106A19CCcD62D793DEf189C`
- Deployment transaction: `0x9faa596495415efedc2a40512bf7aec3a4c947d1e0c7a3defda2728b8467f894`
- Explorer: https://explorer-studio.genlayer.com/address/0x57AECF347f700dFEc106A19CCcD62D793DEf189C
- Deploy transaction: https://explorer-studio.genlayer.com/tx/0x9faa596495415efedc2a40512bf7aec3a4c947d1e0c7a3defda2728b8467f894
- Finality/result: `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS`; validator votes agreed.
- Deployed source was byte-for-byte equal to the local corrected source; SHA-256 `2af57c37d9c50639225cb2cd474905e0c12c079639f6b62e4002f3073e3cd56d` (12,291 bytes).
- Test wallets were newly generated and isolated for this Batch D run; they were not reused from another batch/user or workspace wallet.

## Focused live checks

All listed transactions finalized. Expected rejection tests produced execution `ERROR`; they were not treated as success-path passes.

| Check | Transaction | Result |
| --- | --- | --- |
| Creator A opens `capacity_00` | `0xec530073528450696c73031e7fe5a8cb02ff50dee2300537bb3f513b7ebfaa51` | SUCCESS |
| Creator A opens `capacity_01` | `0x2f6ae3dd6c4903fb6d47f4c104509350e1a808cb921a187f4ce0c5f6960fa714` | SUCCESS |
| Creator B independently reuses `capacity_00` | `0x0e9ee67ce205f5aad48c5516e1884555f7decfa9eb6af32b0db26f3afe4c171b` | SUCCESS; readback confirmed separate creator-qualified records |
| Open fixed-roster test round | `0xa4c9124e10bdafb3d6db17a91be177450de13b5c9053bd232bd315eabb4af4bc` | SUCCESS |
| Uninvited registration | `0x915f70da11fd23ba5a4fb55e1af20e5b45fc2a8ae3d526bbef4bba2e49350e32` | Expected ERROR; readback confirmed participant list remained empty |

Local verification: GenVM AST lint passed (3 checks); SDK validation passed; standard typecheck passed with zero diagnostics; direct tests passed (8 tests). Strict Pyright mode reports 20 diagnostics, primarily redundant runtime type guards and unknown types from dynamic/SDK APIs; it is stricter than the standard check and does not indicate an SDK validation failure. No contract source was changed for these optional strict-mode diagnostics. `git diff --check` passed. No reviewer outcome is guaranteed.

## Obsolete deployment — do not submit

- Address: `0x031a5d91fA8367bF8B64B35B0792B66580FE911A`
- Deployment transaction: `0xf9d1b44d2dc53bdcf8dfe62439d6225fb8f92fbd37bca2332e9f5041ac33cbe3`
- This is the earlier shared-capacity/open-registration version and does not match the corrected source.
