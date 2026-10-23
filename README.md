# Batch D1 — CycleClear

CycleClear is a reusable GenLayer contract for discovering and clearing multi-party barter cycles. A creator opens a round with a fixed allowlist of 3–6 wallet addresses; only those wallets may register one offer and one need. After the round is frozen, validators independently classify every directed offer-to-need pair. Deterministic code finds the longest eligible cycle of three or more participants; the cycle clears only after every selected participant accepts.

## Mechanism and distinction

The core mechanism is directed cycle clearing: A may give to B, B to C, and C to A even when no pair can exchange directly. This differs from `flowdispatch` and `donationdoor`, which allocate compatible sources to needs, and from `found-match`, which handles a bilateral handoff. CycleClear requires a closed ring with one incoming and one outgoing exchange per member, followed by unanimous acceptance of that exact ring.

## Boundary

GenLayer classifies semantic fit from the participants' declared descriptions. Code constructs the graph, selects the longest deterministic cycle, and enforces unanimous acceptance. Each creator has an independent lifetime allowance of 20 rounds; round keys include the creator address, so another creator may reuse the same local round name without reading or changing the first creator's record. The fixed invite list prevents uninvited callers from taking participant slots. The contract does not verify ownership, item condition, identity, delivery, value, or legal suitability and does not hold or transfer assets. The result is a public coordination signal only.

## Verify and release

    genvm-lint check contracts/cycle_clear.py
    genvm-lint typecheck contracts/cycle_clear.py --strict
    python -m pytest tests/direct -q -p no:cacheprovider

The earlier deployment used the vulnerable shared registry and must not be submitted. The corrected source is under local verification; deployment, source-byte comparison, and refreshed live abuse evidence are still required. See `STUDIONET_EVIDENCE.md`, `release_manifest.json`, and `SUBMISSION_CHECKLIST.md` for the release gate status.
