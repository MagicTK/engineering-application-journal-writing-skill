# Argument And Prose Craft For Engineering Applications

## Purpose

Use this guide to turn a supported engineering contribution into coherent manuscript prose. It is self-contained: the writing procedure does not require another installed Skill. Apply it after identifying the engineering task, available evidence, and the actual contribution. Language revision must preserve the science and expose missing support in author notes.

The intended reader studies an engineering object: a process, equipment item, production line, sensing arrangement, or operating decision. Keep that object visible while explaining diagnosis, monitoring, root-cause analysis, soft sensing, anomaly detection, or another task. Introduce AI operations when their role in that task becomes clear.

## 1. Choose The Argument From The Contribution

Use [contribution routes](contribution-narratives.md) for route selection and its evidence requirements. Problem novelty and method novelty are separate questions. A manuscript can contribute through a new formulation, interacting conditions, a mechanism for an established problem, engineering adaptation, or a focused comparative finding. Several routes can coexist.

In prose, give the dominant route the emphasis it needs: define what changes in a new formulation; explain the interaction for a coupled-condition study; connect the remaining capability to the mechanism for an established task; and show which operating requirement makes an adaptation necessary. An empirical contribution should explain what the comparison teaches about the engineering task. Classify the work from its formulation and evidence before choosing a label.

The contribution list should follow these actual advances. It has no preset item count. Keep related mechanisms together when they support one claim. A long module list and a blanket best-performance claim do not substitute for a clear advance.

## 2. Build The Engineering Argument

Construct an internal argument map before drafting:

`engineering objective -> relevant operating condition -> established capability -> remaining requirement -> design response -> discriminating evidence -> engineering implication`

Each arrow must express a reason. An operating condition may change which measurements are available; that change may invalidate an assumption; a mechanism may then preserve information that the decision requires. Explain those links using the manuscript's facts. A chain of adjectives cannot supply them.

For each central claim, record:

| Field | What the author must supply |
|---|---|
| Engineering objective | The decision or quantity that matters in the process |
| Relevant condition | The measured or specified constraint, including its source |
| Closest prior capability | What the cited approach accomplishes under its reported assumptions |
| Remaining requirement | The exact capability relevant to this manuscript and why it remains open |
| Design response | The operation that responds to that requirement |
| Evidence | The comparison, intervention, measurement, or analysis that tests the claim |
| Implication | What the evidence changes for the engineering task |

The map is an authoring aid. Do not paste its field labels or audit language into the manuscript. If a field is unsupported, record the missing source or experiment in an author note and draft the supported parts.

## 3. Compare Prior Work Fairly

First explain a method family's achievement and the conditions enabling it. Then identify the difference relevant to the current study. Attribute only claims verified in the source.

Distinguish three statements:

- **An assumption is specified:** the source states or the implementation requires it. Explain its relevance to the current condition.
- **A setting was not evaluated:** the reported evidence leaves performance in that setting unresolved. This does not establish failure there.
- **A limitation was observed:** the source or a documented, fair reproduction measures the limitation. State the tested condition and measurement.

Avoid collective accusations such as “existing methods ignore industrial complexity” and unsupported claims about what authors failed to consider. Describe the relevant methods, assumptions, and evidence. Use “first,” “unexplored,” and “no existing method” only when a documented literature search supports that scope.

For a focused comparison, justify the reference method by task relevance and comparable assumptions. Report improvement relative to the evaluated references. A focused comparison need not claim superiority to every method, and it must still include the closest relevant alternatives when they could change the conclusion.

Generalization is an evaluation claim. Identify what changes between training and evaluation, such as operating regimes, time periods, equipment, or sites. Robustness to a specified missing-data pattern does not by itself establish transfer to another plant. Link practical value to a measured quantity such as false alarms, detection delay, estimation error, annotation effort, or resource demand when that quantity is available.

## 4. Make Sentences Carry The Reasoning

Use these as editing questions, not rigid sentence templates:

1. **Known to new:** does the opening connect to a defined object or the preceding result before introducing the next concept?
2. **Subject and action:** can the reader identify what performs the operation, what changes, and under what condition? Keep the subject near its verb.
3. **Emphasis:** does the sentence end on the information the reader should carry forward?
4. **Specific reference:** replace an ambiguous “this” with “this missingness pattern,” “this comparison,” or the appropriate object.
5. **Information gain:** does the sentence add a fact, relation, operation, evidence, or necessary inference? Delete statements that only announce importance or clarity.
6. **Claim strength:** is an observation presented as an observation, an explanation as an inference, and a hypothesis as something to test?

