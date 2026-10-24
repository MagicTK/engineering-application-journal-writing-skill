# Fictional Weight-Placement Final Response

One new context answered the unchanged A/B request on the final frozen source; only the read root changes. Baseline science, arithmetic and writing already pass. Wrappers, local path/link metadata and whitespace are normalized; exact raw records remain private.

**阅读边界**
预置历史包含该 Skill 的维护、术语审查与双语入口摘要，可能已过时；未据此判断当前源码。当前入口自报版本为 `4.1.65`。以下文献判断依据本轮读取的库记录，**不等于本轮重新阅读了原论文**。

**A. 术语裁定**
**不能因为都叫 `class-weighted`，就使用同一完整机制名。**
- 甲：类别系数乘分类交叉熵，改变分类训练损失。
- 乙：伪类别计数决定系数，先缩放目标特征，再经非线性映射比较分布；分类交叉熵没有该系数。
- 二者的乘法对象、接收运算和训练作用不同；乙也没有题设支持的预测期再缩放或门控。

当前库的实际记录如下，论文全名保留来源归属：

| 记录及来源全名 | 当前记录支持什么、保留什么歧义 |
|---|---|
| P44：[A Multisource Domain Adaptation Network for Process Fault Diagnosis Under Different Working Conditions](../../references/published-evidence.md) | p.5 式(13)的加权特征进入域判别器，不是分类交叉熵外乘类别因子。式(15)及算法含目标标签符号，不能仅凭题名移植为无监督设定。 |
| P96：[An imbalanced domain-adversarial hypergraph convolutional network for robust fault diagnosis of rotating machinery](../../references/published-evidence.md) | p.3 式(3)–(4)明确给交叉熵乘类别因子；p.6 提出的方法另含 logit 间隔，不能把背景定义等同于完整 IDAHGCN 目标。 |
| P97：[Intelligent fault diagnosis for chemical process under imbalanced data: A non-local frequency-domain sparse hash autoencoder approach](../../references/published-evidence.md) | p.4 表1有类别加权表达式，但 p.8 式(35)–(36)显示未按类别加权的二元交叉熵及整体目标系数。冲突未解，不能充作无歧义的第二定义，也不认证完整 NFSH-AE。 |
| P98：[Class-weighted alignment and reliable self-training for cross-domain fault diagnosis under class-imbalanced conditions](../../references/published-evidence.md) | **确有记录**。p.6 式(10)–(12)按目标伪标签计数，在映射前缩放目标特征；不是分类损失系数。具体非线性核未核定，计数公式不能直接称为字面频数倒数；完整 CWA-RST 名称仍须归属来源。 |

因此，**分类损失 `class-weighting`／`weighted-CE` 的匹配双来源准入仍未完成**。这是“有记录，但语义配对未完成”，不是“P98 不存在”，更不是数学加权不合法。译名核验记录也不能补成第二个英文运算定义。[当前准入边界](../../references/engineering-application-terminology-bank.md)

题设算术核对：
\[
\phi(wf)=(3\cdot2)^2=36,\qquad w\phi(f)=3\cdot2^2=12,
\]
二者不同。四样本缩放后为 \([2,4/3,4/3,4/3]\)：

| 量 | 精确结果 |
|---|---:|
| 平均系数 | \(1\) |
| 原特征均值 | \(7/4\) |
| 缩放后均值 | \(3/2\) |
| 平均 \(\phi(wf)\) | \(7/3\) |
| 平均 \(w\phi(f)\) | \(5/2\) |

平均系数为1，**不足以保证特征统计或核几何不变**。例如，以 \(k(a,b)=\phi(a)\phi(b)\) 定义核，第1、2样本的核值由 \(4\) 变为 \(64/9\)。

等价性仍须有条件保留：线性映射，或对相应系数满足一次齐次性的非线性映射，可以满足 \(\phi(wf)=w\phi(f)\)；这也不自动意味着缩放前后几何不变。本反例不指认 P98 的实际核，不要求作者机械移换系数或修改公式。

**B. 英文候选**
按空格计词，连字符词计一词。

方法总览：两句，57词。
A temporal encoder produces diagnostic features and is jointly updated by classification error on labeled source measurements and a distribution comparison of mapped source and target features, with coefficients derived from target pseudo-label class counts multiplying target features before nonlinear mapping. The trained encoder supplies diagnostic features to the classifier, which assigns fault classes to new measurements.

贡献候选：一句，29词。
We jointly train the diagnostic encoder with source classification error and a distribution comparison that scales target features using coefficients derived from target pseudo-label class counts before nonlinear mapping.

结果解释：一句，27词。
Higher overall accuracy than comparators using the same inputs accompanies lower recall for one fault class, revealing a trade-off between aggregate correctness and sensitivity to that fault.

作者说明：贡献句只是机制候选。尚无足以认定文献新颖性的比较，不能把普通加权或常规实验本身认定为创新；给定结果也不能单独证明缩放的独立作用、已实现对齐或鲁棒性收益。未将这些审查提醒塞入英文句子。

**实际读取**
以下均为当前包文件，其中参考文件按相关章节读取：
- 总控入口：[英文](../../SKILL.md)、[中文](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)。
- 术语语境裁定：[英文](../../references/terminology-decisions.md)、[中文](../../references/terminology-decisions_CN.md)。
- 术语库：[英文](../../references/engineering-application-terminology-bank.md)、[中文](../../references/engineering-application-terminology-bank_CN.md)；[已发表证据索引](../../references/published-evidence.md)。
- 摘要贡献入口：[英文](../../skills/engineering-abstract-contributions/SKILL.md)、[中文](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)。
- 摘要贡献指南：[英文](../../references/abstract-and-contribution-craft.md)、[中文](../../references/abstract-and-contribution-craft_CN.md)。
- 实验证据入口：[英文](../../skills/engineering-experiment-evidence-design/SKILL.md)、[中文](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)；[实验指南](../../references/experiment-evidence-design.md)。
- 包外仅另读了历史索引 (private local reference)与会话技能规则 (private local reference)。

本轮未改文件、浏览外链、运行科研实验或调用代理；结论限于上述局部记录、题设算术和候选写法，不代表整库通过或实际科研效果获证。
