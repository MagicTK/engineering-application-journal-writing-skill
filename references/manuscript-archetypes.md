# Engineering-Application Manuscript Archetypes

## Purpose

Choose the evidence architecture before choosing section titles. These archetypes describe how the paper earns its engineering contribution; they are not rigid templates.

## Contents

General method with benchmark and real-world application; background-driven industrial application; engineering system/control/decision framework; selection tests; hybrid cases.

## 1. Archetype A: General Method With Benchmark And Real-World Application

Use when the transferable modeling principle is the main contribution and benchmark and production evidence are both available. Experimental control remains a property to verify, not a condition implied by the benchmark label.

### Evidence division

- **Benchmark**: comparison, class-/condition-wise behavior, ablation, sensitivity, or mechanism analysis, with control and reproducibility documented where claimed.
- **Real-world application**: process provenance, measured characteristics, information timing, selected class/condition coverage and engineering meaning. Check whether selection or balancing changes natural prevalence.

The two cases should have identifiable evidence roles rather than being treated as interchangeable tests. A benchmark may support controlled method analysis when its construction permits that interpretation; the production case may examine behavior under an actual process. A public dataset is not automatically a controlled experiment, and a production dataset does not automatically include every relevant field condition.

### Typical section logic

```text
Introduction
Problem or Motivation and Problem Formulation
Methodology
Experiments
  Experimental settings
  Benchmark process
  Real-world industrial process
  Short discussion, if needed
Conclusion
```

Related Work may be a separate section or may be integrated into the Introduction when the target journal and page budget support a tighter structure. Section titles must be calibrated from matched journal papers, not copied from this outline.

### Common failure modes

- reducing the industrial case to an unexplained second dataset, or confusing a physical process with the data collected from it;
- using the production case to repeat every benchmark analysis;
- claiming deployment from retrospective records;
- importing benchmark results produced under a different data construction;
- giving both cases equal prose even when their evidential roles differ.

## 2. Archetype B: Background-Driven Industrial Application

Use when a production process, equipment class, sensing arrangement, or operational bottleneck generates the scientific problem and method requirements.

### Evidence chain

```text
production mechanism
  -> observable evidence and acquisition chain
  -> operational difficulty
  -> modeling requirement
  -> background-informed design
  -> application evidence
  -> decision relevance and boundary
```

The industrial case is the center of the paper. A public benchmark is optional. Comparisons should represent credible alternatives for the actual engineering task, not a generic leaderboard.

### Typical section logic

```text
Introduction
Industrial Process and Problem Statement
Methodology
Experiments on the Industrial Process
Discussion
Conclusion
```

The process/problem section can remain a continuous narrative when subheadings would fragment the logic. Hardware details belong only when they determine data generation, task assumptions, timing, or evaluation.

### Common failure modes

- proposing a generic model first and attaching industrial terminology afterward;
- treating sensors as independent generic modalities without a physical evidence flow;
- overdescribing hardware unrelated to the scientific question;
- claiming generality beyond the studied process class;
- omitting information timing, label provenance, or operational split units.

## 3. Archetype C: Engineering System, Control, Or Decision Framework

Use when the main contribution is system integration, control architecture, online monitoring, optimization, scheduling, human-AI collaboration, or deployment workflow.

### Engineering chain

```text
operational objective and system boundary
  -> measurements, decisions, constraints, and timing
  -> current workflow limitation
  -> model/controller/optimizer and interfaces
  -> closed-loop or decision evaluation
  -> safety, reliability, and operational benefit
```

Define:

- controlled, optimized, scheduled, or recommended variables;
- objective, constraints, decision horizon, and update frequency;
- plant, operator, information-system, and model interfaces;
- fallback, override, and unsafe-output handling;
- whether the system is advisory, shadow-mode, HIL, pilot, or deployed.

Required evidence may include closed-loop or hardware-in-the-loop behavior, stability or feasibility analysis, timing, interface reliability, operator interaction, resource constraints, and operational objectives such as quality, energy, emissions, throughput, or maintenance cost. Do not evaluate such a paper only with offline prediction accuracy.

### Common failure modes

- using an offline predictor as proof of closed-loop improvement;
- omitting constraint violations, latency, or infeasible actions;
- claiming human-AI collaboration without studying the human decision role;
- reporting only accuracy when the engineering objective is economic or operational;
- describing a software architecture without evidence that interfaces and timing work.

## 4. Choosing Between A And B

Choose A when:

- the method is intended to transfer across process classes;
- a benchmark can isolate its behavior;
- the real process mainly provides engineering validation.

Choose B when:

- the process background is necessary to understand the task;
- sensing, operating rules, or expert knowledge shape the method;
- the real application is the primary source of novelty and evidence.

If both appear plausible, select the archetype supported by the strongest existing evidence, not by the most ambitious claim.

## 5. Contribution Design

For either archetype, contributions are contracts:

| Contribution | Must name | Must be supported by |
|---|---|---|
| Problem contribution | industrial condition and unresolved requirement | process/data evidence and literature positioning |
| Method contribution | mechanism and the challenge it addresses | formulation and the analysis, comparison or mechanism test appropriate to that claim |
| Engineering contribution | practical role or demonstrated process relevance | task-grounded evidence at the claimed level; a relevant simulation can establish mechanism relevance, not actual site deployment |
| Empirical/resource contribution | a new finding, resource or validated capability, not only more experiments | evidence specific to that contribution, with fair comparisons, splits, statistics and artifact traceability where applicable |

Avoid making every module a separate contribution. An evaluation summary may follow the contribution list without being counted as another advance. Use [contribution routes](contribution-narratives.md) to decide whether a finding or resource itself warrants a contribution item.
