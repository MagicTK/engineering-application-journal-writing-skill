# Fictional Multihead Final Response

One fresh task context handled the same two requests on the final frozen source; only the read root changed. The prior response was already scientifically correct. The new record changes evidence availability, not a demonstrated general writing gain. Wrapper, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

本次是同一上下文中的两项请求，不是两次独立模型实验。上下文含预置历史，不能声称记忆空白或可核验完整内部服务轨迹；本轮未额外读取历史、评测、私有审计或实际论文。

**A**
> Each head derives queries, keys, and values from the same input sequence, computes attention-weighted value features, and contributes them to a feature-axis concatenation whose multiplication by the output projection matrix produces the final output.

作者说明：
- **算术**：`H1=(3,4)ᵀ`，`H2=(-1,8)ᵀ`；逐 token 沿特征轴拼接得到 `[[3,-1],[4,8]]`，乘给定 `WO` 得到 **`(1,20)ᵀ`**。仅按给定归一权重计算，不反推未提供的 Q/K。
- **合并对照**：先均值得 `(1,6)ᵀ`，相加得 `(2,12)ᵀ`，均不等于本题输出。均值为 `2×1`，不能继续乘原来的 `2×1 WO`；不得擅补映射。特定投影可以实现和或均值，但不构成恒等关系。
- **五项说法**：头数不等于传感器数或故障类数；相加、均值与拼接不恒等；行归一化只约束权重，不保证最终特征为概率；不同投影不证明独立物理关联；多头也并非普遍优于单头。
- **输入关系**：同一序列经不同 Q/K/V 投影仍可属于 self-attention。若 Q 改来自另一输入，应核对来源及查询方向、所关注的轴、Q/K 匹配维度、时序对应与掩码，以及输出是否随查询位置排列；头数不变不能决定 self/cross 分类。
- **词库状态**：当前[完整多头条目](../../references/engineering-application-terminology-bank.md)已有 P11/P82 的双论文定义记录，范围限于所核对的投影自注意力形式。[中文独立条目](../../references/engineering-application-terminology-bank.md)已记录完整 **multi-head self-attention／多头自注意力（机制）**，但未见完整 **multi-head attention** 的单独中文核验记录，不能由前者或普通 attention/self-attention 补齐。这里只核对现有记录，未重新核验来源；其中第二中文来源仅标题可用，摘要未解析。记录未完成不等于术语无效，作者批准的新名及准确描述仍可保留，无须已有同名先例。

**B**
摘要：

> QueryBlend estimates product quality from two aligned streams of process measurements, A and B. Fixed encoders separately produce sequence features, with A supplying queries and B supplying keys and values. Each of two attention heads computes weights and forms a weighted summary of B's value features. The head outputs are concatenated and transformed by a learned projection, then added to the original A features. Averaging over valid temporal positions yields the representation used for quality regression. Training and normalization use training data only. In two held-out industrial cases under matched settings, QueryBlend achieves lower mean absolute error than a single-head control retaining the same encoders.

设计贡献候选，待文献新颖性核查：

> QueryBlend integrates two process-measurement streams directionally: A supplies queries and B supplies keys and values; two head summaries are concatenated, projected, and added to A before valid-position averaging and product-quality regression.

作者说明：
- 保留批准名 **QueryBlend**，不补中文全名。这里是两路过程测量特征间的查询与汇总，可按输入关系描述为 cross-attention；不据此称为 multimodal、self-attention 或稀疏传感器选择。
- 若 A 特征为 `T×dA`，两头输出分别为 `T×dv1`、`T×dv2`，则拼接后的输出投影须映射至 `T×dA` 才能与 A 相加；有效位置均值须明确有效集合且非空。
- 候选针对两流的定向整合及其质量预测路径，不把常规多头运算单列为发明。给定比较只支持这两个案例中的较低 MAE，不证明头独立性、变量删除效果、物理因果或实际时延优势。
- 按空格计词、连字符复合词计一词：A 方法句 **34** 词，B 摘要 **105** 词，贡献候选 **31** 词；字数限制仅用于本合成练习。
