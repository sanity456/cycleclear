# StudioNet evidence

Test date: 2026-10-23. Network: GenLayer StudioNet (`chainId 61999`, `https://studio.genlayer.com/api`). The deployment and test accounts were created in an isolated CLI profile under the system temporary directory; no pre-existing workspace account was used. Private keys and keystore passwords are intentionally not recorded here.

## Deployment

- Contract: `CycleClear`
- Contract address: `0x031a5d91fA8367bF8B64B35B0792B66580FE911A`
- Deployment transaction: `0xf9d1b44d2dc53bdcf8dfe62439d6225fb8f92fbd37bca2332e9f5041ac33cbe3`
- Deployment receipt: `FINALIZED`; leader execution `SUCCESS`; validator consensus `MAJORITY_AGREE`.
- Local source: `contracts/cycle_clear.py`
- Local SHA-256: `8BBC3AFAB6451B1C1CEEBA340F6DF28D6A2C9EE380472E68A038F4141DD91FEA`
- `genlayer code <address>` read-back matched the local source after normalizing line endings and trailing newline. The on-chain schema exposed the expected 8 methods, including two read-only views.

## Live flow and read-back

- Test round: `batchd_cycle_20261023`.
- Three isolated participants registered complementary intents. Their addresses were `0x94ce68c866439c9cf88bd3cbcdaa4c1aeb533873`, `0xbc8e12997be8f1269a10b9636a6c84708efd9347`, and `0xabef995deacc591f3c0b742d21159abd27477b4a`.
- Frozen-round read-back showed all three participants. The semantic assessment produced the expected three-member directed cycle; read-back showed one `FITS` edge per leg, the selected cycle, and status `AWAITING_ACCEPTANCE`.
- Explorer transaction history confirms the successful `assess_round` transaction: `0xcb6edf0f477b844839ce97ff6f673355c4e34886aaa60c4586b4794280266791` (`FINALIZED`, GenVM `SUCCESS`). The other round-flow transactions visible in Explorer are `open_round` `0xf4f12a7b6a82686527736140720e76214d1b86801aee4ef2200d57969300367a`, registrations `0x96fa5fc93362217bee8136124d1973c3cc4cc541f887dc0142e36e8fc52e0954`, `0x648179e8cb5e70fcbc5ccab74fd877bedcd46bc9f143bbe819b928d615c57555`, and `0x41a29aee3f149db4f5e1a349ffe2f539471f7757a5753573e1fe7d8917c4cd0a`, and `freeze_round` `0x6b014ccde128b49f8614745a02ec2c9881d2c5dc7a420b67c089e29e7a655ffa`.
- Each selected wallet submitted `accept_cycle`. Finalized transaction receipts and the final `get_round` read-back showed all three acceptance flags `true` and status `CLEARED`.
- Captured successful finalized acceptance transactions:
  - Creator: `0xeed619109d6a17d5e37f0554da78b3c4ef320a0aa1afdd9e836f1c4653258677`
  - Participant 3: `0xf331121291dbdb94bf392395e122c1745871daff61aaf22f2ba05b2b7201bdcd`
  - Participant 2: `0x2dfe9529f750e051d086a0e433c756824ab529928bbc2b63cf6e3cbdc719cd99`

## Evidence links and limitations

The earlier CLI wait omitted several hashes, but the public Explorer history now supplies them. A later duplicate `assess_round` transaction (`0x871e72b3ac16df2b1d264caec1d89df841133508a3bf737b9e4537ded74f7199`) reached an already-advanced round and had a leader execution error; it made no state change and is not evidence of a successful assessment.

Public source: https://github.com/sanity456/cycleclear (source-release commit `0f9ce311f036a6e06b07362bcb8933569019871a`). Explorer contract page: https://explorer-studio.genlayer.com/address/0x031a5d91fA8367bF8B64B35B0792B66580FE911A. Successful assessment transaction: https://explorer-studio.genlayer.com/tx/0xcb6edf0f477b844839ce97ff6f673355c4e34886aaa60c4586b4794280266791. Add the public repository, Studio contract, and Explorer contract evidence in the Portal and verify them while logged out.
