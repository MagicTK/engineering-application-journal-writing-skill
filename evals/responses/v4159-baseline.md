# Fictional Weight-Role Baseline

One task context answered two requests on the immutable v4.1.58 release. Core arithmetic, science and linked writing already passed; it accurately reported the missing matched class-weighting definition/Chinese record. Wrapper, local-link and whitespace normalization only; raw records remain private.

A preset history summary was present and disclosed above; it was not used as evidence. All cases and results below are fictional.

**A. Arithmetic And Naming**
Let each class-conditional mean loss equal \(L\). Expected class contributions are \(q_cw_cL\):

| Sampling | Normal contribution | Fault contribution | Normal:fault |
|---|---:|---:|---:|
| Uniform original examples | \(0.9L/900=L/1000\) | \(0.1L/100=L/1000\) | \(1:1\) |
| Equal-probability classes | \(0.5L/900=L/1800\) | \(0.5L/100=L/200\) | \(1:9\) |

Thus the relative shares change from **50%:50% to 10%:90%**. The second arrangement is not inherently wrong: it defines a different, more fault-emphasizing objective needing explanation. It would mismatch an intention to equalize expected class contributions.

For the untouched evaluation, normal-class F1 is \(1900/1950=38/39\); fault-class F1 is zero.

| Metric | Value |
|---|---:|
| Accuracy | \(950/1000=95\%\) |
| Class-support-weighted F1 | \(0.95(38/39)=361/390\approx92.5641\%\) |
| Macro F1 | \((38/39+0)/2=19/39\approx48.7179\%\) |

Weighted F1 neither establishes minority benefit nor indicates a weighted training loss. Its weights are evaluation class supports; here it remains high despite zero fault recall.

Method sentence, 34 words:
Using uniform sampling of original training examples, we fit the classifier with per-example cross-entropy weights of 1/900 for normal and 1/100 for fault; the fitted classifier predicts by ordinary softmax argmax without score reweighting.

**Release record:** No qualifying record was found for **class weighting in classification training loss** in terminology-bank §11 or the published-evidence index. The matched English definition pair is absent; independently verified Chinese wording is absent; qualifying IDs/sections are therefore absent. This does not invalidate the operation.

The nearby **P10/P44** record concerns distribution alignment: P10 pp.5-6, Eqs.(15)-(17), and P44 pp.4-5, Eqs.(12)-(15). **P36**, pp.1-4, concerns task-gradient balancing. Neither these nor feature weighting, sampling, or generic cross entropy supplies the requested admission record.

Base components cannot establish the complete generic name **Causal Minority-Preserving Weight Gate**. One namesake paper supports attributed paper-specific use, not general-category admission; the supplied evidence does not support causal identification. A genuinely new, author-approved proposal may still receive an operationally defined name, with its novelty and causal claims assessed separately.

**B. Fictional Draft**
LabelWeightNet is retained as the approved English name. No Chinese name is invented, and methodological novelty remains pending.

Abstract, 123 words:
Rare fault measurements are limited relative to normal production, motivating diagnostic models that explicitly account for unequal class representation during fitting. We present LabelWeightNet for diagnosing known fault classes from process measurements. A compact temporal encoder supplies representations to a fault classifier. Fixed inverse-training-frequency class weights multiply the per-example cross-entropy terms, adjusting each class's contribution while original training examples are sampled uniformly. The resulting encoder and classifier are retained for prediction, assigning a class through ordinary softmax argmax. Comparisons on a simulated process benchmark and an independent recorded production case use matched splits and seeds against the same architecture trained with unweighted loss. Class-support-weighted F1 is higher in both cases, whereas macro F1 increases on the benchmark and decreases on the production case.

Contribution, 28 words, framed as a bounded empirical finding:
Matched comparisons of LabelWeightNet with its unweighted counterpart identify higher class-support-weighted F1 in both cases, with macro F1 improving on the benchmark but declining on the production case.

Counts use whitespace-separated words, with hyphenated compounds counted as one. The draft preserves the training-to-predictor connection and mixed findings without presenting routine weighting as established novelty.

**Actual Reading**
Only release guidance and index passages were read, not original papers:

- [Release entrypoint](../../SKILL.md) and [abstract companion](../../skills/engineering-abstract-contributions/SKILL.md).
- [Terminology bank](../../references/engineering-application-terminology-bank.md), §§0,11, with targeted [Chinese-mirror](../../references/engineering-application-terminology-bank_CN.md) checks.
- [Terminology decisions](../../references/terminology-decisions.md), naming, alignment and reporting; [published index](../../references/published-evidence.md), P36 and alignment passages.
- [Abstract craft](../../references/abstract-and-contribution-craft.md), §§1-2,4-5.
- [Topic playbooks](../../references/topic-playbooks.md), §2 and task-weighting passage; [evidence guidance](../../references/experiment-evidence-design.md), imbalance and aggregate-comparison passages.
