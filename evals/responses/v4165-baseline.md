# Fictional Weight-Placement Baseline

One context answered A/B on immutable v4.1.64. Scientific judgments, exact arithmetic and writing already pass; P98 is correctly reported absent from that version. Wrappers, local path/link metadata and whitespace are normalized; exact raw records remain private.

历史披露：有预置的旧版发布及术语审查摘要，含 v4.1.22；它可能过时，仅作披露，不作为当前包已修复或通过的依据。

**A. 机制与准入**
不能因为都叫 `class-weighted` 就使用同一完整机制名。甲把类别系数乘到分类交叉熵；乙的链条是“目标特征 → 系数缩放 → 非线性映射 → 映射均值比较”，分类交叉熵没有该系数。乙通过训练目标影响编码器，预测仍使用编码器与分类器，不能改写成加权分类损失或预测门控。

以下是**本轮读取的库内登记**，不是本轮独立精读论文原文后的结论：

| 记录及来源全名 | 当前记录与边界 |
|---|---|
| P44：*A Multisource Domain Adaptation Network for Process Fault Diagnosis Under Different Working Conditions* | pp.4–5、式(12)–(15)记录域对抗及类别加权分布目标，与分类器输出组合分开；不是分类交叉熵外乘类别因子的第二来源。式(15)及算法I中的目标标签符号问题仍保留，不能直接认定无监督。 |
| P96：*An imbalanced domain-adversarial hypergraph convolutional network for robust fault diagnosis of rotating machinery* | p.3、式(3)–(4)提供明确的交叉熵外乘类别因子定义；p.6的提出目标还包含 logit 间隔，不能把背景定义当成完整 IDAHGCN 损失。 |
| P97：*Intelligent fault diagnosis for chemical process under imbalanced data: A non-local frequency-domain sparse hash autoencoder approach* | p.4表1有类别加权交叉熵，但p.8、式(35)–(36)呈现未按类别加权的二元交叉熵及整体目标系数。实现歧义未解决，不能算无歧义的第二个匹配来源，也不能认证完整 NFSH-AE 损失。 |
| P98 | 当前文献索引无此记录，相关术语及技能文本检索亦未发现；不能补造其阅读或准入状态。 |

**结论：分类损失 `class-weighting/weighted-CE` 的双来源准入尚未完成。**这是当前库的证据状态，不是数学加权操作不合法；中文“加权交叉熵损失”的译名记录也不能补足第二个英文运算定义。题设乙不新增实际文献阅读记录。

算术核对：当 \(\phi(v)=v^2,f=2,w=3\)，\(\phi(wf)=36\)，而 \(w\phi(f)=12\)，二者不同。

四样本缩放后为 \([2,4/3,4/3,4/3]\)：

| 量 | 精确结果 |
|---|---:|
| 平均系数 | \(1\) |
| 原特征均值 | \(7/4\) |
| 缩放后均值 | \(3/2\) |
| 平均 \(\phi(wf)\) | \(7/3\) |
| 平均 \(w\phi(f)\) | \(5/2\) |

平均系数为1不足以保证特征统计或核几何不变。例如，两种特征取值在该 \(\phi\) 空间的距离从 \(3\) 变为 \(20/9\)。但不能反向断言任何非线性映射都不等价：线性映射或满足相应一次齐次条件时，两式可以相等。应核对实际映射及实现，不要求作者机械换公式；即使条件下等价，也不自动等同于分类损失加权。

**B. 英文候选**
方法总览：两句，52词。

A temporal encoder produces diagnostic features and is jointly trained using source classification error and a comparison of source and target distributions, with coefficients derived from pseudolabel counts on unlabeled target measurements scaling target features before nonlinear mapping. The trained encoder supplies features to the classifier for fault diagnosis on new measurements.

贡献候选机制表述：一句，30词。

The design scales target features according to pseudolabel counts before nonlinear mapping for distribution comparison, coupling this objective with source classification to train the temporal encoder retained for fault diagnosis.

结果解释：一句，27词。

Relative to comparators using the same inputs, higher overall accuracy accompanies lower recall for one fault class, indicating an aggregate performance gain with a class-specific diagnostic trade-off.

作者说明：贡献仍是候选，尚缺最近相关文献与实际差异的比较，不能认定文献新颖性；普通加权、标准编码器或常规实验本身不构成已确立创新。现有结果也不支持添加显著性、已证对齐或鲁棒性收益。词数按空格分词，连字符词计一个词。

**实际读取与范围**
以下文件读取了正文或相关段落，并非全部逐行审计：
- [主入口 SKILL.md](../../SKILL.md)。
- [术语语境裁定](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/terminology-decisions.md#L145)、[中文对应](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/terminology-decisions_CN.md#L102)。
- [术语库](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/engineering-application-terminology-bank.md#L397)、[中文对应](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/engineering-application-terminology-bank_CN.md#L193)。
- [文献登记与阅读边界](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/published-evidence.md#L110)。
- [摘要贡献技能](../../skills/engineering-abstract-contributions/SKILL.md)、[摘要贡献指南](../../references/abstract-and-contribution-craft.md)。
- [实验证据技能](../../skills/engineering-experiment-evidence-design/SKILL.md)、[实验指南](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/b555c22716c9a6d192916345b60e28a0b3fbe56a/references/experiment-evidence-design.md#L226)。
- 包外另读：通用技能入口 (private local reference)、历史记忆索引 (private local reference)，不作为当前包内容证据。

本轮仅完成指定条目的只读核对、给定算术及虚构文本写作；未改文件、浏览外链、运行科研实验或调用代理，不声称当前源码已修复或整库通过。
