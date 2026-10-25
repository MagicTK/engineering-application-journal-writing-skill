---
name: general-method-benchmark-realworld
description: Plan, write, revise, and audit engineering-application journal papers that propose a broadly applicable method and validate it with both a controlled or public benchmark and a real-world industrial case study. Use when the technical method is the main contribution but the manuscript must remain engineering-first, distinguish the evidential roles of benchmark and production cases, and avoid machine-learning-conference framing or unsupported deployment claims. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# General Method With Benchmark And Real-World Validation

[中文执行版](../../skills-zh/general-method-benchmark-realworld-zh/SKILL.md)

Suite version: `4.2.14`

## Mission

Build a method-centered engineering paper whose general technical contribution is supported by two different forms of evidence:

- a benchmark case study for comparison under a documented evaluation setting; and
- a real-world industrial case study for relevance to the measured production setting.

Explain what each case tests beyond listing two datasets. Neither the word `benchmark` nor the origin of production data establishes experimental control, reproducibility, or coverage of operating variation.

<!-- invariant: no-fabrication -->
<!-- invariant: claim-evidence-alignment -->
<!-- invariant: calibrated-claims -->

Read [manuscript archetypes](../../references/manuscript-archetypes.md) before changing section structure. Topic-specific constraints belong to [topic playbooks](../../references/topic-playbooks.md), not to this general archetype.

## 1. Entry Check

Use this skill when most of the following are true:

- the method is intended to apply beyond one plant or equipment instance;
- the technical challenge can be stated independently of a single site;
- a public or controlled benchmark is available;
- a real-world industrial dataset or case study is available;
- the manuscript needs both methodological rigor and engineering relevance.

Do not use this as the main skill when the contribution is inseparable from one specific production mechanism, plant workflow, or equipment design. Use the background-driven application skill instead.

## 2. Define The Generalizable Problem

Write a one-paragraph problem abstraction containing:

1. the engineering task;
2. the recurring data or process property;
3. what capability remains to be established or improved under that property;
4. the method-level principle needed to resolve it;
5. the industrial scope in which the principle is expected to hold.

The abstraction must be broader than one dataset but narrower than “all industrial data.”

## 3. Separate The Two Evidence Roles

Create an evidence table before writing:

| Evidence role | Benchmark case | Real-world case |
|---|---|---|
| Possible purpose | comparison under a shared evaluation setting | relevance to the documented production setting |
| Strength to verify | accessible data/settings, label provenance, repeatability, controlled factors where available | measured process context and the variation actually present |
| Typical experiments | main comparison, ablation, sensitivity, robustness, visualization | process description, main comparison, selected ablation, engineering interpretation |
| Defensible conclusion | methodological effectiveness | practical relevance under tested conditions |
| Not established | deployment | universal generalization or online operation |

Do not repeat every benchmark experiment in the real-world case unless it answers an engineering question.

Before results are written, pass all intended claims through the [`engineering-experiment-evidence-design`](../engineering-experiment-evidence-design/SKILL.md) skill. The two cases should share a method definition but may require different data preparation, comparison emphasis, and analysis depth.

## 4. Manuscript Story

Use this logical chain:

`recurring industrial challenge -> remaining modeling requirement -> general method principle -> benchmark evidence -> real-world engineering evidence -> scope and boundary`

Each contribution must map to evidence that tests its actual claim. Use [contribution narratives](../../references/contribution-narratives.md) to distinguish new formulations, mechanisms, adaptations and focused comparisons; let [argument and prose craft](../../references/argument-and-prose-craft.md) guide the paragraph progression.

## 5. Abstract

Recommended functions:

1. State the recurring engineering challenge.
2. Identify the precise limitation in existing methods.
3. Introduce the proposed method and organizing idea.
4. Explain the principal mechanism and any other operation essential to the contribution.
5. Name the benchmark and real-world case studies.
6. State the verified outcome and its supported engineering relevance, including a trade-off or unresolved outcome where that is what the evidence establishes.

Keep the final evidence sentence concise. Name the benchmark and real-world case and state what they support. Do not list incidental dataset properties such as class imbalance, noise, or missingness in this high-level sentence unless one of them is the paper's central problem. Calling the collected measurements a dataset is legitimate; explain the production context instead of treating its name as evidence of applicability. Do not claim deployment without operational evidence.

## 6. Introduction

Possible paragraph functions, not a required eight-paragraph outline:

1. Engineering task and importance across the relevant process class.
2. Data or process property that creates the recurring challenge.
3. Established industrial and data-driven methods.
4. Limitation of global, local, stage-wise, rate-wise, condition-wise, or other relevant modeling assumptions.
5. Motivation figure or conceptual distinction when useful.
6. A distinct additional representation requirement, only if needed for the argument.
7. Proposed method as a structured response.
8. The actual independent contributions, with supporting operations kept within the contribution they enable; do not pad a fixed count.

Connect the real-world case to the study's evidence plan; performing the case alone need not be a contribution. Merge overlapping functions and preserve the cited reasoning when integrating Related Work into the Introduction. Do not invent a separate challenge for every module.

## 7. Related Work

Organize around the technical gap:

