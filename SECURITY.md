# Security and trust limits

- Inputs are public declarations. The contract proves only which wallet submitted them, not ownership or truth.
- Model judgment is bounded to a closed enum and is independently recomputed. Missing, malformed, out-of-order, extra, or conflicting rows fail closed.
- Only the round creator freezes membership. Membership and descriptions cannot change afterward.
- Only members of the chosen cycle can accept or decline. Acceptance is one-time; one decline ends the cycle.
- No assets, escrow, reputation, or legal rights move or are represented by this contract.
- The cycle search is bounded to at most six members. It selects one longest cycle; it does not optimize multiple simultaneous cycles.
- A deployment accepts at most 20 permanent rounds to bound storage growth.
- This is an unaudited prototype. The manual review is not a formal security audit.
