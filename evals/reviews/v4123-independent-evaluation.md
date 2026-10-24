# v4.1.23 Whole-Passage Evaluation

## Execution

The initial v4.1.22 probe used one fresh context for two fictional requests. A first repaired candidate used a second fresh context for the same requests plus a positive boundary control. The final frozen candidate used a third fresh context for those three requests. Executing agents read the Skill and supplied facts, not earlier responses or grading notes. A maintainer reviewed the outputs; there was no independent second grader or statistical comparison of model behavior.

The earlier outputs remain in [iteration history](../responses/v4123-iteration-history.md). The final output is in [the response trace](../responses/v4123-revised.md). Numerical values and citation placeholders in these cases are fictional inputs, not experimental findings or real references.

## Observed Defects And Repairs

The initial answer preserved scientific meaning but repeated experiment setup in a conclusion and inserted internal novelty-classification commentary into a contribution. The first repair produced a direct contribution and a more selective conclusion, but relocated split/preprocessing detail into the Introduction. Those responses were not marked fully passed.

The existing contribution, conclusion and prose guides were refined to select facts by section role and turn internal analysis into direct manuscript claims. The rule preserves information in its appropriate Methods/Experiments location and retains a condition wherever omitting it would change a claim. It does not authorize deleting protected manuscript content, banning numbers from conclusions or suppressing unfavorable results.

## Final Scoped Results

| Case | Outcome | Observed behavior |
|---|---|---|
| PROSE4123-A | Pass | Preserved acquisition/arrival distinction, repeated observations, actual training-only reconstruction, fixed model parameters and input-varying weights. Introduction, formulation, method and conclusion carry different jobs. Setup counts remain in author notes for Experiments, while the conclusion retains same-line held-out scope, MAE and the timing-input control. |
| PROSE4123-B | Pass | Preserved the two parallel paths, frozen historical classifier, fixed mixing weights, 48-hour feedback and prediction-before-update order. Contribution describes the supported design directly. Discussion retains higher macro-F1 together with higher false-alarm rates and separately fitted case models. |
| PROSE4123-C | Pass | Replaced a batch-level reliability claim with window-level evidence; retained the single fault batch, 69/72 detected windows and 2% false-alarm rate. Overlapping windows were not treated as independent batch replicates. |

The final B response still includes a sentence about absent statistical-significance evidence that an author could move to an accompanying note. This is not a factual failure of the scoped test, nor a claim that the prose is optimal or free of every avoidable caveat. Manual author review remains necessary.

## Verification Limits

All 102 final instruction/dependency fingerprints stayed unchanged during the final test. Forty-six program tests, bilingual structure checks and installation checks are separate from this semantic review. The new count check compares declared current totals and navigation labels with source IDs; it does not determine scholarly-work identity, reading depth or conceptual equivalence. Historical counts are retained.

No new terminology family was admitted in this revision. Existing two-source and separate Chinese-verification requirements remain in force. No manuscripts, experiments or Overleaf files were modified; no LaTeX rendering or scientific reproduction is claimed. The observed response changes are not a controlled estimate of general writing improvement or full-bank certification.