- engineering methods for the target task;
- representation/modeling approaches for the relevant data property;
- structure-, knowledge-, condition-, or physics-guided methods when central;
- benchmark and real-world validation practices if necessary.

Build a progression from established capabilities to the study's remaining requirement. End a subsection with a supported limitation or open evaluation condition when it advances that argument; otherwise carry its established capability into the next paragraph. An unreported test does not demonstrate inability. Avoid ritual criticism and separate subsections that only list modern time-series models.

## 8. Methodology

The method section must demonstrate generality without becoming detached from engineering meaning.

For each substantive component, identify the following where they apply; ordinary supporting operations need a defined role, not a repeated motivation paragraph:

1. name the recurring engineering/data issue;
2. define the representation and operation;
3. explain why the mechanism can apply across cases;
4. identify case-specific inputs such as topology, stages, rates, or expert knowledge;
5. distinguish fixed design from data-dependent learning.

Do not hide site-specific assumptions inside a supposedly general method.

When the method uses production stages, process topology, sampling schedules, or expert rules, distinguish:

- the transferable design principle;
- the case-specific configuration;
- information learned from data;
- information supplied by engineering knowledge.

## 9. Experiments Overview

Open with a clear division of labor:

- the benchmark establishes comparison under its documented data, labels, splits, and settings;
- the industrial case examines applicability to its measured process conditions and task.

Then introduce:

1. comparison-method categories;
2. shared implementation settings;
3. metrics and fairness rules;
4. case-specific subsections.

## 10. Benchmark Case Study

Include:

- process and task description;
- variables, classes/targets, and data split;
- input construction and preprocessing;
- main comparison;
- ablation aligned with contributions;
- sensitivity only for central hyperparameters;
- robustness only for plausible disturbances;
- visualization only when it answers a scientific question.

Use the case with suitable labels, repeatability, and controlled factors for the corresponding mechanism analysis. Do not infer those properties from the benchmark label alone.

## 11. Real-World Industrial Case Study

Include:

- actual process, equipment, production route, or operational context;
- source and meaning of variables and labels;
- sample unit and split unit;
- noise, missing values, class-frequency variation, condition variation, or other realistic difficulty when it materially affects the case;
- domain knowledge or constraints actually used;
- main comparison and selected ablation;
- engineering interpretation tied to the process.

Do not copy the benchmark subsection structure mechanically. The real-world section should make the production context understandable before reporting scores.

Record whether the study uses retrospective production records, a prospective trial, shadow-mode evaluation, or an online deployed system. These settings justify different levels of practical claim. Use the word `offline` in the manuscript only when the offline/online distinction is needed to interpret the method or evidence; otherwise describe the case as a real-world industrial process or real-world production data.

Disclose class-frequency imbalance at the level where it changes scientific interpretation: class counts in the dataset description, weighting or sampling in the settings, metric choice in the evaluation subsection, and minority-class behavior in the results. Do not elevate it to the Abstract, contribution list, experiment overview, or Conclusion unless imbalance handling is a central research question or contribution.

## 12. Comparison Set

Use a layered, credible set:

- conventional method when still meaningful;
- standard deep-learning method;
- current general method for the data modality;
- strongest relevant industrial/task-specific method;
- proposed method.

Keep method names and model variants consistent when they denote the same comparator. Select comparators relevant to each case and explain substantive differences in the sets or implementations; identical sets are not compulsory when tasks or available inputs differ.

## 13. Results Synthesis

Do not write two disconnected result summaries. Synthesize them:

1. What design claim is supported by the benchmark?
2. Does the real-world case show the same direction of benefit?
3. Which realistic conditions change the relative performance?
4. Which limitations remain case-specific?
5. What level of generality is justified?

Use `consistent with` when the two cases support a common interpretation. Do not claim universal generalization from two cases.

Retain different or reversed effects across cases and discuss the documented differences without inventing their cause. Separate retraining the same method for each case from transferring one fitted model. Do not pool metrics with incompatible targets, units or denominators. Use the [Discussion guidance](../../references/section-writing-guide.md#15-discussion) to turn those patterns into a bounded engineering interpretation.

## 14. Discussion And Conclusion

Discussion should distinguish:

- method principle that transfers across cases;
- process knowledge or configuration that must be adapted;
- evidence for engineering applicability;
- untested conditions that materially limit the claims being made.

Online, cross-site, and long-term tests are needed for the corresponding claims, not as a compulsory closing list for every study.

Conclusion should summarize the general principle, the two evidence roles, and the demonstrated scope. Avoid repeating every table value.

## 15. Quality Gate

Before handoff, verify:

- each case has a justified purpose, with shared and complementary evidence identified;
- the method claim is general but not universal;
- the real-world process is described as an engineering case, not only a dataset;
- comparison settings are fair across cases;
- reported values and visualizations identify their run and aggregation scope; shared results agree and legitimate differences are explained;
- practical applicability is not inflated into deployment;
- the Abstract and Conclusion reflect both evidence types accurately.

## 16. Expected Outputs

Depending on the request, produce:

- a one-page story and evidence map;
- section-level revision plan;
- revised manuscript text;
- benchmark/real-world experiment structure;
- claim-evidence audit;
- concise unresolved author action list.
