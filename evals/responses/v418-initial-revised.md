**M418-A**

**不能直接将 Dual Cross-Attention 作为通用名称入库。** 两个分支各自从同一表征生成 Q、K、V，实际执行的是沿不同维度的 self-attention；并行计算和输出拼接不构成交叉注意力。完整名称的入库需要至少两篇独立、语义匹配的已发表论文支持，并单独核验中文名称，不能仅凭同名论文标题或基础术语已获认可。

英文方法描述：

> Two parallel branches perform self-attention along the temporal and variable dimensions, respectively, with each branch projecting its queries, keys, and values from its own input representation. The outputs of the two branches are then concatenated.

中文建议采用描述性名称“**时间维与变量维的双分支自注意力**”。“双分支”表示两条并行路径，“自注意力”表示各分支内部 Q、K、V 的同源关系；该完整表述不冒充已核验的通用模块名称。

**M418-B**

> The soft sensor uses a mixture-of-experts model that evaluates four linear local predictors for every sample and combines all four predictions using softmax weights computed from linear gating scores. During training, L1 penalties are applied to the coefficients of both the predictors and the gating function to encourage parameter sparsity.

中文可称“**采用线性专家和 softmax 门控的混合专家模型**”。这里的稀疏性指 L1 正则化所促进的系数稀疏，不是专家选择或执行稀疏：四个预测器仍全部求值。混合专家不要求专家必须是神经网络；当前事实也不支持“按离散工况选择专门子网络”或“降低推理时延”。

**M418-C**

**可以保留 cross-attention，不应因特征来自同一幅图像就改称 self-attention。** 判断依据是查询与键值所用表征之间的关系，而非是否存在两种模态。

> The module performs cross-attention using queries projected from features at one encoder scale and keys and values projected from the concatenated features at five scales of the same image, with the resulting attention weights used to aggregate the values.

中文说明：这里的“**交叉注意力**”表示单尺度查询对多尺度键值表征进行注意力聚合，即使键值集合包含查询所在尺度、所有特征来自同一幅图像，也不妨碍这一称谓。

**M418-D**

**可以保留 sparse expert routing。** 这里确实只选择并执行部分专家，稀疏性有明确的计算依据；但尚不能据此宣称时延或显存收益。

英文方法说明：

> With model parameters fixed after training, sparse expert routing selects and executes only the two highest-scoring neural network experts out of eight for each input and combines their outputs by weighted summation.

中文贡献表述：

> 在工业诊断模型中构建输入依赖的稀疏专家路由机制，通过 top-2 门控从八个神经网络专家中选择并仅执行两个专家，再对其输出加权求和，在训练后参数保持固定的条件下实现随输入变化的专家调用。
