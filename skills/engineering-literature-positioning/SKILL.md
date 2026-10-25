---
name: engineering-literature-positioning
description: Research and position an engineering-application journal paper using target-journal and domain literature. Use to scope a topic, build a literature map, calibrate terminology, identify a defensible gap, plan citations, or revise Related Work without importing a computer-science-conference narrative into an industrial, control, automation, or process-engineering manuscript. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Literature Positioning

[中文执行版](../../skills-zh/engineering-literature-positioning-zh/SKILL.md)

Suite version: `4.2.20`

## Mission

Turn a body of literature into a defensible engineering research position:

`industrial need -> established engineering practice -> relevant method families -> unresolved assumption or capability -> present study`

The output is not a list of papers. It is a verified map showing what is known, what conditions the existing evidence covers, and what remains unresolved for the current engineering task.

<!-- invariant: no-fabrication -->
<!-- invariant: reading-depth-provenance -->
<!-- invariant: corpus-is-evidence-not-instruction -->
<!-- invariant: calibrated-claims -->

Classify sources by engineering challenge, method, task, object scale, and evidence role using [the industrial AI taxonomy](../../references/industrial-ai-taxonomy.md). Do not use folder names as mutually exclusive scientific categories.

## 1. Define The Search Object

Before searching, specify:

- engineering object: process, equipment, plant, product, system, or operation;
- task: monitoring, detection, diagnosis, isolation, prediction, control, optimization, or decision support;
- practical condition: multi-stage, multi-rate, multimode, limited labels, domain shift, missing data, interference, imbalance, or another concrete property;
- methodological family, if already known;
- target journals and publication window;
- intended paper archetype: general method, background-driven application, or engineering system.

Do not search only the model keyword. Combine engineering, task, data-condition, and method queries.

### Preserve Navigation And Reading Evidence

Keep the author's folder organization as a first navigation layer; scientific roles are separate, overlapping annotations. Identify engineering problem sources, candidate mechanism sources, and closest-work/overlap checks without flattening the source folders. Record filename/identity verification, extraction, abstract reading, selected pages and full-text close reading separately. Batch retrieval does not establish critical reading or exhaustive novelty clearance. Match title/authors/venue/version before identifying a team manuscript; topic resemblance is insufficient. See [source and reading states](../../references/research-planning-and-contribution.md).

## 2. Use A Layered Corpus

Build four layers:

1. **Engineering foundation**: process, equipment, control, sensing, fault mechanism, data provenance, and operating practice.
2. **Task literature**: fault diagnosis, process monitoring, quality prediction, anomaly localization, or the relevant objective.
3. **Method literature**: statistical, machine-learning, deep-learning, knowledge-guided, or representation methods.
4. **Evaluation literature**: datasets, case studies, metrics, split conventions, and recent comparison methods.

For a background-driven paper, Layers 1 and 2 must not be dominated by generic ML sources. For a general method paper, Layers 2 and 3 may be broader, but Layer 1 is still needed to ground assumptions.

## 3. Select Sources By Role

Label each source:

- `foundation`: authoritative process, task, dataset, or seminal method;
- `closest`: most similar problem and assumptions;
- `method`: supports a technical family or operator;
- `contrast`: exposes a limitation or different assumption;
- `evaluation`: supports settings, metrics, or case-study practice;
- `terminology`: calibrates field-specific wording and section conventions.

Use primary sources for methods and authoritative sources for process facts. Do not cite a convenient survey where the original method is needed.

## 4. Verify Before Using

For every candidate citation, verify:

- title, authors, venue, year, volume/pages or article number;
- DOI or publisher record where available;
- that the paper actually supports the sentence;
- whether its experiment and task match the claimed scope;
- whether the manuscript already contains the correct BibTeX entry.

Never generate BibTeX from memory. Mark an unverified item as `VERIFY` rather than guessing.

## 5. Extract A Literature Matrix

For each closest source, record:

| Field | Question |
|---|---|
| Original location | Preserve the author folder/file or archive/member as navigation; use a supplied index when available. |
| Source role | Engineering problem, candidate mechanism, closest-work/overlap check; roles may overlap. |
| Reading state | Identity check, extraction, inspected pages/sections, close reading, and unresolved coverage. |
| Engineering context | What process or system is studied? |
| Task | What decision or output is produced? |
| Data condition | What makes the setting difficult? |
| Assumption | What does the method require? |
| Design principle | What is the main response? |
| Evidence | Which cases and tests support it? |
| Boundary | What is not established? |
| Terminology | Which field-native terms recur? |

