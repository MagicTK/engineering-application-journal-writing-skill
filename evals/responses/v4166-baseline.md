# Fictional Generalization Baseline

One context answered A/B on immutable v4.1.65. Scientific judgments and writing already pass; the missing matched DG/Chinese record is accurately reported. Wrappers, local path/link metadata and whitespace are normalized; exact raw records remain private.

**A. Information Access**
- **Variant A:** Source-only development followed by inductive, known-class prediction under held-out operating conditions. Computing each input window’s own mean and standard deviation is a fixed, window-local transformation, not target-pool fitting. This is compatible with a domain-generalization information boundary; it does not establish successful generalization.
- **Variant B:** Source-trained weights with **unlabeled, whole-target-pool statistical adaptation before prediction**. Updating batch-normalization buffers changes the effective predictor even when network weights remain unchanged. Its access is transductive, not the strictly target-unseen prediction setting of A.
- **Neither is automatically invalid.** B can be legitimate when whole-pool access is explicitly part of the setting. Presenting it as A, or comparing the variants as though their information access were identical, would be misleading. These classifications are not independent validation of an implementation.

An unseen **operating condition** does not establish recognition of unseen **fault classes**. All four classes already have labeled source measurements here.

**“Source-free zero-shot fault diagnosis” does not fully or accurately describe these facts.** Absent target labels does not make known-class diagnosis zero-shot. “Source-free” concerns source-sample availability during a specified adaptation phase, not absence of historical source supervision. B could additionally satisfy that restriction if source samples are unavailable during adaptation; that availability restriction is not explicitly supplied.

A style-transfer reference called **“target” need not be the held-out target domain**: it may denote a desired style or donor representation drawn from source data. Its provenance and computational use decide the access setting. No particular style-transfer paper was inspected here.

**Library Evidence**
**The inspected release does not establish two matched published industrial DG definition contexts or separately verified Chinese DG wording.** This is an incomplete library-evidence record, not evidence that the terminology is invalid or absent from the literature.

The following are **reading scopes recorded by the library**, not papers freshly read in this session:

| Source IDs | Recorded Scope | Supported Distinction and Limit |
|---|---|---|
| **P50** | PDF pp.1,3–4; Eqs.(3)–(11) | Source-feature statistics and training perturbations. This does not complete a two-source DG definition record or verify generalization results. |
| **P10; P44** | P10 pp.4–6; P44 pp.2,4–6 | Target-involved domain adaptation with differing class-space/supervision details. They cannot simply be counted as two source-only DG definitions. |
| **P78; P79** | P78 p.1, pp.2–3 §III, selected pp.4–5 including Algorithm 1; P79 author version p.1, p.6 §§3.1–3.2, p.8 §§3.3–3.4, p.9 §3.4.1 | Adaptation-stage source-sample restrictions, with different updated components. These are SFDA contexts, not DG substitutes; complete implementations/results remain uncertified. |
| **P05; P06; P80** | P05 pp.3–4 §3, p.7 Algorithm 1/§4.3; P06 p.1, pp.2–3 §II-A, p.4 §IV-A; P80 p.1, pp.2–3, selected pp.4–5, p.6 §III-C | Class-semantic zero-shot settings and distinct retained predictors. They do not convert unseen operating conditions into unseen faults. |

Recorded Chinese checks include **JOS6146/TCES231335** for zero-shot wording and **JOS6467/JCST DOI 10.1007/s11390-021-1106-5** for source-free adaptation wording. Those checks concern bilingual titles/abstracts/keywords, with JOS6467 also including an introductory definition. They cannot certify Chinese DG wording. I did not reopen those online sources.

**B. Finished Prose**
Method overview:

The method learns a temporal encoder and classifier exclusively from labeled measurements under three source operating conditions covering four shared fault classes. Training combines source-statistic feature perturbations with jointly optimized representation-consistency and source-classification objectives, encouraging consistent diagnostic representations under the applied perturbations. At prediction, each window is normalized using its own mean and standard deviation before the frozen encoder extracts features and the classifier produces the diagnosis.

Candidate contribution:

A source-only training strategy combines source-statistic feature perturbations with representation consistency and source classification to learn temporal diagnostic features, while retaining only the trained encoder and classifier for prediction.

Result interpretation:

Diagnostic performance improved in one held-out condition and declined in another, revealing condition-dependent outcomes with no established pooled benefit.

**Author note:** These excerpts describe Variant A. Novelty remains unverified. The supplied evidence establishes neither unseen-fault rejection, physical causal identification, nor a guarantee. No additional validation or rerun is asserted or required by this wording.

**Actual Reading**
Preset memory was supplied in the environment; this was **not a memory-blank exercise**. I opened no memory files and did not use preset memory as evidentiary support.

I read [SKILL.md](../../SKILL.md) in full, plus selected passages of:
- [Terminology decisions](../../references/terminology-decisions.md): decision procedure, state/condition/adaptation, and label objects.
- [English terminology bank](../../references/engineering-application-terminology-bank.md) and [Chinese companion](../../references/engineering-application-terminology-bank_CN.md): admission rules and relevant checked entries.
- [Published evidence](../../references/published-evidence.md): scope, complete source index, and relevant supervision, adaptation, training-target, and perturbation notes.
- [Topic playbooks](../../references/topic-playbooks.md): domain-shift/adaptation section; [experiment guidance](../../references/experiment-evidence-design.md): split-integrity section.
- [Prose craft](../../references/argument-and-prose-craft.md): §§1–6; [contribution narratives](../../references/contribution-narratives.md): contribution calibration and prose guidance.

Other portions, [terminology/style](../../references/terminology-and-style.md), and [taxonomy](../../references/industrial-ai-taxonomy.md) were keyword-screened only. No paper PDFs or external pages were opened; no files were edited, experiments run, installations made, or work delegated.
