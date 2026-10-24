# Fictional Query-Phase Corrected-Source Retest

One new task context answered the unchanged A/B request on the corrected 102-file final snapshot. An intermediate v61 audit found remaining compact input-adaptation restrictions, which were corrected before this retest; its raw response and source fingerprint remain private. Baseline and intermediate science/writing already passed. Only wrappers, local links/line suffixes and whitespace are normalized. See the evaluation review for scope and limits.

我有预置历史上下文，不能称为 memory-blank。以下仅依据本次实际读取的当前包，不凭历史宣称“已修复”；全程未修改文件、运行实验、浏览或调用代理。

**A. 六项判断**
判断依据是**阶段、实际信息访问及用途**，不是 `query` 这个名称；标签不进入反向传播，也仍可能影响模型选择。

1. **可用：训练 query 监督。** 元训练 query 标签用于监督损失并更新编码器，本身不是测试泄漏。须保留基础数据来源、episode及support/query成员记录、损失定义与参数更新记录，并说明其与最终评价数据的边界。

2. **可用：真实独立验证上的选择。** 验证 query 标签可以选择embedding宽度和停止epoch，随后在未参与选择的最终集合评分。须保留原始划分及独立单位、候选配置、验证指标与选择规则、最终模型冻结记录、最终预测与评分记录。“记录过”不能代替实际隔离。

3. **不能作为独立最终评价。** 用最终 query 标签挑best checkpoint已经让评价答案影响模型选择，无须发生反向传播。可以如实报告为经该集合选择后的结果，但不能继续称其为未参与选择的最终评价。须保留全部候选、比较历史及选择依据。

4. **可用：训练拟合排序，验证选择数量。** 验证标签决定保留特征数属于模型选择，不等于最终测试泄漏。须分别记录排序拟合数据、排序结果、验证候选数量及指标、选定子集，以及最终预测器实际采用的拟合流程。

5. **不能靠改名恢复独立性。** 反复比较过的同一集合不会因改称validation而成为独立最终测试。须保留原始用途、比较和决策历史、样本归属及重叠记录。**来自同一总体并非问题本身**：另取真正独立且未参与选择的样本可以支持最终评价，但题设未提供这种证据。

6. **在声明条件下可用：批次无标签目标适应。** 目标测量统计可以拟合选择器；这不是training-only选择，也不授权访问目标真实标签。须保留目标批次成员、统计量及拟合状态、真实标签的隔离用途、比较方法的匹配访问条件。结论应限定在该批次访问设置，不能自动扩展为纯归纳或实时流式能力。

**当前文本核对**
- 中英文构思入口的[中文第59行](../../skills-zh/engineering-research-ideation-zh/SKILL.md)与[英文第59行](../../skills/engineering-research-ideation/SKILL.md)，都允许训练query监督和实际划定的验证query选模型，同时禁止最终评价标签选模型。**未见实质中英冲突，无必改项。** 可选的最小澄清是明确验证episodes与训练、最终评价的隔离，而非把所有query标签统一禁用。
- [research-planning-and-contribution第33行](../../references/research-planning-and-contribution.md)起的段落，也明确区分上述阶段，并禁止事后改名冒充独立评价。没有把合法训练监督、验证选择或无标签访问一概判错。
- [特征选择证据段第376行](../../references/experiment-evidence-design.md)明确并列training-only、预定义设置、验证选择和无标签目标池拟合。“Supervised selection is part of model fitting”结合后文，并非禁止验证选特征数。若担心混淆，可最小澄清为“监督选择会影响最终预测器，并分别记录选择器拟合与配置选择的数据”；这是可选措辞调整，不是第4、6项已被当前文本否定。

因此，这些定点段落**未发现必须纠正的一刀切禁令**；这不是全包行为测试或全部规则通过的结论。

零样本最终评价语境下，“不使用评价query标签”**无需机械删除**：若可能被理解为连评分也禁止，最小限定为“仅用于评分，不用于拟合或选择”。`training-only schedule`作为确实采用的一种设置也可保留；不能将其提升为唯一合法选项，更不能代替本题已经给定的验证选择或目标适应事实。

**B. 可复用英文**
方法总览，60词；保留训练到最终匹配预测的关系，不把常规组织包装成新颖性。

EpisodeAxisFD learns an encoder and a specified matching function from episodes constructed using labeled base data, with training support features and supervised query losses guiding training. During final evaluation, labeled support examples define references for the current classes, and the trained encoder maps each query into the learned embedding space for matching against these references to predict its fault class.

选择设置，45词；将验证选择、参数冻结和最终评分边界集中在这里。

Embedding width and stopping epoch are selected using query annotations from documented validation episodes separate from training and final evaluation. The selected model is then frozen: final labeled support examples form class references without parameter updates, and final query labels are used only for scoring.

**实际读取**
以下包含完整入口读取及关联指南的定点检索、段落读取，不表示所有指南均已通读：
- [总入口SKILL.md](../../SKILL.md)
- [中文构思入口](../../skills-zh/engineering-research-ideation-zh/SKILL.md)、[英文构思入口](../../skills/engineering-research-ideation/SKILL.md)
- [research-planning-and-contribution.md](../../references/research-planning-and-contribution.md)、[experiment-evidence-design.md](../../references/experiment-evidence-design.md)
- [中文证据设计入口](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)、[英文证据设计入口](../../skills/engineering-experiment-evidence-design/SKILL.md)
- [topic-playbooks.md](../../references/topic-playbooks.md)、[abstract-and-contribution-craft.md](../../references/abstract-and-contribution-craft.md)
- [section-writing-guide.md](../../references/section-writing-guide.md)、[argument-and-prose-craft.md](../../references/argument-and-prose-craft.md)

这些虚构设计及文字判断，不能证明真实稿件的数据独立性，也不能证明投稿、录用或科学验证状态。
