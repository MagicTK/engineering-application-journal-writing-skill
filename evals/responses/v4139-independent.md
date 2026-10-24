# Fictional Class-Evidence Final Response

One fresh context handled the same four requests after the prose clarification and source-table/validator repair. Initial and prose-retest answers remain available; no general writing-performance gain is claimed.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. These synthetic checks are not scientific experiments.

访问说明：四题由同一个任务上下文处理，并非四次独立运行。上下文已预置历史摘要与规则；本次未检索记忆、历史、评测、旧答复、私人记录、真实论文或其他项目。实际读取了指定技能、摘要/贡献子技能及相关当前写作与术语参考，另完成必需启动文档读取、两次只读额度服务调用和内存计算。未编辑文件、安装、浏览文献、开展实验、发布或调用其他代理。以下只解释题设虚构定义，不认证真实产线或实验。

**M4139-A**

| 样本 | \(S\) | \(e\) | \(b\) | \(p\) | \(u\) | 拒绝结果 |
|---|---:|---|---|---|---:|---|
| A | 10 | [7,1] | [0.7,0.1] | [0.8,0.2] | 0.2 | 拒绝，候选为第1类 |
| B | 100 | [79,19] | [0.79,0.19] | [0.8,0.2] | 0.02 | 不拒绝，输出第1类 |

\(b\)与\(p\)不能互换：\(\sum b=1-u\)，而\(\sum p=1\)，且\(p_k=b_k+u/2\)。单位先验下二者的最大分量位置相同，不代表数值或含义相同。\(u\)不能直接解释为该样本的错误概率。

草稿中，若“类别置信度”明确指\(\max p\)，两者均为0.8，这一点成立；B的\(u\)为A的十分之一也成立。但这不能推出诊断可靠性提高十倍，更不能保证未知故障检测。

英文方法句组，45词：
> The network produces nonnegative class evidence. Adding a unit prior yields Dirichlet parameters whose normalized values provide expected class probabilities. Their argmax gives the candidate class; uncertainty mass, defined as two divided by total concentration, triggers rejection only above 0.1, fixed using independent calibration data.

**M4139-B**

原始量为\(\alpha=[8,2]\)、\(p=[0.8,0.2]\)、\(u=0.2\)。

| 操作 | 新\(\alpha\) | 新\(p\) | 新\(u\) |
|---|---|---|---|
| 先将\(e\)乘10，再加先验 | [71,11] | \([71/82,11/82]\approx[0.865854,0.134146]\) | \(2/82\approx0.024390\) |
| 直接将原\(\alpha\)乘10 | [80,20] | [0.8,0.2] | 0.02 |

两种操作不相同。就\(p\)与\(u\)而言，“只有不确定性变化、类别概率保持不变”在第一种操作中不成立，在第二种中成立；这不意味着第二种的\(\alpha\)或隐含证据未变。这些代数变化不代表在线再训练或序贯观测更新。

英文解释，33词：
> Scaling evidence before adding the prior changes the class probabilities here. Scaling all original Dirichlet parameters instead preserves their normalized probabilities and reduces the uncertainty mass tenfold; the two operations are therefore distinct.

**M4139-C**

| 模型 | 错误率 | 0.8置信度分箱的经验准确率 | 绝对置信度差值 | \(u\) |
|---|---|---|---|---|
| A | \(4/20=20\%\) | \(16/20=80\%\) | \(|0.8-0.8|=0\) | 0.2 |
| B | \(12/20=60\%\) | \(8/20=40\%\) | \(|0.8-0.4|=0.4\)，即40个百分点 | 0.02 |

英文结果段，45词：
> For the same 20 samples, both models assigned top-class probability 0.8. Model A achieved 80% accuracy and 20% error, matching confidence in this bin with zero absolute gap. Model B achieved 40% accuracy and 60% error, yielding a 40-percentage-point gap despite its smaller uncertainty mass.

作者注：A在这20个样本构成的分箱内经验匹配成立，不等于所有人群均已校准。独立校准集上固定拒绝阈值，与验证类别概率校准不是同一个事实；前者确定拒绝规则，不能自动证明概率与正确频率匹配。

**M4139-D**

英文摘要，174词：
> Rotating equipment operating under changing noise conditions requires diagnosis that distinguishes known faults while rejecting fault categories absent from training. This study develops a diagnostic approach in which signal quality governs how synchronized vibration and current measurements contribute to classification and rejection. Separate encoders convert the measurements into vibration and current features. Signal quality indicators available at prediction time determine their relative fusion weights, producing a combined representation that feeds a nonnegative evidence head. Adding a unit prior to the evidence yields Dirichlet parameters. Their normalized values provide expected class probabilities for selecting a candidate known class, while an uncertainty mass governs rejection through a threshold fixed beforehand on an independent calibration set. The resulting decision assigns either the selected known class or an unknown label. Training uses only known-class labels from the training set. Fixed-setting evaluations on a benchmark and data from actual production equipment show higher known-class classification accuracy before rejection and higher unknown rejection rates than the comparison method, at the cost of a higher false rejection rate for known samples.

整体设计贡献候选，50词：
> We propose a diagnostic design that uses signal quality available at prediction time to weight vibration and current features during fusion. The fused representation supplies an evidential head whose expected probabilities select known classes and whose uncertainty mass governs rejection, linking quality-dependent feature combination to diagnosis under changing noise conditions.

作者说明：
- 接口为同步信号分别编码→质量指标控制特征融合权重→融合向量进入证据头→类别概率与不确定性分别用于类别选择和拒绝。预测时权重随输入变化，不表示模型参数逐样本更新。
- 公式应统一为\(\alpha_k=e_k+1\)、\(S=\sum_k\alpha_k\)、\(p_k=\alpha_k/S\)；该单位先验形式的不确定性为\(u=K/S\)，其中\(K\)为已知类别数。D未指定类别数及阈值数值，不套用A的二分类阈值。
- 收益对应拒绝前的全部已知样本分类准确率和独立统计的未知拒绝率；已知误拒率同时增加。生产设备数据不代表现场接入，结果不写成统计显著性结论。
- 新颖性仍待作者与最近前作核实；已有证据头本身不自动构成创新，两组常规测试不另列为第二贡献。词数按空格计，连字符词计一词，仅适用于本题。
