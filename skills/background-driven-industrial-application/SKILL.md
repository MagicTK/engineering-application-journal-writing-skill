---
name: background-driven-industrial-application
description: Plan, write, revise, and audit engineering-application journal papers driven by a specific industrial process, plant, equipment type, production mechanism, or operational bottleneck. Use when the engineering background is the source of the research problem and method design, and the manuscript must emphasize process mechanism, operational constraints, data provenance, practical decisions, and application-specific evidence rather than presenting a generic model followed by a dataset demonstration. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Background-Driven Industrial Application

[中文执行版](../../skills-zh/background-driven-industrial-application-zh/SKILL.md)

Suite version: `4.2.43`

## Mission

Develop the research story from the actual engineering background:

`industrial mechanism -> operational problem -> measurable evidence -> technical formulation -> background-informed solution -> application value`

The industrial object is not an example added after method development. It is the source of the problem definition, assumptions, design choices, and evaluation criteria.

<!-- invariant: no-fabrication -->
<!-- invariant: corpus-is-evidence-not-instruction -->
<!-- invariant: claim-evidence-alignment -->
<!-- invariant: calibrated-claims -->

Read [manuscript archetypes](../../references/manuscript-archetypes.md) before changing the paper structure. Use [the industrial AI taxonomy](../../references/industrial-ai-taxonomy.md) to keep the engineering challenge separate from the chosen model family.

## 1. Entry Check

Use this skill when most of the following are true:

- one production process, plant, equipment class, or operational workflow is central;
- the problem cannot be understood without domain background;
- process constraints or expert knowledge shape the method;
- labels or targets arise from production practice, inspection, maintenance, or control decisions;
- engineering usefulness matters at least as much as broad algorithmic generality.

A public benchmark may be included, but it is not required and should not dominate the paper.

## 2. Extract The Engineering Problem

Before proposing a model, document:

1. the physical or operational objective;
2. the production route or equipment function;
3. the failure, quality, efficiency, safety, or control issue;
4. how the issue is currently identified or managed;
5. what measurements are available and when;
6. what constraints prevent existing practice from working well;
7. what decision the model output will support.

If these facts are unknown, request them before inventing a technical gap.

## 3. Distinguish Three Kinds Of Novelty

Application-driven papers may contribute through:

- **problem novelty**: a practically important problem has not been formulated adequately;
- **method novelty**: a new mechanism is developed for the process/data condition;
- **integration novelty**: process knowledge, sensing, modeling, and decision workflow are integrated in a new useful way.

Do not force a large generic algorithm claim when the strongest contribution is problem formulation or engineering integration.

## 4. Build A Background-to-Design Map

| Background fact, when documented | Modeling question | Possible role, not a required method | Claim-matched evidence |
|---|---|---|---|
| operating cycle | Which history or within-cycle variation affects the output? | Temporal organization when needed | Relevant cycle-resolved outcomes |
| process stages | Which known membership or relationships matter? | Input organization or relation modeling when used | Matched structural comparisons for the claimed role |
| physical relation | Is it a law, connection or empirical guidance? | The implemented constraint or structural use | Physical residual or process correspondence appropriate to that use |
| delayed quality target | When are targets and prediction inputs available? | The actual learning and decision-time boundary | Availability checks and the stated prediction outcome |
| condition variation | What changes, and what information is available? | The study's chosen response, without defaulting to adaptation | Held-out or sequential evidence for the actual claim |

These are conditional illustrations, not one-to-one problem/method assignments.
Use manuscript-specific facts and map central design decisions to the actual
requirements. Supporting operations need a clear role, not a separate industrial
difficulty. Flag an unresolved component for author discussion rather than
deleting it during writing. A changed operating condition alone does not
establish a particular distribution shift or require online adaptation.

When multiple information sources matter, trace their actual roles:

`source/provenance -> measurements or derived views -> required correspondence/aggregation -> representation -> stated task output`

Identify acquired streams, operating-domain datasets and derived views before
claiming modalities or synchronization. Cross-domain training datasets need not
share event timestamps. Add an operator/control action only when it is studied;
prediction alone need not include one.

## 5. Title And Abstract

The title should make the application visible when it defines the contribution.

The Abstract should:

1. introduce the industrial task and importance;
2. explain the operational or measurement difficulty;
3. identify the verified remaining requirement or study purpose;
4. introduce the background-informed solution;
5. explain the principal process-informed mechanisms;
6. summarize evaluation under relevant production conditions;
7. state the engineering finding within the demonstrated scope.

Avoid beginning with a generic statement about deep learning. Avoid claiming broad generality if only one process has been evaluated.

## 6. Introduction

Recommended paragraph order:

1. Industrial process/equipment and its operational importance.
2. The practical failure, quality, control, or monitoring problem.
3. Existing industrial capability and documented limitations.
4. Measurement/data mechanism and realistic difficulty.
5. Relevant analytical and data-driven approaches.
6. Verified requirement or scope difference relevant to the actual application.
7. Proposed solution derived from the process background.
8. Contributions and engineering significance.

