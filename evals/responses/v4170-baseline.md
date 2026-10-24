# Fictional Counterfactual-Use Baseline

One context answered A/B on immutable v4.1.69. Scientific, balance/decision arithmetic and prose already pass; the missing scoped definition/Chinese ledger finding is accurate. Wrappers, local links and whitespace are normalized; raw records remain private.

**A. Class, Bounds And Balance**
The balance residual below is \(a+b-4\).

| Vector | Sum | Model class | Individual bounds \([0,4]\) | Exact balance |
|---|---:|---|---|---|
| Observed \((2,2)\) | 4 | Fault | Both pass | Pass; residual 0 |
| Candidate \((1,1)\) | 2 | Normal | Both pass | Fail; residual −2 |

**No model-normal vector is feasible in this fixed context:** feasibility requires \(a+b=4\), whereas model-normality requires \(a+b\leq3\). Their intersection is empty. This establishes an incompatibility between the classifier’s normal region and the declared feasible set, not a real fault or cause.

The candidate satisfies the **model-level target-label condition**, but not physical consistency. Editing measurement inputs also does not establish an achievable control action: measurements need not be directly manipulable, and actuator-to-measurement relationships, dynamics and safety are unspecified. Under the unchanged balance and classifier, a feasible model-normal destination is impossible.

The intended use matters:
- **Model explanation:** the candidate illustrates a decision-boundary crossing in input space, outside the declared physical feasible set.
- **Training augmentation:** it can be considered a synthetic training construction, without calling it a physically normal observation. Its downstream usefulness requires appropriate real-data evaluation.
- **Process action:** it cannot substantiate the proposed physical transition under this exact balance.

This does not invalidate counterfactual methods generally. Nor does causal evidence universally require physical trials: observational causal identification can be legitimate with a specified target, justified identifying assumptions and adequate evidence. None is established by this toy calculation.

**Terminology finding:** the inspected v4.1.69 bank/index contains **no completed matched counterfactual-generation definition pair and no separate Chinese wording record for that term**. P62 records input weighting/ranking and a counterfactual objective; P94 records prototype selection before augmentation. These are not two matched generation definitions. Missing admission is a ledger limitation, not invalidity or literature absence. Conversely, a familiar label guarantees neither feasibility, controllability, causality nor augmentation benefit.

**B. Reusable Prose**
Counts use whitespace-separated words; hyphenated compounds count as one. Labels are excluded.

1. **Abstract/method chain: 41 words, 3 sentences**
During training augmentation, a generator adjusts permitted measurement inputs toward a requested diagnostic class. An unchanged diagnostic model checks target-class agreement, and retained candidates supplement real training data used to fit a downstream classifier. The trained downstream classifier diagnoses new measurements.

2. **Candidate contribution: 24 words, 1 sentence**
We evaluate how candidates retained through diagnostic-model checking affect downstream classification after class-directed training-input editing, using macro-F1 and rare-fault recall on held-out real measurements.

3. **Result/interpretation: 23 words, 1 sentence**
On held-out real data, macro-F1 improves while rare-fault recall decreases, indicating a trade-off between the aggregate classification score and sensitivity to rare faults.

**Author/Review Notes**
- **Method:** B’s interface is accepted as verified within the fiction. It does not inherit A’s balance. Joint feasibility remains unevaluated, not disproved; the prose claims neither physical correction nor generator use at inference.
- **Contribution:** this is a candidate empirical contribution, not established novelty. Routine class targeting supplies no automatic advance. Establish the substantive difference from prior augmentation and a matched comparator; isolate retention separately only if claiming its individual benefit.
- **Result:** a real manuscript needs traceable comparator/test outputs, split and selection provenance, metric definitions and class support supporting both directions. Magnitude, significance, stability or causal explanations need additional corresponding evidence. No counterfactual-generation requirement is imposed on diagnosis papers generally.

**Read Log**
Release references were read selectively as listed; targeted search matches and surrounding text were also inspected. No source papers or linked websites were opened.

- [Release SKILL.md](../../SKILL.md): entire entry, including Mission, Core Invariants and §§1–9.
- [Abstract/contributions companion](../../skills/engineering-abstract-contributions/SKILL.md): entire entry.
- [Terminology bank](../../references/engineering-application-terminology-bank.md): Scope; §0; §11 English-ledger excerpts, weighting boundary, Chinese-record introduction and closing limitations; whole-file searches for counterfactual/反事实.
- [Terminology decisions](../../references/terminology-decisions.md): Decision Procedure; Objects And Data Units; Weight Roles And Class Decisions excerpts; Structure And Operations excerpts, including observational causality and training/prediction roles.
- [Published evidence](../../references/published-evidence.md): P62/P94 rows and search context; “Weighting Roles, Fitted Predictors And Class-Level Evidence” excerpt; “Selection, Weighting And Measurement Dependencies”; “Classification Factors And Differentiation.”
- [Evidence design](../../references/experiment-evidence-design.md): §1; §7 including Knowledge And Physical-Constraint Claims; opening of §8.
- [Abstract/contribution craft](../../references/abstract-and-contribution-craft.md): §1; selected §3 examples; §§4–6.
- [Argument/prose craft](../../references/argument-and-prose-craft.md): §§4–6.
- Runtime/preset reads, not case evidence: using-superpowers (private local reference) and its Codex adaptation reference (private local reference), both entire files.

No files were edited, browsing or scientific experiments performed, external model APIs called, threads created, or account settings changed.
