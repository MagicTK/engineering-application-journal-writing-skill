# Actual Regression-Coordinate Baseline Response

One fresh context used retained v4.2.9 on fictional requests. Baseline science already passed; this is not an invented model failure or controlled general gain. Wrapper/path/link/line/whitespace and quota metadata only are normalized. Raw/dispatch remain private. Original papers and metric implementations were not read by this agent.

**审查结论**
应纠正的是物理单位标签和负 R² 的截断；不能因有限值替换或归一化评价本身就判定结果错误或造假。以下计算仅来自题给向量，不代表复现任何论文或指标代码。

**A：计算与作者决定**
采用 \(MAE=\frac1n\sum|p_i-y_i|\)、\(RMSE=\sqrt{\frac1n\sum(p_i-y_i)^2}\)，以及题定的 \(R^2=1-SSE/SST\)，其中 \(SST=\sum(y_i-\bar y_{\rm scored})^2\)。

变换后的参考为 `[-1,0,1]`，预测为 `[-0.5,-0.5,1.5]`，固定值比较器为 `[-1,-1,-1]`。

| 可由向量确认的量 | 预测模型 | 固定值比较器 |
|---|---:|---:|
| 物理 MAE，g/L | 1 | 2 |
| 物理 RMSE，g/L | 1 | 2.581989 |
| z 坐标 MAE，无量纲 | 0.5 | 1 |
| z 坐标 RMSE，无量纲 | 0.5 | 1.290994 |
| 物理 SSE；SST，(g/L)² | 3；8 | 20；8 |
| z 坐标 SSE；SST | 0.75；2 | 5；2 |
| R²，两种坐标相同 | 0.625 | −1.5 |
| 物理 MAPE | 8.492063% | 15.079365% |

**具体作者决定：**
1. **MAE/RMSE 两格：**`0.5 g/L` 与这些向量的常规定义不符；`0.5` 恰好是 z 坐标结果。但这不能证明原代码确实用了 z 坐标。核实每格的输入坐标、逆变换、样本与聚合后，选择报告 `1 g/L`，或保留 `0.5` 并明确标为归一化指标、去掉 g/L。归一化评价可以合法保留。
2. **R² 一格：**`0.625` 的算术正确，但不能据此识别其计算坐标，因为对参考和预测共同使用该非零仿射变换，SSE/SST 不变。仍须核实采用的是题定公式及评分参考均值。
3. **MAPE 一格：**物理坐标下，\(100(1/10+1/12+1/14)/3=8.492063\%\)，故 `8.492%` 与物理 MAPE 的舍入一致；这仍不是原表计算路径已核实的证据。须确认公式、坐标和百分数显示方式。
4. **比较器：保留 −1.5，不截断。**它表示 SSE 是评分参考均值基线的 2.5 倍，即在该评分集上比恒预测均值更差。这里 SST>0，负值是有效结果，不是未定义情形。

若在中心化后的 z 上计算相对误差 MAPE，三项为 `50%、未定义、50%`：中间参考为零、绝对误差为 0.5，普通除法无法给出有限结果，浮点运算可能得到 `+∞`。即使其余分母非零，中心化也改变了相对误差的参照，不能解释为物理浓度百分比。**不替作者选择 epsilon、删零样本或其他实现；任何已有规则都应明确披露。**

**英文 Results，57 词**
Across the three concentration samples, the predictions achieved an MAE of 1.00 g/L and an RMSE of 1.00 g/L, with a physical-scale MAPE of 8.492%. The coefficient of determination was 0.625, compared with -1.500 for the fixed-value comparator. The predictions reduced squared error from 20 to 3 (g/L)^2, demonstrating lower concentration estimation error on this toy set.

**B1：常量参考与相关系数**
| 预测 | SSE | SST | 普通 R² 的实数定义 | 已声明的有限替换 |
|---|---:|---:|---|---:|
| `[5,5,5]` | 0 | 0 | 未定义，原始运算为 0/0，常表示为 NaN | 1 |
| `[5,5,6]` | 1 | 0 | 未定义，原始数值运算常表示为 −∞ | 0 |

报告的 `1、0` **与所声明实现一致**，但不使普通 R² 数学上变为有定义，也不证明整个计算流程没有错误，更不构成造假证据。由向量可独立确认：完美预测逐点误差为零；不完美预测存在误差，SSE=1。后者的替换值 0 不能按普通非恒定参考下的 R²=0 解释。

**作者应报告或核查：**注明该目标恒定、SST=0、原始非有限情形及 `NaN→1、−∞→0` 约定；核对已有函数/版本、替换选项和这些样本是否确为评分输入。可同时报告由现有向量直接算出的 MAE/RMSE，避免有限替换掩盖残差。这里没有进行或要求虚构一次重跑。

**平方 Pearson 相关系数不等于一般的决定系数。**对非恒定参考，若 \(p_i=y_i+c,\ c\ne0\)，则相关系数平方为 1，而题定 \(R^2=1-nc^2/SST<1\)。作者应将另一表明确标为 `Pearson r²` 并给出定义；若原意是决定系数，则检查现有计算与表格，不能只换名称。常量参考下 Pearson 相关本身也未定义。

**B2：多目标汇总**
令两个目标单位分别为 \(u_1,u_2\)，尺度为 \(s_1=1u_1,s_2=10u_2\)。样本内取均值后，输出间权重均为 `1/2、1/2`。

| 模型 | 目标1 MAE，u₁ | 目标2 MAE，u₂ | 未缩放数值等权均值 | 分尺度后的两个 MAE | 缩放后等权均值 |
|---|---:|---:|---:|---|---:|
| A | 1 | 10 | 5.5 | 1，1 | 1 |
| B | 4 | 0 | 2 | 4，0 | 2 |

**作者决定：两种排名可以保留，但必须分别命名并解释。**未缩放的数值汇总是 B 优于 A；按给定训练尺度衡量的相对误差汇总是 A 优于 B。它们回答不同问题，排名翻转本身不是错误；A 的目标1更好，B 的目标2更好，不能宣称全面占优。

不同单位的未缩放均值**没有任一目标的单一物理单位**。它至多是固定单位约定下的数值指数，单位换算可能改变排序；缩放后的汇总则无量纲。保留逐目标结果、尺度来源和等权规则，不把任何一种汇总解释成未提供的应用成本，也不强制所有作者采用同一种归一化。

**来源与读取披露**
依据该 Skill 的[回归指标核查](../../references/rigor-and-handoff.md)与[指标完整性指导](../../references/experiment-evidence-design.md)，区分公式、坐标、单位和聚合；上述具体数值由题给向量直接计算。

本地 [P17 记录](../../references/published-evidence.md)涉及浓度预测、稀疏标签和重构；[P34 记录](../../references/published-evidence.md)涉及质量输出、潜变量角色及拟合/预测区别。**浓度误差、趋势准确性、阈值达标结果、归一化质量预测指标不能互相替代。**所读记录不足以核实其具体指标实现；未查原文，未声称复现。

主动读取限于指定发布目录：主 `SKILL.md`、审查子 Skill，以及 `rigor-and-handoff.md`、`experiment-evidence-design.md`、`argument-and-prose-craft.md`、`published-evidence.md` 的相关内容；另在该目录的 `references/` 和审查/实验证据两个子 Skill 内检索关键词，并列出参考文件名。未读取 evals、记忆文件、原始论文或其他项目。

运行环境自动提供了工作区规则、环境信息、技能清单和历史记忆摘要；后者未用于本次判断。唯一账户访问是规定的只读配额检查：[private quota values]。未浏览、编辑、训练、安装、发布或重置配额。
