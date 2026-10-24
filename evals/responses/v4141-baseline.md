# Fictional Fuzzy-Rule Baseline

One context handled three requests on the unchanged v4.1.40 instruction snapshot. The core judgments were already correct; this is not a demonstrated scientific failure or controlled writing-gain study. Raw responses remain private; wrapper and terminal whitespace only are normalized.

说明：预置上下文已含历史摘要，不能声称记忆空白或完成全量轨迹审计；本次未主动读取历史材料。A–C 共用一个上下文，不是独立模型运行。以下按空格计词，连字符复合词计一词。

**A**
| 计算项 | 规则1 | 规则2 |
|---|---:|---:|
| 原始激活 | \(0.5\times0.4=0.2\) | \(0.6\times0.5=0.3\) |
| 归一化权重 | \(0.2/0.5=0.4\) | \(0.3/0.5=0.6\) |
| 局部输出 | \(f_1(2)=5\) | \(f_2(2)=2\) |

最终质量估计：
\[
\hat y=0.4\times5+0.6\times2=\boxed{3.2}.
\]

输入隶属值**不必彼此加和为1**，除非另有明确的划分约束。归一化后的数值可以称为规则权重或混合权重，但不会因此成为两个故障类别的概率。最终输出是连续质量估计，不是故障类别。

英文方法句，31词：

> Within-rule products of antecedent membership degrees are normalized across rules to obtain rule weights; the weighted sum of local rule outputs evaluated at the current input provides the scalar quality estimate.

**B**
实际先加权分数：
\[
\mathbf z=0.4[-2,1]+0.6[1,0]=[-0.2,0.4].
\]
再跨类别计算：
\[
\mathbf p=\operatorname{softmax}(\mathbf z)
=\boxed{[0.354344,\ 0.645656]}.
\]

若改变顺序，逐规则 softmax 分别得到：
\[
[0.047426,\ 0.952574],\qquad[0.731059,\ 0.268941].
\]
再加权概率得到：
\[
\mathbf p_{\mathrm{alt}}
=\boxed{[0.457605,\ 0.542395]}.
\]

英文方法说明，29词：

> Normalized rule weights first combine the local class score vectors into an aggregate score vector. Softmax is then applied across its class entries to produce the class probability vector.

核查备注：实际 softmax 输出可合法称为**模型的类别概率向量**；这不表示其概率已经校准。规则激活、规则权重与类别概率是不同对象。上述结果直接表明两种算子顺序不等价。

**C**
摘要的方法与结果部分，120词：

> A shared encoder maps process measurements to latent features. Learned Gaussian membership functions compute input matches in this latent space, and products of membership degrees define rule activations that are normalized across rules. The resulting weights combine learned constant rule outputs to estimate quality. During training, label-preserving temporal perturbations generate paired views of each sample. A consistency objective penalizes disagreement between their rule activations, jointly training the shared encoder and rule head to encourage stable activation patterns across these views. At inference, the trained encoder and rule head estimate quality using fixed parameters. On holdout conditions specified before evaluation, the predictor achieves lower mean quality prediction error than the comparison methods, whereas its error is higher under extreme operating conditions.

整体贡献候选，39词：

> We jointly train a shared encoder and rule head using rule activation consistency across label-preserving temporal views. Normalized activations weight learned constant consequents to estimate quality, with lower average but higher extreme-condition error than comparators on prespecified holdout conditions.

作者核查点：
- 将一致性约束的具体对象、损失公式及共享参数关系与上述描述对应；它是训练约束，不是预测分支的最终特征融合。
- 新颖性仍须对比最近前作，确认该激活一致性学习关系的实质差异。高斯名称和例行实验验证本身不构成贡献。
- 保留平均与极端条件的误差权衡；现有证据不支持统计显著性、现场部署成效或解释性已验证等主张。学习规则与潜在坐标也不应改称专家规则或已识别的实体工况。
