# Problem-First Industrial Classification

[中文](problem-first-classification_CN.md)

Use this reference when the request is to organize industrial problems, describe
data/annotation limitations, or prepare later literature routing. It complements
the [five-axis taxonomy](industrial-ai-taxonomy.md), not a new model catalogue.
In **problem-only** mode, methods, experiments and manuscript archetypes stay
unselected unless the user requests them. Unknown tasks remain unknown.

## 1. Start With The Industrial Difficulty

Folder labels are search leads, not scientific definitions. Read the identified
papers' problem statements to establish the affected object, difficulty and
decision. A folder may mix several roles; keep cross-tags instead of forcing a
single hierarchy. Do not rename the user's library or treat its presence as
evidence that every topic has been reviewed.

| Search lead | What it identifies first | Problem to establish, not assume |
|---|---|---|
| Missing data, multi-rate, irregular sampling | Observation limitation | Which measurement is absent or unavailable when needed, and why |
| Few-shot, weak supervision, limited labels | Support or annotation limitation | Quantity, granularity, reliability, class coverage and stage-specific access |
| Multimode, nonstationary, unseen conditions | Operating/distribution setting | Discrete regimes, continuous change, or a specified development-to-use shift |
| Compound faults | Coexisting-fault setting | Whether several faults coexist, how combinations are labeled and what the output represents |
| Plant-wide, multistage, multiblock | Object/scale and possible structure | Which coupling, propagation or heterogeneous relationships obstruct the decision |
| Multisource, multimodal | Input provenance/heterogeneity | Domain differences, acquired-stream relations or incompatible representations |
| Anomaly localization, root-cause analysis | Intended task/output | Required location or explanation and what evidence can establish it |
| Attention, graph, diffusion, fuzzy modeling, MoE, LLM, slow feature analysis, transfer learning | Candidate technical families | Read the application problem; no one-to-one problem follows from a method name |
| Lightweight/efficient models | Technical objective/response | Measured or specified resource, deadline or hardware constraint |
| XAI/interpretability | Method/evaluation theme and possible decision requirement | Who needs an explanation, of which decision, for what action or audit |
| Journal names; review/survey | Publication or document type | Literature filters, not an industrial challenge or method |

Compound-fault diagnosis can use multi-label outputs, but combinations may also
be modeled as classes or other declared outputs. Multi-label learning is not the
definition of compound faults and does not follow from a title. Likewise, MoE
is not restricted to LLMs; a source's expert/router design needs its own account.

## 2. Problem Terms And Their Boundaries

These are conditional descriptions, not newly certified mechanism/module names.
Use only the rows supported by the current study. Existing scoped evidence is
in the [published index](published-evidence.md) and
[terminology bank](engineering-application-terminology-bank.md).

| Industrial difficulty | Candidate English wording | What makes the wording precise |
|---|---|---|
| Incomplete observations | missing measurements; missing values; incomplete process data | Identify variable/time coverage and missingness mechanism; actual absent values differ from deliberately masked evaluation targets |
| Different acquisition rates | multi-rate sampling; multi-rate process measurements | Different variable/group sampling clocks; do not infer irregular intervals within each clock |
| Uneven timestamps | irregularly sampled measurements | Variable time gaps, not merely several different fixed rates |
| Timing mismatch or late availability | asynchronous measurements; reporting delay; delayed quality measurements | Separate acquisition time, report-availability time, alignment and physical process lag |
| Few measured targets/annotations | limited labeled data; label scarcity; sparsely labeled process data | Specify the labeled unit, target and count; abundant unlabeled measurements are not scarce data overall |
| Coarse or uncertain annotation | coarse-grained labels; label ambiguity; noisy labels/targets | State label granularity and label reliability separately; candidate alternatives differ from simultaneous true labels |
| Unequal class support | class imbalance; long-tailed class distribution when established | Counts and affected classes; not a synonym for few-shot learning or an automatic headline |
| Changing operation/distribution | multiple operating modes; nonstationary operation; distribution shift | Determine discrete versus continuous variation and the development/use boundary; changing inputs alone do not prove concept drift in the input-to-target relation |
| Coupled process behavior | process coupling; interacting production stages; cross-stage dependencies | Identify physical/known versus learned relations; plant-wide scope alone is not a demonstrated coupling problem |
| Different information sources | heterogeneous process data; heterogeneous sensing; cross-domain distribution differences | Establish source/domain/stream/modality/view roles before naming the difficulty |
| Simultaneous faults | compound faults; simultaneous faults | State constituent faults, combination coverage and output definition, without presupposing a particular loss |
| Restricted execution resources | limited computational resources; memory constraints; inference-time requirements | Name the actual hardware/resource/deadline; parameter count is not measured operational efficiency |

For a title or introductory problem sentence, prefer the particular limitation
over an umbrella label: for example, `quality prediction with limited labeled
data` when assay targets are scarce, or `fault detection from coarse-grained
segment labels` when time-point labels are absent. These are wording patterns,
not required titles, established module names or evidence of novelty. Do not add
an industrial cause, such as safety restrictions or assay cost, unless supplied
or documented. Explain an important limitation where it motivates the study;
minor dataset characteristics belong in dataset/analysis sections.

