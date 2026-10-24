# Fictional Attention-Relation Final Response

One fresh task context answered the same two requests on the frozen final source; only the read root changed. The earlier response already passed core science and writing. The new record changes maintained evidence availability, not a demonstrated general writing gain. Wrappers, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

**A．机制与术语**
以下依据本地 Skill v4.1.56 的维护记录；本轮未联网重核原文。

| 设计 | 输入关系 | 多头标签 |
|---|---|---|
| design1 | Q/K/V 均由同一编码序列 X 投影得到，属于 self-attention。 | 可同时称 multi-head self-attention。 |
| design2 | U 提供查询，拼接的 [U;V] 提供键和值，属于跨尺度 cross-attention；上下文包含查询自身的尺度。 | 可同时称 multi-head cross-attention。 |

- **不同投影矩阵不等于不同物理来源。** self/cross 描述输入关系，multi-head 描述并行头结构，并非三个互斥机制。
- cross-attention **不要求不同模态，也不要求从键值集合排除 U**。本题的两个尺度均来自同一测量窗口；两个头也不代表两个生产阶段。
- 注意力行归一化的是键位置上的权重。加权特征及其后续投影不是因此就成为类别概率，更不自动获得概率校准。[操作边界](../../references/terminology-decisions.md)

英文操作记录的范围也有限：P11 PDF p.3、式(3)–(4)与 P82 PDF p.4、式(4)/图5支持已核对的投影式多头自注意力；P24 p.3 **不是第三份已核对的头输出合并定义**。cross-attention 的配对记录是 P38 p.6、式(7)与 P43 pp.4–5、式(1)–(2)/图6–7，后者明确包含拼接尺度上下文。[英文记录](../../references/engineering-application-terminology-bank.md)

**三个中文记录的实际状态，分别如下：**

| 完整英文项 | 当前中文状态 | 库内确切来源与阅读范围 |
|---|---|---|
| generic multi-head attention | **已独立核验：多头注意力（机制）**，不是从子类继承。 | 《系统仿真学报》2025, 37(10):2594–2604，DOI `10.16182/j.issn1004731x.joss.24-0490`：原始中英文摘要；《自动化学报》2023, 49(9):1889–1903，`c220767`：图1中英文图注。不是完整方法正文核验。[记录](../../references/engineering-application-terminology-bank.md) |
| self-attention | **已核验：自注意力。** | 《自动化学报》`c220027`：图2中英文图注；`c220715`：中英文摘要。支持基础译名，不自动准入所涉完整变体名。[记录](../../references/engineering-application-terminology-bank.md) |
| multi-head self-attention | **已单独核验：多头自注意力（机制）。** | 《化工学报》2024, 75(12):4654–4665：中英文摘要及关键词；《江苏大学学报（自然科学版）》2023, 44(4):444–451，DOI `10.3969/j.issn.1671-7775.2023.04.011`：中英文标题。后者摘要正文仍为未解析模板，不能算已读摘要。[记录](../../references/engineering-application-terminology-bank.md) |

这些中文来源证明的是译名，不增加工程操作定义的来源数量。同一工作的预印本、期刊版和镜像只计一次；未列入也不等于术语无效。

**基础记录不能准入完整名称 “Spatio-Causal Multihead Cross-Process Gating Module”。** 各基础词的记录不能拼接成完整名称的通用准入，本题也未提供其空间、物理因果、跨过程或额外门控含义的依据。作者自拟名称是另一状态，需要批准及操作定义。[完整名称规则](../../references/engineering-application-terminology-bank.md)

以下词数统一按空白分词，连字符词、`[U;V]`、`U's` 各计一词。

方法句：**32 words**
Multi-head cross-attention uses two separately projected heads with queries from coarse-scale U and keys and values from concatenated [U;V] to aggregate features across two temporal resolutions of the same measured process window.

**B．作者说明**
保留批准的英文提议名 ScaleQueryFD，不另造中文全名。贡献项仅为候选表述，创新性比较仍待核验；普通多头或交叉注意力本身不作为创新依据。结果只采用合同给出的一个模拟基准比较，不补数值、显著性或外推结论。

摘要：**129 words**
ScaleQueryFD is proposed for known-class fault classification from multivariable industrial-process windows. Parallel convolutional branches encode each window at two temporal resolutions, producing U and V. Queries from coarse U attend to keys and values from concatenated [U;V], allowing each coarse position to aggregate context across both scales. Two separately projected heads produce feature outputs that are concatenated and mapped through a learned output projection. The transformed output is added to a dimension-matched U bypass, and mean pooling over U's sequence positions supplies the classifier with a window summary for an endpoint class decision. Prediction uses fixed weights and measurements available within the completed window before the decision. In one simulated process benchmark case, ScaleQueryFD yields lower classification error than the same encoder and predictor without the cross-scale attention path.

候选贡献：**35 words**
ScaleQueryFD links coarse-scale queries to concatenated temporal-scale context and classifies their residual mean-pooled summary, yielding lower classification error in one simulated process benchmark comparison against the same encoder and predictor without the cross-scale attention path.
