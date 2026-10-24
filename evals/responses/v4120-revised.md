# Frozen 4.1.20: Actual Fictional-Case Response

One fresh responding context. Only local repository link targets were made relative; the response text is unchanged. The fictional names and numerical examples are test inputs, not recommended modules or research results.

以下依据指定 Skill 及其相关文件作答。文献依据均为 **Skill 已有核查记录**，本轮未重新检索或查阅论文原文。

**A｜两句均与实际结构不一致**

第一句把“局部标签空间”误写成“标注歧义消解”；第二句把局部 softmax 分数误当成整个系统只能输出一个故障。建议整体替换为：

:::writing{variant="standard" id="68314"}
Each local classifier produces softmax scores over a partial label space comprising two single-fault classes and an “other” class defined for that classifier. The relevant local outputs are combined using a predefined averaging rule to obtain a score for each fault. Fault-specific thresholds determined from the training data then convert these scores into a predicted fault set, allowing multiple faults to be selected for the same sample.
:::

中文理由：标签已完整确定，不存在需要消解的候选标签歧义。最终决策由“局部分数→规定平均→逐故障阈值”形成，不能仅凭局部 softmax 判断其为单故障输出；局部“其他”类别也不代表未知故障拒识。Skill 的 P37（PDF pp.3–4）、P39（pp.3–6）核查记录支持这些层次区分，但不意味着两篇论文的具体融合规则相同。[已有核查记录](../../references/published-evidence.md)

**B｜逐项准确率相同，但完整故障集合识别表现不同**

按题目给出的二值结果直接核算：
- 平均逐项错误率（Hamming loss）＝错误元素数 ÷ 16。
- 完整标签集合正确率（exact-set accuracy）＝整行完全正确的样本数 ÷ 4。

| 指标 | 模型 A | 模型 B |
|---|---:|---:|
| 各样本错误元素数 | 1、1、1、1 | 4、0、0、0 |
| 平均逐项错误率 | 4/16＝25% | 4/16＝25% |
| 逐项准确率 | 75% | 75% |
| 完整标签集合正确率 | 0/4＝0% | 3/4＝75% |

原句不成立：相同的错误总数，分别分散在四个样本和集中在一个样本，导致完整集合恢复率不同。

:::writing{variant="standard" id="68315"}
For these four samples, both models have a Hamming loss of 25% and an entrywise accuracy of 75%, whereas exact-set accuracy is 0% for model A and 75% for model B. Thus, identical entrywise accuracy does not imply equivalent recovery of complete fault sets.
:::

这仅报告所给结果，不推断显著性或模型机理。上述指标区分符合 [Skill 的评价指导](../../references/experiment-evidence-design.md)；其中 P40 的记录仅支持区分评价作用，未核验其所引用的全部指标公式或实现，本题数值来自直接计算。

**C｜无需因此重写任务定义或重做实验**

当前是有效的**四类互斥状态分类**：A+B 是一个复合状态类别，其确定映射仍表示两个故障同时存在。选择一个状态类别，不等于只能表达一个物理故障。因此，“复合故障必须使用多个 sigmoid”不成立。只需把既定类别和映射说明清楚，不必改成另一种任务。

:::writing{variant="standard" id="68316"}
This study formulates diagnosis as four-class classification over normal operation, fault A, fault B, and the predefined compound state A+B, with a single softmax classifier selecting one state and the A+B class representing the simultaneous presence of both faults.
:::

该表述直接限定四种状态，没有附加未知组合识别能力，也不需要重复防御性声明。Skill 明确要求保留符合实际任务的复合类别评价，不因其他论文采用多标签方法而强制重构。[相关指导](../../references/experiment-evidence-design.md)

**D｜两个名称应分别判断**

**“Adaptive Fault Coalition Module／自适应故障联盟模块”：目前不能推荐为通用模块名称。** 按题设，论文甲只能支持其自身定义的专用名称；论文乙的普通注意力既没有该全名，也没有相匹配的故障集合构造。“都涉及权重”不能构成完整名称的语义等价证据。此外，题设未提供该完整中文译名的独立核查依据，不能把直译当作已核验的通用译名。

这不是禁止新命名：介绍论文甲时可以保留其名称并注明归属；作者也可以为真正提出、已有操作定义的组件命名，明确属于本工作，并保留在项目术语表中。它与进入通用术语库是不同事项。[名称准入规则](../../references/engineering-application-terminology-bank.md)

**“multi-label learning／多标签学习”：可以推荐用于题述任务。** Skill 已有匹配记录：P37（pp.2、4）和 P39（pp.2–3）涉及同一样本的多个故障指示；两篇为同一作者组合的不同工作，P40（p.3）另提供不同团队的二值样本—标签矩阵定义。这支持基础任务术语，不支持任意扩展模块名。[英文核查记录](../../references/engineering-application-terminology-bank.md)

中文“多标签学习”另有《微电子学与计算机》2022.0266及《软件学报》2024年第35卷第6期双语题名、摘要的既有核查记录。因此可用于“多个标签可以同时为真”的任务，但不自动表示标签歧义、故障物理相互作用或某种固定输出层结构。[中文核查记录](../../references/engineering-application-terminology-bank.md)

