# Fictional Class-Evidence Prose-Retest Response

One fresh context handled the same four requests after a two-reference prose clarification. The actual initial response and its review remain available; no general writing-performance gain is claimed.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. These synthetic checks are not scientific experiments.

访问披露：本会话有系统预置的历史项目与偏好摘要，并非历史空白环境；本轮未检索或援引记忆、历史记录。实际访问包括指定技能、摘要与贡献子技能、四份相关参考正文及章节写作指南的关键词检索，以及必要的两份引导文件和只读额度服务。计算与字数核验在内存完成；未访问评测材料、私有记录、真实论文或其他项目，未修改文件、安装、开展科研实验、发布或调用其他代理。以下四题在同一任务上下文完成，均仅按题给虚构事实解释。

**M4139-A**

| 样本 | e | b | p | u | 决策 |
|---|---|---|---|---|---|
| A，S=10 | [7,1] | [0.7,0.1] | [0.8,0.2] | 0.2 | 拒绝 |
| B，S=100 | [79,19] | [0.79,0.19] | [0.8,0.2] | 0.02 | 保留第一类 |

`b` 与 `p` 不能互换：\(p_k=b_k+u/2\)，且 \(\sum b_k=1-u\)，而 \(\sum p_k=1\)。本定义下两者的最大分量位置相同，不代表数值或含义相同。`u` 不能直接解释为该样本的错误概率。

草稿中，若“类别置信度”特指最大期望类别概率，则两者同为0.8成立；B的`u`为A的十分之一也成立。但这不推出诊断可靠性提高十倍，更不保证未知故障检出。

英文方法句组，50词：
> The network's nonnegative evidence e defines alpha = e + [1,1]. Expected probabilities p = alpha/S determine the candidate class by argmax, with S = sum(alpha). Reject the sample when the uncertainty mass u = 2/S exceeds 0.1; otherwise retain that class. The threshold was fixed on independent calibration data.

**M4139-B**

原始状态为 \(\alpha=[8,2]\)、\(p=[0.8,0.2]\)、\(u=0.2\)。

| 操作 | 新 α | 新 p | 新 u |
|---|---|---|---|
| 先将e乘10，再加单位先验 | [71,11] | [71/82,11/82] ≈ [0.865854,0.134146] | 1/41 ≈ 0.024390 |
| 直接将原α乘10 | [80,20] | [0.8,0.2] | 0.02 |

就`p`和`u`而言，“只有不确定性改变、类别概率保持不变”对第二种操作成立，对第一种不成立。固定单位先验时，第二种操作对应的新证据是[79,19]，不是[70,10]。这些是输出量的代数变换，不是在线再训练或序贯贝叶斯观测更新。

英文解释，31词：
> Multiplying evidence before adding the unit prior changes both expected class probabilities and uncertainty. Multiplying alpha directly preserves expected class probabilities and reduces u to one tenth of its original value.

**M4139-C**

| 模型 | 错误率 | 0.8置信度分箱的经验准确率 | 绝对置信度差值 | u |
|---|---|---|---|---|
| A | 4/20 = 20% | 16/20 = 80% | \|0.8−0.8\| = 0 | 0.2 |
| B | 12/20 = 60% | 8/20 = 40% | \|0.8−0.4\| = 0.4，即40个百分点 | 0.02 |

英文结果段，47词：
> On the same 20 samples, both models assigned top-class expected probability 0.8. Model A achieved 80% accuracy in this bin, exactly matching confidence, with 20% error. Model B achieved 40% accuracy, with 60% error and a 40-percentage-point confidence gap, despite its smaller uncertainty mass (0.02 versus 0.2).

作者注：A在这个有限样本分箱中的经验匹配成立，不能扩展为所有人群的校准保证。独立校准集上固定拒绝阈值，是拒绝规则的设定事实；概率校准关注预测概率与实际频率是否匹配，两者不是同一个事实。

**M4139-D**

英文摘要，180词：
> Fault diagnosis of rotating equipment under changing noise requires identifying known faults while rejecting fault categories absent from training. We develop a signal-quality-guided fusion approach that links synchronized vibration and current measurements to evidence-based classification and rejection. The two signals are encoded separately, and quality indicators available at prediction time control the relative weights of their features during fusion. The resulting vector is passed to a nonnegative evidence head, whose outputs define a Dirichlet distribution over known classes. Its expected class probabilities determine the candidate diagnosis, while an uncertainty mass determines whether that candidate is retained or replaced by an unknown label. Known-class labels from the training set supervise learning of this diagnostic mapping. The rejection threshold is fixed beforehand using an independent calibration set. Comparisons under fixed test settings on a benchmark and data from actual production equipment show higher classification accuracy over all known samples before rejection and higher unknown-fault rejection rates than the comparison method. These gains are accompanied by higher false-rejection rates for known samples, exposing a trade-off between rejecting unknown faults and retaining known cases.

整体设计贡献候选，49词：
> For rotating-equipment diagnosis, quality indicators available at prediction time control the fusion of separately encoded vibration and current features. The fused representation feeds a single evidential head whose expected class probabilities determine known-class predictions and whose uncertainty mass supports unknown rejection through a threshold fixed on independent calibration data.

作者说明：以\(K\)个已知类记，单位先验形式为 \(\alpha_k=e_k+1\)、\(S=\sum_k\alpha_k\)、\(p_k=\alpha_k/S\)、\(u=K/S\)。融合向量进入证据头；`p`产生候选类别，`u`接入已固定的拒绝规则，拒绝仅输出未知标记。随输入计算融合权重不等于更新模型参数。

分类准确率保留全部已知样本、拒绝前的统计口径，拒绝指标分开报告。结尾保留两组测试共同支持的准确率和未知拒绝收益，以及已知误拒增加的代价；不添加统计显著性或现场接入主张。贡献仍是整体设计候选，新颖性待作者对照最近前作核实，不能仅凭采用已有证据方法认定；普通测试不另列为第二贡献。

字数按空白分词，连字符复合词计一词。
