# Fictional Mask-And-Routing Final Response

One fresh task context answered the same two requests on the frozen final source; only the read root changed. The earlier response already passed core science and writing. The new record changes maintained evidence availability, not a demonstrated general writing gain. Wrappers, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

本轮按预设虚构测试作答，依据本地 v4.1.55 文件与题设；未联网复核来源，也未执行研究实验。

**A. 运算与裁定**
掩码及掩码后的参数为：
\[
M=\begin{bmatrix}1&0&1\\1&1&0\end{bmatrix},\qquad
W_M=\begin{bmatrix}1&0&-2\\0.2&0.5&0\end{bmatrix}.
\]

| 核对项 | 掩码前 | 掩码后 |
|---|---:|---:|
| 输出 | \([4.04,\ 2.44]\) | \([4.00,\ 2.40]\) |
| 非零系数数 | 6 | 4 |
| 分配的参数槽位 | 6 | 6 |
| 参数数组形状 | \(2\times3\) | \(2\times3\) |
| 输出形状 | 二维向量 | 二维向量 |

置零比例为 \(2/6=1/3\approx33.3\%\)。

- **“少存储33.3%字节”：不成立。** 相同数据类型下，稠密数组仍保存六个系数槽位；实际文件大小不能由非零比例推出。
- **“时延降低33.3%”：不成立。** 原稠密内核仍执行，不能把非零数下降换算为实际加速；题设没有时延测量。
- **“结构化通道移除”：不成立。** 仅移除两个标量权重的有效连接，没有删除完整输入列或输出行。这是固定掩码的非结构化权重剪枝，输出维数保留。
- **“所有输入相关特征权重都是剪枝”：不成立。** 随输入计算的特征系数或激活属于中间对象，不自动等于模型参数移除；须检查实际操作及作用对象。
- **“选择缓存模型就是在线参数学习”：不成立。** 运行选择改变调用哪个模型，不改变其权重或掩码；状态相关决策与参数更新是两回事。

**术语库记录：有，但范围有限。** [基础词条](../../references/engineering-application-terminology-bank.md)与[核查记录](../../references/published-evidence.md)已维护以下两篇不同已发表作品的操作配对：
- **P85**：*Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT*，TCCN 11(5), 2025, 3486–3501，DOI `10.1109/TCCN.2025.3529688`。记录检查作者托管的已发表PDF第4页、III-A2节：低幅值权重/卷积核置零、重训，之后运行时选择模型实例；成本比例属于模型假设。
- **P86**：*A Hardware-Friendly Approach Towards Sparse Neural Networks Based on LFSR-Generated Pseudo-Random Sequences*，TCSI 68(2), 2021, 751–764，DOI `10.1109/TCSI.2020.3037028`。记录检查研究组托管的已发表PDF第3–5页、II-B1节及III节/图2：参数移除与重训，另有保留位置生成及稀疏执行设计。

配对支持的是**网络参数/连接选择、置零或移除这一基础操作**，不是两篇流程诊断实现，也不认证完整JOPA/LGPS名称或性能结论。[中文独立记录](../../references/engineering-application-terminology-bank_CN.md)以《自动化学报》`10.16383/j.aas.c180275`原始双语摘要、配对关键词及相关图注核对 **network pruning／网络剪枝**；可读材料不含完整方法正文。

题名、书目提及、同一作品的不同版本、权重裁剪、输入加权和多项式阶数调整，均不能自动补作匹配剪枝定义。未收录也不等于术语无效。[完整名称准入规则](../../references/engineering-application-terminology-bank.md)不允许基础词条自动认证 **Causal Age-Pruning Reliability Module**；当前记录未支持该完整名称，题设操作也未建立其中的因果、时间或可靠性含义。

方法句，**32词**：
A fixed magnitude mask implements unstructured weight pruning by setting coefficients with absolute values below 0.1 to zero and keeping those positions zero, yielding a masked linear transform with two output components.

**B. 中文核查意见**
保留作者批准的英文提名 **MaskRouteFD**，不另造中文全称。候选设计的贡献落在模型选择、任务路由与边缘算力分配的协调关系，普通剪枝不单独列为创新；相对已有工作的新增性仍待作者核查。

模型准备与运行调度分开：评价前完成训练、固定掩码及分别微调，准确率来自声明的开发/校准子集而非评价标签；评价期固定CNN权重与掩码。约束使用模型准确率估计，不保证每次分类正确。证据仅支持规定成本模型下的两组模拟交通比较，不扩展为设备时延、稀疏序列化收益、现场部署、因果或跨厂结果。

计词按空白分隔，连字符词及斜线连接项各计一词；以下摘要 **130词**，贡献 **34词**。

MaskRouteFD addresses timely known-class bearing fault classification in an IIoT service through prepared-model selection and task routing. Before evaluation, a trained CNN parent yields three individually fine-tuned variants through fixed parameter masks; a declared development/calibration subset supplies their accuracy estimates. During evaluation, weights and masks remain fixed. A learned scheduler uses available queue and wireless-link state to select a cached local variant or route the task to the full parent on an edge server, while allocating edge computing capacity. The selected model determines the fault class, with scheduling targeting timely completion subject to estimated model-accuracy requirements. Across two held-out simulated IIoT traffic scenarios replaying recorded bearing signals, MaskRouteFD yields a lower simulated late-task fraction than always executing the full parent locally, under an inference-cost model proportional to retained nonzero weights.

We propose MaskRouteFD to coordinate cached-model selection, local or edge execution, and edge computing allocation for bearing fault classification, targeting timely completion under estimated model-accuracy requirements with inference costs modeled from retained nonzero weights.
