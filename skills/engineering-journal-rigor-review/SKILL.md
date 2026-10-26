---
name: engineering-journal-rigor-review
description: Perform a submission-level rigor review of an engineering-application journal manuscript. Use to evaluate engineering significance, argument coherence, methodological correctness, evidence relevance, experimental fairness, numerical consistency, citation integrity, terminology, reproducibility, claim scope, and presentation before submission to leading IEEE, Elsevier, IFAC, or related journals. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Journal Rigor Review

[中文执行版](../../skills-zh/engineering-journal-rigor-review-zh/SKILL.md)

Suite version: `4.2.44`

## Mission

Review the manuscript as an engineering-journal referee, not only as a language editor or ML benchmark reviewer.

Lead with actionable findings. Distinguish manuscript errors, unsupported claims, missing evidence, author decisions, and optional improvements.

<!-- invariant: no-fabrication -->
<!-- invariant: cross-paper-substantive-delta -->
<!-- invariant: authoritative-source-lock -->
<!-- invariant: claim-evidence-alignment -->
<!-- invariant: layout-lock -->
<!-- invariant: calibrated-claims -->

## 1. Establish Review Scope

Record:

- target journal or journal class;
- manuscript archetype;
- engineering task and claimed contribution;
- authoritative source/PDF version;
- confirmed incomplete experiments or placeholders;
- author-defined content, data, and layout locks.

Review the latest manuscript, tables, figures, bibliography, and available experiment notes together.

## 2. Review Dimensions

Before inspecting headline results, write a short review contract containing the manuscript's strongest intended claim, the minimum evidence needed to support it, and the conditions that would force the claim to be weakened. This reduces result-driven rationalization during review.

Score or assess nine dimensions:

1. **Engineering significance**: Is the practical problem important and well defined?
2. **Positioning and novelty**: Is the gap literature-grounded and nontrivial?
3. **Argument coherence**: Do problem, design, claims, and evidence form one chain?
4. **Methodological correctness**: Are assumptions, formulas, symbols, dimensions, and operations coherent?
5. **Evidence relevance**: Does each experiment test the claim attached to it?
6. **Experimental rigor**: Are splits, comparisons, metrics, ablations, and settings fair and reproducible?
7. **Scope calibration**: Are robustness, generalization, interpretation, and practical claims bounded correctly?
8. **Source and data integrity**: Are citations, results, captions, tables, and prose consistent?
9. **Presentation quality**: Are terminology, figures, tables, captions, and layout readable and professional?

## 3. Severity Levels

- **Critical**: invalidates a central claim, task, result, or submission artifact.
- **Major**: materially weakens novelty, correctness, evidence, reproducibility, or interpretation.
- **Minor**: should be fixed but does not change the central conclusion.
- **Suggestion**: optional improvement with a clear benefit.

Do not inflate style preferences into major findings.

## 4. Engineering Significance Audit

Check whether:

- the industrial object and decision objective are explicit;
- the difficult condition arises from process, sensing, operation, data, or workflow;
- the method addresses a real requirement rather than a generic representation gap;
- the output has a defined diagnostic, predictive, monitoring, control, or inspection role;
- practical relevance is supported by the case-study design.

For background-driven papers, verify that the process mechanism truly shapes the method. For general methods, verify that the abstraction is broader than one dataset but not universal.

## 5. Positioning And Novelty Audit

Check:

- representative engineering and method literature;
- current target-journal terminology;
- closest methods and their assumptions;
- absence of strawman criticism;
- novelty at problem, method, integration, evidence, or system level;
- contribution items that map to method and experiments.

Flag novelty claims based only on renaming known modules.

### Cross-Paper Contribution Review

For related studies, trace reused data/modules/code and attribution, the actual mechanism change, operating assumptions, new capability and isolating evidence. Use [the cross-paper delta record](../../assets/templates/cross-paper-delta.md). Familiar tasks do not invalidate independent follow-up work; a focused adaptation can be legitimate. Conversely, names, seeds, arbitrary subset changes or rewritten prose alone do not justify a separate paper. Recommend merging or dropping unsupported standalone claims; similarity software does not replace substantive review. Track A/B/C does not determine venue tier or relax evidence standards. Apply [contribution boundaries](../../references/research-planning-and-contribution.md).

## 6. Argument Coherence Audit

Build this map:

`observation -> gap -> requirement -> design -> claim -> evidence -> conclusion`

Flag:

- motivated problems not addressed by the method;
- modules without a role in the stated requirement;
- contributions without the evidence they need, whether analysis, experiments or operational validation;
- experiments unrelated to claims;
- conclusions that introduce new claims;
- benchmark and real-world cases presented as interchangeable.

## 7. Method And Mathematics Audit

Check:

