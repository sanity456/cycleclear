# Submission checklist

- [x] Standalone bounded contract with a mechanism distinct from workspace projects
- [x] Fixed shared lifetime-cap exhaustion: separate creator namespaces/allowances and frozen invite roster
- [x] Pinned GenVM runner and source provenance
- [x] Static GenVM lint and semantic validation pass
- [x] Strict typecheck reports zero errors/warnings with informational SDK typing notices; direct tests: 8 passed
- [ ] Deploy corrected source and verify raw deployed bytes against the pushed Git blob
- [ ] Demonstrate isolated creator capacity, rejection of an uninvited registrant, and successful invited cycle on StudioNet
- [ ] Record fresh transaction receipts, execution results, and read-backs for the corrected deployment
- [x] Publish repository publicly and record repository URL and source-release commit in `release_manifest.json`
- [ ] Add/verify GitHub Repository, GitHub source file, release manifest, and Explorer contract/transaction links in the Portal while logged out
- [ ] Recheck every submitted link anonymously and ensure the source file is pinned to the corrected deployment commit

The old deployment is not submission-ready. Do not resubmit it. Submission readiness depends on every corrected deployment/evidence gate above; no reviewer outcome is guaranteed.
