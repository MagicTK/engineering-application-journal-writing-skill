# Fictional Energy-Convention And Wording Final Response

One new task context answered the unchanged A/B request on the final frozen source. Baseline science and writing already pass; only the read root changes. Public normalization changes wrappers, local links/line suffixes and whitespace; exact raw records remain private.

预置上下文含该包的历史摘要，本次未将其作为证据。以下仅依据本轮读取的包内记录；未浏览外链、修改文件或启动科研实验，不构成整库认证。

**A. 算术审查**
原始两个样本的 softmax 都是：
\[
(p_1,p_2)=\left(\frac{e}{e+1},\frac1{e+1}\right)\approx(0.731059,0.268941).
\]
两者的已知类候选均为类别1；拒识结果如下：

| 情形 | 阈值 \(t\) | \(E(A)\) | \(E(B)\) | A决策 | B决策 |
|---|---:|---:|---:|---|---|
| 原始 | −1.8 | −2.313262 | −1.313262 | 保留类别1 | 拒为未知 |
| 所有 logits 加3，阈值减3 | −4.8 | −5.313262 | −4.313262 | 保留类别1 | 拒为未知 |
| 仅B的 logits 加5 | −1.8 | −2.313262 | −6.313262 | 保留类别1 | 保留类别1，漏拒 |

因为
\[
p(z+a\mathbf1)=p(z),\qquad E(z+a\mathbf1)=E(z)-a,
\]
全局统一加3并同步移动阈值，**类别概率、类别排序、跨样本能量排序及拒识决策全部不变**。

仅B加5时，类别概率和类别排序仍不变，但能量排序从 \(E(B)>E(A)\) 翻为 \(E(B)<E(A)\)。本例甚至不能用另一个全局阈值恢复“A保留、B拒识”：前者要求 \(t\ge E(A)\)，后者要求 \(t<E(B)\)，两条件矛盾。

这些只是给定合成输入的计算与恒等式，不是真实模型表现；等价平移本身不要求科研重跑，输入相关偏置也不能保证由一个全局阈值补偿。

**当前译词记录**
下面报告的是**包内已有记录**，不是本轮重新核验外部原文的结论。

| 证据层 | 本轮实际读到的记录及边界 |
|---|---|
| 词形 | 中国物理学会名词委员会参考词表，PDF第1、72、83页，记录 `free energy / 自由能` 及Helmholtz限定词；封面为**2010年3月修订初稿**。 |
| 分类打分语境 | CCF多媒体专委会论文导读第04项方法段使用 `Energy（Helmholtz自由能）` 描述分类器OOD评分。这是有限语境用例，**不是中文期刊原始方法定义**。 |
| 两篇英文运算定义 | P18《EnergyMatch》p.3式(4)称带温度的负log-sum-exp为 `free energy`；P51《GWLSTM》p.5式(18)称单位温度对应计算为 `energy function`。支持限定运算对应，不是两个完全相同的名称或用途。 |
| 中文独立公式 | 《电子学报》2026,54(1):153–166，第3.1节式(9)记录logit能量函数，第4.3节使用能量分数；这支持 `能量函数/能量分数`，**不直接确立分类打分中 `free energy / 自由能` 的精确对应**。作者网站中译版第2.2节使用“能量分数”，但不是第二个独立方法定义，也不是IEEE官方中文版。 |
| 正式审定标准 | 所读记录未提供现行正式审定标准依据。官方组织或期刊网站托管的修订草稿，不能因域名权威而升级为现行标准。 |

因此，不能说“自由能完全没有记录”，也不能说“已有两篇中文独立公式及正式标准认证”。基础分数记录亦不认证P51仍有疑点的完整阈值规则。准入或译词记录缺失，不禁止使用精确英文或准确的功能描述。

**B. 可复用英文**
方法总览：**恰好3句，66词**。按空白分词，连字符复合词计一词。

ScoreRouteFD trains a temporal encoder and a classifier head on labeled training windows to distinguish known fault classes. At prediction time, logits from the same head provide a known-class candidate and an energy score computed as the negative log-sum-exp of those logits. A frozen threshold determines the final output: samples with scores above the threshold are labeled unknown, whereas all remaining samples retain their known-class candidates.

结果句：**1句，34词**，采用同一计词方式。

Matched tests showed that ScoreRouteFD achieved higher AUROC for distinguishing unknown from known samples, but falsely rejected more known-class samples at the frozen operating point, exposing a trade-off between ranking performance and known-class retention.

中文说明：阈值由独立校准集确定后冻结，常规选择细节留在实验设置中；这不等于概率校准。最近前作的新颖性检索未完成，上述文字仅描述既定路径与给定权衡，不将常规组合宣称为新贡献。

**实际读取文件**
正文或相关选段：
- [SKILL.md](../../SKILL.md)
- [术语库英文版](../../references/engineering-application-terminology-bank.md)、[中文版](../../references/engineering-application-terminology-bank_CN.md)
- [published-evidence.md](../../references/published-evidence.md)
- [experiment-evidence-design.md](../../references/experiment-evidence-design.md)
- [摘要与贡献技能入口](../../skills/engineering-abstract-contributions/SKILL.md)、[abstract-and-contribution-craft.md](../../references/abstract-and-contribution-craft.md)
- [terminology-decisions.md](../../references/terminology-decisions.md)、[topic-playbooks.md](../../references/topic-playbooks.md)

另仅读取关键词命中行，未逐篇通读：
- [industrial-ai-taxonomy.md](../../references/industrial-ai-taxonomy.md)、[corpus-calibration-workflow.md](../../references/corpus-calibration-workflow.md)、[experiment-execution.md](../../references/experiment-execution.md)
- [abstract-and-contribution-craft_CN.md](../../references/abstract-and-contribution-craft_CN.md)、[terminology-decisions_CN.md](../../references/terminology-decisions_CN.md)、[terminology-and-style.md](../../references/terminology-and-style.md)
- [astra-editable-figure-pipeline.md](../../references/astra-editable-figure-pipeline.md)、[research-ideation入口](../../skills/engineering-research-ideation/SKILL.md)、[review-response入口](../../skills/engineering-review-response/SKILL.md)
- [rigor-review入口](../../skills/engineering-journal-rigor-review/SKILL.md)、[experiment-evidence-design入口](../../skills/engineering-experiment-evidence-design/SKILL.md)、[paper-router入口](../../skills/industrial-ai-paper-router/SKILL.md)

虚构设计、给定结果设定和上述算术，均不能证明真实实验已经完成、实际部署有效或论文已获接收。
