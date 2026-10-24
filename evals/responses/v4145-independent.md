# Fictional Class-Semantic Final Response

One fresh task context handled the same three requests on the final source snapshot. Baseline core judgments already passed; no controlled general writing gain is established. Wrapper, local-reference links if any and whitespace only are normalized; raw answers remain private.

说明：上下文含预置历史摘要；本次仅依据题设与指定 Skill 的当前相关说明作答。A–C 共用同一上下文，不是独立模型运行，也不声称记忆空白或内部轨迹完整。

**M4145-A**
作者注：可以称为生成式 zero-shot。边界是未见类没有真实训练测量，不是分类器损失中不能出现其 ID。400 个合成向量的类别来自生成条件，不是400次真实采集或人工故障标注。历史已见类标签和专家语义仍是监督资源，因此也不是“完全无标签学习”。

英文方法说明，39词：

> Using four seen faults' labeled features and descriptions, a generator synthesizes 200 feature vectors per unseen class from expert descriptions predefined for all six classes. Conditioning IDs label synthetic examples for six-class classifier training, without additional real fault acquisition.

**M4145-B**
作者注：
- 这是通过语义比较识别具体故障名的 zero-shot 诊断，不是仅拒识 unknown。未见类专测还须明确候选标签集合：候选仅含未见类时为常规 ZSL；已见/未见联合识别为 GZSL。未见类专测不必强制报告已见/未见调和指标。
- 取 \(S=0.9,\ U=0.3\)，调和均值为 \(H=2SU/(S+U)=0.45\)，即45%；0.6是算术均值。
- 全部无标签目标测量共同参与批量调整，具有 transductive 信息访问，不是纯 inductive 评估。此适应可以合法采用，但应披露调整对象、目标数据访问和选择边界，并匹配比较方法的访问条件。预先提供未见类语义本身不否定 ZSL。

英文预测路径，32词：

> An encoder maps process measurements into a semantic-space vector, which is compared with predefined candidate fault-description vectors. The matching candidate supplies the predicted fault name, including unseen faults without labeled training measurements.

**M4145-C**
英文摘要，169词：

> Acquiring labeled measurements of rare industrial faults can be unsafe and difficult, leaving some fault categories unrepresented in diagnostic training data. This study investigates zero-shot diagnosis using labeled measurements from four seen fault classes and expert descriptions specified in advance for all six classes. A generator is trained on seen-class features with the corresponding descriptions as conditions. A semantic reconstruction constraint requires generated features to reconstruct their conditioning descriptions, guiding feature generation toward the supplied class semantics. After learning, the generator synthesizes features for the two unseen classes. These synthetic features and their conditioning class IDs are combined with real seen-class features and labels to train a six-class classifier. For real test measurements, an encoder extracts features and the classifier predicts a specific fault category. Evaluation uses independent class splits without target-measurement adaptation, with hyperparameters fixed using permitted training and development data. Comparisons on simulated benchmarks and production measurements show higher unseen-class mean accuracy and a higher seen/unseen harmonic mean than existing zero-shot methods, alongside lower seen-class mean accuracy.

一项贡献候选，32词：

> Descriptor-conditioned feature generation is constrained by reconstructing each conditioning description from its generated features. Synthetic unseen-class features complement real seen-class features in training a classifier that predicts fault categories from encoded measurements.

作者注：重构约束指导生成学习，不是预测时的文本融合；题设预测路径仅保留编码器和分类器。贡献候选描述实际设计，未把既有 zero-shot 设置或普通验证列为创新；新颖性另核。摘要保留了已见类准确率下降这一权衡。

词数按空格分词，连字符连接词及斜线连接项各计一词。
