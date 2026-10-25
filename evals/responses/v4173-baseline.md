# Fictional Source-Role Baseline

One context answered A/B on immutable v72. Counts, source-role interpretation and prose already pass; it recognizes the existing conditional guidance. This is a routing clarification, not a manufactured baseline repair. Wrappers, local links and whitespace are normalized; raw records remain private.

**A. Source Roles**
**Case D:** “Source” denotes an operating-condition domain/dataset, not an additional sensor modality. Across the two labeled datasets:
- **200 acquired parent windows:** 100 per condition, measuring the same six process variables.
- **400 deterministic model views:** 200 sequence views and 200 spectrogram views.
- **200 parent-level annotation assignments:** copying labels produces 400 label-bearing views, not 400 annotations.

The condition datasets contain unrelated events and require no cross-condition event synchronization. Each parent’s two representations are associated views, not independently acquired evidence. They remain valid model representations. Any additional target training pool has an unspecified size and is outside these counts.

**Case P:** “Source” denotes the separately acquired video and current modalities. There are **100 paired production cases and 200 stream records:** 100 video records plus 100 current records. Annotation counts are unspecified. Separate acquisition does not certify statistical independence.

**Applicable checks:** Preserve parent/view associations in D and case/stream associations in P across splits; assess overlap and run-level dependence without assuming independence. For P, verify temporal correspondence and information availability when joint use requires them. Neither “multisource” nor cross-modal training automatically mandates missing-modality tests or every training modality at prediction; follow the actual deployed interface.

**Adaptation and evaluation:** D may use permitted unlabeled target training measurements while withholding held-out labels from fitting and selection. That is target-access domain adaptation, not source-only domain generalization or source-free adaptation with source measurements unavailable during adaptation. P supplies no adaptation setting. Match evaluation access to the declared setting; alignment alone establishes no diagnostic gain.

**Fair reading of the Skill:** Taxonomy §2 already distinguishes acquisition sources from modalities; Topic §3 separates training alignment from prediction combination; Topic §4 distinguishes derived views from independently acquired modalities. Its broad evidence-priority bullets must be applied conditionally, not converted into automatic synchronization or missing-modality requirements.

**B. Reusable Prose**
Counts use whitespace-separated words; hyphenated forms count as one word. Counts exclude headings.

**1. Abstract/Method: 54 words, 2 sentences**
To address operating-condition variation in fault diagnosis, two branches, each comprising an encoder and classifier, are trained on labeled datasets from their respective conditions, with feature alignment guided by a permitted unlabeled target training pool. At prediction, both frozen branches process the same single target window, and their class-probability vectors are averaged for diagnosis.

**2. Candidate Contribution: 28 words, 1 sentence**
The design addresses operating-condition variation through condition-specific supervised branches whose features are aligned using unlabeled target training data and whose class probabilities are averaged for each target window.

**3. Case D Data/Evidence: 33 words, 1 sentence**
Each condition supplies 100 acquired windows measuring the same six process variables: two conditions yield 200 parent windows, 200 parent-level label assignments and 400 deterministic views, one sequence and one spectrogram per parent.

**Author/Review Notes**
- The verified B interface aligns **features during training** and averages **class probabilities at prediction**, \( \bar{\mathbf p}(x)=[\mathbf p_1(x)+\mathbf p_2(x)]/2 \). It does not average logits or fuse feature vectors. Runtime uses one target window, two frozen branches, no source samples, no second sensor modality and no parameter updates.
- The alignment criterion, architecture details, model-selection procedure and final class-selection/tie rule remain unspecified. Document them without held-out-label selection. Shared classes are supplied for B, not imposed on adaptation generally.
- Block 2 is a candidate design statement, not established novelty. Routine adaptation and averaging alone establish no advance. These fixtures supply no gains, industrial-performance evidence, cross-site generalization or physical causality, and admit neither a new general mechanism nor a Chinese translation. Their branches are not a prescription for other papers.

**Sections Read**
The following records substantive text reads; additional heading/keyword scans were navigation only.
- [Main SKILL.md](../../SKILL.md): Mission; Core Invariants; §§1–9, including all subsections.
- [industrial-ai-taxonomy.md](../../references/industrial-ai-taxonomy.md): Purpose; §§1–4, including all five axes and Boundary Rules.
- [topic-playbooks.md](../../references/topic-playbooks.md): §3 “Multimode, Nonstationary, Domain-Shift, Or Continual Operation”; §4 “Multisource, Multimodal, Or Cross-Modal Industrial Evidence.”
- [engineering-abstract-contributions/SKILL.md](../../skills/engineering-abstract-contributions/SKILL.md): Start From The Actual Study; Revise Within The Author's Scope; Return A Decision-Ready Proposal; Acceptance Check.
- [abstract-and-contribution-craft.md](../../references/abstract-and-contribution-craft.md): opening guidance; §§1, 2, 4, 5 and 6. Section 3 examples were not read.
- [argument-and-prose-craft.md](../../references/argument-and-prose-craft.md): Purpose; §§1–8, including §7 examples A–G; Adaptation Note.
- [experiment-evidence-design.md](../../references/experiment-evidence-design.md): §3 “Split Integrity Checklist”; §4 “Comparison Fairness Record,” excerpt at lines 103–127.
- [engineering-application-terminology-bank.md](../../references/engineering-application-terminology-bank.md): §0 “Admit Names, Not Search Counts.”

Read-only fictional-fixture review completed. No files changed, browsing, scientific experiments, external model API calls, thread creation or account-setting changes.
