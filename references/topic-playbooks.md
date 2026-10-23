# Topic Playbooks For Data-Driven Industrial AI Papers

## Purpose

Load only the playbook matching the manuscript's actual challenge and method. These are conditional supplements to the general engineering narrative, not mandatory themes.

Evidence lists are menus, not a requirement to run every test. Select a test because it can distinguish the stated claim from a plausible alternative. A multi-rate soft sensor, a zero-shot classifier and a weakly labeled detector need different targets, splits and metrics even when all use neural networks. Source IDs below refer to [published passages and transfer boundaries](published-evidence.md); they support scoped examples, not universal prescriptions.

## Contents

Observation and sampling; scarce supervision; multimode/nonstationary operation; multisource/multimodal data; plant-wide and multistage systems; graph/knowledge/causal/fuzzy models; generation and diffusion; LLMs; efficiency and edge use; interpretability and root cause; mixture of experts; compound/open-set faults; dynamic and time-frequency representations; control and decision systems.

## 1. Incomplete, Asynchronous, Or Multi-Rate Observation

First identify whether the study concerns missing values, irregular timing, delayed measurements, or groups with different fixed sampling rates. Do not merge these definitions for convenience.

Writing priorities:

- explain the industrial acquisition mechanism before mathematical encoding;
- state what is observed, when, and at what rate or delay;
- distinguish native observations from values created by interpolation, aggregation, padding, or alignment;
- explain information loss, bias, or computational cost at the assumption level;
- keep a multi-rate paper centered on the multi-rate industrial process rather than rebranding it as generic irregular sampling.

Evidence priorities:

- rate/missingness construction and provenance;
- leakage-safe preprocessing;
- comparison under common information access;
- rate/missingness severity analysis;
- masks, timestamps, and reconstruction fidelity when they affect the task.

Choose the narrative from the observation mechanism. For fixed multi-rate streams, explain which variables are measured at each rate and how slow measurements align with the prediction target. For irregular observations, explain how elapsed time differs from sequence position. P24 explicitly encodes both; its solution does not make every multi-rate problem irregular. For delayed quality assays, distinguish the time represented by a label from the time it becomes available. `Offline assay` can accurately describe laboratory measurement even when `offline dataset` adds nothing to provenance.

If completion and prediction are coupled, identify which quantities are observed, imputed or merely latent, and which branches are used at inference (P25). Do not claim physically accurate reconstruction from downstream prediction accuracy alone. If the target is causal structure (P08), structure-recovery assumptions and evidence take priority over a generic diagnosis comparison. Do not invent a universal minimum number of rates from one paper's definition.

Also distinguish acquisition from augmentation. P26 deliberately transforms time sampling to create a self-supervised target; its title alone does not establish naturally irregular industrial acquisition. Describe a synthetic sampling transformation as a learning operation unless the data provenance independently establishes an irregular observation process.

## 2. Scarce Labels, Few-Shot, Zero-Shot, Weak, Or Self-Supervised Learning

Writing priorities:

- define exactly which classes, conditions, samples, or label levels are unavailable;
- separate semantic transfer, representation pretraining, pseudo-labeling, and sample generation;
- state what target-domain or unseen-class information is accessible during training and tuning;
- tie the challenge to industrial annotation cost, safety, rarity, or emergence of new faults.

Branch by the actual supervision arrangement:

| Setting | Essential writing distinction | Claim-matched evaluation |
|---|---|---|
| Few-shot classification | What counts as a shot, which classes are known, and whether support/query episodes or a fixed split are used | The declared label budgets and sampling variability; do not impose episodic evaluation on a non-episodic design |
| Zero-shot diagnosis | Which fault classes lack labeled training samples; where their semantics come from; whether unseen-class measurements are used during adaptation | Class-disjoint evidence and semantic-source checks; seen/unseen balance or harmonic metrics when the test is generalized zero-shot, not automatically for unseen-only testing |
| Semisupervised classification | Which samples are labeled, how unlabeled data affect learning, and whether source and target distributions differ | Matched label budgets and unlabeled-data controls; separate class-prior imbalance from feature-distribution shift |
| Semisupervised regression/soft sensing | Which quality targets are observed and how unlabeled process measurements constrain the predictor | Regression error in the target's units, label-budget sensitivity and a relevant supervised control; no seen/unseen class metric without classes |
| Weak segment/bag labels | The labeled unit and the finer prediction unit; how training relates the two | Evaluate at the claimed output granularity; bag accuracy alone does not validate point localization |
| Candidate-label ambiguity | Whether one true label lies in a supplied candidate set, and how alternatives are resolved | Evaluate against independently established target labels; a candidate set is not a statement that all listed faults coexist |
| Inaccurate labels or targets | Which annotations or assay values may be wrong, how this was established, and what the learning mechanism changes | Distinguish sensor corruption from target corruption; performance against an uncertain reference alone does not establish accuracy against the true physical target |
| Self-supervised learning | How targets are constructed, what augmentation preserves physically, and how pretraining supports the downstream task | Relevant pretraining/target controls and downstream evaluation; do not imply that no labels are used anywhere if a downstream head is supervised |
| Unsupervised clustering | Which object is clustered, how the number of clusters is determined, and how clusters are related to fault identities | Clustering quality and the declared evaluation-only label matching; do not conceal labels used for model selection or imply cluster indices already identify faults |

