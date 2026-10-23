# Batch D1 — CycleClear

CycleClear is a reusable GenLayer contract for discovering and clearing multi-party barter cycles. Participants register one surplus offer and one need in a round. After the round is frozen, validators independently classify every directed offer-to-need pair. Deterministic code finds the longest eligible cycle of three or more participants; the cycle clears only after every selected participant accepts.

## Mechanism and distinction

The core mechanism is directed cycle clearing: A may give to B, B to C, and C to A even when no pair can exchange directly. This differs from `flowdispatch` and `donationdoor`, which allocate compatible sources to needs, and from `found-match`, which handles a bilateral handoff. CycleClear requires a closed ring with one incoming and one outgoing exchange per member, followed by unanimous acceptance of that exact ring.

## Boundary

GenLayer classifies semantic fit from the participants' declared descriptions. Code constructs the graph, selects the longest deterministic cycle, and enforces unanimous acceptance. The contract does not verify ownership, item condition, identity, delivery, value, or legal suitability and does not hold or transfer assets. The result is a public coordination signal only.

## Verify and release

    genvm-lint check contracts/cycle_clear.py
    genvm-lint typecheck contracts/cycle_clear.py --strict
    python -m pytest tests/direct -q -p no:cacheprovider

A StudioNet deployment and three-party smoke test are recorded in `STUDIONET_EVIDENCE.md`; `release_manifest.json` records the deployed source hash and public source repository. See `SUBMISSION_CHECKLIST.md` for the remaining Portal evidence gates.
