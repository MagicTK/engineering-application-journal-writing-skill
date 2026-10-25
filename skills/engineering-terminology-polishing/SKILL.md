---
name: engineering-terminology-polishing
description: Polish English or Chinese engineering-application journal prose while preserving technical meaning, formulas, citations, confirmed results, and layout. Use to remove computer-science-conference phrasing, improve engineering terminology, paragraph transitions, sentence rhythm, claim calibration, and author voice in industrial, control, automation, process, and equipment papers. Use this canonical version for English-language requests, regardless of manuscript language; use the -zh mirror for Chinese-language requests.
---

# Engineering Terminology And Polishing

[中文执行版](../../skills-zh/engineering-terminology-polishing-zh/SKILL.md)

Suite version: `4.2.28`

## Mission

Improve precision, readability, and engineering register without changing the science.

Polishing is constrained revision, not rewriting by instinct.

Read [argument and prose craft](../../references/argument-and-prose-craft.md) when revising argument flow, prior-work comparisons, contribution framing, or defensive prose. Its procedures and engineering examples are self-contained.

<!-- invariant: authoritative-source-lock -->
<!-- invariant: layout-lock -->
<!-- invariant: calibrated-claims -->
<!-- invariant: anti-defensive-writing -->
<!-- invariant: multiple-innovation-routes -->
<!-- invariant: author-manuscript-separation -->

## 1. Establish Locks

Before editing, identify:

- authoritative manuscript version;
- content that may or may not be rewritten;
- confirmed terminology, formulas, citations, and numerical values;
- author-defined figure/table placement and style;
- target journal and language;
- author writing samples or preferred wording.

If the task is language-only, do not alter equations, experimental settings, results, references, floats, table fonts, or figure sizes.

When both an uploaded archive and a live collaborative manuscript exist, compare their current contents before choosing the revision base. Reused filenames do not establish version identity. Review active LaTeX and the compiled PDF; exclude comments and disabled branches from findings about published text. Keep local revision, author approval, online synchronization, and verified online compilation as separate states.

## 2. Build A Terminology Map

Create a manuscript-specific map:

| Concept | Preferred term | Avoid or restrict | Reason |
|---|---|---|---|

Cover:

- process/equipment names;
- task definition;
- variables, sensors, stages, units, rates, and conditions;
- domain/expert knowledge;
- model objects;
- metrics and case-study names;
- offline, online, real-world, and deployment wording.

Use the same term for the same object across title, Abstract, figures, formulas, tables, and Conclusion.

Use the shared [engineering-application terminology bank](../../references/engineering-application-terminology-bank.md) for generic terms and caution words. Keep manuscript-specific terminology maps in the manuscript project rather than adding them to the shared bank.

