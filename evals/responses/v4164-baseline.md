# Fictional Information-Access Reference Baseline

One context answered A/B on immutable v4.1.63. Its science and writing already pass; it identifies one overbroad English instruction while preserving the correctly qualified Chinese rule. Wrappers, local path/link metadata and whitespace are normalized; the exact raw response remains private.

**A. 核查结论**
**允许保留，但必须限制解释。** 该列回答的是“在本数据上增加这项信息后，预测表现如何”，不是预测时点相同信息条件下的竞争，也不是已证明的最优上界。应明确分列、说明化验结果后到且部署不可用，并排除在同信息条件的胜负统计之外。

它不符合主任务的信息约束，但这不自动证明主方法泄漏，也不自动要求删列、删稿或重跑。

本次发现 **1 处局部过度限制**：

- **英文实验入口第96行**：[确切位置](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/563e971d7ca59774fd8c1e8d6c29cb7c3ea9398b/skills/engineering-experiment-evidence-design/SKILL.md#L96) 写道：“Do not compare a method using future information with one restricted to online-available variables.” 这里没有限定“作为公平主对比”，容易被执行成全面禁比。中文对应[第90行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/563e971d7ca59774fd8c1e8d6c29cb7c3ea9398b/skills-zh/engineering-experiment-evidence-design-zh/SKILL.md#L90) 已限定为不能“直接公平比较”，不应同样判错。**最小修正方向**：将英文禁令收窄为不得冒充同信息条件的公平竞争，并明确允许单独报告、限制解释的额外信息参考。

以下正确规则应保留，不另凑问题：

- [深层实验指南第95—101行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/563e971d7ca59774fd8c1e8d6c29cb7c3ea9398b/references/experiment-evidence-design.md#L95) 针对实际预测时点检查信息访问；主方法必须遵守，但不能扩张为禁止一切非匹配参考。
- 英文入口第98行、[深层指南第137行](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/563e971d7ca59774fd8c1e8d6c29cb7c3ea9398b/references/experiment-evidence-design.md#L137) 已区分源侧选择与声明的目标适应，并非无条件“只能训练/验证”。
- 已读的双案例、摘要和架构入口及相关指南，没有发现第二处与本情境直接冲突的明确禁令。摘要指南要求保留影响解释的信息边界，同时避免堆叠防御性声明，适用于这里。

**B. 可复用英文**
实验设置：两句，共61词。

The proposed method and the main comparison methods predict product quality using only process measurements available at the prediction time. A separately reported additional-information reference also uses laboratory quality assay results released later and unavailable at deployment, examining prediction performance with that extra input on this dataset rather than serving as an online competitor; it is excluded from same-information win-loss counts.

结果解释：一句，共30词，不预设优劣。以上均按空格计词，连字符复合词计一词。

This comparison examines how product-quality prediction on this dataset varies with access to the additional laboratory assay information, rather than which method performs best under the same prediction-time information constraint.

**读取范围**
科学判断是“可保留、限解释”；当前文本问题是英文实验入口的局部禁令过宽。两者不等于对未提供的实验结果作认证，也不构成整库通过。

历史披露：会话预置了早期版本摘要，我也只读查阅了历史索引；未以历史记录推断当前已修复。全过程未修改文件、浏览外链、运行科研实验或调用代理。

实际正文读取文件如下；参考文件为相关段落核对，关键词检索命中不视为全文读过：

- 总控：[英文](../../SKILL.md)、[中文](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)。
- 实验：[英文](../../skills/engineering-experiment-evidence-design/SKILL.md)、[中文](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)。
- 通用基准与真实案例：[英文](../../skills/general-method-benchmark-realworld/SKILL.md)、[中文](../../skills-zh/general-method-benchmark-realworld-zh/SKILL.md)。
- 摘要：[英文](../../skills/engineering-abstract-contributions/SKILL.md)、[中文](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)。
- 论文架构：[英文](../../skills/engineering-paper-idea-architecture/SKILL.md)、[中文](../../skills-zh/engineering-paper-idea-architecture-zh/SKILL.md)。
- 对应参考：[实验与证据](../../references/experiment-evidence-design.md)、[论文范式](../../references/manuscript-archetypes.md)、[摘要英文指南](../../references/abstract-and-contribution-craft.md)、[摘要中文指南](../../references/abstract-and-contribution-craft_CN.md)、[章节指南](../../references/section-writing-guide.md)、[研究规划与贡献边界](../../references/research-planning-and-contribution.md)。
- 包外辅助读取：流程说明 (private local reference)、历史索引 (private local reference)。
