# Reproducible Execution And Result Synchronization

## Inputs Before Runs

Define what one sample is and what each tensor axis means. A process variable vector for one product is not a temporal window merely because a convolution accepts it. For multi-rate data, record timestamps, availability, interpolation direction and masks. For weak labels, distinguish the labeled bag/segment from the predicted instance/point. For zero-shot evaluation, define unseen classes and semantic information available without query labels.

Separate raw-data units, prepared samples and independent evaluation units. Campaigns, products, runs or sites can be the appropriate isolation unit. Non-overlapping windows are not necessarily independent when they come from the same run. Reproduce a published split when scientifically appropriate, but do not inherit a dataset name as proof that the split is leakage-free.

## Selection Is Part Of The Experiment

Record hyperparameter selection, stopping and checkpoint selection independently. A training-only schedule, validation-based early stopping and a fixed epoch count are different. A plateau scheduler needs an identified monitored quantity. No-validation designs must explain the actual selection rule without introducing a fictional validation subset. Repeatedly selecting settings, seeds or checkpoints by test performance contaminates that test; relabeling it does not repair the evidence.

A result selected after exploratory comparisons remains exploratory. Before confirmatory runs, freeze the selected configuration and a suitable independent evaluation plan. Do not discard lower-scoring completed seeds unless an exclusion rule was set in advance and justified.

## A Minimal Run Ledger

Use [the template](../assets/templates/experiment-run-manifest.md). Save code/data/split identifiers, configuration, input shape and meaning, seed, environment, selected checkpoint, selection metric/population, predictions or statistics, and run status. Hashing a file establishes identity, not scientific validity or permission to share it.

Keep runs immutable. New processing or model logic gets a new version. Associate derived tables and figures with explicit run IDs and the aggregation script version. A hand-edited PDF or table is not the source of numerical truth.

## Arithmetic And Statistics

- Verify counts, supports, split totals, percentage-point differences and metric direction.
- For ordinary single-label classification on the same complete class set, support-weighted recall equals overall accuracy. Check scope, weights and averaging before flagging a difference.
- Per-class F1 is computed from that run's precision and recall. Mean F1 generally differs from the harmonic mean of mean precision and mean recall.
- Support-weighted means can be reconstructed only with the correct supports and compatible run aggregation. Rounding introduces tolerance.
- A pooled confusion matrix, one selected run and a mean of normalized matrices are different artifacts. State which is plotted.
- Standard deviation, standard error and confidence intervals are not interchangeable. Specify repetition units and interval construction; do not demand a fixed number of seeds for every claim.
- Statistical significance is not established by bold type, a higher mean, overlapping/non-overlapping standard-deviation bars, or the word `significant`.

For continuous monitoring, preserve the raw scores, emitted alarm times, threshold source and label intervals before applying a scoring adjustment. Record the window-to-output mapping and distinguish pointwise, point-adjusted, window-level and event-level results. Derive alarm delay from the actual timeline, not the adjusted labels or the model's forward-pass runtime; use [the monitoring metric guidance](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when) when this distinction affects the claim.

## Graph And Figure Provenance

Use actual results for the actual revision. When curves summarize repeated runs, show uncertainty if it helps answer the sensitivity question and available data support it; not every plot needs bars. For independently fitted t-SNE/UMAP projections, preserve labels and comparable plotting conventions but do not interpret coordinate alignment across panels. A fixed random seed alone does not make separately fitted latent spaces directly aligned.

Record preprocessing and projection settings, selected samples, seeds and source checkpoints. A plot can corroborate class separation; it does not prove causality or quantitative generalization. Keep an approved figure design unless changing it is authorized.

## Reporting A Real-World Case

Explain the process and target, data acquisition period when verified, sample/label construction, partition and counts, then preprocessing and model settings. Avoid repeating category names in each paragraph. Protect confidential dimensions, operating recipes and product specifications, including in comments and release artifacts. Preserve reproducibility by documenting allowed units and transformations, not by exposing restricted facts.

An industrial case can complement a benchmark through a different task target, measurement setting or production variation. Do not assert complementarity merely because one dataset is public and the other private. Describe the measured engineering implication without claiming an online deployment that was not performed.

## Stop And Handoff

Separate transcription correction, result inconsistency, absent evidence and optional enhancement. Give the owner a specific verification: exact figure/table/cell, expected relation, source artifact needed and consequence for the claim. Avoid open-ended tasks such as `check all data`.

Storage maintenance is scoped: inventory owned intermediates and their reproducibility; preserve unique source/data/checkpoints/results and required recovery. Confirm deletion that affects historical recovery or a different project. A completed run, a rendered page and a submitted manuscript are separate milestones.
