**A**
审稿意见的三项判断均不成立：

- **可以称为知识蒸馏。** 三个投影头匹配教师的倒数第二层特征，属于特征层面的知识迁移；教师预测参与学生的回归目标，属于回归输出层面的蒸馏。蒸馏不要求必须存在 softmax 或分类概率。
- **蒸馏不必在预测时融合师生特征。** 本例教师提供训练指导，部署时不执行教师，不能将训练匹配写成预测时的师生特征融合。
- **动态退出不等于在线学习。** 置信度预测器决定是否提前退出，改变的是执行路径；参数不更新，因此不能据此声称在线学习。

英文方法摘要，两句：
:::writing{variant="standard" id="84621"}
For quality regression, a student learns from three pretrained teachers through three projection heads that match their respective penultimate-layer features and a regression objective targeting a weighted combination of teacher predictions and training ground truth. The trained student performs prediction without executing the teachers, while an optional confidence predictor controls early exit with all model parameters fixed.
:::

**B**
不能使用所给表述，但可以保留 **domain adaptation** 这个总称。

- 目标标签空间 `{0,1}` 是源标签空间 `{0,1,2,3}` 的真子集，不是 identical label spaces；可明确描述为多源、目标标签空间为源标签空间子集的域适应设定。
- `CE(target,y_t)` 本身不能确定是否无监督。若 `y_t` 是不依赖目标真实标注生成的伪标签，可以与无监督域适应相容；若训练使用目标真实标注，则须按实际标注覆盖情况界定为有监督或半监督设定。
- 域判别损失参与训练，不代表存在预测时的源、目标特征融合。已知预测操作是**源分支分类器输出的加权组合**。

保留未知条件的英文改法：
:::writing{variant="standard" id="84622"}
The method performs multi-source domain adaptation with a target label space that is a strict subset of the source label space. Domain-discrimination and classification losses jointly train the encoder, while inference combines the weighted outputs of source-specific classifiers. The supervision setting remains unresolved because the target labels used in the classification loss have not been identified as ground-truth annotations or pseudo-labels.
:::

**最重要的核实问题：** `y_t` 究竟如何获得，目标域真实类别标注是否在训练、伪标签生成或模型选择中的任何环节被使用？

**C**
**暂不将“竞优状态蒸馏门控”作为通用工业术语收录。** 一篇论文可以确立其自定义名称，但另外两篇仅出现 `distillation`，不能支持整个复合名称。讨论该论文时可保留带出处的 `dynamic competitiveness balancing distillation`；中文名称及通用性分别标为待核实。“状态”和“门控”也需要对应的对象定义与实际运算，不能从名称或蒸馏损失自行补出。

令
\[
p_s=\operatorname{softmax}(z_s/\tau),\qquad
p_t=\operatorname{softmax}(z_t/\tau).
\]
所给损失是 \(D_{\mathrm{KL}}(p_s\|p_t)\)，比较的是**经温度缩放和 softmax 归一化后的分布**，不是直接匹配未经归一化的分数 \(z_s,z_t\)。若这些分数对应类别，匹配的是软化的类别分布；若对应其他对象，则须明确归一化的轴及其含义，不能自动称为类别概率。KL 的方向是学生分布到教师分布，不能随意颠倒。

文字与公式存在冲突；图中重复同式只能说明图与公式一致，不能证明实现正确。应核对实际损失实现或取得作者澄清，再统一文字、公式和图示。

后续核验应分开进行：
- **完整英文名称：** 检查至少两篇不同的相关工程应用期刊论文，在正文定义或公式中确认完整名称或语义等价名称对应相同对象与操作；有歧义时优先补足三至五篇，不能按共有单词或同一论文的不同版本凑数。
- **中文译名：** 独立查询术语权威来源或可靠中文学术文献，确认英文对应、定义和使用语境，记录网址及具体段落；存在竞争译法时再找独立来源。证据不足时保留英文名称并给出操作性说明，不宣称已有标准中译。

本次没有联网核验，以上是处理建议与待执行的核验步骤。
