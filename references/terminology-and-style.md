# Engineering Terminology And Style

## Purpose

Use this reference for sentence-level revision, terminology normalization, title/abstract polishing, and removal of conference-style or AI-like prose.

For argument construction, fair comparisons, paragraph progression, and worked examples, use [argument and prose craft](argument-and-prose-craft.md). Treat writing guidance as a way to communicate the supported contribution. Language cannot establish problem novelty, a mechanism's effectiveness, or practical benefit.

## Contents

Terminology hierarchy; variables and model objects; process/case terms; knowledge and constraints; evidence claims; verbs; sentences; Abstract; Results; hyphenation; anti-AI and anti-defensive writing.

## 1. Terminology Hierarchy

Describe each concept at the correct level.

| Level | Preferred focus | Typical terms |
|---|---|---|
| Industrial object | physical process or system | production line, process unit, furnace, mill, reactor, equipment, plant |
| Measurement | observed or controlled quantities | process variable, measured variable, manipulated variable, sensor signal, quality variable |
| Engineering structure | physical or operational organization | stage, unit, route, topology, operating condition, control loop, material flow |
| Modeling object | mathematical representation | input channel, sample, window, feature, graph node, latent representation |
| Model operation | algorithmic mechanism | encoding, grouping, fusion, attention, filtering, alignment, adaptation |
| Evidence | observation and evaluation | case study, comparison, ablation, robustness test, visualization, engineering interpretation |

Move from upper levels to lower levels when introducing a method. Do not begin an industrial problem statement with tokens, embeddings, patches, or channels.

## 2. Engineering Objects And Conditional Model Correspondence

Recommended sequence:

1. Introduce the physical system, measurements, operating conditions, and engineering task.
2. Explain the process role of each object that matters to the scientific problem.
3. Define a correspondence to channels, nodes, tokens, patches, modalities, experts, or other model objects only when that correspondence is part of the selected method.
4. Use the model term only for operations performed on that model object.

The following guidance is conditional. Load it only when the manuscript actually studies variable relationships, variable grouping, multiblock/multistage structure, or channel-wise processing. It is not a default narrative for engineering papers.

For such manuscripts, introduce measured or manipulated process variables first, explain their units, stages, rates, control roles, or relationships, and then state explicitly when one process variable is represented as one input channel. Use `channel-wise` only after this correspondence is defined.

Prefer:

- relationships among process variables;
- partitioning variables by process unit or production stage;
- data-adaptive grouping or clustering within a stage;
- feature interaction or feature fusion between production stages;
- variable-wise representation learning;
- stage-specific or unit-specific process measurements.

Use cautiously:

- channel dependency;
- channel strategy;
- token interaction;
- global embedding space;
- spatial dependency when no physical, topological or graph relation is defined.

`Dependency` describes a modeled or statistical dependence; it does not itself imply causality. Do not substitute `correlation` unless the corresponding statistical meaning is justified. Use `relationship`, `interaction`, `coupling`, `association`, or `feature fusion` only when they describe the actual object or operation. Avoid vague `information exchange` when a specific operation can be named. See [context-sensitive decisions](terminology-decisions.md) for state/condition, sample/record, variable/attribute and feature distinctions.

See the [external-corpus terminology bank](engineering-application-terminology-bank.md) for semantic boundaries and the [Chinese companion](engineering-application-terminology-bank_CN.md) for a concise Chinese reference.

## 3. Process, Production, And Industrial Case Terms

Choose the term that matches the evidence:

- **industrial process**: broad technical setting;
- **production process**: actual production route or manufacturing operation;
- **plant-wide process**: interconnected units or stages across a plant-scale system;
- **process unit**: equipment or functional sub-process;
- **production stage**: sequential or logically separated stage;
- **real-world industrial case study**: evaluation using data from an actual industrial setting;
- **actual production conditions**: measured conditions from production, without implying online deployment;
- **process measurements** or **real-world production data**: measured data from an actual process; use `records` only for actual acquisition/log/database records and `samples` for the defined learning/evaluation units.

Use `offline` only when the distinction from prospective, online, shadow-mode, or closed-loop evaluation is methodologically relevant. It is not a routine synonym for real-world production data and need not be repeated in the Abstract, contributions, or Conclusion.

