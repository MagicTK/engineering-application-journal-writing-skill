# Fictional Loss-Factor And Logit-Offset Baseline

One context answered A/B on immutable v4.1.61. Core arithmetic, scientific distinctions and linked writing already passed; current matched-name evidence was correctly reported as incomplete. Only wrappers, local links/line suffixes and whitespace are normalized; raw records remain private.

披露：上下文含早期版本的预置历史，本次不将其作为当前包的证据。以下仅依据本次读取的 v4.1.61 包内内容和虚构题设，不代表整库认证；未浏览、改文件、启动科研实验或调用代理。

**A. 操作核对**
不能仅因都用于应对不平衡，就互换名称、公式或训练/预测用途。三者分别改变训练损失幅度、训练 softmax 分布和预测排序。

以下使用自然对数，温度为 1，不采用任何软件默认 reduction：

| 操作 | 按题设计算 |
|---|---|
| 1. 外乘类别因子，固定分母为 1 | 原 softmax 为 \([1/2,1/2]\)。\(L_1=-3\log(1/2)=3\log2\approx2.079442\)。 |
| 2. 训练 logit 加 \(\log\pi_c\)，再算普通交叉熵 | 调整后为 \([\log(3/4),\log(1/4)]\)，softmax 为 \([3/4,1/4]\)。\(L_2=-\log(1/4)=\log4\approx1.386294\)，没有外乘因子。 |
| 3. 预测使用 \(z_c-\log\pi_c\) | 分数约为 \([0.287682,1.386294]\)，因此预测**第二类**；原始 logits 则并列。 |

若操作 1 改为除以该单样本的权重总和 \(\alpha_y=3\)，则
\[
L'_1=\frac{3\log2}{3}=\log2\approx0.693147。
\]
**结果改变**。归一化是损失定义的一部分，不能省略后宣称等价；这个单样本的权重抵消也不能推广为任意批次都没有类别加权效果。

**当前库的准入状态：没有完成记录。** [术语库的权重边界](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/62ba3b4c2c63f542bbfdb79ff7b8491d624510fb/references/engineering-application-terminology-bank.md#L397)明确说明，现有材料没有完成 `class weighting in classification loss / weighted cross-entropy` 的匹配双论文定义记录：

- 包内记录中，P92 对生成样本的选择加权，P93 对拟合残差加权，P94 对增强原型选择加权；P39 使用预测相关的 focal 因子。这些不是同一个运算的配对定义。
- `weighted cross-entropy loss / 加权交叉熵损失` 的双语摘要配对只支持词语对应；记录注明可读材料没有损失方程，不能补成完整运算或双论文准入。
- 按[准入规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/62ba3b4c2c63f542bbfdb79ff7b8491d624510fb/references/engineering-application-terminology-bank.md#L40)，单篇对既有操作的实质性背景定义可以算一个来源，但词语出现不够，一个来源不等于两个，其背景定义也不保证整个源方法采用同一运算。本轮未复核原论文。

这不妨碍保留“固定类别因子缩放真实类别的训练交叉熵项”等准确功能描述，也不应把标准损失自动包装成新模块。

**B. 可复用英文**
方法总览，59 词；按空格计词，连字符复合词计一词：

BalanceFlowFD classifies faults from process measurements using a temporal encoder and classifier. In each training round, class counts from the training set and that round's class-specific errors jointly determine updated loss coefficients. These coefficients scale the cross-entropy term for each sample's true class to train both components. Prediction uses the trained encoder and classifier directly, without coefficient-based score scaling.

关联贡献候选，32 词：

BalanceFlowFD couples a loss-coefficient update driven jointly by training class counts and current-round class-specific training errors with true-class cross-entropy scaling to train the temporal encoder and classifier used for process fault diagnosis.

候选贡献落在“训练类别计数与本轮类别训练误差共同更新系数”的规则，以及它如何训练最终诊断器，而不是“用了加权交叉熵”。最近前作的创新检索尚未完成，因此这里只确立候选表述，不确认创新性。详细系数公式和选择记录留在方法与实验设置。

结果应如实收束为：**在题设匹配比较中，weighted F1 提高，但 macro F1 降低，少数类表现有升有降，呈现不同汇总指标与类别之间的权衡。** 不能据此宣称普遍改善、少数类整体受益或物理误分类成本下降，也不能单凭该比较认定增益由更新规则造成。这些结果解释与核查边界无需全部塞入方法总览。

**实际读取文件**
全文或相关章节：
- [SKILL.md](../../SKILL.md)
- [摘要与贡献子 Skill](../../skills/engineering-abstract-contributions/SKILL.md)
- [术语库](../../references/engineering-application-terminology-bank.md)
- [术语语境裁定](../../references/terminology-decisions.md)
- [已发表证据记录](../../references/published-evidence.md)
- [Topic Playbooks](../../references/topic-playbooks.md)
- [摘要与贡献写作指导](../../references/abstract-and-contribution-craft.md)
- [实验证据指导](../../references/experiment-evidence-design.md)

另仅读取了搜索命中片段，未通读：
- [工业 AI 分类](../../references/industrial-ai-taxonomy.md)
- [术语词表](../../references/engineering-application-terms.txt)
- [图与 LaTeX 指导](../../references/figure-and-latex-production.md)
- [中文术语库](../../references/engineering-application-terminology-bank_CN.md)
- [语料校准流程](../../references/corpus-calibration-workflow.md)
- [术语与风格](../../references/terminology-and-style.md)
- [中文术语语境裁定](../../references/terminology-decisions_CN.md)
