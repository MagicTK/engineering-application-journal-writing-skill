# Regression-Coordinate Independent Response

One actual fresh context used frozen v4.2.10 on fictional requests. The actual independent baseline already passed; no controlled general gain is claimed. No original-paper reading by this agent, scientific experiment, second independent grader or controlled general writing gain is claimed. Only wrapper/path/link/line/whitespace and quota metadata are normalized; raw and dispatch remain private.

**读取边界**
主动读取仅限指定 Skill（v4.2.10）内的以下文件：
- 主 [SKILL.md](../../SKILL.md)。
- 定向读取参考段落：[指标与坐标](../../references/terminology-decisions.md)、[实验依据](../../references/experiment-evidence-design.md)、[本地来源记录](../../references/published-evidence.md)、[结果写作](../../references/argument-and-prose-craft.md)。
- 仅作关键词检索：[严谨性审查 Skill](../../skills/engineering-journal-rigor-review/SKILL.md)、[证据设计 Skill](../../skills/engineering-experiment-evidence-design/SKILL.md)。

运行时自动提供了规则、环境、工具与技能清单，以及历史记忆摘要；该摘要未作为本次证据，也未主动读取记忆文件。未读 evals、原论文或其他项目，未浏览、编辑、训练、安装或发布。唯一账户调用是只读额度检查：包含额度[private quota values]；未使用重置或余额。另执行了只读算术和词数核对。

**A：数值与作者决定**
以下均按三个样本等权计算，定义 \(R^2=1-\mathrm{SSE}/\mathrm{SST}\)，其中 SST 使用**当前评分参考值的均值**。

变换后，参考值为 \([-1,0,1]\)，预测值为 \([-0.5,-0.5,1.5]\)；两空间的参考均值分别为 12 和 0。

| 预测器与评分坐标 | MAE | RMSE | SSE | SST | \(R^2\) |
|---|---:|---:|---:|---:|---:|
| 给定预测，物理空间 | 1 g/L | 1 g/L | 3 | 8 | 0.625 |
| 给定预测，变换空间 | 0.5 | 0.5 | 0.75 | 2 | 0.625 |
| 固定预测器，物理空间 | 2 g/L | 2.581989 g/L | 20 | 8 | −1.5 |
| 固定预测器，变换空间 | 1 | 1.290994 | 5 | 2 | −1.5 |

SSE、SST 在物理空间的单位均为 \((\mathrm{g/L})^2\)，变换空间中无量纲。

**表格的具体处理：**
- **MAE/RMSE：**“0.5 g/L”不符合这些向量的物理空间误差；0.5 恰好符合变换空间误差，但这不能证明代码实际使用了该坐标。请核对每格的评分输入、公式和逆变换路径，再决定报告“变换空间误差 0.5”还是“物理空间误差 1 g/L”。不禁止规范报告归一化坐标结果。
- **\(R^2\)：**0.625 与指定公式一致，但不能据此辨认评分坐标，因为一致的非零仿射变换使 SSE、SST 同比例变化。评分参考均值用于定义分数，本身不等于用测试标签拟合模型或预处理。
- **固定预测器：保留 −1.5，不截为零。**其 SSE=20，大于评分参考均值预测器的 SSE=8；负值具有明确意义，不是越界错误。

物理空间 MAPE 为：
\[
\frac{100}{3}\left(\frac1{10}+\frac1{12}+\frac1{14}\right)
=8.49206349\%.
\]
因此“8.492%”与物理空间普通 MAPE 的舍入值一致，仍需确认代码确实采用该分母、样本和百分数显示方式；相对数值本身为 0.0849206349。

**中心化后的 MAPE 不能直接解释为浓度相对误差。**按普通公式 \(100\,\mathrm{mean}(|\hat z-z|/|z|)\)，三项为 \(0.5,\;0.5/0,\;0.5\)，整体没有有限定义。中心化改变了分母含义，并制造了零值。若实现使用 epsilon、删除零参考样本或其他规则，必须明确披露，不能擅自选定；纯乘法缩放则不会改变普通相对误差比值。

**英文 Results（52 词）**
Across the three concentration samples, the predictions achieved an MAE and RMSE of 1.0 g/L, with R2 = 0.625 and MAPE = 8.492%. Compared with the fixed 10 g/L predictor, MAE decreased from 2.0 to 1.0 g/L and RMSE from 2.582 to 1.0 g/L, demonstrating lower concentration errors on this illustrative set.

**B1：常量参考与两种 R2**
参考均值为 5，SST=0：

| 预测 | SSE | 原始比值问题 | 已说明的软件映射 | MAE / RMSE |
|---|---:|---|---:|---|
| [5,5,5] | 0 | \(0/0\)，未定义 | 1 | 0 / 0 |
| [5,5,6] | 1 | 分母为零；浮点计算通常得到 −∞ | 0 | 1/3 / \(\sqrt{1/3}\) |

**作者决定：有限值可以保留，但必须注明常量目标处理约定。**它们不使普通 \(1-\mathrm{SSE}/\mathrm{SST}\) 在这里获得数学定义，也不单独证明没有预测误差，更不足以认定报告造假。第一组无误差由向量证明，第二组明确存在误差。

报告应列明公式、常量参考情形、非有限值替换规则；核对现有函数/版本、配置、评分输入及日志是否与说明一致。这里没有执行或假定任何重跑，未提供的执行证据仍标为未核实。

**平方 Pearson 相关与上述 \(R^2\) 不可互换。**对于非恒定参考及 \(\hat y=y+c\)，相关平方为 1，而残差定义的 \(R^2=1-nc^2/\mathrm{SST}\)，非零偏移会降低它，甚至使其为负。另一张表应准确标为“平方 Pearson 相关系数”，不能借其值说明没有系统偏差；常量序列还会使 Pearson 本身未定义。

**B2：多目标汇总与排名**
令两个目标的不同单位分别为 \(U_1,U_2\)，尺度带有各自对应单位。

| 逐目标 MAE | 模型 A | 模型 B | 较低者 |
|---|---:|---:|---|
| 目标1 | \(1U_1\) | \(4U_1\) | A |
| 目标2 | \(10U_2\) | \(0U_2\) | B |

- **原单位数值等输出平均：**A=(1+10)/2=5.5，B=(4+0)/2=2，B 更低。
- **按声明尺度标准化后等输出平均：**A=(1/1+10/10)/2=1，B=(4/1+0/10)/2=2，A 更低。

**作者决定：两种排名均可保留，但必须准确命名并保留逐目标结果。**前者回答既定单位表示下的数值误差汇总，后者回答相对于训练尺度的误差汇总；两者均为目标各占 1/2，但尺度改变了原误差的相对贡献。前者没有某一个目标的物理单位，且随单位表示变化；后者无量纲。二者都不会自动成为应用成本，亦无须强制所有作者采用同一归一化方式。两模型不存在逐目标全面占优。

**本地来源的适用范围**
仅据 Skill 内部记录：P17 区分浓度误差、趋势分类与来源自定义的容差通过率；P34 记录归一化及质量预测指标。这些记录不证明其全部评分代码、逆变换或阈值实现。以上算术不是对原论文的复现，也不支持由误差指标推导趋势准确性、通过率、在线控制收益或跨工厂迁移。