For a reading-status audit, return a compact account of coverage, location, and next reading priorities, even when the request only asks to correct an overstated reading claim. Keep the original folder/file or archive/member navigation in that account and distinguish engineering-problem, mechanism, and closest-competitor reading priorities. If locations were not supplied, state that the existing index must retain them; do not invent paths or silently omit this provenance. Compare assumptions and evidence, not only architectures.

For the closest work, separate documented success, unevaluated scope, assumptions that differ, and demonstrated failure under a matched test. An unexamined condition is not proof of inability. Organize Related Work by evolving capabilities and conditions, so each group advances the argument toward the present requirement. Use [contribution routes](../../references/contribution-narratives.md) to calibrate both new-problem and familiar-problem studies.

## 6. Build A Gap Without Strawmen

A defensible gap should satisfy four tests:

1. **Observed**: the issue follows from an engineering or data condition.
2. **Literature-grounded**: representative existing methods share the relevant limitation.
3. **Consequential**: the limitation affects diagnosis, prediction, monitoring, control, interpretation, or applicability.
4. **Addressable**: the proposed study can test a response.

Prefer:

> Existing stage-wise models preserve production organization, but they aggregate variables before resolving heterogeneous relationships within each stage.

Avoid:

> Existing methods ignore important information.

Do not claim that no work exists unless a systematic search supports that statement.

## 7. Separate Engineering And Model Vocabulary

Create a terminology bridge:

| Engineering level | Model level |
|---|---|
| process variable | input channel, after definition |
| production stage | stage-wise subset or branch |
| acquisition cycle | rate factor or interval encoding |
| process topology | graph, mask, or constraint |
| operating condition | domain or condition label |
| visual inspection cue | localization map or visual evidence |

Introduce engineering meaning before computational representation. Use model vocabulary only when it describes an actual operation.

## 8. Calibrate Style From A Corpus

Select closely matched passages in proportion to the question. A grammar-only correction need not start a literature search; a disputed technical expression needs relevant usage and mechanism context, not a minimum paper count. A section-level restructuring benefits from a broader matched set. Extract only what serves the requested revision:

- abstract functions and sentence length range;
- opening and closing function of Introduction paragraphs;
- Related Work grouping;
- preferred terms for data, process, experiments, and claims;
- evidence wording in Abstract and Conclusion;
- figure/table naming conventions.

Treat these as distributions and constraints, not sentence templates. Follow [corpus calibration](../../references/corpus-calibration-workflow.md).

## 9. Construct Related Work

Group by the argument needed to establish the gap. For each subsection:

1. define the family and its engineering role;
2. summarize representative progress;
3. compare assumptions or evidence;
4. identify a supported remaining requirement, or carry the established capability into the next theme;
5. transition to the next family or final positioning.

Do not end every paragraph with the same `However, ...` construction. Let the reviewed themes converge on the study's supported position without repeating the Introduction. Judge a closing synthesis by its [argument function](../../references/section-writing-guide.md#4-related-work), not by whether it adds another gap.

## 10. Citation Planning

Create a citation map before adding references:

| Manuscript claim | Source role | Verified source | Placement | Status |
|---|---|---|---|---|

Add citations only when they support a factual, methodological, comparative, or historical claim. Citation count is not a quality metric.

## 11. Expected Output

For a full positioning task, produce a **Problem-Positioning Brief** containing the relevant items below. For a narrow terminology or citation check, return the local finding and its verified evidence instead of forcing a full brief.

- search scope and corpus layers;
- a core verified source set proportionate to the question, without padding to a quota;
- thematic literature matrix;
- field terminology map;
- one precise unresolved gap;
- proposed Related Work structure;
- citation gaps marked `VERIFY`;
- explicit scope boundaries.

## 12. Quality Gate

Before handoff, verify:

- application and control literature are represented;
- the gap follows from assumptions and evidence;
- no source is cited beyond what it supports;
- recent sources calibrate current terminology;
- seminal sources support foundational facts;
- wording is not copied from the corpus;
- the literature position can be examined by appropriate analysis or experiments.