P05-P06 exemplify semantic transfer; P17 uses labeled and unlabeled measurements for concentration prediction; P21 couples self-supervised and diagnostic learning; P22 learns from segment labels for point-level detection. Their method names do not make these supervision arrangements interchangeable. P18 adds long-tailed classes and cross-domain information, in an adjacent equipment setting.

For an interval/window-to-point claim, trace the actual output rather than broadcasting the training label. P22 defines a point-scoring mechanism and evaluates its point outputs without point adjustment. A different model that only classifies windows should retain that output scope. The [continuous-monitoring metric guidance](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when) separates window classification, point scores, interval adjustment, event detection and alarm timing; none is a substitute for another merely because the reported metric is called F1.

State target-data access positively and precisely. Unlabeled test-time adaptation can be legitimate under its declared setting (P05); it is not equivalent to inductive prediction and must not access held-out labels. Calibration, class-disjoint splits and prompt sensitivity are appropriate only when the task or claim calls for them. Choose chronological or entity-disjoint evaluation where acquisition dependence requires it, independently of the supervision label.

P19 learns an affinity representation for spectral clustering of fault samples, while P20 groups partial-discharge pulses. These are adjacent mechanical/electrical examples of clustering as an output task, not evidence that an internal variable-grouping layer should be called a diagnostic clustering method. A permutation-invariant metric may use held-out labels solely for evaluation; choosing clusters or tuning the model with those labels is a different information boundary.

Do not infer annotation semantics from `partial-label`, `multilabel` or `label enhancement` in a title. P39 defines known simultaneous fault indicators and partial classifiers over pairs of fault types; its partial label spaces are not evidence that each training sample has an ambiguous candidate set or missing annotations. P40 alternates a learned continuous label representation with feature selection. Such values can guide learning without being measured severity, calibrated probabilities or corrected ground truth. Specify what generated them and the physical evidence required for any stronger interpretation. Keep learned targets inside the declared training boundary; do not silently replace evaluation labels with model-generated values.

For the abstract or contribution, connect the actual label limitation to the operation that uses that information: bag aggregation relates coarse supervision to instance prediction; a candidate-label method resolves alternatives; a target-refinement method changes training guidance. These are different mechanisms, not synonyms for `using fewer labels`. Preserve a precise paper-specific term when its definition is sound, and explain it before borrowing it for another study.

## 3. Multimode, Nonstationary, Domain-Shift, Or Continual Operation

Writing priorities:

- distinguish discrete operating modes from continuous drift;
- define source/target or historical/current information access;
- explain how process changes alter the data distribution or task boundary;
- avoid treating random train/test splits as evidence for temporal adaptation.

For static domain adaptation, describe source/target data access and the representation or objective being aligned. A training alignment objective is not necessarily part of the deployed prediction path (P10). For continual updates, additionally describe update triggers, retained information, adaptation delay and forgetting. A static cross-condition comparison does not establish continual learning. Reserve unknown-class rejection for an actual open-set task; an unseen operating condition need not contain an unseen fault class.

Check whether adaptation actually concerns learned parameters. Input-dependent routing can respond to a new window with frozen parameters; a recurrent state or rolling score reference may change without retraining. These mechanisms can be described as adaptive at their defined level, but they do not alone constitute continual learning. P24 conditions temporal weighting on observed intervals, whereas P04 defines a rolling statistical score after reconstruction. Keep the changing object consistent from contribution to Methods and evaluation; do not add an online-learning experiment to a paper that claims only input-conditioned weighting.

Select chronological, mode-held-out, cross-period or cross-site evaluation according to the claimed shift. When drift and class proportions both change, distinguish their effects rather than attributing all change to a generic domain gap.

