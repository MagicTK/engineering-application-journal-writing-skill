# Fictional Loss-Graph Baseline

One context answered A/B on immutable v4.1.66. Science, exact calculus and prose already pass; the narrower matched record is correctly reported absent. Wrappers, local path/link metadata and whitespace are normalized; raw records remain private.

**Reading Disclosure**
I read the specified v4.1.66 `SKILL.md` and relevant sections of its linked terminology banks, terminology decisions/style, published-evidence index, experiment guide, contribution/prose guides, and polishing skill. Preset memory was supplied; this was not a memory-blank trial. I opened no memory files or source-paper PDFs and performed none of the prohibited actions.

**A. Derivatives**
These calculations concern your fictional definitions, not a source implementation. All logarithms are natural.

Since \(a'(q)=-2(1-q)\), \(\ell'(q)=-1/q\), and \(dq/dz=q(1-q)\), full differentiation gives
\[
\frac{dL}{dq}
=a'\ell+a\ell'
=2(1-q)\log q-\frac{(1-q)^2}{q},
\qquad
\frac{dL}{dz}
=2q(1-q)^2\log q-(1-q)^3.
\]

For \(\widetilde L=\operatorname{sg}[a(q)]\ell(q)\), where stop-gradient preserves the forward value but assigns zero derivative to the factor,
\[
\frac{\partial\widetilde L}{\partial q}
=-\frac{(1-q)^2}{q},
\qquad
\frac{\partial\widetilde L}{\partial z}=-(1-q)^3.
\]

At \(q=\tfrac12\):

| Training rule | Gradient with respect to \(q\) | Gradient with respect to \(z\) |
|---|---:|---:|
| Full differentiation | \(-\tfrac12-\log 2\) | \(-\tfrac18-\tfrac{\log 2}{4}\) |
| Stopped factor | \(-\tfrac12\) | \(-\tfrac18\) |

Both forward passes have \(a=\tfrac14\) and loss \(\tfrac{\log 2}{4}\). **Matching coefficient values does not match gradients:** full differentiation additionally includes \(\ell\nabla_\theta a\). For the same nonzero predictor Jacobian and ordinary SGD settings, the parameter updates therefore differ. Freezing an unrelated network changes nothing here; even freezing a coefficient-producing network’s parameters would not automatically detach its dependence on predictor-derived inputs.

The roles are distinct:
- A fixed **class-dependent factor** \(c_y\) distinguishes classes and multiplies their specified log-loss terms.
- A **confidence-dependent factor** \(a(q)\) varies with predictions, potentially within one class, and contributes an additional gradient when differentiated.
- An **overall objective coefficient** \(\lambda\) scales the complete classification objective, or its contribution within a larger objective; it does not itself distinguish classes. Evaluation-support weights are another separate role.

**Bank Status**
**This copy does not document a completed clean two-source admission record even for the narrower class-factor operation.** That conclusion follows from the recorded scopes, not titles:

| Record | Available evidence and boundary |
|---|---|
| P96, p.3, Eqs.(3)–(4) | Explicit class factor multiplying cross-entropy. Its proposed p.6 objective additionally modifies a logit through a margin. |
| P97, p.4, Table 1 versus p.8, Eqs.(35)–(36) | A class-weighted expression conflicts with later binary cross-entropy carrying an overall objective coefficient. The discrepancy remains unresolved. |
| P39, p.5, Eq.(13) | Recorded as a prediction-dependent focal factor, not a second checked fixed-class-factor definition. This reading scope does not establish that its full equation lacks other factors. |
| Other weighting records | P92/P94 concern selection; P93 weights residuals; P18 adjusts logits; P98/P44 weight features. These do not complete the requested pair. |

The Chinese weighted-cross-entropy record verifies bilingual wording only, without an accessible equation. Neither a complete ordinary weighted-cross-entropy loss nor a full adaptive-loss mechanism is certified by these records. A narrow class-factor admission, were completed, would still not certify either broader mechanism. See the local [bank boundary](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/840b90f0c0cd25e34816c325283d6d5c8703ee12/references/engineering-application-terminology-bank.md#L398) and [source-consistency notes](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/840b90f0c0cd25e34816c325283d6d5c8703ee12/references/published-evidence.md#L139).

**Incomplete admission prohibits neither a mathematically valid weighted loss nor an author-defined new component.** It limits presenting a name as an established shared category; accurate operational descriptions and explicitly defined proposals remain permissible.

**B. Method Overview**
A temporal encoder and classifier learn fault diagnosis from labeled process measurements using classification log-loss terms scaled by a prediction-derived factor. Differentiating through both the factor and the classification probabilities shapes updates to the encoder and classifier, whose trained composition supplies the diagnostic predictions.

**Candidate Contribution**
A differentiable prediction-dependent loss trains the temporal encoder and classifier through both the weighting factor and the classification probabilities, carrying the resulting parameter updates into the retained diagnostic predictor.

**Result Interpretation**
Higher macro-F1 and lower support-weighted F1 indicate improved F1 under equal-class averaging but reduced F1 under averaging weighted by evaluation class supports.

**Author Note**
Prediction dependence concerns training, with no separately trained coefficient network or inference-time learning. Novelty and isolated-component effects remain unestablished; class-wise evidence is needed to identify which rare faults improve.
