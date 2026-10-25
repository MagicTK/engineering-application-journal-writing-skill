# Fictional Resource/Wording Final Response

A new context answered the same A/B prompt on frozen v4.2.2; only the reading root changed. Baseline main science/prose already pass; newly read source details are separately checked. Only wrappers, private path/link/line metadata and whitespace are normalized; exact raw/dispatch remain private. Runtime orientation is not case evidence.

运行取向：本轮在 Codex 工程协作环境中，按中文入口 v4.2.2 选择“问题优先分类＋术语校准”；这不是案例证据。以下数值均为题设虚构值，本轮未读取论文原文。

**A**
**成立的积极结论：**总参数量由 4M 降至 1M，减少 **75%**，为原来的四分之一；声明的同一测试比较中，准确率由 92% 提高至 93%，增加 **1 个百分点**。因此可以写“参数层面更紧凑”“以更少参数获得更高测试准确率”，保留准确率与参数量两项比较的改善。没有分工况结果，不能进一步说两种负载下分别都提高。

**不能据此成立：**“resource-constrained real-time edge deployment is achieved”。设备与预算未给，不能编造现场算力、内存、能耗或通信瓶颈；参数减少也不自动证明训练更便宜、预测更快、运行内存减少 75%，更不证明已部署、满足实时期限、统计显著或方法新颖。**纯参数比较本身合理，不应为保留该比较而强制硬件试验。**

工况搭配应按事实选择：
- 本题最准确：`under two known load conditions`；概括不同工况比较可用 `under different operating conditions`。
- `under variable operating conditions` 和 `under varying operating conditions` 是可用搭配；`under operating varying conditions` 的修饰顺序不合适。
- `under time-varying operating conditions` 明确引入随时间变化的含义。两种已知负载、没有时间顺序，不能自动支持这种表述，也不能推出连续漂移或未见工况泛化。[本地规则](../../references/problem-first-classification_CN.md)

仅据 ROOT 的记录，三个来源角色应分开：
| 记录 | 来源角色及边界 |
|---|---|
| P31，p.10，Table VIII/Fig.10 | 复杂度、训练时间及参数量语境；不能替代设备预测时延证据。 |
| P45，pp.7–8，Table II及设备讨论 | 记录设备预测阶段的推理与资源比较；不能移植为本虚构分类器的测量结果或普遍实时保证。 |
| P85，p.7，式(16) | 模拟服务中多部分端到端任务时延的建模；不是当前设备实测时延。 |

以上转述的是[ROOT 的阅读记录](../../references/published-evidence.md)，不表示本轮读过原文、复现过结果或认证其全部公式。

英文比较段，61 词：

In the stated test comparison using data from two known load conditions, the classifier achieves 93% accuracy versus 92% for the baseline, while reducing the total parameter count from 4 million to 1 million. This comparison shows that a 75% reduction in parameter count accompanies an accuracy gain of one percentage point, yielding a more compact classifier with higher test accuracy.

**B**
按题设各阶段顺序执行、时间不重叠，各内存项同时存在且不重复计数：

- **总时延：**80＋110＋50＋20＋10＝**270 ms**。从输入窗结束起计算，超过 250 ms 时限 **20 ms**，本次未达标。
- **同时内存需求：**6＋9＋14＋8＋3＝**40 MB**。两份必须常驻的权重均须计入，超过 32 MB 预算 **8 MB**；给定同时驻留需求不满足容量约束。

**20 ms 模型时延不能证明达标**，因为它只是端到端响应的一部分；**1 s 采样周期也不能证明达标**，因为这里明确的决策时限是 250 ms，而不是下一次采样之前。

**迟发不等于未来信息泄漏。**所有输入在窗结束时已发布，本题没有给出使用更晚信息的证据；已知问题是输出超时，不能仅因输出较晚就判为泄漏。

**单次记录不能证明所有负载下的最坏时延。**它能确认本次超时；其他负载下的时延变化、最大值及最坏界仍未知，也不能由此断言每次都会超时。[本地规则](../../references/problem-first-classification_CN.md)

英文问题句，35 词：

In this fictional case, the system must return decisions within 250 ms of input window closure and operate within 32 MB, yet the recorded response takes 270 ms and simultaneous memory demand reaches 40 MB.
