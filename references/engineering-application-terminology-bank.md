# Engineering-Application Terminology Bank

## Scope And Evidence Boundary

This reference supports writing for industrial, control, automation, process,
manufacturing, and equipment-oriented journals. The current release provides a
[published evidence index](published-evidence.md) and
[context-sensitive decisions](terminology-decisions.md). Earlier private corpus
frequency counts are omitted because this public package cannot reproduce them.
Author drafts are not terminology authorities; computer-science channel-strategy
papers may inform a scoped method discussion, not the generic engineering bank.

A term is recommended only when its meaning matches the engineering object and
model operation. Corpus absence is not a prohibition. The tables below explain
semantic choices; they are not certification that every complete phrase has
passed the multi-source admission check. Named-mechanism recommendations follow
the evidence states below, including names already present in topic guides.

## 0. Admit Names, Not Search Counts

Before adding or recommending a mechanism, module, method, operation or processing
stage as a reusable category, classify the **complete name**:

| Status | Admission and permitted use |
|---|---|
| Multi-source general term | At least **two distinct published papers in relevant leading engineering/application journals** use the name, or semantically verified equivalents, for the same kind of object and operation. Prefer three to five when a term is new, polysemous or disputed. Record differences, not just supporting hits. This supports scoped use, not field-wide prevalence. |
| Attributed paper-specific name | A source defines its own component. Retain its exact name with attribution when discussing that paper; one paper is sufficient for that purpose, not for promoting its name to a generic family. |
| Functional description | Describe a verified action in ordinary prose, such as `a gate weights the features using the elapsed time since measurement`. This does not establish a named category. Do not disguise an unsupported capitalized module/acronym as a description to bypass the check. |
| Author-proposed name | A genuinely new component may have an author-approved name and operational definition. Label it as the current work's proposal and keep its map in that project; novelty does not require two earlier papers with the same name. |
| Pending | Evidence or semantic matching is incomplete. Do not list it as an established recommended mechanism. Keep the correct source name or a precise operational description while checking; do not invent a replacement mechanism. |

This is a shared-bank admission rule, not a demand to attach two citations to
every ordinary sentence or erase established method identities during a local
grammar pass. Use existing verified records instead of repeatedly searching the
same term. An unlisted name has **no completed admission record in this bank**;
that is not evidence that it is invalid or absent from the literature.

For each proposed entry:

1. Read the manuscript operation, input/output and scope before searching.
2. Inspect the relevant source definitions or equations. A bibliography entry,
   quoted title or isolated citation mention does not count. A paper's
   substantive explanation of an existing operation can count; it need not
   claim to invent it.
3. Deduplicate by scholarly work, not filename, website or page count. A
   preprint, journal version and mirrored copy of one work count once. Note
   shared lineage; repeated use of the same inherited paper-specific name is
   not automatically an independent general category.
4. Record exact matches separately from semantic equivalents. A shared word
   such as `fusion` does not validate every adjective added to it. Similarity
   must concern the operation and object, not merely a dictionary synonym.
5. Verify Chinese **separately** through a standards/terminology authority or
   a reliable Chinese scholarly source with an identifiable English term and
   matching definition. Record the URL and passage/section checked. Search
   snippets are leads; inaccessible bodies remain an access limitation. For
   competing translations or cross-field meanings, seek a second independent
   Chinese source. Machine translation and repetition on blogs are not evidence.
6. Record English admission and Chinese verification as separate states. When
   Chinese evidence is missing, keep the English term and a clearly descriptive
   explanation, not a claimed standard translation. A Chinese computing paper
   may establish a translation without establishing industrial-process usage.

Minimal entry: `full English name | object/operation | status | distinct source
IDs + PDF pages/sections | exact/equivalent use + differences | Chinese form +
source URL/passage + status | permitted scope | unresolved checks`.

