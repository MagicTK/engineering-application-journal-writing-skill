# Chinese Execution And Evidence-Object Parity

Primary report: [current forward report](../forward-test-report.json).

## Source Review And Repairs

A separate reviewer read the complete execution and journal-migration pairs:
49/47 and 63/48 lines respectively (207 lines, no truncation). The Chinese
execution guide omitted continuous-monitoring evidence retention and weakened
immutable runs to a prohibition on silent overwriting. Both were repaired;
the same reviewer reread the exact English rows and Chinese 17-34 lines and
confirmed them. That follow-up is not a second independent review. No material
migration mismatch was found within this scope.

The maintainer read the complete abstract-example pair (367/130 lines) and
clarified one standalone mass phrase as belief mass, reducing confusion with
product quality. The existing [Chinese authority](https://www.cjig.cn/zh/article/doi/10.11834/jig.250475/)
was reopened: PDF page 5, Section 1.2, uses the belief/uncertainty-mass wording.
This is a bounded terminology recheck, not new generic-name admission or
certification of that review's mathematics. An unsuccessful PDF screenshot
and a truncated compound search were not treated as evidence; the later
successful bounded text passage is the basis for the clarification.

## Procedure And Judgment

One new responding context used the frozen 4.2.41 instructions for the two
fictional requests below. The maintainer judged its complete first answer
against criteria saved before dispatch. No corrective feedback or retest was
needed; no baseline behavior failure, controlled improvement, independent
second grader or full-suite certification is claimed.

- A correctly preserves the original run, scores, alarms, labels, threshold
  source and window mapping. It distinguishes a newly versioned scoring
  derivative from a new model run and computes the supplied onset-to-alarm
  difference as 3 seconds, not zero or 2 milliseconds.
- B preserves belief mass, its actual combination and the supplied final
  decision. It does not invent a product-quality target, a named combination
  rule, calibrated probabilities or measured improvements.
- Both requested English passages retain positive operation descriptions.
  A is detailed experimental-setting prose, not an abstract brevity model.
  Neither answer establishes correctness of an unspecified metric or rule.

The respondent reported preloaded context without memory search; a truncated
keyword lookup was recovered by bounded relevant reads. Its actual file/range
record is retained below. Source-root use is distinct from installed client
discovery. Public local paths and writing wrappers are normalized; private
exact records preserve the original answer. No real paper or experiment was
edited, run or certified. Historical tests retain their original snapshots.

## Actual Request

Use the suite at <suite root>, current candidate 4.2.41. Read the Chinese experiment-automation entry for A and the Chinese abstract-contributions entry for B, with their relevant references. Do not read evaluation/history or private maintenance records, use memory search, browse, edit files, run experiments or spawn agents. Included quota checked at 79% remaining; no resets, credit use or paid fallback. Stop if quota blocks use. Answer only these two fictional requests; no whole-paper review. Give the actual read ranges and any inherited context/truncation recovery after the answer. Do not self-grade.

A. A continuous process is measured each second. Run r17 uses four-sample trailing windows; output times are 3,4,5,6,7 seconds and the corresponding scores are 0.2,0.3,0.9,0.2,0.1. The threshold 0.8 was fixed using training normal data. The first emitted alarm is at time 5; the labelled fault interval is [2,5]. Point adjustment marks the entire labelled fault interval positive when any alarm falls inside it. The model's measured forward-pass runtime is 2 ms. A colleague proposes reporting zero alarm delay after point adjustment, or 2 ms as the delay, and overwriting r17 predictions/figures with a corrected scoring script after notifying coauthors. No new model run is authorized. Give a compact Chinese handoff and two connected English Experimental Setup sentences. Distinguish what is preserved from what may be newly derived; do not calculate an unspecified benchmark metric or execute anything.

B. A fictional engineer reads the suite's evidence-combination example and interprets mass as the measured product-quality target. In this classifier, each of two sensor encoders actually produces belief masses over the same known fault-class frame. A specified combination rule outputs a combined mass function, and a supplied decision rule maps that function to the final fault label. No product-quality scalar, probability calibration, deployment or comparative performance is supplied. Explain the Chinese term and give two connected English Methods sentences. Do not invent the name of either rule.

## First Answer

**A. 中文交接与 Experimental Setup**
- **实际时序：**四样本尾随窗口对应 `[t−3,t]`，四个采样点跨越3秒；输出从3秒开始，2秒没有模型输出。阈值0.8来自训练正常数据，原始告警序列为 `0,0,1,0,0`，首次实际告警在5秒。以标注故障起点2秒为参照，告警延迟为 **3秒**。
- **不能替代：**点调整将 `[2,5]` 回填为阳性，只改变事后计分，不会产生2秒时实际发出的告警，因此不能报告零延迟。2 ms仅为模型前向计算耗时，也不是告警延迟或完整端到端时延。
- **必须保留：**r17的原始时间戳、分数 `0.2,0.3,0.9,0.2,0.1`、预测、实际告警、标签区间、阈值来源、窗口映射，以及原运行记录、脚本版本和图件均保持不可变；通知合作者不构成覆盖授权。
- **可新派生：**上述3秒延迟可由既有记录直接推导。后续若获准修正评分，可基于同一批保存输出另建评价版本，记录其与r17的关联、评分脚本版本、有效输出范围、点调整规则及新旧差异，并生成独立图件；这不是新模型运行，也不能把缺失的2秒输出冒充原始预测。本次不执行处理，不计算未指定的基准指标。

Run r17 used four-sample trailing windows of measurements sampled once per second, mapping each window [t−3, t] to its endpoint score at t = 3, 4, 5, 6, and 7 s with a threshold of 0.8 fixed using normal training data. Relative to the labelled fault onset at 2 s, the first emitted alarm at 5 s gives an unadjusted detection delay of 3 s; point adjustment retrospectively marks the labelled interval [2, 5] s positive for scoring only, while the measured 2 ms forward-pass runtime is reported separately.

**B. 术语解释与 Methods**
这里的 **信念质量（belief mass）** 是分配给故障类别命题或类别集合的支持量；“质量”对应 *mass*，不是产品品质 *quality*，也不是实测产品质量目标。两个编码器输出的是同一已知故障类别识别框架上的质量函数，组合后仍是质量函数，须经给定决策规则才能得到故障标签。不能直接将其等同于经过校准的类别概率，也不能据此声称部署或性能优势。

Each of the two sensor encoders produces belief masses over the same frame of known fault classes. The specified combination rule fuses these mass functions into a combined mass function, which the supplied decision rule maps to the final fault label.

**读取与恢复**
核实所读入口版本为 **4.2.41**。实际正文读取范围如下，另对最后三份参考做过关键词定位，未全文通读：
- [总入口](../../SKILL.md)：1–220行。
- [中文实验自动化入口](../../skills-zh/engineering-experiment-automation-zh/SKILL.md)：1–46行。
- [中文实验执行参考](../../references/experiment-execution_CN.md)：1–49行。
- [中文摘要贡献入口](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)：1–56行。
- [中文摘要贡献参考](../../references/abstract-and-contribution-craft_CN.md)：1–84行。
- [连续监测评价参考](../../references/experiment-evidence-design.md)：641–650行。
- [中文接口例子](../../references/abstract-mechanism-examples_CN.md)：60–68行。
- [中文术语裁定](../../references/terminology-decisions_CN.md)：349–375行。

本轮没有上下文压缩或续接；预置记忆摘要未用作答题依据，未进行记忆搜索。一次关键词定位输出被截断，随后定范围补读了接口例子60–68行及术语裁定349–375行，相关依据已完整取得。未读取评测、历史或私有维护记录，未联网、编辑文件、运行实验或启动代理。
