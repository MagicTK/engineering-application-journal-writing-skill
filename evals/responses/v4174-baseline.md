# Fictional Evidence-Role Baseline

One context answered A/B on immutable v73. Science, arithmetic and prose already pass; the respondent identifies narrower wording while recognizing the existing analytical/resource and coupled-control guidance. Only wrappers, local link/path metadata and whitespace are normalized. Exact dispatch/raw remain private.

**A. Exact Result**
Define the signed equality residual as \(r(y)=By-1\). Since \(BB^\top=2\) and \(Bz-1=1\),
\[
c(z)=(2,0)-\tfrac12(1,1)=(1.5,-0.5),\qquad r(c(z))=0.
\]
After ReLU, the output is \((1.5,0)\), giving residual \(1.5-1=\boxed{0.5}\).

For any full-row-rank \(B\), the general construction with target \(b\) satisfies
\[
Bc(z)-b=(Bz-b)-BB^\top(BB^\top)^{-1}(Bz-b)=0.
\]
Thus it enforces the declared equalities in exact arithmetic and is the Euclidean orthogonal projection onto their affine solution set. This does **not** establish nonnegativity, improved industrial predictive performance, calibration, safety, unencoded physical constraints, or finite-precision correctness. Later nonlinear processing need not preserve feasibility. Numerical implementation requires separate checks of the actual computation, conditioning and tolerances.

| Item | Appropriate Evidence Role |
|---|---|
| (i) Exact equality at the specified corrected output | Direct exact calculation; the general algebraic argument supports all inputs under its assumptions. No empirical deletion row is needed to establish this identity. |
| (ii) Improved industrial predictive performance | Relevant held-out industrial evaluation, valid references/targets, fair comparisons and uncertainty assessment where stochastic variation matters. Equality satisfaction is not that evidence. |
| (iii) Genuinely new annotated benchmark | Resource validation: provenance, annotation definitions and validity, version/scope, and documented access conditions. Accept the stipulated novelty, but leave annotation validity and access unverified; restricted access is not automatically invalid. |
| (iv) Run/configuration or metric reproduction | Implementation/reproducibility evidence: traceable configuration, data version, run artifacts and metric definitions/recomputation. This establishes the checked consistency, not independent novelty or industrial effectiveness. |

**Controls And Wording**
Neither every meaningful control needs its own novelty contribution nor every contribution its own empirical model-deletion row. Controls may support a design claim, check an implementation, reproduce a metric, or examine a joint interaction. A coupled intervention changing several objects supports the **joint comparison**; unique component attribution requires additional justification.

The existing guidance already recognizes analytical evidence, meaningful replacements, coupled tests, resource contributions and justified exact guarantees. In particular, [“Knowledge And Physical-Constraint Claims”](../../references/experiment-evidence-design.md) explicitly distinguishes mathematical guarantees from empirical residual checks.

The local issue is **scope ambiguity/over-narrow wording**, not absence of those rules: the reference’s [“Map every ablation to a contribution”](../../references/experiment-evidence-design.md) does not clearly accommodate validity-only controls. The English [§15 gate](../../skills/engineering-experiment-evidence-design/SKILL.md) and Chinese §十六 leave “test/测试” unspecified. Meanwhile, English §6’s “may require analysis as well as experiments” is conditional, so it does **not** literally mandate experiments for every analytical claim. The coherent reading is role-appropriate evidence for each retained claim, with an explicit question for each control.

**B. Reusable Prose**
Counts use whitespace-separated words; decimal expressions remain within their whitespace tokens. Notes are excluded.

1. Abstract/method chain: **52 words, 3 sentences**.
The network predicts process variables, and the declared affine correction maps these predictions onto the equalities specified for each input. During training, the corrected estimates supply the supervised loss used to fit the network. During prediction, the same correction yields the retained process estimates, which satisfy the declared equalities in exact arithmetic.
Author/review note: The interface, constant full-row-rank matrix and known input-specific equality target are stipulated here, not unresolved premises. Actual numerical implementation remains unverified; predictive gains and broader physical consistency are not supplied.

2. Candidate contribution: **27 words, 1 sentence**.
Known equalities are incorporated into the learning and output interface by using corrected predictions both to compute the supervised loss and to provide the final process estimates.
Author/review note: This positively states the supported design relationship. Its eligibility as a novelty contribution remains unresolved; neither a routine projection nor its placement alone certifies novelty or empirical advantage.

3. Analytical result: **22 words, 1 sentence**.
In exact arithmetic, the specified correction yields (1.5, -0.5) with zero equality residual; applying ReLU afterwards yields (1.5, 0) with residual 0.5.
Author/review note: This describes Request A’s calculation and postprocessing limitation. It does not insert ReLU into Request B, whose retained output satisfies the declared equalities without needing an empirical ablation to establish that algebraic property.

**Read Inventory**
Full-section reads, with partial reads identified explicitly:
- [Root English skill](../../SKILL.md): **Mission; Core Invariants; §§1–9**, including §6 subsections. [Root Chinese mirror](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md): **§§一–十**, complete.
- [English evidence companion](../../skills/engineering-experiment-evidence-design/SKILL.md): **Mission; §§1–15**, complete. [Chinese evidence mirror](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md): **§§一–十六**, complete.
- [Abstract/contribution companion](../../skills/engineering-abstract-contributions/SKILL.md): **Start From The Actual Study; Revise Within The Author’s Scope; Return A Decision-Ready Proposal; Acceptance Check**.
- [Evidence reference](../../references/experiment-evidence-design.md): **§§1–5; §6 opening through missing-data supervision; “Knowledge And Physical-Constraint Claims”; §8 metric definitions, head-count-control paragraph, “Multilabel And Compound-Fault Decisions,” “Continuous Monitoring: What Is Scored And When,” “Scores, Probabilities And Rejection Decisions”; §§9–11**. Other search-returned passages were excerpts, not complete-section reads.
- [Contribution narratives](../../references/contribution-narratives.md): **Record Novelty On Separate Axes; Separate A Principle From Its Implementation; Select The Argument Route; Make Interactions Real; Position Prior Work Fairly; Choose Comparisons Proportional To Claims; Turn Analysis Into Manuscript Prose**.
- [Abstract/contribution craft](../../references/abstract-and-contribution-craft.md): **§§1–2; §3 excerpt at lines 115–155; §§4–6**, plus search excerpts elsewhere. [Argument/prose craft](../../references/argument-and-prose-craft.md): **§§4–6**, plus heading/search excerpts.

No files or approved results were changed; no browsing, scientific experiments, external model calls, thread creation or account-setting changes occurred. These fixtures establish neither a new general mechanism nor a terminology/translation admission.
