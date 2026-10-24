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

Choose the narrative from the observation mechanism. For fixed multi-rate streams, explain which variables are measured at each rate and how slow measurements align with the prediction target; verify frequency versus period units before comparing rates. For irregular observations, explain how elapsed time differs from sequence position. P24 explicitly encodes both; its solution does not make every multi-rate problem irregular. For delayed quality assays, distinguish the time represented by a label from the time it becomes available. `Offline assay` can accurately describe laboratory measurement even when `offline dataset` adds nothing to provenance.

Turn acquisition facts into the specific estimation requirement. A complete-observation comparator may discard useful measurements between shared observation times; a model that uses an observed-subset likelihood should explain how those measurements enter estimation. This is a different route from constructing a completed input grid, aligning rate-dependent representations, or learning with sparse quality targets. Name the route actually implemented and the intermediate object it supplies to the output. Do not add an imputation stage merely because some variables are unobserved. P08 develops representation alignment from a granularity question; P17 develops semisupervised regression from assay scarcity; P34 defines separate measurement and quality equations under multirate acquisition. These are alternative argument structures, not interchangeable remedies or evidence of complete information recovery.

If completion and prediction are coupled, trace the completed measurements, their encoded representations and the final quality/fault output separately (P25, P33). In an abstract or contribution, connect the operation to its recipient: estimated missing measurements may supply a predictor, while a reconstruction loss may constrain a shared encoder during training (P17). Preserve the actual parallel or sequential structure; a decoder, padding value or aligned latent vector does not by itself establish an imputation output. If a numerical placeholder is excluded by a mask, describe that role rather than calling it a recovered measurement.

