# Auxiliary Guidance: Revised-Source Use

Fictional inputs; suite 4.2.21. A separate responding context received the same original request, not the earlier answer or private criteria. One later editorial message in the same context is not an independent retest. Suite paths and display formatting are normalized; scientific content is preserved.

## Original Request

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

## First Answer

**1. 英文摘要**
约174词，按空格计词；开头两句保持原文。

Fault diagnosis under changing operating conditions is complicated by scarce and unevenly distributed fault labels. This study develops a diagnostic approach that learns from labeled source measurements and unlabeled measurements from a target condition. A shared encoder supports a diagnostic head and an auxiliary class-estimation head, both trained on source labels; the auxiliary objective additionally includes source-proportion-based logit adjustment. The auxiliary head's predictions on the unlabeled target adaptation pool are counted to estimate class proportions, which are compared with predefined reference distributions to set an adjustment strength using a fixed rule. This strength controls adjustment of the diagnostic head's logits on weakly augmented target samples before hard pseudo-label assignment. These pseudo-labels supervise strongly augmented views of the same samples, updating the encoder and diagnostic head. After adaptation, the encoder and diagnostic head classify new samples with fixed parameters. In one independent target evaluation from a simulated process, fault recall increased from 50% to 80%, while normal-class recall decreased from 95% to 82.5% and overall accuracy fell from 86% to 82% relative to the baseline.

**2. 候选贡献**

We link auxiliary estimation of target class proportions to diagnostic-head pseudo-label learning through fixed-rule comparisons with predefined reference distributions. An auxiliary head trained with source-proportion-based logit adjustment supplies these estimates from unlabeled target measurements; the resulting adjustment strength regulates the diagnostic head's logits on weakly augmented views before hard pseudo-label assignment. These labels supervise strongly augmented views of the same samples, updating the shared encoder and diagnostic head so that target-pool information shapes the final fixed-parameter classifier.

作者说明：这是对已实现操作及其联系的**候选贡献表述，不是新颖性结论**。相对最近工作的具体增量仍待文献对照确认；当前整体比较也不能证明每个环节的独立效果。

**3. 实质修正**
- 删除“恢复全部过程信息”。共享编码器支撑两个任务头，不等于保全全部信息。
- 将“无假设识别真实目标先验”改为“根据辅助头预测计数估计类别比例”。源比例调整、预设参考分布和固定规则均有实际作用，不能称为“prior-free”，也没有无偏伪标签保证。
- 明确适配与预测的边界：调整的是诊断头弱增强视图的 logits，由此产生的硬伪标签监督强增强视图；适配后仅编码器和诊断头分类，不融合两头概率，不继续更新参数。

现有数字支持以下**单次评价中的取舍**：

| 指标 | 基线 | 方案 |
|---|---:|---:|
| 故障召回率 | 50% | 80% |
| 正常类别召回率 | 95% | 82.5% |
| 总体准确率 | 86% | 82% |
| 平衡准确率（两类召回率均值） | 72.5% | 81.25% |

即漏判故障由10个降至4个，同时正常样本误报由4个增至14个。不能据此宣称全面优越、所有工况有效、统计显著、实际产线适用或提前预警，也不能证明比例估计准确、伪标签无偏或某个组件单独带来改善。

**读取披露**
文件读取仅限指定目录内以下五个公开文件：
- [英文总控入口](../../SKILL.md)：第1–220行。
- [中文总控入口](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)：第1–240行范围。
- [英文摘要与贡献 Skill](../../skills/engineering-abstract-contributions/SKILL.md)：第1–300行范围。
- [中文摘要与贡献 Skill](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)：第1–220行范围。
- [摘要与贡献参考](../../references/abstract-and-contribution-craft.md)：标题索引及第1–61、70–101行，未读可选案例正文。

继承上下文中存在预置的历史项目摘要，本次未采用，也未另读记忆文件；算例依据仅为你本轮提供的事实与数字。上述工具输出未报告截断，选读不等于全文审查。未读 `evals/tests`、私有维护记录、真实论文或其他项目；未联网、改文件、训练或委派。实现和结果按题设接受，未声称完成代码或原始数据核验。

## Editorial Feedback

科学含义、原开头和数字判断都保持。这版不再使用D/E符号，作用也连清楚了；我还希望做一次编辑性打磨：摘要中部与贡献仍有按事实表逐步转述的读感。请基于已读Skill再作一版，把“类别比例估计如何调节伪标签学习”作为组织关系来讲，辅助头的源侧训练细节可合并到其作用说明，不必为每个支撑步骤单列主句。贡献也围绕该联系及对最终诊断器的作用组织，避免再次完整复述算法。不能把有事实依据的估计、参考模板和弱/强视图关系删没，也不能新增效果、创新保证或部署融合。不要为了变短而删除必要含义，不必机械凑180词。只返回修订摘要、一条候选贡献和实际改动说明；原请求的作者说明及科学边界继续有效。

## Final Answer

**修订摘要**

Fault diagnosis under changing operating conditions is complicated by scarce and unevenly distributed fault labels. This study develops a diagnostic approach that learns from labeled source measurements and unlabeled measurements from a target condition. Pseudo-label learning is regulated by an estimate of target class proportions obtained from prediction counts over the unlabeled adaptation pool. An auxiliary head supplies this estimate, sharing the encoder and source-label supervision with the diagnostic head while additionally using source-proportion-based logit adjustment in its training objective. Through fixed-rule comparisons with predefined reference distributions, the estimate controls the strength of diagnostic logit adjustment on weakly augmented target samples, whose hard pseudo-labels supervise strongly augmented views of the same samples. This supervision updates the encoder and diagnostic head, which together classify new samples with fixed parameters after adaptation. In one independent target evaluation from a simulated process, fault recall increased from 50% to 80%, while normal-class recall decreased from 95% to 82.5% and overall accuracy fell from 86% to 82% relative to the baseline.

**候选贡献**

We connect pool-level estimation of target class proportions to sample-level pseudo-label learning through logit adjustment governed by fixed-rule comparisons with predefined reference distributions. This connection allows the auxiliary estimate to shape the shared encoder and diagnostic head through supervision of strongly augmented views by hard pseudo-labels from weakly augmented views, incorporating information from the unlabeled adaptation pool into the final fixed-parameter diagnostic predictor.

**实际改动**
- 摘要以“比例估计调节伪标签学习”为组织关系，将预测计数作为估计来源，将辅助头的共享结构、源标签监督及源比例调整合并到其作用说明。
- 将参考分布比较、调整强度、弱视图伪标签与强视图监督连成同一关系句，再承接其对最终诊断器的训练作用。贡献仅保留这条联系，不再完整复述辅助头训练和估计步骤。
- 原开头、结果数字及其取舍保持不变；未增加效果、新颖性保证或部署融合。仅使用已读 Skill 和题设，未新增文件读取；原作者说明及科学边界继续有效。