Name the distribution that changes, not just `concept drift`. P30 defines a change in `P(X|Y)` while keeping class priors fixed; other work may use drift terminology for `P(Y|X)`, `P(X)` or `P(Y)`. Preserve the manuscript's equations and assumptions rather than transferring a name alone. Do not equate every observed prediction error with a detected drift event.

For adaptive models, state **what triggers which update, using what available information**. P27 triggers learning strategies from error-related events; this does not establish event-triggered sensor sampling or a fault alarm. If the trigger uses a true quality target, explain when that target becomes available. If adaptation is the advance, distinguish prediction before feedback from performance after the update; select recovery delay, update cost or retained performance only as needed for that claim.

## 4. Multisource, Multimodal, Or Cross-Modal Industrial Evidence

Writing priorities:

- trace each source from physical event to sensor response and sample unit;
- explain synchronization, alignment, and information timing;
- distinguish complementary evidence from duplicated inputs;
- make the fusion mechanism answer a concrete heterogeneity or reliability issue.

Evidence priorities:

- single-source and fusion comparisons; for numerical-to-image same-source views, select numerical-only, visual-only, fusion, and a simple image-model control as needed to isolate representation or pretrained-backbone claims;
- missing/corrupted modality tests;
- alignment perturbation;
- modality contribution and failure cases;
- localization or decision evidence when the application requires it.

Distinguish acquisition alignment, representation compatibility and learned interaction. P38 synchronizes video/current acquisition, maps their different input shapes into compatible token dimensions, and learns directional cross-modal interactions. Equal embedding widths alone do not establish temporal pairing or one-to-one correspondence. State which modality queries which information when this affects the output, without assuming the paper's arrow convention is universal. Separate class-level decisions from pixel-level localization and match each to its annotation and evaluation; reconstructing a prediction map is not necessarily reconstructing the original measurements. Two derived views of the same signal should not be presented as independently acquired modalities.

## 5. Plant-Wide, Multistage, Multiblock, Or Production-Process Modeling

Writing priorities:

- define system boundaries, units, stages, material/information flow, and hierarchy;
- distinguish physical topology, control structure, temporal order, and learned relation;
- state the system level and output localization level;
- avoid reducing a plant-wide problem to a flat variable matrix without explanation.

Evidence priorities:

- stage/block/unit ablations;
- relationship or topology perturbation;
- batch-, campaign-, unit-, or route-level split integrity;
- process-wide versus local performance;
- computational scaling with variables, units, or graph size.

Load variable/channel terminology only when the selected mechanism actually models, groups, clusters, or routes process variables. In that case:

- introduce measured or manipulated variables and their process roles before defining one variable as one input channel;
- distinguish fixed process-informed partitioning from data-driven grouping or clustering;
- use `relationship`, `interaction`, `coupling`, `correlation`, or `feature fusion` according to the implemented operation rather than defaulting to `channel dependency`;
- keep channel-strategy terminology in the method-level computational explanation, not as the default engineering motivation for every multistage paper.

If the method does not manipulate variable-level relations, do not introduce channel-strategy language merely because the data are multivariate.

Keep the hierarchy explicit: physical unit membership may be fixed, variable grouping may be learned, and pooled stage features may later return context to variable features. An overview should name those transitions without turning every level into a separate contribution. P01 links multiscale extraction and stage fusion; P04 distinguishes process knowledge from learned connections. Neither makes every plant-wide method require grouping or a residual branch. A batch's temporal phases (P09) should not silently become spatial production units.

## 6. Graph, Knowledge-Guided, Causal, Or Fuzzy Modeling

Writing priorities:

- state the source of every graph, rule, membership function, or knowledge constraint;
- separate known structure, expert input, learned relation, and causal assumption;
- distinguish a physical causal claim from a defined computational term such as causal convolution; match assumptions and evidence to the intended claim;
- use fuzzy terminology for actual membership/rule mechanisms, not as a decorative synonym for uncertainty.

Make the knowledge entry point explicit: data organization, graph edge/bias, loss term, hard constraint, decision rule, or inference-time correction. These choices have different consequences. P04 uses process structure in representation learning; P12 uses expert rules in decision-space design. Do not reduce both to an unexplained `knowledge-feature fusion` operation.

Check knowledge provenance separately from its name. In P12, variable-wise class statistics construct the expert support, abstention and rejection regions; `expert system` does not mean that every quantity was supplied independently by a human expert. Describe which rules are specified, which quantities are estimated from labeled measurements, and which partition supplies those measurements. P14 uses process-informed subgraphs and prediction-trained adjacency. A given physical partition, learned edge weights and a decision-level support vector are not interchangeable priors.

