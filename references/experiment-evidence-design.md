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

For a focused review or a single requested verification item, prioritize the unresolved premise that can change the claim. Do not replace it with a generic audit of facts already supplied as established. With possibly inaccurate assay targets, for example, trace test-reference samples to calibration periods and independent quality-control or re-assay evidence where available. A clean split and reproducible MAE do not resolve reference validity. Preserve the observed comparison against the recorded assays, but keep accuracy against the true physical target unverified until a trustworthy reference supports it. Propose this as an author check, not permission to relabel test data or run new experiments.

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

Judge this boundary at the actual output time, not from an architecture name. A bidirectional encoder may analyze a complete batch at batch end, or a completed trailing window for its endpoint decision. Unmasked attention within that available input is not automatically future leakage or a pointwise causal model. Likewise, smoothing over a TRAIN sequence can support parameter fitting while TEST prediction uses only current and past observations. A historical state estimate revised with later observations is a delayed estimate, not the prediction originally available at that earlier time. State the target time, information cutoff and issued output before proposing a mask or model change.

Inspect the observations actually used, not only the latest permitted cutoff. A late output can result from computation on inputs already available at the target time, with no later-information access. Such a delay still needs truthful timing, but is not by itself future-data leakage. If later-released measurements are actually used, assess the estimate at its declared delayed issue time; do not relabel it as an earlier zero-delay decision. Keep this access check separate from meeting a latency deadline.

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

