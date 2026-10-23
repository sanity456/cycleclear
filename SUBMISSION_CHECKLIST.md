# Submission checklist

- [x] Standalone bounded contract with mechanism distinct from workspace projects
- [x] Per-creator namespaces/lifetime allowances and immutable invite roster
- [x] Concrete GenVM runner pin and source provenance
- [x] GenVM AST lint passed (3 checks); direct tests passed (8)
- [x] SDK validation passed using the pinned GenVM `v0.2.16` bundle; standard typecheck passed with zero diagnostics
- [ ] Optional strict Pyright mode reports 20 diagnostics, primarily redundant type guards and unknown SDK/API types; disclosed in `STUDIONET_EVIDENCE.md` (no source/deployment change made solely to silence these)
- [x] Corrected StudioNet deployment finalized successfully and deployed bytes matched the corrected source
- [x] Live creator namespace isolation verified; uninvited registration failed closed without participant-state mutation
- [x] Public repository and commit-pinned source link recorded in `release_manifest.json`
- [ ] Before submission, independently open every repository/source/Explorer URL while logged out and ensure Portal evidence uses these corrected deployment details, not obsolete ones
- [ ] Before submission, check the Portal preview; reviewer acceptance cannot be guaranteed

Obsolete deployment `0x031a5d91fA8367bF8B64B35B0792B66580FE911A` is not submission-ready. Use only corrected deployment `0x57AECF347f700dFEc106A19CCcD62D793DEf189C` if/when all gates above are cleared.