## 3. Supervision Information And Training Signals

Record both axes. First describe **what task information is available**; then
describe **how the training objective obtains its targets**. The labels below
are not mutually exclusive categories of complete systems.

| Term | What must be stated | Do not infer |
|---|---|---|
| Supervised learning | The task targets used for fitting, their unit and provenance; classification labels or continuous regression targets | Abundant, correct labels, no auxiliary losses, or generalization to unseen classes |
| Semi-supervised / semisupervised learning | Task-labeled and task-unlabeled examples both contribute to learning; identify affected outputs and access stages | Merely storing unused unlabeled data is sufficient; all papers require pseudo-labeling or separate pretraining |
| Weakly supervised learning | Which supervision is incomplete, coarse, ambiguous or inaccurate; state the convention used | A fixed label fraction, no supervision at all, or universal exclusion of semi-supervised learning |
| Unsupervised learning | Which fitting stage lacks externally supplied task targets; record label use for selection, thresholding, cluster interpretation and evaluation separately | No human knowledge anywhere, known cluster identities, or guaranteed anomaly semantics |
| Self-supervised learning | Targets derived from data/transformations and the fitted objective; joint or separate training; retained prediction path | An umbrella for weak/unsupervised learning, compulsory contrastive learning, or an entirely annotation-free pipeline |

Under the broad taxonomy in [Zhou's foundational review](https://doi.org/10.1093/nsr/nwx106),
incomplete supervision includes semi-supervised learning. Other communities use
weak supervision more narrowly for coarse/inexact or unreliable labels. State
the actual annotation arrangement rather than insisting on one universal tree.

Industrial checks support these distinctions: P17 p.2 Section II defines sparse
continuous assay targets; P21 p.3 Section III-A trains labeled classification and
self-generated temporal learning jointly; P26 p.3 Section III constructs a
sampling-transformation target alongside labeled classification. P22 p.3
Section III-A explicitly separates segment labels from point-level outputs.
Thus, labeling every segment does not supply every time point's target. P19 p.6
Section III-D defines a label-free clustering objective; this passage alone does
not settle label use for tuning or cluster interpretation. P20 p.3 documents
manual dataset annotation, while pp.4,6 describe self-supervised training roles;
do not conclude that its entire development/evaluation path never uses labels.
These are selected passage checks, not complete implementations or result audits.

Normal-only modeling needs its own account: how was normality established,
which targets enter fitting, and what sets the alarm threshold? Preserve an
attributed community term such as unsupervised detection, while explicitly
recording curation/selection information relevant to the claim. Reconstruction
loss alone cannot classify the entire pipeline's supervision.

## 4. A Small Annotation Profile

For the current task, record only known fields:

```text
Target/output and labeled unit:
Label quantity and coverage (classes, conditions, time periods, sites):
Label granularity (point/window/event/product/batch or other actual unit):
Label reliability and how targets were obtained:
Task-unlabeled measurements available and actually used:
Constructed training signals and joint/separate schedule, if specified:
Label/data access at fitting, selection, adaptation and final evaluation:
Unknowns that affect terminology:
```

No universal label ratio or sample cutoff defines few-shot or semi-supervised
learning. A zero-labeled target domain, a novel fault class with known semantics,
and zero labels throughout development are different statements. State which one
holds; do not collapse them into zero-shot. An observed batch may contain many
correlated windows; a synthetic view is not another acquired labeled batch.

## 5. Minimal Problem-Only Deliverable

Return the industrial difficulty, conditional EN/CN wording, task/scale if known,
annotation/observation profile and a short list of unresolved facts. Write
`Method: not selected` and `Evidence: not supplied` where appropriate. Do not
select an archetype, propose networks, map a problem to a preferred algorithm,
design new experiments or launch an idea-generation workflow in this mode.
Later, when requested, add candidate responses and their matched evidence
without turning co-occurrence in a folder into causation or a unique solution.

## Wording Evidence / Reading Limits

English learning-setting passages above reuse indexed P17/P19/P20/P21/P22/P26;
they add no new engineering-study IDs or full module-name admissions. The
foundational NSR review's Introduction/Incomplete Supervision sections clarify
terminological overlap, not process-industry prevalence. Original bilingual
[AAS semi-supervised abstract](https://www.aas.net.cn/cn/article/doi/10.3724/SP.J.1004.2013.01871)
supports 半监督学习; the original
[AAS contrastive-learning abstract/keywords](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220421)
supports 自监督学习 as distinct from 对比学习. The original
[Chinese Journal of Image and Graphics abstract](https://www.cjig.cn/zh/article/doi/10.11834/jig.220854/)
supports 弱监督 and coarse-label usage in a vision setting, not a second
industrial mechanism definition. A sought AAS unsupervised-wording page failed
to load; it is not completed translation evidence. Existing wording is not
silently invalidated by that access failure. No new compound Chinese name is
promoted by this routing guide.
