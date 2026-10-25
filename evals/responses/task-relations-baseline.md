# Related Quality Targets: Earlier Guidance

Fictional teaching study only; no real experimental result or private paper is included. One first-answer context received the same request with zero feedback. Inherited context and read limits are disclosed in the response. Only machine-path displays and writing-block wrappers are normalized for portability.

## Request

# Fictional multivariate soft-sensing writing request

Use the current Engineering Application Journal Writing Skill at
`the repository root`.
Read the relevant current instructions/references, not previous evaluation
responses/reviews, private maintenance files or other manuscripts. All facts
below describe a fictional teaching study; do not run research experiments,
edit files or access external services. A required read-only quota check under
the workspace policy is permitted; no account changes or paid fallback.

Our paper estimates two quality quantities from process measurements: A is a
concentration measured in mass percent and B is a concentration measured in mg/L.
The laboratory does not measure both quantities for every historical window.
The availability of A and B is separately recorded. We have no evidence about
why either assay is missing. At prediction, only permitted process measurements
enter the model; neither current quality value is an input.

The implemented design uses a shared encoder and shared expert features.
Different gates combine those expert features for the A and B predictor heads.
During fitting, each target's loss is computed only where its measured reference
is available and is normalized by that target's available-label count. A
training-only rule adjusts task-loss coefficients using gradients on the shared
encoder. Those coefficients are not the gates' expert weights. Both prediction
heads remain at inference, but the loss-coefficient update does not execute then.
The task-specific expert-sharing and gradient-based coefficient rules are
adapted from established methods; our claimed engineering adaptation handles
the separately recorded quality-reference availability. We have not completed
a search proving that adaptation new.

The held-out evaluation contains measured references for both quantities. The
following are supplied synthetic point estimates from the same held-out windows,
using the same input information and each target's corresponding training labels:

| Fitting arrangement | A MAE, mass-percent units | B MAE, mg/L |
|---|---|---|
| Separate single-target predictors | 0.50 | 20 |
| Shared model with fixed task-loss coefficients | 0.40 | 24 |
| Implemented availability-aware joint design | 0.38 | 18 |

No isolated control for the gradient rule or gating rule, uncertainty estimates,
other sites, new operating conditions, live deployment or control outcomes are
supplied. An internal draft says: "The average MAE decreases from 10.25 to 9.19,
proving that each newly invented module prevents negative transfer and improves
online product quality." The authors want to improve this writing, not to add
experiments or another model.

Draft one coherent English abstract of about 150 words and a short contribution
statement with whatever item count is justified. Make the relationships between
the operations clear without listing each as an independent invention or
inserting every implementation detail into the abstract. Put definite
corrections and unresolved scientific claims in a concise Chinese author note;
do not turn that note into a new experiment plan. State actual source reads,
inherited context and any truncated reads. Do not invent source citations,
results, assay procedures or physical explanations.

## First Answer

**Abstract**
148 words，按空格分词，连字符词计为一词。

This study examines joint soft sensing of two quality concentrations from process measurements when historical windows do not always have both laboratory references. The design adapts established task-specific expert sharing and gradient-based task balancing to the separately recorded availability of each target's reference. Target-specific gates form different combinations of shared expert features for the two prediction heads. Fitting uses each target's available references to compute its mean loss, with shared-encoder gradients guiding training-only adjustments of task-loss coefficients. Both heads subsequently estimate quality from process measurements alone. In this fictional teaching study, supplied synthetic held-out MAEs for A and B are 0.38 mass-percent units and 18 mg/L, versus 0.50 and 20 for separate predictors and 0.40 and 24 for fixed-coefficient joint fitting, respectively. Fixed-coefficient sharing improves A but worsens B relative to separate fitting; the availability-aware design has lower point-estimate errors for both targets on the same evaluated windows.

**Contribution**
合并为一项工程适配贡献；模型对比作为其支持证据，不另凑贡献条目。

We adapt established task-specific expert sharing and gradient-based task balancing to jointly estimate quality quantities with separately recorded reference availability. Each target's loss excludes unavailable references and is normalized by its available-label count, allowing joint fitting from the observed supervision while distinct gates combine shared expert features for the two quality predictors.

**作者说明**
- **确定修正：**原句中的 10.25、9.19 算术无误，但直接平均不同量纲的 MAE，不能得到有明确物理意义的共同误差指标。应分别报告：相对单目标拟合，A 的 MAE 降低 24%，B 降低 10%。按可用标签数归一化损失，不等于统一目标量纲。
- **关系澄清：**可用性标记决定各目标损失的计算范围和分母，不表示把缺失参考当作零，也不是缺失过程输入。分别记录不等于统计独立，更不能推出随机缺测；缺测原因仍未知。专家门权重与任务损失系数不同；后者仅在训练期更新，推理保留两个预测头，且不输入当前质量值。
- **未决主张：**专家共享和梯度规则来自既有方法，不能称为逐个“新发明”；可用性适配的文献新颖性尚未确立。整体比较不能识别门控或梯度规则各自的效果，也不能证明每个模块消除了负迁移。没有不确定性信息，不能宣称统计显著或稳定优势。
- **证据边界：**这里只支持给定虚构教学研究中的合成误差点估计比较，不支持跨站点、新工况、在线部署或产品质量改善。未提供正文、公式、图示或代码，因此未核验其与本段文字的对应关系；也未补造方法文献引用。

**读取与继承**
本次使用当前技能 **v4.2.29**，实际读取如下：

- 全文：主技能 (`SKILL.md`)、摘要与贡献技能 (`skills/engineering-abstract-contributions/SKILL.md`)、贡献论证 (`references/contribution-narratives.md`)、机制关联写作 (`references/abstract-and-contribution-craft.md`)、论证与行文 (`references/argument-and-prose-craft.md`)。
- 选段：术语判断 (`references/terminology-decisions.md`)中的对象、误差量纲、权重、标签、门控、软测量及证据范围；术语与风格 (`references/terminology-and-style.md`)第 5、8、9 节；章节指南 (`references/section-writing-guide.md`)第 1–95 行。另读取了通用会话技能规则 (generic workflow guide)。
- 一次跨文件检索输出被截断，相关条款随后定向重读；上述全文读取无截断，选段未视为全文。
- 科学事实仅取自题面。继承的工作区规则用于行为约束；系统预载历史摘要未作为证据。未打开记忆文件、旧评测或评审、私人维护材料或其他稿件。除获准的只读额度检查外，未访问外部服务；未运行实验或编辑文件。
