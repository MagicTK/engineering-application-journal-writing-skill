# Fictional Annotation-Acquisition Baseline

One task context answered two requests on the immutable v4.1.57 release. Scientific and writing distinctions already passed; the response correctly reported the absent active-learning source group and separate Chinese record, and identifies an ambiguous compact query-label instruction. Wrappers, local links/line suffixes and whitespace only are normalized; raw records remain private.

本次是**非记忆空白的预设虚构测试**。以下依据题设及 v4.1.57 包内记录，不代表真实实验复核；未联网、修改文件或运行实验。

**A．信息角色**
“Query labels cannot select the model”不能解释为所有名叫 query 的标签都禁用。[简写规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/d9162f3952a1a5f69689a0076b7fd33bf298740b/skills/engineering-experiment-evidence-design/SKILL.md#L68)存在被泛化的风险，而[专题说明](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/d9162f3952a1a5f69689a0076b7fd33bf298740b/references/topic-playbooks.md#L100)明确区分训练查询与评价查询。关键是**阶段、访问权限和实际用途**。

| 安排 | 信息角色及判定 | 能说明与不能说明的内容 |
|---|---|---|
| 1 | 从授权训练池选择待标注样本，获取真实标签，再监督拟合预测器；操作上属于池式 active learning，不是最终评价标签泄漏。 | 建立“选择样本→获取标注→扩大标注集→重拟合”的路径；单凭此安排不证明性能提高、人工节省或方法新颖。 |
| 2 | 训练 episode 的 query 标签提供监督损失，与最终评价 query 分离，属于合法训练监督。 | 说明查询标签的训练角色；不自动证明类别未见、样本独立或全流程标注成本低。 |
| 3 | 最终评价 query 标签用于选择 embedding width，属于超参数选择信息泄漏。 | 即使没有直接计算训练梯度，也破坏了该最终评价对模型选择的独立性。 |
| 4 | 题设的主动诊断设计选择工厂激励输入，以区分故障假设；选择对象是物理输入，不是待标注样本。 | 描述了激励与故障区分的设计目的；不构成标注查询，也不凭设计描述证明实测收益或因果识别。 |

**标注账：**新增查询 **30** 个不同样本的真实标签；累计获取 **12＋30＝42** 个。缓存复用于 **5 个训练 epoch** 不增加标注量，不能乘以五。这些是 oracle 提供的真实标签，不是模型生成目标；模型预测产生的伪标签即使用于训练，也应另列，不能计为新增真实标注。

若 oracle 只是揭示已有 benchmark 标注，测量的是**受限标签访问下的采集策略和预测表现**，不是实际专家标注工时、难度或费用。模拟查询次数不能直接换算为实际人工劳动节省。

**维护记录**
核对[英文已核验表](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/d9162f3952a1a5f69689a0076b7fd33bf298740b/references/engineering-application-terminology-bank.md#L331)、[中文对应表](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/d9162f3952a1a5f69689a0076b7fd33bf298740b/references/engineering-application-terminology-bank_CN.md#L136)及已发表证据索引后：

| 核查项 | 该版实际状态 |
|---|---|
| active-learning 基础操作的英文来源组 | **无已完成维护记录**；没有可报告的匹配来源对／多来源组、定义页码与操作范围。 |
| 完整基础中文对应 `active learning／主动学习` | **无单独完成的译法核验记录**；不能冒称该版已核验。 |
| 对应中文来源的阅读范围 | **无可报告记录**，不能补造双语标题、摘要、定义正文或全文阅读范围。 |

包内 P47 的记录涉及训练查询监督与预测查询边界，**不能拿来补成 active-learning 操作来源组**；标题出现 active、参考文献列出相关论文，也不算已读定义。

“Expert-Causal Class-Preserving Query Module”没有获批操作定义，不能靠基础词拼接获得准入。反过来，[名称规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/d9162f3952a1a5f69689a0076b7fd33bf298740b/references/engineering-application-terminology-bank.md#L29)允许作者批准且定义明确的新名称，**未入库不等于无效**。

英文按空白分隔计词，连字符不拆分；仅统计各块正文。

**方法句：32 词**
An acquisition selector requests true labels for samples from the authorized unlabeled training pool, adds them to the labeled set, and refits the diagnostic predictor while independent final evaluation labels remain sealed.

**B．摘要：127 词**
QueryBudgetFD addresses known-class industrial fault classification with limited acquired labels. A small labeled seed initializes a shared encoder-classifier. Each round, current classifier uncertainty and feature-space coverage jointly score the remaining authorized unlabeled training pool. Selected samples receive true labels from an oracle, leave the pool, and enlarge the labeled set for refitting the encoder-classifier. Acquisition continues up to a predeclared query budget. The retained encoder-classifier predicts known classes from new process measurements without oracle access. Choices are fixed independently of final evaluation labels. Comparisons use a simulated process benchmark and a held-out recorded-production case, with annotation simulated by revealing existing labels for selected training samples. With identical initial labeled seeds and numbers of newly acquired labels, QueryBudgetFD achieves higher weighted F1 than random acquisition in both cases.

**贡献候选：39 词**
QueryBudgetFD couples uncertainty and feature-space coverage scoring with training-label acquisition and encoder-classifier refitting, retaining the trained predictor for known-class diagnosis and achieving higher weighted F1 than random acquisition at matched initial seeds and label budgets in both evaluated cases.

**作者备注**
- 保留作者批准的英文名 **QueryBudgetFD**，不擅定中文名。贡献仍是候选：与最接近方法的差异和新颖性比较尚待完成，不能仅凭组合名称认定创新。
- 题设支持的是两个案例中**相同初始标注种子、相同新增标注数下，相对随机采集的 weighted F1 更高**；未提供增幅或显著性证据。
- 未测量实际人工标注时间、等 F1 下更少标签、跨厂迁移、因果识别或在线部署。无标签池用于采集评分，不据此补写伪标签训练、新类发现、强化策略或工厂激励。
