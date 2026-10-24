# Fictional Attention-Relation Baseline

One task context answered two requests on the immutable v4.1.55 release. Scientific and writing distinctions already passed; the response correctly reported the missing separate generic Chinese multi-head attention record. Wrappers, local links/line suffixes and whitespace only are normalized; raw records remain private.

以下按虚构契约作答。来源阅读深度均指发布包的维护记录，不代表本轮联网复核。

**A：机制判断**
三者不是互斥分类：multi-head 描述头的组织方式；self-attention／cross-attention 描述查询与键值的输入表征关系。

| 设计 | 输入关系 | 可共存的标签 |
|---|---|---|
| design1 | 每头的 Q、K、V 均由同一表征 X 投影得到，属于 self-attention | multi-head self-attention |
| design2 | Q 来自 U，K、V 来自 `[U;V]`，属于同一测量窗口内的跨尺度 cross-attention | multi-head cross-attention |

不同投影矩阵只是不同的学习映射，不意味着不同物理来源，也不证明头间统计独立。cross-attention 不必跨模态，其键值集合可以包含查询所属的 U；两个头也不意味着两个生产阶段。

注意力行归一化约束的是被关注位置上的系数，不是故障类别上的校准概率。加权特征以及后续拼接、投影输出不会因此成为校准故障概率。依据见[操作判别规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/9659045c9ed670f767a04778936382265b229668/references/terminology-decisions.md#L171)。

**中文准入状态**
须分别报告，不能从子类型继承通用词的记录：

| 完整英文术语 | 当前库中实际中文状态 | 记录的来源与阅读范围 |
|---|---|---|
| generic multi-head attention | **没有独立完成的中文核验记录**。不能泛译成“多头自注意力”，也不能声称“多头注意力”已通过本库独立核验 | 英文基础条目存在，但范围限定为已核投影自注意力形式；这不补足通用词的中文记录 |
| self-attention | **已单独核验：自注意力** | 《自动化学报》c220027，图2双语图注；c220715，双语摘要。不是两篇完整方法全文阅读 |
| multi-head self-attention | **已单独核验：多头自注意力（机制）** | 《化工学报》2024，75(12)：4654–4665，原始双语摘要及关键词；《江苏大学学报（自然科学版）》2023，44(4)：444–451，原始双语题名。后者摘要为未解析模板，未计为已读证据 |

对应维护位置：[英文操作记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/9659045c9ed670f767a04778936382265b229668/references/engineering-application-terminology-bank_CN.md#L164)、[独立中文核验记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/9659045c9ed670f767a04778936382265b229668/references/engineering-application-terminology-bank_CN.md#L224)。

英文定义证据也有明确范围：self-attention 对应 P11、P24 的 PDF p.3；受限多头形式对应 P11 p.3 式(3)–(4)及 P82 p.4 式(4)、图5。维护记录注明 P11 读取了 p.1 元信息及选定 pp.2–4，并视检 p.3；P82 读取了 p.1 元信息及选定 pp.4–5，并视检 p.4。P24 p.3 已读、已渲染，但未展开头合并操作，不能算第三个合并定义来源。见[阅读范围记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/9659045c9ed670f767a04778936382265b229668/references/published-evidence.md#L106)。

按学术作品去重：不同版本、镜像及中英文维护表不构成新增来源；中文译名页也不增加工程操作定义计数。未列入不等于无效。

基础记录**不能准入**完整名称 “Spatio-Causal Multihead Cross-Process Gating Module”。该全名没有已完成的维护记录；基础 attention／gating 记录不能替其中所有限定词背书。作者批准的新提名称可另行定义，但不能据此宣称它是既有通用类别。见[完整名称准入规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/9659045c9ed670f767a04778936382265b229668/references/engineering-application-terminology-bank.md#L19)。

**英文方法句**
35 words。以下三项均按空格分词；连字符词、`[U;V]`、`U's` 各计一词。

Two attention heads use separate learned projections to form queries from coarse-scale sequence U and keys and values from concatenated sequences [U;V], producing context-weighted features from two encoder scales of the same measured process window.

**B：作者核查**
保留作者批准的英文提议名 ScaleQueryFD，不扩写未批准的中文全称。贡献仍是候选，独创性比较待完成，普通多头注意力本身不作为创新依据。契约只给出单个模拟基准个案的相对误差结果，不能补入误差数值、显著性或第二个案例。

完整窗口在端点决策前已经可用，因此窗口内部的位置交互与该决策时间边界相容；这不构成提前预警或物理因果证据。以下正文只陈述契约中的计算路径和比较结果。

**英文摘要**
130 words。

ScaleQueryFD classifies known fault classes from completed multivariable industrial-process windows. Parallel convolutional branches encode each window at two temporal resolutions, producing a coarse sequence U and a second sequence V. Queries from U attend to keys and values projected from the concatenation [U;V], allowing coarse positions to aggregate context from both scales. Two heads use separate learned projections; their feature outputs are concatenated and mapped through a learned output projection. This transformed output is added to a dimension-matched U bypass, and mean pooling over U's sequence positions produces the summary used for the endpoint class decision. Prediction uses fixed model weights and measurements available within the completed window. In one simulated process benchmark case, ScaleQueryFD yields lower classification error than the same encoder and predictor without the cross-scale attention path.

**英文候选贡献**
36 words。

ScaleQueryFD forms a mean-pooled residual summary from coarse-query attention over concatenated temporal scales for endpoint fault classification, yielding lower error in one simulated benchmark case than the same encoder and predictor without the cross-scale attention path.
