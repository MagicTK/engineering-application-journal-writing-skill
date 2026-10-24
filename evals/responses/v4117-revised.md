以下“已核实”均指 **Skill 4.1.17 的既有记录**；本次只读取 Skill 及相关参考文件，未访问原始论文或外部服务。

**A**
依据：[术语库 §11](../../references/engineering-application-terminology-bank.md)及[已发表证据“不确定性对象与决策”节](../../references/published-evidence.md)。

| 名称 | 当前记录支持的英文含义 | 中文核验状态 |
|---|---|---|
| `energy function` | 分类器 logits 的负 log-sum-exp 函数；P51 为单位温度形式 | **能量函数**：已有匹配语境的核验 |
| `energy score` | 由这类计算得到、用于评分的标量；不是另一个独立机制 | **能量分数**：已有核验 |
| `free energy` | P18 对带温度缩放的负 log-sum-exp 量的名称 | **自由能**：在此分类器语境中的译法尚未核实 |

两篇英文定义来源：
- **P18：[EnergyMatch](https://doi.org/10.1016/j.ress.2025.112013)**，PDF 第3页，式(4)：定义上述带温度缩放的量，名称为 `free energy`，用于其域学习相关操作。
- **P51：[GWLSTM](https://doi.org/10.1109/TSMC.2026.3703212)**，PDF 第5页，式(18)：将对应的单位温度计算称为 `energy function`，用于开集决策。两者是在所述 logit 约定下的计算对应，不是三种名称分别获得了两篇逐字定义。

中文来源的身份与已读位置：
- **[《电子学报》2026，54(1):153–166](https://www.ejournal.org.cn/zh/article/doi/10.12263/DZXB.20250761/)**：中文期刊来源。记录已读 §3.1、式(9)，印刷页157–158／PDF第5–6页，以及 §4.3，印刷页162／PDF第10页；支持匹配的 logit 函数定义和“能量分数”用语。
- **[Class-Specific Semantic Reconstruction for Open Set Recognition 作者托管中译版](https://mftp.mmcheng.net/Papers/22PAMI-OpenSet-cn.pdf)**：记录已读 §2.2、PDF第3页，使用“能量分数”讨论 OOD 评分。它由作者发表列表链接，**不是 IEEE 官方中文版，也不是第二个独立机制定义**。

**术语决定：**函数称“能量函数”，其输出称“能量分数”；引用 P18 时保留其 `free energy` 名称，不宣称“自由能”已在此语境核实。物理振动能量与分类器 logit 评分的对象、运算不同，不能凑作匹配机制证据；同一工作的译本也不能重复计数。“能量值就是未知故障概率”没有依据，应删除。Skill 还记录了 P51 的符号与阈值疑点，不能直接照搬其完整判决规则。

按已记录的单位温度形式，可写：
:::writing{variant="standard" id="71831"}
We compute an energy score as the negative log-sum-exp of the classifier logits.
:::

**B**
应按运算分别命名，不能统一叫“残差连接”：

| 对象或操作 | 建议中文名称 |
|---|---|
| 尾随移动平均 \(m(t)\) 与 \(r(t)=x(t)-m(t)\) | 尾随移动平均分量；减去该均值后的信号余项 |
| \(u=h+F(h)\) | 加法残差连接，包含恒等直连路径 |
| 将 \(u\) 与单独编码的 \(m(t)\) 拼接 | 特征拼接；不是残差连接 |
| 报告统计量 \(e=y-\hat y\) | 预测残差，或按该符号约定定义的预测误差 |

这些计算事实不证明“去除噪声”或“泛化能力”；移动平均余项也不能直接等同于噪声。当前没有相应评估依据，应去掉这些效果断言。

[术语库 §11](../../references/engineering-application-terminology-bank.md)记录的两项中文核验为：
- **[《煤炭科学技术》2025，53(2):96–108](https://mtkxjs.com.cn/cn/article/pdf/preview/10.12438/cst.2024-1441.pdf)**：§1.3及双语图3，印刷第99页／PDF第5页，明确对应 `residual connection / 残差连接`。
- **[《农业工程学报》2026，42(7):1–11](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.202505227.pdf)**：§2.1，第4页，明确对应上述术语，并描述先前输入与后续特征相加。

它们支持网络连接的基础译法，不支持把信号余项、拼接或预测误差都改称残差连接。

:::writing{variant="standard" id="71832"}
We subtract the trailing moving average \(m(t)\) from \(x(t)\) to obtain \(r(t)\), which is encoded as \(h\). We then compute \(u=h+F(h)\) through an additive residual connection and concatenate \(u\) with a separate encoding of \(m(t)\) for classification. The prediction residual \(e=y-\hat{y}\) is reported separately.
:::

**C**
依据[术语库 §0“Admit Names, Not Search Counts”](../../references/engineering-application-terminology-bank.md)：

- **稿内可以保留 `Elapsed-Interval Gate`。** 明确它是本文定义的组件，并写清输入、输出和乘法作用即可，不要求新组件先有两篇同名论文。但已有同名先例，因此不能仅凭命名宣称首创；若继承该先例，应注明出处，若不同，应说明区别。当前未提供先例正文，无法核实机制是否相同。
- **完整名称目前不应进入“已确立机制家族”的共享术语库。** 一篇同名论文不足以完成多来源准入；另外两篇没有经过时间输入，只能支持一般门控操作，不能验证完整的时间限定名称。该名称可保留在项目术语表中。
- **不建议译为“年龄门控”。** 输入是距测量发生的已过时间，不是人的年龄或设备老化程度。保留英文名称，中文描述为“依据测量后的已过时间，对各测量编码进行乘法加权的门控机制”。Skill 已核验基础译法“门控机制”，但没有核验这个完整名称的中文标准译法。

:::writing{variant="standard" id="71833"}
The Elapsed-Interval Gate uses the time elapsed since each sensor measurement to produce one multiplicative weight for its encoded representation.
:::
