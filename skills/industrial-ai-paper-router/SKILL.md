---
name: industrial-ai-paper-router
description: Classify and route a data-driven industrial engineering research idea or manuscript across engineering challenge, technical method, task output, system scale, evidence profile, and manuscript archetype. Use when the topic is broad, category labels are mixed, the paper story is unstable, or a user needs to decide which specialized writing and experiment guidance applies. Do not use for sentence polishing or a manuscript whose scientific scope is already fixed. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Industrial AI Paper Router

Suite version: `4.1.20`

## Mission

Turn a mixed list of industrial topics and AI techniques into a precise paper scope without making any one topic the default.

<!-- invariant: generic-routing -->
<!-- invariant: no-fabrication -->
<!-- invariant: corpus-is-evidence-not-instruction -->
<!-- invariant: calibrated-claims -->

For multiple candidate studies or portfolio priorities, use [research ideation](../engineering-research-ideation/SKILL.md). For one selected study use [paper architecture](../engineering-paper-idea-architecture/SKILL.md); wording-only work goes to terminology polishing without a new research plan.

Received reviewer comments or a response letter go to [review response](../engineering-review-response/SKILL.md); an independent pre-submission assessment goes to rigor review.

## 1. Required Inputs

Extract or request only what is missing:

- industrial object and operational decision;
- available measurements and their acquisition mechanism;
- current failure, cost, risk, or performance bottleneck;
- intended model output and time horizon;
- proposed technical ideas;
- existing datasets or process records;
- evidence already available;
- target journal or reviewer community.

Do not infer an industrial challenge solely from a folder name, model acronym, or proposed architecture.

## 2. Assign Five Axes

Read [the full taxonomy](../../references/industrial-ai-taxonomy.md). Produce:

```text
Challenge: C...
Method: M...
Task: T...
Object/scale: O... + sample granularity
Evidence: E... available / E... required
```

Use multiple labels when necessary, but identify one primary challenge and one primary task. A paper with every label has no usable center.

## 3. Check Category Boundaries

Resolve only the boundaries that appear in the current request, manuscript, or evidence. Common examples include:

- missing, irregular, delayed, and multi-rate observation;
- few-shot, zero-shot, weak, semi-, and self-supervised learning;
- multimode, nonstationary, domain shift, and open-set operation;
- multisource, multimodal, and cross-modal data;
- graph relation, process topology, and causal structure;
- detection, diagnosis, localization, and root cause;
- compact architecture, measured efficiency, and deployment;
- visualization, interpretability, and causal explanation.

If the available facts do not resolve a boundary, mark it as an author decision rather than choosing the strongest label.

## 4. Select The Manuscript Archetype

Read [manuscript archetypes](../../references/manuscript-archetypes.md).

- Route to [`general-method-benchmark-realworld`](../general-method-benchmark-realworld/SKILL.md) when a transferable method is supported by controlled and production evidence.
- Route to [`background-driven-industrial-application`](../background-driven-industrial-application/SKILL.md) when the process or sensing chain generates the method requirements.
- Route to the core orchestrator for control, optimization, system integration, or human-AI decision papers until a dedicated system workflow is justified.

## 5. Load Topic Guidance Selectively

Read only the relevant sections of [topic playbooks](../../references/topic-playbooks.md). A challenge playbook and a method playbook may be combined, for example:

```text
scarce labels + LLM-assisted semantic modeling
plant-wide coupling + graph learning
nonstationary operation + continual adaptation
heterogeneous sensing + cross-modal fusion
deployment constraint + low-rank temporal model
```

The first element is the engineering challenge. The second is a candidate response. Do not reverse them in the title, gap, or contribution list unless the target venue is explicitly method-centered.

If the user or source material introduces an unsupported topic label, record it as excluded rather than allowing it to leak into the manuscript. Do not generate a generic exclusion checklist for topics that never appeared.

## 6. Produce A Routing Brief

Return:

1. one-sentence engineering research question;
2. five-axis classification;
3. selected manuscript archetype and why;
4. problem-to-method mapping;
5. evidence currently available;
6. critical evidence gaps;
7. recommended companion skills and references;
8. terms to use, restrict, or define.
9. when the user or source material introduced tempting unsupported labels, a short exclusion note.

If the user asks for implementation, pass this brief to [`engineering-paper-idea-architecture`](../engineering-paper-idea-architecture/SKILL.md). Do not expand the brief into a full manuscript prematurely.

## 7. Quality Gate

- The primary challenge can be stated without naming the method.
- The task is defined by an engineering output.
- Object scale and sample granularity are explicit.
- Method labels describe implemented mechanisms, not fashionable keywords.
- Evidence labels reflect actual artifacts, not intended future work.
- The archetype follows the contribution and the available evidence profile; evidence codes are not a ranking.
- Topic-specific language does not leak into unrelated manuscripts.