For a causal claim, name the target (for example a directed dependence structure, an intervention effect or a root-cause ranking), its assumptions and the evidence available. Good diagnostic accuracy does not establish any of these by itself. An expert-consistent graph can support engineering plausibility without proving causal identification.

A causal temporal convolution concerns past-versus-future information access; a predictive adjacency is a learned relationship; physical causal identification needs additional assumptions and evidence. P14 provides a useful place to inspect these distinct roles, not a license to equate them. Check the complete computation before using `hard exclusion`, `sparse` or `independent`: logit reweighting followed by softmax is not automatically class exclusion, and a block-diagonal adjacency does not prevent a later dense layer from combining groups. Resolve equation, pseudocode and implementation differences in author notes before strengthening the prose.

For fuzzy models, define the membership domain, rule/aggregation operation and intended interpretation. Normalized memberships or softmax assignments are not automatically calibrated class probabilities. P07 uses fuzzy states to construct temporal relationships and training constraints; that does not justify applying calibration metrics to every membership value. Evidence might instead examine rule effects or membership sensitivity. Probability calibration is pertinent when the output is explicitly a probabilistic forecast; evidential masses and fuzzy memberships require their own definitions.

Do not treat all fuzzy mechanisms as a rule base. P27 uses a fuzzy predictor after deep feature extraction, P28 uses layer-wise fuzzy clustering to reinforce reservoir features, and P33 couples fuzzy clustering with imputation. Identify whether membership describes an input region, a temporal state, a cluster or another defined object. Clustering memberships do not by themselves supply readable expert rules; a fuzzy layer or a physically motivated kernel does not make the entire model interpretable without specifying what can be explained and to whom.

Choose removed/randomized/corrupted-prior controls when they isolate the knowledge claim. Preserve constraints that define a valid process when constructing a perturbation; a physically impossible random graph can be a stress test but not a realistic operating alternative.

## 7. Generative, Diffusion, Or Data-Augmentation Methods

Writing priorities:

- establish whether generation is the primary task or a training aid for diagnosis/prediction;
- explain the actual need for generation and the limitation addressed; scarcity, imbalance and corruption are possible motivations, not compulsory background claims;
- state conditioning information and prevent train-test contamination.

Evidence priorities:

- real-test-set downstream performance;
- diversity, coverage, fidelity, and class consistency;
- comparisons against simpler augmentation;
- synthetic-to-real ablations;
- expert or mechanism checks where meaningful.

For generation as the task (P32), distinguish fidelity, diversity, condition consistency and downstream utility. Downstream utility can be one evaluation dimension without making diagnosis the primary task. P32 motivates generation with data availability, but this does not require another manuscript to assert an unobserved shortage. For augmentation as the means (P35), trace real training samples through the generator to the downstream learner, then evaluate that learner on untouched real test units. Do not put an augmentation-only generator into the diagnostic inference path. A latent-space generator also needs its encoder/decoder roles made clear; lower latent dimensionality alone does not measure total generation cost.

Do not call diffusion-step denoising the removal of actual sensor noise unless that restoration task is defined and tested. A fault label, health indicator or other generation condition is not necessarily an `operating condition`. Similar-looking generated trajectories do not demonstrate physical validity or privacy protection. State the real-data split before fitting the generator, synthetic/real training proportions and the conditioning information; avoid a blanket `privacy-preserving` claim from synthetic data alone.

## 8. LLM, Foundation-Model, Or Semantic-Reasoning Assistance

Writing priorities:

- specify whether the model supplies semantics, code, retrieval, reasoning, labels, or decisions;
- identify prompt, knowledge, and external-information sources;
- keep the industrial data and decision path primary;
- do not imply physical understanding from fluent text alone.

Evidence priorities:

- prompt/model/version sensitivity;
- ablation of semantic information;
- hallucination and invalid-output rate;
- privacy and data-governance boundary;
- comparison with non-LLM semantic baselines;
- human review when outputs enter operational decisions.

If an LLM supplies category semantics rather than predictions, trace `source text -> verified descriptor -> downstream learner`, including whether the text identifies test classes or outcomes. P05 motivates this distinction. Knowledge retrieval, semantic annotation and test-time adaptation are separate operations; do not hide their information access under a single `LLM-assisted` label. Do not transmit private process data to a service without explicit authorization.

