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

Coverage means the number within the sources actually searched, not a claim about the whole field. Mark unsearched usage as unchecked, not zero. A local grammar request does not require a whole-manuscript frequency ledger.

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
2. **Problem layer**: multi-stage, multi-rate, multimode, missing data,
   limited labels, nonstationarity, compound faults, or anomaly localization.
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
| Engineering challenges | multi-stage/plant-wide, multi-rate, multimode, nonstationary, missing data, limited labels, compound faults, anomaly localization |
| Engineering tasks | fault detection, fault diagnosis, process monitoring, quality prediction, remaining-life estimation, control, optimization, decision support |
| Method families | feature fusion, graph modeling, attention, transfer/adaptation, lightweight modeling, self/weak supervision, diffusion, fuzzy modeling, multimodal learning, language models |
| Evidence profiles | benchmark-only, benchmark plus real-world case, background-driven application, online/shadow evaluation, deployed system |

Keep the generic core stable. A topic-specific entry must state both the
engineering problem it names and the method/evidence context in which it is
appropriate.

## 11. Checked Core Names And Remaining Scope

Targeted definition checks on 2026-10-24 support the following **English base
terms**, not all modified module names containing them. P IDs and PDF page
positions refer to the [published index](published-evidence.md). These are
original semantic summaries, not extracted source passages.

