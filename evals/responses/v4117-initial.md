以下“已核实”均指 **Skill v4.1.17 已记录的核查结果**，不是本轮重新查阅原文。依据为[术语库 §0、§11](../../references/engineering-application-terminology-bank.md)及[已发表证据中的“不确定性对象与决策”](../../references/published-evidence.md)。

**A**
**术语决定：三种称呼不能直接当作三个不同机制，也不能脱离计算定义互换。**

| 术语 | Skill 已记录的英文含义 | 中文核实状态 |
|---|---|---|
| `energy function` | P51 将单位温度下、由分类器 logits 计算的负 log-sum-exp 称为能量函数 | **能量函数**已核实 |
| `energy score` | 上述分类器能量量作为评分使用；不是另一种已独立核实的计算机制 | **能量分数**已核实 |
| `free energy` | P18 对温度缩放负 log-sum-exp 的原文称呼；在记录所述 logit 约定下，与前述单位温度计算对应 | 此语境的 **“自由能”尚未核实**，保留英文并解释计算 |

两篇英文来源的定义位置：
- **P18，[EnergyMatch](https://doi.org/10.1016/j.ress.2025.112013)**：PDF 第3页，式(4)，名称为 `free energy`，用于其跨域学习过程。
- **P51，[GWLSTM](https://doi.org/10.1109/TSMC.2026.3703212)**：PDF 第5页，式(18)，名称为 `energy function`；第5–6页涉及已知／未知判断。Skill 另记有符号、数值范围与阈值的一致性疑点，不能连同完整判定规则一起背书。

中文来源身份及已读位置：
- **中文期刊《电子学报》2026，54(1):153–166**：[来源](https://www.ejournal.org.cn/zh/article/doi/10.12263/DZXB.20250761/)。§3.1、式(9)，印刷页157–158／PDF第5–6页，核对 logit 能量函数定义；§4.3，印刷页162／PDF第10页，核对能量分数用语。
- **作者网站提供的《Class-Specific Semantic Reconstruction for Open Set Recognition》中译稿**：[来源](https://mftp.mmcheng.net/Papers/22PAMI-OpenSet-cn.pdf)。§2.2、PDF第3页，记录了 OOD 评分语境的“能量分数”。它由作者发表列表链接，**不是 IEEE 官方中文版，也不是新增的独立机制定义证据**。

物理振动能量与分类器 logit 能量的对象、运算不同，不能因同含 `energy` 就合并计数；同一学术工作的原文、中译本或镜像也不能重复计数。“能量值就是未知故障概率”应删除：现有记录没有概率映射或校准依据。推荐方法中明确计算为 `energy function`，输出作为评分时称 `energy score`；介绍 P18 时保留其 `free energy` 原名。

:::writing{variant="standard" id="64181"}
We compute an energy score from the classifier logits using a temperature-scaled negative log-sum-exp function; the score is not interpreted as the probability of an unknown fault.
:::

**B**
四种操作不能统称“残差连接”：

| 对象或操作 | 推荐中文 |
|---|---|
| \(m(t)\) | 后向滑动平均，作为局部均值参考 |
| \(r(t)=x(t)-m(t)\)，随后编码为 \(h\) | 相对滑动均值的偏差，或明确定义的信号残差；编码本身不是残差连接 |
| \(u=h+F(h)\) | **加性残差连接**，这里直接相加，不增设投影 |
| 拼接 \(u\) 与单独编码的 \(m(t)\) | **特征拼接**，可描述为拼接式特征融合 |
| \(e=y-\hat y\) | **预测残差**，是单独报告的统计量，不是网络连接 |

Skill §11 记录的两个中文核查来源：
- [《煤炭科学技术》2025，53(2):96–108](https://mtkxjs.com.cn/cn/article/pdf/preview/10.12438/cst.2024-1441.pdf)：§1.3及双语图3，印刷页99／PDF第5页，明确对应 `residual connection／残差连接`。
- [《农业工程学报》2026，42(7):1–11](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.202505227.pdf)：§2.1，第4页，明确对应上述术语，并描述前层输入与后层特征相加。

这些来源支持**网络连接的译法**，不支持把减均值、拼接或预测误差都改名为残差连接。现有事实也不能证明去噪或泛化：\(r(t)\) 未被证明是噪声，结构描述不等于效果验证。

:::writing{variant="standard" id="64182"}
We compute the trailing moving average \(m(t)\) and encode the deviation \(r(t)=x(t)-m(t)\) as \(h\). The additive residual connection produces \(u=h+F(h)\), which is concatenated with a separate encoding of \(m(t)\) for classification. Separately, \(e=y-\hat y\) is reported as the prediction residual.
:::

**C**
- **稿内名称可以保留。**将 `Elapsed-Interval Gate` 明确为本文定义的组件，并交代输入、输出及作用对象。题设称已有论文使用同名，但未提供可核查来源或定义，因此既不能认定两者机制相同，也不能声称该名称首次提出；若实际沿用前作，应明确归属。
- **完整名称目前不能作为既定机制家族收入共享术语库。**依 Skill §0，须有至少两篇独立论文对完整名称或经语义核实的等价名称提供匹配定义。两篇普通特征门控论文没有已逝时间输入，只能支持基础门控概念，不能补足 `Elapsed-Interval` 限定部分的证据。
- **不宜译为“年龄门控”。**本组件不估计人的年龄或设备老化。可保留英文，配本文描述性名称“测量后历时门控”，明确指“依据距各次测量时刻的已逝时间进行加权”；这不是已核实的通行译名。Skill §11 核实的基础译法“门控机制”也不能自动认证整个复合名称。

:::writing{variant="standard" id="64183"}
The Elapsed-Interval Gate takes the elapsed time since each sensor measurement as input and outputs one multiplicative weight for each encoded measurement.
:::
