# Fictional Class-Semantic Baseline

One context handled three requests on unchanged v4.1.44 instructions. Core judgments already passed; no demonstrated scientific failure or controlled writing gain. Wrapper and whitespace only are normalized.

说明：上下文含预置历史摘要，未检索既往答案。三题共用同一上下文，并非三次独立模型运行；不声称提供完整内部轨迹。以下词数按空格分词，连字符词计一词。

**A**
仍可称为生成式 zero-shot diagnosis：未见类没有真实训练测量，分类器使用合成特征的条件类别 ID 不会改变这一事实。已见类历史标签和专家语义均已使用，因此不是“完全无标签学习”。400 个向量是合成训练对象，不能计作新增 400 次真实采集或人工逐样本标注；专家语义投入应另行核算。

方法说明，42 词：

> Trained on labeled measurement features and expert descriptions of four seen faults, the generator uses two unseen classes' expert descriptions to synthesize 200 vectors each. Conditioning IDs label synthetic examples for six-class classifier training, without new real measurements or manual sample annotations.

**B**
这是利用类别语义识别具体未见故障的 zero-shot diagnosis，不是仅拒识 unknown。

- 未见类专测且候选集合也仅含未见类时，属于 conventional ZSL；联合测试并允许预测已见/未见并集时，属于 generalized ZSL。未见类专测不必强制报告已见/未见调和指标。
- 联合测试中，若 \(S=0.9\)、\(U=0.3\)，则 \(H=2SU/(S+U)=0.45\)。0.6 是算术平均值，不能称为 harmonic mean。
- 使用完整无标签目标批次进行调整属于 transductive 信息访问，不能称为纯 inductive。预先提供未见类语义、声明清楚的无标签目标适应都可以成立；应交代调整对象及访问范围，并保持比较条件一致。

预测路径，36 词：

> The encoder maps process measurements into a semantic vector, which is compared with predefined candidate fault-description vectors. The selected description determines the predicted fault name, including unseen faults when their descriptions belong to the candidate set.

**C**
摘要，173 词：

> Safely collecting labeled measurements of rare industrial faults is difficult, motivating diagnosis of classes absent from real training measurements. Four seen fault classes provide labeled measurements, whereas two unseen classes provide none; experts supply descriptions for all six classes. Expert descriptions condition a generator trained on seen-class measurement features. A semantic reconstruction loss guides the generator by requiring a reconstructor to recover conditioning descriptions from generated features. After learning, unseen-class descriptions condition feature generation. These synthetic features and their conditioning class IDs, together with real seen-class features and labels, train a six-class classifier. At prediction, only an encoder and the classifier map real test measurements to specific fault categories. Hyperparameters are fixed using permitted training and development data, with no target measurements used for adaptation. Comparisons with existing zero-shot methods on a simulated benchmark and production measurements under independent class splits show higher unseen-class mean accuracy and a higher harmonic mean of seen- and unseen-class mean accuracies, but lower seen-class mean accuracy. The observed trade-off improves unseen-fault recognition while reducing accuracy on seen faults.

贡献候选，41 词：

> Expert descriptions condition feature generation, while a reconstructor is trained to recover those descriptions from generated features, guiding generator training. Synthetic unseen-class features with conditioning IDs and real labeled seen-class features train a six-class classifier for fault identification from encoded measurements.

作者注：重构目标是条件描述，约束指导生成器训练，不是预测时的文本与测量融合。贡献候选陈述实际设计，不将 zero-shot 设置或普通验证本身列为创新；新颖性仍须另核。整体比较结果也不能单独证明重构约束的增益。
