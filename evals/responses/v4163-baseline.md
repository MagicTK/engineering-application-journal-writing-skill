# Fictional Energy-Convention And Wording Baseline

One context answered A/B on immutablev4.1.62. Its arithmetic, scientific judgments and writing already pass; the old Chinese wording gap is reported accurately. Only wrappers, local links/line suffixes and whitespace are normalized; raw records remain private.

预置上下文含旧版本摘要，检索也带出包内旧测试片段；以下均不据此判断修复状态或整库质量。

**A. 算术审查**
按自然对数计算，拒绝条件为 \(E>-1.8\)：

| 样本 | 能量 \(E\) | Softmax | 类别候选 | 决策 |
|---|---:|---|---|---|
| A：[2,1] | −2.313262 | [0.731059, 0.268941] | 第1类 | 保留 |
| B：[1,0] | −1.313262 | [0.731059, 0.268941] | 第1类 | 拒为未知 |

对全部类别统一加常数 \(a\)，有：
\[
\operatorname{softmax}(z+a\mathbf1)=\operatorname{softmax}(z),\qquad E(z+a\mathbf1)=E(z)-a.
\]

- **所有样本均加3，阈值同步减3：** 新阈值为 −4.8，A、B能量分别为 −5.313262、−4.313262。类别概率、类别排名、样本间能量排名与拒绝决策均不变。
- **仅B全部类别加5：** B能量变为 −6.313262，概率及类别排名不变，但能量排序由 \(E_A<E_B\) 翻为 \(E_B<E_A\)。沿用原阈值时，B也被保留。此时若仍要保留A、拒绝B，须同时满足 \(t\ge-2.313262\) 与 \(t<-6.313262\)，无解。因此输入相关偏置不总能由一个全局阈值修复。

这些只是合成算术恒等式及反例，不证明真实模型表现，也不构成科研重跑的理由。

**A. 词库证据**
以下仅报告当前包内记录，本次未打开原始论文或网站。

| 证据层 | 当前记录及边界 |
|---|---|
| **词形对应** | 所读词库没有单独完成 `free energy／自由能` 的词形核验记录；不能用常见译法替包补证。 |
| **分类打分语境** | 已记录 `energy function／能量函数`、`energy score／能量分数`；该语境下 `free energy／自由能` 的精确中译仍明确标为未核验。 |
| **两篇英文运算定义** | P18 **EnergyMatch**，PDF第3页式(4)，称带温度的负log-sum-exp为 `free energy`；P51 **GWLSTM**，PDF第5页式(18)，称相应单位温度计算为 `energy function`。这是限定条件下的运算等价，不是两个短语各有两篇字面证据，也不认证P51存在疑点的完整阈值规则。 |
| **中文公式与译用** | 《电子学报》2026，54(1):153–166，第3.1节式(9)，刊页157–158／PDF第5–6页，记录logit“能量函数”；第4.3节、刊页162／PDF第10页记录分数用词。它不完成“自由能”的精确对应。作者网站中译版第2.2节、PDF第3页支持“能量分数”译用，但不是IEEE官方中文版或第二个独立方法定义。 |
| **正式审定标准** | 未见支持该精确对应的正式标准编号、现行状态与匹配定义记录。不能将官方组织网站托管的草稿升级为现行标准，也不能把导读当作中文期刊原始方法证据。 |

因此可保留精确英文，或写“由分类头logits计算的负log-sum-exp分数”。准入或译词记录缺失不等于禁止这种表达。

**B. 英文文本**
方法总览：**62词，恰好3句**，按空白分词。

ScoreRouteFD trains a temporal encoder and a known-class classification head on labeled training windows for fault discrimination. For each prediction window, logits from the same head determine the known-class candidate and yield an energy score computed as the negative log-sum-exp of the logits. Inputs with scores above a frozen threshold are labeled as unknown, whereas the remaining inputs retain their known-class candidates.

结果句：**28词，1句**。

Matched tests show better known-versus-unknown ranking AUROC, but more false rejections of known-class inputs at the frozen operating point, revealing a trade-off between ranking performance and thresholded decisions.

作者说明：此处取 \(T=1\)，阈值由独立校准集确定后冻结；阈值选定不是概率校准证明。最近前作的新颖性检索未完成，上述文字只交代既定路径，不将常规组合包装为新贡献。

**读取清单**
正文或相关段落实际读取如下；另做过包内关键词检索，检索命中不等于逐篇精读：
- [入口 SKILL.md](../../SKILL.md)
- [摘要／贡献 SKILL.md](../../skills/engineering-abstract-contributions/SKILL.md)、[实验 SKILL.md](../../skills/engineering-experiment-evidence-design/SKILL.md)
- [英文词库](../../references/engineering-application-terminology-bank.md)、[中文词库相关条目](../../references/engineering-application-terminology-bank_CN.md)
- [发表证据台账](../../references/published-evidence.md)、[实验证据指南](../../references/experiment-evidence-design.md)
- [摘要／贡献指南](../../references/abstract-and-contribution-craft.md)、[Topic指南](../../references/topic-playbooks.md)

本次未改文件、启动科研实验或调用代理；该虚构设计及其给定结果不能证明真实实验完成、实际部署或论文接收状态。
