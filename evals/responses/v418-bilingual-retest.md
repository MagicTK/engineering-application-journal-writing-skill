**M418-A**

**不能直接将 Dual Cross-Attention 收入通用工程术语库。** 你描述的是两个沿不同维度计算的自注意力分支，输出拼接并不构成交叉注意力。即使已发表论文使用同名架构，也应保留其来源归属，不能仅凭标题将其推广为通用类别；完整名称的入库还需至少两篇独立、语义匹配的已发表论文及单独的中文译名核验。

英文方法描述：

> Two parallel branches perform self-attention along the temporal and variable dimensions, respectively, with each branch projecting its queries, keys, and values from its own input representation. The outputs of the two branches are then concatenated.

中文可描述为“**时间维与变量维的双分支自注意力**”：双分支指两条并行路径，自注意力指各分支内部 Q、K、V 来自同一表征；这是准确的功能描述，不宣称该完整名称已成为通用术语。

**M418-B**

> The soft sensor uses a mixture-of-experts model that evaluates all four linear experts for each sample and combines their predictions using weights obtained by applying softmax to linear gating scores. During training, L1 penalties are applied to the coefficients of both the experts and the gating function to encourage parameter sparsity.

中文可称“**采用线性专家和 softmax 门控的混合专家模型**”。混合专家不要求专家必须是神经网络；这里的 L1 惩罚促进的是系数稀疏，不代表只执行部分专家。由于四个预测器全部求值、没有离散工况定义或时延结果，应删去“选择工况专属子网络”和“降低推理时延”的表述。

**M418-C**

**可以保留 cross-attention，不应仅因特征来自同一幅图像而改为 self-attention。** 交叉注意力并不要求两种模态。

> The module performs cross-attention using queries projected from features at one encoder scale and keys and values projected from the concatenated features at five scales of the same image, with the resulting attention weights used to aggregate the values.

中文说明：这里的“**交叉注意力**”指单尺度查询对多尺度键值表征进行注意力聚合，判据是查询与键值所用表征的关系，而非是否跨模态，键值集合也可以包含查询所属尺度。

**M418-D**

**可以保留 sparse expert routing。** 仅执行所选的两个专家，已明确支持“稀疏专家路由”的描述；参数固定不妨碍选择随输入变化，但这不是在线参数学习，也不能直接推出时延或显存收益。

英文方法说明：

> With model parameters fixed after training, sparse expert routing selects and executes only the two highest-scoring neural network experts out of eight for each input and combines their outputs by weighted summation.

中文贡献表述：

> 在工业诊断模型中构建输入依赖的稀疏专家路由机制，通过 top-2 门控从八个神经网络专家中选择并仅执行两个专家，再对其输出加权求和，实现训练后参数固定条件下随输入变化的专家调用。
