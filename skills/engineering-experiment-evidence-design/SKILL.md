---
name: engineering-experiment-evidence-design
description: Design, audit, and organize experimental evidence for engineering-application journal papers. Use for benchmark and real-world case roles, data splits, comparison methods, ablations, robustness, sensitivity, interpretability, statistical reporting, numerical consistency, reproducibility, or deciding which claims current results can support. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Experiment And Evidence Design

[中文执行版](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)

Suite version: `4.2.9`

## Mission

Make every experiment answer a scientific or engineering question. Replace result accumulation with a traceable evidence chain:

`claim -> appropriate evidence -> data/assumptions and controls -> metric or derivation -> evidence artifact -> allowed conclusion`

<!-- invariant: no-fabrication -->
<!-- invariant: verified-data-version -->
<!-- invariant: claim-evidence-alignment -->
<!-- invariant: result-dependent-artifacts -->
<!-- invariant: calibrated-claims -->

## 1. Start With Claims

Classify each intended claim:

- `structural`: a specified mathematical/architectural property under stated assumptions;
- `resource`: a reusable data/annotation/benchmark capability with documented provenance and access conditions;
- `comparative`: method improves a measured outcome;
- `component`: a module contributes to the outcome;
- `robustness`: performance remains acceptable under disturbances;
- `generalization`: prediction on new samples from a stated population, or transfer across defined conditions, sites, products or domains;
- `interpretability`: outputs correspond to meaningful process or fault information;
- `efficiency`: resources, latency, or model size are reduced;
- `practical`: method is useful under tested industrial conditions;
- `deployment`: method operates in an actual online workflow.

Each claim type requires different evidence. Accuracy on one split cannot support all of them.

## 2. Build A Claim-Evidence Matrix

| Claim | Evidence required | Case/data | Controls | Metric | Artifact | Status | Allowed wording |
|---|---|---|---|---|---|---|---|

Use `planned`, `available`, `verified`, `inconsistent`, or `missing` for status.

## 3. Assign Case-Study Roles

### Benchmark

Use the benchmark's documented settings for relevant comparisons and mechanism analysis. Verify label provenance, controlled factors, and repeatability rather than assuming them from its name; choose ablation, sensitivity, robustness, or class-wise analysis only when it answers the claim.

### Real-World Industrial Case

Describe measured process conditions, data and label provenance, the variation actually present, and the engineering interpretation. Production-source measurements may still contain artificial fault injections or restricted operating coverage; distinguish these facts rather than calling all conditions and faults real.

Dataset properties should appear at the level where they affect evidence. For class imbalance, report counts with the data, handling with the settings, metric consequences with the metric definitions, and affected-class behavior with the results. Keep it out of high-level summaries unless imbalance is the research problem or a claimed contribution.

### Single Background-Driven Case

Use for operational value, condition coverage, current practice comparison, and process-informed analysis. Add a benchmark only if it tests a genuinely transferable claim.

Do not call two datasets complementary unless their evidential roles are stated.

### Inherit Verified Dataset Versions

Reuse source-verified settings before asking the author. Record source version/page or file/config/hash, raw points, windows, independent events, class range, sampling interval, condition splits and unlabeled-data access; same dataset name is not a version identifier. Use [the data-version record](../../assets/templates/data-version-record.md) when these facts affect comparability. Diagnose transcription/export conflicts before proposing a matched rerun; do not silently blend result populations.

Define low-label, few-shot, zero labeled target-condition data, and unseen fault-class zero-shot separately. Labels reserved for final evaluation cannot select the model. Training-query supervision, documented validation-query model selection and labels acquired through a declared active-learning pool have different, potentially valid roles; identify the actual stage and permissions. Do not invent a validation split to justify selection. Adjacent/non-overlapping windows do not by themselves constitute independent shots. Verify the actual condition-by-class file matrix rather than assuming a full factorial dataset. Apply [task and representation boundaries](../../references/research-planning-and-contribution.md) when missingness, tokenization, multi-label claims, or early-fault timing matters.

## 4. Audit Data Provenance And Splits

Record:

- sample unit: point, window, run, batch, product, campaign, machine, or site;
- label source and annotation timing;
- training, validation, and testing separation unit;
- window overlap and adjacency;
- normalization statistics and where they are estimated;
- missing-value and resampling operations;
- future, downstream, or privileged information;
- repeated products, runs, patients, machines, or production campaigns;
- class distribution and imbalance handling.

Prevent leakage across the operational unit that matters. A random window split may be invalid when adjacent windows come from the same run or product.

## 5. Choose Comparisons By Assumption

Use a layered comparison set when appropriate:

- established statistical or machine-learning method;
- standard deep-learning architecture;
- relevant current time-series or multimodal method;
- strongest industrial or task-specific method;
- proposed method.

