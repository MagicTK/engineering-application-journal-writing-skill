**M418-A**

不宜将 **Dual Cross-Attention** 直接收入通用工程术语库。按你给出的计算过程，每个分支内部的 Q、K、V 来自同一输入表征，属于 self-attention；沿不同维度并行计算、再拼接输出，并不构成 cross-attention。完整名称的通用入库还需至少两篇独立、语义匹配的已发表论文支持，并单独核验中文名称，不能由基础词的认可推及整个复合名称。

:::writing{variant="standard" id="41801"}
Two parallel branches perform self-attention along the temporal and variable dimensions, respectively, with the queries, keys, and values in each branch projected from the same input representation within that branch. The outputs of the two branches are then concatenated.
:::

中文可描述为“**分别沿时间维和变量维计算的双分支自注意力**”。“双分支”指两条并行计算路径，“自注意力”指各分支内部 Q、K、V 的同源关系；这是与你的方法对应的描述性名称，不将其宣称为已获通用认可的完整术语。

**M418-B**

:::writing{variant="standard" id="41802"}
The soft sensor uses a mixture of four linear experts, evaluating all four for each sample and combining their predictions using weights obtained by applying softmax to linear gating scores. During training, L1 penalties are applied to the coefficients of both the experts and the gating function to encourage parameter sparsity.
:::

可保留 **mixture-of-experts** 这一符合计算结构的方法类别，中文可描述为“**由 softmax 门控加权的四个线性局部预测器组成的混合模型**”。这里的 L1 惩罚促进的是参数稀疏，并非只激活部分专家：四个预测器仍全部执行。现有事实也不支持“神经子网络”“按离散工况选择专门模型”或“降低推理时延”，因此这些表述均应删除。

**M418-C**

不应仅因特征来自同一幅图像就改称 self-attention。按你描述的查询与键值来源，可以保留 **cross-attention**；是否跨模态不是其必要条件。

:::writing{variant="standard" id="41803"}
Cross-attention uses queries projected from features at one encoder scale and keys and values projected from the concatenated features at five scales, with the resulting attention weights used to aggregate the values.
:::

中文可解释为“**单尺度查询对多尺度键值特征进行注意力聚合**”，这里的“交叉”体现查询与键值所用表征集合的区别，而不是要求两种模态；此中文表述是功能说明，不宣称为已独立核验的标准译名。