Avoid repeatedly calling a real production process a `dataset`. Use `dataset` when discussing the data object and `case study`, `process`, or `production line` when discussing the engineering setting.

## 4. Domain Knowledge And Constraints

Use:

- domain knowledge;
- expert knowledge;
- process knowledge;
- process topology;
- physical constraints;
- known process connections;
- engineering constraints;
- process-informed grouping or fusion.

Choose among them based on source:

- topology/flow diagram -> process topology, material flow, equipment connections, or inter-stage relationships;
- operator or engineer judgment -> expert knowledge;
- physics or conservation law -> physical knowledge or physical constraints;
- stage/unit assignment -> process-informed partition;
- matrix added to a score -> prior matrix or structural bias.

Do not call every engineering fact a `prior`. If used as an ordinary noun phrase, write `domain knowledge` without a hyphen. To avoid stacked modifiers, prefer:

- `fusion guided by domain knowledge`;
- `a gate constrained by the process topology`;
- `a process-informed variable partition`.

## 5. Claims About Practical Value

Match wording to validation strength.

| Evidence | Defensible wording |
|---|---|
| Public benchmark only | effectiveness on the benchmark; controlled comparison |
| Retrospective or held-out real-world case | practical relevance; engineering applicability; effectiveness on the evaluated production data |
| Cross-site or cross-line evaluation | transferability across the evaluated sites or lines |
| Online shadow test | online feasibility under the tested setting |
| Closed-loop or deployed system | deployment or operational benefit, limited to the demonstrated system |

Do not move upward in this table without evidence.

Name the dimension of generalization: across evaluated time periods, operating conditions, equipment, production lines, or sites. A random held-out split within one case does not establish transfer across sites. Name the disturbance for robustness claims, and connect practical value to the evaluated engineering quantity. A lower estimation error, fewer false alarms, and lower annotation cost are different benefits and require their own evidence.

Keep the status of a literature statement precise. An explicit assumption, an untested setting, and an observed failure are different facts. When a source did not evaluate a condition, describe the evidence gap; do not turn it into a claim that the method fails. Use respectful, specific attribution to explain what prior work enables before stating the remaining requirement.

## 6. Preferred Verbs

Use verbs that state function rather than praise:

- characterize, represent, organize, partition, align, integrate;
- regulate, constrain, coordinate, preserve, suppress, separate;
- evaluate, examine, quantify, compare, verify, demonstrate;
- indicate, suggest, support, reveal, remain, depend.

Avoid habitual use of:

- leverage, empower, unlock, revolutionize;
- significantly outperform when no statistical or practical significance is established;
- prove for ordinary empirical evidence;
- guarantee, universally, fully, completely;
- effectively in every method sentence.

Preserve `combine`, `adapt`, `extend`, or `integrate` when those verbs accurately describe the design. Choosing a more impressive verb cannot change the innovation level. Use active or passive voice according to the sentence's subject and information flow; neither is mandatory throughout a manuscript.

## 7. Sentence Design

Prefer one main function per sentence. Use subordinate clauses when they clarify causality, contrast, or condition. Split a sentence when its independent claims or nested details obscure the main relation; do not enforce a fixed clause or word count.

Good paragraph rhythm:

1. topic sentence establishes the engineering or scientific subject;
2. middle sentences provide facts, literature, method, or results;
3. final sentence states the unresolved issue, implication, or transition.

Connect known information to new information. Begin with an already defined engineering object, condition, or finding, then introduce the operation or implication that the next sentence will develop. Keep the subject close to its verb, and use the sentence ending for the information that deserves emphasis. A paragraph need not end with a summary when its reasoning is complete.

For revision, annotate the paragraph's main job in author notes: establish a condition, compare capabilities, derive a requirement, explain an operation, interpret evidence, or discuss application scope. Remove sentences that add no fact, reasoning, evidence, or necessary guidance. Keep these diagnostic labels out of the manuscript.

Avoid:

- several consecutive sentences beginning with `This`;
- long noun stacks;
- repeated `Furthermore`, `Moreover`, and `In addition`;
- rhetorical questions in technical sections;
- `It is worth noting that` and `It can be clearly seen that`;
- vague references such as `the above problems` when the problems can be named;
- repeated restatement of a figure caption in prose.

## 8. Abstract Register

