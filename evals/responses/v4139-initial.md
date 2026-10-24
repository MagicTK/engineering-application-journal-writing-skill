# Fictional Class-Evidence Response

One fresh context handled four requests; scientific checks passed, but the maintainer identified a redundant defensive ending in C. This is diagnostic, not the repaired final-source release test.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. Synthetic checks are not scientific experiments.

本轮在同一任务上下文中处理 A–D，并非四次独立运行。全部计算与写作仅针对题设虚构事实，不认证真实生产或实验。英文按空格计词，连字符词计一词。

**M4139-A**

| 量 | 样本 A | 样本 B |
|---|---|---|
| \(S\) | 10 | 100 |
| \(e=\alpha-[1,1]\) | [7,1] | [79,19] |
| \(b=e/S\) | [0.7,0.1] | [0.79,0.19] |
| \(p=\alpha/S\) | [0.8,0.2] | [0.8,0.2] |
| \(u=2/S\) | 0.2 | 0.02 |
| 候选类别与拒绝结果 | 第一类；拒绝 | 第一类；保留 |

\(b\) 与 \(p\) 不能互换：\(p_k=b_k+u/2\)，且 \(\sum b_k=1-u\)，而 \(\sum p_k=1\)。本设定下它们的最大值位置相同，不代表数值含义相同。\(u\) 也不能直接解释为该样本的错误概率。

原句中，若“类别置信度”明确指最大期望类别概率，则两者同为 0.8；B 的不确定性质量确为 A 的十分之一。但这不能推出诊断可靠性提高十倍，也不能保证未知故障检测。

英文方法句组，48 词：

> The network maps inputs to nonnegative evidence and adds a unit prior to obtain Dirichlet parameters. Expected class probabilities determine the candidate label by argmax. Uncertainty mass controls rejection: the candidate is retained when u≤0.1 and reported as unknown otherwise, using a threshold fixed on independent calibration data.

**M4139-B**

原始输出为 \(\alpha=[8,2]\)、\(p=[0.8,0.2]\)、\(u=0.2\)。

| 操作 | 新 \(\alpha\) | 新 \(p\) | 新 \(u\) |
|---|---|---|---|
| 先将 \(e\) 乘 10，再加单位先验 | [71,11] | [71/82,11/82] ≈ [0.865854,0.134146] | 1/41 ≈ 0.024390 |
| 直接将原 \(\alpha\) 乘 10 | [80,20] | [0.8,0.2] | 0.02 |

因此，在比较 \(p\) 与 \(u\) 的意义上，原句对第一种操作不成立，对第二种成立。两种操作不等价：直接缩放后的隐含证据为 [79,19]，不是 [70,10]；也不能把概率不变理解为所有其他量均不变。

英文解释，31 词：

> Multiplying evidence before adding the unit prior changes the class probabilities here. Multiplying alpha directly preserves all expected class probabilities and reduces uncertainty mass tenfold; the two operations are not equivalent.

作者说明：这里讨论输入条件化输出量的变换，不表示在线再训练或序贯贝叶斯观测更新。

**M4139-C**

| 指标 | 模型 A | 模型 B |
|---|---|---|
| 错误率 | 4/20 = 20% | 12/20 = 60% |
| 0.8 置信度单分箱的经验准确率 | 16/20 = 80% | 8/20 = 40% |
| 绝对置信度差值 | \(|0.8-0.8|=0\) | \(|0.8-0.4|=0.4\)，即 40 个百分点 |
| \(u\) | 0.2 | 0.02 |

英文结果段，43 词：

> In the 0.8-confidence bin, Model A has 80% accuracy, 20% error, and zero absolute confidence-accuracy gap. Model B has 40% accuracy, 60% error, and a 40-percentage-point gap despite smaller uncertainty mass. A's empirical match in this bin does not establish calibration across populations.

作者说明：在独立校准集上固定拒绝阈值，是拒绝规则的阈值选择事实；概率校准涉及预测概率与经验正确频率的匹配。两者不是同一个事实，前者不自动证明后者。这里 A 的经验匹配成立，但仅限这 20 个样本构成的分箱。

**M4139-D**

英文摘要，169 词：

> Rotating equipment diagnosis under changing noise requires recognition of known faults and rejection of fault categories absent from training. We present a diagnostic design that links signal-quality-controlled vibration-current fusion to evidential decision-making. Synchronized vibration and current measurements are encoded separately, and signal quality indicators available at prediction time control the weights assigned to the two feature representations during fusion. The resulting fused vector is passed to a nonnegative evidence head, whose outputs define a Dirichlet distribution over known classes. Expected class probabilities determine the candidate known-fault label, while an uncertainty measure triggers rejection above a threshold fixed beforehand on an independent calibration set. Accepted samples receive the candidate label; rejected samples are reported as unknown. Training uses only known-class labels from the training set. Fixed-setting tests on a benchmark and data from actual production equipment show higher known-class classification accuracy before rejection and higher unknown-fault rejection rates than the comparison method, accompanied by higher false rejection of known samples. These results indicate a classification-rejection trade-off within the evaluated settings.

整体设计贡献候选，37 词：

> We propose an integrated diagnostic design in which prediction-time signal quality controls vibration-current feature fusion, and the fused representation feeds an evidential head whose expected probabilities and uncertainty measure support known-fault classification and threshold-based unknown rejection, respectively.

作者说明：
- 内部对应关系为：融合向量进入证据头；\(\alpha_k=e_k+1\)，\(p_k=\alpha_k/S\)，\(u=K/S\)。其中 \(K\) 为已知类别数；候选类别取 \(\arg\max p\)，仅当 \(u>\tau\) 时拒绝，\(\tau\) 已预先固定。逐样本变化的权重与输出不等于模型参数更新。
- 分类准确率以全部已知样本、拒绝前的预测计算；未知拒绝率和已知误拒率另行统计。摘要保留两组共有的收益与误拒代价，不声称统计显著或现场接入。
- 整体设计仍是贡献候选，新颖性须由作者对照最近前作核实；使用已有证据头本身不能确立创新，普通测试也未另列为第二贡献。

访问披露：上下文预置了历史摘要、偏好及环境指令，因此并非“记忆空白”。本轮未检索或采用历史作为题设证据；实际只读了指定主技能、摘要贡献子技能、术语决策及摘要贡献写法参考，在章节写作和论证写法参考中定向检索，并读取两份必要启动文档、调用只读额度服务。除获准额度核查外，未访问私人记录、真实论文原文、其他项目、记忆、历史或评测记录；未编辑文件、安装、浏览文献、开展科学实验、发布或调用其他代理。
