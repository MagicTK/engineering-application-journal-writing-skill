# Fictional Query-Phase Baseline

One context answered A/B on immutable v4.1.60. Core science/writing already passed; the actual response independently identified three overbroad or bilingual-inconsistent instruction locations. Only wrappers, local links/line suffixes and whitespace are normalized; raw records remain private.

已有预置历史摘要，因此本次不是 memory-blank；未读取历史记忆文件，也不据历史声称当前包“已修复”。以下仅依据本次读到的当前包及题设，未修改文件、训练、浏览或调用代理。

**A. 逐项判断**
判断依据是阶段、用途和实际信息访问，不能仅凭 `query` 名称决定权限。以下接受题设已经明确给定的隔离条件，不要求重复证明这些虚构事实。

| 项目 | 可用性与条件 | 作者应保留的证据 |
|---|---|---|
| 1 | **可用。** 元训练 query 标签属于训练监督，可通过损失更新编码器，不等于最终测试标签泄漏。 | 训练 episode 构造、标签来源、损失定义和参数更新路径。 |
| 2 | **可用。** 真实独立的验证 query 标注可以选择宽度与停止 epoch；另一个未参与选择的最终集合承担评价。验证标签没有参与梯度，也仍属于模型开发资源。 | 三阶段划分及独立单位、候选设置与验证选择日志、冻结模型及最终评价记录。 |
| 3 | **不能据此声称独立最终评价。** 用最终 query 标签选 best checkpoint 已让评价反馈影响模型选择；不反向传播不能消除这种影响。 | 全部候选与评分、checkpoint 选择规则及时间线，如实记录该集合已经承担选择角色。 |
| 4 | **可用。** 训练数据拟合排序，隔离验证标签选择保留数量，是合法的拟合与选型分工；不必全部限制为 training-only。 | 排序拟合的数据与处理过程、验证集身份、数量候选与选择日志、最终固定特征集合和测试记录。 |
| 5 | **不能仅靠改名恢复独立性。** 本题没有给出新的隔离事实，不能继续将已经反复比较的数据称为独立最终测试。注意：来自同一总体本身不排斥独立新留出，问题在实际使用历史。 | 原划分、历次比较及其影响的决策、改名记录、最终报告所用数据身份；不能删除历史来制造“未使用”。 |
| 6 | **在已声明的批次无标签目标适应设置下可用。** 目标测量统计可拟合选择器，应保留其真实访问范围及匹配比较；不能改写成 training-only，也不能扩展为目标真实标签可用于拟合或选型。 | 目标批次范围、统计量及拟合过程、访问时序、标签隔离记录，以及各比较方法的信息访问设置。 |

**当前包的局部问题**
以下是措辞范围问题，不意味着相关行为全部失败。

1. **中文入口过宽，且中英不完全一致。** [中文构思入口第59行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/c1263c8bdd896d495a012b4bcd6eaa7ad58f7d6a/skills-zh/engineering-research-ideation-zh/SKILL.md#L59)写“模型选择不接触查询标签”；[英文对应第59行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/c1263c8bdd896d495a012b4bcd6eaa7ad58f7d6a/skills/engineering-research-ideation/SKILL.md#L59)只要求“separate model selection”。最小方向：将禁用对象限定为**保留作最终评价的 query 标签**，明确真实隔离的验证 query 标签可用于选型，并保持训练 query 监督的合法角色。

2. **研究规划指南同样缺少阶段限定。** [research-planning-and-contribution 第33行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/c1263c8bdd896d495a012b4bcd6eaa7ad58f7d6a/references/research-planning-and-contribution.md#L33)写“freeze model/hyperparameter selection independently of query labels”。最小方向：在这里限定为**最终评价 query 标签**；如实际存在独立验证 episodes，应如实记录其标签选型用途，不强制所有研究另设验证集。

3. **特征选择段将合法选项列得过窄。** [实验证据指南第376行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/c1263c8bdd896d495a012b4bcd6eaa7ad58f7d6a/references/experiment-evidence-design.md#L376)要求“training-only selection procedure or a predefined setting”。作为通用指令，这遗漏了第4项的真实独立验证选型和第6项的已声明无标签目标拟合。最小方向：要求报告**实际执行、符合任务权限的拟合与选择过程**，保留 training-only、预定义设置，并容纳上述两种合法情形；继续禁止最终评价标签驱动选择及虚构验证划分。

包内也已有正确区分：中英实验证据入口第68行明确允许训练 episode query 监督，并禁止最终评价标签选模型；实验证据指南第91行及第324—345行区分了合法目标池访问与目标标签驱动选择。因此，这是局部收窄与一致性问题。

**不需要机械删除另外两类表述。** 零样本最终评价中“不使用评价 query 标签”若指不用于预测、拟合和选型，应保留，同时允许标签用于最终评分，也不能扩大成禁止一切历史监督或无标签目标访问。`training-only schedule` 若确为实际采用、未受最终评价反馈影响的训练安排，也可保留；应删除的是其“唯一合法选项”的暗示，而不是选项本身，更不能拿它替换第2、4、6项的真实设计。

**B. 可复用英文**
方法总览，62词，保留训练到最终匹配预测的关系，不将常规组织包装为创新：

EpisodeAxisFD learns an encoder and the specified matching function from labeled base-data episodes, using training support features and a supervised loss on training queries. At final evaluation, encoded support examples and their labels define references for the current classes. The learned encoder maps query examples into the embedding space, where the matching function compares them with these references to predict fault classes.

选择设置，43词，将验证选型和最终评价边界集中交代：

Embedding width and the stopping epoch were selected using query annotations from recorded validation episodes separated from both training and final evaluation. After selection, model parameters were frozen. Final query labels were used only for scoring, without checkpoint selection or online parameter updates.

**实际读取范围**
完整读取的入口或指南：
- [包总入口](../../SKILL.md)；[中文研究构思](../../skills-zh/engineering-research-ideation-zh/SKILL.md)；[英文研究构思](../../skills/engineering-research-ideation/SKILL.md)。
- [研究规划与贡献边界](../../references/research-planning-and-contribution.md)；[中文实验证据入口](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)。

读取相关段落或作定向检索的关联文件，未声称全部精读：
- [英文实验证据入口](../../skills/engineering-experiment-evidence-design/SKILL.md)；[实验证据指南](../../references/experiment-evidence-design.md)；[专题指南](../../references/topic-playbooks.md)。
- [章节写作指南](../../references/section-writing-guide.md)；[摘要与贡献写作](../../references/abstract-and-contribution-craft.md)；[论证与行文](../../references/argument-and-prose-craft.md)。
- [术语决策](../../references/terminology-decisions.md)；[术语与风格](../../references/terminology-and-style.md)；[研究协作流程](../../references/research-collaboration-workflow.md)。

这些虚构设计只能用于条件判断和文字测试，不能证明任何真实稿件的数据独立性，也不能证明其投稿或录用状态。
