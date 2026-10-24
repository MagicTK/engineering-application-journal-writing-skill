# Fictional Mask-And-Routing Baseline

One task context answered two requests on the immutable v4.1.54 release. Core calculations and writing already passed; the response correctly reported the absent scoped English pruning pair while preserving the separate Chinese record. This is an evidence-coverage gap, not a demonstrated scientific reasoning failure. Wrappers, local links and whitespace only are normalized; raw records remain private.

**A. 中文核查意见**
按给定操作，掩码及变换后的系数为：

\[
M=\begin{bmatrix}1&0&1\\1&1&0\end{bmatrix},\qquad
W'=\begin{bmatrix}1&0&-2\\0.2&0.5&0\end{bmatrix}.
\]

| 项目 | 掩码前 | 掩码后 |
|---|---:|---:|
| 输出 | \([4.04,\ 2.44]\) | \([4,\ 2.4]\) |
| 非零系数数目 | 6 | 4 |
| 系数数组形状 | \(2\times3\) | \(2\times3\) |
| 输出形状 | 二维向量 | 二维向量 |

屏蔽比例为 \(2/6=1/3\approx33.3\%\)；输出变化为 \([-0.04,-0.04]\)。

逐项判断：
- **“少存储33.3%的字节”：不成立。** 同样的数据类型和稠密表示仍存储6个系数槽位，非零数下降不等于系数存储字节下降。
- **“延迟降低33.3%”：不成立。** 原稠密内核仍执行原来的计算，不能从非零比例推出加速，更没有实测延迟依据。
- **“结构化通道移除”：不成立。** 被屏蔽的是两个独立标量系数，没有整行或整列删除，输入仍为3维、输出仍为2维。这是可准确描述的非结构化权重剪枝。
- **“所有输入相关的特征权重都是剪枝”：不成立。** 固定系数属于模型参数；随输入计算的特征、注意力系数或门值属于中间量。加权本身不等于删除；确有特征移除时，才按实际对象与操作判断。
- **“调度器选择缓存模型就是在线参数学习”：不成立。** 选择改变的是被调用的模型，不是其参数；题设没有在线参数更新。

**词库状态：未完成所问组合记录。** [维护记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/953a5873a18697e6d7bee3333901a141d967f195/references/engineering-application-terminology-bank.md#L462)明确指出：P31的自适应多项式阶数调整不是剪枝；P74的选择性加权保留表示集合；P76的背景措辞与原始WGAN权重裁剪冲突，其梯度惩罚也是另一操作。另读作者预印本虽然描述参数掩码，但期刊正文不可访问、版本对应未核实，不能补足两个不同已发表工作的操作定义记录，也不能将同一工作的版本重复计数。

中文基础措辞则有**单独的既有核查记录**：`network pruning / 网络剪枝`，来源为《自动化学报》c180275的双语摘要及配对关键词；可访问范围为摘要、图题等，并非完整方法正文。[记录位置](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/953a5873a18697e6d7bee3333901a141d967f195/references/engineering-application-terminology-bank.md#L402)。本轮未联网复核。缺少完整准入记录不等于术语无效，题名、书目或操作不匹配的文字不能补足记录。

基础词条**不能准入完整名称** `Causal Age-Pruning Reliability Module`；基础词的证据不覆盖新增修饰语及其组合。本题也未提供支持该名称的年龄、因果或可靠性机制。

英文方法句，**32词**：

A fixed magnitude mask sets coefficients with absolute values below 0.1 to zero and preserves those zeros, leaving four nonzero weights in a linear transform that maps three inputs to two outputs.

**B. 中文作者说明**
- 保留作者批准的英文候选名 **MaskRouteFD**，不扩写缩写、不创造中文全名。候选贡献落在模型选择、边缘路由与算力分配的组织设计；新颖性比较仍待核查，普通剪枝不单独作为创新。
- 评价前完成母模型训练、三个掩码变体的分别微调及开发／校准子集准确率估计，评价标签不参与估计；评价时CNN权重与掩码固定，调度器选择执行位置和模型，由所选模型给出故障类别。
- 准确率约束针对模型准确率估计，不是逐样本正确性保证。结果仅覆盖两个留出的模拟交通场景及所给成本假设，不推出设备延迟、稀疏文件节省、现场部署、因果或跨厂结论；也没有在线CNN拟合。

三个英文产物统一按**空白分词**计数，连字符词及含斜杠词各算一词，不计标签。

英文摘要，**123词**：

MaskRouteFD targets timely known-class bearing fault classification in an IIoT service subject to estimated model-accuracy requirements. Before evaluation, a trained CNN parent supplies three variants through fixed parameter masking and individual fine-tuning; their classification accuracies are estimated on a declared development/calibration subset. During evaluation, CNN weights and masks remain fixed. A learned scheduler observes available queue and wireless-link state to select a cached local variant or route the task to the full parent on an edge server, while allocating edge computing capacity. The selected model produces the fault-class decision. In two held-out simulated IIoT traffic scenarios replaying recorded bearing signals, MaskRouteFD yields a lower simulated late-task fraction than always running the full parent locally, under an inference-cost model proportional to retained nonzero weights.

英文贡献候选，**35词**：

We propose MaskRouteFD, a scheduling design that uses queue and wireless-link state to select cached CNN variants or edge execution and allocate edge computing capacity for timely known-class bearing fault classification under estimated model-accuracy requirements.
