---
name: engineering-paper-idea-architecture
description: Convert an industrial problem, partial method idea, dataset, or engineering observation into a coherent engineering-journal paper architecture. Use to evaluate research novelty, choose the manuscript archetype, derive method components from engineering challenges, design the paper story, or decide what evidence is needed before drafting. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Paper Idea And Architecture

Suite version: `4.1.21`

## Mission

Construct one coherent paper before optimizing prose:

`engineering observation -> research question -> technical gap -> design principle -> method -> evidence -> bounded contribution`

An engineering observation or a method insight can seed the study. Before drafting its claims, establish the industrial task, the remaining requirement, and why the proposed mechanism addresses it; a method name alone does not supply that justification.

<!-- invariant: generic-routing -->
<!-- invariant: contribution-calibration -->
<!-- invariant: plural-contribution-routes -->
<!-- invariant: no-fabrication -->
<!-- invariant: claim-evidence-alignment -->

If the topic mixes challenges, methods, tasks, and application scales, first use [`industrial-ai-paper-router`](../industrial-ai-paper-router/SKILL.md). Load only the selected sections of [topic playbooks](../../references/topic-playbooks.md).

## 1. Inventory Available Material

Identify:

- process, equipment, system, and decision objective;
- measurements, labels, sampling, stages, units, conditions, and knowledge sources;
- existing method, code, figures, results, and unresolved errors;
- benchmark and real-world data availability;
- target journal and page constraints;
- claims the author wants to make;
- facts that remain unknown.

Label information as `verified`, `author-confirmed`, `inferred`, or `missing`.

## 2. Choose The Manuscript Archetype

Calibrate the choice with [manuscript archetypes](../../references/manuscript-archetypes.md); do not infer it from the model name.

### General Method With Benchmark And Real-World Validation

Choose when the recurring technical problem exists across processes and the method is intended to transfer with limited configuration.

### Background-Driven Industrial Application

Choose when one process, equipment class, production mechanism, or operational workflow generates the problem and shapes the solution.

### Engineering System Or Automation Framework

Choose when system integration, interfaces, timing, decision workflow, control architecture, or deployment behavior is central.

Do not choose from the algorithm name. Choose from the strongest contribution and evidence.

## 3. Formulate The Research Question

A useful engineering research question specifies:

- the engineering task;
- the difficult condition;
- the missing capability;
- the intended operating scope.

Topic-neutral pattern:

> How can `[engineering output]` remain reliable under `[verified industrial condition]` given `[remaining capability limit or assumption boundary]`, while respecting `[operational or information boundary]`?

Fill every bracket from process facts. Do not reuse an observation, relation, frequency, or supervision theme merely because it appeared in a calibration paper.

Avoid questions that merely ask whether a new network improves accuracy.

## 4. Distinguish Novelty Types

Assess novelty across:

- **problem formulation**: a practical condition is represented more faithfully;
- **method principle**: a new mechanism addresses the condition;
- **engineering integration**: sensing, knowledge, modeling, and decision output are connected coherently;
- **evidence**: a difficult industrial case or diagnostic capability is evaluated credibly;
- **system contribution**: interfaces, workflow, timing, or automation behavior are demonstrated.

State the primary novelty and only the supporting forms the evidence justifies. Do not inflate all five or impose a fixed contribution count.

Assign a provisional contribution track: mechanism-oriented (A), substantive engineering adaptation (B), or focused incremental improvement (C). These are planning categories, not journal quartiles or acceptance predictions. Shared tasks, data and baseline code are permitted with attribution; independent work needs a substantive delta and corresponding evidence. See [contribution boundaries](../../references/research-planning-and-contribution.md) and the [cross-paper delta record](../../assets/templates/cross-paper-delta.md).

The gap can be a capability that remains improvable under established conditions; it need not introduce a new problem or assert that every existing assumption fails. Separate borrowed modules from the proposed modification.

### Choose A Contribution Narrative

