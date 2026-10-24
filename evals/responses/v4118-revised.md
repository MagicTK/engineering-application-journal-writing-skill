# 4.1.18 Fictional-Case Response

One fresh responding context used only the candidate Skill and the three author requests. The response is retained below; 6 local source-link targets were normalized to repository-relative links and line suffixes removed. No substantive answer text was changed. This is response evidence, not an independent grading verdict.

以下仅依据指定 Skill 及其参考文件的现有记录，未重新查阅论文原文或网页。

**A. 名称准入**
**证据不足，不能将完整名称作为通用模块家族入库，也不应统一改名其他融合模块。**

- 八次出现仍是一篇工作的证据；预印本、期刊版及作者中译版不能算作三个独立工作。中译版至多另作译名核对材料。
- 另两篇定义普通特征融合，不能自动支持带有 **High-Order** 限定的完整名称。通用名称至少需要两篇不同已发表工程／应用期刊论文，在对象与运算上提供匹配定义；有争议时宜有三至五篇。
- **可以保留两类命名**：综述原论文时，明确归属并保留其组件名称；作者也可以为真正新设计、已定义输入输出和运算的组件提出名称，但应标明是本文提出，在本项目中维护，不能直接作为公认家族入库。允许命名本身不等于新颖性已经得到证明。

依据：[术语库 §0，名称状态与去重规则](../../references/engineering-application-terminology-bank.md)。

**B. 措辞诊断**
第一处是**通过拼接进行特征融合**，对象为 \(u,v\)，输出 \(z\) 供两个分类头共同使用。第二处是**固定权重的预测融合／概率加权平均**，对象为 \(p,q\)，不是隐特征。

两处均无依据称为 *adaptive*：拼接规则和组合权重固定，输出随输入变化并不意味着组合机制自适应。“aggregation 必须降维，而 fusion 不降维”也不成立；维度变化取决于具体运算及作用轴，不能由名称决定。依据：[自适应的判断](../../references/terminology-decisions.md)、[组合层级与运算区别](../../references/terminology-decisions.md)。

方法表述，三句：

:::writing{variant="standard" id="73104"}
The two measurement streams are encoded as \(u\) and \(v\) and fused by concatenation to form \(z=[u;v]\). Two separate classifier heads take this shared representation as input and produce class-probability vectors \(p\) and \(q\), respectively. These predictions are combined using the fixed weighted average \(r=0.4p+0.6q\) for the final classification.
:::

贡献表述，一句，仅陈述设计，不声称性能提升或已证实的新颖性：

:::writing{variant="standard" id="73105"}
We present an industrial classification architecture that combines two measurement-stream representations by concatenation and integrates the predictions of two classifier heads using fixed weights.
:::

**C. 已有证据**
**Feature fusion 可以作为基础通用术语使用**，指在明确层级上组合特征来源；它并不指定唯一运算。Skill 已记录以下方法定义，页码均为 **PDF 文件页序**：

| 论文 | 方法位置 | 实际组合对象及运算 |
|---|---|---|
| P01，*Feature hybrid fusion-based fault diagnosis of multi-scale and multi-stage industrial processes* | pp.4–5，§3.4，式(7)–(10) | 组合各阶段特征，分别利用拓扑矩阵与相似性矩阵形成组合结果，再将两路输出相加；此前的阶段内池化是另一操作。 |
| P03，*A Temporal-aware Dual-attention Network for Fault Diagnosis in Industrial Processes* | pp.4–5，§2.3.2，式(17) | 对两种注意力产生的特征表示进行学习权重控制的加权相加。 |
| P14，*A Knowledge-Data Integrated Graph Convolutional Network for Fault Diagnosis in Industrial Processes* | p.4，§III-D4，式(35) | 拼接多尺度卷积输出，送入后续分类器；式(28)的块对角邻接矩阵组装不是这里的特征融合。 |

这是三个不同工作，其中 P01/P03 有共同团队背景；支持基础名称，不证明全领域普遍性或三者机制相同。记录位置：[术语库的 feature fusion 条目](../../references/engineering-application-terminology-bank.md)。

中文“**特征融合**”已有独立译名核对记录：**《自动化学报》c190428，DOI 10.16383/j.aas.c190428 的中英文摘要及关键词**。其图像重建语境支持英汉对应，不是新增的流程工业方法证据。见[中文核对条目](../../references/engineering-application-terminology-bank.md)。

关于 EHOPN：
- **能确认**：P02 的 p.5、§3.3.2、式(31)，把一阶与二阶池化特征的加权组合称为 *high-order feature aggregation*。
- **存在未解决的不一致**：文字把某一输入称为 max pooling，而式(28)定义的是平均运算。当前记录未核验实现，不能确认作者实际采用最大值还是平均值，也不能自行判定哪处应改。
- 因此，学生不能仅凭该文字把 max pooling 当作已确认的忠实实现；需要代码、勘误或作者澄清。同时，部分 aggregation 与 fusion 都使用加权组合，只说明用法有重叠，**不能推出完整名称等价，更不能推出所有 feature fusion 都是同一机制**。

上述依据及限制均见[特征组合核对记录](../../references/published-evidence.md)。
