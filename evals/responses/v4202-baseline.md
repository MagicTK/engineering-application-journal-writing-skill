# Fictional Resource/Wording Baseline

One context answered A/B on immutable v4.2.1. Its main science and prose already pass; missing source-specific details are left unverified. Only wrappers, private path/link/line metadata and whitespace are normalized; exact raw/dispatch remain private. Runtime orientation is disclosed, not case evidence.

运行定位：本轮为 Codex 桌面中的只读写作校准，使用指定 ROOT 的中文入口及选择性参考路由；未读论文原文。以下数字均为虚构算例，不是论文或工业结果。

**A｜紧凑性与措辞**
- **可以保留的积极结果**：总参数从 4M 降至 1M，减少 **75%**、剩原来的四分之一；声明的同一测试比较中，准确率从 92% 升至 93%，提高 **1 个百分点**。可以表述为“参数规模更紧凑，同时取得更高的测试准确率”。
- **不能随之推出**：训练更快、推理更快、运行内存或能耗更低、统计显著提升、已完成边缘部署或满足实时要求。原句 `resource-constrained real-time edge deployment is achieved` 超出了现有证据；应改写该主张，**不是删除已有参数与准确率收益**。纯参数数量比较不必强制硬件试验。[资源主张边界](../../references/topic-playbooks.md)
- **现场困难不能补造**：实际边缘资源不足、通信瓶颈、设备老化、传感器退化、标签稀缺、持续工况漂移等均未给出。两种负载是已知比较条件，不自动证明它们造成了诊断困难，也不能从总体准确率推出每种负载下都提高。

工况搭配首选 **`under two known load conditions`**；概括时可用 `under different operating conditions`。`under operating varying conditions` 修饰顺序不自然；通常搭配是 `under varying operating conditions`，但本例直接点明“两种已知负载”更准确。**工况之间不同，不等于工况随时间变化**：没有时间顺序，不能自动写 `time-varying operating conditions`，也不能断言非平稳、渐变或持续适应。[问题分类边界](../../references/problem-first-classification_CN.md)

仅按 ROOT 的来源记录区分如下，**不将笔记中的既往阅读描述冒充本轮原文核查**：

| 记录 | 能支持的来源角色与边界 |
|---|---|
| P31 | 记录中的阶次调整发生在训练阶段，应区分训练侧工作与预测侧成本；所读记录没有具体训练耗时，不能据此认证训练加速，更不能推出诊断实时性。 |
| P45 | 记录区分训练指导、退出预测与预测结构转换。设备预测测量若存在，属于特定设备及计时边界下的运行证据，不是训练成本，也不自动是完整链路时延；**所读记录未给设备与计时细节，本轮不能认证其设备测速**。 |
| P85 | 记录涉及预先准备模型变体及运行选择，使用计算成本模型；相应模拟任务时延受模型假设约束，不能改写成实际设备或现场完整链路的实测时延。 |

依据为 ROOT 的[来源记录](../../references/published-evidence.md)及[成本模型说明](../../references/published-evidence.md)，不补报原文测量数值。

英文比较段，56 词：

In this hypothetical test comparison using data from two known load conditions, the classifier increases accuracy from 92% to 93% while reducing its total parameter count from 4 million to 1 million. This represents a one percentage point gain with 75% fewer parameters, yielding a more compact diagnostic model with higher accuracy in the evaluated setting.

**B｜时限与容量**
以输入窗结束为起点，阶段互不重叠且顺序执行，因此直接相加：

- **此次总时延**：`80 + 110 + 50 + 20 + 10 = 270 ms`。超过 `250 ms` 截止时间 **20 ms**，此次未达标；不另外加入窗结束前的采集时间。
- **同时内存需求**：`6 + 9 + 14 + 8 + 3 = 40 MB`。超过 `32 MB` 预算 **8 MB**。两份权重都必须常驻，不能只计当前选择的一份；已确认各项独立，不作重复扣减。

**20 ms 模型时延不能证明达标**，它只是完整链路的一部分。**1 s 采样周期也不能证明达标**：采样间隔不是决策截止时间；即使 `270 ms < 1 s`，仍超过规定的 `250 ms`。

**此次迟发不是未来信息泄漏的证据**。所有实际输入在窗结束时已发布，按给定事实，这是计算与传递导致的迟发；不能据此认定读取了未来信息，也不能把迟发结果报告为按时完成。[信息访问与迟发的区别](../../references/terminology-decisions_CN.md)

这些单次记录只能确定此次超时、给定同时驻留配置超容量；**不能证明所有负载下的最坏时延**。全负载时延上界、波动范围及其他配置的峰值内存均未知，不补造额外开销或保证。

英文问题句，30 词：

In this hypothetical system, a 250 ms decision deadline and a 32 MB memory budget are exceeded by the specified 270 ms processing chain and 40 MB simultaneous memory requirement.