A different route textualizes numerical measurements before embedding them (P29). Specify the measurements, time context, units and prompt information available to the textualizer, and distinguish its output from independently supplied class descriptions. Check that true fault labels or later outcomes were not inserted into sample text. External textualization cost belongs to the inference boundary when it is required for each prediction; a training-only semantic lookup has a different boundary. P29 formulates its compression-derived prior on embedded samples, not directly on the raw measurements or prose. Identify the compressed object and its encoding before interpreting a compression score; such a proxy is not automatically a physical measure of system complexity.

## 9. Lightweight, Efficient, Online, Or Edge-Oriented Methods

Writing priorities:

- name the resource being compared; specify target hardware and timing boundaries for runtime or deployment claims, not as a prerequisite for a scoped parameter-count comparison;
- separate compact design from deployment evidence;
- report the accuracy-cost trade-off rather than only a smaller parameter count.

Evidence priorities:

- parameters, FLOPs/MACs where appropriate;
- measured latency, throughput, peak memory, and energy on named hardware;
- declared end-to-end timing boundaries, including preprocessing, data transfer, routing, image conversion, tokenization, and any required external-model calls; separate cold-start and steady-state costs when relevant;
- batch size and software environment;
- scaling and stability under online updates;
- comparison at similar accuracy or resource budgets.

Separate **parameter efficiency, training efficiency, generation cost and diagnostic latency**. A frozen reservoir can reduce trainable parameters while retaining substantial state-update work (P28). Event-triggered learning can reduce updates without changing per-prediction computation (P27). Adaptive polynomial degree changes a model's work as well as its parameterization (P31); name what is actually timed. For a real-time claim, relate measured end-to-end latency and its variability to the decision interval or deadline. A small parameter count, low FLOPs or an `online` update rule alone does not establish deadline compliance. Do not require a hardware trial merely to report a correctly scoped parameter-count comparison.

## 10. Interpretability, Localization, Root Cause, And Trust

Writing priorities:

- define the user, decision, and explanation target;
- distinguish visualization, feature attribution, localization, diagnosis, and root cause;
- state whether the explanation is intrinsic or post hoc;
- avoid turning attention weights into causal conclusions.

Evidence priorities:

- fidelity, deletion/insertion, perturbation, or counterfactual tests;
- stability across seeds and nearby inputs;
- variable/component/region-level ground truth where available;
- engineering consistency and expert review;
- useful negative and boundary cases.