Select [the dominant contribution route](../../references/contribution-narratives.md) independently of the manuscript archetype: new formulation, familiar problem/new mechanism, interacting constraints, engineering adaptation, or focused comparison. Respect prior work's documented achievements, identify the condition-specific remaining requirement, and connect the design to a discriminating test. A stronger method need not imply a new problem, and a new problem does not imply a new mechanism. Specify what evidence would support improved generalization or practical value before using those outcomes in the narrative.

## 5. Build The Problem-Design-Evidence Blueprint

| Engineering/data challenge | Remaining capability limit or assumption boundary | Design response | Required evidence | Boundary |
|---|---|---|---|---|

Map each main component to its role and give each major claim matching evidence. Test the claimed increment with suitable comparisons, analysis, or intervention; deleting a coupled component is not always a valid isolated ablation. Standard supporting components need attribution and a justified role, not a fabricated independent novelty claim. Flag an apparently unjustified component for author discussion rather than deleting it during prose revision.

## 6. Derive A One-Sentence Thesis

Use this structure:

> For [engineering task] under [specific condition], [design principle] enables [capability], as examined through [evidence scope].

This is an internal design sentence, not necessarily manuscript text. If it cannot be written precisely, the paper architecture is not ready.

## 7. Design The Evidence Before The Sections

For each claim, decide whether it requires:

- comparison;
- ablation;
- robustness or condition variation;
- sensitivity;
- visualization or interpretation;
- efficiency or timing;
- real-world case evidence;
- expert or process consistency;
- statistical uncertainty.

Do not promise generalization, robustness, interpretability, efficiency, or deployment without corresponding tests.

## 8. Plan The Figure Story

Common figure roles:

1. process or system context;
2. motivation and limitation of existing approaches;
3. overall framework;
4. key module details;
5. benchmark or experimental process;
6. results answering specific questions;
7. engineering interpretation or case examples.

Each figure should have a scientific job. An overview and a module detail may be complementary when the detail supplies needed operations or information flow; remove redundant content only with the author's agreement. A writing review does not authorize redrawing an approved framework.

## 9. Build The Section Architecture

### Method-Centered Paper

`Introduction -> Related Work -> Problem/Motivation -> Method -> Benchmark -> Real-world case -> Discussion -> Conclusion`

### Background-Driven Paper

`Introduction -> Process/System and diagnostic evidence -> Method -> Industrial experiments -> Engineering discussion -> Conclusion`

### System/Automation Paper

`Introduction -> Background/requirements -> System architecture -> Implementation -> Evaluation -> Discussion -> Conclusion`

These are possible logical structures, not compulsory headings. Integrate Related Work into the Introduction or combine Motivation and Problem Formulation when that preserves the cited argument and suits the paper. Adapt to verified journal requirements; do not add sections solely for symmetry.

## 10. Write Contributions As Contracts

State one primary contribution and only the supporting contributions needed to explain the study; do not pad a fixed count. Each should contain:

- contribution object;
- mechanism or formulation;
- intended effect;
- evidence when appropriate.

The contribution list is a contract: the method and experiments must fulfill every item.

## 11. Test The Architecture

Run five adversarial questions:

1. Is the industrial setting necessary to understand the task, information constraints, or evaluation? A broadly reusable method may remain unchanged across settings; that alone does not make an engineering application superficial.
2. Does each module have a justified function? A standard preprocessing or prediction component can be essential without constituting an independent contribution.
3. Does the strongest claim depend on an experiment that is missing or weak?
4. Are site-specific assumptions hidden inside a general claim?
5. Does the real-world case affect the scientific conclusion, or is it only decoration?

## 12. Expected Output

Produce:

- manuscript archetype and rationale;
- one-sentence thesis;
- research question and scope;
- novelty hierarchy;
- Problem-Design-Evidence Blueprint;
- section outline with paragraph functions;
- figure and table roles;
- experiment requirements;
- concise author-decision list.

## 13. Quality Gate

The architecture is ready only when:

- the problem is supported independently of the chosen model;
- the design addresses the stated problem, without inventing a historical engineering derivation;
- evidence is planned for each claim;
- the industrial case has a defined role;
- novelty is specific and bounded;
- terminology remains at the engineering level until model objects are defined;
- no missing fact has been silently invented.
