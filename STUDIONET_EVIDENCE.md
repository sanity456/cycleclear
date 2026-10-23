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
- Each selected wallet submitted `accept_cycle`. Finalized transaction receipts and the final `get_round` read-back showed all three acceptance flags `true` and status `CLEARED`.
- Captured successful finalized acceptance transactions:
  - Creator: `0xeed619109d6a17d5e37f0554da78b3c4ef320a0aa1afdd9e836f1c4653258677`
  - Participant 3: `0xf331121291dbdb94bf392395e122c1745871daff61aaf22f2ba05b2b7201bdcd`
  - Participant 2: `0x2dfe9529f750e051d086a0e433c756824ab529928bbc2b63cf6e3cbdc719cd99`

## Evidence limitations

The transaction hash for the successful `assess_round` call was not captured during a long CLI wait, although its state transition was verified through `get_round`. A later duplicate `assess_round` transaction (`0x871e72b3ac16df2b1d264caec1d89df841133508a3bf737b9e4537ded74f7199`) reached an already-advanced round and had a leader execution error; it made no state change and is not evidence of a successful assessment. The round creation, some registrations, and freeze hashes were likewise not captured, but their state changes were read back before continuing.

This file records local CLI evidence. Add direct StudioNet and Explorer URLs to the Portal submission after the public repository and commit are ready.
