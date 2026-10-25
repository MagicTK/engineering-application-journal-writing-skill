# Topic Playbooks For Data-Driven Industrial AI Papers

## Purpose

Load only the playbook matching the manuscript's actual challenge and method. These are conditional supplements to the general engineering narrative, not mandatory themes.

Evidence lists are menus, not a requirement to run every test. Select a test because it can distinguish the stated claim from a plausible alternative. A multi-rate soft sensor, a zero-shot classifier and a weakly labeled detector need different targets, splits and metrics even when all use neural networks. Source IDs below refer to [published passages and transfer boundaries](published-evidence.md); they support scoped examples, not universal prescriptions.

Names in these guides are scoped examples or routing labels, not an already
certified glossary. Apply the [name-admission and Chinese-translation procedure](engineering-application-terminology-bank.md#0-admit-names-not-search-counts)
before promoting a mechanism to a shared recommendation. A single source can
support its own clearly attributed module, not a general method family; describe
the verified operation when a broader name has not been established.

## Contents

Observation and sampling; scarce supervision; multimode/nonstationary operation; multisource/multimodal data; plant-wide and multistage systems; graph/knowledge/causal/fuzzy models; generation and diffusion; LLMs; efficiency and edge use; interpretability and root cause; mixture of experts; compound/open-set faults; dynamic and time-frequency representations; control and decision systems.

## 1. Incomplete, Asynchronous, Or Multi-Rate Observation

Identify the per-stream observation schedule, cross-stream timing, missing entries and measurement-release delay. These properties can coexist: streams with different fixed periods need not share timestamps, while a multirate study may also contain irregular observations. State the actual setting rather than forcing mutually exclusive categories.

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

Choose the narrative from the observation mechanism. P08/P73 define rate-dependent groups and available observations, while P24 distinguishes sequence position from measured time intervals. Explain how those particular observations or timing quantities enter the predictor: an observed-subset equation, a timing-conditioned representation and an estimated completed grid are different interfaces. Verify frequency/period units and offsets before calling streams aligned. For delayed quality assays, distinguish the time represented by a label from its release time. `Offline assay` can accurately describe laboratory measurement even when `offline dataset` adds nothing to provenance.

Turn acquisition facts into the specific estimation requirement. A complete-observation comparator may discard useful measurements between shared observation times; a model that uses an observed-subset likelihood should explain how those measurements enter estimation. This is a different route from constructing a completed input grid, aligning rate-dependent representations, or learning with sparse quality targets. Name the route actually implemented and the intermediate object it supplies to the output. Do not add an imputation stage merely because some variables are unobserved. P08 develops representation alignment from a granularity question; P17 develops semisupervised regression from assay scarcity; P34 defines separate measurement and quality equations under multirate acquisition. These are alternative argument structures, not interchangeable remedies or evidence of complete information recovery.

If completion and prediction are coupled, trace the completed measurements, their encoded representations and the final quality/fault output separately (P25, P33). In an abstract or contribution, connect the operation to its recipient: estimated missing measurements may supply a predictor, while a reconstruction loss may constrain a shared encoder during training (P17). Preserve the actual parallel or sequential structure; a decoder, padding value or aligned latent vector does not by itself establish an imputation output. If a numerical placeholder is excluded by a mask, describe that role rather than calling it a recovered measurement.

Distinguish the acquisition mask from additional entries deliberately hidden during learning or evaluation, and from the positions included in each loss. State whether the reconstruction target is the original observation, a corrupted input or another defined quantity. Observed input values can provide reconstruction targets even when quality labels are scarce; those two kinds of supervision are not interchangeable. Follow the [missing-value evidence check](experiment-evidence-design.md#6-robustness-design) before claiming recovery accuracy. If the target is causal structure (P08), structure-recovery assumptions and evidence take priority over a generic diagnosis comparison. Do not invent a universal minimum number of rates from one paper's definition.

Also distinguish acquisition from augmentation. P26 deliberately transforms time sampling to create a self-supervised target; its title alone does not establish naturally irregular industrial acquisition. Describe a synthetic sampling transformation as a learning operation unless the data provenance independently establishes an irregular observation process.

## 2. Scarce Labels, Few-Shot, Zero-Shot, Weak, Or Self-Supervised Learning

When the request is only to classify industrial problems, start with the
[annotation profile and supervision/signal boundaries](problem-first-classification.md#3-supervision-information-and-training-signals),
not a candidate training method or experiment plan. These are overlapping
descriptions of information and learning, not one exclusive ladder. For example,
self-supervised targets can be used within a semi-supervised quality predictor;
weak supervision may include incomplete labels under a stated broad convention.
Proceed to the writing/evaluation choices below only when that scope is requested.

Writing priorities:

- define exactly which classes, conditions, samples, or label levels are unavailable;
- separate semantic transfer, representation pretraining, pseudo-labeling, and sample generation;
- state what target-domain or unseen-class information is accessible during training and tuning;
- tie the challenge to industrial annotation cost, safety, rarity, or emergence of new faults.

Branch by the actual supervision arrangement:

| Setting | Essential writing distinction | Claim-matched evaluation |
|---|---|---|
| Few-shot classification | What counts as a shot, which classes are known, and whether support/query episodes or a fixed split are used | The declared label budgets and sampling variability; do not impose episodic evaluation on a non-episodic design |
| Zero-shot diagnosis | Which fault classes lack labeled real training measurements; where their semantics come from; whether generated features or unlabeled unseen-class measurements enter learning/adaptation | Verify the acquired-training class split and semantic source, not merely class IDs appearing in a loss; use seen/unseen balance or harmonic metrics for the declared joint-class evaluation, not automatically for unseen-only testing |
| Semisupervised classification | Which samples are labeled, how unlabeled data affect learning, and whether source and target distributions differ | Matched label budgets and unlabeled-data controls; separate class-prior imbalance from feature-distribution shift |
| Semisupervised regression/soft sensing | Which quality targets are observed and how unlabeled process measurements constrain the predictor | Regression error in the target's units, label-budget sensitivity and a relevant supervised control; no seen/unseen class metric without classes |
| Active annotation acquisition | Which samples or targets can be requested, from which pool/stream, at what cost and before which learner update | Match initial labeled resources and acquisition budgets; keep labels reserved for final evaluation separate and distinguish simulated label revelation from measured human effort |
| Weak segment/bag labels | The labeled unit and claimed prediction unit; distinguish bag classification from an explicitly defined finer-output mechanism | Evaluate at the claimed granularity; bag accuracy alone does not validate point localization, and a bag-only task need not invent point outputs |
| Candidate-label ambiguity | Whether one true label lies in a supplied candidate set, and how alternatives are resolved | Evaluate against independently established target labels; a candidate set is not a statement that all listed faults coexist |
| Inaccurate labels or targets | Which annotations or assay values may be wrong, how this was established, and what the learning mechanism changes | Distinguish sensor corruption from target corruption; performance against an uncertain reference alone does not establish accuracy against the true physical target |
| Self-supervised learning | How targets are constructed, what augmentation preserves physically, and whether the auxiliary objective is trained jointly with the task or in a separate phase | Relevant objective/path controls and downstream evaluation; preserve the actual training schedule and do not imply that no labels are used anywhere |
| Unsupervised clustering | Which object is clustered, how the number of clusters is determined, and how clusters are related to fault identities | Clustering quality and the declared evaluation-only label matching; do not conceal labels used for model selection or imply cluster indices already identify faults |

P05-P06 exemplify semantic transfer; P17 uses labeled and unlabeled measurements for concentration prediction; P21 couples self-supervised and diagnostic learning; P22 learns from segment labels for point-level detection. Their method names do not make these supervision arrangements interchangeable. P18 adds long-tailed classes and cross-domain information, in an adjacent equipment setting.

If class-frequency imbalance is central, distinguish the learning response from
the evaluation average. A class-dependent loss factor, altered sampling
probabilities and generated minority examples act at different points. P92's
generation-seed weights, P93's weighted fitting residuals and P94's
augmentation-prototype selection illustrate why a shared weight word does not
identify the operation. State what changes the training distribution or
objective, how it trains the retained classifier and which decision is used for
new measurements. A larger weighted F1 can coexist with worse minority or macro
performance. Select class-wise/macro or application-cost evidence when those
benefits are claimed, rather than renaming an aggregate gain as balanced
diagnosis. Record train/evaluation class counts and matched sampling/weighting
controls; multiple balancing operations can be legitimate, but their combination
defines a different objective. This conditional route does not turn ordinary
class weighting into a novel contribution or make imbalance every paper's
headline. See [weight roles](terminology-decisions.md#weight-roles-and-class-decisions).

Distinguish outer loss factors from training-logit offsets and later score
adjustments. P18 uses prior-dependent logits for training and a separate
pseudo-label construction; P96 combines a class factor with a margin. Neither
design is described faithfully by moving every balancing operation into a final
prediction gate. A source's proposed loss and its background definition are also
different passages, and P97's algorithm/equation conflict needs implementation
evidence before either can be treated as its definitive training rule.

For zero-shot diagnosis, trace how semantic knowledge reaches the final decision.
P05/P06 map measurements toward class-semantic descriptions, whereas P80 uses
descriptions to generate unseen-class features before fitting a diagnostic
classifier. Its attribute classifier also supplies a hidden representation for
the final feature transformation; do not assume every generator-side component
is discarded. These are different semantic-to-predictor relationships, not a
mandatory final fusion of text and sensor features. Labeled generated vectors
can support zero-shot learning without supplying new real fault acquisitions.
State the actual retained computation, semantic provenance and allowed target
access. P05's selected target predictions adjust semantic references; full-batch
unlabeled access is not a purely inductive comparison merely because weights stay
fixed. Use the [base-name record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope)
without transferring full FHZSL/ACGAN-FG/test-time-adjustment names as generic families.

These labels need not be mutually exclusive. Semisupervised learning describes the use of labeled and unlabeled examples for the task; self-supervision describes how an auxiliary learning signal is constructed. P21 jointly trains diagnostic and self-generated temporal objectives, while P26 shares an encoder between class prediction and sampling-transformation prediction. Neither requires an invented pretraining/fine-tuning sequence. Conversely, adding a self-supervised objective to fully labeled task data does not by itself establish a semisupervised setting. In the abstract or contribution, connect the auxiliary target to the shared representation and task output rather than listing the two learning names. If both appear, do not use `SSL` ambiguously for both.

For weak supervision, name the actual limitation instead of assuming coarse labels or annotation noise. P22 pp.3-4 trains with segment labels for point predictions; P25 pp.2,4-5 uses its weakly-supervised name for completed auxiliary measurements with sparse quality targets and model-derived guidance. Preserve those source-specific meanings without treating them as one shared operator, importing bags into regression or renaming every semisupervised model. A self-generated transformation label or pseudo-target is a training signal, not an additional independently measured fault/quality annotation; report those counts separately when discussing annotation savings. See the [base-name records](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

For contrastive learning, name the contrasted objects and how their training relation is constructed. P20 contrasts graph representations, whereas P21 contrasts temporal contexts and later latent features across views. A positive pair need not mean normal operation, and a negative pair need not contain a different fault class. Verified class labels can legitimately define supervised contrastive pairs; preserve that setting when implemented. Temporal separation or a distribution-distance rule alone does not prove statistical independence. Check whether an augmentation preserves the diagnostic property before claiming fault invariance, particularly when amplitude or timing carries the fault signature.

Trace generated class guidance to its actual consumer: P18 uses adjusted predictions as hard training targets; P21 uses soft class distributions to guide relationships between training samples. Such a sample graph is not a graph of sensors or physical production links. P21's later-feature prediction is a training objective, and only its encoder/classifier are used for diagnosis at test time. Do not recast that pretext task as physical forecasting or future-measurement access during diagnosis. These distinctions belong in the method; an abstract needs only the connection central to the claimed advance. Use the [paired terminology records](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) for the base names, not as permission to borrow complete source-specific module names.

中文核查重点：对比对象及配对依据、伪标签的硬/软形式和实际使用者、样本图与物理变量图、训练任务与预测输出分别核对。正负配对不自动是正常/故障分类；真实类别指导的有监督配对可以成立。增强是否保留故障特征需依据，不将这些内部核查逐项塞进摘要。

When a few-shot method uses class prototypes, connect the support features, prototype construction and query-scoring operation. P47 computes support-feature means and uses a learned matching function; the mean construction is not itself a newly invented physical-state estimator. A prototype can be derived from a trained embedding without being an independently optimized parameter. Do not impose this mean construction on a method that defines exemplars, multiple representatives or another estimator. Put the actual advance in the contribution, not every standard constituent of this chain.

For episodic learning, distinguish labeled queries used to train the model from held-out queries whose labels are unavailable to prediction. The former is not automatically test-label leakage. Independently defined validation episodes can use their query labels for model selection when that partition was actually performed; retrospective renaming of selected final queries does not create independent evaluation. Conversely, calling a sample a `query` does not establish its permitted use: state the training/validation/evaluation phase, the support/query roles and any allowed test-time adaptation. Verify class overlap separately from sample disjointness; few-shot does not by itself guarantee previously unseen classes. P47's formulation permits partial overlap or disjoint base/support classes, so its name cannot substitute for the actual split definition.

Scope the label budget to its stage. P47 uses abundant labeled base data before limited support examples, whereas P69 pp.2-3,8-9 uses a small fixed training set with augmentation rather than an episodic support/query design. Both use `few-shot learning`; this establishes a shared limited-example setting, not one mandatory algorithm or a universal numerical cutoff. Report available source/base annotations, current-task labels and generated training views separately. Reusing a label over many episodes or augmentations does not create new independent annotations. A small support budget can substantiate adaptation with few current-task labels, but total annotation savings require a comparison that accounts for the relevant earlier labeling resources as well. Keep the abstract's scope accurate and develop the full accounting in the settings; do not turn every contribution into a resource disclaimer.

For active learning, trace the acquisition cycle separately from final prediction.
P89/P91 select machinery samples for expert annotation and subsequent classifier
updates; P90 defines an analogous pool-based cycle for chemical-process fault
classification. P89/P91 share a research line. These support the base operation,
not one query criterion, budget unit, classifier or requirement to discover new
classes. Identify the current learner, requested target, available pool/stream,
label provider, stopping rule and retained predictor. A fixed-pool benchmark can
validly reveal cached ground-truth labels for selected training samples, but this
does not measure human annotation time. In a stream, specify when feedback is
available relative to each evaluated decision. Do not infer annotation requests
from an active-diagnosis title when the specified action is physical excitation.
中文：查询训练标注、训练episode的query监督及最终评价标签分别核对；实际选择策略与更新后的预测器要衔接，不强加伪标签或新类发现。

中文核查重点：类原型的来源及后续用途、训练查询与测试查询的标签边界、样本划分与类别划分分别交代；不把类代表写成物理工况，也不要求所有小样本方法都采用均值原型或分任务训练。分别报告基础/源数据、当前任务标注与增强视图；当前任务的少量支持样本不代表整个研究只使用这些标注，也不使合法的历史标注学习成为泄漏。

For an interval/window-to-point claim, trace the actual output rather than broadcasting the training label. P22 defines a point-scoring mechanism and evaluates its point outputs without point adjustment. A different model that only classifies windows should retain that output scope. The [continuous-monitoring metric guidance](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when) separates window classification, point scores, interval adjustment, event detection and alarm timing; none is a substitute for another merely because the reported metric is called F1.

For multi-instance learning, define the bag, its members and the prediction unit before naming the supervision setting. P22 pp.3-4 treats a time series as a bag and extends point instances to subsequences of different lengths. P68 pp.3-5 defines bags formally, then constructs latent feature instances and aggregates class-related scores. These members are not automatically separate acquired samples or raw temporal regions. Report production-unit/bag counts separately from internal instance counts; preserve the grouping unit when evaluating generalization. In an abstract or contribution, connect instance construction to the actual aggregation and output, rather than treating `multi-instance` as a synonym for more labeled data.

Choose the instance semantics for the industrial phenomenon. A collective anomaly can require a temporal pattern even when individual measurements lie in their usual ranges; do not require every positive bag to contain a point that is individually distinguishable as anomalous, or require P22's particular tree architecture. For a bag-only classifier, instance-localization evidence is needed only if localization is claimed. Likewise, a paper's complete `multi-instance multilabel` name does not establish simultaneous physical faults: P68's inspected experiments evaluate seven bearing states, and its full name alone does not verify a multilabel or compound-fault decision rule. Retain attributed names and describe the supported output; do not automatically rename the source or import its particular pooling/metric formulas.

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

For **domain generalization**, make the unobserved-condition requirement lead to
the actual source-side learning operation, then to the predictor retained for
new measurements (P50/P99). State which domains supply training and model
selection; do not infer an available validation split or impose another paper's
source count. Source-statistic perturbations and same-label feature swapping
are different attributed responses, not a required common DG module. A
within-window input transform may remain fixed while its numerical result
depends on the input. Fitting stored statistics from a whole target pool changes
that profile, even without gradient updates; report a legitimate target-adaptive
variant separately. Keep the evidence boundary in settings and the actual
mechanism-to-prediction relation in the abstract. Use the
[scoped setting record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope)
without turning an invariance objective into physical causal identification.

Check **label-space relations and label availability separately**. P10 uses identical source/target class spaces with unlabeled target measurements, whereas P44 addresses a target class subset and its training equations include target-label symbols. Neither assumption transfers automatically to another adaptation paper. If a target label enters a loss, identify whether it is observed, inferred or evaluation-only before assigning a supervision category; a pseudolabel is not a measured annotation. Domain adaptation is broader than unsupervised adaptation. In a multisource design, distinguish distribution alignment during fitting from a separate weighted combination of classifier predictions; the two may coexist without any source/target feature fusion at inference.

When historical measurements cannot be provided for target adaptation, describe
what the source-trained model supplies and how target measurements use that
knowledge. P78 updates selected encoder/classifier parameters, while P79 keeps its
classifier weights as class references and updates its encoder. The common
source-free constraint is adaptation-stage data access, not one fixed update
architecture. In the abstract and overview, connect the model handoff, actual
target-derived guidance and retained diagnostic predictor. A loss with
`supervised` in its attributed name may use inferred target labels; follow their
origin before classifying the study. P79's separate unknown-class decision is
part of its declared label-space setting, not a capability supplied by the base
source-free name. Use the [definition record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope)
and [data/phase distinctions](terminology-decisions.md#state-condition-and-mode)
without making these requirements the default story for ordinary classification.

Name the aligned populations and criterion. A lower marginal discrepancy alone cannot establish class correspondence or target diagnostic accuracy; legitimate class-conditional alignment should retain its class guidance and access conditions. Evaluate the claimed prediction benefit separately from the internal alignment statistic, with class-level analysis when label-space mismatch is central. The [alignment distinctions](terminology-decisions.md#alignment-state-the-object-and-criterion) also prevent confusing domain matching with acquisition synchronization or mutual-information estimation.

Check whether adaptation actually concerns learned parameters. Input-dependent routing can respond to a new window with frozen parameters; a recurrent state or rolling score reference may change without retraining. These mechanisms can be described as adaptive at their defined level, but they do not alone constitute continual learning. P24 conditions temporal weighting on observed intervals, whereas P04 defines a rolling statistical score after reconstruction. Keep the changing object consistent from contribution to Methods and evaluation; do not add an online-learning experiment to a paper that claims only input-conditioned weighting.

Select chronological, mode-held-out, cross-period or cross-site evaluation according to the claimed shift. When drift and class proportions both change, distinguish their effects rather than attributing all change to a generic domain gap.

Trace adaptation at its actual granularity. P63 separates an evolving subspace/classifier from out-of-sample prediction and conditions classifier learning on revealed labels. P64 assumes operator-known mode switches for model updates and separately adapts an alarm threshold; its online wording does not establish automatic switch discovery. P05's test-time operation pools selected unlabeled predictions to adjust semantic references without another network forward/backward pass. State whether a current sample, a past window or the full target batch supplies an update, and whether the resulting state persists or resets between cases. Use that information in the method overview and the [adaptive evaluation check](experiment-evidence-design.md#adaptive-state-feedback-and-retention) when adaptation is a central claim.

Write initial target-side fitting separately from evaluation-time adaptation.
Specify the data used by each component's input, loss and changing statistics;
control-only forward inputs do not establish sensor-free fitting. Known-healthy
calibration and absent fault-type labels are also different resource statements.
Use the [scoped test-time record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope)
without treating all adaptive forward calculations as learning or every current
batch as illegal access. The actual decision time determines the allowed horizon.

For retention or replay claims, identify what remains accessible. P64 caches historical latent features and constrains parameter changes; P65 avoids replay of previous target-domain instances while continuing to use labeled source-domain samples and an earlier model. Neither example establishes a requirement to store raw data, a universal source-free setting or a privacy guarantee. Explain the retained information and its role in the next update, then assess earlier as well as current conditions if retaining earlier capability is claimed. Shared labels across changing domains are compatible with continual learning; new fault classes require a separate class-incremental definition.

Name the distribution that changes, not just `concept drift`. P30 defines a change in `P(X|Y)` while keeping class priors fixed; other work may use drift terminology for `P(Y|X)`, `P(X)` or `P(Y)`. Preserve the manuscript's equations and assumptions rather than transferring a name alone. Do not equate every observed prediction error with a detected drift event.

For adaptive models, state **what triggers which update, using what available information**. P27 triggers learning strategies from error-related events; this does not establish event-triggered sensor sampling or a fault alarm. If the trigger uses a true quality target, explain when that target becomes available. If adaptation is the advance, distinguish prediction before feedback from performance after the update; select recovery delay, update cost or retained performance only as needed for that claim.

## 4. Multisource, Multimodal, Or Cross-Modal Industrial Evidence

First resolve what source denotes: operating-domain datasets, separately
acquired input streams or derived views. For domain-transfer questions use
Section 3; for actual acquisition/representation interactions use this section,
or combine both when justified. A multisource title alone does not require
synchronizing unrelated condition datasets or adding sensor-modality tests.
See [source roles](terminology-decisions.md#source-roles-and-representation-provenance).

中文：先辨来源角色再选方向与评价，不把多个工况域默认写成多种同步传感输入；父样本及其派生表示不重复算独立采集。

Writing priorities:

- trace each source from physical event to sensor response and sample unit;
- explain synchronization, alignment, and information timing;
- distinguish complementary evidence from duplicated inputs;
- make the fusion mechanism answer a concrete heterogeneity or reliability issue.

Evidence priorities:

- single-source and fusion comparisons; for numerical-to-image same-source views, select numerical-only, visual-only, fusion, and a simple image-model control as needed to isolate representation or pretrained-backbone claims;
- missing/corrupted modality tests relevant to the claimed availability or disturbance robustness;
- alignment perturbation;
- modality contribution and failure cases;
- localization or decision evidence when the application requires it.

Distinguish acquisition alignment, representation compatibility and learned interaction. P38 synchronizes video/current acquisition, maps their different input shapes into compatible token dimensions, and learns directional cross-modal interactions. Equal embedding widths alone do not establish temporal pairing or one-to-one correspondence. State which modality queries which information when this affects the output, without assuming the paper's arrow convention is universal. Separate class-level decisions from pixel-level localization and match each to its annotation and evaluation; reconstructing a prediction map is not necessarily reconstructing the original measurements. Two derived views of the same signal should not be presented as independently acquired modalities.

Classify attention from its inputs, not `cross` in a title. P42 applies self-attention along time and variable axes; P43 instead derives queries from one encoder scale and keys/values from concatenated scales of the same image. Cross-attention can therefore operate within one modality. Identify the query representation, the key/value representation and the aggregation axis when defining it; do not force that detail into every abstract. A published architecture's name remains an attributed identity even when its components need a more precise description.

中文写作也要区分“跨时间/跨变量的自注意力”和“交叉注意力”。依据查询、键、值的来源判断，不因出现 cross 就换成另一种机制，也不要求交叉注意力必须跨模态。

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

For hypergraphs, establish the node identity and hyperedge membership before
describing higher-order relations. Node-to-hyperedge-to-node propagation can
use sample-neighborhood groups (P96) or equipment relations (P105); these do
not imply the same physical object. Trace fixed membership, fitted weights and
changing features separately. A per-batch construction rule may change the
structure without online parameter learning. Connect propagation to the actual
node-level or graph-level decision, and select
[structure/access checks](experiment-evidence-design.md#hypergraph-structure-and-access)
only when relevant to the claim. No universal hypergraph advantage follows
from losing set information in an unweighted pairwise projection.

中文：先定节点、超边及输出对象；固定归属、学习权重和依输入变化分别写，不把样本邻域说成物理变量关联，也不把批次重建自动写成在线学习。

Writing priorities:

- state the source of every graph, rule, membership function, or knowledge constraint;
- separate known structure, expert input, learned relation, and causal assumption;
- distinguish a physical causal claim from a defined computational term such as causal convolution; match assumptions and evidence to the intended claim;
- use fuzzy terminology for actual membership/rule mechanisms, not as a decorative synonym for uncertainty.

Make the knowledge entry point explicit: data organization, graph edge/bias, loss term, hard constraint, decision rule, or inference-time correction. These choices have different consequences. P04 uses process structure in representation learning; P12 uses expert rules in decision-space design. Do not reduce both to an unexplained `knowledge-feature fusion` operation.

Check knowledge provenance separately from its name. In P12, variable-wise class statistics construct the expert support, abstention and rejection regions; `expert system` does not mean that every quantity was supplied independently by a human expert. Describe which rules are specified, which quantities are estimated from labeled measurements, and which partition supplies those measurements. P14 uses process-informed subgraphs and prediction-trained adjacency. A given physical partition, learned edge weights and a decision-level support vector are not interchangeable priors.

For a knowledge-based contribution, connect the known fact to its actual recipient:

| Implemented form | Connection to explain | Claim boundary |
|---|---|---|
| Process-based architecture or input organization | Which connections, groups or delays follow the process description, and what remains learned? P57 uses subprocess structure in network construction. | A structural correspondence is not automatically a solved physical equation. |
| Distribution over an uncertain object | Which graph/parameter is random, how prior information enters its distribution, and how permitted observations update it? P56 makes uncertain graph knowledge explicit. | A normalized matrix alone does not establish a distribution over matrices or a Bayesian update. |
| Additional training penalty | Which measured quantity, output or latent relation is penalized, and how does that shape the predictor? P58 operates on latent pair distances. | Penalizing deviations does not by itself enforce exact satisfaction. Latent distances are not physical balance residuals without a justified mapping. |
| Construction or constrained computation | Which specified relation is satisfied, over which output/domain, under what assumptions and numerical tolerance? | Preserve a verified guarantee for that relation; do not extend it to all process laws or operating conditions. |

These are operational distinctions, not four interchangeable module families. Keep a source's complete proposed name attributed. In an abstract or contribution, write the connection positively, for example, `A balance-residual penalty couples the predictor to the process model during training`, only when that is the implemented operation. Put unresolved source-equation differences in the author notes, not a succession of disclaimers in the manuscript. A source's use of `ensure` or `physics-informed` is not a substitute for checking its equations and the represented physical quantities. Name a supported mechanism and its tested effect instead of making every knowledge-guided design a physics-informed neural network.

The [checked PINN base category](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) includes algebraic physical constraints and hard-constrained variants; do not require every valid instance to solve a PDE through a residual loss. Conversely, an industrial adjacency or generic embedding regularizer does not establish that category by itself. State the actual relation before selecting the label.

When a constraint operation is central, distinguish a layer used in the training loss and differentiation path from correction applied only after training. P59 Section 3.2, Remark 3, explicitly separates these. A nontrainable layer can still affect learned parameters through its gradients. Write the causal connection positively, for example, `The predictor is trained through a differentiable constraint layer, so parameter updates account for the corrected outputs.` Use this only when the implementation follows that path; a detached correction needs a different description. Preserve the requested contribution scope rather than adding all these checks to its wording.

中文同样区分“工艺知识决定连接”“先验分布描述不确定对象”“损失项惩罚偏离”和“构造满足指定约束”。先把作用写准确，再选择名称；确有保证则保留其明确范围，不为了谨慎而一律降成“可能有帮助”。PINN不限于PDE损失，固定参数的约束层也可能通过梯度影响训练，不能直接称为训练后修正。只有命名或保证性主张涉及这些区别时才展开，不给普通语言润色额外安排物理建模任务。

For a causal claim, name the target (for example a directed dependence structure, an intervention effect or a root-cause ranking), its assumptions and the evidence available. Good diagnostic accuracy does not establish any of these by itself. An expert-consistent graph can support engineering plausibility without proving causal identification.

Do not make real-world intervention experiments a universal naming requirement. A specified observational identification argument can justify a conditional causal interpretation; it does not automatically validate the assumed graph in a plant. Keep population-level intervention effects, event-specific origins and predictive relationships distinct. For a mechanism that attacks nodes in a learned graph, describe the modeled operation before interpreting it as a physical experiment. The [interpretation check](experiment-evidence-design.md#7-interpretation-design) preserves valid observational and intervention-based routes without equating them.

A causal temporal convolution concerns past-versus-future information access; a predictive adjacency is a learned relationship; physical causal identification needs additional assumptions and evidence. P14 provides a useful place to inspect these distinct roles, not a license to equate them. Check the complete computation before using `hard exclusion`, `sparse` or `independent`: logit reweighting followed by softmax is not automatically class exclusion, and a block-diagonal adjacency does not prevent a later dense layer from combining groups. Resolve equation, pseudocode and implementation differences in author notes before strengthening the prose.

For fuzzy models, define the membership domain and the quantity passed to the
next operation. In the checked normalized-rule predictors, input matches form
rule activations that weight numerical outputs; P27 uses them for quality
regression, whereas P77 combines class scores before a class-axis softmax.
Rules need not correspond to fault classes, and numerical rule weights are not
the final class probabilities. Other inference architectures need their own
definitions. P07 instead uses fuzzy states to construct temporal relationships
and training constraints. Select evidence for the claimed role: rule effects,
membership sensitivity or the actual prediction decision. Probability calibration
is relevant when an output is interpreted probabilistically, not a compulsory
test for every fuzzy membership. See the
[quantity and operator-order check](terminology-decisions.md#fuzzy-rule-outputs).

For a TSK-named design, use the [scoped rule-definition record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope), not Gaussian shape alone. Connect local numerical models to their input-dependent rule combination and task output. Specify whether linearity concerns local inputs, scores as functions of consequent coefficients with fixed antecedents, or the complete predictor before using it as a contribution. A numerical model can remain nonlinear overall and need not assign each rule a physical mode; retain a documented physical interpretation when the inputs and rules actually support it.

中文：局部后件、固定前件时分数对后件系数的关系和完整预测器三个层次分别判断，不由局部线性推断全模型线性，不把数值规则默认翻译成实体工况。

Trace what an uncertainty-related quantity represents and where it acts. P49 pp.5-6 weights learned responses at feature positions; its specified weighted sum is not the formal Dempster combination discussed in its preliminaries. P50 pp.3-4 models variation in feature statistics to generate perturbed training features. Neither operation alone supplies a sample's probability of being correctly diagnosed. In contrast, P52 pp.2-3 connects class evidence, a Dirichlet distribution and a sample-level uncertainty output. These are attributed examples of different roles, not interchangeable modules or a completed general admission record for every evidential-learning name.

Write the actual connection positively: when implemented, `Input-dependent weights combine the learned responses into features used by the diagnostic classifier.` If a separate score controls rejection, describe that subsequent decision instead of hiding it inside `reliable fusion`. State a demonstrated effect in the results; normalization, a loss named calibrated, or a paper title containing trustworthy does not by itself establish empirical probability calibration. Follow [the score-to-decision evidence check](experiment-evidence-design.md#scores-probabilities-and-rejection-decisions) only when the manuscript makes that claim.

For the checked Dirichlet class-evidence formulation (P52/P75), connect the encoder to the evidence head, then distinguish the expected class probabilities from the uncertainty quantity and its actual use. The same head can supply these different outputs; they need not form a serial feature-fusion pipeline. See [the quantity definitions](terminology-decisions.md#evidential-classification-quantities). A smaller reported uncertainty is not itself an observed diagnostic improvement. Locate any advance in the particular learning/decision design and evidence, not merely the use of this existing base method. Other priors, regression outputs and evidence-combination rules need their own definitions.

For actual mass-function combination, preserve the map from encoded evidence to
mass construction, any source weighting, the combination operator and the final
decision. P49/P84 supply a scoped base-rule definition record, not proof that
every network named evidence fusion implements it. Distinct heads do not prove
source independence. Define total-conflict behavior when relevant and distinguish
uncommitted mass from a new unknown-fault class. See
[the combination check](terminology-decisions.md#combining-belief-masses).

中文也应先交代量的对象和用途：用于特征加权、构造训练扰动、描述类别分布，还是控制最终拒识。它们可以共同服务诊断，但不能只因都与“不确定性”有关就写成同一类机制。实际合成质量函数时，连清编码证据、质量构造、源加权、合成操作及最终决策，P49/P84只支持限定基础规则。不同头不证明独立，未分配质量也不直接新增未知故障类别。方法段写清实际操作，实验段再报告已检验的作用，不必为普通分类器额外虚构拒识或校准任务。

Do not treat all fuzzy mechanisms as a rule base. P27 places fuzzy prediction
after deep feature extraction, P28 uses fuzzy clustering to reinforce reservoir
features, and P33 couples clustering with imputation. P77's fuzzy decisions also
guide a deep branch through a training objective, a different relationship from
concatenating their outputs. Identify the represented input region, temporal
state, cluster or rule and its actual consumer. A rule learned on embeddings can
serve numerical prediction without having a verified linguistic or physical
interpretation. Preserve a documented readable rule base when the inputs and
rule meanings support it; specify what can be explained and to whom rather than
awarding or rejecting interpretability from the word `fuzzy` alone.

Treat source-specific uses of `reinforcement` by their defined operation. P28 p.3 uses fuzzy clustering and center-related targets for feature fitting; that name is not evidence of reinforcement learning. Describe the actual objective and information flow. Only use the reinforcement-learning category when the study implements the corresponding learning setup, rather than inferring it from this word alone.

Choose removed/randomized/corrupted-prior controls when they isolate the knowledge claim. Preserve constraints that define a valid process when constructing a perturbation; a physically impossible random graph can be a stress test but not a realistic operating alternative.

## 7. Reconstruction-Based, Generative, Diffusion, Or Data-Augmentation Methods

For missing-value imputation, identify the measurement entries being estimated
and whether completion is the main output or an input to another predictor.
P106/P107 add two industrial measurement contexts to the existing P25/P33
record, not one universal architecture. Separate prefill, model estimates,
candidate iteration and parameter learning; preserve declared frozen or
transductive fitting rather than assigning all methods the same test interface.
Follow the [mask/target distinction](terminology-decisions.md#imputation-masks-and-training-targets)
for training and evaluation references, and the existing missing-value evidence
check for recovery versus downstream utility. Do not import a source's complete
median-filled or masked-completion name as a general module.

中文：插补本身为任务还是给下游预测器供输入须分清；预填、候选迭代与参数拟合不是同一操作。真实未知位置没有实测参照，训练遮挡目标和评价留出参照也不互换。

Writing priorities:

- identify the role: reconstruction-based representation learning, probabilistic latent modeling, generated-data output or downstream augmentation;
- connect the reconstructed or generated object to its actual consumer, separating training objectives from the retained prediction path;
- explain the need for that role; scarcity, imbalance and corruption are possible motivations, not compulsory background claims;
- state conditioning information and the data available during fitting and prediction.

Select evidence by that role:

- for representation learning, evaluate the downstream task and use matched objective/path controls when claiming their benefit;
- for a reconstruction-based detector, define the scored quantity, reference distribution and alarm rule; a latent-space statistic need not be a reconstruction residual;
- for generated-data output, examine fidelity, coverage, diversity and condition consistency where they answer the stated generation question;
- for augmentation, evaluate on untouched real test units, compare relevant simpler alternatives and check the synthetic/real training composition;
- use expert or mechanism checks for physical claims when meaningful, not as a ritual for every decoder.

An autoencoder's reconstruction objective does not make its complete pipeline unsupervised or require every latent representation to have fewer coordinates. P66 pp.2-3 defines encoder/decoder reconstruction, while pp.5-6 retains token dimensions, uses label-dependent objectives and removes decoding from the classification path. P67 pp.3-4 instead connects recurrent encoding and contrastive training to a latent-space monitoring statistic. In abstracts and contributions, state how the learned representation supports the claimed output; do not replace either actual path with synthetic-data generation, imputation or a mandatory residual threshold. Keep source-specific full model names attributed.

For a VAE, identify the latent prior, approximate posterior, decoder likelihood and variational objective before transferring the name (P17 pp.3-4; P64 pp.2-3). A stochastic latent variable is not by itself proof of a variational objective or calibrated predictive uncertainty. Check whether an encoder head returns a standard deviation, variance or log variance: these require different transformations in Gaussian sampling. State the actual prediction rule, such as a latent mean or an average over samples, if it affects the claimed output. Do not import an ambiguous source formula or imply that every application must produce uncertainty intervals or synthetic samples. Paired base-name and Chinese-translation records are in the [terminology bank](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

For generation as the task (P32), distinguish fidelity, diversity, condition consistency and downstream utility. Downstream utility can be one evaluation dimension without making diagnosis the primary task. P32 motivates generation with data availability, but this does not require another manuscript to assert an unobserved shortage. For augmentation as the means (P35), trace real training samples through the generator to the downstream learner, then evaluate that learner on untouched real test units. Do not put an augmentation-only generator into the diagnostic inference path. A latent-space generator also needs its encoder/decoder roles made clear; lower latent dimensionality alone does not measure total generation cost.

For methods with a generator and discriminator, inspect what is generated and what the discriminator predicts before writing the method-to-task link. P70 pp.3-4 maps acquired measurements to features and uses source/target discrimination to inform performance-grade learning; its full GAN-named method does not establish synthetic sample augmentation. P72 p.5 instead generates training examples for a separate fault classifier. P71 pp.4-5 retains generator inversion and discriminator scores for detection, then describes a discriminator-derived classification path. Thus neither `all generators run at diagnosis time` nor `all generators are discarded after training` is a safe generalization. In an abstract or contribution, connect the particular training signal or generated object to the retained predictor; a training adversary need not become another sequential inference module. Keep full source names attributed, and do not promise exact alignment, equilibrium or preserved fault information merely because the objective is adversarial.

Purposefully changing diagnostic inputs to induce errors is a different role;
the shared word adversarial does not make that design a GAN. Use the conditional
[input-attack evaluation route](experiment-evidence-design.md#input-attack-evaluation)
for those claims and retain the actual training-to-prediction relationship.

中文要点：先分清“生成的是样本还是特征”“判别的是真伪还是域”，再写它怎样支持最终任务；不同预测分支可保留不同部件。无需强行把原论文专名改掉，但不能由专名补出样本增强或推理步骤。基础名称配对与独立译名见[术语记录](engineering-application-terminology-bank_CN.md#九已核验核心名称与未完成范围)。

When turning this role check into an abstract or overview, use the [mechanism-to-prose check](abstract-and-contribution-craft.md#2-give-each-sentence-a-job-and-a-connection) to select the relationships the reader needs. Keep diagnostic exclusions in author notes unless they resolve a necessary scientific distinction; do not paste the full audit or repeat a training-versus-prediction fact as the closing benefit. No minimum length is needed to make a role description complete.

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

For **knowledge distillation**, identify who supplies the training target, what is matched, which data each side can access and which components remain at prediction. Teacher/student are learning roles, not a requirement that the teacher be larger or more accurate on every sample. P45 transfers hidden features and regression predictions; KD therefore does not require class probabilities or softmax. P46 transfers multisensor guidance to single-sensor learning, so sensor availability may be the motivation rather than compression. Output distributions, raw scores, hidden features and prototype similarities are different objects: inspect normalization, temperature and the loss before choosing the noun. P46's rendered Eq.(6) contradicts the neighboring unnormalized-score explanation; keep that conflict explicit in source notes rather than copying either claim as verified implementation.

Distillation changes training; any teacher execution, student routing or branch combination at prediction must be established separately. A teacher used only for training is not fused into each prediction, but do not remove a teacher that the actual inference procedure still calls. Compare the trained student with the same student trained without distillation when isolating that effect; teacher comparisons answer a different question. If compression or speed is claimed, evaluate the retained prediction graph and any auxiliary calls, not the number of training branches. A confidence target computed from training errors can train a predictor used for exit decisions (P45); do not infer test-label access without following that training-to-prediction interface, or call input-conditioned exits online parameter updates.

For selection-based designs, identify whether the output is a ranking, a weighted input, selected descriptor indices or a subset of physical measurements. P40/P61 implement explicit removal; P62's attributed selection layer weights inputs and supplies rankings. Link that operation to the retained classifier before claiming a cost benefit. Selecting six derived descriptors may retain all their source sensors; selecting two raw measurements can reduce the model's acquisition requirement when the remaining computation uses only those inputs. Explain the actual dependency, rather than importing a multistage or missing-data story into every selection method. Use the [selection evidence check](experiment-evidence-design.md#selection-outputs-and-resource-claims) when the paper claims a smaller input or resource demand.

Separate fewer attention queries from fewer retained tokens. P74 pp.4-5 preserves patch representations, aggregates channel values with one class query, then retains the other value tokens for later processing. Its full selective-module names are attributed examples, not pruning-family admission. P31 p.4 changes polynomial degree during the described training procedure, not by deleting a subset of nodes. P45 p.5 instead describes converting compatible training branches for prediction; that conversion is distinct from its distillation losses and conditional exits. In an abstract or contribution, explain which operation changes, what representation remains and how it reaches the task output. Do not turn all three designs into the same compression story or equate a smaller score map with complete-model acceleration. Use the [mechanism-to-prose check](abstract-and-contribution-craft.md#2-give-each-sentence-a-job-and-a-connection) to keep implementation checks in author notes unless needed to define the contribution.

For a parameter-masked design, distinguish scalar sparsity from deleting whole
filters/channels, changing a value range and penalizing gradients. Identify
whether the modified network is the retained predictor or an auxiliary training
copy. A sparse copy used to construct contrastive views can train a full predictor
without compressing it. A contribution may concern this particular learning
interaction, subject to prior-work and outcome checks; do not recast it as edge
deployment or treat the pruning ratio as the measured latency reduction. Check
the [operation and phase distinctions](terminology-decisions.md#structure-and-operations)
and [resource boundary](experiment-evidence-design.md#selection-outputs-and-resource-claims)
only when relevant to the manuscript's claims.

P85 p.4 prepares and retrains pruned variants before selecting execution at a
gateway or edge server; P86 pp.3-5 separates parameter removal from the hardware
representation and nonzero-index generation needed to execute it. This supports
the [scoped base pruning record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope),
not a universal ratio between zeros, stored bytes and latency. For a runtime
selection design, connect state observations to the chosen fixed predictor and
decision, not to invented online fitting. A collection of resident variants has
its own memory footprint. Keep simulated resource gains under their stated cost
model distinct from observed device gains; an accuracy-profile constraint uses
an estimate rather than guaranteeing each task's diagnostic correctness.

中文也区分生成并重训模型变体、运行时选择模型以及真正更新参数。说明被选模型如何形成故障决策；内存对应单个变体还是常驻集合，成本来自模拟假设还是设备测量，准确率条件使用什么估计，都须与实际证据相符，不为所有轻量化研究强加同一部署故事。

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

For counterfactual outputs, first identify their use. P62 pp.5,7 returns
generated inputs and model responses for interpretation; P94 pp.4-5 uses
target-class generation for augmentation and importance analysis. Connect the
candidate to the explanation or trained predictor instead of inventing a final
feature-fusion stage. A desired-class match and small input distance are not
the same as a physically achievable correction. Use the
[counterfactual-output route](experiment-evidence-design.md#counterfactual-outputs)
for the actual claim; retain legitimate model-level explanations and do not
infer a causal action merely from the shared name.

中文：生成的候选用于解释模型、训练增强还是建议动作，应分别交代输出和使用者；不把分类目标一致性直接写成实际工艺可行性，也不因未验证工艺动作而否定模型级解释。

For an origin-location method, trace what connects the learned relationships to the returned candidate. P13 pp.4-5 learns unit and variable graphs through prediction, then performs graph-node attacks and a separate top-down score search. P16 pp.6,10 instead follows fault detection with abnormal-link annotation and process-based interpretation. Preserve their attributed names and different decision rules; neither establishes one mandatory root-cause module. In an overview or contribution, explain how the relationship model supplies the search or interpretation, and why its unit of output answers the engineering question. Do not append a fault classifier to a method that returns a root location, or turn a diagnostic classifier's heatmap into an origin decision without a defined rule and evidence. A graph-load score is a modeled quantity, not automatically physical equipment load or measured process intervention response.

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

An expert need not be a neural subnetwork: P41 combines linear expert predictions with input-dependent gates. Name the actual expert model and mixed object. Sparsity in fitted coefficients is different from activating only a subset of experts at inference; report the latter only when the execution actually skips experts. Learned mixture weights do not by themselves identify discrete physical operating modes. In knowledge-guided mixtures, keep possibility-based prior information, mixture probabilities and fitted responsibilities distinct rather than calling every weight a probability.

“混合专家”是基础类别，专家可以是线性模型；是否为神经网络、是否稀疏执行、是否对应物理工况，都要分别核实。“系数稀疏”“专家路由”和“任务梯度平衡”不能互换。

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

Connect the predictor to the final fault decision, not just to a vector called probabilities. Local softmax scores may be combined and thresholded to select several faults, as in P37/P39; multilabel output does not require a particular activation in every component. Alternatively, a model may select one predefined composite class such as `A+B`: this is a multiclass formulation whose ability to identify constituent faults depends on an explicit class-to-fault mapping. Preserve the implemented route and its supported combination space. A ranking, individual fault indicators and a completely correct fault set answer different engineering questions; use the [multilabel evaluation check](experiment-evidence-design.md#multilabel-and-compound-fault-decisions) when interpreting results.

中文核查重点：局部分类器的互斥输出不等于最终结果只能有一个故障；将复合组合编码为单一类别也不等于允许任意组合的多标签预测。正文应连清局部输出、组合规则与最终故障集合，不为统一名词而替换真实结构。

For open-set recognition, connect known-class prediction to the decision that flags an input as outside the known label set. P51 uses a score derived from classifier logits, whereas P52 uses evidential uncertainty. Rejecting a sample as unknown does not identify its previously unseen fault type. Nor does performance on unseen operating conditions necessarily test unknown classes: define the retained fault labels and held-out conditions separately. A concise contribution can explain how a representation supports known-class classification and how the specified score supports rejection; merely adding the familiar two operations is not automatically a new contribution.

Check the complete decision rule before copying a threshold: score definition, sign, temperature if present, comparison direction, and selection data. In P51, the displayed logit activation, energy sign and stated threshold require clarification before reproducing the rejection rule; Algorithm 1 shows training updates and a separate test classification loop, so nearby `testing loss` prose is not evidence of test-label optimization. The paired base-score definition in the terminology bank does not certify that full implementation.

## 13. Dynamic, Multiscale, Slow-Feature, Or Time-Frequency Representation

Writing priorities:

- identify the modeled scale: an architectural receptive field, a sampling/time window, a frequency band, or a production hierarchy; relate it to process behavior when making that physical claim;
- distinguish slow operating evolution, transient response, periodic structure, and measurement noise;
- explain why a representation is needed before naming its encoder or transform;
- define the scope of `local/global features`; architectural locality is legitimate, but is not automatically a physical process scale or plant-wide coverage.

Evidence priorities:

- static-versus-dynamic and time-versus-frequency comparisons;
- scale, lag, window, or retained-band sensitivity grounded in the process;
- controlled removal or replacement of each representation branch;
- transient, steady-state, and mode-specific analysis when relevant;
- efficiency analysis if the representation is claimed to be lightweight.

Verify that the modeled axis is acquisition time before interpreting trends, lags or frequencies physically. Stacking unrelated product samples or repeating a static vector does not supply a temporal trajectory. For multiscale or local/global descriptions, identify whether scale means time window, frequency band, graph neighborhood or production hierarchy. Convolutional feature channels need not correspond to the original process variables (P11). Describe training regularizers separately from prediction-time branches rather than making the abstract list every loss as another representation module.

For multiscale convolution, follow the varying support to the output and its next consumer. P11 pp.3-4 concatenates different-kernel branch outputs before later relation modeling; P15 pp.4-5 passes concatenated outputs to an LSTM; P01 p.4 adds parallel branch outputs and later pools each stage before fusion. These support a common different-support extraction principle, not a compulsory concatenation operator or one universal temporal axis. A short abstract can state what neighborhoods are encoded and how the combined representation supports the next operation; a contribution should explain the supported advance rather than list kernel sizes as novelty. Different kernel widths alone do not establish isolated frequency bands, physical time constants, noise removal or superior diagnosis. Test those interpretations when claimed; otherwise keep an accurate architectural description without demanding a separate physical-scale experiment.

When thresholding is central, state whether it acts on measured signals,
transform coefficients or learned feature values, and how the result reaches the
decision. P87/P88 define soft feature shrinkage with different threshold-generation
and fusion designs. It need not involve wavelets, sensor removal, parameter
pruning or online fitting. Describe the actual input-dependent transformation
and its tested task benefit; keep full source module names attributed. 中文：
说明阈值处理的对象及后续融合，不将低幅值直接认定为噪声；特征收缩与参数剪枝、传感器删除不是同一主张。

中文要点：先说明尺度是模型感受野还是有依据的工艺尺度，再连清分支输出及后续用途。可以合理使用已定义的local/global，不必强改成物理尺度；多尺度不等于多工序，也不由卷积核大小直接推出频带分离。基础名称和独立译名依据见[术语核验表](engineering-application-terminology-bank_CN.md#九已核验核心名称与未完成范围)。

For SFA claims, trace the temporal objective and its nontriviality constraints. The classical definitions in P54/P55 minimize derivative energy under zero-mean, unit-variance and decorrelation constraints. A learned slow representation is not simply a moving-average trend; retain ordinary smoothing terminology when that is the actual operation. A deep model may instead use soft penalties or probabilistic dynamics: describe those choices rather than asserting exact equivalence to all classical constraints. Reconstruction does not itself impose zero mean, and decorrelation alone does not establish statistical independence. See the [feature-scale check](experiment-evidence-design.md#8-metric-integrity) before interpreting a smaller temporal-difference loss as better dynamics modeling.

Slow variation alone does not establish quality relevance, and a rapidly varying component is not necessarily noise. P34 distinguishes a quality-related latent component from an auxiliary component that helps recover information under multirate observation; its measurement and target equations define their roles. Explain what supervision or constraint relates a representation to quality. An auxiliary component can contribute to joint state inference without entering the output equation directly. In P53, parallel slow and fast-feature streams feed a common regression head, while temporal-difference, reconstruction, covariance and prediction terms regulate training. Use that operation-to-output relationship to connect an abstract or contribution; do not turn the loss terms into serial inference modules or infer computational savings from parallel layout alone.

Keep the meaning of `global/local` explicit. P54 pp.4-5 applies one historical-data SFA projection and separately estimates a local projection from each available input window, then passes the combined features and their differences to a classifier. These are time/data-scope definitions, not plant/stage hierarchy. Recomputing a projection on a window is different from applying a fixed projection or advancing a recurrent hidden state. State what is fitted or updated, using which data and at what decision time; neither a moving window nor a state difference alone proves parameter learning or handling of arbitrary nonstationarity. For state-space or bidirectional models, use the [decision-time check](experiment-evidence-design.md#3-split-integrity-checklist); a backward training computation does not alone establish a future-data violation at prediction time.

For a latent state-space model, separate model structure, state estimation, parameter fitting and the task output. P34 pp.3-6 uses latent inference to supply a quality predictor; P73 pp.4-6 uses inferred dynamic/static variables and residuals for monitoring statistics. Their filtering/smoothing operations help fit or apply the model, but are not interchangeable with an online parameter-learning rule. In an abstract or contribution, state how the inferred representation supports that final task, selecting the needed connection rather than listing every estimation step. A latent coordinate need not be physically interpretable, and a valid mechanism-based physical-state model should not be relabeled as uninterpretable merely for consistency. P73's global/local scopes refer to shared versus rate-specific latent structure, not production stages. A step with no acquired measurement can propagate a model prediction without adding a new measured observation. Check the actual observation schedule, conditioning horizon and prediction release time before claims about missing-data recovery, forecast horizons or zero-delay operation; choose additional tests only for the interpretations claimed.

### Forecasting And Life Targets

Choose the target before borrowing prognostic language. P45 p.6 defines a
window-to-RUL task with a maximum life label; P81 p.3 defines RUL regression and
p.6 distinguishes its engine and time-to-failure cases. P95 pp.3-4 instead
predicts future process-variable trajectories for a later limit-crossing alarm.
These routes share a future-oriented engineering purpose, not one output or
mandatory architecture. A current health indicator, future temperature vector,
remaining-life estimate and fault-class label are different targets.

For RUL, establish the failure endpoint or end-of-use criterion, prediction time,
units and label construction. A capped or piecewise life label has a defined
early plateau; that is not evidence that physical remaining life is constant.
Historical end times can legitimately construct supervised training targets
without being supplied to prediction. If an endpoint was not observed, state
the actual available label information rather than silently treating the last
record as failure. Do not turn an equipment-life convention into the default
target for a chemical-process forecast.

For trajectory prediction, define the input cutoff, target variables, horizon
and direct-output or recursive rollout. Distinguish measurements available at
issue time from later realized inputs; a genuinely known planned control
sequence can be a legitimate input in another declared task. Explain how the
encoded history supplies the retained prediction head. If a forecast is
converted to an alarm, connect the explicit rule to its event/timing evaluation;
lower trajectory error alone establishes neither longer warning lead nor a
life estimate. Keep mixed horizon and alarm outcomes in Results and the
abstract's closing finding when material. See [target semantics](terminology-decisions.md#forecast-targets-and-life-quantities)
and [forecast/life evidence](experiment-evidence-design.md#forecasting-and-life-evaluation).

中文：先按最终输出区分未来过程量、当前健康指标、剩余寿命与故障类别。
寿命截断标签不等于实际寿命恒定；未来轨迹误差、越限事件识别与提前量是不同证据。
不用一种设备寿命写法统一所有流程工业预测。

For soft sensing or forecasting with an uncertainty output, identify whether
the model estimates a mean, a new observation's distribution or a joint region.
P103's monitoring distribution and P104's scalar quality intervals have different
consumers. Connect the estimated quantity to actual interval endpoints and any
warning rule; do not borrow calibration, safety or condition-wise reliability
from a Bayesian, fuzzy or probabilistic label. Read the
[output-interval guidance](experiment-evidence-design.md#output-prediction-intervals)
only for the corresponding claim. A point-prediction study need not add an
interval model, and a latent-variable model need not output uncertainty bounds.

中文：软测量或预测含不确定性输出时，先分清均值、新观测值分布与联合区域，再连接到区间和实际决策；不把重复训练误差条当成单样本预测范围，也不为普通点预测强加区间实验。

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
