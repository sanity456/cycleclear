# Review and release check

Scope: `contracts/cycle_clear.py` and its tests. This is an engineering review, not a formal security audit or a guarantee of Portal acceptance.

## Findings and controls

- **Fixed before corrected deployment:** the initial shared deployment allowed anyone to consume the single deployment-wide 20-round allowance and allowed unsolicited wallets to occupy any round's six participant slots. This was a submission blocker. The corrected source namespaces rounds by creator, assigns a separate 20-round lifetime allowance to each creator, and freezes an explicit 3–6 wallet invite list when opening a round. The old deployment does not contain these fixes and must not be submitted.

- The contract builds a directed compatibility graph, selects one deterministic longest simple cycle of at least three participants, and clears only after every selected participant accepts.
- Participant membership is frozen before semantic assessment. The leader and validators each check a complete, ordered edge list with closed labels; deterministic code—not the model—selects the cycle and enforces lifecycle transitions.
- Inputs, participant count, per-creator round count, and graph search are bounded. No goods or funds are held or transferred.
- Workspace comparison identifies this as distinct from bilateral matching and source-to-need allocation: it requires a closed multi-party ring and unanimous acceptance.

## Verification performed locally (2026-10-23)

- `genvm-lint check` passes with the pinned `py-genlayer` runner `1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`, using the compatible GenVM `v0.2.16` bundle.
- `genvm-lint typecheck --strict`: zero errors and zero warnings. Pyright emits informational unknown-type notices for GenLayer's dynamic nondeterministic APIs.
- GenVM lint/SDK validation passes for the corrected source with the pinned runner.
- Direct tests: 8 passed, including independent owner capacities, same-name namespace isolation, fixed invite enforcement, forged validator output, and terminal-state replay.
- **Not yet verified:** no corrected StudioNet deployment or live abuse demonstration has been run. Prior deployment and receipts cover the vulnerable source only.

## Remaining submission gates

- Public source repository: https://github.com/sanity456/cycleclear. The release manifest records the repository and source-release commit.
- Push the corrected source, deploy that exact pushed revision, and verify its raw source bytes against the public Git blob.
- Demonstrate live that one creator cannot consume another's round allowance, an uninvited wallet cannot register, and valid invited participants can complete a round.
- Refresh every manifest receipt/read-back and Portal evidence link to the corrected deployment. Existing address/transaction links demonstrate only the old vulnerable source.
- Verify all final evidence links anonymously. Semantic agreement can vary; participant claims, ownership, item condition, delivery, and legal suitability are not verified.

## Known limits

Only one longest cycle is selected; the contract does not find a maximum set of disjoint cycles. It provides a coordination result, not escrow, identity verification, fulfillment, or dispute resolution.