Prefer verbs that name operations: estimate, constrain, align, propagate, compare, or measure. Keep conventional passive constructions when the measured object deserves emphasis. Preserve an accurate verb such as “combine” or “extend” when it describes the work; replacing it with “develop” cannot increase scientific novelty.

## 5. Give Each Paragraph One Main Job

Write a one-line author note describing the paragraph's purpose. Then check whether each sentence advances it. A paragraph may establish a phenomenon, compare a method family, derive a requirement, explain a mechanism, interpret a result, or discuss a transfer condition.

A useful progression is point -> supporting facts or reasoning -> implication. A paragraph need not end with a summary when the reasoning already reaches its destination. Transitions should carry substantive links: the changed condition, the remaining requirement, or the consequence of the previous operation. Repeated “Furthermore” or “To address this issue” cannot establish those links.

When successive paragraphs motivate different parts of a method, identify what changes between them. One may concern **which relationships are represented**, another **which temporal information is available**, and another **what supervision constrains learning**. These are useful distinctions only when supported by the paper. The next paragraph should introduce its own consequence, not repeat `complex dependencies remain challenging` with different module names. Conversely, one underlying problem can motivate several cooperating operations; do not invent a separate research gap for each component.

Checked examples show several valid structures: P04 moves from structural information to a frequency-representation question; P08 develops one information-granularity issue using an illustrative sampling example; P17 distinguishes scarce quality labels from degraded measurements; P34 relates quality relevance to incomplete multirate observation. These are observations about argument organization, not endorsements of every broad limitation claim in those papers. Use [the source locations](published-evidence.md) and retain only distinctions established for the current study.

For Related Work, arrange the progression around changing capabilities and assumptions. For example, a discussion may move from learning with complete measurements, to using partial observations, to jointly handling observation loss and scarce labels. Use that sequence only when the cited literature and the paper's task support it. Explain what each family enables and which condition motivates the next family. The sequence need not be chronological, and each subsection need not end by criticizing prior work.

If Related Work is integrated into the Introduction, first map each retained paragraph to its role: establish prior capability, compare assumptions, support a remaining requirement, or supply essential context. Place its evidence near the claim it supports, combine overlapping summaries, and write the connecting sentence around the shared object. Preserve useful opening/closing logic without preserving every original sentence. Do not remove the entire evidence chain because its section heading disappears, or move citations so far that they appear to support a different claim.

For Results, distinguish the roles of text and figures. The text states and interprets the supported finding; a caption identifies the setup, plotted quantities, and enough context to read the figure. Keep them consistent without requiring the same conclusion to appear three times.

## 6. Remove Defensive And Empty Prose

Classify a flagged sentence before editing it:

| Function | Treatment |
|---|---|
| Protective metadiscourse or imagined objection | Delete when it adds no scientific information |
| Repeated claim about importance, clarity, or novelty | Replace with the specific finding or delete |
| Necessary scope condition | State the evaluated scope directly; keep it close when omission would mislead |
| Methodological limitation | Describe its effect on interpretation in Methods or Discussion |
| Real uncertainty | Name its source and calibrate the verb |
| Substantive contrast | Retain when the distinction is part of the argument |

Flag habitual “not X but Y,” “we do not claim,” “to avoid misunderstanding,” “it should be emphasized,” and “this further clarifies.” They are inspection cues, not forbidden strings. Retain a meaningful distinction, such as fault localization versus causal identification, when the reader needs it. Remove the surrounding self-protection.

Keep an essential qualifier in the Abstract or result sentence when the claim would otherwise change meaning. Put detailed design limits in Methods and their practical consequences in Discussion. Repetition is warranted only when another statement independently needs the boundary to remain accurate.

Do not remove uncertainty to sound confident, soften a confirmed result into multiple hedges, or add unmeasured benefits while polishing. Natural academic style follows from precise objects, informative verbs, and cumulative reasoning. Evaluate language by information, logic, and evidence. Vocabulary, punctuation, and sentence length cannot establish whether a passage was AI-generated; do not impose mechanical word bans, punctuation quotas, sentence-length quotas, or AI-detection probability targets. Do not introduce artificial variation merely to change a surface pattern.

## 7. Small Engineering Revision Examples

These examples demonstrate language choices in hypothetical settings. They report no project findings and supply no experimental numbers. The revised prose is usable only when the stated prerequisite is confirmed; otherwise retain the issue in author notes. Literature citations must come from verified sources.

### A. An Established Problem With A Specific Remaining Requirement

**Author diagnosis:** the problem is fault diagnosis with incomplete measurements. The draft's “entirely new problem” label has no support. The relevant cited methods require a fixed sensor set, while the current study addresses varying sensor availability. Verify that distinction before drafting.

