# Section Writing Guide

## Purpose

Use this reference when planning or restructuring a complete engineering-application manuscript. Select the relevant manuscript archetype first.

Then identify the supported contribution route: a new problem/formulation, an interaction between familiar conditions, a mechanism for an established problem, an engineering adaptation/integration, or a focused comparative finding. These routes can coexist. Use [argument and prose craft](argument-and-prose-craft.md) to connect the engineering objective, prior capability, remaining requirement, mechanism, and evidence.

The sequences below describe section functions. Merge or omit functions that do not serve the manuscript; do not treat them as fixed sentence counts, paragraph counts, page allocations, or mandatory mechanisms. Follow current target-journal requirements when formatting a real submission.

## Contents

Title; Abstract; Introduction; Related Work; problem statement/formulation; framework and method; experiment settings and case studies; results, ablation, sensitivity, robustness and interpretation; Discussion; Conclusion; captions.

## 1. Title

A good title identifies:

- the technical contribution or modeling idea;
- the engineering task;
- the application scope when it is scientifically important.

Method-oriented pattern:

`[Method or design idea] for [engineering task] in [process class]`

Application-oriented pattern:

`[Engineering task] in [specific process or equipment] using [method family or engineering mechanism]`

Avoid titles that are only an acronym plus a list of fashionable modules. Keep the acronym only when it is memorable, stable, and used throughout the manuscript.

## 2. Abstract

### Method With Benchmark And Real-World Validation

Recommended functions:

1. General engineering context and the main difficulty.
2. Specific limitation of existing methods.
3. Proposed method and its purpose.
4. Principal mechanism and the requirement it addresses.
5. Any additional operation essential to that mechanism or its output, with the actual relationship made clear.
6. Benchmark and real-world case studies.
7. Evidence-based conclusion on effectiveness and practical relevance.

Do not report every module or every metric. The abstract should explain the organizing idea.

Combine the mechanism functions when the method has one principal idea. For an established problem, make the remaining capability and the design response clear without manufacturing a new problem. For a coupled-condition contribution, state what the interaction changes. An empirical or application contribution may instead emphasize the engineering finding and the conditions that make it useful.

### Background-Driven Application

Recommended functions:

1. Specific process/equipment objective and why it matters.
2. Operational or measurement difficulty in that setting.
3. Limitation of current practice or available methods.
4. Proposed engineering solution.
5. How process knowledge, data characteristics, or operational constraints shape the method.
6. Evaluation under relevant production conditions.
7. Main engineering finding and practical implication.

Do not make a site-specific study sound universally validated. State the scope precisely.

### System Or Automation Framework

Recommended functions:

1. Operational task and system context.
2. Limitation in current workflow, integration, timing, or decision support.
3. Proposed system or framework.
4. Core architecture and information flow.
5. Evaluation scenario and system-level metrics.
6. Operational implication and remaining boundary.

## 3. Introduction

### Shared Requirements

The Introduction must answer:

- Why does the engineering task matter?
- What property of the actual process/data makes it difficult?
- What has already been attempted?
- Why is the gap still unresolved?
- Why is the proposed design a logical response?
- What exactly is contributed and evaluated?

State the contribution at its actual level. A new formulation requires a substantive difference in the task, information, decision, or constraints. A method paper can address a familiar task by overcoming an evidenced limitation under a stated condition. An application paper can establish value through a necessary adaptation or validated engineering insight. Present each route with its appropriate evidence rather than equating novelty with a new task name.

### Method-Oriented Introduction

Suggested paragraph sequence:

1. Industrial task and plant/process significance.
2. Established data-driven approaches and the capabilities they provide.
3. The specific structural, temporal, statistical, or operating challenge.
4. Related solution family, the assumptions relevant to the stated challenge, and the remaining capability supported by source evidence.
5. Optional motivation figure and the exact distinction it illustrates.
6. Additional representation requirement if central to the method.
7. Proposed framework and design logic.
8. Contributions.
9. Paper organization, if it helps navigate an unfamiliar structure.

Connect the motivation figure to the paragraph's scientific distinction, rather than inserting an isolated caption-like description. Starting with `Fig. 1 illustrates ...` is not itself an error if the sentence develops the argument. Preserve a settled author preference for another construction without turning it into a universal ban.

