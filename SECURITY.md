# Security and trust limits

- Inputs are public declarations. The contract proves only which wallet submitted them, not ownership or truth.
- Model judgment is bounded to a closed enum and is independently recomputed. Missing, malformed, out-of-order, extra, or conflicting rows fail closed.
- Only the round creator freezes membership. Membership and descriptions cannot change afterward.
- Only members of the chosen cycle can accept or decline. Acceptance is one-time; one decline ends the cycle.
- Enrollment is limited to the creator's frozen invite list; unrelated callers cannot occupy participant capacity.
- Round names are scoped under creator addresses. The lifetime cap of 20 rounds is charged to that creator alone.
- No assets, escrow, reputation, or legal rights move or are represented by this contract.
- The cycle search is bounded to at most six members. It selects one longest cycle; it does not optimize multiple simultaneous cycles.
- Each creator can open at most 20 permanent rounds in this deployment to bound per-creator storage growth; closing a round does not recycle its slot.
- This is an unaudited prototype. The manual review is not a formal security audit.
