# Weak-Signature Problem Final Response

One completed fresh context read the corrected frozen v4.2.5 guidance; two fictional requests, not research experiments. The v4.2.4 baseline already passed scientific decisions. A first candidate context was stopped before completion after structural checks found stale source-count metadata; it is not a passed review. No controlled general writing gain is claimed. Only wrapper/path/link/line metadata and whitespace are normalized; exact raw/dispatch remain private.

**A. Problem Classification**
The engineering difficulty is **normal/fault discrimination under small imposed perturbations and measurement noise**. The task is binary fault detection, not fault-type identification or prognosis.

Suitable wording:
- **English:** “Binary fault detection under small-amplitude step perturbations and measurement noise.”
- **Chinese:** “测量噪声条件下小幅阶跃故障扰动的正常/故障二分类检测。”
- **Attributed usage:** “Scenarios termed *incipient faults* by the source author, implemented here as fixed-severity, small-amplitude step perturbations.”
- **Chinese attribution:** “沿用原作者所称的‘微小故障（incipient faults）’情景，在本测试中实现为固定严重度的小幅阶跃扰动。”

“Weak fault signatures / 微弱故障特征” is appropriate **if the measured fault-related response is established as weak**. The 0.5% imposed step does not itself establish that: closed-loop dynamics can alter the response’s magnitude and shape. A dynamic measured transient is not evidence of increasing fault severity. These distinctions are explicit in the [English problem-first guidance](../../references/problem-first-classification.md) and [Chinese counterpart](../../references/problem-first-classification_CN.md).

This test alone establishes **none** of the following: physical early-stage degradation, slowly growing faults, intermittence, robustness across noise levels, or shorter detection delay. Intermittence concerns fault appearance/disappearance, not fluctuating measurements. One noise setting is not a noise-level robustness comparison; known injection time alone does not supply alarm-delay evidence.

**Input-variable amplitude and learned feature activation magnitude are different quantities.** Feature scaling and transformations can change activation magnitude without changing physical severity. Likewise, the two percentages do not define an SNR: the relevant signal, noise, measurement location and amplitude/power convention remain unspecified.

Introduction note, **52 words**:

Small imposed fault perturbations must be distinguished from normal process variation in noisy measurements. This study considers simulated step perturbations at a fixed selected severity, termed incipient-fault scenarios by the source author. The methodological aim is to improve binary normal/fault discrimination from the resulting dynamic process responses under the stated benchmark conditions.

**B. Classification Versus Warning**
The higher F1 supports **better fault-classification F1 on the evaluated completed windows**. It does not establish earlier warnings, shorter detection delay, physical-onset localization, prediction of future faults, or safety benefits. Keeping the window-classification scope requires **no additional timing experiments**.

Four properties must remain separate:
- **Early after onset:** observations occupy an initial post-onset interval.
- **Small severity:** the fault perturbation is small relative to a specified reference; temporal proximity to onset does not establish this.
- **Issued alarm:** a decision is actually emitted after its required information becomes available and processing finishes.
- **Future-event prediction:** an output issued before a defined future event targets that event at a stated horizon.

Consequently, the first ten post-onset samples are not automatically “incipient faults.” Nor can a completed-window decision be retrospectively assigned to the window’s beginning.

**Timing:** ten timestamps separated by two seconds span `(10 − 1) × 2 = 18 seconds` between endpoints. Twenty seconds could describe ten explicitly defined two-second intervals, or onset-to-last-sample time if the first sample occurs two seconds after onset. Neither makes the timestamp endpoint span twenty seconds. The exact rule already appears in [research-planning-and-contribution.md](../../references/research-planning-and-contribution.md).

Only if the authors retain a warning claim is follow-up necessary:
1. **Earlier post-onset alarms:** obtain a justified onset reference, time-stamped sequential outputs and a defined alarm rule; account for input availability and processing. Compare first-alarm delays with the reference method, reporting detected/total events and false-alarm burden under comparable criteria.
2. **Prediction before a future event:** additionally define that future event and forecast target/horizon, then evaluate genuinely pre-event issued warnings and their lead times.

Suitable existing records may support this assessment; new data collection is necessary only if the required evidence cannot be recovered. Safety-intervention trials are not a prerequisite for measuring alarm timing, but classification F1 supplies no intervention-benefit evidence. The [existing alarm guidance](../../references/experiment-evidence-design.md) explicitly preserves accurately scoped window classification.

**Current Skill Assessment**
**The correct rules already exist and are directly discoverable.** The [Chinese entrypoint](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md) routes problem-only work to the Chinese problem-first reference. Its relevant subsection explicitly separates severity and timing, then links to both existing timing references; the English version does likewise.

For this scoped baseline, the problem-first route makes the distinction straightforward to find. No missing rule or additional Skill file is indicated. No files were changed, and no original papers or external evidence were consulted.
