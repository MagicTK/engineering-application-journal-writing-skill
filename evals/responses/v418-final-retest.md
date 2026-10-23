**M418-A**

**不能直接将 Dual Cross-Attention 作为通用术语入库。** 你描述的是分别沿时间维和变量维计算的自注意力，拼接两路输出并不构成交叉注意力。论文特有架构名可以带来源保留，但完整名称成为通用推荐，需要至少两篇独立、语义匹配的已发表论文支持，并单独核验中文译名，不能仅凭标题中的同名用词。

英文方法描述：

> Two parallel branches perform self-attention along the temporal and variable dimensions, respectively, with the queries, keys, and values in each branch projected from that branch’s own input representation. The outputs of the two branches are then concatenated.

中文建议描述为“**时间维与变量维的双分支自注意力**”：双分支指并行计算路径，自注意力指各分支内部 Q、K、V 来自同一表征；这一完整表述是功能描述，不宣称为已获通用认可的模块专名。

**M418-B**

> The soft sensor uses a mixture-of-experts model that evaluates all four linear experts for each sample and combines their predictions using weights obtained by applying softmax to linear gating scores. During training, L1 penalties are applied to the coefficients of both the experts and the gating function to encourage parameter sparsity.

中文可称“**采用线性专家和 softmax 门控的混合专家模型**”。混合专家不要求专家必须是神经网络；本方法中的 L1 惩罚促进系数稀疏，并不意味着稀疏执行或只选择一个专家。四个预测器全部求值，门控权重也没有被定义为离散工况标签，因此应删除“选择工况专属子网络”和未经测量支持的“降低推理时延”。

**M418-C**

**可以保留 cross-attention，不应仅因特征来自同一幅图像而改称 self-attention。**

> The module performs cross-attention using queries projected from features at one encoder scale and keys and values projected from the concatenated features at five scales of the same image, with the resulting attention weights used to aggregate the values.

中文说明：这里的“**交叉注意力**”表示单尺度查询对多尺度键值表征进行注意力聚合，不要求跨模态，键值集合包含查询所属尺度也不改变这一判断。

**M418-D**

**可以保留 sparse expert routing。** 此处确实只执行所选专家，稀疏性有实际计算依据；参数固定不妨碍路由随输入变化，但不构成在线参数学习，也不直接证明时延或显存收益。

英文方法说明：

> With model parameters fixed after training, sparse expert routing selects and executes only the two highest-scoring neural network experts out of eight for each input and combines their outputs by weighted summation.

中文贡献表述：

> 在工业诊断模型中构建输入依赖的 top-2 稀疏专家路由机制，从八个神经网络专家中选择并仅执行两个专家，再对其输出加权求和，实现训练后参数固定条件下随输入变化的专家调用。
