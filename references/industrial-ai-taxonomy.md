# Industrial AI Paper Taxonomy And Routing

## Purpose

Use this reference before selecting a paper archetype, literature corpus, method family, or experiment plan. It prevents a common category error: treating an engineering challenge, a modeling technique, a prediction task, and an application scale as if they were interchangeable topics.

The taxonomy is multi-label. A manuscript normally receives one or more labels on every axis.

## Contents

Five independent axes; boundary rules; routing procedure; manuscript archetype selection; topic-playbook selection; worked routing record.

## 1. Five Independent Axes

### C. Engineering Challenge

| Code | Challenge | Questions that must be answered |
|---|---|---|
| C1 | Incomplete or asynchronous observation | Are values missing, irregularly timed, delayed, censored, or sampled at different fixed rates? What mechanism creates the observation pattern? |
| C2 | Scarce supervision | How many labels exist per class, stage, or condition? Are unseen classes, coarse labels, or unlabeled records involved? |
| C3 | Distribution evolution | Are operating modes discrete, continuously drifting, nonstationary, cross-site, or open-set? What information is available during adaptation? |
| C4 | Heterogeneous information | Are there multiple sources, modalities, temporal scales, or semantic levels? How are they synchronized and what physical evidence does each carry? |
| C5 | Interacting subsystem and process coupling | Do interactions, propagation paths, material/information flows, or long-range dependencies make local modeling insufficient? Which relationships are known and which must be learned? |
| C6 | Deployment constraints | Are latency, memory, energy, bandwidth, edge hardware, online updating, or operator workload part of the research question? |
| C7 | Trust, safety, and decision accountability | Are calibrated uncertainty, auditable evidence, risk control, human confirmation, or a safe abstention mechanism required? What evidence can validate that requirement? |

Do not infer the challenge from the proposed model name. Remove the model mentally and ask what remains difficult in the industrial system.

### M. Method Or Technical Strategy

| Code | Family | Typical mechanisms |
|---|---|---|
| M1 | Statistical and dynamic latent modeling | PCA/PLS variants, SFA, state-space models, Kalman filtering, dynamic residuals |
| M2 | Temporal and sequence representation | CNN, RNN/GRU, Transformer, state-space sequence models, temporal mixing |
| M3 | Relational and structured modeling | graph learning, topology constraints, causal discovery, knowledge-guided relations |
| M4 | Multiscale, time-frequency, and fusion modeling | multiscale encoders, spectral analysis, cross-attention, multimodal or multisource fusion |
| M5 | Generative modeling | GAN, VAE, diffusion, conditional synthesis, reconstruction |
| M6 | Learning and adaptation strategy | transfer, domain adaptation, continual/incremental learning, self-/semi-/weak supervision, test-time adaptation |
| M7 | Routing, foundation-model, and uncertainty mechanisms | mixture of experts, LLM-assisted semantics, fuzzy systems, probabilistic calibration |
| M8 | Efficient or intrinsically interpretable mechanisms | low rank, sparsity, distillation, pruning, compact operators, ante-hoc explanations |

Methods are responses, not the paper's engineering problem. A method label never substitutes for a challenge, task, or evidence label.

### T. Engineering Task

| Code | Task | Primary output |
|---|---|---|
| T1 | Data restoration or synthesis | repaired, reconstructed, or generated industrial records |
| T2 | Fault/anomaly detection and process monitoring | abnormality decision, alarm, monitoring statistic, or event interval |
| T3 | Fault diagnosis or condition classification | fault type, operating condition, or unknown-class decision |
| T4 | Localization, isolation, and root-cause analysis | responsible variable, unit, component, region, or propagation path |
| T5 | Soft sensing, quality, KPI, environmental, or health prediction | continuous process/product variable, efficiency/emission indicator, or health indicator |
| T6 | Forecasting and prognostics | future trajectory, remaining useful life, or degradation horizon |
| T7 | System identification and causal discovery | dynamic relation, graph, mechanism, or causal structure |
| T8 | Control, set-point optimization, scheduling, or decision support | control action, operating target, production plan, or ranked quality/energy/emission/throughput decision |
| T9 | Human-AI collaborative operation | recommendation plus operator interaction, confirmation, or intervention |

Encode the task from the final decision output, not from the loss function.

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
- **Few-shot vs. zero-shot vs. weak/self-supervision**: distinguish limited labeled examples, no labeled examples for test classes, coarse labels, and supervision generated from the data itself.
- **Nonstationary vs. multimode**: continuous drift and discrete operating regimes are different phenomena even when both occur.
- **Multisource vs. multimodal vs. cross-modal**: different acquisition sources are not automatically different modalities; cross-modal claims require explicit alignment or interaction.
- **Graph vs. causality**: a graph can encode correlation, topology, similarity, or message passing. Causal language requires causal assumptions and corresponding validation.
- **Detection vs. diagnosis vs. localization**: whether, what type, and where/why are distinct outputs and need distinct evidence.
- **Interpretability vs. root cause**: attention or variable ranking is not root-cause proof. Validate fidelity, stability, and engineering correspondence.
- **Lightweight vs. efficient**: parameter count alone does not establish latency, memory, energy, or deployability.

## 3. Routing Procedure

1. Identify the industrial object and the decision supported by the output.
2. Assign the task code from that output.
3. State the engineering challenge without naming the proposed model.
4. Assign method codes only to mechanisms that materially address that challenge.
5. Record the system scale and sample granularity.
6. Inventory evidence already available and evidence still required.
7. Select the manuscript archetype only after these axes are stable.

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
