# Context-Sensitive Terminology Decisions

Use this alongside the [terminology bank](engineering-application-terminology-bank.md), not as a replacement dictionary. Published use establishes that a term can be legitimate; it does not establish that it describes this manuscript's object. Source IDs refer to the [published evidence index](published-evidence.md). Author preferences belong in the individual manuscript's terminology map.

## Decision Procedure

1. Identify the referent: physical quantity, acquired observation, sample, latent feature, condition, learned state, or model operation.
2. Inspect the sentence, the definition/equation, and its recipient. Do not infer an operation from a module name alone.
3. Check comparable published contexts. Search exact phrases and inflections, excluding references and quoted titles; inspect whether a match is a noun, verb or citation.
4. Classify the decision: correct; correct but needs definition; author preference; ambiguous; scientifically inconsistent; evidence unavailable.
5. Propose a local clause-level change only if needed, with source/page and rationale. Never run global substitution on these entries.

No search hit means **not found in this searched corpus**, not ungrammatical or forbidden. Search frequency is not a measure of scientific correctness. The optional terminology audit script only finds candidates for human review.

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

P05-P06 use semantic attributes for zero-shot fault categories; P20 uses graph-node attributes. These uses are compatible with preferring `process variables` for physical measurements. The word `attribute` as a verb in an explanation is unrelated to that decision.

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

Do not replace `state` with `condition` merely for fluency: a continuously changing local representation is not automatically a discrete operating regime. `Local operational state` is usable if the model actually adapts to local measured behavior; it should not silently assert that the model identifies physical states. Never introduce `prototype state` when the method has no defined prototype.

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

## Structure And Operations

| Distinction | Decision |
|---|---|
| intra-stage / inter-stage / cross-stage | intra = within a stage; inter = between stages; cross = across stage boundaries. `Inter-stage relationships` and `cross-stage fusion` can coexist coherently. Do not reverse intra/inter or force identical prefixes onto different roles. |
| stage-wise / stage-level / stage-structured | stage-wise describes separate treatment; stage-level describes granularity; stage-structured claims a retained arrangement. Use the last only when that structure is actually retained and defined. |
| partition / grouping / clustering | partition may be fixed by knowledge; grouping may be learned or predefined; clustering implies a defined data-driven grouping mechanism. Soft assignments need not yield hard clusters. |
| aggregation / fusion / interaction | aggregation summarizes a set; fusion combines information sources; interaction models influence. They overlap in some designs but are not automatic synonyms. |
| relationship / dependency / correlation | relationship is broad; dependency is statistical or modeled dependence, not automatically causation; correlation needs a defined statistic or justified usage. |
| topology / prior / constraint | identify the engineering source and mathematical role. An additive attention bias is not necessarily a hard constraint or a causal graph. |
| spatial / spatiotemporal | define the physical, topological or graph relation and the temporal axis. Tensor column order alone establishes neither. |
| gate / attention / fusion module | a gate regulates a contribution; attention computes weighted relations/aggregation; a fusion module combines paths. Verify shapes and operations instead of interchanging names. |
| unified / global / plant-wide representation | name the scope actually represented. Combining two paths does not itself prove universal generalization or complete plant coverage. |

## Topic-Specific Terms

- **Multi-rate:** sampling rate, sampling interval, asynchronous observation and missingness are different properties. Repeated/static values do not create a temporal signal. See P08 and P23-P26.
- **Limited supervision:** few-shot counts labeled examples; zero-shot requires a clear unseen-class definition and available semantics; semi-supervision uses labeled and unlabeled data; weak supervision may use bags or coarse labels; self-supervision specifies how targets arise. These settings are not interchangeable. See P05-P06 and P17-P22.
- **Fuzzy models:** membership degree is not automatically a calibrated probability; define rules, memberships and aggregation. An evidential uncertainty score is a different object unless the method establishes a connection. See P07.
- **Knowledge-guided models:** distinguish expert rules, process topology, physical laws and learned similarities. A prior's provenance and role matter more than the adjective. See P04, P12-P14.
- **Quality-related diagnosis:** explain the measured quality target and its relation to process behavior. Avoid repeating a particular defect name throughout the abstract and experiment overview. See P09 and P16.

## Reporting And Scope

`Real-world data` describes provenance, not online operation. Do not routinely prefix it with `offline`; retain the distinction if retrospective versus prospective evaluation matters. Class imbalance belongs in dataset/metric analysis when relevant. Mention it in an abstract or contribution only when it is part of the research problem or supported advance, not merely a property of one case.

`Experimental settings` is a useful ordinary heading. `Evaluation protocol` is also legitimate when a reproducible evaluation procedure is genuinely being defined. An author's preference against it is not a field-wide ban.

The non-negotiable restrictions concern false meaning: fabricated results/citations, invented input semantics, unsupported causal/deployment/generalization claims, and concealed selection leakage. No ordinary word alone establishes any of these failures.
