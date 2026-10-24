# Fictional Loss-Factor And Logit-Offset Final Response

One new task context answered the unchanged A/B request on the frozen final source; only the read root changed from the baseline. Baseline science and writing already passed. Only writing wrappers, local links/line suffixes and whitespace are normalized; raw prompts and responses remain private.

预置历史披露：上下文含该包早期维护摘要；以下判断仅依据本次实际读取的文件，不据历史声称当前问题已修复或整库已认证。A/B 均按虚构请求处理；本次未浏览、修改文件、运行科研实验或调用代理。

**A．操作核对**
三者不能仅因都用于应对不平衡，就互换名称、公式或训练／预测用途。关键是系数进入哪里、改变什么、在哪个阶段使用。以下采用自然对数，不假定任何软件默认 `reduction`。

1. **训练时外乘真实类别交叉熵项。** 原始 softmax 为 `[1/2,1/2]`。按给定固定分母 1：
   \[
   L_1=\frac{\alpha_2[-\log(1/2)]}{1}=3\log2\approx2.079442.
   \]
2. **训练时在 logit 内加先验偏置，再算普通交叉熵。** 调整后的 softmax 为 `[3/4,1/4]`，没有外乘因子：
   \[
   L_2=-\log\frac{e^{z_2+\log\pi_2}}{\sum_c e^{z_c+\log\pi_c}}
   =-\log(1/4)=\log4\approx1.386294.
   \]
3. **预测时减去对数先验。** 判类分数为：
   \[
   z-\log\pi=[0.287682,\;1.386294],
   \]
   因而预测第二类。这是预测端分数校正，不能据此把前两种训练操作移到预测端，或把加号、减号视作可互换写法。

若操作 1 改为除以**本次单样本实际权重之和**，分母是 \(\alpha_y=3\)，不是全部类别因子的和 \(1+3\)。此时 \(L'_1=3\log2/3=\log2\approx0.693147\)，**结果不保持不变**。这里只说明该单样本的正权重被分母抵消，不代表一般批次中的类别加权无效。

**当前库的准入状态：未完成完整匹配双论文记录。** 本次核对的是包内证据记录，没有重新读取原论文或核验其实现：

| 包内记录 | 能支持什么 | 不能据此补足什么 |
|---|---|---|
| P96，p.3，Eqs.(3)–(4) | 一篇论文的背景段明确给出类别因子外乘交叉熵 | 其 p.6 提出的方法另含 logit margin，不能把背景定义当作整个源方法 |
| P97，p.4 Table 1 与 p.8 Eqs.(35)–(36) | 前者出现类别加权表达式 | 后者是二元交叉熵加整体目标系数；内部差异未解决，不能算干净的第二个匹配定义 |
| P18 | 训练损失内部的先验 logit 调整，以及另一处伪标签构造 | 不是外乘类别因子的第二个定义，也不能自动移作最终诊断预测 |
| P92／P93／P94、P39 | 分别涉及生成选择、残差加权、增强原型选择和预测相关 focal 因子 | 共享“weight”或不平衡目的，不等于相同运算 |

中文条目记录了 `weighted cross-entropy loss / 加权交叉熵损失（函数）` 的双语摘要对应，但没有损失方程，只支持译词，不补足两篇英文运算定义。词语出现、单篇背景定义、整个源方法一致性是三个不同层次。准入未完成不禁止正确的数学操作：仍可准确描述“类别因子缩放真实类别的训练交叉熵项”，不把标准损失自动包装成新模块。

**B．英文文本**
方法总览：53 词，按空格计数，连字符词计一词。

BalanceFlowFD uses a temporal encoder and classifier to assign fault classes to process measurements. During training, loss coefficients are updated using both training class counts and per-class errors from the current training round. These coefficients scale the true-class cross-entropy terms used to train both components. Prediction uses the trained encoder and classifier alone.

关联贡献候选：29 词，同一计数规则。

BalanceFlowFD couples training class counts and current-round per-class errors to update loss coefficients, which scale true-class cross-entropy terms to train the temporal encoder and classifier retained for fault diagnosis.

第二段把“类别计数与本轮类别误差共同驱动的系数更新规则”连接到所训练并保留的诊断器，而非把采用加权交叉熵本身当创新。最近前作检索尚未完成，因此它只是**关联贡献候选**，不是已确立的新颖性结论。系数公式与选择记录留在方法／设置；总览不添加目标适应、额外支路或在线更新。

结果解释应收束到给定匹配比较：**weighted F1 提高，但 macro F1 降低，少数类表现有升有降。** 这体现不同聚合口径及类别表现之间的取舍，不能写成普遍诊断改善或少数类一致受益；也不能由这些指标推出物理误分类成本下降。逐类差异放结果分析，必要的取舍放结果总结，不把全部核查排除项塞进方法总览。

**实际读取文件**
正文或相关片段核读：
- [SKILL.md](../../SKILL.md)
- [中文总控 SKILL.md](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)
- [摘要与贡献 SKILL.md](../../skills/engineering-abstract-contributions/SKILL.md)
- [terminology-decisions.md](../../references/terminology-decisions.md)
- [engineering-application-terminology-bank.md](../../references/engineering-application-terminology-bank.md)
- [published-evidence.md](../../references/published-evidence.md)
- [abstract-and-contribution-craft.md](../../references/abstract-and-contribution-craft.md)
- [topic-playbooks.md](../../references/topic-playbooks.md)
- [experiment-evidence-design.md](../../references/experiment-evidence-design.md)

另仅读到检索命中行，未作正文核读：
- [figure-and-latex-production.md](../../references/figure-and-latex-production.md)
- [engineering-application-terminology-bank_CN.md](../../references/engineering-application-terminology-bank_CN.md)
- [corpus-calibration-workflow.md](../../references/corpus-calibration-workflow.md)
- [术语润色 SKILL.md](../../skills/engineering-terminology-polishing/SKILL.md)
- [严谨性审查 SKILL.md](../../skills/engineering-journal-rigor-review/SKILL.md)
