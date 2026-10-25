# Weak-Signature Problem Baseline

One fresh read-only context on the v4.2.4 guidance. Scientific decisions and the 56-word note already pass; the actual improvement is navigation/evidence, not a fabricated model failure. Only wrapper/link/line metadata and whitespace are normalized; exact dispatch and raw response remain private.

**Request A**
The engineering difficulty is **normal/fault discrimination for small imposed process perturbations under measurement noise**, in a dynamically responding simulated closed-loop process.

- **English:** “fault detection under small-amplitude imposed perturbations and measurement noise.”
- **Chinese:** “测量噪声下小幅施加扰动的故障检测。”
- Preserve attribution: “simulated scenarios termed *incipient faults* by the source author” / “源作者称为‘早期故障’的仿真场景”，并说明其实现为固定严重度的小幅阶跃扰动。

“Weak observable fault signatures / 微弱故障表征” is appropriate only if the measured response supports that description. A small injected change does not by itself establish a small measured response.

This test alone cannot establish:
- **Physical early-stage degradation or slowly growing faults:** no degradation trajectory or lifecycle evidence exists. A gradual measured transient can result from closed-loop dynamics despite a step input.
- **Intermittent faults:** a fixed-severity condition does not demonstrate repeated fault appearance/disappearance.
- **Noise robustness across levels:** the evidence concerns the specified noise setting.
- **Shorter detection delay:** a known injection time plus binary classification results does not supply alarm-delay measurements.

The 0.5% perturbation and 2% noise standard deviation describe different quantities; they do not define the measured response’s SNR. **Physical input-variable amplitude is also not learned feature activation magnitude**: their scales, units and transformations differ. Small activations do not establish small physical faults.

Introduction note, **56 words**, with no algorithm or invented mechanism:

Small imposed process changes can be difficult to distinguish from measurement noise in a dynamically responding closed-loop process. Using simulated scenarios termed incipient faults by the source author, this study examines normal-fault discrimination for fixed-severity perturbations. The methodological aim is to distinguish fault-related measurement patterns from normal responses under the specified process dynamics and noise setting.

**Request B**
The valid finding is **higher fault-classification F1 on completed windows under the reported evaluation**. That finding does not establish earlier warnings, and retaining this scope does **not** require new timing experiments.

| Property | What it means |
|---|---|
| Early-after-onset interval | A temporal position relative to an identified onset; not automatically an incipient physical condition |
| Small severity | Perturbation or damage magnitude; independent of elapsed time since onset |
| Issued alarm | An actual decision emitted at a specified time, after required information becomes available and processing completes |
| Future-event prediction | A prediction issued before the defined target event, with an explicit future target/horizon |

Thus, the first ten post-onset samples are not automatically “incipient faults.” Moreover, calling them post-onset requires an onset reference not supplied in this paper.

**Ten timestamps spaced two seconds apart span `(10−1)×2 = 18 seconds`.** If the first timestamp equals onset, the last is onset +18 seconds. If the first is onset +2 seconds, the last is onset +20 seconds, but their endpoint span remains 18 seconds. Twenty seconds of interval coverage is possible under an explicitly defined bin/window convention, not as the timestamp endpoint span.

Only if the authors retain a stronger warning claim is follow-up necessary:
1. Define the reference event and comparator: faster **post-onset detection** or warning **before a future event**.
2. For post-onset timing, first reuse recoverable time-resolved records: establish onset references, information availability, the alarm rule and actual issue times; compare unadjusted first-alarm delays alongside detected/total events and a relevant false-alarm measure. Completed windows cannot be backdated to their starts or centers.
3. For pre-event warning, additionally define and evaluate the future event target, event matching and warning lead time. Safety-intervention trials are necessary only for a retained safety/intervention-benefit claim, not merely a timing claim.

If the necessary records cannot be recovered, additional time-resolved evaluation is needed **only to support the stronger claim**. No new method is implied.

**Current Guidance**
The Skill already contains correct rules:

- [research-planning-and-contribution.md:51](../../references/research-planning-and-contribution.md) separates early-after-onset from low-severity/incipient properties and gives `(n−1)Δt`.
- [experiment-evidence-design.md:600](../../references/experiment-evidence-design.md) distinguishes window scores from onset accuracy; line 604 specifies actual alarm timing, missed events and bounded trace reanalysis, while explicitly exempting accurately scoped window-classification papers.
- [experiment-evidence-design.md:458](../../references/experiment-evidence-design.md) separates prediction horizon, execution latency and measured warning lead.

**Discoverability is weaker than correctness.** The [Chinese entrypoint’s problem-only route](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md) leads to the problem-first reference, but neither language version directly presents this fault-severity/onset/alarm distinction or links to those specific rules. This is a navigation gap, not an absent timing rule or justification for another Skill file.

Read-only assessment completed; no files changed or experiments run.
