# Numerical Pretraining And Generated Categories: Candidate Actual Response

A separate context used frozen v4.2.22 and the same fictional request, with only SUITE_ROOT changed. Both cases passed maintainer review without feedback. This does not measure general improvement over the already passing initial answer. See the [initial request](pretrained-role-initial.md).

## Actual Response

**1. 中文判断**
两项研究应独立叙述，不能统称为语言模型应用。

- **A：自监督数值预训练 → 有监督浓度回归。** 遮挡重建提供预训练目标；20 个生产批次的实测浓度监督低秩增量与回归头。预测时执行含已学增量的编码器和回归头，输出当前浓度，不进行评价时更新。这里没有语言推理。
- **B：有监督音频—语言适应 → 类别文本生成与规则映射。** 模板描述依赖训练标签和元数据，是监督目标，不是新增独立故障样本。预测输入不含真实标签或目标描述。
- 冻结基座不等于无需标签，也不意味着没有推理计算。B 删除不匹配回答后的准确率不能替代总体准确率；类别文本不能证明维护解释有效，`uncertain` 也不构成已实现、已验证的未知故障拒识。

**2. 结果核算**
**A：** 以下差值依据给定 MAE，并非从原始预测重新计算：
- 绝对降低：\(0.16-0.12=0.04\ \mathrm{g/L}\)。
- 相对降低：\((0.16-0.12)/0.16=25\%\)，分母为未预训练对照的 MAE。
- 八个批次是独立留出单位，不一定是 MAE 的分母。若合并窗口计算，分母为八批次的窗口总数 \(N=\sum_{b=1}^{8}n_b\)；若等权平均批次 MAE，则外层分母为 8，各批次内部仍除以 \(n_b\)。题设未指定聚合方式或窗口数，不能补造。

**B：** 第 1、2、3、5、7 次正确；第 4 次为有效类别错分；第 6、8 次不匹配。
- **总体准确率：\(5/8=62.5\%\)**，全部八次决策各计一次。
- 有效输出率：\(6/8=75\%\)；不匹配率：\(2/8=25\%\)。
- 有效输出内的条件准确率：\(5/6=83.33\%\)。其分母是六条有效回答，不能称为全部决策的准确率。

**3. English: Study A**
**Method Overview**

Current concentration is estimated from industrial measurement windows using a numerical time-series encoder and a regression head. The encoder is pretrained by reconstructing deliberately masked values in an external multivariate time-series corpus. With the pretrained encoder weights frozen, additive low-rank weight updates and the regression head are jointly trained using measured concentration targets from 20 production batches. At prediction, each available measurement window passes through the encoder with the learned updates and the head to produce one current concentration estimate using fixed fitted parameters.

**Results**

On eight held-out production batches, the pretrained predictor achieved an MAE of 0.12 g/L, compared with 0.16 g/L for a matched predictor using the same encoder architecture without pretraining. With the downstream fitting data and update/head budget held constant, this represents an absolute MAE reduction of 0.04 g/L and a relative reduction of 25% in the evaluated concentration-estimation task.

**4. English: Study B**
**Method Overview**

Bearing diagnosis is formulated as category-text generation from vibration windows. A pretrained general-audio encoder and language decoder are adapted using vibration/text training pairs, with base weights frozen and low-rank updates learned. Target descriptions are constructed from templates populated with known training fault labels and metadata, providing supervised targets for adaptation. At prediction, a vibration window and a fixed instruction condition answer generation. Whitespace trimming and lowercasing are followed by exact matching to normal, inner-race, or outer-race; unmatched answers are counted as unsuccessful decisions.

**Results**

Across eight independent held-out decisions, five generated answers matched the reference categories, yielding an overall diagnostic accuracy of 62.5% (5/8). Six answers matched an allowed category string, giving a valid-output rate of 75% (6/8). Accuracy among these valid outputs was 83.33% (5/6). The complete evaluation comprised five correct category outputs, one incorrect allowed-category output, and two unmatched answers, with all eight decisions retained in the overall denominator.

**仅需条件核查**
A 的 MAE 聚合方式与窗口数需补充说明。除此之外，只在作者坚持保留相应强主张时补证：保留“无额外推理开销”，需明确比较边界、低秩增量实际执行或合并方式，以及对应计算量或计时依据；保留“可执行维护解释”或“可靠未知故障识别”，需分别有维护效用证据，或实际未知类决策机制及未知类评价。当前段落不保留这些主张，无需统一追加提示词、幻觉、部署或新对比实验。已核实的 A 预训练来源与评价序列隔离不再列为未知项。

**阅读披露**
实际读取公开入口 [SKILL.md](../../SKILL.md)、[README.md](../../README.md) 第 1–53 行；[topic-playbooks.md](../../references/topic-playbooks.md) 第 53–108、365–527 行；[指标完整性段](../../references/experiment-evidence-design.md)第 371–477 行；[行文衔接与边界段](../../references/argument-and-prose-craft.md)第 55–103 行，以及这些公开文件和 `terminology-and-style.md` 的检索命中片段。一次检索输出被截断，关键段已定点重读。另按系统要求读取通用技能调用说明。会话预带通用用户／工作区摘要，未用作研究依据；未读取记忆文件、评测、测试、私有维护记录、实际稿件或其他项目，未浏览、委派、改文件或开展研究实验。