For a limited-label comparison, record unique source/base annotations, current-task support labels and derived training examples separately. Repeated episodes and augmented views can reuse the same labels. Match earlier training/semantic resources when the claim is about that comparison, or disclose the relevant difference and scope the finding accordingly; a pretrained model is not invalid merely because it used more historical labels. A `K`-shot result concerns its declared support budget, not automatically the total human annotation cost. A total-cost claim also needs the relevant earlier labeling resources and a defined comparison. Use the [few-shot distinctions](topic-playbooks.md#2-scarce-labels-few-shot-zero-shot-weak-or-self-supervised-learning) only for studies with this claim, not as extra requirements for every diagnostic paper.

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

For missing-value recovery claims, separate accuracy at withheld entries from the downstream prediction result. When ground truth is available by deliberately hiding observed values in independent held-out units, score the hidden entries and report the masking pattern and denominator. Keep those values out of the supplied input and fitted preprocessing; define an aggregation that remains interpretable across different missing fractions and variable scales. A loss divided by the number of sequences is not automatically an error per missing entry. Naturally unobserved values without an independent reference cannot supply a direct recovery error; downstream diagnosis can still be evaluated legitimately. Randomly withheld values support the tested masking setting, not every sensor outage pattern. A reconstruction loss on observed entries (P33) or training degradation mask (P17) is not a substitute for this held-out evidence.

When a method claims to leave observed measurements unchanged, inspect the final output equation or implementation rather than the mask's name. For finite placeholders, `x_complete = M*x_input + (1-M)*x_estimate`, with `M=1` at observed positions, preserves them by construction; masked selection must handle NaNs safely if they are present. A mask inside an encoder, or adding a learned output to the input, needs a separate check. Preservation is a useful property to report, not proof that the missing entries are accurate. This check does not require a method that estimates its output directly from available observations to introduce an imputation stage.

## 7. Interpretation Design

Match the artifact to an engineering question:

| Artifact | Question | Validation |
|---|---|---|
| t-SNE/UMAP | Are classes/stages separated in representation? | labels, repeats, quantitative separability |
| attention/heatmap | Where does the model assign weights or highlights, and do these reflect its predictive dependence? | a defined attribution target, perturbation/fidelity checks, process consistency, expert review |
| learned graph/group | Are interactions structurally plausible? | known topology, stability, alternative initialization |
| localization map | Where is the fault/anomaly? | region annotation or inspection evidence |
| frequency response | Which bands reflect condition changes? | signal/process analysis |

Use causal wording for a specified causal target supported by its identification assumptions, argument and study evidence. A physical intervention is one route, not a universal prerequisite: observational data can identify an effect under justified assumptions. Do not infer those assumptions from predictive accuracy or a directed graph alone. Where the evidence establishes only structural agreement or engineering plausibility, `consistent with` describes that result more accurately. A model-node attack or input deletion changes a computation; calling it an intervention does not by itself establish a physical process intervention. State the perturbation semantics and check whether out-of-distribution inputs explain an apparent attribution effect.

Separate the reference and scoring unit before interpreting a diagnostic number. P13 p.7 counts recovered directed relations for graph precision/recall/F1, while its subsequent table evaluates root locations; P16 p.6 separates a fault/quality-relevance decision from abnormal-link analysis. Graph-edge F1, fault-class F1 and root-location success are different quantities. Root-cause accuracy needs an independent origin reference and a defined unit, such as an event, component or variable; class labels alone may not supply it. An earliest measured response can be a declared localization proxy without being the physical initiating disturbance. For ranked candidates, state the candidate universe, k and event denominator; when several origins are possible, specify whether a hit means finding any or all reference origins. Score a two-level unit/variable search end to end as well as conditionally when that distinction governs the claim. Do not add a root-cause benchmark to a paper that claims only fault classification.

A confusion matrix can be useful when class-pair errors are scientifically important; it is not required for every classification paper. During evidence planning, prefer analysis that answers a central mechanism or engineering question. For an existing approved manuscript, preserve its figures and metrics: a constrained page budget or language review is not authorization to delete evidence. Propose any change to that scope for author confirmation.

Sensitivity and interpretation plots are result-dependent artifacts. Their curves, point clouds, heat maps, and error bars must be generated from traceable experimental outputs; a design brief or placeholder may be prepared before the data, but the visible result cannot be fabricated.

### Knowledge And Physical-Constraint Claims

If the claimed benefit is physical consistency, define the tested equation or inequality, its variables/units, applicable conditions and tolerance. Evaluate its residual or violation at the claimed output and on the claimed evaluation domain; a smaller total training loss or better diagnostic score does not establish this property. A finite-weight penalty can trade off against other objectives. Even a zero residual at training points does not by itself prove satisfaction everywhere. For an exact construction or projection, check the relation it actually enforces and preserve a justified guarantee within that scope; empirical residual checks and mathematical guarantees are different evidence.

Check the coordinate system of that relation. If network variables are standardized or scaled, either transform the physical equation consistently or evaluate it after returning to physical units; a sum-to-one identity in scaled coordinates is not automatically a physical balance. For distance-based corrections, state the space and weighting of the distance: unequal scaling changes which feasible point is nearest. Satisfying selected equalities does not additionally guarantee nonnegative outputs or unencoded inequalities. Audit only constraints actually claimed, not an invented set of process laws.

For an iterative constrained layer, distinguish feasibility, distance optimality and prediction accuracy. A solved KKT system in a nonconvex problem does not generally certify the globally nearest feasible point; P60 author version v2 explicitly makes this distinction in Section 2. A finite iteration budget alone does not certify convergence. When relevant, ask for residual tolerance, failure handling and the actual differentiation path; compare against a post-training correction only if that isolates the claimed training benefit. These are author checks, not permission to run extra experiments or weaken a verified analytical construction.

For a knowledge-guided architecture without a physical-consistency claim, select evidence about its actual contribution, such as prediction quality with the specified structural information. Do not require a conservation-law experiment or redesign. If an uncertain prior is central, state its source, what is updated and which data are available for that update; examine prior misspecification only when it is part of the claim. Keep these as targeted author checks, not permission to alter results or launch experiments. For knowledge represented in latent space, establish the mapping before interpreting embedding-distance changes as physical-law compliance.

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

Also identify the discrimination target. In P70, it is source versus target domain; in P71/P72's generation definitions, it is real versus generated input. Low domain discrimination can reflect confusion or a weak discriminator, not automatically useful class-conditional alignment; it is not a generation-fidelity score. A low GAN training loss or near-chance real/generated score does not establish convergence, diversity or diagnostic improvement. Evaluate the actual retained detection/classification path. If detection optimizes a latent input at prediction time (P71), include that work when making a latency claim; augmentation-only generation cost belongs to its actual training/generation phase.

Plan repetitions before the principal comparison according to the sources of randomness, independent run/event/condition units, uncertainty needed for the claim, and available budget. Separate training-seed variation from variation across independent data units. Repeated deterministic calls on fixed data add no independent evidence; repeatedly slicing one sequence does not create independent runs. A pilot or best seed alone cannot establish stable superiority. Contribution tracks and journal tiers do not set reliability thresholds or a universal repetition count. Reuse existing run-level evidence and report actual n, selection rules, and appropriately constructed uncertainty using [the repetition-reporting guidance](journal-migration-and-completeness.md#report-actual-repetitions).

Lock the aggregation and comparison unit along with the metric. Mean run-wise scores, metrics from pooled predictions and a single representative run answer different questions; numerical disagreement alone does not make one erroneous. Retain matched split/run/block identifiers when a comparison is paired, rather than reconstructing difference uncertainty from separate mean +/- SD columns. A seed-based interval on a fixed test set concerns that declared source of variation, not a new plant/site population. Use [the same reporting guidance](journal-migration-and-completeness.md#report-actual-repetitions) before proposing a correction, inferential claim or figure conversion; reading these checks does not authorize changing results or rerunning experiments.

For a claimed improvement in learned temporal slowness, audit feature scale and the time axis. If `z_new(t) = c z_old(t)`, its unnormalized squared first-difference energy scales by `c^2` even though the trajectory has only changed amplitude. Check normalization or noncollapse constraints, sampling intervals, feature dimensions and the aggregation before comparing scores; a first difference per sample is not a derivative per physical unit time when intervals differ. Classical SFA constrains the representation to exclude trivial constant solutions, whereas a deep model may encourage the corresponding properties with soft penalties. Report the actual objective and separately evaluate the retained prediction or monitoring claim. Do not prescribe a new SFA experiment for a model that only claims ordinary trend smoothing.

### Adaptive State, Feedback And Retention

For a central adaptation claim, record the object that changes, its update trigger, permitted observations/labels and the order of prediction, scoring and update. Include resets or persistence between domains, tasks and independent runs. Batch access can be legitimate when declared: P05 adjusts semantic references from a target test set without fitting network weights. That evaluation should be compared under matching target-data access, rather than described as a causal real-time stream merely because it uses no target labels. Conversely, a truly sequential method should retain the predictions made before later feedback or updates.

Inspect side information used to trigger adaptation. P64 assumes an operator supplies mode-switch timing; this is different from detecting switches from unlabeled measurements. Threshold updates and network updates may follow different rules. When a threshold should be computed from past accepted values, preserve decision-before-update and any freeze/exclusion rule; computing it with the current anomaly can alter the alarm being evaluated. Do not convert an adaptive threshold into proof of learned fault representations.

If earlier capability is part of the claim, compare it before and after adaptation alongside performance on the new condition. Improved current-condition accuracy alone does not demonstrate reduced forgetting. Report the actual reference and retention quantity; an explicit regularizer is a design intended to retain knowledge, not a guarantee that forgetting has been eliminated. Retain a mixed adaptation/retention result when it occurs.

Specify the scope of replay-free or data-access statements: past target examples, source examples, feature buffers, generated examples and saved model parameters are different resources. P65 retains source data despite not replaying past target instances; P64 caches features. Neither statement alone establishes data privacy or the absence of all historical information. Select additional memory, update-cost or recovery analyses only when needed for the paper's claim.

### Selection Outputs And Resource Claims

For a feature/sensor-selection claim, identify the candidate objects, ranking or selection rule, retained output and its use in the predictor. A positive weighting of all inputs does not itself delete a feature, even if the source calls its layer feature selection. For explicit subsets, trace retained descriptors back to required raw measurements and preprocessing. Permit computation of only selected descriptors when the actual dependencies support it; do not assume the complete original feature pipeline must always run.

State which data fit the selector, label transformations, subset size and stopping rule. Supervised selection is part of model fitting, so test labels used to choose a subset also influence the reported predictor. Use an actually performed training-only selection procedure or a predefined setting; do not invent a validation split to repair the account. Independent selection stability is relevant when stability is claimed, not mandatory evidence for every local grammar revision.

Report resource savings at the measured level: descriptor count, required measurement channels, prediction latency or another stated quantity. A reduced descriptor count alone establishes none of the others. If the deployed computation demonstrably reads only two sensors, retain that reduced-input result; claiming that the plant can remove hardware or reduce maintenance costs additionally requires evidence about its other sensing and control uses. Learned ranks or counterfactual changes in a classifier do not alone identify physical fault causes.

For attention-cost analysis, record query count, key/value count, embedding widths and any later concatenation. A score array has `n_query * n_key` entries; its weighted output may be smaller while the downstream representation retains all value tokens (P74). That entry count is neither a complete FLOP count nor measured runtime. Trace projections, normalization, later layers, memory layout and any actually skipped work when those affect the claim. Dense zeroing and a dimension-reduced execution graph have different cost implications. If a converted graph is claimed to be exactly equivalent, check inference-mode statistics and activation placement against the original graph before comparing resources; a faster nonequivalent graph may be a valid approximation, but needs that description and its task evaluation.

### Multilabel And Compound-Fault Decisions

Use this check when several labels can apply to one sample or when the claim concerns identifying a complete compound fault. Distinguish scores/rankings, thresholded label indicators and the final fault set. Document threshold selection and the encoding of normal operation; do not silently impose an all-zero convention on a study with a separate normal label or detector. Local mutually exclusive classifiers can still yield a multilabel final decision through a defined combination rule (P37/P39).

Per-label errors and exact recovery of the full set are not interchangeable. For a binary `N`-sample by `L`-label target, Hamming loss normally averages incorrect entries over `N*L`; exact-set accuracy counts samples whose entire label vector is correct. State the actual definitions rather than copying a metric name. A reduction in the former need not improve the latter, and many absent labels can inflate entrywise accuracy. P40 p.5 reports both label-averaged metrics and zero-one loss, but refers its formulas elsewhere; this source supports distinguishing evaluation roles, not importing an uninspected implementation.

Select metrics for the claim, not a compulsory list. When complete combination identification is central, evaluate complete sets alongside the relevant label-wise evidence; when the task only ranks candidate faults, retain that narrower output scope. Report the treatment of empty sets and averaging where it changes a metric. Preserve valid composite-class evaluation when that is the actual task; do not require a multilabel redesign solely to match other papers. These checks can often be made from existing predictions and labels without retraining, subject to the author's authorization.

### Continuous Monitoring: What Is Scored And When

Use this branch only for a claim about a time sequence, fault interval or alarm. Identify the target timestamp and prediction unit before interpreting a metric. A window labeled positive when it contains any anomalous observation is a window-level target; its classification score does not establish pointwise localization or onset accuracy. State any verified rule mapping overlapping window outputs to point scores and evaluate that output at its actual granularity.

Pointwise, point-adjusted and event-level scores answer different questions. In one common point-adjustment rule, a single hit inside a labeled anomaly interval makes all its points count as detected. This changes the scoring outcome, not the alarms actually emitted. Such F1 can hide late or sparse detection and weights long intervals differently from an event-level recall. P07 uses that adjustment, whereas P22 explicitly omits it for point-level evaluation; see the [passage notes](published-evidence.md). Describe the chosen rule and compare methods under that same rule rather than imposing one published convention or relabeling an adjusted score as timely warning. If raw and adjusted rankings differ, report the trade-off relevant to the stated objective.

For a timing claim, separate the time represented by the input, the time all required information becomes available, model computation, and the first emitted alarm. A centered window with future observations is delayed analysis of its center even when its forward pass is fast. Derive detection delay from unadjusted alarm times and an identified onset reference; report missed events separately rather than silently excluding them. For a bounded follow-up using existing traces, calculate per-event first-alarm delay alongside detected/total events. False-positive observations, false alarm episodes and alarms per operating hour have different denominators; name the one used. Do not require these additional metrics for a paper that only makes an accurately scoped window-classification claim.

### Scores, Probabilities And Rejection Decisions

Use this check for a claimed confidence, uncertainty or rejection capability, not as an extra experiment suite for every fuzzy model or classifier. First follow the quantity from its definition to its consumer: a feature weight, class probability, uncertainty score and thresholded rejection have different evidence needs.

| Claim | Relevant check |
|---|---|
| weights improve feature combination | isolate the weighting operation with matched inputs and inspect the task outcome; unit-sum weights alone do not measure reliability |
| predicted probabilities reflect correctness frequencies | compare predictions with held-out outcomes over the stated population; classification accuracy alone does not establish calibration |
| a score distinguishes known from unknown inputs | evaluate the declared known/unknown sets and score direction; ranking performance does not establish a useful fixed threshold or calibrated probabilities |
| a rejection rule is useful at an operating point | report known-class errors including false rejection, unknown rejection, and threshold selection without held-out test labels; an aggregate depends on the known/unknown mixture |
| abstaining improves accepted predictions | report both the fraction retained and errors among retained predictions, with rejected samples accounted for separately |

For classifier-logit energy `E(z) = -T log sum_c exp(z_c/T)` with fixed positive `T`, adding the same constant `a` to every class logit leaves softmax probabilities unchanged but changes energy to `E(z)-a`. This algebraic check shows why the score is not itself a probability and why a threshold is not portable merely because class probabilities match. Verify score sign and range against the actual implementation; do not replace a disputed sign or threshold by guessing. P18 and P51 use related base definitions for different purposes, as recorded in [the terminology bank](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

Keep the proposed evaluation proportional to the retained claim. If a model only learns feature perturbations and outputs known fault labels, evaluate its stated condition-generalization task without inventing a rejection head. If an uncertainty estimate does drive rejection, the chain `estimate -> decision -> measured outcome` should appear consistently in the overview, contributions and results. Designing these checks does not authorize running new experiments or changing recorded outcomes.

For a Dirichlet class-evidence output, reduced uncertainty mass is a change in a model quantity, not an error-rate measurement. Probability calibration evaluates the stated probabilities against outcomes; calibration of an error-probability score would target that different event. Neither follows merely from threshold selection on separate calibration data. Equal class-probability means can accompany different concentration, so preserve both the score definition and the measured decision outcome before describing a reliability improvement. Use the [quantity check](terminology-decisions.md#evidential-classification-quantities) without requiring every uncertainty score to be an error probability.

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