Before adding another challenge paragraph, check whether it introduces a different information requirement or merely restates the previous gap. Structural organization and temporal representation can be complementary dimensions; they are not opposing methods merely because one paragraph follows the other. Choose a contrast marker only for an actual contrast. For guidance on preserving the logic of Related Work during integration, see [paragraph connections](argument-and-prose-craft.md#5-give-each-paragraph-one-main-job).

### Background-Driven Introduction

Suggested paragraph sequence:

1. Process/equipment background and operational importance.
2. Existing industrial practice and its limitations.
3. Data-generation mechanism, operating variability, and practical constraints.
4. Existing analytical or data-driven approaches.
5. Gap between those approaches and the actual application need.
6. Proposed solution derived from the process background.
7. Contributions and engineering significance.

The specific application should remain visible throughout. Do not replace it with a generic time-series problem after the first paragraph.

### Contribution List

Group the actual contributions into the smallest clear set. A formulation, mechanism, engineering adaptation, and empirical finding are possible contribution types; none is mandatory. Do not pad the list to a preset count or treat every module as an independent advance.

Each item should identify the object, the substantive advance, and the evidence that can test it. An evaluation becomes a contribution when it establishes a new engineering finding or capability; `extensive experiments` alone describes work performed. Match each claim to the relevant method, analysis, figure, or result. Preserve the author's contribution-list formatting unless revision is requested or a verified venue rule requires a change; bold lead-ins are a style choice, not a measure of scientific quality.

## 4. Related Work

Choose themes that build the gap. Typical themes may include:

- industrial monitoring or diagnosis for the relevant process class;
- representation learning for the relevant measurement condition;
- structure-, knowledge-, physics-, or graph-guided modeling;
- adaptation, weak supervision, reliability, or another central challenge.

For each subsection:

1. Define the method family or engineering concern.
2. Explain how representative approaches develop the relevant capability and change the underlying assumptions.
3. Identify what they contribute.
4. State the remaining requirement relevant to this manuscript when one follows from the evidence, or carry the established capability into the next theme.

The limitation should not be `accuracy remains low`. It should identify a mismatch in assumptions, data organization, process structure, operating conditions, supervision, or evaluation.

Make the progression cumulative: what one family enables becomes the starting point for the next condition or capability. For example, a justified sequence could move from complete observations to partial observations and then to partial observations with sparse labels. Use this sequence only when it matches the sources and the paper's scientific question. Each paragraph should develop one comparison or relation; it need not contain a ritual criticism followed by `To address this issue`.

Represent prior work fairly. A source that evaluates one setting establishes evidence for that setting. An untested setting remains unresolved; it is not an observed failure. Identify a limitation through an explicit assumption, a reported result, or a documented comparison, and cite the source supporting that exact statement. Avoid unqualified `existing methods ignore` or `all methods fail` claims.

Avoid a final synthesis paragraph if it merely repeats all subsection endings. Retain it only when it introduces a genuinely new integration gap.

## 5. Problem Formulation

Motivation and problem formulation may be written as one continuous section when the industrial phenomenon naturally leads into the mathematical task. Do not create separate `Industrial Motivation` and `Problem Formulation` subsections merely to fill an outline. Use subsections only when each carries a distinct scientific function.

Define:

- sampling unit and time/index convention;
- input measurements and dimensions;
- process grouping, conditions, stages, units, or rates when relevant;
- output target and class/regression meaning;
- training and inference objective;
- assumptions and scope.

Use notation that remains stable through the paper. If a process variable becomes an input channel, state the correspondence explicitly here or at the method input.

Keep definitions that establish the task, assumptions or later derivation. Remove unused notation that serves none of these functions; a useful problem definition need not be repeated literally later.

The opening should turn the preceding engineering requirement into the quantities and information actually available. The ending should identify the resulting estimation, classification or optimization task that Methodology addresses. Those links can take a clause each; do not add a second miniature Introduction. Keep the task definition separate from the proposed solution: an assumed production-unit partition may belong here, whereas a newly designed grouping module usually belongs in Methodology. P17 connects process and assay availability to the regression task; P30 defines a changing distribution before deriving a response. Neither supplies a mandatory section length or heading.

## 6. Overall Architecture

An `Overview` or `Framework Overview` subsection is optional. It is useful when a framework figure and several modules need a shared data-flow explanation. Otherwise, introduce the framework in the opening paragraphs of Methodology and begin numbered subsections with the first substantive mechanism.

Describe the forward logic rather than mechanically listing components.

For a sequential prediction path, the following questions often provide a useful order:

1. how the input is organized according to the engineering object;
2. how local or temporal information is represented;
3. how relationships or constraints are modeled;
4. how information is fused or transferred;
5. how the output is produced;
6. where an auxiliary path or safeguard actually acts.

Explain parallel branches where they diverge and meet. Describe training objectives, pretraining and test-time adaptation with their own information access and timing, rather than placing every component into that sequential prediction path. An auxiliary decoder or alignment loss can influence learned parameters without running during inference. If the training and prediction architectures differ, name the difference once in the overview and keep the figure consistent.

Refer to the framework figure after the organizing principle is stated. Do not write `the architecture consists of five components` unless enumeration is genuinely the clearest explanation.

## 7. Method Subsections

For each mechanism:

1. State the mechanism's role in the already established requirement, without inventing another gap for each module.
2. Define the input representation.
3. Present the operation and formula.
4. Define symbols and dimensions.
5. Explain the information retained, removed, exchanged, or constrained.
6. Connect the output to its actual recipient or, for a training objective, identify what it optimizes.

For central design decisions, explain which engineering requirement selects the operation and why a relevant alternative would change the trade-off. This explanation should follow from the design or evidence; do not invent alternatives considered by the authors. Distinguish an intended effect from a validated effect, and carry the corresponding claim into the evaluation.

Use transitions that explain why the next operation is needed and what it receives. Define an equation's scientific role, not only its symbols. A short explanation can be sufficient when the operation is standard and its purpose is clear; the required detail follows complexity and novelty, not a sentence quota.

Validate that the formula actually entails the stated effect. Define whether a mask acts on inputs, scores, probabilities or admissible outputs, and whether normalization or a later mixing operation changes that effect. If a source equation, algorithm and implementation disagree, record the unresolved choice rather than improving fluency around an uncertain mechanism. This is an author-side check; the paper need only state the verified operation and its relevant consequence.

At the same time, do not repeat the same motivation before and after every equation. The appropriate density defines symbols and dimensions, explains the operation's effect, and connects it to the next step without turning the method into an implementation report.

## 8. Experiments Overview

Open the Experiments section with a short paragraph stating what evidence is presented and how the case studies or evaluation blocks are organized. A concise `Experimental Settings` subsection may combine shared data preparation, comparison methods, implementation details, and metrics when this reduces repetition.

### Method Paper With Benchmark And Production Evidence

Recommended opening:

1. State the benchmark case study and which method question it evaluates; name controlled factors only when documented.
2. State the real-world case study and what engineering condition it evaluates.
3. Introduce comparison-method categories.
4. State common implementation settings.

Use this organization when both evidence types are present. A single-case or multi-benchmark study should describe its actual evidence roles without inventing a production case.

Keep data split and process details in each case-study subsection.

### Background-Driven Application Paper

Recommended opening:

1. Define the real engineering site, process, equipment, or operating task.
2. Explain data acquisition and label or target generation.
3. State the evaluation question and comparison set.
4. Explain training/testing separation and operational realism.
5. State implementation settings.

A public benchmark may be used as supplementary evidence, but it should not obscure the central application.

## 9. Case-Study Description

Include only facts that support understanding and reproducibility:

- process route or equipment structure;
- variables, sensors, controls, rates, stages, or conditions;
- sample and class/target definition;
- the actual training, model-selection and test arrangement; describe a validation subset only if it exists;
- missing-value, normalization, and windowing operations;
- knowledge or constraints used by the method;
- source of labels and their timing relative to prediction.

Use a process figure when the textual description is difficult to follow, and introduce its engineering context before interpreting result figures. Exact float placement follows the template and approved layout; this reading order does not authorize moving protected figures.

## 10. Comparison Methods

Select methods by scientific relevance:

- established conventional method when still meaningful;
- standard neural architecture;
- current general method for the data modality;
- engineering/task-specific method;
- proposed method.

Explain why the set is representative. Do not add many weak methods simply to create a large margin. Methods without credible implementation or comparable input should not be included as if fully reproduced.

A focused contribution can compare against a defined reference method when that reference answers the scientific question. Explain its relevance, include the closest alternatives that could affect interpretation, and report the result within that comparison set. Do not rewrite a focused advantage as universal state-of-the-art superiority.

State model-scale variants once in prose when necessary, while keeping table names concise.

When an existing method requires interpolation, aggregation, padding, masking, or another input construction, describe that construction in the settings. Do not create many artificial `strategy + model` table rows unless the strategy itself is an evaluated research question.

Use one consistent subsection convention across cases, such as `Performance comparison`, `Comparative experiments`, or `Comparative analysis`, selected from matched target-journal papers. Avoid switching between vague labels such as `Comparison results` and dataset-specific variants without reason.

## 11. Experimental Settings

Report settings in logical groups:

1. software and hardware;
2. optimizer, learning rate, and regularization;
3. batch size and training control;
4. input construction, window, patch, rate, stage, or grouping settings;
5. model-specific parameters central to reproducibility;
6. comparison-method tuning rule.

Do not present one long list of unrelated parameters. Report hardware and software details needed to reproduce the work. Parameter counts, FLOPs, timing and memory benchmarks are useful when they support comparison, resource feasibility or efficiency claims; they are not mandatory for every paper. Keep model hyperparameters needed for reproduction distinct from parameter-count benchmarks.

Use direct factual wording. Ordinary implementation details do not require `experimental protocol`, `reporting protocol`, or `fairness protocol` labels.

Use `XXX` only in an internal draft. Final submission must contain verified values or omit nonessential settings.

## 12. Main Results

Recommended paragraph sequence:

1. Identify the table and evaluation focus.
2. State the main result with an appropriate metric.
3. Compare against the strongest relevant methods, not only the weakest.
4. Discuss class-, condition-, stage-, unit-, or target-specific behavior.
5. Connect the observation to the proposed design cautiously.
6. Note a trade-off or difficult case when present.

Write the supported finding directly, followed by its measurement and interpretation. Keep figure captions readable on their own, but do not mechanically repeat each result in an opening paragraph, closing paragraph, and caption. Distinguish observation from a mechanism inference; a plausible explanation needs a discriminating comparison or analysis before it can be treated as demonstrated.

Select the pattern that answers the experimental question rather than narrating every model row. A main comparison can establish the aggregate ordering, a difficult fault or target can qualify that ordering, and a matched control can test the proposed explanation. These are distinct evidential roles, not compulsory paragraphs. A lower comparator score alone does not identify which feature it failed to learn. State numerical differences with their units and reference: percentage points for a difference between percentages, relative percent change only with an explicit denominator, and physical units for unnormalized prediction errors.

Keep manuscript prose distinct from the accompanying review. A short Results/Discussion passage should state the relevant pattern, its engineering trade-off and the scope needed to read it correctly. Do not append a catalogue of absent experiments or unclaimed benefits to every paragraph. Put detailed verification requests in author notes; retain a material limitation in the prose when omission would alter its meaning. Direct descriptions of the measured setting can often carry scope without repeated `does not prove` clauses. Do not compensate for excessive detail by hiding an unfavorable outcome or splitting it into many tiny paragraphs.

For imbalanced classification, do not rely on accuracy alone. Use macro metrics, weighted metrics, and class-wise behavior as appropriate.

## 13. Ablation And Sensitivity

Each ablation row must correspond to a real design claim. The full-model result must match the main table when the same run and metric are claimed.

Write:

- what was removed or changed;
- how performance changed;
- what design claim this supports;
- whether interactions between components limit one-at-a-time interpretation.

Sensitivity analysis should cover only hyperparameters that influence the method's central behavior. Explain the practical range rather than praising one optimal point.

If a control outperforms the full model, retain it and distinguish what the comparison establishes from the intended mechanism. It may narrow the component's claimed benefit, expose a trade-off or motivate further study; it is not permission to relabel the control as the original full model. Likewise, a sensitivity point above the chosen setting does not make the reported experiment invalid, but the chosen setting should not be described as best across that sweep. Record how it was selected and whether the sweep is exploratory. Reusing the same default runs in several plots does not create additional independent repetitions.

## 14. Robustness, Visualization, And Interpretability

Robustness tests should have a plausible engineering disturbance model: noise, missing values, drift, sensor fault, load change, label scarcity, or another relevant perturbation.

For a joint-condition claim, explain what the evaluation reveals about each condition and their interaction. Naming two perturbations does not establish a new coupled problem. For generalization claims, name the held-out operating regimes, times, equipment, lines, or sites and the information allowed during adaptation. A within-case random split cannot establish cross-site transfer.

Visualizations should answer a question:

- feature projection -> class or operating-condition separation;
- heatmap -> variable/stage/unit contribution or interaction;
- confusion matrix -> difficult conditions and failure patterns;
- learned graph/group -> agreement with known structure;
- trend plot -> temporal response or prediction quality.

Use `supports`, `is consistent with`, or `provides auxiliary evidence`. Do not call visualization causal proof without causal validation.

For feature projections, identify samples, model/run, preprocessing and projection settings. Matching colors and subplot scales do not verify that different methods used the same sample set. If an inherited comparison plot lacks its original embeddings or sample identifiers, record that provenance limit rather than inventing a common projection procedure. A visually separated projection is not proof of out-of-sample diagnosis or of learned physical causality.

A confusion matrix is optional when designing the evidence presentation. It is useful when specific class confusions carry engineering meaning; other analyses may answer a different central question better. When revising an existing manuscript, preserve approved figures and their layout. Suggest a possible omission or alternative separately if needed; language review or a page target does not authorize deleting them.

## 15. Discussion

Use Discussion to synthesize rather than repeat results.

Possible functions:

- reconcile controlled and real-world evidence;
- explain dependence on process knowledge or data conditions;
- describe transfer limits across lines, sites, or operating regimes;
- clarify computational, sensing, or maintenance requirements;
- identify what must be validated before online use.

Keep limitations concrete. Do not use a generic paragraph that could be attached to any model.

Explain what the findings imply for the engineering decision and why the remaining condition matters. State necessary scope directly. Remove apology-like discussion of what the paper does not claim when it adds no information. Preserve a boundary in the Abstract or result sentence when that sentence would otherwise mislead; the detailed account can remain here or in Methods.

Discussion may be a short subsection at the end of Experiments. Its length follows the findings and their implications, not a minimum paragraph count. One specific paragraph can be more useful than several generic ones.

Across cases, separate an unchanged method principle from case-specific topology, inputs, labels and fitted parameters. The same method trained separately in two cases is not a trained model transferred between them. When effects differ, report the difference and examine documented task/data/configuration changes; do not assign a cause merely because the case names differ. Compare directions or normalized quantities only where meaningful, and do not average incompatible task metrics into a new overall score. A common positive result supports the evaluated cases; a mixed result may reveal a useful boundary rather than invalidate the entire study.

An engineering implication should explain what a finding changes for the stated use: for example, whether extra measurements provide useful prediction information or whether reduced computation meets a stated deadline. If only model-level evidence exists, retain that level. Do not turn a classification gain into reduced downtime, financial savings or a maintenance recommendation without the corresponding decision and cost evidence. Put hypotheses and the specific comparison needed to test them in author notes or clearly identified discussion, not into completed-result language.

## 16. Conclusion

Recommended order:

1. Restate the engineering problem and core methodological response.
2. Summarize the principal mechanism at the idea level.
3. Summarize benchmark and/or real-world evidence without repeating the full results table.
4. State engineering relevance within the demonstrated scope.
5. When useful, give focused future work linked to a material remaining condition.

Do not introduce new contributions, experiments, or claims in the Conclusion.

Select facts by their role in the closing argument, not merely because they were verified. Detailed split counts, preprocessing checks and scoring procedures usually belong in Methods or Experiments; repeating the full checklist can displace the principal finding. Retain a condition here when it changes the finding's meaning, such as a required feedback delay, a demonstrated operating range or a measured accuracy-resource trade-off. A decisive number may help; omit neither an unfavorable result nor the evidence needed to interpret it. Connect what the design makes possible to what the evaluation actually establishes, without converting a plausible mechanism into a proven cause.

Close with what is now established, not another module inventory or a list of fashionable methods. Future work is optional unless required by the venue; choose an unresolved condition, why it matters, and the evaluation or capability needed next. A proposed next study is not an achieved benefit. P01 and P11 close without a future-work list, whereas P03 and P25 discuss extensions; these variations support choice, not a mandatory conclusion template. See the [source-reading notes](published-evidence.md).

## 17. Captions And Cross-References

Captions should be understandable without reading the full paragraph:

- define each subfigure;
- state the comparison or process content;
- define uncommon abbreviations;
- avoid interpreting results beyond what the figure shows.

In prose, explain why the figure or table matters. Do not simply repeat the caption.
