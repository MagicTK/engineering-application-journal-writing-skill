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
model operation. Corpus absence is not a prohibition.

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

| Model action | Preferred term | Boundary |
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

Preferred patterns:

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
boundary. A term copied from an author draft is not evidence for inclusion.

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