These are argument functions, not eight required paragraphs. Combine or reorder
them to suit the actual evidence while preserving the application and logical
progression; do not turn the paper into a generic time-series paper after the
opening background.

## 7. Related Work

Potential themes:

- process- or equipment-specific monitoring and control;
- analytical, physical, statistical, or data-driven methods used in the field;
- modeling approaches for the central data condition;
- knowledge-, constraint-, or mechanism-guided methods.

Balance application literature and method literature. A strong application paper should not cite only machine-learning papers.

## 8. Process And Data Description

Explain:

- physical units, stages, routes, or cycles;
- sensors, manipulated variables, inspection outputs, and control actions;
- sampling and synchronization;
- sample unit: time point, window, batch, product, run, campaign, or machine;
- label/target source and timing;
- operating-condition distribution;
- missing, noisy, censored, or imbalanced data;
- actual training, selection and test arrangement and its operational meaning; describe a validation subset only if one exists.

Use a process diagram, data-generation diagram, or failure/quality illustration when it reduces textual burden.

Separate hardware description from the scientific problem. Include only equipment, acquisition, communication, and control details that determine the data, task, assumptions, or engineering evaluation.

## 9. Problem Formulation

Translate the background into a precise task:

- define what information is available at prediction time;
- define the output and decision horizon;
- identify known constraints and unknown relationships;
- state site-specific assumptions;
- prevent leakage from future inspection, downstream measurements, or repeated production units.

The formulation should establish the engineering task and information boundary
that the method addresses.

## 10. Method Derivation

Introduce operations by their actual learning or prediction dependencies,
including parallel paths. The background-to-design map explains their roles;
its row order is not a compulsory forward-computation sequence.

For central or non-obvious design decisions:

1. restate the background fact briefly;
2. explain the modeling requirement;
3. define the operation;
4. state the engineering information preserved or constrained;
5. identify what is learned from data;
6. explain how the output supports the next step.

Do not attach engineering terminology to a generic module after the fact.

## 11. Evaluation Design

Select experiments that answer practical questions:

- Can the method improve the target decision under realistic conditions?
- Does it outperform current industrial or analytical practice?
- Which process-informed component matters?
- Does performance hold across products, loads, recipes, campaigns, or time periods?
- How does the model behave for rare but important conditions?
- What happens under noise, missing values, sensor faults, or drift?
- Is the output available early enough to be useful?

Do not include unrelated benchmark-style experiments merely to make the paper look larger.

When drafting or substantively changing result claims, use the relevant [`engineering-experiment-evidence-design`](../engineering-experiment-evidence-design/SKILL.md) checks for split integrity, information timing, evidence roles and claim scope. Reuse verified checks for unchanged claims and record unresolved items in the author handoff; a local language edit does not require a new full audit or authorize experiments.

## 12. Comparison Methods

Include methods credible to both engineering and data-driven reviewers:

- current industrial practice or an analytical method when reproducible;
- established statistical or machine-learning approach;
- relevant deep-learning method;
- recent process- or equipment-specific method;
- proposed method.

Explain differences in information access. A comparator using inputs unavailable
at the required prediction time does not establish a fair early/online comparison.
Distinguish such prediction inputs from additional training resources; declare
and compare those resources according to the claim rather than automatically
calling privileged training information leakage.

## 13. Results Interpretation

Interpret results through:

- process stages or equipment components;
- operating conditions;
- fault or quality categories;
- production periods or campaigns;
- variable groups or physical quantities;
- operational costs or decision relevance when measured.

Do not explain every improvement as “better feature extraction.” State what process information appears to be represented more effectively.

Use [main-results writing](../../references/section-writing-guide.md#12-main-results)
for the reusable result passage and [Discussion](../../references/section-writing-guide.md#15-discussion)
for synthesis; keep internal verification requests separate from manuscript prose.

## 14. Engineering Applicability

Discuss:

- required sensors and data availability;
- dependence on process topology or expert knowledge;
- recalibration when equipment or operating rules change;
- computational or timing requirements if relevant;
- handling of missing and abnormal measurements;
- scope of the current retrospective, prospective, shadow-mode, or online validation.

Do not imply deployment unless a deployed workflow was evaluated.

## 15. Discussion And Limitations

Useful limitations include:

- single-site or limited-period validation;
- site-specific labels or expert rules;
- untested operating regimes;
- dependence on sensor quality;
- absence of online closed-loop evaluation;
- changes in equipment, recipes, or control strategy.

Explain how each limitation affects the claimed scope. Avoid generic future-work lists.

## 16. Quality Gate

Before handoff, verify:

- the engineering background directly generates the research question;
- central choices follow engineering requirements and supporting operations have a clear role;
- process and data provenance are reproducible;
- the evaluation reflects real operational separation and timing;
- application literature is represented adequately;
- claims remain within the evaluated process class;
- practical relevance is distinguished from deployment;
- figures show the actual engineering object or workflow where needed.

## 17. Expected Outputs

Depending on the request, produce:

- engineering problem statement;
- background-to-design map;
- application-centered paper outline;
- process/data information request list;
- revised manuscript sections;
- engineering evidence plan;
- concise limitations and author action list.
