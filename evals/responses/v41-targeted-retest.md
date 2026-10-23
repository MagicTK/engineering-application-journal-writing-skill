# Same-Context Targeted Retest

These five responses use the original briefs and the current English and Chinese abstract-and-contribution-craft references. This is a same-context retest, not a new independent test. The original responses.md is retained unchanged; no new study facts or external evidence have been introduced.

## v41-training-prediction

Replace only the two supplied method sentences:

> The shared encoder learns through quality prediction on labeled measurements and reconstruction of unlabeled measurements. At inference, the quality predictor estimates concentration from the encoder's features.

The first sentence explains how the prediction and reconstruction objectives train the shared representation; the second follows that representation into concentration prediction. In the supplied design, E feeds P and D during training, but only E and P run at inference. D does not first repair or impute the measurements, and its outputs do not enter a fusion head. These are local corrections to the training and prediction relationships, not a deployment claim. Leave all other abstract sentences unchanged.

## v41-contribution-finding

Yes. Two items distinguish the actual advances more clearly than an encoder item, an aggregation item, and an experiment inventory:

1. **Method contribution:** the new delay-aware aggregation rule, including the operation that differs from prior approaches and the requirement it addresses. The unchanged encoder supplies its inputs and belongs in the supporting method description, not a separate novelty claim.
2. **Empirical engineering contribution:** the documented trade-off between assay delay and the value of acquiring an additional measurement, under the evaluated conditions. The contribution is the resulting engineering finding, not the fact that two experiments were conducted.

Before drafting precise claims, inspect the aggregation specification and closest-method comparison, the controlled study's settings and information timing, the definition of measurement “value,” and the traceable results and uncertainty that establish the trade-off. Check any proposed direction, threshold, or operating recommendation against those records. If “value” means prediction improvement, do not silently turn it into an economic saving. The brief establishes that a controlled finding exists but supplies no values; preserve that distinction rather than inventing numbers or a universal acquisition policy. The experiments can support the two items without becoming additional contribution items.

## v41-minimal-abstract-edit

仅替换所给原句：

> For cross-stage fusion, the grouped variable features within each stage are pooled into a single stage vector; these vectors form topology-biased context that variable-level gates feed back to the variable features.

这句话保留了理解该操作所必需的尺度变化和输出去向：分组后的变量特征先池化为每工序一个向量，工序向量用于形成拓扑偏置引导的上下文，再通过变量级门控写回变量特征。前文已经说明软分组，无须重述其算法；`within each stage` 在这里标明池化范围，可以保留。拓扑偏置也没有被改写成硬约束或与特征直接拼接。

不修改开头、方法或其他摘要句，不为凑字数扩写。这里只能定位到提供的原句；没有全文和 PDF，不能给出已核实的页码或声称正文、公式与图已同步。

## v41-multitask-mixture

Replace only the two method sentences:

> Each quality target uses a softmax gate to combine the feature outputs of all shared experts for its prediction head. During training only, the task losses are reweighted using their gradient norms on the shared parameters.

The first sentence describes a task-specific, dense mixture of expert features: every expert runs for every input. The second explains how those tasks train the shared parameters; it is not a later feature-processing module at inference. Neither operation establishes one-expert selection by process mode, device or expert load balancing, or faster prediction. Those claims should be removed, while the rest of the abstract stays unchanged.

## v41-holdout-delayed-soft-sensor

可讨论的四句英文替换稿如下，第一句原样保留：

> A shared encoder extracts features from the available process measurements. Prediction and reconstruction objectives shape this shared representation using labeled and unlabeled training samples, respectively. At inference, observation-mask gating weights the encoded features from the preceding four-minute measurement window for the prediction head to estimate the current concentration. Evaluation uses historical, batch-disjoint holdout data from a single plant.

**简短理由**

- 第二句承接共享表征，说明两个训练目标如何利用有标签和无标签样本；第三句交代门控作用于编码特征，并将其接到浓度预测。重构头仅参与训练，实际预测只运行编码器、门控和预测头，不是先补全测量再预测。
- `preceding four-minute measurement window` 指截至预测时刻的四分钟测量窗口，目标是该时刻即窗口末端的浓度。传感器每 2 秒采样、化验每 12 分钟取样及 18 分钟后返回，应在数据与问题定义中分别说明。标签应对应化验取样时刻，其返回时刻决定何时可用；门控依据观测掩码，不读取尚未返回的当期化验值。
- 最后一句只写已有评价范围。相同标签数量下的无标签数据利用对照，以及相同缺测构造下的门控对照，可在实验说明中分别展开，不必塞入概述末句。未给分数，不能把做过对照写成已经改善性能；单厂批次隔离留出也不证明跨厂泛化、实时时限或现场部署。

**贡献组织**

可先用一项完整的**方法候选贡献**组织：共享预测与重构学习利用有标签和无标签测量，观测掩码门控再调节用于浓度预测的编码特征。它回应的是所给监督条件和缺测输入，但“存在化验延迟”本身不等于提出了新的延迟建模机制。两个设计可在同一项内说明各自职责，不必按编码器、重构头、门控的数量拆成三项创新。

两项已有对照分别服务于无标签数据利用和门控作用的验证，不单列“开展了两项实验”为贡献。若最近前作与具体运算的比对表明两个设计各有独立的实质推进，再考虑拆成两项；目前不预设贡献数量，也不因措辞更顺就认定创新。

仍缺少最近前作及明确技术差异、具体目标与门控运算的说明，以及可追溯的对照结果和影响结论的不确定性。已给出的相同标签预算、相同缺测构造是有价值的控制条件，但没有结果就不能断言两种机制均有效；即使有效，也不能仅据此认定其新颖性。公式和图未提供，技术对应关系尚不能进一步核实。本次只给讨论稿，不修改源稿。

**Reference-Change Scope**

The updated guidance changes how detailed mechanism checks are distilled into replacement prose; it does not change the supplied studies or their evidence boundaries. Among the 16 initial cases not retested here, v41-generation-boundaries is the other case directly using this abstract/contribution guidance. The same distinction between essential framing and secondary detail would apply to any later abstract rewrite, but its original request asks only for framing comments. Its generation task, diffusion-step meaning, utility evaluation, and privacy boundary therefore need no substantive revision from this change alone.

I do not identify a required response change in the other 15 initial cases on this basis: they concern terminology, routing, evidence, rigor, or artifact handling rather than replacement abstract prose. This is a bounded scope judgment from the original briefs and the earlier same-context work, not a new independent review of those cases. They have not been re-answered or added to the retest.
