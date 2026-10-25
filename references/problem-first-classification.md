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
| Measurement noise, sensor errors, outliers | Observation quality or a diagnostic target | Which quantity is affected, what establishes an error, and whether the change is interference or a signal to diagnose |
| Few-shot, weak supervision, limited labels | Support or annotation limitation | Quantity, granularity, reliability, class coverage and stage-specific access |
| Multimode, nonstationary, unseen conditions | Operating/distribution setting | Discrete regimes, continuous change, or a specified development-to-use shift |
| Compound faults | Coexisting-fault setting | Whether several faults coexist, how combinations are labeled and what the output represents |
| Incipient faults, weak fault signatures, early detection | Fault severity/observability or a timing objective | Separate imposed severity, measured response, fault evolution and the time of an issued decision |
| Plant-wide, multistage, multiblock | Object/scale and possible structure | Which coupling, propagation or heterogeneous relationships obstruct the decision |
| Batch processes, multiphase operation | Production organization and temporal structure | Which within-batch changes, duration differences or quality-availability limits matter for the task |
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
In problem-only mode, leave methods unselected; when the author requests
candidates, use the [problem-to-method navigation](#6-when-requested-problem-to-method-navigation).

## 2. Problem Terms And Their Boundaries

These are conditional descriptions, not newly certified mechanism/module names.
Use only the rows supported by the current study. Existing scoped evidence is
in the [published index](published-evidence.md) and
[terminology bank](engineering-application-terminology-bank.md).

| Industrial difficulty | Candidate English wording | What makes the wording precise |
|---|---|---|
| Incomplete observations | missing measurements; missing values; incomplete process data | Identify variable/time coverage and missingness mechanism; actual absent values differ from deliberately masked evaluation targets |
| Unreliable measured inputs | measurement noise; noisy process measurements; measurement bias when established | Identify the measurement and reference; a present but inaccurate value differs from a missing value, an incorrect label and a genuine process change |
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
| Subtle fault-related changes | weak fault signatures; small-amplitude fault perturbations; incipient faults in a defined/source-attributed setting | Separate perturbation size, measured response and physical development; a small learned activation is not fault severity |
| Restricted execution resources | limited computational resources; memory constraints; inference-time requirements | Name the actual hardware/resource/deadline; parameter count is not measured operational efficiency |

For a title or introductory problem sentence, prefer the particular limitation
over an umbrella label: for example, `quality prediction with limited labeled
data` when assay targets are scarce, or `fault detection from coarse-grained
segment labels` when time-point labels are absent. These are wording patterns,
not required titles, established module names or evidence of novelty. Do not add
an industrial cause, such as safety restrictions or assay cost, unless supplied
or documented. Explain an important limitation where it motivates the study;
minor dataset characteristics belong in dataset/analysis sections.

### Batch Processes, Temporal Phases And Quality Targets

Distinguish a production batch from a training minibatch, a temporal phase
within a batch from a physical production unit, and either from a training
stage. Published `stage`/`phase` usage varies; define the referent instead of
imposing a universal translation. A learned temporal partition need not match
an operating procedure's phase boundaries.

For this problem profile, establish the following before choosing a method:

- **Unit and count:** numbers of production batches, measured variables and
  time points/windows. Unfolding trajectories creates modeling samples, not
  additional independent production batches or quality assays.
- **Temporal difficulty:** changing within-batch behavior, unequal total
  durations and differing phase boundaries are distinct. Equal-length padding
  alone does not align physical progress; a normalized index is not elapsed time.
- **Target and availability:** distinguish a measured concentration trajectory,
  a final quality value and a batch quality category. Reusing a final value as
  the supervised target of earlier training windows does not create measured
  instantaneous quality values, nor make that label an available prediction input.
- **Decision point:** whole-batch assessment and prediction during an evolving
  batch have different available histories. Actual completion time may support
  retrospective alignment; an earlier issued prediction cannot silently use it.
  A genuinely known schedule is a different input. Reuse the
  [time-boundary guidance](experiment-evidence-design.md#3-split-integrity-checklist)
  when checking the actual implementation.

In the introduction, select the consequential difficulty, not all these fields.
In Results/Discussion, connect phase or duration effects to the specified target
and decision point; batch-end accuracy alone does not show earlier intervention
or improved product quality. Keep problem-only work free of prescribed alignment
algorithms, networks or new experiments.

P118 pp.1-3 distinguishes units/phases, unfolding and unequal durations. P119
pp.2-4 illustrates final-quality targets replicated across time and few training
batches; its case assumes equal durations. P09 pp.3-4,6-7 instead distinguishes
concentration regression from batch-category prediction and discusses variable
lengths and phase-boundary mismatch. These are scoped examples, not common
implementations or validation of every source claim. Chinese **多时段** and
**多阶段** both occur for temporal phases: see the bilingual titles/abstracts in
[AAS](https://www.aas.net.cn/cn/article/doi/10.3724/SP.J.1004.2010.00366)
and [CIESC Journal](https://hgxb.cip.com.cn/EN/10.11949/j.issn.0438-1157.20180570).
Neither usage licenses translating all phases as physical 工序.

### Weak Fault Signatures And Early Detection

Separate four questions when subtle faults motivate the study: what physical or
simulated perturbation was imposed; how it appears in the measured response;
whether a development trajectory is known; and when the diagnostic decision is
issued. State the amplitude's quantity, reference and units where needed. A
small imposed change can produce a different-sized closed-loop response;
small feature activations are another quantity. Low signal-to-noise ratio needs
a stated signal/noise definition, not just two percentages.

P109 pp.7-8 uses an incipient-fault subset containing step, random-variation
and valve-sticking scenarios. P110 pp.9-10 discusses weak measured signatures
and closed-loop masking in selected step/random-disturbance cases. These are
different teams using the TE benchmark, not independent field observations or
proof that all incipient faults must grow slowly. Preserve a source's defined
incipient-fault setting while describing how the current test realizes it;
a fixed small perturbation alone does not establish physical degradation.
Intermittence additionally concerns appearance/disappearance over time, not
merely small severity or a changing measurement.

For an introduction, select the actual difficulty, such as distinguishing weak
fault signatures from normal process fluctuations, then explain the verified
response. Keep implementation details and unresolved checks in their appropriate
sections or author notes. Early-after-onset intervals, low severity, shorter
post-onset detection delay and prediction before a future event are different
claims. Reuse the [existing timing rule](research-planning-and-contribution.md#representation-and-task-boundaries)
and [alarm-evidence guidance](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when);
do not demand new timing experiments for correctly scoped classification.

### Measurement Quality And Diagnostic Signals

Establish the affected quantity and its task role before using a data-quality
label. An error in an input measurement, an uncertain assay used as a regression
target, and an incorrect fault-category annotation affect different parts of the
study. A continuous target can itself be measured; describe its uncertainty at
the target, rather than treating all measurement noise as input corruption.

A statistical outlier identifies unusualness relative to a stated reference,
not its physical cause. A process disturbance can produce a valid measured
response. A biased or stuck sensor may be the fault to diagnose in one study
and an input limitation for another. Identify the role before recommending
cleaning, replacement or exclusion. Keep the acquisition-quality issue separate
from genuine process dynamics and class novelty.

For this problem profile, record only the affected input/target, the supplied
reference or known intervention, the affected variables/intervals, and the
intended decision. Unknown causes stay unknown. Artificially added noise is a
declared test condition, not evidence that the original acquisition was noiseless
or that field noise has that distribution. In paper prose, lead with the actual
difficulty and connect it to the verified response; use the existing
[robustness guidance](experiment-evidence-design.md#6-robustness-design) when
evidence design is requested, without selecting denoising or a new experiment
during problem-only classification.

P87 p.8 and P88 pp.6-7 evaluate diagnosis under specified added-noise scenarios;
P115 pp.4-5 instead uses outlier indicators as information for feature extraction.
These contexts support a role-sensitive reading, not a universal outlier-removal
rule, certification of their results, or admission of their full module names.

### Observation Availability And Counting

Use this profile when incomplete or differently timed measurements are the
industrial difficulty. The existing sampling and mask guides already distinguish
these objects; establish them here before selecting a method or experiment.

| Field | Record only what affects this problem |
|---|---|
| Native schedule | Physical quantity, time units, native schedule and expected acquisitions; distinguish regular clocks from irregular acquisition times and gaps caused by lost observations |
| Availability | Acquisition/represented time, release time and decision time; separate late reporting, unavailable measurements and physical process lag |
| Input identity and set | Physical variable IDs/units, configuration-specific membership and correspondence; distinguish an added/retired measurement from a lost expected value or merely reordered columns |
| Model grid | Which positions are acquired, held, interpolated, padded or entirely unsampled; a measured zero remains an observation |
| Extent and counting unit | Affected variables, intervals or units; numerator, denominator and whether the count concerns values, windows, events or elapsed duration |
| Provenance | Actual acquisition limitation versus deliberate masking; known causes and unknowns, without identifying a statistical missingness mechanism from the mask alone |

A blank on a common model grid need not be a failed expected acquisition.
A slower clock may schedule no measurement there. A value can also exist but
remain unavailable at the declared decision time. Later release can support a
declared delayed estimate; it does not make the value available to an earlier
issued decision. Uneven received gaps do not by themselves identify whether
the native schedule was irregular or a regular acquisition was lost.

Keep a generator parameter separate from its realized missing fraction. A
segment-start count divided by sequence length is not the fraction of missing
measurement entries: segment length, overlap, boundary clipping and affected
variables matter. State the denominator before comparing percentages, including
whether it covers expected acquisitions, all model-grid positions, only affected
variables or the entire variable set. Compute a realized fraction from the
specified mask when available; do not invent one from an incomplete description.

P73 p.3 Section III-A/Fig.1 distinguishes sampling-group observations and blank
grid positions. P24 pp.2-3 describes changing acquisition intervals, not merely
several fixed clocks. P37 p.6 Section III-B defines its segment-start ratio and
separately controls segment length; its code-level overlap/clipping behavior and
realized entry fractions are not established by that passage. These are different
observation roles, not a shared new module or a result audit.

Keep this detail in the working profile or data/settings section. In an abstract,
contribution or introductory transition, select the actual consequential
limitation and connect it to the verified response; do not list every mask and
clock field. A classification-only request does not authorize imputation, a new
predictor, a preferred learning paradigm or a new experimental plan.

### Changing Input Variables And Configurations

When instrumentation changes, establish which physical variables exist in each
configuration and which were available during model development. Equal vector
widths can conceal different variables; different column orders can preserve
the same variables. An expected measurement that was lost is another case.
Representing these situations in one array does not make their meanings equal.

P63 pp.2-3 distinguishes added, retired and missing sensor measurements in a
sequential diagnosis setting. P66 pp.3-4 instead represents heterogeneous input
subsets through a declared universe of observed variable types. These different
published contexts support an input-identity question, not one common module or
proof of arbitrary future-variable handling. Pooled known configurations and
sequentially changing inputs need their actual development/use boundaries.

For an introductory problem statement, connect the consequential difficulty to
the requirement in positive terms. For example, when these facts hold:
`Changes in instrumentation alter the variables available for diagnosis, while
occasional acquisition failures leave scheduled measurements unobserved.
Learning from these configurations therefore requires preserving variable
identity and distinguishing structural input differences from missing values.`
This is an illustrative connection, not a fixed sentence or a new method claim.
Put the detailed configuration inventory, missing-rate denominator and untested
future-variable scope in settings or author notes unless one is the central
problem. New input variables do not by themselves establish new fault classes.

<a id="operating-variation-and-class-novelty"></a>

### Operating Conditions And Cross-Condition Problems

Use `operating conditions` for the industrial circumstances being compared.
Select the modifier from the stated facts, not as a stylistic rotation:

| Wording | Appropriate meaning |
|---|---|
| under variable operating conditions; under varying operating conditions | Conditions vary; no single temporal speed or trajectory is implied |
| under different operating conditions | A comparison across specified conditions |
| under time-varying operating conditions | The study explicitly concerns variation over time |
| under unseen operating conditions | The stated development boundary excludes those conditions; specify access separately |

P10 p.1 uses `under variable operating conditions`; P81 p.1 uses both
`under time-varying operating conditions` and `under varying operating conditions`.
These are actual wording contexts, not a field-wide frequency ranking or a
requirement to import their methods. Prefer this established operating-conditions
wording here, without globally banning `operational conditions` or rewriting a
correct `operational state`. `operating varying` is not the intended modifier
order. A broad `varying conditions` can be made explicit when operating context
would otherwise be unclear. Keep meaningful state/mode/condition differences.

Treat operating variation, fault-class space and target-data access as separate
coordinates. They may coexist; none selects an algorithm by itself.

| Known fact | Wording it can support | What still needs evidence |
|---|---|---|
| Different loads, grades, recipes, sites or specified regimes | the actual operating-condition difference; unseen operating conditions if excluded from development as stated | A particular changed distribution, physical cause or temporal drift pattern |
| Ordered observations with changing statistical properties | nonstationarity or a precisely defined temporal distribution change | Abrupt/gradual/recurring behavior and which quantity changes; a performance decrease is not a drift detector |
| A fault category absent from the fitted classifier's class set appears | an unseen/unknown fault category relative to that set | A defined rejection decision, ability to identify its type, or automatic class learning |
| New combinations of known constituent faults | unseen fault combinations under the specified combination split | A genuinely new constituent fault type or support for arbitrary combinations |
| New-condition data are available during fitting, selection or adaptation | the actual information-access setting | Whether labels are used and which decisions occur before or after that access |

A product grade can be an operating setting or the prediction target; record
its role before treating it as a domain. An unseen condition can retain exactly
the known fault labels. Conversely, an unseen fault can occur under a familiar
condition. Encountering that fault is not proof that a model rejects it, names
it or learns a new class. Preserve legitimate open-set terminology when an
unknown-class task is defined, without claiming its capability before evidence.

Check temporal ordering before writing about drift speed or continuous
adaptation. Multiple operating modes and nonstationarity are not opposites:
switching or changing mode frequencies can change a pooled distribution even
when mode-conditional behavior is stable. A cross-condition split without a
declared chronology does not establish a gradual temporal trajectory. Likewise,
normal dynamic responses or individual outliers do not by themselves establish
distribution change. Do not assign equipment aging, sensor deterioration or a
changed physical mechanism merely because prediction error increased.

When using a distribution name, identify its direction and stability assumptions:

| Quantity | What it describes |
|---|---|
| `P(X)` | Distribution of the defined measured/encoded inputs |
| `P(Y)` | Target distribution; in classification, frequencies of the specified labels |
| `P(X|Y)` | Input distribution conditional on a target/class |
| `P(Y|X)` | Target relation conditional on the input, including a classification posterior |

These are related by the joint distribution, not independent checklist labels.
An altered `P(X)` with fixed `P(Y|X)` can also change `P(Y)`; a changed class
frequency does not establish a label-shift model with fixed `P(X|Y)`.
`P(X|Y)` and `P(Y|X)` are not interchangeable meanings of conditional.
For example, P30 p.2 Section II Eq.(2) uses **conditional drift** for fixed
`P(Y)` and changing `P(X|Y)`. Preserve that source convention, not a universal
definition or an assertion that every conditional distribution must change.
Use descriptive wording if the current facts do not identify the quantity.

For problem-only work, add only the fields needed here:

```text
Operating variable/regime and its role in the task:
Comparison boundary and temporal ordering, if known:
Fault-class space and any held-out combination space:
Target-data access at fitting, selection, adaptation and prediction:
Changed/stable distributions actually specified or supported:
Unresolved cause, timing or novelty claims:
```

This profile describes the problem; it is not a mandatory test plan or an
instruction to choose adaptation, rejection, continual learning or another model.
P30's process setting, P27 p.2's environmental quality setting, P50 p.2's
source-only unseen-condition setting and P51 p.1/Section II-B's unknown-fault
purpose illustrate different problem roles. Their full mechanisms, performance
and P51's previously unresolved threshold convention are not certified here.

### Resource And Decision-Time Requirements

Separate an actual capacity limit or decision deadline from a comparison
objective. Lightweight describes a design aim, edge identifies an execution
location, online concerns access/execution over time, and real-time concerns a
specified timing requirement. None establishes all the others. A method study
can legitimately compare parameter counts without inventing an edge device,
requiring a hardware trial for that narrow claim, or claiming deployment.

| Question | Facts needed for the problem description |
|---|---|
| What is limited? | The actual compute, resident memory, working memory, energy, communication or response-time requirement; distinguish a fixed capacity from a preference to reduce cost |
| Where does the requirement come from? | Device specification, operational decision interval, service requirement, measured bottleneck or author-stated study objective; unknown values stay unknown |
| Which path is constrained? | Training, updating, data generation or prediction; which modules/calls remain active and where they execute |
| What must coexist? | Concurrent requests and simultaneously resident models, activations, buffers and workspaces; separate unique live allocations from overlapping accounting |
| What is the timing boundary? | Start event, required output/consumer and deadline, including the relevant acquisition availability, preprocessing, queueing, transfer and postprocessing |
| What is established? | Analytical cost, simulated cost, measured device behavior or integrated operation; keep the actual workload/software/hardware and summary type attached |

A sampling period is not automatically the decision deadline. Network forward
time is not end-to-end response time, and throughput is not per-request latency.
Do not sum overlapping pipeline intervals or memory allocations; when they are
explicitly nonoverlapping, include all relevant components. One observed request
can show that its deadline was missed, but cannot establish a worst-case bound
over all workloads. A delayed output using inputs already available at its
declared cutoff is a timing issue, not automatically later-information leakage.

The problem may be retaining diagnostic or predictive performance within a
specified operational budget, or obtaining a better accuracy-size trade-off in
a comparative study. State the actual one. Do not force compression, offloading,
sparse routing, a fixed millisecond limit or a new experiment plan in problem-only
mode. Preserve positive measured results at their supported level.

P31 p.10 reports complexity/training-cost context; P45 pp.7-8 reports device
inference/resource comparisons; P85 p.7 Eq.(16) models several end-to-end delay
components. These are different evidence roles, not interchangeable timing
measurements or a new general mechanism admission. Source formulas and reported
gains are not reproduced as validated results here.

## 3. Training Samples, Annotation And Learning Objectives

Separate the data instances from the information used to learn. **Training and
test samples** are data instances, counted in their actual units. Their task
labels, measured targets, constructed targets and loss constraints have different
roles. The ML expression `training signal` can describe learning guidance; it is
not a synonym for a training sample or necessarily a physical sensor signal.
Prefer the concrete object when explaining an industrial study.

First describe **what task information is available**; then describe **how the
learning objective obtains its targets**. The labels below are not mutually
exclusive categories of complete systems.

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
Learning targets/constraints and joint/separate schedule, if specified:
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

## 6. When Requested: Problem-To-Method Navigation

Use this section only when the author asks for candidate methods, literature
directions or research ideas. Problem-only classification above still leaves
methods unselected. The relationships are **many-to-many**: select a small set
from the actual task, available samples/annotations and decision-time inputs,
not one fashionable model per folder.

| Established industrial condition | Candidate responses and their role | Transfer condition and useful evidence |
|---|---|---|
| Several quality quantities or related diagnostic attributes need prediction | Multitask learning with shared structure and task-specific objectives; separate predictors remain relevant alternatives. | Define each task, reference availability, units and retained output. P36/P130 illustrate different forms; shared inputs or extra heads alone do not establish useful transfer or require a mixture of experts. |
| Different variable clocks, uneven observation times or delayed measurements | Rate-aware state estimation; timestamp/mask-aware representation; documented resampling when appropriate. These can support prediction without necessarily imputing a complete grid. | Preserve native times, availability and the task output. P24/P34/P73 illustrate different interfaces; irregular-sequence methods are leads for a multi-rate process, not a reason to rename its acquisition mechanism. |
| Missing measurements or unavailable sensors | Learn from available observations directly, reconstruct selected values, or condition a generative imputer on observed entries. | Decide whether the required output is completed data or diagnosis/prediction despite missing inputs. Match missingness and information access; separately test restoration and downstream use when both are claimed. P25/P33 and CSDI below illustrate different roles. |
| Few task-labeled samples with useful task-unlabeled data | Joint supervised/auxiliary representation learning or semisupervised estimation; small-support comparison methods when their support/query arrangement fits. | Specify which samples and targets enter each objective. P17/P21/P47 are distinct routes, not interchangeable supervision labels. Coarse or unreliable labels need a response to that limitation, not just fewer examples. |
| New or changing operating conditions | Transfer and domain adaptation when target data are available; source-side generalization when they are not; sequential adaptation when permitted feedback arrives over time. | Separate condition novelty, fault-class novelty and label access. P10/P50/P64 have different access/update assumptions. Few-shot adaptation requires stated labeled support; normalization or a feature router alone does not establish continual learning. |
| Additional labeled fault categories enter a learning sequence | Class-incremental learning can update a hierarchical or shared classifier while addressing earlier class capability. | Define class identifiers, labels, historical resources and cumulative versus task-restricted prediction. P92/P131 use different forms; registering new training labels does not detect unknown faults from unlabeled measurements. A designed task sequence is not a verified production chronology. |
| Limited fault coverage or rare training classes | Representation transfer, conditional sample generation or semantic guidance can supply different kinds of support. | Generated samples are not new independent observations, and class descriptions do not identify an unknown class without a matching output mechanism. Preserve independent real evaluation. P05/P06/P35 concern different semantic/generation paths; an LLM is not automatically required. |
| Heterogeneous variable relationships across units or blocks | Process-informed partitioning and learned within/across-group interactions; compare independent and joint variable modeling where relevant. | Establish variable identities, group knowledge and the output before borrowing a channel strategy. P01/P14 ground industrial structure; DUET below is a forecasting lead, not proof that learned groups are physical stages or causal units. |
| Several sensing modalities, derived views or unequal prediction-time availability | Representation interaction/fusion, or teacher-to-student guidance when richer inputs exist only during training. | Identify actual streams and event correspondence. Equal channel/token widths do not align modalities; two views derived from the same measurements are not independent acquisitions. P38/P46 have different training/prediction interfaces. |
| A plausible benefit from visual or foundation-model representations | Convert the specified observations into a suitable representation and adapt the source model to the actual output; compare an appropriate numerical route. | Image conversion, text/semantic guidance and numerical pretrained models are alternatives, not one method. The leads below have different tasks; preserve timestamps, masks, scaling, units and the information cutoff through conversion. |
| A stated memory, latency or accuracy-size objective | Compact operators, low-rank designs, distillation or selective execution may change different costs. | Locate the actual constrained path; include conversion or external-model calls when present. P31/P45/P85 provide different cost contexts, not automatic deployment evidence. |

### Time-Series Mechanism Leads, Not Engineering Naming Authorities

These selected conference papers are **attributed mechanism references** for an
adaptation discussion, separate from the shared engineering-terminology bank.
They do not establish a general industrial module name, a preferred Chinese
translation, process-industry prevalence or success on the current task. Reuse
the industrial sources and the name-admission rule for those decisions.

| Source and inspected passage | Actual source task/interface | What an industrial adaptation must resolve |
|---|---|---|
| [ViTST, NeurIPS 2023](https://papers.neurips.cc/paper_files/paper/2023/hash/9a17c1eb808cf012065e9db47b7ca80d-Abstract-Conference.html), PDF pp.3-4, Section 3 | Timestamped per-variable observations become line-plot images for a fine-tuned classifier. | Plot interpolation is not verified recovery of missing physical values. Check time/value resolution, missingness visibility, layout and the required classification/regression output. |
| [VisionTS, ICML 2025](https://proceedings.mlr.press/v267/chen25be.html), PDF pp.3-5, Section 3 | Regular indexed histories are segmented and resized; reconstructed image regions map back to forecasts. The inspected version forecasts variables independently. | This is not ViTST's classification interface or evidence of native irregular/multi-rate handling. Define any timing adaptation, output conversion and required variable interactions; retain its actual pretraining/fitting access. |
| [CSDI, NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/cfe8504bda37b575c70ee1a8276f3486-Abstract.html), PDF pp.3-6, Sections 3.1/4/5 | Observations condition missing-value sampling; masked observed entries supply learning targets. | Distinguish imputation from class augmentation and label generation. Restrict conditioning to available observations for an issued prediction; all-window reconstruction is not automatically an online estimator. |
| [DUET, KDD 2025](https://doi.org/10.1145/3690624.3709325), PDF pp.3-4, Sections 3/4.1 | Temporal-pattern features and a learned channel-relation mask feed a forecasting predictor. | Its complete module names remain attributed. Map channels to actual variables and known blocks; do not turn a channel mask into process topology, physical-mode labels or cross-modal alignment. |

For a selected route, produce a compact rationale:

```text
Industrial difficulty and task:
Available training/test samples, annotations and decision-time inputs:
Candidate source mechanism and its original task:
What is retained, changed, and why the engineering condition requires it:
Closest industrial/team work and the substantive difference:
Comparison that could support or reject the proposed benefit:
```

Keep proposed benefits separate from findings. Borrowing a mechanism is a research
starting point, not novelty clearance or permission to repackage another paper.
Connect the verified problem to the actual adaptation and its evidence in the
Introduction, contribution and method; do not merely exchange computer-science
words for engineering ones. For portfolio comparison and author-approved next
steps, use [research ideation](../skills/engineering-research-ideation/SKILL.md).

## Wording Evidence / Reading Limits

P109/P110 support the problem usage above through selected introductions and
benchmark definitions, not full mechanism admission or reproduced results.
The original bilingual [AAS review title/abstract](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.2016.c160105)
and [CIESC Journal chemical-process title/keywords](https://hgxb.cip.com.cn/CN/abstract/abstract22988.shtml)
pair incipient fault with 微小故障. The original
[bearing-review title/abstract](https://www.jxcd.net.cn/zh/article/doi/10.16578/j.issn.1004.2539.2023.03.022/)
also uses 早期故障 in its adjacent machinery context. These wording checks
do not impose one Chinese translation, certify a physical early-life stage or
admit the sources' complete proposed modules. Publisher search records confirmed
the two English identities; direct publisher-page retrieval failed, so the
selected body reading uses the supplied published PDFs.

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

The operating profile additionally rereads P27/P30/P50/P51 in the stated
passages, not their complete methods. The original bilingual
[AAS c200984 title/abstract](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c200984?viewType=HTML)
corroborates 概念漂移 in an industrial soft-sensing context; it is not a full-body
distribution definition or admission of Chinese drift subtype/module names.
A sought Journal of Software review timed out; its search snippet does not
complete that reading or a subtype translation check.

For the operating-condition wording, P10/P81 p.1 supply the stated English
forms. The original [AAS coal-power review](https://www.aas.net.cn/article/doi/10.16383/j.aas.c200993),
bilingual title/abstract and Fig.6 caption, corroborates 工况/运行条件 language;
the original [satellite article's bilingual title/abstract](https://www.spacejournal.cn/cn/article/id/a49f9f4e-a980-489e-8eff-2f4d2685aa0b)
pairs 变工况 with variable operating conditions in an adjacent application.
The original [industrial-edge review title/abstract](https://xk.sia.cn/article/doi/10.13976/j.cnki.xk.2021.1030)
pairs 工业边缘计算 with industrial edge computing. These are limited wording
checks, not full-body method definitions, prevalence rankings or adoption of
guarantees and numerical targets from the sources.
