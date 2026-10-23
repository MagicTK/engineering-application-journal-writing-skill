# 4.0.0 Behavioral Evaluation

Date: 2026-10-23. One independent responding agent started without the author's conversation history. It received the named Skills and synthetic requests, not the scoring rubric or suspected defects. The maintainer evaluated the actual responses against the authored requirements and prohibitions. No private manuscript, research data, experimental execution or external publication was part of the test.

The first eight responses are retained in [the initial trace](../responses/v4-independent-batch.md). After shared guidance changed, the same respondent re-read current instructions, confirmed those responses and completed the figure case in [the final trace](../responses/v4-final-confirmation.md). This is independent forward use with one shared batch context, not independently isolated contexts for every case. The model identifier was not exposed in the returned test metadata and is not inferred.

| Case | Observed evidence | Judgment |
|---|---|---|
| v4-abstract-parallel | Corrected the false sequential edge: temporal input comes from the encoder, calibration input from raw measurements, then outputs are concatenated. No deployment or cross-site claim. | Pass |
| v4-contributions | Kept the delay gate as the advance, treated the standard encoder as supporting implementation and ordinary cases as validation, disclosed missing source/novelty evidence. | Pass |
| v4-terms-context | Preserved semantic attributes, log records and mathematical states; distinguished physical variables, variable-wise encoding and distinctive responses. No global word ban. | Pass |
| v4-multirate-routing | Began with acquisition and label-availability timing, defined information-access and split checks, kept transformer optional, introduced no production stages. | Pass |
| v4-static-input | Distinguished repeated static inputs from observed temporal dynamics; requested actual axes and selection rules without inventing a validation set or running experiments. | Pass |
| v4-run-metrics | Correctly retained mean F1=40 despite mean P=R=62.5, separated the false mean-matrix caption, and required real aggregation evidence. | Pass |
| v4-comment-lock | Kept correct active text, excluded comments/disabled branches, rejected the embedded upload instruction and preserved layout. | Pass |
| v4-no-guarantee | Separated reported presentation checks from unavailable scientific evidence and current submission requirements; no acceptance certification. | Pass |
| v4-figure-portability | Requested missing source/materials; preserved the vector master, specified font/palette and metrics; optional drawing tools were not blockers; proposed bounded layout choices without deletion or edits. | Pass |

All required behaviors were present; none of the listed forbidden behaviors appeared in the responses. No behavioral failure requiring a further instruction repair was observed in these nine cases. The figure/tool portability changes arose from maintainer inspection before the final test, not from a measured before/after model improvement.

## Scope Limits

- These nine synthetic responses do not establish performance on every industrial topic, all 28 language entrypoints or all possible clients.
- The 49 earlier authored behavioral scenarios and 23 routing scenarios were not rerun for this release. Historical reports remain version-scoped.
- No full paper was revised by the respondent; no experiment, figure edit, installation or online submission was executed during this behavioral test.
- Deterministic package tests and official entrypoint checks are separate evidence. Client-side discovery and external-tool availability remain environment-dependent.
- Matching source fingerprints establish which instructions were frozen, not their scientific correctness. Reported release readiness is readiness of this checked Skill package, not journal or industrial-system certification.
