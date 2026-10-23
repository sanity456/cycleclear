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

## Completed three-person exchange

The corrected deployment completed one full three-person round on 2026-10-23. The three offers were a cordless drill, folding step ladder, and drill-bit set; each participant needed the next participant's item. The validator judged all six directed pairs: exactly three `FITS` edges formed the selected cycle, while all reverse/pairwise edges were `DOES_NOT_FIT`. The selected cycle included all three invited wallets. Each acceptance finalized successfully and the final `get_round` readback was `CLEARED` with all three acceptances true.

| Step | Explorer transaction | Status / execution / votes |
| --- | --- | --- |
| Open `review_cycle_20261023` | https://explorer-studio.genlayer.com/tx/0x24d511c7a0734fa886292207afbae51e653e385cca8240556d38b9634ed43f25 | FINALIZED / SUCCESS / `[5,5,1,1,1]` |
| Register owner intent | https://explorer-studio.genlayer.com/tx/0xafb4c7e59434b69405e5ae8b08563906d233177d574782090edf601cd620cd2d | FINALIZED / SUCCESS / `[5,1,5,1,1]` |
| Register participant 2 intent | https://explorer-studio.genlayer.com/tx/0xebbcba7f46c1cc7f4754b1658dc1b94a56ef03d8afc83ba947f3fa288c9f5ef6 | FINALIZED / SUCCESS / `[1,5,5,1,1]` |
| Register participant 3 intent | https://explorer-studio.genlayer.com/tx/0xfbd6b0b2f8c4e5c0317b59d90baf1a0904569a317b6538943a8ecab076293681 | FINALIZED / SUCCESS / `[1,5,1,5,1]` |
| Freeze round | https://explorer-studio.genlayer.com/tx/0x0234fe85d8fa15e54827a48507c2593749c2c6e683318a7268bbdf7c09dd9205 | FINALIZED / SUCCESS / `[1,1,5,1,5]` |
| Assess pairwise fits and select cycle | https://explorer-studio.genlayer.com/tx/0xa496089f9b00091ee273d5b33b5f9d758dcc8d12062c9970dc00a38c5036b76c | FINALIZED / SUCCESS / `[5,1,5,1,1]` |
| Owner accepts | https://explorer-studio.genlayer.com/tx/0x7732f2d0f798420b5e125f69ae7e7acd8de3e468c0897cbb6d08e802e391872d | FINALIZED / SUCCESS / `[1,5,1,5,1]` |
| Participant 2 accepts | https://explorer-studio.genlayer.com/tx/0x9aeaffb06324dde5e7abc68bc63caf340d18ac5f3d9c4f2fa7e30676c02986ef | FINALIZED / SUCCESS / `[1,1,1,1,1]` |
| Participant 3 accepts and clears round | https://explorer-studio.genlayer.com/tx/0x1165249d629e5e7d505f36b7af6d2d9809e3f00cfe191f530d348155d969da79 | FINALIZED / SUCCESS / `[1,1,1,1,1]` |

Final readback key: `0xd0bfe06a010bb6167838ad3ee07a5d30d27906fc|review_cycle_20261023`; status `CLEARED`; three acceptances true. No physical delivery or ownership was verified; the contract records a coordination result only.

Local verification: GenVM AST lint passed (3 checks); SDK validation passed; standard typecheck passed with zero diagnostics; direct tests passed (8 tests). Strict Pyright mode reports 20 diagnostics, primarily redundant runtime type guards and unknown types from dynamic/SDK APIs; it is stricter than the standard check and does not indicate an SDK validation failure. No contract source was changed for these optional strict-mode diagnostics. `git diff --check` passed. No reviewer outcome is guaranteed.

## Obsolete deployment — do not submit

- Address: `0x031a5d91fA8367bF8B64B35B0792B66580FE911A`
- Deployment transaction: `0xf9d1b44d2dc53bdcf8dfe62439d6225fb8f92fbd37bca2332e9f5041ac33cbe3`
- This is the earlier shared-capacity/open-registration version and does not match the corrected source.
