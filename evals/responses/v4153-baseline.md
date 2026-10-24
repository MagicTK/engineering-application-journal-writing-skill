# Fictional Target-Stage Baseline

One task context handled two requests on the immutable v4.1.52 release. Core science already passed and the answer accurately reported the missing scoped full-name record. No controlled general writing gain is claimed. Wrapper, links and whitespace only are normalized; raw records remain private.

本轮在同一上下文处理 A、B，含预置历史，不是“记忆空白”或两次独立模型实验；也无法提供完整内部服务轨迹。仅核读指定 Skill 与适用参考，未外查或执行实验。

**A**

作者说明：
- **计算：**均值为 `3`，偏置由 `0` 调整为 `−3`。调整前 `f(2)=2，f(4)=4`；调整后 `f(2)=−1，f(4)=1`。
- **变化对象：**第一种只是固定函数产生输入相关的系数值，不能据此认定在线参数学习。第二种更新统计参考 `b`，同时改变了 `f` 的加性偏置；若它存作网络参数，该参数也确实改变。统计参考、类别语义参考与网络参数应按实际角色区分，不能以是否反向传播判定一切适应。
- **数据与时间：**明确允许的无标签目标整批访问不必然泄漏，但属于批次访问，不能冒充逐样本因果预测。对 `2` 的调整结果依赖 `4`，不能称为只见首个样本时的零延迟结果。适应阶段 source-free 限定该阶段不访问源样本，不否认源训练历史或模型保留的源知识。
- **命名记录：**按[准入规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/89a9deec630dbeb2f1971698eb55bf4cdedd2540/references/engineering-application-terminology-bank.md#L19)和[现有记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/89a9deec630dbeb2f1971698eb55bf4cdedd2540/references/published-evidence.md#L485)，基础名 **test-time adaptation** 尚未完成所要求的两篇工业论文匹配定义及独立中文原始记录。普通 domain adaptation、continual learning 或 P05 单篇的 test-time semantic adjustment 专名不能补位。未完成不等于词无效；可保留准确描述或作者批准的新名，也不能自动准入任意完整 **Replay-Test-Time Fusion** 名称，本例更未给出回放或融合操作。

方法句，32 词：
> Before prediction, the model sets its additive reference bias to the negative mean of the permitted unlabeled target batch, then adds this adjusted bias to each sample to obtain the batch outputs.

**B**

摘要，126 词：
> ControlRefFD detects industrial anomalies through control-conditioned correction of sensor reconstructions. A reconstructor is first trained on healthy source data to reconstruct only sensor measurements from joint sensor and control inputs. With the reconstructor frozen, a corrector driven by control variables is fitted before evaluation on a small set of confirmed healthy target calibration samples by minimizing corrected sensor reconstruction error. During evaluation, both networks retain fixed weights, while the corrector adapts its normalization statistics using the currently available control-variable batch. Its correction is added to sensor reconstructions, and the resulting sensor residuals are compared with a predetermined threshold. Across two held-out industrial cases, ControlRefFD yields lower false alarm rates at matched detection rates than the same model evaluated without updates to normalization statistics at test time.

设计贡献候选，待新颖性核查，34 词：
> ControlRefFD couples source-trained sensor reconstruction with a control-driven corrector fitted by minimizing corrected reconstruction error on healthy target samples, then adapts the corrector's normalization statistics batchwise to supply additive corrections for residual-based anomaly detection.

作者说明：
- 保留批准名称 **ControlRefFD**，不擅加中文全名。源训练重构器使用 `x,w`、仅重构 `x`；健康目标校准时固定 `theta`、拟合 `phi`。`h_phi(w)` 的前向输入只有控制变量，但拟合损失使用传感测量及其重构，已确认健康也是监督信息，不能抹去。
- 评价时 `theta/phi` 与阈值固定，仅更新 `h` 的归一化统计，仍有测试期统计适应。允许先访问完整当前控制变量批次，不涉及未来批次、目标故障类别标签或评价标签调参；不宣称零延迟。
- 贡献候选针对上述连接设计，普通统计更新不单列为发明。证据仅支持给定两案相同检测率下较低误报，不支持运行时延、物理因果、跨厂泛化或独立新颖性结论。词数按空格分词，连字符词计一词，仅适用于本练习。
