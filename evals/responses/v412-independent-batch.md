## v412-alternating-target-selection

**Abstract method sentences**

Starting from binary training fault indicators, the method alternates neighborhood-based updates of continuous training-label weights with descriptor selection: the currently selected descriptors define the neighborhoods used to update the weights, and those weights guide the next selection. The resulting descriptor indices are frozen, and the trained diagnostic classifier uses only the selected descriptors at prediction time.

**Candidate contribution**

- An alternating training procedure couples neighborhood-derived label weights with descriptor selection, allowing each selected subset to determine the neighborhoods for the next weight update and the updated weights to guide the next subset selection, yielding fixed descriptor inputs for fault diagnosis.

**Consequential corrections**

- The continuous values are constructed training-label weights, not measured physical severity or calibrated probabilities.
- Weight updates and descriptor selection interact repeatedly during fitting; describing them as a one-way sequence loses that reciprocal dependence.
- Selecting descriptors does not establish that physical sensors are removed.
- Prediction uses the frozen descriptor subset and trained classifier; the described method does not fuse labels and features for each prediction.

## v412-supervision-semantics

四项应按监督的粒度、歧义、共存含义和可靠性分别命名。题设未给出支持 few-shot 判断的样本数量；只有 C 明确给出了真实同时存在的故障。

| 研究 | 已知监督形式 | 合适的问题定位 | 关键区分 |
|---|---|---|---|
| A | 每段序列一个异常标签，输出逐时刻报警 | 段级弱监督的逐时刻异常检测 | 标注粒度粗于输出粒度；报警不等于故障类型诊断。 |
| B | 每个样本两个候选故障类型，恰好一个真实 | 候选标签歧义下的单标签故障诊断，可称 partial-label learning | 两个候选是备选类型，不是两种故障同时发生。 |
| C | 完整多热标签，两个正项均表示真实存在 | 完整多标签监督下的并发/复合故障诊断 | 多个正项表达真实共存，不表示标签含糊或缺失。 |
| D | 所有浓度目标均有标注，部分化验值可能不准确 | 目标值可能不准确的浓度回归/软测量 | 问题在目标可靠性，不是标签缺失，也没有输入传感器受扰的依据。 |

各自的英文问题描述：

- **A:** Detect anomalies at individual time steps using only segment-level anomaly labels for training.
- **B:** Identify the true fault type when each training sample is annotated with two candidate types, exactly one of which is correct.
- **C:** Identify co-occurring fault types using complete multi-hot training labels, in which two positive entries indicate two faults that are genuinely present simultaneously.
- **D:** Estimate concentration from process variables when assay targets are available for every sample but some may be inaccurate because of laboratory instrument calibration failure.

## v412-partial-classifier-title

**建议替换**

The method fuses local decisions from classifiers for pairs of known fault types and known classes outside each pair's label set, using complete multi-hot fault labels and a small, nonzero set of compound-fault training samples.

**简短理由**

- 完整多热向量的多个正项表示真实共存，不能转述为 ambiguous candidate labels；这里的 Partial-Label 应按作者定义理解为分类器的局部标签空间，不能仅凭题目推断标注歧义。
- 少量但非零的复合故障训练样本不能写成 without any compound-fault training samples。
- 局部标签集合之外的类别仍是已知类别，不能据此宣称检测系统级未知故障。修改的是综述中的转述，不是对源文方法的全面否定。

## v412-selected-features-not-sensors

**Replacement sentence**

Feature selection reduces the diagnostic classifier's input from eight descriptors to four, while the deployed pipeline still samples all three sensors and computes all eight descriptors before selecting the four inputs.

**Author note**

The halving concerns classifier input width, not sensor count or preprocessing cost. Latency, memory, energy savings, and real-time capability have not been established; stating the four-descriptor input does not require hardware experiments.

## v412-uncertain-assay-evaluation

**Corrections**

The draft conflates TRAIN-only target construction with correction of TEST ground truth, interprets agreement with uncertain assays as accuracy against true concentration, and attributes the problem to sensor noise that has not been established.

**Bounded replacement**

The model derives continuous targets from neighboring TRAIN samples for training and achieves a lower MAE in the reported comparison against the unchanged TEST assay values. Because an unknown subset of those assay values may be inaccurate, this result establishes better agreement with the recorded TEST assays but does not establish improved accuracy relative to true concentration.

**One practical verification item**

Audit the saved split IDs and evaluation files to confirm that neighbor-based target construction uses only TRAIN samples, the original TEST assay vector remains unchanged and is shared across the reported comparison, and the saved predictions reproduce the reported MAE. This checks the existing comparison without treating model-generated values as test references or establishing assay validity.