| Base term | Checked distinct papers and operation | Boundary |
|---|---|---|
| feature extraction | P01 p.4 constructs multiscale features from stage measurements; P14 p.3 constructs temporal features through convolution. | Extracting representations is not selecting an existing subset or combining final decisions. |
| feature selection (explicit subset operation) | P40 pp.3-4, Section III-B and Algorithm 1, removes low-ranked descriptors and returns feature indices; P61 pp.3-4, Eq.(5), and p.6, Step 3, ranks and recursively removes process-variable inputs. | Two distinct journal works support subset selection, with different input objects and ranking criteria. P62 p.4, Section 2.1, instead defines an attributed `feature-selection layer` through trainable input weights; its p.5, Section 3.1, uses those weights for ranking. Preserve that local name without inferring a reduced subset, fewer sensors, calibrated relevance or physical causes. |
| incremental learning | P30 p.4, Eqs.(10)-(13), updates classifier weights after labeled examples; P63 pp.3-5, Sections II/III and Algorithm 1, updates a subspace and classifier as sensory inputs evolve, with classifier learning requiring labels. | Matched base sense of updating an existing learner with new information, different update objects and information conditions. It does not require new classes or establish one universal predict/update order; preserve the source-specific training and out-of-sample distinction. |
| continual learning | P64 p.3, Section 2.2, and pp.5-6, Section 3.3/Algorithm 1, learn new operating conditions while addressing earlier-condition retention; P65 pp.3-6, Section III-A/D/F, adapts to successive unlabeled target domains while constraining loss of earlier knowledge. | Two distinct industrial works support the sequential learning/retention purpose, not identical supervision or memory. P64 uses a feature buffer; P65 retains source data and earlier model information without replaying old target instances. A method can be evaluated for continual learning even when retention is imperfect. |
| feature fusion | P01 pp.4-5, Section 3.4 and Eqs.(7)-(10), combines stage features using topology and similarity matrices, then adds the two outputs; P03 pp.4-5, Section 2.3.2 and Eq.(17), combines two attention-derived representations by learned weighting; P14 p.4, Section III-D4 and Eq.(35), concatenates multiscale convolution outputs before classification. | Three distinct works, including two related team papers, support the base feature-combination term, not one universal operator. P14's block-diagonal graph assembly in Eq.(28) is a different operation. Neither the shared base word nor these definitions establish a generic `causal`, `reliable` or topology-qualified module family. |
| attention mechanism / self-attention | P11 p.3 and P24 p.3 define query/key/value weighting with the self-attention inputs drawn from the same representation. | The checked common operation does not make all source-specific attention variants equivalent, causal or physically interpretable. |
| gating mechanism | P08 p.5 uses multiplicative feature gating; P19 p.5 computes scale weights; P33 p.6 gates attention outputs. | Same general regulating role, different inputs and recipients. This does not establish an `age`-qualified module family. |
| residual connection | P02 p.3 describes the residual backbone connection; P14 p.2 specifies an additive residual operation. | Check addition and any projection. A generic bypass, concatenation or any parallel branch is not automatically the same residual operation. This network connection is distinct from a prediction error or the remainder after trend subtraction; specify the operands before transferring `residual` wording. |
| message passing | P13 p.3 aggregates graph-node information; P14 p.4 updates features through graph convolutional propagation. | Graph computation, not evidence of physical fault propagation or communication-network transfer. |
| fuzzy clustering; fuzzy c-means (FCM) | P28 p.3, Eqs.(4)-(7) and Algorithm 1, uses membership-weighted distances and alternating center/membership updates; P33 pp.3-4, Section III-C and Eqs.(5)-(6), defines FCM before its clustering architecture. | Same base clustering algorithm, different roles: reservoir-feature reinforcement versus incomplete-series clustering. The sources are machinery and general time-series studies. Their full network names, reinforcement steps and imputation mechanisms are not interchangeable. |
| diffusion model | P32 p.3, Section III-A, defines artificial forward noising and learned reverse generation for sequences; P35 p.3, Section III-A and Eq.(14), applies conditional diffusion to compressed features and decodes generated signals. | Common generative operation, different generated objects and conditioning. This does not establish sensor-noise restoration, identical inference cost or a universal industrial diffusion-module name. |
| graph convolution; graph convolutional network (GCN) | P07 p.7, Eqs.(18)-(19), combines normalized adjacency, feature projections and a gated nonlinearity; P14 p.4, Eqs.(33)-(34), uses adjacency-weighted feature projection and ReLU. | Common graph-feature computation, not identical graphs: variable-time nodes versus process-variable nodes. A GCN operation does not establish a physical or causal meaning for learned edges. |
| cross-attention | P38 p.6, Eq.(7), uses queries from one modality and keys/values from the other; P43 pp.4-5, Eqs.(1)-(2) and Figs.6-7, uses queries from one encoder scale and keys/values from concatenated scales. | Same query-to-key/value weighting principle, different representations and attention axes. Distinct modalities are not required; key/value features may include the queried scale. P42 p.4 defines cross-time and cross-variable **self-attention** despite its dual-cross-attention title. That title is not a second definition of the P38/P43 operation. Preserve attributed names, but inspect inputs before classifying a new module. |
| mixture of experts (MoE) | P36 pp.2-3, Eq.(2) and Eqs.(5)-(6), defines gated combinations of expert outputs and task-specific expert features; P41 pp.2-3, Eqs.(1)-(3), defines weighted expert predictions with input-dependent gates. | Shared mixture principle, not identical experts or outputs. P41 uses linear expert models, so `neural network` is not part of the base definition. Coefficient sparsity from regularization does not establish sparse expert execution, and a gate need not select one discrete operating mode. |
| domain adaptation | P10 pp.4-5 defines labeled-source/unlabeled-target learning with identical class spaces and local/global distribution losses; P44 pp.2,4-6 defines multiple source-target branches, distribution losses and prediction combination with a target class space contained in the source space. | Both address transfer across domain distributions, but label-space relations and label access differ. P44 Eq.(15) and Algorithm I explicitly contain target-label symbols; do not label its setting unsupervised from its title. An alignment objective and prediction fusion are distinct operations. |
| knowledge distillation (KD) | P45 pp.3-5 trains student heads to match teacher hidden features and regression targets; P46 pp.3,5-6 transfers multisensor-model guidance to single-sensor predictions through softened-output and semantic-similarity losses. | Teacher-guided learning is shared; task, transferred objects and sensor access differ. Classification probabilities, identical architectures and model compression are not universal requirements. P46's prose about unnormalized scores conflicts with the displayed softmax/temperature definition in Eq.(6); that specific claim is excluded. These adjacent equipment studies support the base method, not every named distillation variant or process-industry prevalence. |
| class prototype | P46 pp.5-6, Eqs.(7)-(10), computes class-conditioned feature means used in a similarity-transfer objective; P47 p.3, Eq.(4), computes labeled-support feature means consumed by query matching on pp.3-4. | Checked common sense: a feature-space class representative. Its downstream role, source samples and update rule must be stated. It is not automatically a physical state, independently optimized parameter or learned cluster; this record does not require every prototype method to use a mean or one vector per class. The motor and smart-grid contexts do not establish process-industry prevalence or a universal prototype-module name. |
| max pooling | P11 p.2, Eq.(2), takes the maximum in a feature-map region; P15 p.5, Eq.(12), takes the maximum in a specified convolutional-output window. | Same regional reduction, not certification of every pooling variant. State the reduced and retained axes. A maximum activation is not automatically a fault-relevant feature or evidence of noise robustness. |
| soft assignment (to clusters) | P48 p.5, Section II-A and Eqs.(1)-(3), explicitly defines graded sample-to-centroid assignments; P33 p.3, Section III-B and Eqs.(1)-(3), substantively defines the corresponding normalized Student-t cluster-assignment operation in its DEC preliminaries. | P48 is an exact name match; P33 is a checked semantic equivalent, not a literal-phrase hit. Both inherit DEC-related machinery, so they support the base operation, not independent invention or a universal module name. These sample-level assignments do not establish variable grouping, fuzzy-set semantics or calibrated physical-mode probabilities in another model. |
| contrastive learning | P20 p.6, Section III-D and Eqs.(18)-(21), scores node features against graph summaries with constructed positive/negative examples; P21 pp.4-5, Section III-C and Eqs.(4)-(6), contrasts temporal contexts with later latent features across augmented views. | Both explicitly name and define contrastive learning, but contrast different objects. Positive/negative denotes the training relation, not necessarily normal/faulty or same/different diagnosed classes. Neither pair construction is mandatory for the whole family, and their full module names remain source-specific. |
| pseudo-label / pseudolabel | P18 p.5, Eq.(10), generates a hard class target from adjusted classifier outputs; P21 p.5, Section III-D and Eq.(7), uses estimated class distributions to construct a pseudolabel graph over samples. | Same base sense of model-derived class guidance, different forms and consumers: hard targets versus distribution-derived sample relations. Preserve this distinction. These are not observed annotations, automatically calibrated probabilities, or verified physical process relations. |
| energy function / free energy (classifier-logit score) | P18 p.3, Eq.(4), calls its temperature-scaled negative log-sum-exp quantity `free energy`; P51 p.5, Eq.(18), calls the corresponding unit-temperature computation an `energy function`. | Checked equivalent computation under the stated logit convention, different names and consumers: domain-learning operations versus open-set decisions. Preserve source-specific notation. This is neither physical signal energy nor graph-Laplacian energy, and does not calibrate a probability, admit the full `graph-energy` name or validate P51's disputed threshold. Chinese checks below support `energy function` and `energy score`, not yet the exact `free energy` translation in this context. |
| open-set recognition | P51 pp.5-6 defines known-class classification and unknown rejection; P52 accepted-version p.2, Section II-A, defines training known classes and test inputs including new classes. | Matched task sense with different scoring mechanisms. Unknown rejection is not identification of an unseen fault type; new operating conditions do not alone establish new label classes. No universal threshold or uncertainty mechanism follows. |
| missing-value imputation | P25 p.4, Section 3.1, estimates unobserved auxiliary measurements before quality prediction; P33 p.5, Section IV-B and Eqs.(13)-(15), combines observed values with estimates at missing positions. | Matched base operation, different targets and mechanisms: process-input completion versus incomplete-series representation/clustering. Numeric padding and latent-feature alignment are not necessarily imputation. P25's mask and added linear output require an explicit preservation rule before its unchanged-observations claim can be transferred. P33 is adjacent time-series evidence, not a second process-industry case. |
| reconstruction loss | P17 pp.4-5, Eqs.(6), (14), compares reconstructed inputs with input targets alongside concentration prediction; P33 p.6, Eq.(18), compares decoded sequences with observations using a mask. | Shared reconstruction objective, not a universal norm, denominator or scoring subset. State the target, mask and reduction actually used. Reconstruction may regularize a predictor without producing completed measurements at inference; a lower training loss does not measure unknown physical values. |
| distribution alignment | P10 pp.5-6, Eqs.(15)-(17), reduces source/target feature-distribution discrepancy through a training objective; P44 pp.4-5, Eqs.(12)-(15), uses domain-adversarial and class-weighted distribution objectives. | Common distribution-matching purpose, different criteria, feature sets and supervision. Not timestamp synchronization, sample pairing or proof of retained fault semantics. Distinguish a marginal from a class-conditional target and measured reduction from an optimization aim. |
| maximum mean discrepancy (MMD) | P10 p.5, Eq.(15), defines a kernel mean-embedding discrepancy for source/target features; P32 p.4, Eqs.(10)-(11), defines a kernel discrepancy between sampled noise and predicted noise within diffusion training. | Same base discrepancy, different operands and loss roles. P32's full Ada-MMD name and mutual-information wording do not follow from the base definition. P44's introductory mention alone is not a third operational definition. Check the actual estimator, kernel and aggregation before reproducing a formula. |
| slow feature analysis (SFA) | P54 p.3, Eqs.(5)-(8), and P55 p.3, Eqs.(1)-(4), define mappings that minimize average squared temporal derivatives under zero-mean, unit-variance and decorrelation constraints. | Matching classical definitions in an industrial application and a methodological survey, with shared foundational lineage, not two independent inventions. This does not admit every supervised, probabilistic or deep variant as the same optimization. Slowness is temporal variation relative to feature scale, not low sampling rate, computational speed, quality relevance or low-pass filtering. P34 and P53 illustrate different adaptations whose stated objectives must be checked separately. |
| multilabel / multi-label learning and classification | P37 pp.2,4, Section II-B2 and Eqs.(16)-(19), combines pairwise predictions into multiple subsystem-fault decisions; P39 pp.2-3, Section II-A, defines binary fault indicators with more than one positive for compound faults and a subsequent decision rule. P40 p.3 defines a binary sample-by-label matrix, with multilabel evaluation on p.5. | P37/P39 are distinct works by the same author pair; P40 provides a different team's related feature-selection setting. The shared target permits several labels per sample, not ambiguous alternatives or necessarily missing annotations. Pairwise classifiers and their fusion rules are source-specific. A local softmax classifier can participate in a multilabel system; inspect the final output rather than prescribing sigmoid heads or calling every compound-fault task multilabel. |
| physics-informed neural network (PINN) | P59 author version, Section 1 and Section 3.2; P60 author version v2, Section 1 and Section 2: physical constraints inform neural surrogate models through training penalties or constrained outputs. | Two distinct chemical-engineering works, with P60 extending P59's line of work. The base category is not limited to PDE residual losses; its hard/soft variants and complete proposed names are not interchangeable. Specify the implemented physical relation and its entry point. |

