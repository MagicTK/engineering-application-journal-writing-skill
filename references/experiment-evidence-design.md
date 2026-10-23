# Experiment And Evidence Design Guide

## Contents

Claim types; evidence roles; split integrity; comparison fairness; ablation; robustness; sensitivity and interpretation; metrics; consistency; claim wording; experiment-owner handoff.

## 1. Evidence Begins With Claim Type

| Claim type | Required evidence | Frequent failure |
|---|---|---|
| comparative improvement | fair, relevant comparison | weak or mismatched comparison set |
| component contribution | a valid isolating comparison, replacement, intervention or analysis | only full-model performance used to attribute an individual effect |
| robustness | tests covering the stated disturbance/condition range | one tested point presented as robustness across untested disturbances |
| generalization | independent held-out evidence for the stated target population; condition/site/time separation when transfer is claimed | within-population testing presented as cross-condition or cross-site transfer |
| interpretation | process, label, perturbation, expert, or annotation validation | heatmap treated as proof |
| efficiency | the resource measure relevant to the claim: parameter count, operation count, measured memory, timing or energy | parameter savings presented as measured latency or deployment readiness |
| engineering relevance | evidence linking the task and evaluated conditions to an engineering need | a dataset name used as the entire engineering argument |
| applicability to a production setting | representative evidence from that setting, with acquisition and selection scope stated | a simulator result or curated subset presented as all field conditions |
| deployment | evaluated operational integration, timing, interfaces, and actual mode of use | historical data or streaming replay called deployed |

## 2. Evidence Role Matrix

### Benchmark Case Study

Potential evidence roles, when the construction supports them:

- controlled fault definitions;
- reproducible records;
- broad comparison;
- class-wise analysis;
- ablation and sensitivity;
- disturbance injection under defined settings.

Check rather than assume:

- simulated, test-rig or field origin and any simplification;
- label definition, version, split integrity and what is actually controlled;
- whether the evaluated conditions represent the claimed target setting.

### Real-World Industrial Case Study

Potential evidence roles:

- production-source data;
- measured process characteristics and the conditions actually retained in the dataset;
- process-specific labels and engineering meaning;
- evidence for practical relevance.

Check rather than assume:

- proprietary data and limited reproduction;
- single-site or single-period scope;
- possible annotation and selection bias;
- no automatic proof of deployment or transfer.

For a dual-evidence method paper, do not duplicate the benchmark experiment suite mechanically. Put broad ablation, sensitivity, controlled robustness, and representation analysis in the benchmark unless a production-specific question requires repetition. Use the real case for process provenance, actual data conditions, engineering interpretation, focused comparison, and a compact contribution check.

These roles are not guaranteed by the source label. A production-derived benchmark can be curated or class-balanced, while a simulator can support a well-defined engineering mechanism test. P38 in [the evidence index](published-evidence.md) selects a roughly balanced subset from much longer production recordings. Its selected class proportions are not the plant's natural event prevalence. Describe engineering relevance from the task and conditions; reserve site applicability and operational claims for evidence at those levels.

Separate the provenance of measurements from the provenance of fault conditions and labels. A dataset can combine production measurements, recorded real faults and artificially injected sensor faults, as illustrated by P31 in [the evidence index](published-evidence.md). Report those subsets without implying that every injected condition occurred in the plant. Simulation, test-rig and field measurements can each provide useful evidence, but they answer different validity questions. Protect confidential product specifications while retaining enough acquisition, target, sampling and split information to interpret the study.

Treat class imbalance as a dataset property, not as a required headline. When it materially affects training or interpretation, report the class counts in the dataset subsection, define the weighting or sampling strategy in the settings, justify macro/weighted/class-wise metrics in the metric subsection, and analyze affected classes in the results. Do not elevate imbalance to the Abstract, contribution summary, experiment overview, or Conclusion unless handling imbalance is itself a central research question or claimed contribution. Conversely, do not hide it when it changes metric choice, optimization, or the meaning of aggregate performance.

### Field Trial Or Online Deployment

Requires:

