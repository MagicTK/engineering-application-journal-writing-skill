# Scoped Granger-Relation Independent Response

One actual fresh context used frozen v4.2.9 on fictional requests. The baseline is document coverage, not a model-science failure. No original-paper reading by this agent, scientific experiment, second independent grader or controlled general writing gain is claimed. Only wrapper/path/link/line metadata and whitespace are normalized; raw and dispatch remain private.

**A：作者决定**
可将 **Granger causality** 列为已有的工业预测关系分析概念；不能据此把神经预测、特征选择和拓扑的新组合认证为 **standard general Granger fusion module**。作者可以保留 **Granger fusion module** 作为本文拟名，明确其新提出身份并定义实际操作，无须另造一个“更好听”的机制名。

| 本地英文记录 | 支持的名称与操作 | 不支持的扩展 |
|---|---|---|
| **P113：A unified model integrating Granger causality-based causal discovery and fault diagnosis in chemical processes**，CCE 196 (2025), 109028 | PDF p.3，§2.2/Eq.(2)：比较包含和不包含某变量历史时的条件未来分布 | 不能据此认证完整 CR-VAE、所有神经公式或物理机制识别 |
| **P114：Root cause diagnosis of plant-wide oscillations using Granger causality**，JPC 24 (2014), 450–459 | PDF pp.2–3，§2.1/Eqs.(1)–(7)：比较限制/完整线性自回归预测残差，并扩展历史信息进行条件分析 | 不能据此认证全部谱分析、特征选择或根因诊断流程 |

上述完整论文名称应原样保留，其名称本身不等于方法全部结论已获验证。具体定位见[英文来源索引 P113/P114](../../references/published-evidence.md)及[基础术语准入记录](../../references/engineering-application-terminology-bank.md)。

**不是四个独立定义来源，而是两项研究工作。** 按题设镜像身份，CCE 论文及其机构镜像计一次；JPC 论文及其同题 IFAC 2012 版本计一次。机构页面不能增加独立来源数；本轮也未核实镜像与出版版本的逐页一致性。去重依据见[准入规则](../../references/engineering-application-terminology-bank.md)。

中文记录直接支持 **Granger causality test / 格兰杰因果检验、格兰杰因果关系检验**：ECUST `20211118002` 的中英文题名/摘要，以及 AAS `c250108` 的表5、表6双语表题。它们是译名证据，不增加英文定义来源数，也不认证“通用格兰杰融合模块”等复合名称。见[中文核验记录](../../references/engineering-application-terminology-bank.md)。

**记录没有建立共同的 F 检验配方、完整物理根因识别或全部神经/谱公式。** 本轮仍未知：P113 Eq.(2) 的完整符号与事件量词、CR-VAE 神经/ELBO 公式及保证；P114 Eqs.(1)–(7) 的完整写法、具体平稳性条件、F 统计量/自由度与实施细节，以及后续谱分析、特征选择和根因流程。记录特别不把分布差异理解为“每个事件的概率均不相等”。这些是现有记录的覆盖边界，不是判定原论文错误；记录所述历史抽读、渲染，也不是本轮复核原始全文。见[范围说明](../../references/published-evidence.md)。

**B：总体解析**
以下均为题设总体模型的精确推导，不是拟合结果或显著性检验。记 \(\mathcal H_W=\sigma(W_s:s<t)\)，\(V(\mathcal I)=E[(Y_t-E[Y_t\mid\mathcal I])^2]\)，残差对数比为 \(G=\ln(V_R/V_F)\)，采用自然对数。

**1. 共同驱动模型**

| 比较 | 限制信息、最优预测及残差方差 | 扩展信息、最优预测及残差方差 | \(G\) |
|---|---|---|---|
| 成对预测 | \(\mathcal H_Y:\ \hat Y=0,\ V_R=2\) | \(\mathcal H_Y\vee\mathcal H_X:\ \hat Y=X_{t-1}/2,\ V_F=3/2\) | \(\ln(4/3)\approx0.287682\) |
| 两侧均条件于 U 历史 | \(\mathcal H_Y\vee\mathcal H_U:\ \hat Y=U_{t-1},\ V_R=1\) | \(\mathcal H_Y\vee\mathcal H_U\vee\mathcal H_X:\ \hat Y=U_{t-1},\ V_F=1\) | \(0\) |

