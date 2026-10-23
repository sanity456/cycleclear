# Architecture

1. A caller opens a unique round with a bounded exchange context.
2. Each wallet registers exactly one offer and one need. The creator freezes the participant set at three to six wallets.
3. Any caller requests assessment. The leader and each validator independently classify every directed pair into `FITS`, `DOES_NOT_FIT`, or `UNCERTAIN`; the complete ordered result must match exactly.
4. Deterministic code builds a directed graph from `FITS` edges, enumerates simple cycles of length at least three, and selects the longest cycle with a stable lexicographic tie break.
5. Each selected wallet accepts or declines. A cycle becomes `CLEARED` only after all members accept; any member may decline and close it.

The semantic judgment matters because participants do not know the counterparties when they register and cannot enumerate all indirect matches by themselves. The code, rather than the model, selects the cycle and enforces that every selected member's outgoing offer satisfies the next member's registered need.

Bounds: 20 rounds per deployment, six participants per round, 800 UTF-8 bytes per offer or need, 1,000 bytes per context, and at most 30 directed judgments per assessment. Round identifiers are permanent and cannot be reused.
