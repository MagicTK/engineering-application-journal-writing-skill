# Engineering-Application Terminology Bank

## Scope And Evidence Boundary

This reference supports writing for industrial, control, automation, process,
manufacturing, and equipment-oriented journals. The current release provides a
[40-paper published evidence index](published-evidence.md) and
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
| Weighted combination into a context vector | feature aggregation; context aggregation | appropriate for attention-weighted sums |
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
enters the model. Published examples include P04 and P12-P14 in the evidence index.

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
| feature fusion | P01 p.1 combines stage-wise representations; P03 p.1 combines temporal/series features; P14 pp.1-2 combines representations across scales/subgraphs. | Different fusion sources and levels; none licenses an arbitrary `causal`, `reliable` or topology-qualified name. |
| attention mechanism / self-attention | P11 p.3 and P24 p.3 define query/key/value weighting with the self-attention inputs drawn from the same representation. | The checked common operation does not make all source-specific attention variants equivalent, causal or physically interpretable. |
| gating mechanism | P08 p.5 uses multiplicative feature gating; P19 p.5 computes scale weights; P33 p.6 gates attention outputs. | Same general regulating role, different inputs and recipients. This does not establish an `age`-qualified module family. |
| residual connection | P02 p.3 describes the residual backbone connection; P14 p.2 specifies an additive residual operation. | Check addition and any projection. A generic bypass, concatenation or any parallel branch is not automatically the same residual operation. |
| message passing | P13 p.3 aggregates graph-node information; P14 p.4 updates features through graph convolutional propagation. | Graph computation, not evidence of physical fault propagation or communication-network transfer. |
| fuzzy clustering; fuzzy c-means (FCM) | P28 p.3, Eqs.(4)-(7) and Algorithm 1, uses membership-weighted distances and alternating center/membership updates; P33 pp.3-4, Section III-C and Eqs.(5)-(6), defines FCM before its clustering architecture. | Same base clustering algorithm, different roles: reservoir-feature reinforcement versus incomplete-series clustering. The sources are machinery and general time-series studies. Their full network names, reinforcement steps and imputation mechanisms are not interchangeable. |
| diffusion model | P32 p.3, Section III-A, defines artificial forward noising and learned reverse generation for sequences; P35 p.3, Section III-A and Eq.(14), applies conditional diffusion to compressed features and decodes generated signals. | Common generative operation, different generated objects and conditioning. This does not establish sensor-noise restoration, identical inference cost or a universal industrial diffusion-module name. |
| graph convolution; graph convolutional network (GCN) | P07 p.7, Eqs.(18)-(19), combines normalized adjacency, feature projections and a gated nonlinearity; P14 p.4, Eqs.(33)-(34), uses adjacency-weighted feature projection and ReLU. | Common graph-feature computation, not identical graphs: variable-time nodes versus process-variable nodes. A GCN operation does not establish a physical or causal meaning for learned edges. |

Chinese wording is independently supported for selected entries below. These
translation sources do **not** enlarge the 40-paper industrial corpus or certify
the performance/style claims made by their authors.

| Chinese check | Primary online locator and checked content | Status and transfer boundary |
|---|---|---|
| feature fusion / 特征融合 | [Acta Automatica Sinica, c190428](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190428?viewType=HTML), bilingual abstract and keywords | Verified translation for combining features; image-reconstruction context, not an industrial method-prevalence claim. |
| self-attention / 自注意力 | [Acta Automatica Sinica, c220027](https://www.aas.net.cn/article/doi/10.16383/j.aas.c220027), bilingual Fig.2 caption; [c220715](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220715?viewType=HTML), bilingual abstract | Translation for self-attention, including named variants. This does not admit those variant names as general families or validate cross-attention. |
| gating mechanism / 门控机制 | [Acta Automatica Sinica, c250366](https://www.aas.net.cn/article/doi/10.16383/j.aas.c250366), bilingual abstract | Verified base translation; the source concerns expert modules in language processing, not a time-interval gate in a process model. |
| message passing / 消息传递 | [Journal of Software, 006311](https://www.jos.org.cn/jos/article/abstract/6311), bilingual abstract | The graph-computation context matches the intended sense; not a claim that all physical information transfer is GNN message passing. |
| fuzzy clustering / 模糊聚类; fuzzy c-means / 模糊c均值 | [Acta Automatica Sinica, c200392](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200392?viewType=HTML), bilingual title and abstract | The abstract explicitly discusses traditional FCM and a source-specific robust weighted variant in wastewater monitoring. Supports the base wording, not adoption of that variant's full name as a general family. |
| diffusion model / 扩散模型 | [Journal of Software, 007511, journal issue page 413](https://ebook.xml-journal.net/rjxb/2026/04/files/basic-html/page413.html), bilingual title, abstract and Chinese keywords | Confirms generative-model terminology in an image-generation review. Does not add process-industry application evidence or justify a sensor-restoration claim. |
| graph convolutional network / 图卷积神经网络 | [Acta Automatica Sinica, c190720](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190720?viewType=HTML), bilingual Fig.8 caption | Verifies the network-name translation. The accessible caption does not independently verify every graph-convolution variant or a physical meaning for its edges; the English operation evidence is recorded above. |

Other Chinese counterparts and other method-family names have not all received
this completed paired record. Keep them as source-attributed or definition-based
working terminology until checked for the requested recommendation. In
particular, a single checked soft-clustering example (P33), cross-attention
example (P38), or mixture-of-experts example (P36) is not a two-paper admission
record for that complete category. This is a limit of this ledger, not a claim
that these methods occur only once in the field.

`Cross-stage feature fusion`, `process-topology-guided integration` and similar
compositional phrases above describe an operation only when the manuscript
implements it. Their head words do not certify a conventional named module.
Where an author defines a specific name, keep that identity separate from the
shared-bank recommendation. More source checks should extend the evidence rows,
not turn this incomplete snapshot into an automatic whitelist or blacklist.
