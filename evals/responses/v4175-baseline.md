# Fictional Fuzzy-Rule Baseline

One context answered A/B on immutable v74. Science and prose already pass; the response correctly distinguishes existing Gaussian/rule guidance from a missing specific TSK admission row. Only wrappers, local link/path metadata and whitespace are normalized; exact dispatch/raw remain private.

**A. Scalar Analysis**
\[
y(x)=\frac{x(2x+1)+(-x+3)}{x+1}
=\frac{2x^2+3}{x+1}.
\]

| \(x\) | \(y(x)\) |
|---|---|
| 0 | \(3\) |
| 1 | \(5/2\) |
| 2 | \(11/3\) |

The unit-step second finite difference is
\[
\Delta^2y(0)=y(2)-2y(1)+y(0)=\frac{11}{3}-5+3=\frac53.
\]
Thus, **affine local consequents do not make the complete map affine**: input-dependent weights change the combination. Nor do normalized rule weights make its output a probability; here \(y(0)=3\).

With antecedent functions fixed,
\[
y(x)=[a_1(x)x,\ a_1(x),\ a_2(x)x,\ a_2(x)]\theta,
\qquad \theta=(2,1,-1,3)^\top,
\]
so the output is linear in the consequent coefficients, although nonlinear in \(x\). Jointly fitting antecedent and consequent parameters changes the basis functions and generally produces a nonlinear joint fitting problem. In classification, a subsequent softmax also makes probabilities nonlinear in the score coefficients.

Constant consequents need not produce a constant map: \(c_1=1,c_2=0\) gives \(y=x/(x+1)\). None of these calculations assumes Gaussian memberships; the weights are stipulated.

**Admission Audit**
I found **no completed specific TSK-rule/classifier admission record** in this release. Its Markdown search returned no TSK/Takagi/Sugeno match. This is a library-record gap, not evidence that the name is wrong or nonexistent.

The [Gaussian-membership record](../../references/engineering-application-terminology-bank.md) cites P27 and P77 for the base matching function. The separate “Fuzzy Rule Outputs” guidance distinguishes memberships, activations, normalized weights, local outputs and task probabilities; it does not complete TSK-specific admission. A survey’s bare mention supplies no additional checked equation definition. A substantively checked background definition can support that operation without certifying the source’s complete proposed architecture.

The [recorded Chinese checks](../../references/engineering-application-terminology-bank.md) support **高斯隶属度函数** through USTB 2011.05.013, §2.2/Fig.3, PDF pp.2–3, and **前件/后件** through the Tsinghua University Press trial chapter, §1.1, PDF p.5. These are existing library records, not fresh online verification, additional English-definition sources, or verification of a complete Chinese TSK compound name.

**B. Reusable Prose**
Counts use whitespace-separated words; hyphenated forms and compact equations count as single words. Labels and notes are excluded.

1. Abstract/method chain: **61 words, 4 sentences**.

An encoder maps available process measurements to latent features for Gaussian membership matching. Normalized rule activations weight affine local class scores, whose combination supplies softmax class probabilities and the decision. During training, consistency between rule activations from two deterministic views shapes the encoder and antecedent parameters alongside supervised classification. At prediction, the fitted encoder and rule classifier process one acquired sample.

Author/review note: The stipulated interfaces are accepted. Exact view operators, consistency formulas and implementation details were not supplied. Softmax provides legitimate model class probabilities, without calibration evidence; latent rules have no supplied expert-defined physical meanings.

2. Candidate contribution: **30 words, 1 sentence**.

Consistency between rule activations from two deterministic views shapes the encoder and antecedent parameters during supervised training, linking representation learning to the fitted rule classifier retained for single-sample class decisions.

Author/review note: This identifies the specific training interaction, not established originality or benefit. Those claims require prior-art comparison and supporting evaluation; routine Gaussian matching is not independently certified as novel.

3. Analytical result: **23 words, 1 sentence**.

The synthetic scalar map yields y(0)=3, y(1)=5/2 and y(2)=11/3, with second finite difference 5/3 at unit spacing, demonstrating nonaffinity despite affine local consequents.

Author/review note: This reports Request A’s analytical example only, not classifier performance, plant results or deployment evidence.

**Reading Record**
Substantive local reading, with partial sections identified:
- [Release SKILL.md](../../SKILL.md): complete, including Mission, Core Invariants and §§1–9.
- [Abstract/contributions skill](../../skills/engineering-abstract-contributions/SKILL.md): complete, all four sections.
- [Terminology-polishing skill](../../skills/engineering-terminology-polishing/SKILL.md): complete, Mission and §§1–14.
- [Terminology bank](../../references/engineering-application-terminology-bank.md): “Scope And Evidence Boundary”; §0 “Admit Names, Not Search Counts”; §11 introduction, Gaussian-membership and Chinese-translation rows, with surrounding table rows scanned.
- [Terminology decisions](../../references/terminology-decisions.md): lines 610–675, covering the preceding distinction-table tail, “Alignment: State The Object And Criterion,” “Fuzzy Rule Outputs,” and “Evidential Classification Quantities.”
- [Abstract craft](../../references/abstract-and-contribution-craft.md): §§1–2; §3 excerpt at lines 283–325, including “Rule-based prediction” and adjacent illustrations; §§4–5.
- [Published evidence](../../references/published-evidence.md): “Scope And Reading Depth” and “Fuzzy Matching, Rule Outputs And Task Decisions.” Other search hits/headings were scanned, not treated as full-section reading.

This was a local, read-only analytical/writing audit under ordinary runtime instructions, not a blank-context test or research experiment. No files were changed, and no browsing, training, external model calls, thread creation or account-setting changes occurred.
