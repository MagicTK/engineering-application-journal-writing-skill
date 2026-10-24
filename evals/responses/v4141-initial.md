# Fictional Fuzzy-Rule Initial Response

The initial frozen source passed the three core checks. A historical source-count sentence was then corrected, the snapshot refrozen and the same requests retested. This is a metadata repair, not a scientific-answer failure. Raw responses remain private; wrapper and whitespace only are normalized.

说明：上下文已预置历史摘要，不能称为记忆空白或完全追踪审计。本次仅主动读取指定 Skill、相关当前引用及必需引导；A–C 是同一上下文中的三个请求。字数按空白分词，连字符复合词计一词。

**M4141-A**
原始规则激活：
\[
a_1=0.5\times0.4=0.2,\qquad a_2=0.6\times0.5=0.3.
\]

归一化规则权重：
\[
w_1=\frac{0.2}{0.5}=0.4,\qquad w_2=\frac{0.3}{0.5}=0.6.
\]

局部输出及最终质量估计：
\[
f_1(2)=5,\quad f_2(2)=2,\qquad
\hat y=0.4\times5+0.6\times2=\boxed{3.2}.
\]

英文方法句，30 词：

> Within each rule, antecedent membership degrees are multiplied to obtain its activation. Normalizing these activations across rules yields rule weights that combine local regression outputs into the final quality estimate.

作者备注：输入隶属值**不必彼此加和为 1**，除非另行规定这样的隶属分区约束。归一化得到的 `[0.4, 0.6]` 可以准确称为规则权重，但不因此成为两个故障类别的概率；最终的 `3.2` 是数值质量估计，不是故障类别。

**M4141-B**
实际先加权类别分数：
\[
\mathbf s=0.4[-2,1]+0.6[1,0]=[-0.2,0.4].
\]
再沿类别轴执行 softmax：
\[
\mathbf p=\frac{[e^{-0.2},e^{0.4}]}{e^{-0.2}+e^{0.4}}
=\boxed{[0.354344,\ 0.645656]}.
\]

另一顺序分别得到：
\[
\operatorname{softmax}([-2,1])=[0.047426,\ 0.952574],
\]
\[
\operatorname{softmax}([1,0])=[0.731059,\ 0.268941].
\]
再加权概率：
\[
\tilde{\mathbf p}=\boxed{[0.457605,\ 0.542395]}\ne\mathbf p.
\]

英文方法说明，29 词：

> Normalized rule weights combine the local class score vectors into an aggregated score vector. A softmax across classes then converts these aggregated scores into the predicted class probability vector.

核查备注：实际 softmax 输出可以合法称为**预测类别概率向量**，但未据此证明概率已经校准。规则激活、归一化规则权重与类别概率是不同对象；上述两种计算顺序不等价。

**M4141-C**
摘要的方法与结果部分，124 词：

> A shared encoder maps process measurements to latent features. Gaussian membership functions evaluate input matching in this learned feature space, and products of membership degrees yield rule activations. Normalizing these activations across rules provides weights that combine constant rule outputs into a quality estimate. The encoder, membership parameters, and rule outputs are learned from data. During training, paired temporally perturbed views preserve the quality label, and a consistency constraint encourages agreement between the corresponding rule activations. This constraint jointly shapes the shared encoder and rule head toward stable rule responses. The trained predictor estimates quality using fixed parameters. On held-out conditions fixed in advance, it yields lower average quality prediction error than the comparison methods, but its error is higher under extreme operating conditions.

整体贡献候选，33 词：

> We formulate a training constraint that aligns rule activations across label-preserving temporal perturbations, jointly shaping a shared encoder and learned rule head whose normalized activations weight constant rule outputs for industrial quality prediction.

作者核查点：
- 对比最近相关前作，确认该训练约束及其联合学习关系的实质差异；目前仅为贡献候选，高斯函数名称本身不构成创新。
- 在公式中明确一致性约束使用原始还是归一化规则激活，以及具体损失形式；不将其改写为最终特征融合。
- 规则来自数据学习，潜在坐标没有已验证的物理含义。现有证据不支持统计显著性、现场部署或解释性已验证的声明，也不支持把平均误差优势外推为普遍优势。
