# Same-Context Retest

This retest uses the existing conversation context and the updated shared references. It is not fresh-context evidence.

## v412-uncertain-assay-evaluation

**Corrections**

The method constructs training targets; it does not correct the unchanged TEST assay values, and no sensor corruption is established. The lower MAE supports better agreement with the recorded TEST assays, not proven improvement against true concentration.

**Bounded replacement**

The model derives continuous targets from neighboring TRAIN samples for training and achieves a lower MAE in the reported comparison against the unchanged TEST assay values. Because calibration records suggest that an unknown subset of those values may be inaccurate, this result establishes better agreement with the recorded assays but does not establish improved accuracy relative to true concentration.

**One practical verification item**

Ask the author to cross-reference TEST assay sample or batch identifiers and assay times with the calibration records, including any flagged periods, and any existing independent quality-control records, to determine which evaluation references may be affected and whether their validity has trustworthy corroboration. Where the records cannot resolve reference validity, document that uncertainty and retain the reported MAE comparison with true-concentration accuracy unverified. This is an existing-records check, not a request to replace TEST targets, obtain new assays, or retrain models.

## v412-rerun-and-approved-ablation

No numerical correction is required. Retain **82.31%** in the main table and **82.18%** in the ablation table: they are correctly defined mean macro-F1 values from separately documented independent rerun sets, not conflicting reports of the same runs. Numerical equality is not required across those sets. Preserve all approved rows, plots, and fonts; this difference alone warrants neither retraining nor further manuscript changes.

## Effect On The Other Original Answers

The updated references do not change the meaning of `v412-alternating-target-selection`, `v412-supervision-semantics`, `v412-partial-classifier-title`, or `v412-selected-features-not-sensors`. Their distinctions between training and prediction, supervision meanings, local versus global label spaces, and descriptors versus sensors remain applicable; no rewrites are needed. The repeated assay case instead changes the priority of its verification item to reference validity. `responses.md` is preserved unchanged.
