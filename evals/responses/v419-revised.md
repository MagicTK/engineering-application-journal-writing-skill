**A**
审稿意见的三项判断均不成立：

- **没有 softmax 仍可构成知识蒸馏。** 本例通过教师隐层特征匹配和教师回归预测传递知识，属于特征与回归输出层面的教师指导，不依赖分类概率。
- **蒸馏不要求预测时融合师生特征。** 本例教师只参与训练指导，预测时不执行教师。
- **提前退出不等于在线学习。** 置信度预测器控制执行路径，参数保持固定；不能据此声称在线参数更新，也不能直接推断已实现时延收益。

英文方法摘要：
:::writing{variant="standard" id="71943"}
For quality regression, a student learns from three pretrained teachers by matching their respective penultimate-layer features through three projection heads and regressing a weighted target combining teacher predictions with training ground truth. The trained student estimates quality without executing the teachers, while an optional confidence predictor controls early exit with model parameters held fixed.
:::

**B**
不能使用原句，但应保留 **domain adaptation** 这个总称。

目标标签空间 `{0,1}` 是源标签空间 `{0,1,2,3}` 的真子集，因此不能写 `identical label spaces`。`y_t` 的来源尚不清楚，不能确定 `unsupervised`；伪标签与真实标注也不能混为一谈。域判别损失影响训练，而已知预测操作是源分支分类器输出的加权组合，不是源、目标特征融合。

下列英文只陈述已知机制，不预判监督类型：
:::writing{variant="standard" id="71944"}
The method addresses cross-condition diagnosis using three source domains, with the target label space forming a strict subset of the source label space. Domain-discrimination and classification losses jointly train the encoder, while inference combines the weighted outputs of the source-specific classifiers.
:::

**作者待澄清：** 若目标训练项仅使用由无标注目标数据生成的伪标签，可与无监督域适应相容；若使用目标真实标注，应按实际标注使用范围界定监督设定。该条件须在定稿时明确，不能只靠删除 `unsupervised` 掩盖。

**最重要的核实问题：** `L_cls` 中的 `y_t` 究竟来自真实标注还是伪标签，其获取、生成及模型选择过程是否使用了目标域真实类别标签？

**C**
**暂不将“竞优状态蒸馏门控”收录为通用工业术语。** 单篇论文可以确立其自定义专名；另外两篇仅出现 `distillation`，不能为完整复合名称提供多来源依据。可保留带来源归属的 `dynamic competitiveness balancing distillation`，将通用性与中文译名分别标为待核实。“状态”“门控”也不能在没有对应定义和运算时自行补入译名。

按所给公式，
\[
p_s=\operatorname{softmax}(z_s/\tau),\qquad
p_t=\operatorname{softmax}(z_t/\tau),\qquad
L=D_{\mathrm{KL}}(p_s\|p_t).
\]
**匹配对象是经过温度缩放及 softmax 归一化的分布，而非未经归一化的分数本身。** 若分量对应类别，可称为类别预测分布；否则应先明确分量及归一化轴的含义。KL 的方向是 \(p_s\|p_t\)，不能随意调换。

文字与公式冲突，图中重复同式并不能验证实现。应由作者核对损失实现或澄清定义，再统一文字、公式与图示；目前只能确定“所示公式如何计算”，不能宣称实际程序已核实。

后续核验分两条：
- **完整名称：** 核查至少两篇不同的相关工程应用期刊论文，确认完整名称或语义等价表达具有相同对象和操作；争议较大时优先核查三至五篇。按研究工作去重，不以共有单词、参考文献题名或同一论文的多个版本凑数。
- **中文译名：** 独立查询术语权威来源或可靠中文学术文献，核对英文对应、定义及语境，记录网址和具体段落；存在多译法时补查独立来源。基础词“知识蒸馏”的译名依据不能自动证明整个复合名称成立。

本次未联网核验；证据补齐前，保留英文专名并给出明确标为解释性的中文说明，不宣称标准中译。

**D**
不应采纳该建议。**同架构不妨碍知识蒸馏成立，蒸馏也不要求删除实际存在的教师预测路径。** 本例训练阶段匹配特征，预测阶段执行两个网络并组合类别概率，是“特征蒸馏训练＋预测层加权组合”，不能改写为特征融合。删除教师路径会改变方法；没有压缩或时延证据，也不能称为轻量化。

英文方法说明及中文贡献表述：
:::writing{variant="standard" id="71945"}
For equipment diagnosis, a student is trained to match the features of a teacher with the same architecture. At inference, both networks are executed, and their class-probability predictions are combined with weights of 0.2 for the teacher and 0.8 for the student.

本研究构建设备诊断方案，将教师特征指导的学生训练与预测阶段的师生类别概率加权组合相结合，形成最终诊断输出。
:::
