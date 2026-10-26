# Rate Conversion: Actual First Response

Fictional-use response. Local links, client writing-block wrappers and account-status metadata are normalized for publication; substantive answers are unchanged. The exact private response is retained. See [request, criteria and scope](../reviews/rate-conversion-evaluation.md).

## Actual Request

### Fictional Writing Request

Use the engineering terminology polishing skill in `$SUITE_ROOT`. Read its relevant instructions and references as needed. This is a read-only independent fictional-use check, not permission to edit files, run experiments, browse private manuscripts, or publish anything. Do not read evals/, tests/, maintainer notes, memory files or old answers. Disclose any inherited context or material access limitations. Return the response here.

请帮我处理以下三个互相独立的小请求。不要为了字数重写整篇论文，也不要改算法。

### A

虚构冷却过程案例：压力原始流均匀采集于12 Hz，模型输入用 `z[k] = x[4k]`，从x[0]开始；没有做时间分箱平均，没有滤波。另一独立温度流原生采集于3 Hz。作者写："Both variables were acquired at 3 Hz. Anti-aliased resampling averages every four pressure observations and retains a 2 Hz pressure component at its original frequency." 请核对并给2句可用于Methods的英文，另给作者一条简短必要说明；不要静默加滤波或改已有数据。这个2Hz说法在所述采样下是否成立？没有故障诊断结果可用。

### B

虚构数据只有t=0,2,7秒的三个压力观测，值分别为0,4,14。事后插值在t=4秒形成输入：一份实现按真实时间线性插值，另一份错误实现把数组位置0,1,2当等间距坐标，并将查询位置设成两后端点索引的中点1.5。请核查两份实现t=4的数值，以及"interpolation preserves the original sampling process"这句。另一个任务在真实t=4发出预测，届时只有前两个观测，能否沿用同一事后插值输入？最后，训练器对稀有类别样本重复抽取以调整类别比例，是否也能写成同一种time-series resampling？只给准确用词和必要修改说明，不拟新网络、实验或数据划分。

### C

一篇工程文章用upsampling描述利用较快过程变量预测较慢变量在公共网格上的值。作者另有两段实现：MATLAB `upsample(x,3)`；以及MATLAB `resample(x,tx)`，tx是不等间隔的观测时间，没有传目标fs或滤波参数。他想把所有upsampling都统一改写成"linear interpolation with an anti-aliasing filter"，并把每个新网格点都计入"additional acquired samples"。是否适合？请给一段简短中文解释，分别列出相关英文和中文用词，并指出依据是工业论文用例还是数值工具定义。不要把一篇论文的具体用法说成普遍规则。

## Actual First Response