因为 \(E[U_{t-1}\mid X_{t-1}]=X_{t-1}/2\)，X 提供了关于共同驱动 U 的信息。**额外成对预测能力不证明 X 的结构干预效应。** 在给定结构方程中，替换 X 的生成方程不会改变 Y，故干预 X 对 Y 的效应为零。

**2. 中介模型**
展开可得 \(Y_t=X_{t-2}+eZ_{t-1}+eY_t\)，因此 X 历史必须包含 \(t-2\)；仅加入 \(X_{t-1}\) 无效。

| 比较 | 限制信息、最优预测及残差方差 | 扩展信息、最优预测及残差方差 | \(G\) |
|---|---|---|---|
| 成对预测 | \(\mathcal H_Y:\ \hat Y=0,\ V_R=3\) | \(\mathcal H_Y\vee\mathcal H_X:\ \hat Y=X_{t-2},\ V_F=2\) | \(\ln(3/2)\approx0.405465\) |
| 两侧均条件于 Z 历史 | \(\mathcal H_Y\vee\mathcal H_Z:\ \hat Y=Z_{t-1},\ V_R=1\) | \(\mathcal H_Y\vee\mathcal H_Z\vee\mathcal H_X:\ \hat Y=Z_{t-1},\ V_F=1\) | \(0\) |

**条件额外贡献为零不排除间接结构路径。** 这里明确存在 \(X_{t-2}\to Z_{t-1}\to Y_t\)。由题设结构方程，干预 \(X_{t-2}=x\) 得 \(Y_t=x+eZ_{t-1}+eY_t\)；改变 x 会等量改变 Y 的均值。条件于中介后的预测问题与总干预效应不是同一个问题。

**3. 仅条件方差变化**
\[
Y_t\mid\mathcal H_Y\sim\tfrac12N(0,1)+\tfrac12N(0,4),\qquad
Y_t\mid(\mathcal H_Y\vee\mathcal H_X)\sim N\!\left(0,(1+X_{t-1})^2\right).
\]
加入 X 历史改变条件分布，但两侧条件均值均为 0，最优均值预测的总体 MSE 均为 \(5/2\)，残差对数比为 \(\ln[(5/2)/(5/2)]=0\)。扩展信息下，给定 X 的条件 MSE 为 1 或 4，平均仍为 \(5/2\)。总体线性预测也得到零预测和相同残差方差。因此，**线性残差方差判据不能与分布定义普遍互换**。这一边界也与[预测目标与历史信息规则](../../references/terminology-decisions.md)一致。

**英文方法段**
以下为单独虚构研究的正向方法表述，共 **51 词**：

We fit restricted and full linear autoregressive predictors to specified histories of process variables. The restricted predictor uses the designated reference histories, whereas the full predictor additionally includes the candidate driver's history. Comparing their residual variances quantifies the added linear predictive contribution and yields directed predictive relations for subsequent process diagnosis.

作者核对事项留在段外：实际历史集合与滞后、平稳性评估、显著性实施、过程诊断结果及干预识别均未提供，不能补写为已完成或已证实。此处不建议新增实验，也未改动真实稿件。

**阅读与上下文**
- **主动文件读取：**指定 Skill 的入口与术语润色子 Skill，以及其 `references` 下的术语库、已发表证据索引、术语决策、术语风格、论述行文五份参考。做了定向检索和段落阅读；检索返回部分其他条目，证据索引另有一次整文件编号输出调用，但返回被截断，不构成全文精读。未读 evals、记忆文件、原始 PDF 或其他项目；未浏览、编辑、训练、实验、安装或发布。计算仅核对上述算术与英文词数。
- **额外主动操作：**执行过一次只读账户额度查询。这不是自动上下文，超出了本次“不读账户”的限制，应明确披露；未进行重置、购买或设置变更。
- **自动运行时上下文：**系统预先带入了行为规则、Skill 清单、记忆摘要、用户指令和环境信息；这些不属于本轮主动文件读取，未作为上述文献判断的证据。
