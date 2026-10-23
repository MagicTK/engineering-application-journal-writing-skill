# Topic Playbooks For Data-Driven Industrial AI Papers

## Purpose

Load only the playbook matching the manuscript's actual challenge and method. These are conditional supplements to the general engineering narrative, not mandatory themes.

## Contents

Observation and sampling; scarce supervision; multimode/nonstationary operation; multisource/multimodal data; plant-wide and multistage systems; graph/knowledge/causal/fuzzy models; generation and diffusion; LLMs; efficiency and edge use; interpretability and root cause; mixture of experts; compound/open-set faults; dynamic and time-frequency representations; control and decision systems.

## 1. Incomplete, Asynchronous, Or Multi-Rate Observation

First identify whether the study concerns missing values, irregular timing, delayed measurements, or groups with different fixed sampling rates. Do not merge these definitions for convenience.

Writing priorities:

- explain the industrial acquisition mechanism before mathematical encoding;
- state what is observed, when, and at what rate or delay;
- distinguish native observations from values created by interpolation, aggregation, padding, or alignment;
- explain information loss, bias, or computational cost at the assumption level;
- keep a multi-rate paper centered on the multi-rate industrial process rather than rebranding it as generic irregular sampling.

Evidence priorities:

- rate/missingness construction and provenance;
- leakage-safe preprocessing;
- comparison under common information access;
- rate/missingness severity analysis;
- masks, timestamps, and reconstruction fidelity when they affect the task.

## 2. Scarce Labels, Few-Shot, Zero-Shot, Weak, Or Self-Supervised Learning

Writing priorities:

- define exactly which classes, conditions, samples, or label levels are unavailable;
- separate semantic transfer, representation pretraining, pseudo-labeling, and sample generation;
- state what target-domain or unseen-class information is accessible during training and tuning;
- tie the challenge to industrial annotation cost, safety, rarity, or emergence of new faults.

Evidence priorities:

- class-disjoint and time-disjoint splits where applicable;
- several label budgets or shots;
- seen/unseen and harmonic metrics;
- semantic-source and prompt sensitivity for LLM-assisted methods;
- calibration and failure cases for safety-critical classes.

## 3. Multimode, Nonstationary, Domain-Shift, Or Continual Operation

Writing priorities:

- distinguish discrete operating modes from continuous drift;
- define source/target or historical/current information access;
- explain how process changes alter the data distribution or task boundary;
- avoid treating random train/test splits as evidence for temporal adaptation.

Evidence priorities:

- chronological or mode-held-out evaluation;
- adaptation delay, forgetting, and old-mode retention;
- unseen-condition and open-set behavior;
- cross-period or cross-site validation when claimed.

## 4. Multisource, Multimodal, Or Cross-Modal Industrial Evidence

Writing priorities:

- trace each source from physical event to sensor response and sample unit;
- explain synchronization, alignment, and information timing;
- distinguish complementary evidence from duplicated inputs;
- make the fusion mechanism answer a concrete heterogeneity or reliability issue.

Evidence priorities:

- single-source and fusion comparisons; for numerical-to-image same-source views, select numerical-only, visual-only, fusion, and a simple image-model control as needed to isolate representation or pretrained-backbone claims;
- missing/corrupted modality tests;
- alignment perturbation;
- modality contribution and failure cases;
- localization or decision evidence when the application requires it.

## 5. Plant-Wide, Multistage, Multiblock, Or Production-Process Modeling

Writing priorities:

- define system boundaries, units, stages, material/information flow, and hierarchy;
- distinguish physical topology, control structure, temporal order, and learned relation;
- state the system level and output localization level;
- avoid reducing a plant-wide problem to a flat variable matrix without explanation.

Evidence priorities:

- stage/block/unit ablations;
- relationship or topology perturbation;
- batch-, campaign-, unit-, or route-level split integrity;
- process-wide versus local performance;
- computational scaling with variables, units, or graph size.

Load variable/channel terminology only when the selected mechanism actually models, groups, clusters, or routes process variables. In that case:

- introduce measured or manipulated variables and their process roles before defining one variable as one input channel;
- distinguish fixed process-informed partitioning from data-driven grouping or clustering;
- use `relationship`, `interaction`, `coupling`, `correlation`, or `feature fusion` according to the implemented operation rather than defaulting to `channel dependency`;
- keep channel-strategy terminology in the method-level computational explanation, not as the default engineering motivation for every multistage paper.

If the method does not manipulate variable-level relations, do not introduce channel-strategy language merely because the data are multivariate.

## 6. Graph, Knowledge-Guided, Causal, Or Fuzzy Modeling

Writing priorities:

- state the source of every graph, rule, membership function, or knowledge constraint;
- separate known structure, expert input, learned relation, and causal assumption;
- use `causal` only when assumptions and validation justify it;
- use fuzzy terminology for actual membership/rule mechanisms, not as a decorative synonym for uncertainty.

Evidence priorities:

- removed, randomized, or corrupted prior structure;
- learned-versus-given relation comparison;
- rule/membership sensitivity and calibration;
- structure recovery or intervention evidence for causal claims;
- expert consistency as supporting, not sole, validation.

