依据当前 Skill **v4.1.15** 及相关共享参考作答。以下文献与中文来源均来自库内记录，未联网重查；未修改文件或运行实验。

**A. 保留模型，修正操作含义**
> Each sampling stream is encoded at its native sequence length, and a learned linear layer maps the encoded sequence to a common length \(T\). A contrastive training objective encourages agreement between representations of paired views of the same underlying stream, shaping the representations used by the fault classifier.

理由：长度投影改变的是**编码表示的尺寸**，对比目标约束的是**成对表示的关系**。二者都不等于恢复缺失测量或同步物理采样时刻；这里仅修正解释，不增加插补、同步或融合模块。

**B. 收紧贡献表述**
> We combine source-label cross-entropy with an MMD objective that encourages alignment of the pooled source and target feature distributions, training the encoder and fault classifier with labeled source samples and unlabeled target samples. At inference, diagnosis uses only the trained encoder and classifier.

这是**边缘特征分布层面的训练约束**，不是同类样本逐一匹配，也不能保证目标域故障可分。声明诊断获益前，最低限度需要：

1. 明确目标域训练数据与评估数据的使用边界，确保评估标签未参与训练、调参或模型选择，并披露是否使用了评估样本的无标签输入。
2. 在相同数据划分、骨干和训练预算下，与移除 MMD 的源域监督基线比较，隔离该目标的实际作用。
3. 检查目标域诊断指标、关键故障类别的错误及适当的重复运行波动，避免总体分数掩盖负迁移。MMD 降低不能替代诊断证据。

目前可保留上述方法性条目，但不能据此宣称已改善诊断；创新性还需最相关方法的差异依据。

**C. 不应一概删除**
两个术语都有明确操作依据，应保留并解释其对象和准则，而不是因为 `alignment` 多义就删除。

**Design 1：**共享触发和已标定延迟补偿支持采集层面的 temporal synchronization，但不能额外声称零残余误差。
> Video frames and current measurements are temporally synchronized using a shared acquisition trigger and compensation for a calibrated 2 ms sensor delay before multimodal samples are constructed.

**Design 2：**两域已观测训练标签与逐类 MMD 支持 class-conditional distribution alignment。这不是无监督目标域学习，也不意味着同类样本逐一配对。
> Using observed training labels in both domains, class-conditional distribution alignment minimizes a separate MMD term for each corresponding fault class, while held-out target labels are reserved for evaluation.

**D. 数学判断**
原句错误。互信息取决于联合分布，而不只取决于两个边缘分布：
\[
I(X;Y)=\sum_{x,y}p(x,y)\ln\frac{p(x,y)}{p_X(x)p_Y(y)}.
\]

- **独立：**四种组合均有概率 \(1/4\)，故 \(I(X;Y)=4(1/4)\ln 1=0\)。
- **\(Y=X\)：**仅 \((0,0)\)、\((1,1)\) 各有概率 \(1/2\)，故 \(I(X;Y)=2(1/2)\ln 2=\ln 2\approx0.6931\ \text{nats}\)。

两种情形的边缘分布都相同，所以总体层面的 \(\mathrm{MMD}(P_X,P_Y)=0\)，但配对依赖不同。

> Identical Bernoulli(1/2) marginals yield zero population MMD in both cases, whereas the mutual information is zero under independence and \(\ln 2\) when \(Y=X\).

工业表征中的边缘分布匹配，因此不能单独证明成对信息保留、互信息相等或故障语义一致。这一反例不否定比较**联合分布与边缘分布乘积**的依赖度量；关键是检查实际比较对象。

**E. 通用名称准入**
按当前[术语库准入规则](../../references/engineering-application-terminology-bank.md)，通用名称需要至少两篇不同论文中对象与操作相符的实质依据，中文译名另行核验。以下页码均为库内记录的 **PDF 页序**。

**distribution alignment / 分布对齐：可以在已核验范围内纳入。**

- **P10：[A Local-Global Domain Adaptation Framework for Industrial Fault Diagnosis Under Variable Operating Conditions](https://doi.org/10.1109/TSMC.2026.3704330)**，pp.5–6，Eqs.(15)–(17)：通过训练目标约束源域与目标域特征分布差异。
- **P44：[A Multisource Domain Adaptation Network for Process Fault Diagnosis Under Different Working Conditions](https://doi.org/10.1109/TIE.2022.3194654)**，pp.4–5，Eqs.(12)–(15)：采用域对抗与类别加权分布目标。两篇支持共同的分布匹配目的，但监督条件、准则及预测路径不同。
- **可靠中文来源：**库内已核验[《自动化学报》c250653 的双语摘要](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c250653?viewType=HTML)，对应缺失变量条件下 KPI 预测的表征分布约束，支持“分布对齐”。它不为时间同步、逐样本匹配或故障语义保持背书。

**maximum mean discrepancy (MMD) / 最大均值差异：可以作为基础差异度量纳入。**

- **P10**，p.5，Eq.(15)：定义源域与目标域特征的核均值嵌入差异。
- **P32：[Diff-MTS: Temporal-Augmented Conditional Diffusion-Based AIGC for Industrial Time Series Toward the Large Model Era](https://doi.org/10.1109/TCYB.2024.3462500)**，p.4，Eqs.(10)–(11)：在扩散训练中比较采样噪声与预测噪声的核分布差异。两篇的比较对象与损失作用不同。
- **可靠中文来源：**库内已核验[《自动化学报》c190593 的双语摘要](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c190593?viewType=HTML)，在轴承故障检测语境中支持“最大均值差异”。P44 引言中的 MMD 提及不计作操作定义；这些记录也不使完整 Ada-MMD 名称自动准入，更不证明 MMD 等价于互信息。

**Dual-domain Causal Alignment Gate：不能据单篇定义升级为通用推荐名称。**可保留为有明确来源归属的论文专名；完整名称中的 `Causal` 等限定词不能借基础词 `alignment` 的准入获得认可。这不是判定该名称无效。

**Production Event Alignment Unit：保留为作者提出的组件名称。**既然已有明确操作定义，应在首次出现时说明是本文提出的组件，并在该项目内保持名称、定义和图文一致。新组件不需要先有两篇同名论文，但其名称不能直接进入“已确立的通用推荐名称”类别，也不自动证明创新性或诊断效果。**库中未收录只表示没有完成该库的准入记录，不表示术语无效。**