- operating duration and workflow;
- prediction timing and latency;
- human or control-system interface;
- failure handling;
- maintenance and recalibration;
- prospective or online evaluation criteria.

## 3. Split Integrity Checklist

Identify the real independence unit:

- window;
- run;
- batch;
- product;
- machine;
- patient;
- production campaign;
- site;
- time period.

Check whether adjacent or overlapping windows cross splits. Ensure normalization, imputation, resampling, feature selection, and threshold selection use training data only unless clearly justified.

For early prediction or online monitoring, exclude future measurements, downstream inspection results, or labels unavailable at decision time.

For adaptive evaluation, record the sequence `predict -> receive permitted feedback -> update` or the actual declared alternative. Target labels used to measure a prediction must not silently enter that prediction's adaptation step. Delayed quality assays require their release times to be distinguished from the time of the represented process sample. For augmentation, split independent real units before fitting the generator; synthetic relatives of a test unit must not leak into training. These rules concern information access, not whether a model is called online, generative or semisupervised.

## 4. Comparison Fairness Record

For each comparison method:

```text
Method:
Primary citation:
Implementation source:
Input representation:
Information available:
Hyperparameter selection:
Training budget:
Evaluation split:
Result source: reproduced | author code | cited
Known adaptation:
```

Report method variants once in the settings. Tables may use shorter names when unambiguous.

Input adaptation such as interpolation, aggregation, masking, or resampling is normally a documented setting, not a separate method row. Select it without test-set access. Do not import published single-rate results into a newly constructed multi-rate, missing-data, multimode, or cross-domain setting unless information access and data construction are demonstrably identical.

## 5. Ablation Design

Map every ablation to a contribution:

| Contribution | Full mechanism | Ablation | Expected observation | Actual result |
|---|---|---|---|---|

Use one-factor removal or a meaningful alternative. If modules interact strongly, add a limited interaction ablation and explain why.

Avoid an ablation table that contains many arbitrary partial models but cannot isolate a scientific claim.

When interaction between constraints A and B is a central claim, state how A changes the information, assumptions, or decisions involved in B. Where meaningful and feasible, compare neither constraint, A only, B only, and both; distinguish this condition 2×2 from switching model components on and off. Select method controls that isolate the claim: unadapted source methods, a naive serial composition, and the joint design with matched information and resource budgets. If a condition is unavailable or scientifically invalid, document the limitation and narrow the claim.

For comparable risk/error measurements on a common scale, the contrast `R_AB - R_A - R_B + R_0`, with uncertainty over the appropriate independent units, can diagnose interaction. It is scale-dependent and does not establish a causal mechanism. A joint design that shows no supported increment over the simpler composition warrants revising, merging, or rejecting that claim; the comparison must not presuppose a win.

## 6. Robustness Design

Choose disturbances from the data-generation process:

- measurement noise and drift;
- missing or delayed measurements;
- communication loss;
- visual occlusion, lighting, water mist, or dust;
- operating-condition variation;
- load, recipe, material, or product changes;
- limited labels, imbalance, or unseen faults.

State severity, injection location, whether training includes the disturbance, and which metric defines acceptable degradation. Verify the original acquisition/generation noise before describing a benchmark as clean; newly injected noise is an additional stress test. Calibrate perturbation magnitude from training statistics and document whether the transformation preserves task labels. If it changes the physical fault state or label meaning, redesign the test or relabel with justified evidence rather than forcing the original label. Choose disturbance families relevant to the claimed scope; one Gaussian injection does not establish all field robustness.

## 7. Interpretation Design

Match the artifact to an engineering question:

| Artifact | Question | Validation |
|---|---|---|
| t-SNE/UMAP | Are classes/stages separated in representation? | labels, repeats, quantitative separability |
| attention/heatmap | Which variables/times/regions influence output? | perturbation, process consistency, expert review |
| learned graph/group | Are interactions structurally plausible? | known topology, stability, alternative initialization |
| localization map | Where is the fault/anomaly? | region annotation or inspection evidence |
| frequency response | Which bands reflect condition changes? | signal/process analysis |

