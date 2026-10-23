# StudioNet evidence

## Corrected release status

The contract source now includes per-creator round namespaces and lifetime allowances, plus an immutable invite list. It has passed local GenVM lint/SDK validation and 8 direct tests. The corrected source has **not yet been deployed or tested on StudioNet**. Do not submit the deployment below as evidence for the corrected source.

## Obsolete deployment (do not submit)

- Address: `0x031a5d91fA8367bF8B64B35B0792B66580FE911A`
- Deployment transaction: `0xf9d1b44d2dc53bdcf8dfe62439d6225fb8f92fbd37bca2332e9f5041ac33cbe3`
- It runs the earlier contract with a shared deployment-wide round limit and open registration. It does not match current `contracts/cycle_clear.py`.
- Earlier success transactions, including the prior three-party clear, prove only that old code path. They do not prove the creator isolation or invite-list guards.

## Required evidence before submission

Deploy the pushed corrected source. Record the new deployment receipt and execution result, public source commit and raw source hash, and compare the deployed source bytes against the Git blob. On StudioNet, show that creator A can use its own allowance, creator B can open the same local round name in an isolated record, an uninvited wallet is rejected without changing state, and invited members can complete a cycle. Record every transaction's final status and execution result, expected failures, and state read-backs. Replace this file and the release manifest only with verified output.