When a source's name conflicts with its equation or the original algorithm it
cites, record the conflict and follow the actual computation before matching
names. Do not count two verbal mentions as two matching definitions. For
example, P76 p.4 calls a WGAN background step `weight pruning`, whereas the
[original WGAN algorithm](https://proceedings.mlr.press/v70/arjovsky17a/arjovsky17a.pdf),
p.4, Algorithm 1, line 7, clips weights to a fixed interval. P76's own Eq.(3)
instead penalizes an input-gradient norm. These are not three synonymous
pruning definitions. This source check does not certify either paper's complete
algorithm or a global Lipschitz guarantee.

Keep audit commentary separate from replacement prose. A method sentence should
positively state the verified computation and its use; remove unsupported
interpretations rather than routinely appending `not a probability`, `not causal`
or similar disclaimers. Explain those limits in the author note unless the
distinction itself is necessary to define the method. For an unchecked Chinese
compound name, prefer a verified base term followed by its actual input/action,
not a newly coined module label. Preserve an explicitly author-approved proposed
name, but do not present its literal translation as established terminology.

Review names across entrypoints, shared references, examples, templates, headings
and figure labels when maintaining the suite. Treat taxonomy labels as routing
descriptors, not automatically admitted technical terms. Historical executed
test prompts/responses remain unchanged evidence; their fictional module names
must not become terminology authorities. English/Chinese mirrors must retain the
same admission limits. A scan or a partial ledger does not establish that all
names have been checked.

## 1. Concept Order

When introducing an unfamiliar engineering setting, this dependency order can help:

`physical process -> measurements -> engineering structure -> model correspondence -> model operation -> evidence`

Example transition:

1. identify measured and manipulated process variables;
2. state their units, stages, rates, routes, or operating roles;
3. define one process variable as one input channel when this is the model design;
4. use channel terminology only for the subsequent model operation.

Do not let a computational term replace the engineering object before this
correspondence is defined. Once the correspondence is established, a method
paragraph can begin with its model object; do not repeat the physical background
or force every paragraph through this sequence.

## 2. High-Frequency Engineering-Language Audit

Do not audit only the terms an author happens to notice. For an authorized
full-manuscript terminology review, extract recurring content words and two-to-four-word collocations,
then review the subset that carries the engineering narrative. Three occurrences
is a useful configurable starting point, not a reason to ignore a consequential
term used once or to audit every common word.

Prioritize terms in the Abstract, Introduction, Related Work, Discussion, and
Conclusion, together with method and experiment sentences that connect:

- the industrial object and operating condition;
- process variables, stages, units, routes, and topology;
- engineering/domain/expert knowledge;
- intra-unit, inter-unit, multi-stage, or plant-wide relationships;
- model operations to engineering meaning;
- benchmark, real-world, online, and deployment evidence.

Do not spend the same effort on standard mathematical operators, activation
functions, element-wise operations, common tensor operations, method names, or
dataset labels unless they are inconsistent.

For each audited item, record:

| Field | Required decision |
|---|---|
| Manuscript frequency | Count by section and as a whole |
| External-paper coverage | Number of independent published papers using the term or collocation |
| Typical context | What engineering object or operation the sources actually describe |
| Semantic decision | retain, clarify, replace, restrict to the method section, or avoid |
| Preferred wording | An operation-specific alternative, not a mechanical synonym |
| Propagation points | Abstract, figures, equations, experiments, Conclusion, and project terminology map |

Coverage means the number within the sources actually searched, not a claim about the whole field. Report candidate-hit works separately from verified substantive uses; the index inventory is not a full-reading count or prevalence denominator. Mark unsearched usage as unchecked, not zero. Use [the corpus profile](corpus-calibration-workflow.md#4-build-a-corpus-profile) for these counting distinctions. A local grammar request does not require a whole-manuscript frequency ledger.

Verify collocations, not isolated words alone. A familiar word can still form
an unidiomatic phrase, and the correct replacement may change the whole clause.
For example, vague `information exchange` may need to become `feature
interaction`, `context aggregation`, or `cross-stage feature fusion`, depending
on the actual model operation. `Fault propagation` describes a different
claim about how a disturbance spreads in a process; it is not a stylistic
replacement for exchanging neural features.

## 3. Core Engineering Objects

| Intended meaning | Preferred terms | Use with care |
|---|---|---|
| Plant-scale system | plant-wide process, plant-wide industrial process | global system, entire network |
| Actual manufacturing route | production process, production line, production route | pipeline, workflow when the object is physical production |
| Functional division | process unit, production stage, sub-process, process block | module when referring to physical equipment |
| Recorded quantities | process variables, process measurements, measured variables, manipulated variables | channels before the model correspondence is defined |
| Operating context | operating condition; operating mode for a defined regime | domain when the meaning is only an operating condition |
| Perturbation to the process | process disturbance; load/setpoint change when that is the actual event | treating a disturbance as synonymous with the background condition |
| Physical/operational structure | process topology, material flow, equipment connection, control interaction, stage relationship | process link, structural token |

Use `channel` for the defined model-level correspondence rather than as the
default name for industrial measurements. This is a semantic distinction, not
a conclusion derived from a word-frequency ranking.

## 4. Partitioning, Grouping, And Clustering

Choose the verb from the actual source of the division.

| Operation | Preferred wording | Meaning |
|---|---|---|
| Fixed division from process design | partition variables by process unit/stage; process-informed partition | membership is known before learning |
| Engineering block construction | divide the process into blocks; group variables by unit or function | grouping follows process knowledge or equipment roles |
| Learned discrete assignment | learned grouping; hard assignment; clustering when a clustering mechanism is defined | learning an assignment alone does not establish a clustering objective |
| Graded assignment | soft grouping; soft assignment; soft clustering when defined | weights or memberships need not be calibrated probabilities |
| Combining block/stage outputs | aggregate local results; integrate stage-wise features; feature fusion | representations or decisions are combined |

Avoid using `organize/organization` as a catch-all operation. Use
`partition`, `group`, `cluster`, `aggregate`, or `integrate`
when those operations are what the method actually performs.

## 5. Feature Operations

| Model action | Candidate wording by meaning | Boundary |
|---|---|---|
| Derive features from measurements | feature extraction | do not use for the final combination step |
| Encode data in a learned space | feature representation; representation learning | name the represented object when ambiguity is possible |
| Model relationships between representations | feature interaction; variable interaction; inter-stage interaction | define the modeled relation; do not infer physical mutual influence or causality |
| Combine two or more feature sources | feature fusion; feature integration | state the sources and level of fusion |
| Combine a defined set of encoded features | feature aggregation; context aggregation when the output is context | specify operands, axis and combination; aggregation is not restricted to attention or dimensionality reduction |
| Transmit or update representations along graph edges | feature propagation; message passing | identify the graph and update; this does not establish physical fault propagation |
| A disturbance spreads through the physical process | fault propagation | requires process knowledge or evidence for the claimed direction and effect |

Name the actual operation instead of using vague `information exchange`
wording. Information exchange remains legitimate when communication or transfer
between defined entities is itself the operation.

Selecting importance need not remove a represented object. P74 p.4 explicitly preserves the patch-module output shape; p.5 Eqs.(9)-(10) uses one class query to aggregate channel values and then retains the other value tokens in the output. Keep its complete SPM/SCM/SCA names attributed. This is not a matched definition of token/channel pruning, nor evidence that fewer physical sensors are required.

## 6. Multi-Stage And Plant-Wide Relations

Use `stage-wise` for separate treatment of stages and `stage-specific` for a
property associated with one stage. Use `inter-stage` or `cross-stage` only
after the production stages have been introduced.

`Stage-level` names a granularity, such as one pooled vector per stage;
`stage-structured` asserts that an arrangement by stage is retained. Neither
is a decorative substitute for the other. A production stage, a temporal phase
of one batch, and a training stage are different objects. Likewise, `local/global`
may refer to temporal receptive fields, variable neighborhoods or plant scope:
name the referent before borrowing the phrase from another paper.

Conditional descriptions, not a list of externally established module names:

- stage-wise feature extraction;
- stage-specific process measurements;
- inter-stage relationships or correlations;
- cross-stage feature fusion;
- process-topology-guided integration;
- plant-wide feature representation.

Define the structure and time axis intended by `spatial` or `spatio-temporal`.
P11 uses spatial terminology for convolutional operations; this model usage
does not itself establish physical proximity or process coupling. Physical
layout, topology, graph neighborhoods and explicitly modeled inter-variable
structure have different meanings. Prefer `inter-variable relationships`
when that is the actual object and a spatial interpretation adds no information.

## 7. Engineering Knowledge

| Knowledge source | Preferred term | Typical use |
|---|---|---|
| Process flows, equipment relationships, control structure | process knowledge; process topology | partition, adjacency, constraints, interpretation |
| Information supplied by engineers or operators | expert knowledge | variable selection, rules, stage relations, validation |
| Broad discipline/process facts used by the model | domain knowledge | umbrella term when the source is mixed |
| Information available before the inference it informs | prior knowledge; prior matrix; structural bias | specify its source, construction and model role; not every preset quantity is knowledge |

State the knowledge source first, then name the mathematical form by which it
enters the model. P14 uses a process-informed partition, P56 models uncertain
graph information probabilistically, and P57 connects subprocess structure to
network construction. These are different uses of knowledge, not three names
for the same module.

`Prior knowledge` is broader than a `prior distribution`. A fixed topology or
normalized weight matrix is not, by itself, a probability distribution over
possible graphs or model parameters. For a Bayesian use, identify the random
object, distribution and data used to update it; do not rename ordinary learned
weights a posterior. A probability normalization constraint is also not a
physical conservation law. The Chinese wording and limited source scope are
recorded in [the knowledge audit](published-evidence.md#knowledge-entry-and-constraint-scope).

Keep knowledge-derived structure, a penalty on a stated relation, and a
constraint-satisfying construction distinct. A physical interpretation needs
the corresponding quantity or mapping, not only an industrial graph or a loss
named `physics`. See [the conditional playbook](topic-playbooks.md#6-graph-knowledge-guided-causal-or-fuzzy-modeling)
before choosing a more specific mechanism name or guarantee.

Prefer syntactically light forms:

- fusion guided by domain knowledge;
- a process-topology prior matrix;
- a stage partition constructed with expert knowledge;
- a structural bias derived from the production route.

## 8. Evaluation And Practical Claims

| Evidence | Preferred wording | Avoid overclaiming |
|---|---|---|
| Public simulator/benchmark | benchmark case study; controlled evaluation only for documented controlled factors | industrial deployment; assumed repeatability or control merely from the benchmark name |
| Production data evaluated retrospectively | real-world industrial case study; real-world production data; actual production conditions | online operation or deployment |
| Sequential or prospective evaluation | online evaluation; prospective validation, as actually implemented | a replay or streaming algorithm is not by itself a deployed system |
| Actual operational integration | deployed system; shadow-mode evaluation; closed-loop use, as tested | distinguish advisory or shadow use from actions affecting the process |

Prefer
`practical relevance` or `engineering applicability` for real-world production
data unless the manuscript demonstrates operational use. Use `offline` only
when the distinction from prospective, online, shadow-mode, or closed-loop
evaluation is analytically important; do not use it as the default label for
all production-source datasets.

For predictive uncertainty, specify the estimated quantity before choosing an
interval label. P103's output distribution used for process monitoring and
P104's quality-variable bounds support an object-to-decision contrast, not one
shared interval algorithm or new module family. Use the
[quantity distinction](terminology-decisions.md#predictive-outputs-and-intervals)
and [conditional evaluation](experiment-evidence-design.md#output-prediction-intervals).

Chinese wording was checked separately in the original
[power-load article](https://html.rhhz.net/dlgcjs/HTML/201123940.html), Section 3
and Figs.8-9: `prediction interval` / 预测区间 and `prediction interval coverage
probability` / 预测区间覆盖率. Its rendered Eq.(8) reverses the inside/outside
indicator relative to its following prose; that unresolved conflict is not
copied as a formula. This is wording evidence, not a second audited English
interval mechanism or validation of every metric/translation in that article.

## 9. Caution List

These are context restrictions, not an absolute blacklist.

| Term | Why it is risky | Prefer |
|---|---|---|
| information exchange | may hide whether the model interacts, aggregates, propagates, or fuses features | name the actual operation; keep exchange when actual exchange is defined |
| process link / known process link | ambiguous if the linked entities and relation are undefined | inter-stage relationship, equipment connection, process topology, directed edge after a graph is defined |
| organization / organize | often hides the actual operation | partition, group, cluster, structure, aggregate, integrate |
| experimental protocol | unnecessary when only settings are listed; legitimate for a defined evaluation procedure | experimental settings, data preparation, implementation details, or retain protocol for an actual procedure |
| stage representation | acceptable after the represented object is defined, but vague in engineering motivation | name a pooled stage vector or the actual variable features; do not change granularity for fluency |
| dependency | must match the modeled dependence; does not itself imply causality | specify the relation; use correlation only with an appropriate definition |
| deployment | requires actual operational integration, not only online computation | practical relevance, real-world industrial evaluation when that is the evidence |
| token / embedding / routing / adapter | model terms that can obscure the engineering problem | introduce only after the engineering object and model correspondence are clear |

## 10. Topic-Specific Expansion Structure

Extend this bank without mixing topic-specific terms into the generic core.

1. **Generic engineering layer**: process, measurements, evidence, claims.
2. **Problem layer**: incomplete or differently timed observations, limited or
   imperfect labels, changing operation, coupling, heterogeneous information,
   simultaneous faults, or actual execution/decision constraints.
3. **Method layer**: graph modeling, feature fusion, adaptation, lightweight
   modeling, diffusion, fuzzy modeling, multimodal learning, or language models.
4. **Manuscript-specific map**: exact terms for one paper, stored with that
   paper rather than in this shared reference.

New entries require external published-paper evidence and a clear semantic
boundary, following Section 0. A term copied from an author draft is not evidence
for general admission. The example families below are routing categories, not
proof that each member or compound phrase has completed that check.

Use separate sub-banks when enough external evidence has been collected:

| Layer | Example categories |
|---|---|
| Engineering challenges | missing/differently timed measurements, limited/imperfect labels, changing operation, process coupling, simultaneous faults, heterogeneous information, resource/decision constraints |
| Object/scale | variables, equipment, production stages, multiblock or plant-wide processes; state the actual structural difficulty separately |
| Engineering tasks | fault detection, fault diagnosis, process monitoring, quality prediction, remaining-life estimation, control, optimization, decision support |
| Task-specific outputs | anomaly localization, fault isolation, supported root-cause explanation; distinguish location from cause |
| Supervision and training signals | supervised, semi-supervised, weakly supervised and unsupervised settings; self-generated learning targets, with stage-specific label use and possible overlap |
| Method families | feature fusion, graph modeling, attention, transfer/adaptation, lightweight modeling, diffusion, fuzzy modeling, multimodal learning, language models |
| Evidence profiles | analytical, benchmark, production-data, prospective/shadow, deployed or external evaluation; combine actual available evidence |
| Manuscript archetypes | method-with-application, background-driven application, or system/decision work; not an evidence level |

Use the [problem-first vocabulary and annotation profile](problem-first-classification.md)
before adding problem sub-banks. A folder labeled weak supervision indicates an
annotation limitation to investigate; self-supervision describes target construction.
Neither alone specifies the task or proves an exclusive supervision class.

Keep the generic core stable. A topic-specific entry must state both the
engineering problem it names and the method/evidence context in which it is
appropriate.

## 11. Checked Core Names And Remaining Scope

Targeted definition checks recorded on 2026-10-24 and 2026-10-25 support the following **English base
terms**, not all modified module names containing them. P IDs and PDF page
positions refer to the [published index](published-evidence.md). These are
original semantic summaries, not extracted source passages.

| Base term | Checked distinct papers and operation | Boundary |
|---|---|---|
| hypergraph; hyperedge | P96 p.3, Section 2.2, defines node membership in hyperedges; P105 author manuscript Section III defines equipment-node sets joined by hyperedges and a node-by-hyperedge matrix. | Two distinct ESWA/TIM works support set-valued grouping, not the same node identity, physical mechanism or complete proposed module. Ordinary pairwise projection does not retain all membership information. |
| hypergraph convolution (normalized node-edge-node base operation) | P96 p.3 Eq.(2), p.5 Section 3.3/Eq.(6); P105 author manuscript Section IV-B, Eqs.(5)-(8), defines degree-based node-edge-node feature propagation. | Matched base operation, not identical implementations: sample neighborhoods with uniform weights versus equipment construction and trainable weights. P105's signed matrix/degree interface and complete Res-HGCN remain outside this check. Do not infer universal superiority over weighted graphs, physical causality or online parameter learning. |
| counterfactual generation (classifier-targeted input form checked) | P62 p.5, Section 3.1/Fig.3, conditions changed inputs on a desired class and checks them with the diagnostic model; p.7 retains generated explanations. P94 pp.4-5, Section 3.2/Fig.5, perturbs selected inputs toward target fault classes for augmentation. | Two distinct ESWA/CCE works support the scoped input-to-target operation, not a shared full architecture or prediction interface. Model target agreement differs from true fault identity, physical feasibility and actionable control. Source-specific constraints, causal interpretations, necessity/sufficiency quantities and performance claims are not certified. |
| class weighting (classification log-loss factor; placement checked) | P96 p.3, Eqs.(3)-(4), and P100 author accepted manuscript, Section II-B, Eq.(9), apply category factors to classification log-loss terms. | Matched factor placement, not identical whole losses. P100 adds a prediction-dependent batch factor and has an unresolved coefficient map. Ordinary weighted-CE and full adaptive-loss names are not admitted by this narrower record. |
| domain generalization (DG; source-only development to unseen-domain prediction) | P50 p.2, introduction and Section II-A, defines source-data training without target access; pp.3,6 specify source training and unseen-domain testing. P99 p.4, Section II-B3, defines learning on available domains for unseen distributions; p.7 Algorithm 1 and Section V-A separate source training/selection from testing. | Two distinct TCYB machinery works support this learning/evaluation setting, not one perturbation, invariance or causal mechanism. Both inspected implementations use multiple sources; their source counts are not a universal minimum. Ordinary measurement input at prediction is permitted; target-pool statistic fitting is a different access profile. New operating conditions need not introduce new fault classes. Full DGNSU/Lifeisgood mechanisms, the latter's theoretical guarantees, P50's unresolved style-symbol interface and complete results are not certified. |
| remaining useful life (RUL) prediction / estimation | P45 p.6, Section IV-A, constructs window-linked life labels from run-to-failure trajectories and imposes a maximum RUL; P81 p.3, Section III-A, defines measurement-to-RUL regression, with p.6 specifying its engine life labels and separate TTF application. | Two distinct published works support estimating remaining life to a defined endpoint, not a mandatory network, cap or sampling clock. Their engine examples share a benchmark convention; this is not independent invention or evidence that every future-variable forecast estimates RUL. Full MDER/DATCN names, label-index details, normalization and performance claims remain unverified by this target check. |
| active learning (annotation-acquisition setting checked) | P89 p.3, Section II-B, selects batches from an unlabeled pool for expert labels and updates the classifier; P90 pp.4-5, Section 3.1/Fig.4/Table 1, defines the corresponding selection, labeling and refitting loop for chemical-process classification; P91 p.4, Section II-B, connects queried expert labels to classifier retraining for compound faults. | Three distinct published works support label acquisition for learning, not one query criterion, budget unit or predictor architecture. P89/P91 share authors and a research line; P90 is a different process study. Training-pool query labels are not held-out evaluation labels or model-generated targets. A specified excitation-based diagnosis design is a different use of active. Full MCAL/DGMR/E-ECos names, source pseudocode details, annotation savings and field deployment are not certified by this base record. |
| soft thresholding / soft-threshold function (nonnegative-threshold form) | P87 p.3, Eq.(4), defines zero output inside the threshold interval and signed magnitude reduction outside it; P88 p.3, Section III-B1/Eq.(2), defines the same base map before a source-specific joint-filter design. | Two distinct TSMC/TIM works support this operation in process and adjacent machinery diagnosis, not independent invention or complete AST/JTM/AM-MAST names. A feature channel need not be a measured variable. Zeros in feature values are not network-parameter pruning or evidence of sparse execution. Threshold generation and subsequent bypass/fusion differ; P88's printed sigmoid expressions conflict with their stated range and are not adopted. Neither small amplitude nor this map alone identifies noise or certifies denoising quality. |
| network pruning / DNN model pruning (parameter-selection setting checked) | P85 p.4, Section III-A2, selects low-magnitude coefficients/kernels for zeroing and then retrains model instances; P86 pp.3-4, Section II-B1 and III/Fig.2, explains parameter removal and retraining, with pp.4-5 specifying its own retained-index design. | Two distinct published engineering works match selection of network parameters/connections, with different criteria and purposes. P85 is an IIoT-service study; P86 is adjacent sparse-hardware research, not another process-diagnosis implementation. This base record does not admit all channel/token/graph pruning variants, full JOPA/LGPS names, or a universal sparsity-to-latency ratio. Zero masks can retain dense arrays and execution; check the retained graph, representation and actual runtime claim. |
| Dempster's rule of combination (normalized conjunctive rule) | P49 p.3, Eqs.(6)-(7), defines intersection-product combination and conflict normalization; P84 p.8, Eqs.(8)-(11), defines the corresponding mass functions, combination and conflict in a circuit-breaker context. | Two distinct engineering-journal works support this base operation through substantive theoretical definitions. P49's implemented feature-weighted sum, pp.5-6, is different; P84's full IDS-ESN design remains attributed. The record does not establish two implementations of the unmodified rule, industrial-process prevalence, calibrated reliability, or independent evidence merely from separate learned heads. Define the frame, mass construction, conflict handling and actual decision conversion; K=1 is outside the normalized formula. |
| multirate / multi-rate observation (rate-group settings checked) | P34 pp.4-5, Section III-C and Eqs.(37)-(48), separates process/quality rate groups and acquired/estimated entries; P73 p.3, Section III-A/Fig.1 and Eqs.(2)-(3), defines rate-dependent observed subsets. P08 p.3, Section III-A, supplies an additional rate-group definition in a time-series setting. | Two distinct TII/TSMC process studies and an additional TKDE context support observations at multiple rates, not one alignment or imputation mechanism. The checked schedules do not make all multirate systems synchronous, irregular or restricted to a particular integer-ratio convention. P08's rate/period ordering needs unit checking. P24's unequal within-sequence intervals are a related but different timing property; full proposed network names remain attributed. |
| root cause identification / root cause recognition (task labels, not one mechanism) | P13 pp.4-5 defines a graph-based search returning a unit and then a variable; pp.7-8 distinguishes recovered relation scores from root-location results. P16 pp.6,10 uses abnormal-link annotations and process interpretation after detection to recognize origin variables. | Two distinct process studies use these labels for origin-location tasks through different rules. This is not a paired definition of one causal-learning, cascade or automatic-ranking mechanism, nor proof of physical effects. Preserve the defined reference origin, output level and source-specific name; a fault-class label or earliest responding sensor is not automatically that origin. |
| soft sensing / soft sensor modeling; inferential sensor modeling (scoped equivalent) | P34 p.1 describes estimating hard-to-measure quality from available process variables; P57 pp.1-2, Section 2.1 and Eq.(1), defines a predictor from secondary measurements and target history to a key variable. P56 pp.1-2 defines the corresponding quality-inference task under the inferential-sensor name. | Three distinct process studies support model-based indirect estimation, with different structures, targets and information access. P34/P57 explicitly use soft-sensing names; P56 is a checked semantic equivalent, not a second literal match of every name. This is not compliant-material sensor hardware, proof of online deployment, or automatic fault identification. Current-target estimation and future forecasting require their actual target/issue times. Full network names and every virtual-sensing synonym remain outside this base admission record. |
| few-shot learning (FSL) | P47 pp.2-3, Section II-C/D, and p.5, Section IV-A, uses abundant labeled base measurements and a limited labeled support set; P69 pp.2-3, Sections 1-2, and pp.8-9, Section 4.1, trains with a small fixed labeled set and augmented views. | Two distinct adjacent engineering studies support the limited-example setting, not one algorithm. State the shot unit, affected classes and stage-specific label access. Neither episodic meta-learning, unseen classes nor a universal sample cutoff follows from the base name. Support counts do not establish total annotation savings; augmentation does not create independent measured labels. Full L2MP/SSFN component names remain attributed. |
| zero-shot learning (ZSL) / zero-shot fault diagnosis (class-semantic setting checked) | P05 pp.3-4, Section 3, defines disjoint seen/unseen classes with given class semantics; P06 pp.2-3, Section II-A, maps measurements to known fault attributes; P80 pp.2-3, Section II-A/III, and p.6, Section III-C, generates unseen-class features for classifier training. | Three distinct published works support diagnosis of classes lacking labeled real training measurements, with class descriptions available. P05/P06 share author/research lineage; P80 supplies a different team's generative design. Semantics, generated feature labels and declared unlabeled target access do not equal acquired labeled unseen-class measurements. Matching and feature generation are different prediction/training paths; zero-shot does not mean the entire learning history lacks supervision. Define the candidate label space and actual retained predictor. Full hierarchical, generative and test-time component names remain attributed. |
| multi-instance learning (MIL) | P22 pp.3-4, Section III-B and Eqs.(1)-(3), relates instance representations, bag aggregation and bag labels; Section IV-A extends the instance set to temporal subsequences. P68 p.3, Section III, defines bags of instances in its MIML formulation, and pp.4-5, Section IV-B, constructs/aggregates latent feature instances. | Two distinct engineering works support the bag-of-instances learning basis, with different members, label spaces and final outputs. P68 is an adjacent bearing study; its MIML input definition supports this base record, not complete MIML/LWMIML-name admission or verified compound-fault prediction. Internal instance counts are not independent acquisition counts; a collective anomaly need not be detectable from one time point alone. |
| semisupervised / semi-supervised learning | P17 p.2, Section II, defines measured/unmeasured concentration targets and pp.3-4 combines labeled/unlabeled training; P21 p.3, Section III-A, defines labeled and unlabeled batches with supervised and self-supervised learning. P26 pp.3-4 independently defines labeled class targets and unlabeled transformation tasks. | Three distinct works support learning from both task-labeled and task-unlabeled examples, with different outputs and training designs. Neither class-disjoint testing, pseudo-labeling nor a separate pretraining phase is required by the base name. The record concerns these stated settings, not every detection-community use of the label. |
| self-supervised learning | P21 pp.3-5, Sections III-A/C, constructs temporal cross-prediction targets from transformed unlabeled views; P26 pp.3-4, Sections III-A/C, predicts the identity of a deliberately applied sampling transformation. | Two distinct works define self-generated training signals with different prediction objects. Neither target is an observed fault annotation. Self-supervision may be jointly trained with a supervised task; it is not synonymous with contrastive learning, a compulsory pretraining phase or a label-free complete pipeline. P26 is adjacent time-series/equipment evidence, not an additional process-industry prevalence claim. |
| autoencoder (AE) | P66 pp.2-3, Section II-A and Eq.(1), defines an encoder, latent representation, decoder and reconstruction objective; P67 p.3, Section 2.1 and Eqs.(1)-(2), defines the same base input-to-latent-to-reconstruction structure. | Two distinct industrial works support the base architecture, not every full AE module name. P66 pp.5-6 uses equal token dimensions, label-dependent objectives and encoder/classifier inference; P67 pp.3-4 uses a latent-space monitoring statistic. Neither dimensional reduction, an entirely unsupervised pipeline, synthetic-data augmentation nor residual-based decisions are universal requirements. |
| generative adversarial network (GAN) | P71 p.2, Section 2.1, Fig.1 and Eq.(1), defines random-input conditional generation against real/generated discrimination; P72 pp.3-4, Sections 2.2/3.2 and Fig.2, defines the corresponding sample generator/discriminator roles before augmentation in Algorithm 1 p.5. | Two distinct engineering works, one process and one adjacent machinery study, support sample synthesis through generator and discriminator training, not every complete conditional/regularized module name or source formula. These generated data are not automatically inputs crafted to induce diagnostic errors. P70 pp.3-4 instead uses a measurement-to-feature generator and a source/target discriminator; preserve its attributed name without treating it as another matched sample-generation definition. A discriminator need not be the diagnostic classifier, generation need not run at every prediction, and trained adversaries do not alone prove fidelity, equilibrium or physical validity. |
| variational autoencoder (VAE) | P17 pp.3-4, Section III-A and Eqs.(3)-(11), connects a Gaussian latent distribution and reconstruction/prediction objectives with variational/KL terms; P64 p.2, Section 2.1 and Eqs.(1)-(2), explicitly defines prior, approximate posterior, decoder likelihood, ELBO and Gaussian reparameterization. | Shared probabilistic latent-model basis, not identical supervision or task. P17's variance-versus-sampling notation and conditional-posterior account need reconciliation before reproducing its formulas. A Gaussian sample alone does not establish a VAE; latent variance does not establish calibrated output uncertainty or actual sample augmentation. |
| evidential neural network / evidential deep learning (checked Dirichlet classification form) | P52 pp.2-3, Section II-B/C and Section III-A/Algorithm 1, maps nonnegative class evidence to Dirichlet parameters, expected class probabilities and uncertainty; P75 p.3, Section II, Eqs.(1)-(8), defines the same base quantities before its classifier. | Two distinct published works with overlapping authors and close EVGG lineage support this scoped formulation, not independent invention or all evidential methods. Belief masses and expected class probabilities differ. Full EVGG/risk-calibrated component names stay attributed; neither the base name nor a smaller uncertainty mass proves calibration, unknown-fault detection or physical reliability. |
| feature extraction | P01 p.4 constructs multiscale features from stage measurements; P14 p.3 constructs temporal features through convolution. | Extracting representations is not selecting an existing subset or combining final decisions. |
| state-space model (linear Gaussian latent form checked) | P34 pp.2-3, Eqs.(1)-(12), connects latent-state transitions to process/quality observations with Gaussian noise; P73 pp.2-4, Eqs.(1),(3),(8)-(9), defines autoregressive latent dynamics and an augmented first-order observation/state form with Gaussian terms. | Two distinct process-industry works support the transition/observation structure in this scope, not all nonlinear or neural sequence variants. Model states can be statistical latent coordinates, not necessarily measured physical quantities. High-order augmentation, rate-specific static factors and full proposed model names remain distinct. |
| Kalman filter / Kalman filtering | P34 pp.3-4, Eqs.(19)-(25), predicts latent moments and corrects them using observations; P73 p.4, Eqs.(10)-(14), explicitly separates state/covariance prediction and observation-based correction, followed by smoothing for training. | Two distinct process studies support recursive estimation in their linear Gaussian model settings, not identical multirate implementations. Updating state estimates or gains is not automatically parameter learning; covariance is not a calibrated fault probability. Backward training smoothing, current filtering and a delayed retrospective estimate have different information horizons. Source indices, full variants and all formula/guarantee claims are not certified by this role check. |
| multiscale / multi-scale convolution | P11 pp.3-4, Section III-A, Eq.(15) and Fig.2, concatenates parallel different-kernel outputs; P15 pp.4-5, Section III-A, Eq.(10) and Fig.3, also concatenates different-kernel branch outputs; P01 p.4, Section 3.3.1, Eqs.(1)-(2) and Fig.2, adds parallel outputs built with different temporal/variable-axis kernel extents. | Three distinct process-diagnosis works support extraction over differing convolutional supports, with P11/P15 sharing an author and research lineage. Addition and concatenation differ; kernel orientation and the modeled axis must be checked, not inferred from the base name. This record does not certify full MRCC/MRCNN/MSFE names as general families, frequency-band isolation, physical time constants or proven benefits. |
| feature selection (explicit subset operation) | P40 pp.3-4, Section III-B and Algorithm 1, removes low-ranked descriptors and returns feature indices; P61 pp.3-4, Eq.(5), and p.6, Step 3, ranks and recursively removes process-variable inputs. | Two distinct journal works support subset selection, with different input objects and ranking criteria. P62 p.4, Section 2.1, instead defines an attributed `feature-selection layer` through trainable input weights; its p.5, Section 3.1, uses those weights for ranking. Preserve that local name without inferring a reduced subset, fewer sensors, calibrated relevance or physical causes. |
| incremental learning | P30 p.4, Eqs.(10)-(13), updates classifier weights after labeled examples; P63 pp.3-5, Sections II/III and Algorithm 1, updates a subspace and classifier as sensory inputs evolve, with classifier learning requiring labels. | Matched base sense of updating an existing learner with new information, different update objects and information conditions. It does not require new classes or establish one universal predict/update order; preserve the source-specific training and out-of-sample distinction. |
| continual learning | P64 p.3, Section 2.2, and pp.5-6, Section 3.3/Algorithm 1, learn new operating conditions while addressing earlier-condition retention; P65 pp.3-6, Section III-A/D/F, adapts to successive unlabeled target domains while constraining loss of earlier knowledge. | Two distinct industrial works support the sequential learning/retention purpose, not identical supervision or memory. P64 uses a feature buffer; P65 retains source data and earlier model information without replaying old target instances. A method can be evaluated for continual learning even when retention is imperfect. |
| feature fusion | P01 pp.4-5, Section 3.4 and Eqs.(7)-(10), combines stage features using topology and similarity matrices, then adds the two outputs; P03 pp.4-5, Section 2.3.2 and Eq.(17), combines two attention-derived representations by learned weighting; P14 p.4, Section III-D4 and Eq.(35), concatenates multiscale convolution outputs before classification. | Three distinct works, including two related team papers, support the base feature-combination term, not one universal operator. P14's block-diagonal graph assembly in Eq.(28) is a different operation. Neither the shared base word nor these definitions establish a generic `causal`, `reliable` or topology-qualified module family. |
| attention mechanism / self-attention | P11 p.3 and P24 p.3 define query/key/value weighting with the self-attention inputs drawn from the same representation. | The checked common operation does not make all source-specific attention variants equivalent, causal or physically interpretable. |
| multi-head attention / multihead self-attention (projected self-attention form checked) | P11 p.3, Eqs.(3)-(4), defines separately projected attention heads whose feature outputs are concatenated and mapped by an output matrix; P82 p.4, Eq.(4) and Fig.5, defines parallel projected self-attention, with concatenation/output projection on the prediction path and a separate pooling path for coefficient matrices. | Two distinct process studies support this scoped form, not independent invention or all qualified attention names. Head count is not sensor count, class count or evidence of statistically independent physical relations. A head's normalized coefficients and its weighted features are different objects; concatenation plus projection is not generally their mean. P24 p.3 supplies self-attention and Transformer context, not a third inspected head-merger definition. Full MRCC-Transformer/MTCMS names and P82's physical-causality claims remain attributed. |
| gating mechanism (feature-modulation forms checked) | P08 pp.5-6, Eqs.(7)-(9), explicitly gates convolution features with a sigmoid branch; P19 p.5, Eqs.(9)-(11), explicitly derives sigmoid scale weights from pooled features, multiplies the features and adds a residual path; P33 p.6, Eqs.(23)-(24), explicitly gates attention outputs before concatenation. P36 pp.2-3, Eqs.(2)-(6), additionally defines gating networks for expert mixtures. | Three distinct published works explicitly name and define feature gates; P36 supplies a related expert-weighting context, not another identical gate. Targets, axes, normalization and bypass paths differ. P33 is general incomplete-series evidence, not process-industry prevalence. Attention and gating descriptions can overlap, as in P19. A bounded gate need not remove a variable, suppress the final residual output, denote a fault probability or skip branch computation. Full qualified names, including time/age-qualified ones, need their own admission record. |
| Takagi-Sugeno-Kang (TSK) fuzzy rule model / classifier (first-order form checked) | P77 p.5, Eq.(8), substantively defines the first-order rule; P108 p.2, Section II-A/Eqs.(1),(3)-(6), defines affine local class scores and normalized rule combination. | Two different-team TFS works support this scoped rule computation, not identical complete classifiers. P77's background rule is separate from its proposed CNFS. Gaussian membership alone does not establish a full TSK name; neither a fixed rule count, class softmax nor a particular optimizer is universal. Affine local consequents do not make the complete input-output map affine. |
| Gaussian membership function | P27 p.3, Section III-A, Eq.(4), defines products of Gaussian input matches; p.4, Eqs.(5)-(6), normalizes them for quality prediction. P77 p.5, Section III-B, Eq.(3), defines Gaussian matches for modality descriptors before rule combination. | Two distinct TFS works by different teams support the base matching function. Latent features versus constructed indicators, regression versus classification and subsequent consumers differ. A Gaussian-shaped membership function is not by itself a Gaussian data likelihood or an identified operating regime; complete neuro-fuzzy system names remain attributed. |
| source-free domain adaptation (model-access, unlabeled-target setting checked) | P78 pp.2-3, Section III, and p.5 Algorithm 1 separates labeled source pretraining from target adaptation without source samples; P79 author version p.6, Section 3.1, and pp.8-9, Section 3.4, defines the corresponding two-stage setting. | Two distinct process/machinery works support the adaptation-stage source-data restriction. The retained model still supplies learned knowledge. P78 updates selected encoder/classifier parameters; P79 fixes its classifier while adapting the encoder. Target-label access, label-space relations and timing need separate definitions; neither classifier freezing, zero-shot classes, an online stream nor formal privacy follows from the base name. Full TASFA/universal variants remain attributed. |
| test-time adaptation / test-time adjustment (target-informed prediction-stage forms checked) | P05 p.7, Algorithm 1/Section 4.3, adjusts semantic references from target predictions; P83 author v2, Section 4.2/Algorithm 1, separates target-side corrector fitting from test-time statistic updates. | Two distinct process works support the scoped role, with P05 a checked adjustment equivalent rather than a second literal TTA-name match. Weights, references and statistics are different changing objects. State target access, normal-data assumptions and prediction order; backpropagation, source-free access and zero-delay streaming are not universal requirements or guarantees. Full proposed names and final-version formula identity remain outside this record. |
| residual connection (additive network path checked) | P11 p.3, Section II-B3 Eqs.(6)-(7) and Section III-A Eqs.(11)-(13), adds an input to a learned transform; P15 p.4, Section II-B Eqs.(5)-(7) and Section III-A Eq.(9), defines identity and dimension-matching linear paths; P14 p.2, Section II-A Eq.(5), and p.3, Section III-B Eq.(14), adds the input to convolution outputs. | P14 explicitly names residual connections; P11/P15 supply checked residual-learning/block equivalents, not three asserted literal matches. These are three distinct process works with shared P11/P15 author lineage. A dimension-matching linear path is valid and need not be identity; activation/normalization order differs. P02 p.3 supplies backbone-usage context, not another explicit addition definition. Parallel branches or concatenation do not establish this additive operation; preserve an author-proposed name with its actual definition. Addition, projection or a title alone does not prove lossless retention, physical residual decomposition or improved generalization. |
| message passing (graph-neighborhood feature updates checked) | P13 p.2, Section II-B Eqs.(7)-(8), and p.4, Section III-C Eqs.(18),(21), combines node and adjacency-aggregated features; p.3 explicitly calls this message passing. P14 p.4, Section III-D2-3 and Eqs.(33)-(34), explicitly describes GCN message passing and defines adjacency-weighted feature updates. | Two distinct TSMC process studies by different teams support this base graph computation, not one identical layer or every qualified module name. P13's subsequent graph-level readout, Eqs.(9),(19), has a different output role. Check node identities, matrix orientation, normalization and downstream use; this record does not certify source indexing conventions, causal identification, physical fault propagation or communication-network traffic. |
| fuzzy clustering; fuzzy c-means (FCM) | P28 p.3, Eqs.(4)-(7) and Algorithm 1, uses membership-weighted distances and alternating center/membership updates; P33 pp.3-4, Section III-C and Eqs.(5)-(6), defines FCM before its clustering architecture. | Same base clustering algorithm, different roles: reservoir-feature reinforcement versus incomplete-series clustering. The sources are machinery and general time-series studies. Their full network names, reinforcement steps and imputation mechanisms are not interchangeable. |
| diffusion model | P32 p.3, Section III-A, defines artificial forward noising and learned reverse generation for sequences; P35 p.3, Section III-A and Eq.(14), applies conditional diffusion to compressed features and decodes generated signals. | Common generative operation, different generated objects and conditioning. This does not establish sensor-noise restoration, identical inference cost or a universal industrial diffusion-module name. |
| graph convolution; graph convolutional network (GCN) | P07 p.7, Eqs.(18)-(19), combines normalized adjacency, feature projections and a gated nonlinearity; P14 p.4, Eqs.(33)-(34), uses adjacency-weighted feature projection and ReLU. | Common graph-feature computation, not identical graphs: variable-time nodes versus process-variable nodes. A GCN operation does not establish a physical or causal meaning for learned edges. |
| cross-attention | P38 p.6, Eq.(7), uses queries from one modality and keys/values from the other; P43 pp.4-5, Eqs.(1)-(2) and Figs.6-7, uses queries from one encoder scale and keys/values from concatenated scales. | Same query-to-key/value weighting principle, different representations and attention axes. Distinct modalities are not required; key/value features may include the queried scale. P42 p.4 defines cross-time and cross-variable **self-attention** despite its dual-cross-attention title. That title is not a second definition of the P38/P43 operation. Preserve attributed names, but inspect inputs before classifying a new module. |
| mixture of experts (MoE) | P36 pp.2-3, Eq.(2) and Eqs.(5)-(6), defines gated combinations of expert outputs and task-specific expert features; P41 pp.2-3, Eqs.(1)-(3), defines weighted expert predictions with input-dependent gates. | Shared mixture principle, not identical experts or outputs. P41 uses linear expert models, so `neural network` is not part of the base definition. Coefficient sparsity from regularization does not establish sparse expert execution, and a gate need not select one discrete operating mode. |
| domain adaptation | P10 pp.4-5 defines labeled-source/unlabeled-target learning with identical class spaces and local/global distribution losses; P44 pp.2,4-6 defines multiple source-target branches, distribution losses and prediction combination with a target class space contained in the source space. | Both address transfer across domain distributions, but label-space relations and label access differ. P44 Eq.(15) and Algorithm I explicitly contain target-label symbols; do not label its setting unsupervised from its title. An alignment objective and prediction fusion are distinct operations. |
| knowledge distillation (KD) | P45 pp.3-5 trains student heads to match teacher hidden features and regression targets; P46 pp.3,5-6 transfers multisensor-model guidance to single-sensor predictions through softened-output and semantic-similarity losses. | Teacher-guided learning is shared; task, transferred objects and sensor access differ. Classification probabilities, identical architectures and model compression are not universal requirements. P46's prose about unnormalized scores conflicts with the displayed softmax/temperature definition in Eq.(6); that specific claim is excluded. These adjacent equipment studies support the base method, not every named distillation variant or process-industry prevalence. |
| class prototype | P46 pp.5-6, Eqs.(7)-(10), computes class-conditioned feature means used in a similarity-transfer objective; P47 p.3, Eq.(4), computes labeled-support feature means consumed by query matching on pp.3-4. | Checked common sense: a feature-space class representative. Its downstream role, source samples and update rule must be stated. It is not automatically a physical state, independently optimized parameter or learned cluster; this record does not require every prototype method to use a mean or one vector per class. The motor and smart-grid contexts do not establish process-industry prevalence or a universal prototype-module name. |
| max pooling | P11 p.2, Eq.(2), takes the maximum in a feature-map region; P15 p.5, Eq.(12), takes the maximum in a specified convolutional-output window. | Same regional reduction, not certification of every pooling variant. State the reduced and retained axes. A maximum activation is not automatically a fault-relevant feature or evidence of noise robustness. |
| causal convolution (time-indexed sequence filtering) | P81 p.3, Section III-B/Eq.(1), explicitly restricts the filter to present and dilated historical positions; P82 p.3, Section 3.1/Fig.3, explains causal temporal feature extraction over the history before separate relationship learning. | Two distinct published industrial works define the base operation. The P82 phrase spans a typographic line break; it is not merely a causal-graph title hit. Current-position access can be causal; strictly past-only prediction needs the actual lag/target convention. Dilation changes tap spacing on the model grid, not the sensor acquisition rate. A later operation can change the complete path's time access, and this layer alone does not identify physical causes. Full DATCN/MTCMS or other qualified fusion names remain attributed; source-wide formulas and causal guarantees are not certified. |
| average pooling / mean pooling; global average pooling (GAP), scoped feature reductions | P19 p.5, Eq.(7), explicitly defines GAP as the mean over a scale-specific feature vector, which supplies a gate; P01 p.4, Section 3.3.2 and Eq.(3), explicitly uses GAP to obtain each stage's summary before separate stage fusion. P13 p.3, Eq.(9), defines mean pooling over node embeddings followed by a projection/activation; p.4, Eq.(19), uses the readout for interunit modeling. | Three distinct published works support feature averaging, with two explicit GAP uses and a related mean-pooling definition, not one identical axis or readout. P01's operator-level equation does not independently specify every implementation axis. In P19 the original feature vector also survives through a bypass; P13's learned readout includes a uniform mean. Global refers to the stated reduction set, not automatically the whole plant, sensor removal or a learned relationship. Full qualified pooling/fusion names and guaranteed information retention remain outside this record. |
| soft assignment (to clusters) | P48 p.5, Section II-A and Eqs.(1)-(3), explicitly defines graded sample-to-centroid assignments; P33 p.3, Section III-B and Eqs.(1)-(3), substantively defines the corresponding normalized Student-t cluster-assignment operation in its DEC preliminaries. | P48 is an exact name match; P33 is a checked semantic equivalent, not a literal-phrase hit. Both inherit DEC-related machinery, so they support the base operation, not independent invention or a universal module name. These sample-level assignments do not establish variable grouping, fuzzy-set semantics or calibrated physical-mode probabilities in another model. |
| contrastive learning | P20 p.6, Section III-D and Eqs.(18)-(21), scores node features against graph summaries with constructed positive/negative examples; P21 pp.4-5, Section III-C and Eqs.(4)-(6), contrasts temporal contexts with later latent features across augmented views. | Both explicitly name and define contrastive learning, but contrast different objects. Positive/negative denotes the training relation, not necessarily normal/faulty or same/different diagnosed classes. Neither pair construction is mandatory for the whole family, and their full module names remain source-specific. |
| pseudo-label / pseudolabel | P18 p.5, Eq.(10), generates a hard class target from adjusted classifier outputs; P21 p.5, Section III-D and Eq.(7), uses estimated class distributions to construct a pseudolabel graph over samples. | Same base sense of model-derived class guidance, different forms and consumers: hard targets versus distribution-derived sample relations. Preserve this distinction. These are not observed annotations, automatically calibrated probabilities, or verified physical process relations. |
| energy function / free energy (classifier-logit score) | P18 p.3, Eq.(4), calls its temperature-scaled negative log-sum-exp quantity `free energy`; P51 p.5, Eq.(18), calls the corresponding unit-temperature computation an `energy function`. | Checked equivalent computation under the stated logit convention, different names and consumers: domain-learning operations versus open-set decisions. Preserve source-specific notation. This is neither physical signal energy nor graph-Laplacian energy, and does not calibrate a probability, admit the full `graph-energy` name or validate P51's disputed threshold. Chinese function/score wording and the separately corroborated free-energy wording have different source types and limits below. |
| open-set recognition | P51 pp.5-6 defines known-class classification and unknown rejection; P52 accepted-version p.2, Section II-A, defines training known classes and test inputs including new classes. | Matched task sense with different scoring mechanisms. Unknown rejection is not identification of an unseen fault type; new operating conditions do not alone establish new label classes. No universal threshold or uncertainty mechanism follows. |
| missing-value imputation; data imputation | P106 IEEE early-access PDF p.5, Section III-B/Eqs.(16)-(19), estimates unavailable industrial measurements for possible downstream use; P107 published PDF pp.3-4, Sections II-B/III-A/Eqs.(4)-(8), defines missing-position estimation and composition. These add two process-data contexts to the existing P25 p.4/P33 p.5 base record. | Matched estimation task, not a shared full model or fitting profile. P106 uses observed=1; P107 uses missing=1. Prefill, reconstruction targets, delivered completion and downstream quality outputs differ. Full MSST-Former/AM-DAE and empirical results are not certified. P25's preservation ambiguity remains; P33 is still adjacent general time-series evidence. |
| reconstruction loss | P17 pp.4-5, Eqs.(6), (14), compares reconstructed inputs with input targets alongside concentration prediction; P33 p.6, Eq.(18), compares decoded sequences with observations using a mask. | Shared reconstruction objective, not a universal norm, denominator or scoring subset. State the target, mask and reduction actually used. Reconstruction may regularize a predictor without producing completed measurements at inference; a lower training loss does not measure unknown physical values. |
| distribution alignment | P10 pp.5-6, Eqs.(15)-(17), reduces source/target feature-distribution discrepancy through a training objective; P44 pp.4-5, Eqs.(12)-(15), uses domain-adversarial and class-weighted distribution objectives. | Common distribution-matching purpose, different criteria, feature sets and supervision. Not timestamp synchronization, sample pairing or proof of retained fault semantics. Distinguish a marginal from a class-conditional target and measured reduction from an optimization aim. |
| maximum mean discrepancy (MMD) | P10 p.5, Eq.(15), defines a kernel mean-embedding discrepancy for source/target features; P32 p.4, Eqs.(10)-(11), defines a kernel discrepancy between sampled noise and predicted noise within diffusion training. | Same base discrepancy, different operands and loss roles. P32's full Ada-MMD name and mutual-information wording do not follow from the base definition. P44's introductory mention alone is not a third operational definition. Check the actual estimator, kernel and aggregation before reproducing a formula. |
| slow feature analysis (SFA) | P54 p.3, Eqs.(5)-(8), and P55 p.3, Eqs.(1)-(4), define mappings that minimize average squared temporal derivatives under zero-mean, unit-variance and decorrelation constraints. | Matching classical definitions in an industrial application and a methodological survey, with shared foundational lineage, not two independent inventions. This does not admit every supervised, probabilistic or deep variant as the same optimization. Slowness is temporal variation relative to feature scale, not low sampling rate, computational speed, quality relevance or low-pass filtering. P34 and P53 illustrate different adaptations whose stated objectives must be checked separately. |
| multilabel / multi-label learning and classification | P37 pp.2,4, Section II-B2 and Eqs.(16)-(19), combines pairwise predictions into multiple subsystem-fault decisions; P39 pp.2-3, Section II-A, defines binary fault indicators with more than one positive for compound faults and a subsequent decision rule. P40 p.3 defines a binary sample-by-label matrix, with multilabel evaluation on p.5. | P37/P39 are distinct works by the same author pair; P40 provides a different team's related feature-selection setting. The shared target permits several labels per sample, not ambiguous alternatives or necessarily missing annotations. Pairwise classifiers and their fusion rules are source-specific. A local softmax classifier can participate in a multilabel system; inspect the final output rather than prescribing sigmoid heads or calling every compound-fault task multilabel. |
| physics-informed neural network (PINN) | P59 author version, Section 1 and Section 3.2; P60 author version v2, Section 1 and Section 2: physical constraints inform neural surrogate models through training penalties or constrained outputs. | Two distinct chemical-engineering works, with P60 extending P59's line of work. The base category is not limited to PDE residual losses; its hard/soft variants and complete proposed names are not interchangeable. Specify the implemented physical relation and its entry point. |

**Adversarial-role contrast:** P101 pp.1,8 describes deliberately perturbed
diagnostic inputs and their use during training. P102's institutional abstract
describes a spectral input attack in a black-box evaluation. These passages
corroborate the input-attack purpose, not two full definitions of an
adversarial-training or PGD mechanism. Neither generated-data discrimination
(P71/P72) nor domain discrimination (P70/P44) establishes that capability.
Keep attributed names and valid author-defined operations; a missing admission
record is not a ban. New attack-specific Chinese wording was not verified in
this reading. Use the actual actors/actions instead of an unchecked compound.

**Weighting-role boundary:** P92 p.4, P93 p.5 and P94 pp.3-4 supply different
operations: choosing generation seeds, weighting fitting residuals and selecting
augmentation prototypes. These records alone do not complete a matched definition
pair for classification-loss weighting, weighted cross-entropy, focal loss or one universal
balancing module. P39's prediction-dependent focal factor is a further distinct
object. Describe a verified method's actual multiplication and phase; the absent
pair is not a ban on valid mathematical weighting or an approved new name.
P96 p.3, Eqs.(3)-(4), adds one clear background definition of a class factor
multiplying cross-entropy; its p.6 proposed loss also includes a logit margin.
P97 p.4, Table 1, contains a class-weighted expression, but p.8, Eqs.(35)-(36),
instead shows binary cross-entropy with an overall objective coefficient. This
unresolved internal discrepancy is not used to finish a clean definition pair.
P18 p.4, Eq.(6), adjusts training logits inside the loss and is not another
outer-class-factor definition. The P96/P100 row above now supports the narrower
class-factor placement. A matched ordinary weighted-cross-entropy whole-loss
record remains incomplete; do not erase source differences or certify complete
methods and universal weight rules from this component match.
See [contextual decisions](terminology-decisions.md#weight-roles-and-class-decisions).

P98 p.6, Eqs.(10)-(12), supplies a further contrast: coefficients derived from
target pseudo-label counts scale target features before a mapping in an
alignment objective. This does not
contribute to that classification-factor pair or admit its full CWA-RST or
class-weighted-alignment names as generic mechanisms. P44 p.5, Eq.(13), has a
different weighted-feature recipient, a domain discriminator. Match the operand,
recipient and phase, not the shared adjective; normalization does not establish
unchanged feature geometry or calibrated class probabilities.

Chinese wording is independently supported for selected entries below. These
translation sources do **not** enlarge that engineering corpus or certify
the performance/style claims made by their authors.

| Chinese check | Primary online locator and checked content | Status and transfer boundary |
|---|---|---|
| hypergraph / 超图; hyperedge / 超边; hypergraph neural network / 超图神经网络 | [Engineering, Hypergraph Computation](https://www.engineering.org.cn/engi/CN/1159983337043452565), original paired title/abstracts, selected Section 3.2 and opening Section 3.3 | Confirms these base wordings and their set/node meaning. It does not certify every network variant or the English industrial definition pair; incidence-matrix Chinese naming was not independently verified. |
| hypergraph convolution / 超图卷积 | [Complex Systems and Complexity Science, 2025, 22(1):131-137](https://fzkx.qdu.edu.cn/CN/abstract/abstract488.shtml), original paired title/abstracts and keywords | Paired abstract distinguishes intralayer hypergraph convolution and interlayer graph convolution. Wording only: the full multilayer algorithm and reported results were not audited, and this is not another English industrial-definition ID. |
| counterfactual explanation / 反事实解释 | [Control Theory & Applications, CCTA240576](https://jcta.alljournals.cn/cta_cn/ch/reader/view_abstract.aspx?file_no=CCTA240576&html_url=cta_cn/article/html/CCTA240576&journal_id=cta_cn), original bilingual title, abstracts and keywords | Verifies this explanation wording, not a separate industrial-generation definition, the full FICE method or every counterfactual-generation/actionability translation. The generation compound remains an English scoped record or a plain action description; an inaccessible Aerospace Control PDF was not counted as read. |
| domain generalization / 领域泛化; 域泛化 | [Acta Automatica Sinica c200238](https://www.aas.net.cn/article/doi/10.16383/j.aas.c200238), Table 3 and paired Table 11 captions; [AAS c260215](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c260215), priority-publication page, paired title/abstracts/keywords | Two distinct works support these wording variants; the second has no final volume/pages yet. The survey's DA/DG hierarchy is not imposed universally, and the second full federated/open-set method is not audited. This verifies base wording/context, not extra industrial-definition IDs, unknown-fault rejection or performance guarantees. |
| remaining useful life / 剩余寿命; 剩余使用寿命 | [Chinese Journal of Engineering, 2019.10.10.005](https://cje.ustb.edu.cn/article/doi/10.13374/j.issn2095-9389.2019.10.10.005), original paired title/abstracts; [equivalent-cycle battery paper](https://cje.ustb.edu.cn/cn/article/id/e8a2f2f8-f620-4dba-8882-355fe77d5255), original paired title/abstracts | Two original works independently verify wording variants; the first abstract defines time to useful-life end, the second connects battery life to a declared threshold. The accessible HTML lacks complete method equations. These are wording/target checks, not extra industrial-definition IDs or certification of every full prognostic name, threshold value or performance claim. |
| active learning / 主动学习 | [Journal of Software, 2024, 35(3):1125-1139](https://www.jos.org.cn/jos/article/abstract/7073), original paired abstracts; [Journal of System Simulation, 2021, 33(6):1350-1357](https://www.china-simulation.com/CN/abstract/abstract2630.shtml), original bilingual title and abstracts | Two distinct original journal pages pair the base term with selective annotation in multimodal training and soft sensing. These are wording/role checks, not complete method audits or extra English industrial-definition IDs. The accessible pages do not establish every query-strategy translation, predictor family, full proposed name or annotation-cost claim. |
| weighted cross-entropy loss / 加权交叉熵损失（函数） | [Coal Science and Technology, cst.2023-0903](https://www.mtkxjs.com.cn/article/doi/10.12438/cst.2023-0903), original paired abstracts | Explicit bilingual wording in minority-class training. The accessible HTML supplies no loss equation, so this verifies translation, not a full computation or a two-work English definition pair. It does not certify a generic class-weighting Chinese label, inverse-frequency rule, focal variant or complete TLCNN name, and adds no engineering-definition ID. |
| soft-threshold function / 软阈值函数; soft thresholding / 软阈值化 | [Journal of Northeastern University (Natural Science), 2024, 45(11):1587-1594](https://xuebao.neu.edu.cn/natural/CN/10.12068/j.issn.1005-3026.2024.11.009), original paired abstracts; [Journal of Beijing University of Aeronautics and Astronautics, 2021, 47(7):1399-1406](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2020.0194), original paired abstracts and keywords | Two original journal pages verify the function and operation wording, respectively. Their accessible HTML does not supply the complete method equation bodies. This does not admit all residual-shrinkage module names, verify claimed optimality/noise separation, or add two industrial English-definition IDs. |
| Dempster's rule of combination / Dempster合成规则; Dempster组合规则 | [Journal of BUPT, 10.13190/j.jbupt.2018-094](https://html.rhhz.net/buptjournal/html/20190104.htm), original paired abstracts/keywords and Section 1, Definition 1, Eqs.(1)-(2); [Acta Automatica Sinica c190676](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190676?viewType=HTML), paired abstracts and Table 3 | Both wording variants are supported for the base rule. The first supplies the explicit normalized operation; the second accessible page supplies abstracts/tables, not a complete body reading. These Chinese checks do not add two industrial implementations, admit every improved/reliable fusion name or verify the sources' complete derivations. |
| evidential deep learning / 证据深度学习; subjective logic / 主观逻辑 | [Journal of Image and Graphics, jig.250475](https://doi.org/10.11834/jig.250475), original bilingual title/abstract/keywords and Sections 1.2-1.3, PDF pp.1-2,5-6 | The base wordings are verified. Section 1.2 uses 信念质量 for the defined b and 不确定性质量 for u; keep their definitions rather than treating either as class probability. This medical review verifies wording, not another industrial implementation, every translation synonym, uncertainty decomposition or full module name. |
| root cause diagnosis / 根源诊断; propagation path identification / 传播路径识别 | [Acta Automatica Sinica c200257](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200257?viewType=HTML), original bilingual title, abstracts and paired keywords | These source wordings are verified; they do not automatically certify every identification/recognition synonym, the separate phrase 根因识别, or a full causal-module name. The readable page supplied abstract/caption material, not full method definitions. This translation record does not add an implemented industrial-method pair. |
| network pruning / 网络剪枝 | [Acta Automatica Sinica c180275](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c180275), original bilingual abstract and paired keywords | Supports the base translation separately from the P85/P86 English operation pair. The accessible page supplied abstracts/captions, not the full method body. This model-optimization survey does not add another industrial implementation, admit every qualified pruning name or certify acceleration. |
| state-space model / 状态空间模型; Kalman filter/filtering / 卡尔曼滤波; fixed-lag smoother / 固定时延平滑 | [Acta Automatica Sinica c230457](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230457?viewType=HTML), paired Fig.5 caption; [AAS 2013.00043](https://www.aas.net.cn/cn/article/doi/10.3724/SP.J.1004.2013.00043), bilingual title/abstract/keywords; [Bulletin of Surveying and Mapping, 2017.0338](https://html.rhhz.net/CHTB/html/2017-11-6.htm), original bilingual title/abstract/keywords and Sections 1-2 | The first pairs state-space wording inside a deep variant; the second explicitly pairs the Kalman base; the third distinguishes filtering and delayed smoothing. These verify wording, not every full linear-Gaussian/neural/lagged variant or industrial operation. Accessible AAS captions/abstracts are not full-body definition reading, and translation pages add no process-study IDs. |
| generative adversarial network / 生成对抗网络; source variant 生成式对抗网络 | [Acta Automatica Sinica c180831](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c180831), original bilingual title/abstract/keywords; [Journal on Communications, 10.11959/j.issn.1000-436x.2018032](https://www.joconline.com.cn/zh/article/doi/10.11959/j.issn.1000-436x.2018032/), original bilingual title/abstract | Both explicitly pair GAN base wording. These translation sources do not add industrial-operation definitions, certify all named variants or make every complete adversarial pipeline unsupervised. Keep the meaning of generated object and discriminator target explicit. |
| multiscale convolution / 多尺度卷积; receptive field / 感受野 | [Journal of Computer Applications, 10.11772/j.issn.1001-9081.2023020185](https://www.joca.cn/CN/abstract/abstract26521.shtml), bilingual title and abstracts; [Acta Automatica Sinica c190376](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190376?viewType=HTML), bilingual title, keywords and Fig.4 caption | The first directly pairs the convolution name; the second pairs receptive-field wording in its named enhanced variant. Only these base translations are supported. These adjacent computing/vision pages add no process-industry definition IDs and do not admit complete named blocks or validate a physical frequency interpretation. The AAS accessible page supplied captions, not the full body definition. |
| soft sensing / soft sensor modeling / 软测量、软测量建模 | [Acta Automatica Sinica c210035](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c210035), original bilingual title; [Information and Control, 2020.9311](https://xk.sia.cn/article/doi/10.13976/j.cnki.xk.2020.9311?viewType=HTML), original bilingual title and abstract | Both pair soft-sensor modeling with 软测量; the second additionally describes estimating difficult-to-measure variables. This verifies the model-task wording, not every Chinese translation of `inferential`, `virtual`, `primary` or `secondary`, nor the sources' performance claims. These translation pages add no engineering source IDs. |
| few-shot learning / 小样本学习 | [Acta Aeronautica et Astronautica Sinica, 10.7527/S1000-6893.2019.23756](https://hkxb.buaa.edu.cn/CN/10.7527/S1000-6893.2019.23756), bilingual title, abstracts and keywords; [Journal of Software, 006958](https://www.jos.org.cn/jos/article/abstract/6958), bilingual title and abstracts | Both explicitly pair the base term; the first scopes limited supervision to target classes. They verify wording, not an identical training arrangement or industrial-process prevalence. Other low-data descriptions are not automatically equivalent, and these translation sources do not enlarge the engineering corpus. |
| zero-shot learning / 零样本学习; zero-shot fault diagnosis / 零样本故障诊断 | [Journal of Software 6146](https://www.jos.org.cn/jos/article/abstract/6146), original bilingual title/abstract and keywords; [TCES 231335](https://dgjsxb.ces-transaction.com/CN/10.19595/j.cnki.1000-6753.tces.231335), original bilingual title/abstract and paired keywords | Both explicitly pair zero-shot learning with 零样本学习; TCES also pairs the fault-diagnosis term. These accessible abstract pages verify wording and the class-semantic context, not their complete algorithms or every generalized variant. No extra industrial corpus IDs are added. The separately read [CJSI J2514442 abstract](https://yqyb.cis.org.cn/yqyb/article/abstract/J2514442) uses generalized zero-shot/zero-sample variants; it does not establish a unique preferred English variant or a full metric definition. |
| multi-instance learning / 多实例学习; 多示例学习; bag / 包 | [Journal of Nanjing University (Natural Sciences), 2026, 62(2):297-308](https://jns.nju.edu.cn/CN/abstract/article/0469-5097/1791), original bilingual abstract and keywords; [Journal of Computer-Aided Design & Computer Graphics, 10.3724/SP.J.1089.2018.16591](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2018.16591), bilingual title/abstract | The first pairs 多实例 with MIL and describes bags/instances; the second uses 多示例 and pairs bag-space/instance-space with 包空间/示例空间. These are verified wording variants, not different admitted mechanisms or additional industrial studies. Complete hierarchy/selection/fusion names remain attributed. |
| semi-supervised learning / 半监督学习 | [Acta Automatica Sinica, 2013, 39(11):1871-1878](https://www.aas.net.cn/cn/article/doi/10.3724/SP.J.1004.2013.01871), bilingual abstract and paired keywords | The source explicitly connects limited labeled examples and available unlabeled data. Its disagreement-based subtype is not a requirement of all semisupervised methods or an additional industrial application definition. |
| self-supervised learning / 自监督学习 | [Acta Automatica Sinica c220421](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220421), bilingual abstract and paired keywords | Explicit base-name correspondence; the source distinguishes self-supervised, contrastive and metric learning. This translation check does not identify every auxiliary objective as contrastive or certify a complete named variant. |
| weakly supervised / 弱监督 | [Journal of Computer-Aided Design & Computer Graphics, 10.3724/SP.J.1089.2021.18594](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2021.18594), original bilingual title/abstract | Verified wording in image-level supervision for finer defect outputs. This translation does not make coarse annotation the only weak-supervision setting or establish equivalence to the sparse-quality-target use in P25. No paired English record for one universal weak-supervision operator is claimed. |
| autoencoder / 自编码器 | [Acta Automatica Sinica c200684](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200684), paired keywords and bilingual title/abstract; [c190857](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190857), bilingual title and stacked-denoising variant | The first explicitly pairs the base keyword; the second verifies its use inside a named variant. These are translation checks, not admission of their complete module names or proof that all AEs reduce dimension. Other Chinese variants are not certified by this record. |
| variational autoencoder / 变分自编码器 | [Acta Automatica Sinica c210035](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c210035), original Chinese abstract explicitly supplies the English name and VAE, with paired keywords | Verified base translation in industrial soft sensing. Its mixture-regression variant remains source-specific; the abstract does not independently validate a standard sampling formula or predictive calibration. |
| continual learning / 持续学习; source variant 连续学习 | [Acta Automatica Sinica c240805](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240805), bilingual title/abstract/keywords; [c220312](https://www.aas.net.cn/article/doi/10.16383/j.aas.c220312), bilingual abstract and keywords | Both explicitly identify continual learning; the latter uses 连续学习 and separately pairs class-incremental learning with 类增量学习. Preserve these scope differences. A generic incremental-learning Chinese pairing and full test-time-adjustment names have not been independently verified in this round; failed pages are not evidence. |
| feature selection / 特征选择 | [Microelectronics & Computer, 2021.1033](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2021.1033), bilingual title and abstracts; [Acta Automatica Sinica, 2017, 43(5):795-805](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.2017.c150851), bilingual title, abstracts and keywords | Both explicitly pair the base term; the latter describes ranking and redundancy removal to obtain a subset. These verify the translation, not every selection-layer variant, causal interpretation or industrial sensing-cost claim. |
| physics-informed neural network / 物理信息神经网络 | [Earth Science Frontiers, 10.13745/j.esf.sf.2025.10.38](https://jypl.pku.edu.cn/Article/info?aid=388874189), original Chinese abstract explicitly supplies the English term and abbreviation | Base translation verified. This is not admission of arbitrary physics-qualified module names or validation of the article's numerical claims. |
| feature fusion / 特征融合 | [Acta Automatica Sinica, c190428](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190428?viewType=HTML), bilingual abstract and keywords | Verified translation for combining features; image-reconstruction context, not an industrial method-prevalence claim. |
| self-attention / 自注意力 | [Acta Automatica Sinica, c220027](https://www.aas.net.cn/article/doi/10.16383/j.aas.c220027), bilingual Fig.2 caption; [c220715](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220715?viewType=HTML), bilingual abstract | Translation for self-attention, including named variants. This does not admit those variant names as general families or validate cross-attention. |
| multi-head attention / 多头注意力（机制） | [Journal of System Simulation, 2025, 37(10):2594-2604](https://www.china-simulation.com/CN/10.16182/j.issn1004731x.joss.24-0490), original paired abstracts; [Acta Automatica Sinica, 2023, 49(9):1889-1903](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220767?viewType=HTML), original bilingual Fig.1 caption | Two distinct original journal pages verify the generic wording separately from multi-head self-attention. The first uses the base term inside an improved variant; the second is an image-captioning context. These are wording checks, not two full method audits or extra industrial-definition IDs. Do not add the self-attention qualifier unless the query/key/value input relation supports it, or promote either article's complete proposed name to a general family. |
| multi-head self-attention / 多头自注意力（机制） | [CIESC Journal, 2024, 75(12):4654-4665](https://hgxb.cip.com.cn/CN/Y2024/V75/I12/4654), original bilingual abstracts and keywords; [Journal of Jiangsu University (Natural Science Edition), 2023, 44(4):444-451](https://zzs.ujs.edu.cn/xbzkb/CN/10.3969/j.issn.1671-7775.2023.04.011), original bilingual title | Two original scholarly pages pair the complete self-attention wording. The second page's abstract body was unresolved template text, not read evidence. These verify the translation, not the complete MHSA-LSTM/air-data models, head-merger formulas, other qualified attention names or extra industrial-definition IDs. |
| gating mechanism / 门控机制 | [Acta Automatica Sinica, c250366](https://www.aas.net.cn/article/doi/10.16383/j.aas.c250366), original bilingual abstract; [Journal of Electronics & Information Technology, JEIT240977](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240977), original bilingual title and extended abstract, Methods | Two original sources pair the base wording in neural expert and parallel-feature contexts. Their accessible HTML supplies no gate equation; these are translation checks, not new industrial-definition counts. Full proposed module names remain attributed and do not validate an arbitrary time/age-qualified translation. |
| TSK fuzzy classifier / TSK模糊分类器; first-order TSK / 一阶TSK | [CAAI Transactions on Intelligent Systems, 202408015](https://html.rhhz.net/tis/html/202408015.htm), bilingual title/abstract/keywords and Section 1, Eqs.(1)-(3) | Verifies the classifier wording and first-order rule context, not every modified TSK name or the full domain-adaptation method. Its later Gaussian parameter/formula account is not adopted. This translation check adds no English-definition ID. |
| Gaussian membership function / 高斯隶属度函数; antecedent / 前件; consequent / 后件 | [Journal of University of Science and Technology Beijing, 2011.05.013](https://cje.ustb.edu.cn/cn/article/pdf/preview/10.13374/j.issn1001-053x.2011.05.013.pdf), Section 2.2 and bilingual Fig.3, PDF pp.2-3; [Tsinghua University Press trial chapter](https://www.tup.tsinghua.edu.cn/upload/books/yz/053331-01.pdf), Section 1.1, PDF p.5 | The journal caption directly pairs the Gaussian term; the publisher page explicitly pairs the two rule parts. These verify wording, not every complete fuzzy-system name or source formula. The journal's nearby center/width explanation conflicts with its displayed parameter roles and is not adopted. Translation sources add no industrial-definition IDs. |
| source-free domain adaptation / 源域无关的域自适应; source variant 无源域适应 | [Journal of Software 6467](https://www.jos.org.cn/html/2022/4/6467.htm), original bilingual title/abstract/keywords and introductory definition; [JCST 10.1007/s11390-021-1106-5](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-021-1106-5), original Chinese page title and bilingual abstracts | Both describe a source-trained predictor with target measurements rather than available source samples. Keep the verified wording variants, not a unique translation ranking. These computing sources verify wording, not industrial prevalence, full component names or privacy/performance guarantees. |
| test-time adaptation / 测试时适应 | [Journal of Software 7009](https://www.jos.org.cn/jos/article/abstract/7009), original bilingual title/abstract and paired keywords | Verifies the base wording in open-set recognition, not a mandatory open-set task, update objective or complete adaptation-module name. Other Chinese variants are not certified by this single translation record. |
| multi-rate / 多速率; multi-sampling rate / 多采样率 | [AAS c250584](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250584), bilingual title/abstract/keywords; [CIESC 20241121](https://www.hgxb.com.cn/zh/article/doi/10.11949/0438-1157.20241121/), bilingual title/abstract | Base wording variants in process control/soft sensing, not admission of their full layered-learning or TTPA names. The AAS HTML supplied abstracts/captions rather than a full method reading. |
| non-uniform sampling / 非均匀采样; irregular sampling / 非规则采样 | [AAS 2017.c150787](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.2017.c150787?viewType=HTML), bilingual title/abstract/keywords; [AAAS 2021.25019](https://hkxb.buaa.edu.cn/CN/abstract/abstract18389.shtml), bilingual title/abstract/keywords | Separate verified word pairs, not universal equivalence of every system assumption. The AAS accessible body supplied captions/tables, not the full definition. The aerospace abstract describes missingness and irregular timing together; its complete anomaly detector is not a generic industrial module. |
| asynchronous sampling / 异步采样 (optical context) | [Optical Instruments 20210512](https://joi.usst.edu.cn/html/2021/5/20210512.htm), original bilingual title/abstract/keywords and introductory definition | Verifies the wording in dual-comb sampling, not a unique definition for process timestamps, event-driven software or communication. Explain the actual clocks/offsets before transferring its meaning; this is not a paired industrial mechanism record. |
| residual connection / 残差连接 | [Coal Science and Technology, 2025, 53(2):96-108](https://mtkxjs.com.cn/cn/article/pdf/preview/10.12438/cst.2024-1441.pdf), Section 1.3 and bilingual Fig.3, printed p.99 / PDF p.5; [Transactions of the CSAE, downloaded paginated version 2026, 42(8):47-56](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.202505227.pdf), Section 2.1, printed p.50 / PDF p.4 | Both original passages were rechecked and rendered; they explicitly pair the terms, and the second describes addition of earlier inputs and later features. Its cached earlier pagination differs from the downloaded version carrying the same DOI; these are not two works. This verifies the base translation, not all parallel branches, signal remainders, complete attention-module names or empirical guarantees. |
| message passing / 消息传递 | [Journal of Software, 006601](https://www.jos.org.cn/html/2022/8/6601.htm), bilingual title/abstract and Section 1.2 Eqs.(2)-(7); [Acta Automatica Sinica, c220371](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220371?viewType=HTML), bilingual title/abstract/keywords | Two original Chinese sources match the base graph-computation translation: SAT-variable/clause nodes and atom/bond features, respectively. Their full proposed network names remain attributed. The second accessible HTML did not provide the method body; these translation checks are not additional industrial-definition counts or support for every qualified Chinese module name. |
| fuzzy clustering / 模糊聚类; fuzzy c-means / 模糊c均值 | [Acta Automatica Sinica, c200392](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200392?viewType=HTML), bilingual title and abstract | The abstract explicitly discusses traditional FCM and a source-specific robust weighted variant in wastewater monitoring. Supports the base wording, not adoption of that variant's full name as a general family. |
| diffusion model / 扩散模型 | [Journal of Software, 007511, journal issue page 413](https://ebook.xml-journal.net/rjxb/2026/04/files/basic-html/page413.html), bilingual title, abstract and Chinese keywords | Confirms generative-model terminology in an image-generation review. Does not add process-industry application evidence or justify a sensor-restoration claim. |
| graph convolutional network / 图卷积神经网络 | [Acta Automatica Sinica, c190720](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190720?viewType=HTML), bilingual Fig.8 caption | Verifies the network-name translation. The accessible caption does not independently verify every graph-convolution variant or a physical meaning for its edges; the English operation evidence is recorded above. |
| cross-attention / 交叉注意力 | [Acta Automatica Sinica, c250203](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250203?viewType=HTML), bilingual Table 1 heading and its exogenous-variable fusion entries | Verifies this base translation in a time-series review. The table groups several architectures; it does not make their query/key/value definitions identical. English operation evidence comes from P38/P43, not from counting the table's cited titles. |
| mixture of experts / 混合专家 | [Acta Automatica Sinica, c250366](https://www.aas.net.cn/article/doi/10.16383/j.aas.c250366), bilingual title, abstract and keywords | Verifies the base translation. Its language-processing model uses specialized sparse mechanisms; these are not requirements for every industrial MoE or evidence that linear experts are neural subnetworks. |
| domain adaptation / 域适应 | [Acta Automatica Sinica, c200238](https://www.aas.net.cn/article/doi/10.16383/j.aas.c200238), bilingual title and abstracts | Verifies this translation and distinguishes ordinary and complex label-space settings. It does not make identical class spaces a requirement of every adaptation study. Other Chinese variants need their own check before being called equivalent standard translations. |
| knowledge distillation / 知识蒸馏 | [Journal of Software, 006933](https://www.jos.org.cn/jos/article/abstract/6933), bilingual title and abstracts | Verifies the base translation; the abstract also distinguishes output, intermediate and graph-based knowledge. Its introductory large-teacher/small-student account is not a universal restriction on model size or task. This is translation evidence, not an additional industrial application paper. |
| class prototype / 类原型; prototype features / 原型特征 | [Acta Automatica Sinica, c240312](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240312?viewType=HTML), bilingual title, abstracts and Fig.1 caption | Verifies these feature-space terms and distinguishes a mean-based construction from that paper's adaptive construction. Its image-classification context is translation evidence, not another industrial case or permission to borrow the full module name. |
| soft assignment / 软分配 | [Journal of Image and Graphics, jig.200467](https://www.cjig.cn/zh/article/doi/10.11834/jig.200467/), original Chinese and English abstracts | Verified wording for graded assignment of embeddings to cluster centers. The English definition pair is separately recorded above; neither check turns arbitrary softmax weights into fuzzy memberships, physical-mode probabilities or a named gate. |
| max pooling / 最大池化; average pooling / 平均池化 | [Journal of University of Chinese Academy of Sciences, 2018, 35(1):75-83](https://html.rhhz.net/ZGKXYDXXB/20180110.htm), Section 1.1.2; [Microelectronics & Computer, 2023.0574](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2023.0574), bilingual abstracts | Independent translation checks. The first source defines regional maximum selection; the second names both base operations inside its own proposed variant. Neither its full variant name nor either source's performance/invariance claims are admitted by this translation record. English operation records remain separate; these translations do not certify every pooling variant. |
| global average pooling (GAP) / 全局平均池化 | [Acta Automatica Sinica c200070](https://www.aas.net.cn/cn/article/pdf/preview/10.16383/j.aas.c200070.pdf), Section 1.1, Eq.(1) and following bilingual definition, PDF p.3 / printed p.2225; [Journal of Electronics & Information Technology, JEIT200431](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT200431?viewType=HTML), original bilingual abstract | Two different author groups verify this base name. The first reduces a feature map to its channel vector; the second describes channel statistics in action recognition, with no method body in the accessible HTML. These translation checks do not certify full proposed module names, supply additional industrial-definition counts or make one reduction axis universal. |
| contrastive learning / 对比学习 | [Acta Automatica Sinica, c220421](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220421), bilingual title, abstracts, keywords and Figs.4-5 captions | Verifies the base translation and distinguishes it from the broader self-supervised-learning category. The bilingual captions also identify hard and false negative pairs; they do not turn contrastive pair labels into physical fault labels. |
| pseudo-label / 伪标签 | [Application Research of Computers, 2025.11.0460](https://www.arocmag.cn/abs/2025.11.0460), bilingual title and original Chinese abstract | Verifies the base translation in fault diagnosis. The abstract distinguishes model-generated initial labels from subsequently refined soft labels. This translation check does not admit that paper's complete optimization/module names or validate its performance claims. |
| energy function / 能量函数; energy score / 能量分数 (classifier-logit context) | [Acta Electronica Sinica, 2026, 54(1):153-166](https://www.ejournal.org.cn/zh/article/doi/10.12263/DZXB.20250761/), Section 3.1, Eq.(9), printed pp.157-158 / PDF pp.5-6, and Section 4.3, printed p.162 / PDF p.10; [author-hosted Chinese translation of Class-Specific Semantic Reconstruction for Open Set Recognition](https://mftp.mmcheng.net/Papers/22PAMI-OpenSet-cn.pdf), Section 2.2, PDF p.3 | The journal defines the logit-derived function and uses the score term; the author-hosted translation separately uses `能量分数` for OOD scoring. It is a translation linked from the author's publication list, not an official Chinese IEEE edition or a second independent definition. These checks do not verify `free energy / 自由能` in this sense, or transfer probability/calibration guarantees from nearby prose. |
| free energy / 自由能 (scoped wording corroboration) | [CCF Multimedia Technical Committee commentary](https://tc.ccf.org.cn/tcmt/xsdt/lwdd/2025-02-12/837946.shtml), item 04, Methods; [Chinese Physical Society terminology reference draft](https://wulixb.iphy.ac.cn/fileWLXB/cms/news/info/upload/%E7%89%A9%E7%90%86%E5%AD%A6%E5%90%8D%E8%AF%8D%EF%BC%88%E5%8F%82%E8%80%83%EF%BC%89.pdf), PDF pp.1,72,83 | The official commentary uses `Energy (Helmholtz 自由能)` for classifier-based OOD scoring. The physics document corroborates the word form but identifies itself as a March 2010 revision draft, not a current normative standard. Neither is a Chinese classifier-method definition. Use the wording with the actual P18/P51 score convention, not physical thermodynamic units; no extra industrial-definition ID, unique mandatory translation, full module name or performance guarantee follows. |
| open-set recognition / 开集识别 | [Journal of Computer Applications, 2025, 45(7):2195-2202](https://www.joca.cn/CN/abstract/abstract26875.shtml), bilingual title, abstracts and keywords | Confirms the task wording: classify known classes and reject unknown inputs. The image-recognition source supplies translation evidence, not another industrial application or admission of its full component names. |
| data imputation / 数据插补; missing-value imputation / 缺失值插补; source variant 缺失值填补 | [Acta Automatica Sinica, c230534](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230534), original paired title/abstracts/keywords; [Journal of Sichuan University article page](https://journal.scu.edu.cn/info/1104/29335.htm), paired abstracts/keywords | The original AAS normal URL was reread after its query variant timed out; it pairs data imputation with 数据插补. The second corroborates 缺失值填补 as a wording variant, not another industrial-definition ID, full class-center method or endorsement of label access. Full source names, distribution guarantees and performance remain outside this wording check. |
| reconstruction loss / 重构损失 | [Advanced Engineering Sciences, 2022, 54(5):240-248](https://scuaes.ijournals.cn/html/2022/5/202100675.html), bilingual abstracts and paired keywords | Verified loss-name translation in image inpainting. This does not establish a universal mask, industrial restoration capability or equivalent wording for every reconstruction objective. |
| distribution alignment / 分布对齐 | [Acta Automatica Sinica, c250653](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250653?viewType=HTML), bilingual abstracts | Verified wording for a representation-distribution constraint in KPI forecasting with missing variables. The abstract is translation evidence, not verification of its full architecture, theory or results. |
| maximum mean discrepancy / 最大均值差异 | [Acta Automatica Sinica, c190593](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190593?viewType=HTML), bilingual abstracts | Verified base loss/regularizer wording in bearing fault detection. Does not admit the source's full improved variant or establish equivalence to mutual information. |
| slow feature analysis / 慢特征分析 | [Acta Automatica Sinica, c201035](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201035?viewType=HTML) and [c230154](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230154?viewType=HTML), bilingual abstracts and keywords | Both explicitly pair the base name with SFA in process operating-performance assessment. Their KPI-driven and distributed/dynamic variants are not thereby admitted as universal module names. Translation evidence does not validate those variants' equations or experiments. |
| multi-label learning / 多标签学习 | [Microelectronics & Computer, 2022.0266](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2022.0266), bilingual title and abstracts; [Journal of Software, 2024, 35(6):2775-2794, issue page 199](https://ebook.xml-journal.net/rjxb/2024/06/files/basic-html/page199.html), bilingual title and abstract opening | Both explicitly pair the base wording. The former also defines association of a sample with multiple labels. These general learning/software contexts verify translation, not process-industry prevalence, the source-specific feature-selection methods, or physical fault interaction. |
| causal convolution / 因果卷积 | [Acta Automatica Sinica c230634](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230634?viewType=HTML), original bilingual abstracts and Fig.2 caption; [Transactions of China Electrotechnical Society, 2022](https://dgjsxb.ces-transaction.com/fileup/HTML/2022-5-1242.htm), Section 3.1.2 | Independent original sources pair the base term in temporal prediction. The first HTML lacks the equation body; the second's equations are images and were not validated here. These support wording, not every dilated/attention-qualified variant, full system name, physical causal claim or complete-model prediction horizon. |

Other Chinese counterparts and other method-family names have not all received
this completed paired record. Keep them as source-attributed or definition-based
working terminology until checked for the requested recommendation. In
particular, the scoped P33/P48 assignment pair does not admit every soft
assignment mechanism, and paired base MoE or cross-attention records do not admit
all source-specific variants. Modified adaptation/distillation names and other
candidate definitions still require their own completed records. This is a limit of this
ledger, not a claim that these methods occur only once in the field.

P85/P86 complete a scoped parameter-pruning definition pair; they do not change the earlier P31/P74 findings. P31's inspected adaptive-degree method is not parameter removal, and P74's selective weighting preserves its represented set. P76's conflicting background wording is not another matching operation. A separately read author preprint describes masking, but its journal-version method/publication match remains unchecked and is not counted in this pair. P45's multihead/multibranch conversion remains attributed, not admission of every reparameterization family. Search titles, related-work mentions and translation matches do not close these remaining gaps. Accurate author-defined or definition-based descriptions may still be used without inventing a field-wide convention.

`Cross-stage feature fusion`, `process-topology-guided integration` and similar
compositional phrases above describe an operation only when the manuscript
implements it. Their head words do not certify a conventional named module.
Where an author defines a specific name, keep that identity separate from the
shared-bank recommendation. More source checks should extend the evidence rows,
not turn this incomplete snapshot into an automatic whitelist or blacklist.