For an already checked base name, choose the relevant [lookup group](../../references/engineering-application-terminology-bank.md#11-checked-core-names-and-remaining-scope), then read its exact record, scope and separate Chinese wording check. These are reading routes, not exclusive problem/method classes; a local wording query need not load every unrelated record.

Apply its name-admission procedure before recommending a shared mechanism,
module, method or operation category: at least two distinct relevant published
journal papers with matching meanings, preferably three to five for ambiguous
terms. Keep the full name separate from its head word. Verify Chinese online
independently, preserving the English identity when a translation is unverified.
Distinguish attributed single-paper names, author-proposed names and plain
functional descriptions from general terms. Do not erase an accurate name or
invent a replacement just because general-admission evidence is incomplete.

For disputed state/condition, variable/attribute, sample/record and feature wording, read [context-sensitive terminology decisions](../../references/terminology-decisions.md). The read-only `scripts/audit_terminology.py` at the suite root can list candidates and recurring collocations through common literal text-emphasis wrappers, retaining source line spans; it does not judge grammar, expand arbitrary TeX macros or replace active-PDF verification. Do not treat corpus absence as a ban or the author's local preference as a universal rule.

Its ordinary within-paragraph line-wrap handling reports source `line`/`end_line` spans. Excluded metadata and literal directive lines are conservative phrase boundaries, so absence across such syntax is not proof that the rendered phrase is absent. Keep the script's tokenizer limits separate from the semantic terminology review.

For a full-manuscript terminology audit, extract recurring content words and
two-to-four-word collocations, then review those carrying engineering meaning.
Three occurrences is a configurable starting point, not a reason to ignore a
consequential term used once. Inspect relevant published contexts for disputed
usage; record coverage only for sources actually searched. Do not limit a full
audit to the author's examples. For a sentence-level request, stay within the
authorized scope and flag only necessary consistency dependencies. Exclude
routine mathematical operators, activation functions, tensor operations, method
names and dataset labels unless inconsistent. Rewrite by semantic function,
not a global synonym replacement.

## 3. Keep Engineering Objects Primary

Prefer engineering terms before model terms:

- `process variables` before `channels`;
- `production stages` before `branches`;
- `sampling cycles` before `interval embeddings`;
- `process connections` before `graph edges`;
- `operating conditions` before `domains`;
- `inspection regions` before `spatial tokens`.

When a process variable is represented as one input channel, define that correspondence once. Then use `channel` only for model operations.

### Industrial Data Descriptions

- Name the actual object: `sample` for one learning/evaluation instance, `observation` or `measurement` for a measured value or time step, `dataset` for the collection, and `process variable` for a measured or manipulated process quantity. Define whether one sample represents a product, batch, window, or other unit.
- Do not substitute `record`, `snapshot`, `descriptor`, or `attribute` for these objects merely for stylistic variety. These terms remain appropriate when they genuinely denote database/log records, explicitly defined instantaneous states, derived feature descriptors, or semantic/graph attributes. `Dataset size` denotes a count, not the dataset itself.
- Introduce class meanings and counts where the dataset is described. Use ordinary lowercase fault names in prose unless a proper name or official identifier requires otherwise. Repeat names only when the new sentence needs them; preserve labeling priorities for coexisting defects without repeatedly re-listing the taxonomy.
- Describe the production source, authorized collection period, sample/label construction, data partitions, and preprocessing to the extent needed to interpret and reproduce the evaluation. Do not import facts from another paper's dataset. Preserve the distinction between a development set and its training/validation subsets.
- Exclude confidential product specifications, grades, recipes, or selection details when disclosure is not authorized. Where omission affects reproducibility or scope, record the need for an approved aggregate description in the author handoff. Check the shareable source as well as the visible PDF; retain originals only in the protected local history, not in a submission package.
- Removing a term such as `snapshot` must not remove the definition of what the model actually receives. For a vector-based industrial case using a temporal model, explain the real input construction and settings; never describe padding or variable ordering as observed temporal dynamics.

## 4. Use Knowledge Terms Precisely

- `domain knowledge`: process topology, equipment relations, control logic, known production routes, or expert rules.
- `expert knowledge`: information obtained from operators, engineers, or specialists.
- `prior knowledge`: acceptable when the knowledge is introduced before learning.
- `prior`: use as a technical noun only when a mathematical prior, graph, mask, constraint, or bias is defined.

Prefer `fusion guided by domain knowledge` or `domain-knowledge-guided fusion` according to sentence position. Avoid long stacks of hyphenated modifiers.

## 5. Calibrate Engineering Evidence Terms

- `benchmark case study`: evaluation on a defined reference task or dataset; public access and experimental control require separate verification.
- `real-world industrial case study`: production-source evidence.
- `actual production conditions`: tested operating context.
- `practical relevance` or `engineering applicability`: may be supported by a real-world industrial case within its evaluated scope.
- `online operation` or `industrial deployment`: use only with evaluated online/deployed evidence.

Prefer `comparison methods` or `comparative methods` in engineering prose and tables. `Baseline` is acceptable when referring to a specific reference configuration.

## 6. Revise Sentences By Function

For each sentence, ask:

- What fact, relationship, method action, result, or implication does it carry?
- Is the subject the correct engineering or model object?
- Is the verb precise?
- Does the qualifier match the evidence?
- Can a stacked noun phrase be expanded?
- Is the sentence longer than its logical structure can support?

Use subordinate clauses when they clarify the relationship between ideas. Split sentences whose independent claims, enumerations, or nested method details obscure that relationship; do not enforce a fixed clause or word count.

Move from known information to new information: a defined engineering object or result introduces the next operation or implication. Keep the subject near its verb and make pronoun references explicit. Delete sentences that add no fact, relation, evidence, or necessary guidance. Preserve accurate verbs such as `combine`, `adapt`, and `extend`; promotional word substitutions cannot increase novelty.

Length is an outcome, not the objective. Use enough detail to make the engineering meaning and logical progression clear, without redundant restatement. Add missing necessary information and remove repetition as appropriate; do not shorten or expand a mature manuscript simply to make the revision visible.

## 7. Revise Paragraphs By Role

Each paragraph should have one main job:

- opening: establish the point or transition;
- middle: provide evidence, comparison, or technical development;
- closing: state implication, limitation, or transition.

Do not begin a paragraph with `Fig. X illustrates...` when the paragraph's real job is motivation. State the scientific point first and cite the figure naturally.

Avoid repetitive transitions such as a sequence of `However`, `Therefore`, and `To address this issue` paragraphs.

Check the substantive link between paragraphs: the preceding capability, condition, or result should motivate the next requirement or inference. A paragraph need not end with a summary when its reasoning is complete. Keep author-facing paragraph diagnoses out of manuscript prose.

## 8. Abstract Polish

Check six functions:

1. engineering context and challenge;
2. existing limitation;
3. proposed method;
4. principal design ideas;
5. evaluation cases;
6. evidence-based conclusion.

The first sentence should connect context and difficulty without becoming overloaded. Remove implementation transitions that add no scientific relationship. Close on the actual evaluation and its supported conclusion; use a benchmark/production pair only when both exist. Keep this concise without inventing another case or turning it into a leaderboard summary.

## 9. Introduction And Related Work Polish

- Keep the industrial object visible after the opening paragraph.
- Define process/data properties before introducing computational strategies.
- Make topic sentences carry the paragraph argument.
- Explain prior capabilities and the relevant assumptions; identify a remaining requirement only when supported by the source or a documented comparison.
- Introduce the method only after the unresolved requirement is clear.
- Keep contribution items concrete and testable.

Calibrate the argument to the actual innovation route: a new problem/formulation, an interaction between familiar conditions, a mechanism for an established problem, an engineering adaptation, or a focused comparative finding. Routes can coexist. Do not manufacture a new problem during polishing or weaken a supported new formulation merely because the field already has related tasks. Explain what changes and how the evidence tests it.

Organize Related Work by capability development and changing assumptions. Distinguish an explicit assumption, an untested setting, and an observed failure. Avoid treating non-evaluation as failure or using collective criticism such as `existing methods ignore industrial complexity`. Link the supported remaining requirement to the mechanism and its evaluation. Use as many contribution items as the real advances require; there is no preset count.

## 10. Method And Experiment Polish

For methods, use:

`motivation -> input/output -> operation -> engineering meaning -> transition`

For results, use:

`question -> evidence -> comparison -> engineering interpretation -> boundary`

Avoid `Table X shows` as the only analysis. Avoid explaining every improvement as `better feature extraction`.

Separate measured findings, mechanism interpretations, and hypotheses. Identify the changed operating conditions or sites when claiming generalization, and the measured engineering benefit when claiming practicality. A focused comparison supports a statement about its relevant reference set; it does not require a claim of universal superiority. Captions and text must agree without mechanically repeating the same conclusion three times.

## 11. Remove AI-Typical Prose

Revise:

- repeated abstract nouns and inflated adjectives;
- uniform sentence lengths;
- excessive throat-clearing;
- generic phrases such as `plays a crucial role`, `has attracted extensive attention`, or `provides a new perspective` when unsupported;
- repeated negative framing and defensive caveats;
- excessive `not only ... but also ...` structures;
- decorative words such as `novel`, `comprehensive`, `holistic`, and `superior` without specific meaning.

Do not pursue detector evasion. Aim for precise, varied, author-compatible academic prose.

Judge revisions by information, logic, and evidence. Vocabulary, punctuation, and sentence length cannot establish AI authorship. Use contextual diagnosis without mechanical word bans, punctuation or sentence-length quotas, or AI-detection probability targets.

Classify each flagged sentence as empty metadiscourse, a necessary scope condition, a real limitation, an evidence-based qualification, or a useful conceptual contrast. Remove defensive framing aimed at imagined objections and unsupported phrases such as `this further clarifies the superiority`. State the object, operation, or finding directly. Inspect habitual `not X but Y` without deleting a scientifically necessary contrast.

Keep a necessary qualifier beside a claim when omission would change its meaning, including in the Abstract. Put detailed methodological limits in Methods and their implications in Discussion. Avoid repeated caveats unless another statement independently needs them for accuracy. Preserve real uncertainty and name its source. For ordinary experiments, prefer direct descriptions to `protocol` wording.

## 12. Corpus And Author Calibration

Priority:

1. discipline and task terminology;
2. target-journal convention;
3. author's established style;
4. generic academic-writing preference.

Use multiple recent target-journal papers. Author-written samples may calibrate voice only after their technical terminology has passed external-corpus review; they must not define the terminology standard for their own revision. Extract preferences; do not copy sentences. Follow [corpus calibration](../../references/corpus-calibration-workflow.md), [terminology guidance](../../references/terminology-and-style.md), and the [terminology bank](../../references/engineering-application-terminology-bank.md).

## 13. Output Modes

### Direct Revision

Edit the authoritative source, preserve locks, compile when requested, and report substantive changes.

### Suggested Rewrite

Provide original/revised text only when the user wants to decide before editing.

### Terminology Audit

Return a concise table of inconsistent, computer-science-heavy, ambiguous, or overclaimed terms.

### Manuscript Text And Author Notes

Separate proposed manuscript wording from author-facing diagnoses, unverified literature statements, missing evidence, and scientific decisions. Preserve supported text and record the exact source or experiment needed for unresolved claims. Visibly mark placeholders in internal drafts; do not fill them with plausible values or present planned results as completed. Worked examples in the shared guide are hypothetical and become usable manuscript prose only after their factual prerequisites are verified.

## 14. Quality Gate

Before handoff, verify:

- meaning and numbers are unchanged unless explicitly corrected;
- engineering and model objects are not conflated;
- terminology is consistent;
- claims match evidence;
- the contribution route matches the work and prior capabilities are represented fairly;
- sentence rhythm is varied but controlled;
- paragraph transitions reflect logic;
- citations remain attached to the correct claims;
- author diagnostics and unresolved placeholders are distinct from manuscript-ready prose;
- layout locks have not been disturbed.