**Before:** “Existing methods ignore the complexity of real industry. We therefore propose an entirely new fault-diagnosis problem and a revolutionary framework.”

**Manuscript prose after verification:** “The cited methods diagnose faults using a fixed sensor set. Sensor availability varies in the process considered here, requiring diagnostic decisions from different subsets of measurements. The proposed aggregation rule operates on the measurements available in each window.”

The final sentence requires a method that actually performs that operation. Add citations to the first sentence and a source for the operating condition. The paragraph makes no performance claim.

### B. A Coupled Condition Requiring Investigation

**Author diagnosis:** sparse labels and changing operating conditions are both present. Their interaction is a proposed motivation; the mechanism and empirical effect still need evidence.

**Before:** “Few labels and unknown conditions create a fundamentally new problem that previous studies cannot solve.”

**Manuscript prose for a study question:** “This study examines fault diagnosis when labeled examples are scarce and operating conditions change. The evaluation tests how these conditions jointly affect diagnosis and whether the proposed adaptation mechanism reduces the resulting error.”

Use this wording for an evaluation the manuscript actually specifies. To claim a new coupled problem, additionally establish the distinguishing interaction and its relation to the closest formulations. Do not turn a planned test into a completed result.

### C. A Direct Scope Statement

**Author diagnosis:** only historical production records have been evaluated. The scope belongs beside the data description; the paper cannot claim deployed benefit.

**Before:** “We do not claim that the method has already been deployed, and this should not be taken to imply that it resolves every practical issue.”

**Manuscript prose:** “The evaluation uses historical production records from the studied process.”

If timing or feedback affects interpretation, specify it in the experimental design and discuss the required prospective validation. The short sentence alone must not erase such a material limit.

### D. Information Flow In A Method Paragraph

**Author diagnosis:** the method includes a valid indicator for unavailable measurements; its use in the estimator is confirmed.

**Before:** “A mask is introduced. Furthermore, missing data are important. This allows the model to effectively extract better features.”

**Manuscript prose:** “Unavailable sensor readings are marked by a binary mask. The estimator uses this mask to separate observed values from imputed inputs.”

The second sentence develops the object introduced by the first and names the operation. Any accuracy benefit requires separate evidence.

### E. A Quantitative Result That Has Not Been Supplied

**Before:** “The excellent results further clarify the superiority and generalization ability of our method.”

**Author diagnosis:** identify the metric, comparator, evaluation condition, measured difference, and uncertainty. Determine whether the split actually tests generalization.

**Author-only drafting scaffold:** “Under [verified condition], [method] achieves [measured metric] compared with [verified comparator result]. [Additional analysis] supports [specific interpretation].”

This scaffold is not manuscript-ready. Obtain the real values and supporting analysis, or restrict the draft to verified observations. Do not fill the gaps with plausible numbers or substitute another unsupported adjective.

### F. Two Requirements Without Repeating One Gap

**Synthetic, confirmed setting:** the process has a known unit map, and measured response patterns vary over time within those units. The method uses the map for fixed unit membership and learns input-dependent weights inside each unit. No claim about all existing methods is supplied.

**Local transition:** "The unit map specifies where the measurements originate. The observed response patterns vary within these units. An input-dependent weighting mechanism represents these variations while retaining the unit membership."

The connection is between a fixed structural assignment and a changing modeled contribution, not between `good knowledge` and `bad data`. This example explains a design reason, not a demonstrated accuracy gain or proof that learned weights measure diagnostic relevance. It need not be used in a method without those two confirmed properties. For a time-frequency paper, replace this reasoning with its actual temporal or spectral requirement rather than importing a grouping narrative.

## 8. Delivery And Final Pass

Separate the output into manuscript text and concise author notes when unresolved support exists. Author notes identify the source, experiment, or scientific decision needed; the manuscript contains the supported argument. Use visibly marked placeholders only in an internal draft. Do not silently resolve scientific uncertainty through language edits.

Check that the contribution route matches the work; prior capability is represented fairly; each claimed improvement has matching evidence; paragraphs advance through substantive links; essential scope survives; and empty praise, protective metadiscourse, and repeated conclusions have been removed. Preserve formulas, citations, measured values, author terminology locks, and layout constraints.

## Adaptation Note

This guide adapts general practices examined in `anti-defensive-writing`, `research-writing-skill`, `ml-paper-writing`, and `systems-paper-writing`: direct claims with necessary precision, evidence-preserving revision, reader-oriented information order, and traceable design arguments. The engineering examples and procedures here are newly written. Conference page budgets, fixed contribution counts, repetition formulas, and promotional novelty vocabulary are not adopted. Source provenance and currency are tracked at suite level.
