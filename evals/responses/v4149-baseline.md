# Fictional Gating-Path Baseline

One task context handled two constrained requests on the immutable v4.1.48 release. Core judgments already passed; stronger evidence records do not establish a controlled writing gain. Artifact wrapper and whitespace only are normalized; raw records remain private.

预设限制：当前上下文带有历史摘要，不能视为记忆空白或保证历史信息零影响；本次未另读历史材料，也不声称提供完整内部服务轨迹。A、B 共用一个上下文，不是两次独立模型实验。

**A**
方法句，24 词：

> The module scales the feature branch with elementwise sigmoid gates and adds the gated features to the unchanged input to form the residual output.

作者说明：
- `g⊙v=[0.4,-2.4]`，所以 **`y=[2.4,-5.4]`**。乘法分支的幅值缩小，但最终 `y=(1+g)⊙v`，两维幅值分别增至原来的 **1.2、1.8 倍**，并非最终输出抑制所有特征。
- 强制 `g=0` 得到 `y=v=[2,-3]`，关闭乘法分支、仅保留原特征；强制 `g=1` 得到 `y=2v=[4,-6]`，取消分支衰减、保留两路相加。后者可以是双路径结构的恒开门对照，但不是“仅保留原特征”对照。
- 小门值不等于删除变量，残差旁路仍保留原特征；特征坐标也未必对应物理变量。sigmoid 的数值范围不足以建立故障概率语义，仍需明确事件及相应建模依据。
- 原文称其为 attention，可以保留名称并明确实际运算；不能仅凭这个词改动计算，也不能否认其乘法调节作用。这里是 sigmoid 软门控，不代表所有门控都必须采用同一种归一化或硬选择。

**B**
摘要，112 词：

> Industrial classification can use complementary information from individual variable histories and variable neighborhoods. We propose Context-Gated Fusion to combine these representations through input-dependent modulation. A local encoder produces variable history features, while a relation encoder produces neighborhood features. A multilayer perceptron receives their concatenation, and a sigmoid converts its outputs into elementwise gates that scale the neighborhood features. The scaled features are added to the local features through a residual connection, forming the classifier input. After training, the perceptron parameters remain fixed while the gates vary with each input. Across the two evaluated cases, classification accuracy exceeds that of a fixed-gate control using 0.5, with all other model and training settings unchanged.

贡献候选，35 词：

> We propose Context-Gated Fusion: sigmoid gates derived by an MLP from concatenated history and neighborhood features modulate neighborhood features before residual addition to history features, improving classification accuracy over matched fixed-0.5 controls in two cases.

作者说明：
- 计算定义为 `g=sigmoid(MLP(concat(x,h)))`、`r=x+g⊙h`。两类特征先完整计算，门调节的是 `h`；输入相关门值变化不等于参数持续学习，也不是稀疏专家调度、工况概率或采样控制。
- 保留作者批准的 **Context-Gated Fusion** 作为本文提出的新组合名，不作为通用术语入库，也不因缺少前人同名而否决。中文可用基础词“门控机制”；完整中文名未获批准且未核实，故不擅定，不借用 **Age-Aware State Gate** 或“年龄门控”。
- 结果仅限题设两例及匹配的固定 `g=0.5` 对照，不补造提升数值或显著性，不扩展到延迟、省算、跨厂或在线部署。正式稿需作者核对维度对应、公式实现及两例结果记录；本次未作实证复核。

计词按空格分隔，连字符复合词计一词；这些字数限制仅适用于本题。
