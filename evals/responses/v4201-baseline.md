# Fictional Operating-Profile Baseline

One context answered A/B on immutable v4.2.0. Science already passes; no general gain is inferred. Only wrappers, private path/link metadata and whitespace are normalized; exact raw/dispatch remain private. Runtime orientation is disclosed, not case evidence.

运行定向仅含额度、目录及通用技能规则检查，不作为案例证据。以下仅依据虚构题设和指定目录的相关参考；未浏览外网、读取论文原文、修改文件或运行研究实验。

**A：问题边界**
证据允许的核心表述是：**跨产品等级故障诊断，训练未覆盖等级B，但两等级共享相同故障类空间。**

| 维度 | 已知与允许的表述 | 仍未知或不能推出 |
|---|---|---|
| 等级／工况 | 两个已知产品等级间切换；B未被训练覆盖 | 具体运行条件和物理过程差异未给，不能补写过程机理改变 |
| 时间分布 | 已知的是A训练、B评价的跨等级设置 | 采集顺序、变化速度及具体变化的分布均未知，不能称“连续概念漂移”；B误差较高也不等于检测到了漂移 |
| 故障类空间 | 均为正常、故障1、故障2，属于相同标签空间的闭集类别设置 | 未见等级不等于未见故障类别，不能据此写“开放集故障识别” |
| 信息访问 | 训练数据只含A，当前评价对象为B | B测量或标签是否参与模型选择、校准或适应，以及访问时点、后续源数据访问条件，均未说明 |

因此，具体统计分布差异仍待确定，不能仅凭等级不同或误差较高指定漂移类型。**方法保持未选**，不补定适应方式、更新机制或论文范式。依据：[问题优先分类](../../references/problem-first-classification_CN.md)、[跨工况与漂移边界](../../references/topic-playbooks.md)。

另一个独立任务中，出现训练未覆盖的故障3，只证明**当前类别覆盖超出了训练类别覆盖**。它不等于系统已能拒识未知，更不等于已能将其辨认为“故障3”。“输出未知”和“识别具体新故障名称”也是不同能力；尚无拒识规则，不能声称已经实现前者。

英文问题段，58词：

A production line switches between two known product grades, A and B. Training data cover grade A, whereas evaluation concerns grade B. Both grades share the same normal and two fault categories. The problem is fault diagnosis for a grade absent from training, with higher errors reported on B; the temporal evolution of the data distribution remains unspecified.

**B：精确概率**
令 \(q=P(X=1)\)。由全概率公式和贝叶斯公式：

\[
P(Y=1)=\frac15(1-q)+\frac45q,\qquad
P(X=1\mid Y=1)=\frac{(4/5)q}{P(Y=1)}.
\]

| 环境 | \(P(Y=1)\) | \(P(X=1\mid Y=1)\) |
|---|---:|---:|
| 旧环境 | \(\frac15\frac12+\frac45\frac12=\frac12\) | \(\frac{(4/5)(1/2)}{1/2}=\frac45\) |
| 新环境 | \(\frac15\frac15+\frac45\frac45=\frac{17}{25}\) | \(\frac{(4/5)(4/5)}{17/25}=\frac{16}{17}\) |

四种说法**不能互换**：

- **输入分布变了：成立。** \(P(X)\)改变，而题设明确保持\(P(Y\mid X)\)不变；符合通常的协变量偏移约定。
- **类别比例变了：成立。** \(P(Y=1)\)从\(\frac12\)变为\(\frac{17}{25}\)。输入分布变化可以同时伴随类别比例变化，两者并非同义词。
- **仅标签偏移：不成立。** 按“\(P(Y)\)改变、\(P(X\mid Y)\)保持”的约定，本例的\(\frac45\ne\frac{16}{17}\)已经否定后一个条件。
- **输入到目标关系变了：不成立。** 这一方向指\(P(Y\mid X)\)，题设中两环境完全相同。反方向\(P(X\mid Y)\)发生变化，不能据此说前方向也改变。

**P30的来源约定：** 本地记录将其条件漂移写为：**保持类别先验\(P(Y)\)固定，改变类条件分布\(P(X\mid Y)\)**。这不是所有文献对概念漂移的统一定义，也不能与\(P(Y\mid X)\)变化互换。本玩具的\(P(Y)\)也改变，因此不满足P30记录中的固定先验条件。此处**仅依据本地来源记录，未阅读或独立核验P30原文**。依据：[具体分布约定](../../references/topic-playbooks.md)、[P30来源索引](../../references/published-evidence.md)。

新工况、分布漂移、未知故障分别涉及运行条件、概率分布和类别覆盖；它们可以共存，但不彼此蕴含，也不唯一对应某个机制名。

英文定义提示，32词：

According to the local P30 record, conditional drift changes P(X|Y) while holding P(Y) fixed. This source-specific convention is not universal; other concept drift definitions may concern P(Y|X), so retain the conditioning direction.