Distinguish the acquisition mask from additional entries deliberately hidden during learning or evaluation, and from the positions included in each loss. State whether the reconstruction target is the original observation, a corrupted input or another defined quantity. Observed input values can provide reconstruction targets even when quality labels are scarce; those two kinds of supervision are not interchangeable. Follow the [missing-value evidence check](experiment-evidence-design.md#6-robustness-design) before claiming recovery accuracy. If the target is causal structure (P08), structure-recovery assumptions and evidence take priority over a generic diagnosis comparison. Do not invent a universal minimum number of rates from one paper's definition.

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
| Self-supervised learning | How targets are constructed, what augmentation preserves physically, and whether the auxiliary objective is trained jointly with the task or in a separate phase | Relevant objective/path controls and downstream evaluation; preserve the actual training schedule and do not imply that no labels are used anywhere |
| Unsupervised clustering | Which object is clustered, how the number of clusters is determined, and how clusters are related to fault identities | Clustering quality and the declared evaluation-only label matching; do not conceal labels used for model selection or imply cluster indices already identify faults |

P05-P06 exemplify semantic transfer; P17 uses labeled and unlabeled measurements for concentration prediction; P21 couples self-supervised and diagnostic learning; P22 learns from segment labels for point-level detection. Their method names do not make these supervision arrangements interchangeable. P18 adds long-tailed classes and cross-domain information, in an adjacent equipment setting.

These labels need not be mutually exclusive. Semisupervised learning describes the use of labeled and unlabeled examples for the task; self-supervision describes how an auxiliary learning signal is constructed. P21 jointly trains diagnostic and self-generated temporal objectives, while P26 shares an encoder between class prediction and sampling-transformation prediction. Neither requires an invented pretraining/fine-tuning sequence. Conversely, adding a self-supervised objective to fully labeled task data does not by itself establish a semisupervised setting. In the abstract or contribution, connect the auxiliary target to the shared representation and task output rather than listing the two learning names. If both appear, do not use `SSL` ambiguously for both.

For weak supervision, name the actual limitation instead of assuming coarse labels or annotation noise. P22 pp.3-4 trains with segment labels for point predictions; P25 pp.2,4-5 uses its weakly-supervised name for completed auxiliary measurements with sparse quality targets and model-derived guidance. Preserve those source-specific meanings without treating them as one shared operator, importing bags into regression or renaming every semisupervised model. A self-generated transformation label or pseudo-target is a training signal, not an additional independently measured fault/quality annotation; report those counts separately when discussing annotation savings. See the [base-name records](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

For contrastive learning, name the contrasted objects and how their training relation is constructed. P20 contrasts graph representations, whereas P21 contrasts temporal contexts and later latent features across views. A positive pair need not mean normal operation, and a negative pair need not contain a different fault class. Verified class labels can legitimately define supervised contrastive pairs; preserve that setting when implemented. Temporal separation or a distribution-distance rule alone does not prove statistical independence. Check whether an augmentation preserves the diagnostic property before claiming fault invariance, particularly when amplitude or timing carries the fault signature.

Trace generated class guidance to its actual consumer: P18 uses adjusted predictions as hard training targets; P21 uses soft class distributions to guide relationships between training samples. Such a sample graph is not a graph of sensors or physical production links. P21's later-feature prediction is a training objective, and only its encoder/classifier are used for diagnosis at test time. Do not recast that pretext task as physical forecasting or future-measurement access during diagnosis. These distinctions belong in the method; an abstract needs only the connection central to the claimed advance. Use the [paired terminology records](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) for the base names, not as permission to borrow complete source-specific module names.

中文核查重点：对比对象及配对依据、伪标签的硬/软形式和实际使用者、样本图与物理变量图、训练任务与预测输出分别核对。正负配对不自动是正常/故障分类；真实类别指导的有监督配对可以成立。增强是否保留故障特征需依据，不将这些内部核查逐项塞进摘要。

When a few-shot method uses class prototypes, connect the support features, prototype construction and query-scoring operation. P47 computes support-feature means and uses a learned matching function; the mean construction is not itself a newly invented physical-state estimator. A prototype can be derived from a trained embedding without being an independently optimized parameter. Do not impose this mean construction on a method that defines exemplars, multiple representatives or another estimator. Put the actual advance in the contribution, not every standard constituent of this chain.

For episodic learning, distinguish labeled queries used to train the model from held-out queries whose labels are unavailable to prediction. The former is not automatically test-label leakage. Conversely, calling a sample a `query` does not establish its permitted use: state the training/evaluation phase, the support/query roles and any allowed test-time adaptation. Verify class overlap separately from sample disjointness; few-shot does not by itself guarantee previously unseen classes. P47's formulation permits partial overlap or disjoint base/support classes, so its name cannot substitute for the actual split definition.

中文核查重点：类原型的来源及后续用途、训练查询与测试查询的标签边界、样本划分与类别划分分别交代；不把类代表写成物理工况，也不要求所有小样本方法都采用均值原型或分任务训练。

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

Check **label-space relations and label availability separately**. P10 uses identical source/target class spaces with unlabeled target measurements, whereas P44 addresses a target class subset and its training equations include target-label symbols. Neither assumption transfers automatically to another adaptation paper. If a target label enters a loss, identify whether it is observed, inferred or evaluation-only before assigning a supervision category; a pseudolabel is not a measured annotation. Domain adaptation is broader than unsupervised adaptation. In a multisource design, distinguish distribution alignment during fitting from a separate weighted combination of classifier predictions; the two may coexist without any source/target feature fusion at inference.

Name the aligned populations and criterion. A lower marginal discrepancy alone cannot establish class correspondence or target diagnostic accuracy; legitimate class-conditional alignment should retain its class guidance and access conditions. Evaluate the claimed prediction benefit separately from the internal alignment statistic, with class-level analysis when label-space mismatch is central. The [alignment distinctions](terminology-decisions.md#alignment-state-the-object-and-criterion) also prevent confusing domain matching with acquisition synchronization or mutual-information estimation.

Check whether adaptation actually concerns learned parameters. Input-dependent routing can respond to a new window with frozen parameters; a recurrent state or rolling score reference may change without retraining. These mechanisms can be described as adaptive at their defined level, but they do not alone constitute continual learning. P24 conditions temporal weighting on observed intervals, whereas P04 defines a rolling statistical score after reconstruction. Keep the changing object consistent from contribution to Methods and evaluation; do not add an online-learning experiment to a paper that claims only input-conditioned weighting.

Select chronological, mode-held-out, cross-period or cross-site evaluation according to the claimed shift. When drift and class proportions both change, distinguish their effects rather than attributing all change to a generic domain gap.

Trace adaptation at its actual granularity. P63 separates an evolving subspace/classifier from out-of-sample prediction and conditions classifier learning on revealed labels. P64 assumes operator-known mode switches for model updates and separately adapts an alarm threshold; its online wording does not establish automatic switch discovery. P05's test-time operation pools selected unlabeled predictions to adjust semantic references without another network forward/backward pass. State whether a current sample, a past window or the full target batch supplies an update, and whether the resulting state persists or resets between cases. Use that information in the method overview and the [adaptive evaluation check](experiment-evidence-design.md#adaptive-state-feedback-and-retention) when adaptation is a central claim.

For retention or replay claims, identify what remains accessible. P64 caches historical latent features and constrains parameter changes; P65 avoids replay of previous target-domain instances while continuing to use labeled source-domain samples and an earlier model. Neither example establishes a requirement to store raw data, a universal source-free setting or a privacy guarantee. Explain the retained information and its role in the next update, then assess earlier as well as current conditions if retaining earlier capability is claimed. Shared labels across changing domains are compatible with continual learning; new fault classes require a separate class-incremental definition.

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

A causal temporal convolution concerns past-versus-future information access; a predictive adjacency is a learned relationship; physical causal identification needs additional assumptions and evidence. P14 provides a useful place to inspect these distinct roles, not a license to equate them. Check the complete computation before using `hard exclusion`, `sparse` or `independent`: logit reweighting followed by softmax is not automatically class exclusion, and a block-diagonal adjacency does not prevent a later dense layer from combining groups. Resolve equation, pseudocode and implementation differences in author notes before strengthening the prose.

For fuzzy models, define the membership domain, rule/aggregation operation and intended interpretation. Normalized memberships or softmax assignments are not automatically calibrated class probabilities. P07 uses fuzzy states to construct temporal relationships and training constraints; that does not justify applying calibration metrics to every membership value. Evidence might instead examine rule effects or membership sensitivity. Probability calibration is pertinent when an output is interpreted as a probability, including present-condition classification, not only future forecasting; evidential masses and fuzzy memberships require their own definitions.

Trace what an uncertainty-related quantity represents and where it acts. P49 pp.5-6 weights learned responses at feature positions; its specified weighted sum is not the formal Dempster combination discussed in its preliminaries. P50 pp.3-4 models variation in feature statistics to generate perturbed training features. Neither operation alone supplies a sample's probability of being correctly diagnosed. In contrast, P52 pp.2-3 connects class evidence, a Dirichlet distribution and a sample-level uncertainty output. These are attributed examples of different roles, not interchangeable modules or a completed general admission record for every evidential-learning name.

Write the actual connection positively: when implemented, `Input-dependent weights combine the learned responses into features used by the diagnostic classifier.` If a separate score controls rejection, describe that subsequent decision instead of hiding it inside `reliable fusion`. State a demonstrated effect in the results; normalization, a loss named calibrated, or a paper title containing trustworthy does not by itself establish empirical probability calibration. Follow [the score-to-decision evidence check](experiment-evidence-design.md#scores-probabilities-and-rejection-decisions) only when the manuscript makes that claim.

中文也应先交代量的对象和用途：用于特征加权、构造训练扰动、描述类别分布，还是控制最终拒识。它们可以共同服务诊断，但不能只因都与“不确定性”有关就写成同一类机制。方法段写清实际操作，实验段再报告已检验的作用，不必为普通分类器额外虚构拒识或校准任务。

Do not treat all fuzzy mechanisms as a rule base. P27 uses a fuzzy predictor after deep feature extraction, P28 uses layer-wise fuzzy clustering to reinforce reservoir features, and P33 couples fuzzy clustering with imputation. Identify whether membership describes an input region, a temporal state, a cluster or another defined object. Clustering memberships do not by themselves supply readable expert rules; a fuzzy layer or a physically motivated kernel does not make the entire model interpretable without specifying what can be explained and to whom.

Treat source-specific uses of `reinforcement` by their defined operation. P28 p.3 uses fuzzy clustering and center-related targets for feature fitting; that name is not evidence of reinforcement learning. Describe the actual objective and information flow. Only use the reinforcement-learning category when the study implements the corresponding learning setup, rather than inferring it from this word alone.

Choose removed/randomized/corrupted-prior controls when they isolate the knowledge claim. Preserve constraints that define a valid process when constructing a perturbation; a physically impossible random graph can be a stress test but not a realistic operating alternative.

## 7. Reconstruction-Based, Generative, Diffusion, Or Data-Augmentation Methods

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

For SFA claims, trace the temporal objective and its nontriviality constraints. The classical definitions in P54/P55 minimize derivative energy under zero-mean, unit-variance and decorrelation constraints. A learned slow representation is not simply a moving-average trend; retain ordinary smoothing terminology when that is the actual operation. A deep model may instead use soft penalties or probabilistic dynamics: describe those choices rather than asserting exact equivalence to all classical constraints. Reconstruction does not itself impose zero mean, and decorrelation alone does not establish statistical independence. See the [feature-scale check](experiment-evidence-design.md#8-metric-integrity) before interpreting a smaller temporal-difference loss as better dynamics modeling.

Slow variation alone does not establish quality relevance, and a rapidly varying component is not necessarily noise. P34 distinguishes a quality-related latent component from an auxiliary component that helps recover information under multirate observation; its measurement and target equations define their roles. Explain what supervision or constraint relates a representation to quality. An auxiliary component can contribute to joint state inference without entering the output equation directly. In P53, parallel slow and fast-feature streams feed a common regression head, while temporal-difference, reconstruction, covariance and prediction terms regulate training. Use that operation-to-output relationship to connect an abstract or contribution; do not turn the loss terms into serial inference modules or infer computational savings from parallel layout alone.

Keep the meaning of `global/local` explicit. P54 pp.4-5 applies one historical-data SFA projection and separately estimates a local projection from each available input window, then passes the combined features and their differences to a classifier. These are time/data-scope definitions, not plant/stage hierarchy. Recomputing a projection on a window is different from applying a fixed projection or advancing a recurrent hidden state. State what is fitted or updated, using which data and at what decision time; neither a moving window nor a state difference alone proves parameter learning or handling of arbitrary nonstationarity. For state-space or bidirectional models, use the [decision-time check](experiment-evidence-design.md#3-split-integrity-checklist); a backward training computation does not alone establish a future-data violation at prediction time.

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
