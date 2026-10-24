# Context-Sensitive Terminology Decisions

Use this alongside the [terminology bank](engineering-application-terminology-bank.md), not as a replacement dictionary. Published use establishes that a term can be legitimate; it does not establish that it describes this manuscript's object. Source IDs refer to the [published evidence index](published-evidence.md). Author preferences belong in the individual manuscript's terminology map.

## Decision Procedure

1. Identify the referent: physical quantity, acquired observation, sample, latent feature, condition, learned state, or model operation.
2. Inspect the sentence, the definition/equation, and its recipient. Do not infer an operation from a module name alone.
3. Check comparable published contexts. Search exact phrases and inflections, excluding references and quoted titles; inspect whether a match is a noun, verb or citation.
4. Classify the decision: correct; correct but needs definition; author preference; ambiguous; scientifically inconsistent; evidence unavailable.
5. Propose a local clause-level change only if needed, with source/page and rationale. Never run global substitution on these entries.

No search hit means **not found in this searched corpus**, not ungrammatical or forbidden. Search frequency is not a measure of scientific correctness. The optional terminology audit script only finds candidates for human review.

For general names of mechanisms, modules, methods or operations, follow the
[two-source admission and separate Chinese check](engineering-application-terminology-bank.md#0-admit-names-not-search-counts).
One source may establish its own defined name, not a general category. Preserve
attribution, author-proposed identities and accurate plain descriptions. A
familiar head word does not validate every compounded qualifier.

## Objects And Data Units

| Choice | Use when | Do not imply |
|---|---|---|
| process variable / measured variable | temperature, pressure, flow or another measured/controlled quantity | that a latent embedding is a physical variable |
| quality variable | a measured target describing product or process quality | that every label is a continuous quality measurement |
| feature / feature representation | an input descriptor or a learned representation; specify which if material | that the operation changes the measured variable itself |
| channel | a tensor/model axis, after mapping it to variables or signals | one channel equals one variable in every model |
| sample | the unit supplied to learning or evaluation, explicitly defined as a window, plate, batch, cycle or other object | a database row necessarily equals one statistically independent sample |
| instance / bag (in multi-instance learning) | a defined member representation and the collection supplied to a bag-level learner; instances may be points, subsequences or learned features | an internal instance necessarily equals an independently acquired or individually labeled production sample; bag supervision necessarily supports fine localization |
| observation / measurement | an acquired value, vector or observation event | one observation always has the same unit as one sample |
| record | an actual log/database record when describing storage, linkage or acquisition | a preferred synonym for a training sample |
| attribute | an actual semantic descriptor, graph-node attribute or metadata field | a default replacement for measured process variables |

For process-model training counts, prefer `training samples` and `test samples`. Use `development set` only if it really denotes a training/selection pool, and explain its partition. Do not rename a training set to imply an unperformed validation step. Do not replace `records` before determining whether rows and samples differ.

P05-P06 and P29 use semantic attributes for zero-shot fault categories; P20 uses graph-node attributes. P29 explicitly separates structured fault descriptors from sensor measurements and their textualized representations. These uses are compatible with preferring `process variables` for physical measurements. The word `attribute` as a verb in an explanation is unrelated to that decision.

## State, Condition And Mode

| Term | Appropriate meaning | Verification question |
|---|---|---|
| operating condition(s) | load, setpoint, speed, material or other operating circumstances under which data arise | Is this an identifiable regime or condition, rather than a hidden feature vector? |
| operating mode | a defined discrete operating regime | Were mode labels or boundaries defined? |
| operating state / operational state | the current behavior/status of a process, system or local unit | Is the object physical status, inferred status or a learned encoding? |
| process state | a physical, monitored or mathematically defined state of a process | Does the surrounding definition make the state meaningful? |
| latent state / hidden state | an internal mathematical representation | Is it being mistaken for a verified physical condition? |
| prototype | a learned/defined representative vector, exemplar or center | Is an actual prototype mechanism present? |

`Process state` is not an invalid phrase: P04 uses it in plant-level monitoring. P16 uses operational-state language in quality-related diagnosis; P10 studies operating conditions across domains. These are contextual examples, not a ranking of commonness.

A learned fuzzy state (P07), a discrete operating mode and a state vector in a dynamic model have different definitions. That state vector may be a statistical latent representation or have a justified physical meaning; the state-space form alone does not decide which. Preserve those definitions even when `state` occurs in all three. A process disturbance is an input or event that perturbs behavior, not a synonym for the condition under which measurements were obtained.

In a state-space description, connect the transition model, observation model and final output. P34 pp.2-6 estimates latent variables for quality prediction, while P73 pp.2-6 estimates dynamic/static latent variables for monitoring statistics. Neither a latent coordinate nor its covariance is automatically a measured physical state or a fault probability. A physically grounded state remains legitimate when its mapping is defined. P73 p.5 explicitly notes nonunique parameterizations before standardization; a normalization does not by itself make latent coordinates physically identifiable.

Do not replace `state` with `condition` merely for fluency: a continuously changing local representation is not automatically a discrete operating regime. `Local operational state` is usable if the model actually adapts to local measured behavior; it should not silently assert that the model identifies physical states. Never introduce `prototype state` when the method has no defined prototype.

For an actual prototype, name what it represents and how it is constructed: a class-conditioned feature mean, a selected exemplar and an independently optimized reference vector are not interchangeable. P46 and P47 compute class representatives from labeled features, with different later uses. A mean computed through a learned encoder is not necessarily a separate trainable parameter, and a class representative is not a measured operating state. Describe its connection to the next operation, such as query matching or a training loss, rather than assuming every prototype is a classifier or every class has exactly one. See the [paired terminology record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) for the checked scope and Chinese wording.

P79 p.9 defines source-class prototypes from classifier weight vectors and keeps
them fixed during target representation learning. Preserve that attributed
construction rather than rewriting it as stored source-sample means. A model
parameter used as a class reference, a source-instance replay buffer and a buffer
constructed from target measurements are different retained objects.

For `dynamic` or `adaptive`, identify **what changes**. Input-conditioned attention, group assignments or gates can change on every prediction while trained parameters remain fixed. A recurrent state or rolling reference statistic can also update without fitting model parameters. Online learning or test-time parameter adaptation is a different claim, requiring an actual update rule and its permitted information. P24's elapsed-interval weighting and P04's rolling anomaly-score statistics illustrate different changing objects; neither name alone establishes continual learning. Describe the verified operation directly, such as `input-dependent grouping`, without banning an accurately defined adaptive mechanism.

Kalman state prediction/correction and EM parameter fitting also change different objects. Check the conditioning horizon: filtering for time `t` uses permitted observations through `t`; smoothing may revise that state using later observations. A forward/backward E-step on training sequences (P34/P73) does not itself imply future observations enter current-time prediction. Conversely, a fixed-lag retrospective estimate may legitimately use later measurements if issued after their release; it should not be reported as a zero-delay result. Keep prediction-time state recursion, parameter updates and the final quality estimate or monitoring decision distinct in the abstract and Methods. The [paired base-name record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) does not admit every neural, adaptive or multirate full name.

Output delay alone does not establish use of later information: computation may finish late even when every input was already available at the target time. Compare actual measurement-release times with the claimed decision cutoff. Using later-released inputs for a claimed earlier decision is an information-access violation; misreporting a delayed computation as instantaneous is a latency/reporting problem even without later inputs. A cutoff described only as `available by issuance` does not identify the latest observation actually used.

Adaptation need not involve gradient updates: P05 adjusts semantic reference vectors from unlabeled test-sample predictions while retaining its network forward outputs. Describe that changed object and the data available to it. A whole-target-batch adjustment and a causal stream with only past/current observations have different information access, even when both run at test time. Preserve a source's attributed adjustment name; do not call every changing threshold or reference vector incremental parameter learning.

For **source-free domain adaptation**, identify the phase in which source samples
are unavailable. A source-trained model can retain labeled historical knowledge
while its target-side adaptation uses unlabeled measurements (P78/P79). Record
the provided model information and actual updated components: freezing an entire
classifier is one design, not the definition. Source-data access, target-label
access, source/target class overlap and prediction timing are separate axes.
Do not rename known-class adaptation zero-shot merely because target annotations
are absent, or infer a causal online stream from the source-free label.

Trace a `pseudo-source` object to its data origin and construction. A bank of
pseudolabeled target samples does not become acquired source data through its
name, nor add new independent measurements. State the verified access restriction
positively in manuscript prose. If stronger privacy is claimed, establish its
mechanism and scope separately; withholding raw source samples alone does not
certify a formal privacy guarantee. Keep such claim checks in author notes when
they are not needed to define the method.

For incremental learning, specify the new information and model update rather than assuming new classes: P30 updates a classifier under distribution change, while P63 also accommodates changes in measured input dimensions. Continual-learning claims additionally concern learning across a sequence while retaining earlier capability (P64/P65); memory buffers are one possible design, not a requirement. These labels can overlap. State the actual sequence, feedback and retention question instead of forcing them into mutually exclusive categories.

## Variables And Their Features

| Wording | Meaning and caution |
|---|---|
| variable-wise encoding / features | encoding organized separately by variable; define what the output contains |
| independently encoded variable features | features obtained by a path that encodes variables separately; verify the actual independence boundary |
| individual-variable features / features of individual variables | a relatively neutral description of the represented object |
| variable-specific features | features particular to individual variables, potentially emphasizing distinctiveness; valid English, but not identical to independent encoding |
| variable-specific behavior | behavior that differs across variables; name the actual difference, such as responses to a disturbance, when clearer |
| local variable features | features local to a defined unit, stage or neighborhood; not automatically features from an independent branch |

Do not globally replace `variable-specific` with `variable-wise`: the former describes what is distinctive; the latter often describes organization or computation. The reviewed corpus does not establish every exact collocation above. These distinctions are semantic guidance; retain only phrases supported by the actual mechanism and the author's accepted terminology.

For explicit subset selection, `feature selection` retains identified input descriptors: P40 returns selected feature indices, and P61 eliminates process-variable inputs using a ranking criterion. `Feature extraction` constructs descriptors. Published names also need their local definition: P62 calls an input-weighting/ranking layer a feature-selection layer, without defining a fixed-size subset in that layer. Preserve that attributed name and describe the weighting; do not turn every attention weight into a selection mechanism or insist that a weighted input is a newly extracted coordinate.

State which object is reduced. Several retained spectral or statistical descriptors may still require every original sensor. A later implementation may compute only the retained descriptors if their dependencies allow it; neither that saving nor removal of sensors follows from the selected-feature count alone. Check acquisition and preprocessing dependencies before claiming fewer required measurements, and measure the relevant computation before claiming faster inference. An explicitly implemented sensor subset can support a reduced-input claim without requiring a separate physical removal trial.

## Label Objects

| Term or object | Meaning to establish |
|---|---|
| missing annotation | An unknown target, not a confirmed negative; define whether absence applies to an entire sample or selected labels |
| candidate-label set | Alternative possible targets; state how many may be true and whether the true target is guaranteed to be included |
| multilabel target | Multiple labels may genuinely apply to the same sample; this is not ambiguity merely because more than one entry is positive |
| partial label space | A restricted set handled by a classifier, as in P39; do not infer incomplete annotations from the phrase |
| label enhancement / soft training target | A constructed numerical representation whose source and learning role must be defined; not automatically a corrected observation, probability or severity measurement |
| noisy label / noisy measurement | Error in the annotation/target versus corruption of the input observation; identify which is affected and which reference supports evaluation |

P39-P40 are adjacent machinery examples for these distinctions, not evidence that all process-industry supervision has the same form. P40's neighborhood-derived label values illustrate a learned object; a physical severity interpretation requires an independently justified relation to damage, intensity or another stated severity target. Do not rename sound paper-specific terminology globally, or infer field-wide usage from a title.

For zero-shot diagnosis, separate **measured training examples, class semantics
and synthesized training objects**. P05/P06 provide descriptions of unseen faults
without their labeled measurement examples; P80 additionally generates unseen-class
features for classifier fitting. A conditioning class ID on a generated vector is
not a newly acquired and annotated fault sample. Historical seen-class labels and
expert descriptions remain supervision/resources, so zero-shot is not synonymous
with an entirely unlabeled learning history. Record whether unlabeled unseen-class
measurements enter adaptation separately from that labeled-example boundary.

A fault-attribute entry can identify an affected variable or symptom without
being that variable's measured value. P06's attribute hierarchy and P05's category
descriptions have class-semantic roles; they do not rename raw process variables
or define production-stage partitions. Semantic matching can identify a named
unseen candidate, whereas unknown rejection only flags a sample outside the known
set. Specify the candidate pool and the information used to construct or adjust
its descriptions before borrowing either task name. No in-context demonstration
in an LLM prompt is a different resource statement from absent labeled examples
of a fault class.

## Structure And Operations

| Distinction | Decision |
|---|---|
| intra-stage / inter-stage / cross-stage | intra = within a stage; inter = between stages; cross = across stage boundaries. `Inter-stage relationships` and `cross-stage fusion` can coexist coherently. Do not reverse intra/inter or force identical prefixes onto different roles. |
| stage-wise / stage-level / stage-structured | stage-wise describes separate treatment; stage-level describes granularity; stage-structured claims a retained arrangement. Use the last only when that structure is actually retained and defined. |
| partition / grouping / clustering | partition may be fixed by knowledge; grouping may be learned or predefined; clustering implies a defined data-driven grouping mechanism. Soft assignments need not yield hard clusters. |
| aggregation / fusion / interaction | aggregation combines or summarizes a defined set; fusion combines identified information sources at a stated level; interaction computes relationships or exchanges between defined objects. These uses overlap: none alone specifies an operator, reduced dimension or physical influence. |
| relationship / dependency / correlation | relationship is broad; dependency is statistical or modeled dependence, not automatically causation; correlation needs a defined statistic or justified usage. |
| topology / prior / constraint | identify the engineering source and mathematical role. An additive attention bias is not necessarily a hard constraint or a causal graph. |
| causal convolution / predictive dependence / physical causation | A causal convolution excludes future inputs from a specified output; predictive dependence concerns information useful for prediction. Neither alone identifies a physical intervention effect or root cause. |
| spatial / spatiotemporal | Define the represented axis or relation: physical layout, process topology, graph neighborhood, or explicitly defined inter-variable structure. For spatiotemporal, identify the time axis too. Model-grid adjacency does not establish physical proximity or process coupling. |
| gate / attention / fusion module | a gate regulates a contribution; attention computes weighted relations/aggregation; a fusion module combines paths. Verify shapes and operations instead of interchanging names. |
| residual connection / signal residual / prediction residual | An additive network path, a remainder after a specified signal decomposition, and a measurement-minus-prediction error are different objects. Define operands and the next use. A linear dimension-matching path can be a valid residual connection; concatenating independent paths does not establish an additive one. |
| generator / discriminator / diagnostic classifier | Follow the actual input, output and training target. A generator may synthesize samples or encode acquired measurements; a discriminator may predict real/generated identity or domain identity. Neither target is automatically a physical fault class. Preserve attributed source names while describing their actual roles (P70-P72). |
| unified / global / plant-wide representation | name the scope actually represented. Combining two paths does not itself prove universal generalization or complete plant coverage. |

For `stage`, first distinguish a production unit, a temporal phase in a batch, and a learning phase. For `local/global`, identify the domain over which locality is defined. A temporal receptive field is not a plant region. For `propagation`, distinguish graph-feature updates from a physical disturbance spreading through the process. These decisions change scientific meaning, not merely style.

For multi-head attention, separate the head axis, attended positions and feature
axis. P11 concatenates head features before output projection; P82 additionally
routes coefficient matrices to a different summary. State which object is merged
and what receives it. Different query/key/value projections of one input can
still be self-attention; a separate query source changes that input relationship,
not the head count. Normalized attention rows do not make the projected output
a fault probability or prove independent physical relations. Use the [scoped
multi-head record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope),
not the base attention name to admit every full variant.

For causal convolution, inspect the tap offsets, padding and time axis (P81/P82).
Current-position access can satisfy a causal filter; strictly past-only prediction
requires the corresponding input/target lag. Dilation spaces taps on the model
grid rather than changing acquisition frequency. Trace subsequent operations
before claiming pointwise causal output, using the [decision-time check](experiment-evidence-design.md#3-split-integrity-checklist).
A completed trailing window can legitimately support an endpoint estimate even
when internal positions interact across that available window. Preserve the
actual task and [scoped base name](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope),
not an unverified physical-causality or complete qualified-module claim.

For graph-based descriptions, trace the node update separately from any later
unit/graph summary and final decision. P13 combines neighboring and own-node
features before a separate unit readout; P14 applies adjacency-weighted
projections before feature fusion and classification. A mean over updated nodes
does not itself make those node representations identical, although the summary
need not preserve their individual values. State the receiver/sender convention
from the actual multiplication; do not infer it from `A_ij` or a borrowed drawing.
Learned weights within a fixed allowed edge set do not establish that the whole
topology was learned. Use the [scoped message-passing record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope)
without importing a source's full causal or hierarchical component name.

For an additive residual path, check matching feature axes and the position of
projection, activation and normalization (P11/P15/P14). A projected input is not
an identity mapping, but its addition can still be residual learning. Do not infer
lossless retention from the sum or turn a trend remainder into a fault score
without its defined decision rule. Preserve an approved author-proposed component
name while describing its actual merger; a title containing `residual` does not
authorize changing concatenation into addition or admitting the full name as a
general family. See the [checked base record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

For a gate, identify its input, coefficient axis, regulated operand and subsequent
combination. P08 gates convolution features, P33 gates attention outputs and P36
weights experts for quality prediction; their names do not impose one
normalization or discrete-selection rule. P19 also shows why the bypass matters:
its `F + w*F` has coefficient `1+w`, so a small sigmoid weight attenuates the
added branch, not necessarily the final output relative to `F`. Follow later
projections or normalization separately. A feature gate can coexist with an
attention description; preserve an attributed name while explaining the actual
operation. A gate value's range alone establishes neither fault-probability
semantics nor sensor removal. Input-dependent coefficients with fixed trained
parameters are also different from online parameter learning; resource savings
require a verified execution path rather than merely small weights.

For origin analysis, distinguish the initiating disturbance, the earliest observed response and the model's selected node. A learned directed graph, a graph-load redistribution score and a real change to plant operation are different objects (P13/P16). Preserve a valid conditional causal-effect estimate from observational data when its target and identifying assumptions are stated; do not require a physical trial for every causal sentence. Conversely, a predictive relation or simulated graph attack alone does not identify a physical effect. Use the [interpretation evidence check](experiment-evidence-design.md#7-interpretation-design) for the corresponding claims, not as a compulsory addition to ordinary classification.

For `multiscale convolution`, state what varies across branches or layers and along which input axis. Kernel extent, dilation, stride and preceding layers jointly affect the input support; do not equate a kernel width with the full network's receptive field or a measured physical time constant. The checked base-name examples P01/P11/P15 use different branch supports, with addition or concatenation of their outputs. Their complete proposed block names remain attributed. A valid architectural `local/global` description need not claim physical process scales; a spectral-separation or plant-wide interpretation needs its own stated basis. For abstracts and contributions, connect the combined features to their actual next use instead of adding an unsupported physical benefit.

For fusion wording, identify the operands and next consumer before choosing a more specific name. P01 pp.4-5 combines stage representations, P03 pp.4-5 weights attention-derived features, and P14 p.4 concatenates multiscale features before classification. Addition and concatenation can both implement feature fusion; neither automatically implements attention, a gate or a learned alignment. Combining classifier predictions is a different level from combining their hidden features, even if both use a weighted sum. In the abstract, connect the actual outputs to their next use instead of relabeling every combination as the same module. In contributions, explain the supported advance rather than treating a more elaborate fusion name as the advance.

Do not force a rigid aggregation-versus-fusion taxonomy onto source wording. P02 p.5, Section 3.3.2 and Eq.(31), calls its weighted combination of pooled features aggregation; P03 Eq.(17) calls a related combination of different representations fusion. Their complete component names are not thereby interchangeable or multi-source general categories. P02 also calls one input max pooling in prose but defines it by an average in Eq.(28); retain that ambiguity when borrowing implementation details rather than silently choosing the more convenient word. An attributed terminology example does not certify the source's complete algorithm.

For pooling, state which axis is reduced, which axes remain and what consumes the output. P01 p.4 pools each stage's encoded features before a separate stage-fusion operation: `global` pooling within one input does not itself model whole-plant relations. Mean, maximum and covariance pooling are different computations, not stylistic alternatives (P02 p.4 uses covariance-based pooling). Symmetry of a mean/max reduction over encoded positions does not make the whole model insensitive to raw-input order; the preceding encoder may already encode that order. Describe the actual summary and its next use, without automatically claiming denoising or diagnostic improvement.

Check the averaging set and denominator. Equal averaging of unit means and a mean over all nodes differ when unit sizes differ. For a verified masked mean, exclude only the positions defined as padding or unobserved; a measured zero remains a valid value. P13 Eq.(9) averages node features before projection and activation: the readout is learned, but the displayed averaging coefficients are uniform. A later projection does not establish learned node weights. Use the [scoped pooling record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope), not a new name for every summary-to-gate or summary-to-predictor path.

For soft assignments, identify the assigned object, candidate groups/centers, normalization axis and downstream use. P33/P48 define sample-to-cluster weights, not variable-to-group weights. A normalized assignment vector is still distinct from the hard label obtained by a later argmax, and from an attention vector that merely weights a sum. Preserve a genuine soft assignment when implemented, but do not infer physical modes, fuzzy memberships or calibrated uncertainty from normalization alone. In an abstract, connect the assigned representations to their actual next operation; keep index-level details in the method unless needed to resolve ambiguity.

For `mask`, `sparse` and `constraint`, inspect where the operation acts. A zero-valued attention edge, zeroed logit, excluded class and unexecuted expert are different outcomes. Finite zeroed logits still receive positive softmax probability; ordinary dense softmax also does not establish sparse execution. Likewise, a block-diagonal graph restricts that graph operation, not necessarily later feature mixing or physical dependence between units. Keep the abstract's benefit at the level the full computation supports.

For a compression or selection claim, follow tensor sizes and the retained execution graph. P74's smaller query set changes the attention-score operation while its output still includes the other channel-value tokens; selective weighting is not proof of a smaller represented set. Zero weights may remain stored and executed densely, while actual channel removal may reduce later tensor dimensions. Neither operation alone establishes fewer required sensors or measured speed. Preserve an accurately defined removal operation rather than banning it because another source only reweights features.

A fixed parameter mask that zeros selected scalar weights can accurately be
described as unstructured weight pruning even when tensor shapes stay unchanged.
Distinguish the nonzero-weight count, allocated parameter slots, serialized bytes
and executed operations. The named operation does not establish a resource gain.
Conversely, clipping all weights to an interval changes their range, not their
membership in a retained subset. P76's background wording conflicts with the
original WGAN clipping step; its own input-gradient penalty is a third operation.
Preserve source attribution while describing the verified computation. See the
[name-admission check](engineering-application-terminology-bank.md#0-admit-names-not-search-counts)
before promoting complete names to shared recommendations.

Also record **where the modified object is used**. A masked encoder copy may
supply a training view while the original encoder supplies predictions. That
relationship can be useful without making the deployed model smaller. Do not
confuse a parameter mask with a missing-measurement mask, graph-edge removal or
channel deletion. Keep the actual training and retained prediction paths clear
in the abstract, contribution and overview, without inventing a new module name.

An exact branch conversion also depends on operations, not a shared name. P45 p.5 describes merging compatible convolution/normalization branches before a shared activation. Fixed inference normalization can be affine; input-batch-dependent normalization is a different computation. Combining affine preactivations before one activation is not generally equivalent to averaging separately activated head outputs. Check padding, shapes, biases, statistics and activation placement before asserting equality; keep P45's full conversion claims attributed rather than certifying all source formulas or a generic module family.

## Topic-Specific Terms

For **soft sensing**, name the estimated quantity and the measurements available to estimate it. In P57, `primary` and `secondary` describe target/input roles, not an importance ranking or the first and second physical sensors. A target's earlier observed values can also be inputs if released by the prediction time; a past process timestamp alone does not establish that a delayed assay was available. Distinguish training targets, historical target inputs, current estimates and future targets before polishing their names. Keep `predict` when it is an ordinary statistical verb; a forecasting claim additionally needs a future target relative to when the estimate is issued. Use the [scoped base-name record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope), not a new literal translation of every sensor name.

- **Multi-rate observation:** distinguish differences between streams from variation within one stream. Different fixed periods can coexist with noncoincident timestamps; timestamp mismatch does not require each stream to have irregular intervals. Irregular timing, multiple rates and missing entries may also coexist. Define `asynchronous` in the actual acquisition or control context rather than imposing one cross-field meaning. P08/P73 define rate groups and observed subsets; P24 explicitly models unequal sample intervals. These are related observation settings, not one interchangeable module family.

For a uniformly sampled stream, frequency `f` (observations per unit time) and period `Delta t` satisfy `f = 1 / Delta t`. A longer period means a lower frequency. For irregular observations, a declared average-frequency statistic can be useful, but does not make intervals equal; the reciprocal of mean interval and mean reciprocal interval generally differ. Check units before translating a rate-group index or interval multiplier into physical frequency. Sequence position, elapsed observation time, time since the latest measurement, assay-release delay and physical process lag denote different quantities. Use the actual timing input and its recipient, not a new time-qualified mechanism name. Holding a value on a model grid reuses a measurement rather than creating another acquisition.

- **Limited supervision:** few-shot counts labeled examples; zero-shot requires a clear unseen-class definition and available semantics; semi-supervision uses labeled and unlabeled data; weak supervision may use bags or coarse labels; self-supervision specifies how targets arise. These settings are not interchangeable. See P05-P06 and P17-P22.
- **Fuzzy models:** membership degree is not automatically a calibrated probability; define the actual membership and aggregation. A fuzzy clustering layer does not necessarily contain linguistic rules. An evidential uncertainty score is a different object unless the method establishes a connection. See P07 and P27-P29, P33.
- **Knowledge-guided models:** distinguish expert rules, process topology, physical laws and learned similarities. A prior's provenance and role matter more than the adjective. See P04, P12-P14.
- **Quality-related diagnosis:** identify the actual target: a product inspection category, a quantitative quality measurement, or a decision about whether a process fault affects quality. These support different claims. Classification of defect labels does not identify the responsible unit or fault cause. Do not require a quality-related/unrelated decomposition when the method has none; do not omit one when it defines the method's decision. See P01, P09 and P16, and [the task distinctions](topic-playbooks.md#10-interpretability-localization-root-cause-and-trust). Avoid repeating incidental defect names throughout the abstract and experiment overview.

| Direction-specific choice | Meaning to retain | Check before editing |
|---|---|---|
| conditional drift / concept drift | A change in a specified distribution, not one universal shift definition | Which of `P(X)`, `P(Y)`, `P(X|Y)` or `P(Y|X)` changes, and which is assumed stable? P30 uses a particular class-conditional definition. |
| event-triggered learning / sampling / alarm | Respectively a learning update, acquisition event or diagnostic output | What triggers what, and is the required measurement or label available then? P27 concerns learning updates. |
| generation condition / operating condition | The former may be a fault label or health indicator; the latter describes operating circumstances | Do not replace generic conditioning with operating-condition language without checking its variable. See P32. |
| diffusion step / acquisition time | Model noising/denoising iteration versus measurement time | Do not describe diffusion steps as physical temporal evolution or sensor-noise removal by default. See P32, P35. |
| reservoir state / process state | A recurrent model's internal state versus a defined process state | The reservoir in P28 is a computational object, not a physical tank. |
| slow feature / quality-related feature | Temporal variation and target relevance are separate properties | Which objective or equation relates the feature to quality? See P34. |
| filtering / smoothing | State estimation from observations up to the target time versus estimation also using later observations | Specify the estimation time and information cutoff. Training smoothing, delayed retrospective estimates and current-time predictions have different roles; P34 separates fitting from online estimation. |
| efficiency / real time | A specified resource comparison versus meeting a decision-time requirement | Identify training, generation or prediction cost and the timing boundary; parameter count does not establish latency. |
| task balancing / load balancing | Training influence across prediction tasks versus distribution of work or expert usage | P36 balances task gradients; this does not imply sparse routing or device-load balancing. |
| cross-modal alignment / synchronization | Learned representation compatibility versus paired acquisition timing | P38 separates acquisition synchronization, token construction and cross-modal attention; equal feature dimensions do not prove temporal pairing. |
| local outside-class / unknown fault | Outside one sub-classifier's label set versus unknown to the whole system | P37's pairwise OOD class does not by itself establish system-level novel-fault detection. |

### Alignment: State The Object And Criterion

Use `alignment` with the object it actually constrains, not as a synonym for fusion or recovered information.

| Intended operation | What establishes the description | What does not follow |
|---|---|---|
| Acquisition/time correspondence | Timestamp, trigger, lag or event-matching rule linking observations | Equal tensor length or embedding width alone does not pair physical events. |
| Dimensional compatibility | Projection or reshaping to a specified length/width | It need not interpolate measurements or estimate missing values; P08 p.6 maps encoded sequences to a common length. |
| Distribution alignment | A defined statistical or adversarial objective on specified feature populations, as in P10/P44 | A marginal-distribution objective does not by itself align individual pairs or preserve class meanings. Class-conditional objectives require their actual label or pseudolabel source. |
| Pair/representation agreement | A specified relation between paired or contrasted representations, as in P08 | The existence of an agreement objective is not proof of physical synchronization, causality or complete information retention. |

For MMD, name both compared distributions and whether the quantity is a training objective or evaluation statistic. Matching two marginals is not the same as measuring mutual information, which depends on a joint distribution; some dependence criteria compare a joint distribution with a product distribution, so inspect the operands rather than rejecting every possible connection. A kernel discrepancy decreasing on fixed operands supports that limited observation, not automatically more shared diagnostic information. For abstract wording, retain the actual operation and intended task role; put unsupported interpretations and needed evidence in the author note, not a string of defensive qualifications in the replacement sentence.

## Fuzzy Rule Outputs

For a predictor that combines local rule outputs using normalized activations,
trace the quantities rather than using `membership` for the entire computation:

`input representation -> membership degrees -> rule activations -> normalized rule weights -> local-output combination -> task output`

P27 Eqs.(4)-(6) uses this relationship for quality regression. P77 Eqs.(3)-(7)
combines local class scores before a class-axis softmax. The input match, product
activation, rule weight, local consequent and final class probability are
different objects. Membership values need not sum to one unless that partition
is defined; normalization across rules does not make rules fault classes.
Combining scores and then applying softmax generally differs from combining
already-softmaxed probabilities. Preserve the actual order and legitimate class
probability output without claiming empirical calibration from normalization.
Other fuzzy inference systems need their own output and aggregation definitions;
this checked path is not a mandatory architecture for every fuzzy model.

Identify the domain of the rule inputs. A learned latent coordinate can support
a numerical fuzzy predictor without a verified physical label such as high
temperature. Conversely, physically defined inputs and documented linguistic
rules can support a readable interpretation; do not ban that interpretation
merely because another model uses embeddings. State whether rules come from
experts, numerical fitting or both. Centers, widths and consequent coefficients
can be learned without input-conditioned predictions becoming online training.

In an abstract, connect the matching and rule output to the actual quality or
diagnostic decision. If a consistency loss shapes rule activations during
training, name that recipient instead of inventing another inference-time fusion
module. Keep detailed quantity checks in author notes; see the
[base-name and translation record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope).

## Evidential Classification Quantities

For the checked nonnegative-evidence, unit-prior form in P52/P75, use the actual definitions: `alpha_k = e_k + 1`, `S = sum_k alpha_k`, `b_k = e_k/S`, `u = K/S`, and expected class probability `p_k = alpha_k/S = b_k + u/K`. The belief masses sum to `1-u`; the class probabilities sum to one. `S` includes the prior contribution K, so it is not just the learned evidence sum or an acquired-sample count. A different prior or evidential regression model needs its own definitions; do not impose this form on every method with `evidential` in its name.

An input-dependent Dirichlet output is not automatically a sequential Bayesian update or online parameter learning. Equal expected class probabilities can accompany different concentration and uncertainty masses. Scaling evidence before adding the prior is not the same operation as scaling alpha; inspect the actual operands before interpreting a strength change. A smaller u therefore does not itself mean a smaller error probability, a known-class input, or a proportional increase in diagnostic reliability. Conversely, expected probabilities remain legitimate model outputs; do not ban probability language merely because belief masses and uncertainty are also present. Specify what `confidence` refers to when the distinction matters.

Connect each output to its actual consumer: a class decision may use p, while a rejection rule may use u. If the method has no rejection consumer, do not invent one. A trained head's evidence is not physical testimony or a generic feature weight, and the head alone is not a Dempster combination rule. Complete source-specific names remain attributed; the [base-name record](engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope) supports only the stated class-evidence formulation. Keep these semantic checks in author notes unless needed to define the method in prose.

In results about a defined calibration bin, report the observed frequency and confidence gap for that bin. Carry the scope in the result itself, for example, `Confidence agrees with observed accuracy in this bin, whereas the comparison model has a larger confidence-accuracy gap.` When no population-wide claim remains, put the reason for refusing such a guarantee in the author note rather than repeating it as a closing negative sentence. Retain a substantive negative finding or necessary limitation when it changes the result's interpretation.

## Reporting And Scope

`Real-world data` describes provenance, not online operation. Do not routinely prefix it with `offline`; retain the distinction if retrospective versus prospective evaluation matters. Class imbalance belongs in dataset/metric analysis when relevant. Mention it in an abstract or contribution only when it is part of the research problem or supported advance, not merely a property of one case.

`Offline assay` may accurately identify a laboratory measurement procedure or delayed quality label; it is not the same as calling every industrial dataset offline. `Online` may identify sequential computation or actual live evaluation; define which. Deployment requires operational integration, and shadow-mode evaluation does not demonstrate closed-loop benefit.

Task names also require definitions. Detection may denote an alarm, while diagnosis may identify a fault class, location or cause; published usage varies (P02). Inspect the target and evaluation before correcting a name. Quality prediction may target a continuous measurement or a quality category (P09); class labels must not be rewritten as continuous quality variables for apparent consistency.

In continuous monitoring, `window-level`, `pointwise`, `point-adjusted` and `event-level` describe distinct evaluation objects or scoring rules. A positive window does not locate the anomalous point inside it. Filling a labeled interval after one hit changes the reported score, not the emitted alarm times; P07 and P22 use different choices. `Inference time` measures a defined computation, while `detection delay` relates an actual alarm to a reference onset and required information availability. `Early warning` additionally needs a defined advance-warning target; fast computation alone supplies none of these temporal claims. See [monitoring evaluation](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when).

`Experimental settings` is a useful ordinary heading. `Evaluation protocol` is also legitimate when a reproducible evaluation procedure is genuinely being defined. An author's preference against it is not a field-wide ban.

The non-negotiable restrictions concern false meaning: fabricated results/citations, invented input semantics, unsupported causal/deployment/generalization claims, and concealed selection leakage. No ordinary word alone establishes any of these failures.
