# 4.1.9 Adaptation And Distillation Evaluation

## Scope And Provenance

One fresh responding agent read the immutable 4.1.8 public instructions and answered three fictional requests without seeing scoring criteria, private papers, revision notes or expected answers. The same respondent then read the frozen 4.1.9 instructions and answered those requests plus a positive control authored after the freeze. The control explicitly retains teacher execution at prediction, preventing the training-only example from becoming a blanket deletion rule.

The maintainer reviewed the actual answers against the supplied facts. This is an independently generated response with maintainer grading, not a separate independent grader, four fresh contexts or full-suite certification. The runtime did not expose an exact inherited model identifier. All three baseline cases already passed; the candidate results support preservation and added coverage, not a measured performance improvement. No private manuscript, experiment or deployment was evaluated.

## Observed Decisions

| Case | Baseline | Frozen candidate | Evidence in the actual answer |
|---|---|---|---|
| A: regression distillation and exits | Pass | Pass | Retains teacher feature/regression guidance without requiring softmax; distinguishes training from student prediction and fixed-parameter exits. The English keeps the two roles connected without inventing accuracy or speed results. |
| B: label spaces and supervision | Pass | Pass | Retains domain adaptation with a target class subset; asks whether target labels are observed or inferred. It separates fitting losses from classifier-output combination. The revised answer keeps the unresolved condition in an author note and requires it to be resolved before finalization, rather than hiding it by removing one adjective. |
| C: compound name and score discrepancy | Pass | Pass | Does not count partial-word matches as support for a complete module name. Describes the displayed softened distributions without certifying implementation; requires separate Chinese-source verification and does not pretend to have browsed. |
| D: teacher retained at inference | Not run | Pass | Preserves same-architecture teacher/student roles and the stated 0.2/0.8 prediction combination. Rejects an invented lightweight feature-fusion claim and does not delete the actual teacher path. |

The D contribution sentence is a factual method description, not evidence of novelty. The A sentence is relatively detailed; this check does not establish a universally optimal abstract length or style. No execution or speed claim is supported by these fictional facts.

## Records And Limits

- [Baseline responses](../responses/v419-baseline.md) are preserved verbatim.
- [Frozen-candidate responses](../responses/v419-revised.md) are preserved verbatim.
- [Executed report](../history/v4.1.9/forward-test-report.json) records the four requests, criteria and the 102 instruction/dependency fingerprints.
- The [previous report](../history/v4.1.8/forward-test-report.json) is retained as historical evidence, not reused to pass this version.

No behavior-driven instruction repair was required in this scoped run. Before freezing, deterministic checks caught incomplete pending-report fields and a stale expected version; these were corrected without weakening the validators. Structural, installation and publication checks remain separate from these behavioral results. The terminology ledger is still partial, and neither the 46-paper index nor these four cases certifies every named mechanism in the suite.
