# Auxiliary Guidance: Actual Initial Answer

Fictional inputs; suite 4.2.20. Scientific judgment was correct, but the prose was judged too close to a Methods inventory. Suite paths and display formatting are normalized; the raw response is preserved in maintenance records.

## Request

请使用 the current Skill suite，帮助一个虚构的流程工业故障分类稿修订摘要和候选贡献。只读所需公开Skill/参考，不读evals/tests、私有维护记录、真实论文或其他项目；不联网、不改文件、不科研训练、不再委派。不要把它当真实论文或已证新算法。

作者已经确认摘要开头两句，请保持原文：
Fault diagnosis under changing operating conditions is complicated by scarce and unevenly distributed fault labels. This study develops a diagnostic approach that learns from labeled source measurements and unlabeled measurements from a target condition.

以下是本算例已经确认的实现事实，不是要求你设计新方法：
- 正常/故障两个类别在源工况、目标工况中含义相同；不存在未见故障类别。源训练样本有标签且类别不均。目标适配池无任务标签；独立目标评价样本不参与拟合或选择。没有其他历史预训练模型。
- 同一个编码器连接诊断头D和辅助类别估计头E；两头都由源标签训练，E的源训练目标额外含源类别比例相关的logit调整。
- 适配阶段，E对无标签目标适配池作预测，计数形成类别比例估计。它不是人工测得的真实类别比例。程序把该估计与预设的三种参考分布(0.9,0.1)、(0.5,0.5)、(0.1,0.9)比较，再按已实现的固定规则确定调整强度。这里只要求解释作用，不需要你补写该规则公式。
- 该强度用于调整D在目标弱增强视图上的logits，再取硬伪标签，指导同一样本强增强视图的分类损失；该损失更新编码器和D。没有物理守恒/因果约束或无偏性的证明。两种增强及其任务标签保持性是作者已确认的设置，不需要新增增强方法。
- 适配后仅编码器和D对新样本分类。E、整个适配池和模板比较不进入单个新样本的诊断计算；部署中没有参数更新，也没有两头概率融合。

当前结尾草稿是：
An encoder and two classifiers recover all process information. The auxiliary classifier identifies the unknown target prior without assumptions. Three prior-free reference distributions then guarantee unbiased pseudo labels, which are fused with classification outputs during deployment. The resulting method achieves superior diagnosis under all operating conditions.

现有证据只有一次仿真过程的独立目标评价，100个样本：80正常、20故障。基线对正常判对76、对故障判对10；方案对正常判对66、对故障判对16。其余样本均判成另一类。没有其他工况、实地产线、提前预警、重复运行或统计显著性结果。

请给出：
1. 一版完整英文摘要，开头两句不变，重点解释方法之间的实际关系并落到现有发现。约180词即可，必要时灵活，不凑长度，不把全部计数/模板写进去。
2. 一条英文候选方法贡献，强调相互关联的操作和作用，不把普通编码器或完成实验另算贡献。最近文献/新颖性比较尚未提供，请把必要确认写在作者说明而不是强行宣称首创。
3. 中文简短说明你改正了哪些实质意思，以及现有数字支持什么、不能支持什么；不要要求实际重跑。

最后披露实际读取范围、继承上下文和截断情况。

## Response

**1. 英文摘要**
173词，按空格计词；开头两句原文保留。

Fault diagnosis under changing operating conditions is complicated by scarce and unevenly distributed fault labels. This study develops a diagnostic approach that learns from labeled source measurements and unlabeled measurements from a target condition. A shared encoder supports a diagnostic head D and an auxiliary head E, both trained with source labels. E's training objective additionally incorporates logit adjustment based on source class proportions. During adaptation, counting E's predictions on the unlabeled target adaptation pool estimates its class proportions. Comparing this estimate with three preset reference distributions sets the strength of logit adjustment for D through a fixed rule. D's adjusted logits for weakly augmented target samples yield hard pseudo-labels that supervise classification of strongly augmented views of the same samples, updating the encoder and D. After adaptation, only the encoder and D classify new samples, with fixed parameters. In one independent target evaluation of a simulated process, fault recall increased from 50% to 80%, whereas the normal-sample false-positive rate rose from 5% to 17.5% and overall accuracy declined from 86% to 82%.

**2. 候选贡献**
An adaptation procedure links an auxiliary head trained with source-proportion-based logit adjustment to target pseudo-label supervision: counted target predictions estimate class proportions, comparison with preset reference distributions determines diagnostic-logit adjustment strength, and hard pseudo-labels derived from the adjusted weak-view logits supervise strong-view classification. This makes updates to the shared encoder and diagnostic head responsive to estimated target class composition, while subsequent prediction uses only these two components with fixed parameters.

作者说明：这是一条依据给定实现组织的**候选方法贡献**，不是已确认的新算法。最近文献及新颖性比较尚未提供，相对既有工作的具体增量仍待作者确认；当前不宣称首创，也不将普通编码器或完成一次实验另列贡献。

**3. 实质修正**
- **事实纠正：**删除“恢复全部过程信息”；E 输出的是受预测错误影响的类别比例估计，不是无条件识别出的真实目标先验。
- **关系澄清：**比例估计经预设参考分布比较控制 D 的调整强度，再形成弱增强硬伪标签，监督同一样本的强增强分类。参考分布并非“prior-free”，这些操作也不保证伪标签无偏。
- **阶段纠正：**上述关系发生在适配阶段，不是部署时融合。新样本分类仅使用编码器和 D，不调用 E、适配池或模板比较，也不更新参数。

给定计数支持以下描述性结果：

| 指标 | 基线 | 方案 |
|---|---:|---:|
| 故障召回率 | 50% | 80% |
| 正常召回率 | 95% | 82.5% |
| 正常样本误报率 | 5% | 17.5% |
| 总体准确率 | 86% | 82% |
| 平衡准确率（两类召回率均值） | 72.5% | 81.25% |

在这100个评价样本中，方案**少漏判6个故障，同时多误报10个正常样本**。因此，可以报告故障敏感性及平衡准确率提高，但不能称为全面优越；没有误判成本信息，也不能断言工程净收益。一次仿真评价不能支持所有工况有效、实地产线适用、提前预警、重复运行稳定性或统计显著性，更不能单独证明某个部件造成了改善。

**读取与上下文**
实际读取范围如下，均为公开 Skill/参考：
- 指定目录的[英文总控入口](../../SKILL.md)及[中文总控入口](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)，全文。
- [摘要贡献英文 Skill](../../skills/engineering-abstract-contributions/SKILL.md)及[中文 Skill](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)，全文。
- [中文写法参考](../../references/abstract-and-contribution-craft_CN.md)，第1–43、48–100行；[英文对应参考](../../references/abstract-and-contribution-craft.md)，仅检索标题。
- 另读取通用流程 Skill (platform-local path omitted)，并作一次只读额度查询。

继承上下文包括本轮指令、AGENTS/环境信息及自动注入的记忆摘要；未主动读取记忆文件或私有维护记录，也未用继承记忆补充本算例事实。未读取 `evals/tests`、真实论文或其他项目；未联网、改文件、训练或委派。技术对应仅依据题目确认的事实，未核查实现代码。本轮未出现上下文压缩提示或工具输出截断；上述节选属于主动限定读取范围。