## 7. Generative, Diffusion, Or Data-Augmentation Methods

Writing priorities:

- distinguish generation as a means from diagnosis/prediction as the engineering end;
- explain why real industrial scarcity, imbalance, or corruption requires generation;
- state conditioning information and prevent train-test contamination.

Evidence priorities:

- real-test-set downstream performance;
- diversity, coverage, fidelity, and class consistency;
- comparisons against simpler augmentation;
- synthetic-to-real ablations;
- expert or mechanism checks where meaningful.

## 8. LLM, Foundation-Model, Or Semantic-Reasoning Assistance

Writing priorities:

- specify whether the model supplies semantics, code, retrieval, reasoning, labels, or decisions;
- identify prompt, knowledge, and external-information sources;
- keep the industrial data and decision path primary;
- do not imply physical understanding from fluent text alone.

Evidence priorities:

- prompt/model/version sensitivity;
- ablation of semantic information;
- hallucination and invalid-output rate;
- privacy and data-governance boundary;
- comparison with non-LLM semantic baselines;
- human review when outputs enter operational decisions.

## 9. Lightweight, Efficient, Online, Or Edge-Oriented Methods

Writing priorities:

- define the resource constraint and target hardware before claiming efficiency;
- separate compact design from deployment evidence;
- report the accuracy-cost trade-off rather than only a smaller parameter count.

Evidence priorities:

- parameters, FLOPs/MACs where appropriate;
- measured latency, throughput, peak memory, and energy on named hardware;
- declared end-to-end timing boundaries, including preprocessing, data transfer, routing, image conversion, tokenization, and any required external-model calls; separate cold-start and steady-state costs when relevant;
- batch size and software environment;
- scaling and stability under online updates;
- comparison at similar accuracy or resource budgets.

## 10. Interpretability, Localization, Root Cause, And Trust

Writing priorities:

- define the user, decision, and explanation target;
- distinguish visualization, feature attribution, localization, diagnosis, and root cause;
- state whether the explanation is intrinsic or post hoc;
- avoid turning attention weights into causal conclusions.

Evidence priorities:

- fidelity, deletion/insertion, perturbation, or counterfactual tests;
- stability across seeds and nearby inputs;
- variable/component/region-level ground truth where available;
- engineering consistency and expert review;
- useful negative and boundary cases.

For root-cause metrics and distribution shifts introduced by explanation perturbations, use [the interpretation evidence guidance](experiment-evidence-design.md#7-interpretation-design).

## 11. Mixture Of Experts And Adaptive Routing

Writing priorities:

- identify what causes expert specialization: mode, stage, source, regime, task, or uncertainty;
- explain routing information and availability at inference time;
- distinguish adaptive decomposition from merely increasing capacity.

Evidence priorities:

- expert utilization and collapse diagnostics;
- routing ablation and random routing;
- unseen mode or regime behavior;
- load balance and cost; distinguish total parameters, per-input active parameters, resident model memory, and measured peak runtime memory;
- measured sparse-execution benefit on the stated software/hardware; sparse activation alone does not establish latency or memory savings. When efficiency is claimed, compare relevant small dense or distilled alternatives under the declared budget;
- expert specialization interpretation.

## 12. Compound, Concurrent, Hierarchical, Or Open-Set Fault States

Writing priorities:

- define whether multiple faults occur simultaneously, sequentially, hierarchically, or as an unknown class;
- distinguish composite labels from genuinely interacting fault mechanisms;
- describe label construction, temporal overlap, and ambiguity explicitly;
- avoid claiming root cause or fault interaction from a multi-label classifier alone.

Evidence priorities:

- single-fault, compound-fault, and normal-condition separation;
- held-out combinations or unknown-fault evaluation when claimed;
- multi-label metrics, class-wise recall, false alarm, and detection delay as appropriate;
- overlap-severity and fault-order analysis;
- mechanism or expert checks for claimed fault interactions.

## 13. Dynamic, Multiscale, Slow-Feature, Or Time-Frequency Representation

Writing priorities:

- derive relevant time scales, dynamics, or frequency bands from process behavior or sensing physics;
- distinguish slow operating evolution, transient response, periodic structure, and measurement noise;
- explain why a representation is needed before naming its encoder or transform;
- avoid generic `local/global feature` language when no engineering scale is defined.

Evidence priorities:

- static-versus-dynamic and time-versus-frequency comparisons;
- scale, lag, window, or retained-band sensitivity grounded in the process;
- controlled removal or replacement of each representation branch;
- transient, steady-state, and mode-specific analysis when relevant;
- efficiency analysis if the representation is claimed to be lightweight.

## 14. Control, Optimization, Scheduling, And Human-AI Decision

Writing priorities:

- define the controlled/optimized variables, constraints, objective, horizon, and decision frequency;
- connect prediction error to operational consequence;
- distinguish advisory, shadow-mode, and closed-loop use;
- include safety, feasibility, and operator authority.

Evidence priorities:

- closed-loop, simulation, HIL, or prospective decision evaluation as appropriate;
- constraint violations, stability, economic/quality objectives, and robustness;
- latency and update frequency;
- human acceptance, override, or decision-quality measures for collaborative systems.
