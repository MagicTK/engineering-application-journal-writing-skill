# Journal Migration And Completeness

Use for an authorized venue change, section consolidation, or shortening audit. Retarget presentation without silently changing the task, experiments, or evidence. [Chinese counterpart](journal-migration-and-completeness_CN.md).

## Separate Authority From Observation

Verify current author instructions on the destination journal's official site for the applicable article type and submission stage. Record the source, access date, and exact requirement separately from an author preference or internal target. If verification is unavailable, flag uncertainty. A published paper illustrates a writing choice, not an editorial mandate. Neither TSMC: Systems nor Transactions on Cybernetics examples establish one style for all IEEE journals. Do not universalize reference counts, page targets, metric-equation counts, or repetition counts. Replace superseded internal advice with the author's latest authorized preferences without misrepresenting publisher requirements.

## Inventory Before Shortening

Lock the authoritative source and baseline PDF; back up authorized edit targets. Inventory active sections, definitions, assumptions, equations, datasets, splits, metrics, tables, figures, captions, references, and evidence boundaries. Separate active content from comments, archived results, and incomplete author notes. Track each substantive item as retained, rewritten, relocated with a destination, or removed with a reason. A commented block is not published supplementary material. Older data sizes, settings, and scores require provenance checks before restoration; do not mix experimental versions. Check result-dependent prose alongside tables and figures.

## Rebuild The Argument

When integrating Related Work into the Introduction, organize paragraphs around the engineering requirement: prior premise, relevant evidence or capability, limited unresolved issue, then the present response. Keep citations next to the claim they support. Preserve distinctions among close methods; avoid both a pasted literature catalog and blanket claims that earlier work ignores an entire relationship class. Retain necessary boundaries without repeating caveats everywhere.

A standalone Problem Formulation can clarify input units and dimensions, supplied partitions or priors, available labels, prediction targets, and necessary assumptions. Open by connecting the industrial difficulty to these objects. Close by identifying the remaining modeling requirement that the Method overview answers. Put implementation operators in Method unless needed to define the task. Avoid a generic textbook preamble, duplicated module lists, or invented theory to justify a new section. Section placement is conditional, not a journal-wide rule.

## Shorten Without Losing Meaning

Prefer precise paragraphs and removal of duplicated explanations before deleting definitions or evidence for a page target. Retain or restore metric definitions needed to interpret the results, including class-wise versus macro/support-weighted averaging and undefined-denominator handling. Equations may be combined or replaced by unambiguous prose when appropriate; neither deleting all standard metrics nor preserving every equation is automatic. Preserve approved font sizes, numerical data, table geometry, and float locks. Where migration requires changed layout, obtain the relevant authorization and establish new locks before reformatting.

## Report Actual Repetitions

P, R, F1, and Acc. can shorten labels only when defined. Abbreviations do not guarantee that mean +/- SD values fit; render the actual table before proposing an authorized layout change. Recover existing run-level records first. State actual n for each experiment, seeds, fixed or varying splits, and checkpoint selection. Do not relabel completed runs to match a preferred count or demand new experiments merely for uniformity. For a mean run-wise score, compute the metric within each run before averaging, rather than deriving F1 from averaged precision and recall. Sample SD uses n-1; it is undefined for one run. Distinguish variability (SD), uncertainty of the mean (SEM), and a confidence interval with its stated construction.

A deliberately pooled analysis is a different valid summary when defined: combine the declared predictions/counts, then calculate the metric. Nonlinear metrics such as F1 need not match the mean run-wise metric; accuracy can match when run sizes are equal. Do not silently change an approved aggregation merely to reconcile the numbers. Repeated predictions on the same test items are run-example records, not additional independently acquired samples. Preserve the declared class order, weighting, support and denominator for either summary.

Name the source of variation: training initializations on fixed data, cross-validation folds, or independent production units are different. P66 Fig.4 labels its bands as SD over five folds, not five independent seed runs. Descriptive fold SD can be reported, but overlapping training folds do not automatically provide independent replicates for an inferential interval. Choose an uncertainty analysis for the question actually claimed; do not force every study into one run count, resampling scheme or significance test.

For a matched comparison, retain the pairing key and analyze the run/block differences when that is the design. The marginal means and SDs alone do not determine the spread of those differences; covariance matters. Do not sort the methods separately or create a pairing just from equal list lengths or matching seed labels. Overlap of SD bars is not a significance test. A confidence interval for a mean difference needs its construction and sampling assumptions, distinct from the SD of either method. Report a supported higher mean directly without upgrading it to significant superiority or cross-condition robustness.

## Match Uncertainty To The Figure

For repeated sensitivity points, hold other settings fixed and use consistent seed sets where available; report actual n and the selection split. Use error bars at discrete settings or clearly labeled bands for a trend, identifying mean +/- SD, SEM, or CI explicitly. Include repeated robustness intensities and performance axes of efficiency plots; fixed parameter counts need no run-variability bars. Percentage-scale SD is in percentage points.

Confusion matrices and t-SNE require declared representative-run selection, preferably a prespecified seed or validation-based rule, not the best-looking test plot. State normalization for matrices and sample/layer/projection settings for embeddings. Do not average unrelated two-dimensional embeddings. Any across-run matrix summary needs its own aggregation definition. Architecture and process schematics need no statistical bars. Reconcile captions, tables, plots, and prose, then compile and inspect the authorized package.

## Published Examples, Limited Roles

- Zhou et al., *Industrial Fault Diagnosis With Incremental Learning Capability Under Varying Sensory Data*, TSMC: Systems (2025), [DOI](https://doi.org/10.1109/TSMC.2024.3500019), pp.1323-1325: Introduction to definitions/objective in Section II, then a three-module Method. Borrow this transition, not its online-learning assumptions or guarantees.
- Song et al., *Addressing Heterogeneous Time-Frequency Causality: Source Consistency Exploring for Industrial Root Cause Alignment and Diagnosis*, Transactions on Cybernetics (2025), [DOI](https://doi.org/10.1109/TCYB.2024.3515174), pp.1108-1110: Section II problem/motivation precedes Method. It concerns root-cause diagnosis; its causal claims do not transfer to ordinary classification.