For every method, record implementation source, input adaptation, hyperparameter selection, information access, and whether results were reproduced or cited. Do not present methods with different prediction-time information as equal-access competitors. A clearly labeled reference with extra inputs may be reported separately; explain its purpose and access in the [comparison record](../../references/experiment-evidence-design.md#4-comparison-fairness-record).

Separate the industrial challenge from the method family with [the taxonomy](../../references/industrial-ai-taxonomy.md). A preprocessing strategy used to make a comparison method accept the input is not automatically a separate comparison method. Describe its construction and declared data access: training and any separately defined validation data for source-only selection, or permitted target measurements for declared adaptation. Labels reserved for final scoring cannot select the input construction.

## 6. Design Ablations Around Contributions

Give each core design claim evidence appropriate to its scope. When a component can be meaningfully intervened on, an ablation can compare:

- full model;
- one component removed or replaced at a time;
- structurally meaningful alternative;
- same training and evaluation setting.

Avoid arbitrary combinations that cannot be interpreted. A coupled component may need a valid replacement or joint-interaction test rather than deletion. A correct derivation can establish a structural property within its assumptions; empirical benefit and numerical implementation claims need their own appropriate evidence. A validity-only control need not become another novelty item. If a full-model result is reused, it must match the main comparison. Independently repeated runs under the same settings may differ; identify their run populations rather than forcing numerical equality.

## 7. Use Sensitivity Selectively

Analyze only parameters central to the scientific mechanism or practical operation:

- diagnostic window or patch length;
- number of groups, clusters, bands, or stages;
- rate factors or sampling intervals;
- knowledge/gating strength;
- latent size when capacity affects the claim;
- threshold when it affects decisions.

A sensitivity curve should answer whether the method is stable, why a setting is chosen, or how an engineering trade-off behaves.

## 8. Design Robustness And Generalization Tests

Match disturbances to plausible conditions:

- sensor noise, drift, missing values, or corruption;
- class imbalance or limited labels;
- changing load, recipe, product, stage, or working condition;
- unseen fault, machine, site, or production period;
- visual interference, environmental disturbance, or communication delay.

Specify severity and test conditions. A single perturbed point supports a narrow robustness observation, not robustness across a range. For generalization, a leakage-safe independent random split can assess new samples from the same population; cross-condition/site/time transfer requires the corresponding separation. Check acquisition dependence before treating random samples as independent.

## 9. Treat Interpretation As Evidence, Not Decoration

Define what an interpretation artifact is expected to show:

- variable or stage contribution;
- fault-relevant time/frequency region;
- process-consistent interaction;
- localized abnormal region;
- learned grouping or topology;
- failure case or uncertainty.

Low-dimensional projections, attention maps, heatmaps, and clustering do not prove causality. Validate them with process knowledge, labels, perturbation, expert review, or task-specific annotations where possible.

A confusion matrix is optional, not a default requirement. Include it only when class-pair errors answer an important engineering question that is not already visible in class-wise metrics or a more diagnostic analysis.

## 10. Report Metrics Correctly

Choose metrics based on task and class distribution:

- class-wise precision, recall, and F1 for diagnostic categories;
- macro-F1 for equal class importance;
- support-weighted averages for the evaluated sample distribution, which need not equal operational prevalence;
- AUROC/AUPRC for detection when appropriate;
- localization metrics for spatial or variable localization;
- prediction errors for quality/soft-sensor tasks.

State averaging definitions. Recompute aggregates from class support when possible. Do not mix macro, micro, weighted, and overall accuracy in prose.

## 11. Statistical And Reproducibility Discipline

Use repeated runs, uncertainty, or statistical tests when stochastic variation could change the conclusion, especially for small gains. Match the repetition plan and independent units to the claim and budget; a single reported run does not support statistical significance. Apply [the evidence guide](../../references/experiment-evidence-design.md) for constraint interactions, noise-label semantics, explanation perturbations, and repetition design; use [the efficiency and routing playbooks](../../references/topic-playbooks.md) for MoE or end-to-end cost claims.

Record:

- framework and hardware;
- optimizer and learning-rate schedule;
- key model settings;
- training selection rule;
- comparison-method settings;
- data preparation;
- seeds or repeated-run policy when available.

Use placeholders only for genuinely missing author inputs, and list them once.

## 12. Numerical Consistency Audit

Check:

- class-wise values against aggregate values;
- main full model against ablation full model;
- Abstract and Conclusion against latest tables;
- figures against source data;
- percentages versus percentage points;
- metric names and directions;
- class counts and split totals;
- benchmark and real-world result versions.

Flag transcription errors separately from missing experiments.

## 13. Result Writing

For each subsection:

1. state the question;
2. identify the relevant comparison or condition;
3. report the result precisely;
4. interpret it through the design and engineering context;
5. state the boundary when needed.

Do not describe every cell. Focus on results that change the paper's argument.

Use `experimental settings`, `data preparation`, or direct factual description for ordinary settings. `Evaluation protocol` is legitimate for a defined split, access, repetition, or scoring procedure, including an established benchmark procedure; it need not itself be the research contribution. Do not rename a valid procedure merely to avoid the word.

Preserve author-approved table font size, width, grouping, and float order. If a table does not fit, revise its scientific content or column design before shrinking text. Use [figure and LaTeX guidance](../../references/figure-and-latex-production.md) for evidence-bearing artifacts.

## 14. Human Handoff

Return a short list split into:

1. **Confirmed inconsistency**: values or descriptions that conflict.
2. **Missing evidence**: an intended claim has no adequate test.
3. **Author decision**: scientific framing or experiment scope needs approval.
4. **Direct fix completed**: transcription or wording already corrected.

Do not ask the experiment owner to reconfirm information already present and consistent.

Read the expanded [evidence design guide](../../references/experiment-evidence-design.md) when auditing a full manuscript.

## 15. Quality Gate

Evidence is ready only when:

- each retained contribution has claim-appropriate evidence, whether empirical, analytical or resource-validation evidence; a separate model-deletion row is not mandatory for every contribution;
- comparisons have fair information access;
- splits match the real operational unit;
- aggregate and class-wise values are consistent;
- robustness/generalization claims match test diversity;
- interpretation has a validation route;
- practical relevance is not inflated into deployment;
- unresolved tasks are precise and assignable.