The opening can connect structure and difficulty in one sentence:

`[Engineering systems] involve [relevant structure], where [practical phenomenon] complicates [task].`

This is a functional pattern, not reusable wording. Rewrite it from the manuscript's facts.

Method introduction should be direct:

- `To address this limitation, this paper proposes ...`
- `Accordingly, a ... method is developed to ...`

Use those transitions only when the preceding sentence supplies the exact reason. A direct subject and operation is often sufficient. Select the abstract emphasis from the actual contribution: a new formulation, coupled conditions, a mechanism for an established problem, an engineering adaptation, or a focused comparative finding. Do not force every abstract to claim a new problem or superiority to all existing approaches.

Avoid:

- `In the network implementation ...`;
- `In this context ...` when no context is specified;
- `Two complementary case studies ...` unless the complementarity is then explained;
- repeating all contribution items in miniature.

Use `experimental settings`, `implementation details`, `data preparation`, or direct factual descriptions for ordinary experiments. Avoid `experimental protocol`, `reporting protocol`, and `fairness protocol` when no formal protocol is being defined.

For the final result sentence, distinguish:

- benchmark effectiveness;
- real-world engineering relevance;
- actual deployment.

## 9. Result Register

A strong result paragraph generally contains:

1. the principal observation;
2. a useful quantitative comparison;
3. the related engineering or methodological interpretation;
4. a qualification if the metrics or cases disagree.

Prefer:

- `The proposed method achieves the highest macro-F1 among the compared methods.`
- `The larger improvement for the minority conditions indicates ...`
- `This observation is consistent with ..., although ... remains difficult.`

Avoid:

- `Table X clearly shows that our method is the best.`
- `The excellent results prove the superiority and robustness of the model.`
- explaining a result by merely restating the module name.

Separate measured observation from interpretation. An ablation can support a module's contribution under the tested settings; it does not automatically identify the physical cause of a fault. When evidence is incomplete, place the missing metric, comparison, or citation in author notes instead of inventing a result sentence.

## 10. Hyphenation

Use hyphens for conventional attributive compounds when they improve clarity:

- plant-wide process;
- stage-wise representation;
- cross-stage interaction;
- real-world case study;
- class-wise result;
- data-driven method.

Do not hyphenate ordinary noun phrases:

- domain knowledge;
- process variables;
- fault diagnosis;
- production process.

When multiple compounds accumulate, rewrite the syntax rather than adding more hyphens.

## 11. Anti-AI-Writing Check

Flag paragraphs that contain several of these symptoms:

- generic claims that could describe any paper;
- excessive symmetry in sentence length or paragraph structure;
- repeated formulaic transitions;
- inflated adjectives without measurements;
- redundant summaries after every subsection;
- terminology that shifts without scientific reason;
- explanations detached from the actual process or experiment;
- conclusions that are broader than the evidence.

Repair by adding supported manuscript-specific facts, deleting filler, varying sentence function naturally, and returning the interpretation to the engineering object. These symptoms prompt contextual review; words, punctuation, and sentence length do not prove AI authorship. Do not use mechanical word bans, punctuation quotas, sentence-length quotas, or AI-detection scores as a writing target.

Also flag defensive writing:

- repeated caveats aimed at hypothetical criticism;
- apology-like or self-justifying transitions;
- mechanical `not X but Y` contrasts;
- multiple reminders of the same limitation;
- vague modality such as repeated `may`, `could`, or `is intended to` used to hide missing evidence.

Inspect `not X but Y`, `we do not claim`, `this further clarifies`, `it should be emphasized`, and their Chinese equivalents for actual information. A useful conceptual distinction may remain; a sentence that merely protects against an imagined objection should be removed. Do not replace an empty negative sentence with an equally empty positive one.

State the supported scope positively whenever possible. Put a necessary boundary where omission would change the claim: it may be essential in the Abstract or a result sentence. Describe detailed methodological limits in Methods and their consequences in Discussion. Avoid repeating the same caveat unless another statement independently needs it for accuracy. Preserve real uncertainty by naming its source.

For example, `We do not claim universal generalization` can become `The evaluation covers the specified operating conditions` when that is the supported scope. `This further clarifies the effectiveness of our framework` should become a specific measured finding or be deleted. Both changes require inspection of the actual evidence; they are not global replacements.