- problem definition and information available at inference time;
- set, partition, mask, graph, direction, and constraint definitions;
- symbol uniqueness and dimensions;
- predicted probabilities versus predicted labels;
- stage/rate/cluster/class indices;
- objective terms and weights;
- consistency between equations, captions, diagrams, and prose;
- whether equations add necessary formal meaning;
- whether domain knowledge is defined and introduced at the correct operation.

Do not demand more formulas when prose is clearer. For a central mathematical claim, test a minimal example before accepting the wording: zeroing a finite logit does not exclude its class after softmax; row and column normalization have different denominators; a block-diagonal operator does not prove physical independence. Check shapes, reduction axes and subsequent operations against the implementation when available. Treat an unavailable implementation as a verification limit, not permission to silently repair the method. A published reference can motivate this check but cannot override the mathematics.

## 8. Evidence And Experiment Audit

For each main claim, identify the required evidence type. Check:

- data provenance and split unit;
- leakage from adjacent windows, repeated products, future labels, or normalization;
- comparison relevance and information access;
- reproducibility of input adaptations and settings;
- main comparison and ablation alignment;
- plausible robustness conditions;
- sensitivity of scientifically important parameters;
- metric suitability for imbalance and class-wise diagnosis;
- uncertainty when small differences matter;
- interpretation validation beyond attractive visualizations.

Use the [experiment-evidence guide](../../references/experiment-evidence-design.md).

## 9. Numerical And Cross-Artifact Audit

Recompute or compare where possible:

- sample totals and split counts;
- weighted averages from class support;
- main full-model and ablation full-model values;
- Abstract/Introduction/Conclusion values against tables;
- figure labels and captions against source data;
- metric names and percentage/percentage-point wording;
- method names and variants across prose and tables;
- bibliography entries and citation keys.

Classify an issue as transcription, arithmetic, version mismatch, missing result, or scientific inconsistency.

## 10. Claim-Scope Audit

Evidence needed:

| Claim | Minimum evidence |
|---|---|
| improvement | fair comparison |
| component contribution | valid isolating comparison, intervention or analysis |
| robustness | evaluation spanning the claimed disturbance/condition range |
| generalization | independent held-out evidence for the claimed population or transfer setting |
| interpretability | validation against process, label, perturbation, or expert evidence |
| efficiency | parameters/FLOPs/time/memory as claimed |
| engineering relevance | task-grounded evidence under meaningful engineering conditions; not automatically field validation |
| production applicability | evidence from the claimed production setting, with acquisition and selection scope |
| deployment | evaluated actual operational integration, with advisory/shadow/closed-loop scope stated |

Downgrade wording when evidence cannot be expanded. Check comparator, metric and aggregation level before accepting `best`, `all classes` or `consistently`; an aggregate lead is not class-wise dominance. See the [consistency ledger](../../references/experiment-evidence-design.md#9-consistency-ledger).

## 11. Terminology And Presentation Audit

Check:

- engineering objects introduced before model objects;
- process variables versus channels;
- domain/expert/prior knowledge usage;
- real-world, industrial, online, and deployment wording;
- abbreviations defined once;
- section and paragraph functions;
- caption independence and readability;
- table font and figure placement against author locks;
- blank columns, isolated text, tiny labels, and float order in the rendered PDF.

## 12. Independent Review Passes

When scope permits, perform separate passes before synthesis:

1. engineering/domain reviewer;
2. method/math reviewer;
3. experiment/data reviewer;
4. writing/terminology reviewer;
5. adversarial reviewer testing the strongest claim.

Do not let one pass see and merely repeat another pass's verdict. Merge duplicate findings afterward.

If the task is to answer received comments and verify corresponding revisions, use [review response](../engineering-review-response/SKILL.md). For iterative research evidence handoffs use [the collaboration workflow](../../references/research-collaboration-workflow.md).

## 13. Review Output

Write findings first, ordered by severity. Each finding contains:

- ID and severity;
- location;
- observed issue;
- why it matters;
- exact fix or required decision;
- evidence/source used to identify it.

Then provide:

- strengths that should be preserved;
- manuscript-level verdict: ready, minor revision, major revision, or blocked;
- direct-fix list;
- author-decision list;
- experiment-owner list, limited to genuine inconsistencies or missing evidence.

Do not bury critical issues in a long general summary.

## 14. Revision Verification

After revision:

- check every critical and major finding;
- verify that fixes did not create new numerical or layout inconsistencies;
- recompile and inspect affected pages when LaTeX is available;
- run a final citation/reference check;
- distinguish resolved, partially resolved, accepted limitation, and unresolved.

## 15. Quality Gate

A manuscript is submission-ready only when:

- no central claim lacks relevant evidence;
- the method is mathematically and semantically coherent;
- data splits and comparison settings are defensible;
- numbers agree across artifacts;
- citations are real and correctly used;
- engineering significance remains visible;
- claims remain within tested scope;
- the latest source compiles and the rendered manuscript is professionally readable;
- remaining author tasks are short, specific, and non-duplicative.
