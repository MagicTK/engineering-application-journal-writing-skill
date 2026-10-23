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

A learned fuzzy state (P07), a discrete operating mode and a physical state-space variable have different definitions. Preserve those definitions even when `state` occurs in all three. A process disturbance is an input or event that perturbs behavior, not a synonym for the condition under which measurements were obtained.

Do not replace `state` with `condition` merely for fluency: a continuously changing local representation is not automatically a discrete operating regime. `Local operational state` is usable if the model actually adapts to local measured behavior; it should not silently assert that the model identifies physical states. Never introduce `prototype state` when the method has no defined prototype.

For `dynamic` or `adaptive`, identify **what changes**. Input-conditioned attention, group assignments or gates can change on every prediction while trained parameters remain fixed. A recurrent state or rolling reference statistic can also update without fitting model parameters. Online learning or test-time parameter adaptation is a different claim, requiring an actual update rule and its permitted information. P24's elapsed-interval weighting and P04's rolling anomaly-score statistics illustrate different changing objects; neither name alone establishes continual learning. Describe the verified operation directly, such as `input-dependent grouping`, without banning an accurately defined adaptive mechanism.

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

`Feature selection` retains a subset of defined descriptors; `feature extraction` constructs descriptors, and `sensor selection` changes which physical measurements are required. P40 returns selected feature indices. Several retained spectral or statistical features may still require every original sensor and its preprocessing. State the reduced object before claiming fewer sensors, cheaper acquisition or faster inference.

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

## Structure And Operations

| Distinction | Decision |
|---|---|
| intra-stage / inter-stage / cross-stage | intra = within a stage; inter = between stages; cross = across stage boundaries. `Inter-stage relationships` and `cross-stage fusion` can coexist coherently. Do not reverse intra/inter or force identical prefixes onto different roles. |
| stage-wise / stage-level / stage-structured | stage-wise describes separate treatment; stage-level describes granularity; stage-structured claims a retained arrangement. Use the last only when that structure is actually retained and defined. |
| partition / grouping / clustering | partition may be fixed by knowledge; grouping may be learned or predefined; clustering implies a defined data-driven grouping mechanism. Soft assignments need not yield hard clusters. |
| aggregation / fusion / interaction | aggregation summarizes a set; fusion combines information sources; interaction models influence. They overlap in some designs but are not automatic synonyms. |
| relationship / dependency / correlation | relationship is broad; dependency is statistical or modeled dependence, not automatically causation; correlation needs a defined statistic or justified usage. |
| topology / prior / constraint | identify the engineering source and mathematical role. An additive attention bias is not necessarily a hard constraint or a causal graph. |
| causal convolution / predictive dependence / physical causation | A causal convolution excludes future inputs from a specified output; predictive dependence concerns information useful for prediction. Neither alone identifies a physical intervention effect or root cause. |
| spatial / spatiotemporal | Define the represented axis or relation: physical layout, process topology, graph neighborhood, or explicitly defined inter-variable structure. For spatiotemporal, identify the time axis too. Model-grid adjacency does not establish physical proximity or process coupling. |
| gate / attention / fusion module | a gate regulates a contribution; attention computes weighted relations/aggregation; a fusion module combines paths. Verify shapes and operations instead of interchanging names. |
| unified / global / plant-wide representation | name the scope actually represented. Combining two paths does not itself prove universal generalization or complete plant coverage. |

For `stage`, first distinguish a production unit, a temporal phase in a batch, and a learning phase. For `local/global`, identify the domain over which locality is defined. A temporal receptive field is not a plant region. For `propagation`, distinguish graph-feature updates from a physical disturbance spreading through the process. These decisions change scientific meaning, not merely style.

For `mask`, `sparse` and `constraint`, inspect where the operation acts. A zero-valued attention edge, zeroed logit, excluded class and unexecuted expert are different outcomes. Finite zeroed logits still receive positive softmax probability; ordinary dense softmax also does not establish sparse execution. Likewise, a block-diagonal graph restricts that graph operation, not necessarily later feature mixing or physical dependence between units. Keep the abstract's benefit at the level the full computation supports.

## Topic-Specific Terms

- **Multi-rate:** for a uniformly sampled stream, sampling frequency `f` (observations per unit time) and sampling period `Delta t` satisfy `f = 1 / Delta t`. A longer period means a lower frequency, not a higher one. Check units and definitions before translating a source's rate-group index or interval multiplier into `sampling rate`; P08's numbered groups and P24's elapsed intervals require this distinction. For irregular observations, report the relevant interval information rather than assuming one fixed period. Asynchrony, missingness and model-window duration are additional properties; repeating a static value does not create acquired temporal information.
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

## Reporting And Scope

`Real-world data` describes provenance, not online operation. Do not routinely prefix it with `offline`; retain the distinction if retrospective versus prospective evaluation matters. Class imbalance belongs in dataset/metric analysis when relevant. Mention it in an abstract or contribution only when it is part of the research problem or supported advance, not merely a property of one case.

`Offline assay` may accurately identify a laboratory measurement procedure or delayed quality label; it is not the same as calling every industrial dataset offline. `Online` may identify sequential computation or actual live evaluation; define which. Deployment requires operational integration, and shadow-mode evaluation does not demonstrate closed-loop benefit.

Task names also require definitions. Detection may denote an alarm, while diagnosis may identify a fault class, location or cause; published usage varies (P02). Inspect the target and evaluation before correcting a name. Quality prediction may target a continuous measurement or a quality category (P09); class labels must not be rewritten as continuous quality variables for apparent consistency.

In continuous monitoring, `window-level`, `pointwise`, `point-adjusted` and `event-level` describe distinct evaluation objects or scoring rules. A positive window does not locate the anomalous point inside it. Filling a labeled interval after one hit changes the reported score, not the emitted alarm times; P07 and P22 use different choices. `Inference time` measures a defined computation, while `detection delay` relates an actual alarm to a reference onset and required information availability. `Early warning` additionally needs a defined advance-warning target; fast computation alone supplies none of these temporal claims. See [monitoring evaluation](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when).

`Experimental settings` is a useful ordinary heading. `Evaluation protocol` is also legitimate when a reproducible evaluation procedure is genuinely being defined. An author's preference against it is not a field-wide ban.

The non-negotiable restrictions concern false meaning: fabricated results/citations, invented input semantics, unsupported causal/deployment/generalization claims, and concealed selection leakage. No ordinary word alone establishes any of these failures.