Use `consistent with` rather than causal wording unless the intervention and study design support the causal claim. A root-cause accuracy metric needs corresponding root-cause ground truth and an explicit evaluation unit; fault-category labels alone may not supply it. Deletion, replacement, or masking can create out-of-distribution inputs, so state the perturbation semantics and check whether that change explains the apparent attribution effect.

A confusion matrix is useful only when class-pair errors are scientifically important. It is not required for every classification paper. Prefer an analysis that tests a central mechanism or engineering failure mode when page budget is limited.

Sensitivity and interpretation plots are result-dependent artifacts. Their curves, point clouds, heat maps, and error bars must be generated from traceable experimental outputs; a design brief or placeholder may be prepared before the data, but the visible result cannot be fabricated.

## 8. Metric Integrity

Define:

- unit of evaluation;
- positive class;
- averaging method;
- class support;
- threshold selection;
- metric direction;
- repeated-run aggregation.

For weighted metrics, verify:

\[
M_{\mathrm{weighted}}=\frac{\sum_k n_k M_k}{\sum_k n_k}.
\]

Do not assume class-wise F1 averages reproduce micro-F1 or accuracy.

Check a metric's formula, implementation, scale and better/worse direction rather than copying its name from a reference paper. In generation studies, a discriminator's accuracy near chance has a different interpretation from diagnostic classification accuracy; establish the discriminator's data balance and held-out evaluation before interpreting indistinguishability. A generation-utility predictor must use the declared synthetic/real training arrangement and an untouched real test set. Visual overlap alone does not establish generation quality or privacy.

Plan repetitions before the principal comparison according to the sources of randomness, independent run/event/condition units, uncertainty needed for the claim, and available budget. Separate training-seed variation from variation across independent data units. Repeated deterministic calls on fixed data add no independent evidence; repeatedly slicing one sequence does not create independent runs. A pilot or best seed alone cannot establish stable superiority. Contribution tracks and journal tiers do not set reliability thresholds or a universal repetition count. Reuse existing run-level evidence and report actual n, selection rules, and appropriately constructed uncertainty using [the repetition-reporting guidance](journal-migration-and-completeness.md#report-actual-repetitions).

## 9. Consistency Ledger

Maintain one ledger for confirmed results:

| Case | Split/version | Metric | Main table | Ablation | Figure | Abstract/Conclusion |
|---|---|---|---|---|---|---|

Update prose only from the ledger. Reused results from the same runs must agree across artifacts, allowing declared rounding and aggregation differences. Independent reruns under the same setting can differ; record the run population and do not force numerical equality or choose whichever value is more favorable. A changed split, configuration or metric must also be identified.

Audit comparative quantifiers as well as arithmetic. `Highest weighted F1`, `highest F1 for every class`, and `better than reference B on selected classes` require different cells. State the metric, comparison set and aggregation level before using `all`, `consistently` or `best`. An aggregate lead does not establish class-wise dominance, and a lower-ranked comparison does not by itself reveal which representation it failed to learn. Keep confirmed outcomes direct and distinguish a mechanism explanation from a measured attribution.

Link each confirmed result to a `split_id`, `run_id`, metric implementation, and source artifact whenever available. Structured entry may be automated; Abstract, Results, Discussion, and Conclusion must still be rewritten from the verified result pattern.

## 10. Claim Wording By Evidence Status

- `verified`: direct conclusion within tested scope;
- `available but unchecked`: descriptive wording, no strong comparison;
- `inconsistent`: no conclusion until corrected;
- `planned`: identify as planned in an internal plan or an explicitly prospective/future-work passage, never as a completed result;
- `missing`: remove or weaken the claim.

## 11. Experiment-Owner Handoff

Use three short sections:

1. values or artifacts that conflict;
2. missing information required for reproducibility;
3. missing experiment required for a retained claim.

For each item include location, current value, conflicting value or missing field, and requested correction. Do not send a generic reproducibility checklist when only two concrete errors exist.

Preserve author-approved table fonts, widths, grouping, and float order during handoff. A large table should not be made unreadable to solve page composition; revise its evidence density or move secondary detail instead.
