# Industrial AI Paper Taxonomy And Routing

## Purpose

Use this reference before selecting a paper archetype, literature corpus, method family, or experiment plan. It prevents a common category error: treating an engineering challenge, a modeling technique, a prediction task, and an application scale as if they were interchangeable topics.

The taxonomy is multi-label. An established manuscript can receive labels on
every axis; an early problem inventory need not have a selected method, output
or evidence plan. See [problem-first classification](problem-first-classification.md)
for problem-only work and supervision-information versus training-signal profiles.

## Contents

Five independent axes; boundary rules; routing procedure; manuscript archetype selection; topic-playbook selection; worked routing record.

## 1. Five Independent Axes

### C. Engineering Challenge

| Code | Challenge | Questions that must be answered |
|---|---|---|
| C1 | Observation availability and measurement quality | Are values missing, irregularly timed, delayed, censored, sampled at different fixed rates, or affected by established measurement errors? Separate availability from value reliability, and identify whether a sensor fault is the target or an input limitation; use the [measurement-role profile](problem-first-classification.md#measurement-quality-and-diagnostic-signals). |
| C2 | Limited or imperfect supervision | What is limited: label count, granularity, reliability or knowledge of the true label? Distinguish missing annotations, candidate labels, incorrect labels and simultaneous fault labels. |
| C3 | Operating conditions and distribution change | Which operating conditions differ, or vary over time? Are discrete modes defined, and is a distribution change established? What source/target information is available during development and prediction, with or without adaptation? Does the class space also change? |
| C4 | Heterogeneous information | Do acquisition streams, derived representations, temporal scales or semantic levels carry different information? Which inputs require pairing/synchronization, and what physical or derived evidence does each carry? |
| C5 | Interacting subsystem and process coupling | Do interactions, propagation paths, material/information flows, or long-range dependencies make local modeling insufficient? Which relationships are known and which must be learned? |
| C6 | Deployment constraints | Are latency, memory, energy, bandwidth, edge hardware, online updating, or operator workload part of the research question? |
| C7 | Trust, safety, and decision accountability | Are calibrated uncertainty, auditable evidence, risk control, human confirmation, or a safe abstention mechanism required? What evidence can validate that requirement? |
| C8 | Weak or obscured diagnostic signatures | Which perturbation, measured response and interference make discrimination difficult? Separate severity, physical evolution and required warning time using the [problem profile](problem-first-classification.md#weak-fault-signatures-and-early-detection), without selecting a method. |

Do not infer the challenge from the proposed model name. Remove the model mentally and ask what remains difficult in the industrial system.

### M. Method Or Technical Strategy

| Code | Family | Typical mechanisms |
|---|---|---|
| M1 | Statistical and dynamic latent modeling | PCA/PLS variants, SFA, state-space models, Kalman filtering, dynamic residuals |
| M2 | Temporal and sequence representation | CNN, RNN/GRU, Transformer, state-space sequence models, temporal mixing |
| M3 | Relational and structured modeling | graph learning, topology constraints, causal discovery, knowledge-guided relations |
| M4 | Multiscale, time-frequency, and fusion modeling | multiscale encoders, spectral analysis, cross-attention, multimodal or multisource fusion |
| M5 | Reconstruction-based and generative modeling | autoencoders, VAE, GAN, diffusion, conditional synthesis; distinguish representation training from sample generation |
| M6 | Learning and adaptation strategy | transfer, domain adaptation, domain generalization, continual/incremental learning, self-/semi-/weak supervision, test-time adaptation |
| M7 | Routing, foundation-model, and uncertainty mechanisms | mixture of experts, LLM-assisted semantics, fuzzy systems, probabilistic calibration |
| M8 | Efficient or intrinsically interpretable mechanisms | low rank, sparsity, distillation, pruning, compact operators, ante-hoc explanations |

Methods are responses, not the paper's engineering problem. A method label never substitutes for a challenge, task, or evidence label.

This table routes questions; it does not certify every label or modified module
name as an established industrial term. Before recommending a name, apply the
[multi-source terminology admission check](engineering-application-terminology-bank.md#0-admit-names-not-search-counts).
Keep broad descriptive strategies, source-specific component names and general
mechanism families distinct. An uncompleted evidence record does not require
renaming the implemented method.

### T. Engineering Task

| Code | Task | Primary output |
|---|---|---|
| T1 | Data restoration or synthesis | repaired, reconstructed, or generated industrial data or samples |
| T2 | Fault/anomaly detection and process monitoring | abnormality decision, alarm, monitoring statistic, or event interval |
| T3 | Fault diagnosis, condition or quality-category classification | fault type, operating condition, product/quality category, or unknown-class decision |
| T4 | Localization, isolation, and root-cause analysis | located variable/unit/region, isolated fault set, or a supported causal explanation/path; state which is actually produced |
| T5 | Soft sensing, quality, KPI, environmental, or health prediction | continuous process/product variable, efficiency/emission indicator, or health indicator |
| T6 | Forecasting and prognostics | future trajectory, remaining useful life, or degradation horizon |
| T7 | System identification and causal discovery | dynamic relation, graph, mechanism, or causal structure |
| T8 | Control, set-point optimization, scheduling, or decision support | control action, operating target, production plan, or ranked quality/energy/emission/throughput decision |
| T9 | Human-AI collaborative operation | recommendation plus operator interaction, confirmation, or intervention |

Encode the task from the final decision output, not from the loss function.

These are routing codes, not a demand to rename a published task. A quality-category predictor (P09) remains classification even when its features are learned through regression; estimating a continuous quality quantity fits T5. A soft sensor that forecasts a future quantity may use T5 and T6 together. Record the estimated quantity, target time and information available when the estimate is issued. A located region or ranked variable alone does not establish a responsible physical cause.

For T6, use the [forecasting/life-target route](topic-playbooks.md#forecasting-and-life-targets)
to distinguish predicted process trajectories from remaining life and current
health assessment. A downstream alarm requires its own stated decision rule;
the word prognosis does not establish one universal target or an RUL estimator.

A reconstruction objective does not make data synthesis the engineering task.
An autoencoder may supply features to a classifier or a monitoring statistic;
a VAE may support quality prediction without generating augmentation samples.
Keep those final outputs under T2, T3 or T5 as appropriate. Select generation
quality and synthetic-to-real evidence only when generated data are an actual
output or training input; see the [role-specific playbook](topic-playbooks.md#7-reconstruction-based-generative-diffusion-or-data-augmentation-methods).

An adversarially trained feature generator may support performance-grade classification without synthesizing acquired-data samples (P70). Likewise, an adversarial sample generator may be training support for T3 rather than the T1 final output (P72). Record the discriminator's target and the retained prediction path; the word `generator` or `GAN` does not determine the task code.

### O. Engineering Object And Scale

Record both the studied-system level and the output level.

| Code | Scale |
|---|---|
| O1 | variable, channel, pixel, or local region |
| O2 | sensor, actuator, component, or subsystem |
| O3 | equipment or machine |
| O4 | unit operation, production stage, batch, or process section |
| O5 | multistage, multiblock, plant-wide, or full production process |
| O6 | factory, fleet, supply-production system, or enterprise decision layer |

Also record the sample granularity: time point, window, sequence, event, product, batch, campaign, or production period.

### E. Evidence Profile

Evidence codes are non-ordinal. Combine the types actually available; one code does not automatically supersede another.

| Code | Evidence type |
|---|---|
| EA | theorem, property, or analytical argument |
| ES | numerical or mechanism-based simulation |
| EB | public or controlled benchmark |
| EL | laboratory rig, pilot process, or hardware-in-the-loop test |
| ER | retrospective real industrial records |
| EP | prospective or shadow-mode evaluation without automatic actuation |
| EO | online or deployed operation with the actual decision path |
| EX | external validation across sites, assets, lines, or institutions |
| EV | measured operational value such as quality, energy, emissions, throughput, maintenance, safety, or decision benefit |

Record operating status in the internal evidence ledger as `retrospective/offline`, `prospective/shadow`, `advisory`, or `closed-loop`. Real industrial records support engineering relevance, but do not prove online operation, external generalization, or operational benefit. The manuscript need not repeatedly label retrospective production data as `offline` unless that distinction affects the method or claim. Likewise, a multisite retrospective study does not prove deployment, and an online study at one site does not prove multisite generalization.

## 2. Boundary Rules

- **Missing vs. irregular vs. multi-rate**: missing means a required value is absent; irregular means observation intervals vary; multi-rate means variables or groups follow different sampling rates, often regularly within each group. They may coexist.
- **Supervision quantity vs. meaning**: few-shot and zero-shot concern specified labeled support; weak supervision may involve coarse, ambiguous or inaccurate annotations; self-supervision constructs a learning target from data. A multi-hot target for simultaneous faults is not an ambiguous candidate set. Define the particular arrangement rather than routing by a title alone; see the [supervision playbook](topic-playbooks.md#2-scarce-labels-few-shot-zero-shot-weak-or-self-supervised-learning).
- **Operating regimes, temporal change and class novelty**: mode membership and distribution change are different coordinates and can coexist. Do not restrict nonstationarity to continuous drift or infer unknown fault types from new operating conditions. Use the [operating profile](problem-first-classification.md#operating-conditions-and-cross-condition-problems) to separate temporal ordering, label/combination spaces and target-data access before selecting a method.
- **Multisource vs. multimodal vs. cross-modal**: first identify operating-domain datasets, acquired streams and derived views; different acquisition sources are not automatically different modalities. Cross-modal claims require the actual alignment, interaction or training-to-prediction relation, not synchronization of unrelated domain events.
- **Graph vs. causality**: a graph can encode correlation, topology, similarity, or message passing. Causal language requires causal assumptions and corresponding validation.
- **Detection, diagnosis, localization and root cause**: an abnormality decision, a fault identity, a location and a causal explanation are different outputs. Published names vary; route from the actual output and evidence rather than treating every location as a cause.
- **Interpretability vs. root cause**: attention or variable ranking is not root-cause proof. Validate fidelity, stability, and engineering correspondence.
- **Lightweight vs. efficient**: parameter count alone does not establish latency, memory, energy, or deployability.

For problem-only resource classification, use the [capacity/deadline profile](problem-first-classification.md#resource-and-decision-time-requirements). An actual deployment constraint and a comparative compactness objective are both legitimate, but are not the same problem or permission to choose a method.

## 3. Routing Procedure

In **problem-only** mode, return known industrial difficulties, wording,
observation/annotation conditions and unresolved facts; do not select an archetype,
generate methods or impose an experiment plan. Use `Method: not selected` and
`Evidence: not supplied` when appropriate. The full routing sequence below is
for a selected study, not a requirement to fill unknown axes in a library audit.

**Source-role routing:** use the distribution/access questions under C3/M6
when source denotes operating domains, and C4/M4 when heterogeneous acquired or
derived inputs motivate representation/fusion. Use both where both matter;
source count alone does not establish a shift or select a method. Follow the
[source-role account](terminology-decisions.md#source-roles-and-representation-provenance)
before prescribing synchronization, modality-removal tests or a fusion narrative.

1. Identify the industrial object and the decision supported by the output.
2. Assign the task code from that output.
3. State the engineering challenge without naming the proposed model.
4. Assign method codes only to mechanisms that materially address that challenge.
5. Record the system scale and sample granularity.
6. Inventory evidence already available and evidence still required.
7. Select the manuscript archetype only after these axes are stable.

When the author requests candidate mechanisms, use the conditional
[problem-to-method navigation](problem-first-classification.md#6-when-requested-problem-to-method-navigation).
It connects several possible responses to their actual data/access conditions;
conference mechanisms remain attributed leads, not engineering-name authorities.

Use the following compact record:

```text
Object/scale:
Task/output:
Engineering challenge(s):
Method strategy/strategies:
Evidence available:
Evidence required:
Operational boundary:
```

## 4. Generic Narrative Generator

Build the paper from the selected labels without hard-coding a topic:

```text
industrial object and decision
  -> observable engineering challenge
  -> mismatch in existing assumptions
  -> modeling requirements
  -> method mechanisms
  -> claim-specific evidence
  -> engineering interpretation and boundary
```

For example, `C1 + M4 + T3 + O4 + EB/ER` does not automatically mean a multi-rate paper. The exact observation mechanism and engineering setting determine whether the manuscript concerns missing measurements, asynchronous records, multi-rate groups, or another form of incomplete observation.