For root-cause metrics and distribution shifts introduced by explanation perturbations, use [the interpretation evidence guidance](experiment-evidence-design.md#7-interpretation-design).

For quality-related work, distinguish the task from the industrial reason it matters. P01's production case classifies product-shape abnormalities; P09 predicts quality categories using regression-derived representations; P16 defines quality-related detection statistics and a further root-cause analysis. These are different routes, not a hierarchy that every paper must implement:

| Defined target or output | Coherent account | Additional claim needing its own support |
|---|---|---|
| Product grade or defect category | Classify inspection outcomes from associated process measurements | Which process unit or intervention caused the defect |
| Continuous quality quantity | Estimate the measured target, with its units and availability | A diagnosed fault class or a corrective control action |
| Quality-related versus unrelated process fault | Explain the rule, target relation or statistic making that distinction | Root-cause identification beyond the relation test |

One method can be evaluated with different case-specific class meanings. Name those meanings in the case descriptions and use a shared task description only at the level they genuinely share. Separately trained classifiers on process-fault and product-quality labels do not establish transferred class semantics. A production topology used in feature learning can support a quality classifier without providing cause labels. Preserve a technically defined `quality-related diagnosis` term, but do not manufacture quality regression, subspace decomposition or causal identification to make a generic phrase sound more sophisticated.

## 11. Mixture Of Experts And Adaptive Routing

Writing priorities:

- identify what causes expert specialization: mode, stage, source, regime, task, or uncertainty;
- explain routing information and availability at inference time;
- distinguish adaptive decomposition from merely increasing capacity.

Evidence priorities:

- expert utilization and collapse diagnostics;
- routing ablation and random routing;
- unseen mode or regime behavior;
- load balance and cost; distinguish total parameters, per-input active parameters, resident model memory, and measured peak runtime memory;
- measured sparse-execution benefit on the stated software/hardware; sparse activation alone does not establish latency or memory savings. When efficiency is claimed, compare relevant small dense or distilled alternatives under the declared budget;
- expert specialization interpretation.

Start from what is mixed: features, predictions or parameters, and for which task. P36 uses task-specific gates to mix expert features for several quality targets; its balancing mechanism adjusts task gradients during training. This is not evidence of top-k sparse execution, load balancing across devices, or uniformly distributed expert use. Dense weighted mixtures and sparse routing have different computation boundaries. When reduced negative transfer is claimed, compare task-wise outcomes with relevant single-task and shared-model alternatives; an improved aggregate can conceal harm to one quality target. Keep gradient weighting, expert routing and class-frequency reweighting separate, and define any combined score across targets with different units.

## 12. Compound, Concurrent, Hierarchical, Or Open-Set Fault States

Writing priorities:

- define whether multiple faults occur simultaneously, sequentially, hierarchically, or as an unknown class;
- distinguish composite labels from genuinely interacting fault mechanisms;
- describe label construction, temporal overlap, and ambiguity explicitly;
- avoid claiming root cause or fault interaction from a multi-label classifier alone.

Evidence priorities:

- single-fault, compound-fault, and normal-condition separation;
- held-out combinations or unknown-fault evaluation when claimed;
- multi-label metrics, class-wise recall, false alarm, and detection delay as appropriate;
- overlap-severity and fault-order analysis;
- mechanism or expert checks for claimed fault interactions.

An unseen combination of known fault types, an unknown fault type, and a known fault under a new operating condition are three different tests. Use multi-label, composite-class or open-set metrics according to the defined output. Generating combinations of signals does not establish that the corresponding faults physically co-occur or interact in production.

Read local label spaces before transferring terms such as `OOD` or `unknown`. In P37, a pairwise base classifier has an outside-pair class, and its partial predictions are fused into subsystem fault decisions. Such a local rejection class does not itself establish system-wide novelty detection. State whether compound examples are absent, scarce or fully available in training; a small nonzero compound set is not zero-shot. If an alarm gates subsequent identification, distinguish conditional identification results from end-to-end performance that includes missed alarms. Also verify the data generator: P37's industrial estate motivates a simulation system, not a claim that all evaluated measurements were collected during real production faults.

P39 provides a related machinery example: fault indicators allow simultaneous positives, while the base classifiers operate on partial pairwise label spaces and use a small compound-fault training subset. Keep the output's co-occurrence semantics separate from the classifier decomposition and annotation availability. A contribution about combining partial decisions need not be rewritten as resolving uncertain training labels.

## 13. Dynamic, Multiscale, Slow-Feature, Or Time-Frequency Representation

Writing priorities:

- derive relevant time scales, dynamics, or frequency bands from process behavior or sensing physics;
- distinguish slow operating evolution, transient response, periodic structure, and measurement noise;
- explain why a representation is needed before naming its encoder or transform;
- avoid generic `local/global feature` language when no engineering scale is defined.

Evidence priorities:

- static-versus-dynamic and time-versus-frequency comparisons;
- scale, lag, window, or retained-band sensitivity grounded in the process;
- controlled removal or replacement of each representation branch;
- transient, steady-state, and mode-specific analysis when relevant;
- efficiency analysis if the representation is claimed to be lightweight.

Verify that the modeled axis is acquisition time before interpreting trends, lags or frequencies physically. Stacking unrelated product samples or repeating a static vector does not supply a temporal trajectory. For multiscale or local/global descriptions, identify whether scale means time window, frequency band, graph neighborhood or production hierarchy. Convolutional feature channels need not correspond to the original process variables (P11). Describe training regularizers separately from prediction-time branches rather than making the abstract list every loss as another representation module.

Slow variation alone does not establish quality relevance. P34 distinguishes a quality-related latent component from an auxiliary component that helps recover information under multirate observation; its measurement and target equations define their roles. Explain what supervision or constraint relates a representation to quality, rather than relabeling every slow feature as a quality feature. An auxiliary component need not be useless or removable merely because it has no direct target link. Keep a moving-average trend, a slow-feature objective and a latent state-space model distinct.

## 14. Control, Optimization, Scheduling, And Human-AI Decision

Writing priorities:

- define the controlled/optimized variables, constraints, objective, horizon, and decision frequency;
- connect prediction error to operational consequence;
- distinguish advisory, shadow-mode, and closed-loop use;
- include safety, feasibility, and operator authority.

Evidence priorities:

- closed-loop, simulation, HIL, or prospective decision evaluation as appropriate;
- constraint violations, stability, economic/quality objectives, and robustness;
- latency and update frequency;
- human acceptance, override, or decision-quality measures for collaborative systems.