Chinese wording is independently supported for selected entries below. These
translation sources do **not** enlarge that engineering corpus or certify
the performance/style claims made by their authors.

| Chinese check | Primary online locator and checked content | Status and transfer boundary |
|---|---|---|
| continual learning / 持续学习; source variant 连续学习 | [Acta Automatica Sinica c240805](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240805), bilingual title/abstract/keywords; [c220312](https://www.aas.net.cn/article/doi/10.16383/j.aas.c220312), bilingual abstract and keywords | Both explicitly identify continual learning; the latter uses 连续学习 and separately pairs class-incremental learning with 类增量学习. Preserve these scope differences. A generic incremental-learning Chinese pairing and full test-time-adjustment names have not been independently verified in this round; failed pages are not evidence. |
| feature selection / 特征选择 | [Microelectronics & Computer, 2021.1033](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2021.1033), bilingual title and abstracts; [Acta Automatica Sinica, 2017, 43(5):795-805](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.2017.c150851), bilingual title, abstracts and keywords | Both explicitly pair the base term; the latter describes ranking and redundancy removal to obtain a subset. These verify the translation, not every selection-layer variant, causal interpretation or industrial sensing-cost claim. |
| physics-informed neural network / 物理信息神经网络 | [Earth Science Frontiers, 10.13745/j.esf.sf.2025.10.38](https://jypl.pku.edu.cn/Article/info?aid=388874189), original Chinese abstract explicitly supplies the English term and abbreviation | Base translation verified. This is not admission of arbitrary physics-qualified module names or validation of the article's numerical claims. |
| feature fusion / 特征融合 | [Acta Automatica Sinica, c190428](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190428?viewType=HTML), bilingual abstract and keywords | Verified translation for combining features; image-reconstruction context, not an industrial method-prevalence claim. |
| self-attention / 自注意力 | [Acta Automatica Sinica, c220027](https://www.aas.net.cn/article/doi/10.16383/j.aas.c220027), bilingual Fig.2 caption; [c220715](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220715?viewType=HTML), bilingual abstract | Translation for self-attention, including named variants. This does not admit those variant names as general families or validate cross-attention. |
| gating mechanism / 门控机制 | [Acta Automatica Sinica, c250366](https://www.aas.net.cn/article/doi/10.16383/j.aas.c250366), bilingual abstract | Verified base translation; the source concerns expert modules in language processing, not a time-interval gate in a process model. |
| residual connection / 残差连接 | [Coal Science and Technology, 2025, 53(2):96-108](https://mtkxjs.com.cn/cn/article/pdf/preview/10.12438/cst.2024-1441.pdf), Section 1.3 and bilingual Fig.3, printed p.99 / PDF p.5; [Transactions of the CSAE, 2026, 42(7):1-11](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.202505227.pdf), Section 2.1, p.4 | Both explicitly pair the terms; the second describes addition of earlier inputs and later features. Translation evidence for a network connection, not permission to rename every parallel branch or signal remainder, or to borrow a source's full attention-module name. |
| message passing / 消息传递 | [Journal of Software, 006311](https://www.jos.org.cn/jos/article/abstract/6311), bilingual abstract | The graph-computation context matches the intended sense; not a claim that all physical information transfer is GNN message passing. |
| fuzzy clustering / 模糊聚类; fuzzy c-means / 模糊c均值 | [Acta Automatica Sinica, c200392](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200392?viewType=HTML), bilingual title and abstract | The abstract explicitly discusses traditional FCM and a source-specific robust weighted variant in wastewater monitoring. Supports the base wording, not adoption of that variant's full name as a general family. |
| diffusion model / 扩散模型 | [Journal of Software, 007511, journal issue page 413](https://ebook.xml-journal.net/rjxb/2026/04/files/basic-html/page413.html), bilingual title, abstract and Chinese keywords | Confirms generative-model terminology in an image-generation review. Does not add process-industry application evidence or justify a sensor-restoration claim. |
| graph convolutional network / 图卷积神经网络 | [Acta Automatica Sinica, c190720](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190720?viewType=HTML), bilingual Fig.8 caption | Verifies the network-name translation. The accessible caption does not independently verify every graph-convolution variant or a physical meaning for its edges; the English operation evidence is recorded above. |
| cross-attention / 交叉注意力 | [Acta Automatica Sinica, c250203](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250203?viewType=HTML), bilingual Table 1 heading and its exogenous-variable fusion entries | Verifies this base translation in a time-series review. The table groups several architectures; it does not make their query/key/value definitions identical. English operation evidence comes from P38/P43, not from counting the table's cited titles. |
| mixture of experts / 混合专家 | [Acta Automatica Sinica, c250366](https://www.aas.net.cn/article/doi/10.16383/j.aas.c250366), bilingual title, abstract and keywords | Verifies the base translation. Its language-processing model uses specialized sparse mechanisms; these are not requirements for every industrial MoE or evidence that linear experts are neural subnetworks. |
| domain adaptation / 域适应 | [Acta Automatica Sinica, c200238](https://www.aas.net.cn/article/doi/10.16383/j.aas.c200238), bilingual title and abstracts | Verifies this translation and distinguishes ordinary and complex label-space settings. It does not make identical class spaces a requirement of every adaptation study. Other Chinese variants need their own check before being called equivalent standard translations. |
| knowledge distillation / 知识蒸馏 | [Journal of Software, 006933](https://www.jos.org.cn/jos/article/abstract/6933), bilingual title and abstracts | Verifies the base translation; the abstract also distinguishes output, intermediate and graph-based knowledge. Its introductory large-teacher/small-student account is not a universal restriction on model size or task. This is translation evidence, not an additional industrial application paper. |
| class prototype / 类原型; prototype features / 原型特征 | [Acta Automatica Sinica, c240312](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240312?viewType=HTML), bilingual title, abstracts and Fig.1 caption | Verifies these feature-space terms and distinguishes a mean-based construction from that paper's adaptive construction. Its image-classification context is translation evidence, not another industrial case or permission to borrow the full module name. |
| soft assignment / 软分配 | [Journal of Image and Graphics, jig.200467](https://www.cjig.cn/zh/article/doi/10.11834/jig.200467/), original Chinese and English abstracts | Verified wording for graded assignment of embeddings to cluster centers. The English definition pair is separately recorded above; neither check turns arbitrary softmax weights into fuzzy memberships, physical-mode probabilities or a named gate. |
| max pooling / 最大池化; average pooling / 平均池化 | [Journal of University of Chinese Academy of Sciences, 2018, 35(1):75-83](https://html.rhhz.net/ZGKXYDXXB/20180110.htm), Section 1.1.2; [Microelectronics & Computer, 2023.0574](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2023.0574), bilingual abstracts | Independent translation checks. The first source defines regional maximum selection; the second names both base operations inside its own proposed variant. Neither its full variant name nor either source's performance/invariance claims are admitted by this translation record. The paired English entry above covers max pooling, not all pooling variants. |
| contrastive learning / 对比学习 | [Acta Automatica Sinica, c220421](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220421), bilingual title, abstracts, keywords and Figs.4-5 captions | Verifies the base translation and distinguishes it from the broader self-supervised-learning category. The bilingual captions also identify hard and false negative pairs; they do not turn contrastive pair labels into physical fault labels. |
| pseudo-label / 伪标签 | [Application Research of Computers, 2025.11.0460](https://www.arocmag.cn/abs/2025.11.0460), bilingual title and original Chinese abstract | Verifies the base translation in fault diagnosis. The abstract distinguishes model-generated initial labels from subsequently refined soft labels. This translation check does not admit that paper's complete optimization/module names or validate its performance claims. |
| energy function / 能量函数; energy score / 能量分数 (classifier-logit context) | [Acta Electronica Sinica, 2026, 54(1):153-166](https://www.ejournal.org.cn/zh/article/doi/10.12263/DZXB.20250761/), Section 3.1, Eq.(9), printed pp.157-158 / PDF pp.5-6, and Section 4.3, printed p.162 / PDF p.10; [author-hosted Chinese translation of Class-Specific Semantic Reconstruction for Open Set Recognition](https://mftp.mmcheng.net/Papers/22PAMI-OpenSet-cn.pdf), Section 2.2, PDF p.3 | The journal defines the logit-derived function and uses the score term; the author-hosted translation separately uses `能量分数` for OOD scoring. It is a translation linked from the author's publication list, not an official Chinese IEEE edition or a second independent definition. These checks do not verify `free energy / 自由能` in this sense, or transfer probability/calibration guarantees from nearby prose. |
| open-set recognition / 开集识别 | [Journal of Computer Applications, 2025, 45(7):2195-2202](https://www.joca.cn/CN/abstract/abstract26875.shtml), bilingual title, abstracts and keywords | Confirms the task wording: classify known classes and reject unknown inputs. The image-recognition source supplies translation evidence, not another industrial application or admission of its full component names. |
| missing-value imputation / 缺失值插补 | [Acta Automatica Sinica, c230534](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230534?viewType=HTML), bilingual title and abstracts | Verified base translation in wind-turbine measurement completion. Its full network name and claimed performance are not admitted by this translation check. |
| reconstruction loss / 重构损失 | [Advanced Engineering Sciences, 2022, 54(5):240-248](https://scuaes.ijournals.cn/html/2022/5/202100675.html), bilingual abstracts and paired keywords | Verified loss-name translation in image inpainting. This does not establish a universal mask, industrial restoration capability or equivalent wording for every reconstruction objective. |
| distribution alignment / 分布对齐 | [Acta Automatica Sinica, c250653](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250653?viewType=HTML), bilingual abstracts | Verified wording for a representation-distribution constraint in KPI forecasting with missing variables. The abstract is translation evidence, not verification of its full architecture, theory or results. |
| maximum mean discrepancy / 最大均值差异 | [Acta Automatica Sinica, c190593](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190593?viewType=HTML), bilingual abstracts | Verified base loss/regularizer wording in bearing fault detection. Does not admit the source's full improved variant or establish equivalence to mutual information. |
| slow feature analysis / 慢特征分析 | [Acta Automatica Sinica, c201035](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201035?viewType=HTML) and [c230154](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230154?viewType=HTML), bilingual abstracts and keywords | Both explicitly pair the base name with SFA in process operating-performance assessment. Their KPI-driven and distributed/dynamic variants are not thereby admitted as universal module names. Translation evidence does not validate those variants' equations or experiments. |
| multi-label learning / 多标签学习 | [Microelectronics & Computer, 2022.0266](https://mc.spacejournal.cn/cn/article/doi/10.19304/J.ISSN1000-7180.2022.0266), bilingual title and abstracts; [Journal of Software, 2024, 35(6):2775-2794, issue page 199](https://ebook.xml-journal.net/rjxb/2024/06/files/basic-html/page199.html), bilingual title and abstract opening | Both explicitly pair the base wording. The former also defines association of a sample with multiple labels. These general learning/software contexts verify translation, not process-industry prevalence, the source-specific feature-selection methods, or physical fault interaction. |

Other Chinese counterparts and other method-family names have not all received
this completed paired record. Keep them as source-attributed or definition-based
working terminology until checked for the requested recommendation. In
particular, the scoped P33/P48 assignment pair does not admit every soft
assignment mechanism, and paired base MoE or cross-attention records do not admit
all source-specific variants. Modified adaptation/distillation names and other
candidate definitions still require their own completed records. This is a limit of this
ledger, not a claim that these methods occur only once in the field.

`Cross-stage feature fusion`, `process-topology-guided integration` and similar
compositional phrases above describe an operation only when the manuscript
implements it. Their head words do not certify a conventional named module.
Where an author defines a specific name, keep that identity separate from the
shared-bank recommendation. More source checks should extend the evidence rows,
not turn this incomplete snapshot into an automatic whitelist or blacklist.