**A｜采样率与频率分量**
实际操作是 **downsampling / temporal subsampling（下采样／时间位置抽取）**：压力原生采集率为 12 Hz，输入速率为 \(12/4=3\) Hz；温度才是原生 3 Hz。选点不是平均，也没有抗混叠滤波。[数值操作定义](https://www.mathworks.com/help/dsp/ug/design-of-decimatorsinterpolators.html)

Methods 两句：
Pressure was acquired uniformly at 12 Hz, whereas temperature was acquired independently at 3 Hz. The pressure input was downsampled to 3 Hz by retaining every fourth observation, starting with x[0] (z[k] = x[4k]), without time-bin averaging or filtering.

**作者必要说明：**“保留原频率的 2 Hz 分量”不成立：输出奈奎斯特频率为 1.5 Hz，2 Hz 分量会混叠到 1 Hz，因为 \(e^{j2\pi(2/3)k}=e^{-j2\pi(1/3)k}\)。应删除原句中的平均、抗混叠及原频率保留声明，不补写未执行的滤波；没有诊断结果，不能进一步断言诊断性能受损。

**B｜插值、时间可用性与类别抽样**
| 实现 | 计算 | 结果 |
|---|---|---|
| 真实时间线性插值 | \(4+\frac{4-2}{7-2}(14-4)\) | **8** |
| 错误的索引坐标插值 | \(4+\frac{1.5-1}{2-1}(14-4)\) | **9** |

索引中点给两端相同权重，对应两观测时刻的中点 **4.5 秒**，并非 4 秒；正确时间权重是 \(2/5\)。

- **原句需改：**`interpolation preserves the original sampling process` 不准确。这里是 **linear interpolation in physical time（按真实时间线性插值）**，构造未实测时刻的输入；既不改变历史采集事实，也不能把构造序列说成原始采样过程。
- **真实 t=4 的预测不能沿用该事后输入：**数值 8 的这份插值依赖尚不可得的 t=7 观测。它可用于 **retrospective interpolation（事后插值）**，不能冒充当时可得输入。仅有 t=0、2 时，t=4 已超出可用观测区间；若延长这两点的直线，即使也得到 8，仍是 **linear extrapolation（线性外推）**，不是同一插值。
- **类别重复抽样另称：**可用 **minority-class oversampling（少数类过采样）**，并注明重复抽取已有训练样本；上位描述为 **resampling training examples for class balancing（为类别平衡重抽训练样本）**。这不是时间轴上的 **time-series resampling（时间序列重采样）**。

**C｜不能统一替换**
不适合。利用快速变量预测慢速变量、插零、按时间线性插值是不同操作。工业文章可以在明确定义后将第一种操作称为 `upsampling`，但这是该文的具体用法，不构成所有数值算子的通用定义；三者也都不产生新的传感器采集事实。

| 对象 | 准确英文与中文 | 依据及必要限定 |
|---|---|---|
| 利用快速变量预测慢速变量 | **prediction of low-rate process variables on a common time grid**／公共时间网格上的低采样率过程变量预测 | 普通功能描述；Skill 记录了相关工业论文的 `upsampling` 用例，仅支持来源特定用法。[Skill 相关记录](../../references/terminology-decisions.md#rate-conversion-and-interpolation) |
| MATLAB `upsample(x,3)` | **upsampling by zero insertion**／插零上采样 | 每个原序列值后插入两个零，序列长度变为三倍；不是线性插值，也不自行滤波。依据是[数值工具定义](https://ww2.mathworks.cn/help/signal/ref/upsample.html)。 |
| MATLAB `resample(x,tx)` | **linear interpolation onto a uniform time grid**／向均匀时间网格作线性插值 | 输出与 `tx` 有相同端点和点数；该调用不执行抗混叠滤波，不能套用带目标 `fs` 调用的滤波说明。依据是[数值工具定义](https://www.mathworks.com/help/signal/ref/resample.html)。 |

新构造位置分别应称 **predicted grid values（预测网格值）**、**inserted zeros（插入的零值）**或 **interpolated grid values（插值网格值）**，不能计为 **additional acquired samples（新增采集样本）**。尤其 `resample(x,tx)` 在此并不增加总点数。

**实际读取与限制**
- 全文读取了指定请求文件、当前套件 **v4.2.43** 的顶层 Skill，以及术语润色 Skill 的中英文版本。
- 定向读取了中英文术语决策中的采样、时间和速率转换段落，以及 `published-evidence.md` 的速率转换记录；另对术语库、风格指南和发表证据作过关键词定位，**未通读这些参考文件**。一次检索回显截断，实际采用的关键段落已单独完整读取。
- 在线核对了 Skill 链接的四份 MathWorks 官方文档，页面标示 **R2026b**；未运行 MATLAB，未检查本机版本或函数源码。A、B 数值来自题设手算。
- **直接阅读真实论文数量为 0。**工业用例仅依据 Skill 内的二手记录，不声称本次重新验证论文或完成多论文术语准入。
- 进入本轮时，上下文已含用户／项目历史摘要，因此并非完全无继承上下文的盲测；未将其作为答案依据，也未打开记忆文件、旧答案、其他维护者文件、测试或评测目录。
- 未编辑文件、运行实验或发布内容。
