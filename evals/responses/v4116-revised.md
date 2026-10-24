**A**

数值变化完全由缩放解释：\(D(0.1z)=0.1^2D(z)=0.02\)。指标降至原值的 **1%**，不代表时间尺度变慢100倍，更不能推出预测更好。

> Multiplying the encoder output by 0.1 reduces the unnormalized mean squared first difference from 2 to 0.02, reflecting amplitude scaling rather than evidence of slower learned dynamics or improved quality prediction.

最低核查：统一时间间隔、差分轴及统计口径；检查非零方差、尺度归一化及特征塌缩，若声称经典 SFA，还需核查零均值、单位方差与去相关约束。本例中，非退化特征的方差归一化慢度应保持不变。质量相关性和预测优势须另有独立下游评估，不能由慢度指标代替。

**B**

方法／摘要两句：

> Two parallel encoders process the same measurement sequence, one using adjacent-feature difference and input-reconstruction penalties during training and the other using differences between successive hidden states. Their outputs are concatenated for a quality-regression head, with labeled prediction error and a latent covariance-to-identity penalty guiding training; prediction uses fixed neural weights and omits the decoder.

贡献项：

> We formulate a parallel soft sensor that integrates representations from two distinct temporal encoding paths through a common quality-regression head, combining branch-specific representation learning with prediction and latent-covariance regularization during training.

中文说明：重构不保证零均值或独立性；中心化协方差趋近单位阵仅鼓励单位方差与不相关，软惩罚不保证严格满足，更不等于统计独立。需核对协方差定义、作用对象及损失权重。时间差分惩罚不自动证明去除了快速噪声，两个分支的互补性及质量预测收益也待验证。固定权重推理不是在线学习；省去解码器不等于双编码器或训练“零额外成本”。以上贡献项陈述设计，尚无依据认定其相对既有方法的新颖性。

**C**

贡献改写：

> We combine a projection \(W_g\), fitted once on historical training measurements, with a label-free projection \(W_l\) estimated separately from each completed trailing window of 48 measurements. The projected features \(W_gX\) and \(W_lX\), together with their first temporal differences, are concatenated for a fixed CNN that issues a classification only at the window endpoint.

最低报告核查：
- 明确 global/local 指历史数据与当前时间窗口，不是厂级／工序级；没有阶段划分依据。
- 给出 \(X\) 的维度、两个投影的估计目标和预处理范围，以及差分轴、边界对齐和跨窗投影基底的一致性处理。
- 明确窗口为 \(t-47,\ldots,t\)，仅在 \(t\) 决策；报告步长、冷启动和每窗重估开销。核查训练／测试窗口重叠及信息泄漏，不使用端点之后的观测或测试标签。

这里确有**预测时的无标签投影重估**，但 CNN 参数固定，不能写成持续神经网络重训；也不应抹去实际存在的窗口级估计步骤。

**D**

建议保留“趋势平滑与残差特征提取”，或进一步明确为“尾随移动平均趋势估计与残差编码”。这比建议替换的名称更准确：移动平均不是带约束的慢特征学习；残差只是相对平滑估计的偏差，可能包含有用瞬态和噪声，不能预先称为噪声，更没有“消除”证据。“平滑”在这里描述信号处理操作，并不暗示使用未来数据。

> A causal trailing moving average provides a smoothed trend estimate from the process measurements, and the residual is defined as the measurement minus this estimate. Both signals are encoded, and their features are combined for classification.

**E**

**可以，但仅限定义匹配的基础名称。** 当前 Skill 的[准入记录](../../references/engineering-application-terminology-bank.md)提供以下两个不同出版作品的定义位置，页码均为记录中的 **PDF 页序**：

- **P54**：[Abnormal Operating Condition Identification of Industrial Processes Based on Deep Learning With Global-Local Slow Feature Analysis](https://doi.org/10.1109/TIM.2023.3267347)，PDF 第3页，式(5)–(8)。
- **P55**：[Slow Down to Go Better: A Survey on Slow Feature Analysis](https://doi.org/10.1109/TNNLS.2022.3201621)，PDF 第3页，式(1)–(4)。

两处对应经典定义：在零均值、单位方差和去相关约束下，最小化平均平方时间导数。它们共享基础方法谱系，并非两次独立发明；也不自动证明所有深度、监督或概率变体具有相同优化定义。

**中文核验来源**：[《自动化学报》c201035](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201035?viewType=HTML)及[c230154](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230154?viewType=HTML)。Skill [中文记录](../../references/engineering-application-terminology-bank.md)注明，其双语摘要及关键词将 *slow feature analysis / SFA* 与“慢特征分析”对应。本轮依据已有可追溯记录，未联网重核；这些记录支持译名，不替其变体的公式或实验背书。

- **Global-Local Slow Feature CNN**：保留为该论文的专名，并明确归因；单篇定义不足以将完整名称升格为公认方法族。
- **Drift-Guided Residual Unit**：保留为当前作者提出、已有操作定义的新组件名称，注明属于本文提案。无需两篇同名先例才能命名；实际新颖性与效果仍需各自证据。库中未收录不是禁用理由。
