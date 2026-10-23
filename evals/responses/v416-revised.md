# 4.1.6 Revised-Source Terminology Responses

The following are actual responses to fictional requests, not real paper evidence. The first four follow rereading the frozen 4.1.6 source; the last two were requested after that freeze in the same responding context. One private local Skill link target is normalized to a repository-relative link in this public copy. No scientific prose is changed. Original responses remain in private execution records.

## Four Repeated Requests

**compound-name-evidence**
**不作为工业诊断的通用模块收录。** `Acquisition-Age Gating` 可保留为 **A 的论文特有专名**；其通用类别地位及“年龄门控”这一译名，应分别标为证据不足。

各项证据的作用如下：

- **A 的正文定义与公式**：有效，确立 A 对完整名称的定义，以及时间间隔、观测标记与 sigmoid 权重的关系。
- **A 的预印本**：与期刊版属于同一研究，不能重复计为独立来源。
- **A 的首页题名**：既不是另一篇论文，也不增加一个独立的操作定义。
- **B 的正文**：可支持其普通 gating mechanism 的用法，但以当前特征产生权重，并不构成对 `Acquisition-Age Gating` 完整名称的同义验证。

因此，完整名称只有 **一项独立已发表研究**支持，没有满足共享库的多来源准入要求。当前实现使用相应输入，只能说明功能描述应保留这些输入，不能反过来证明名称通行。无需改变实现，可写：

:::writing{variant="standard" id="83146"}
模型根据距最近一次测量的时间间隔和观测标记计算门控权重。
:::

**attributed-name-versus-family**
A source-attributed Related Work sentence is:

:::writing{variant="standard" id="83147"}
Paper C’s Selective Quality Evidence Bridge (SQEB) selects available process measurements using a mask and maps them to the quality predictor through a learned projection.
:::

**Retain the attributed name; do not admit SQEB as a standard method family.** C supplies a definition sufficient to describe its own component fairly, but no evidence of broader adoption.

The admission rule concerns at least two distinct, relevant published papers with matching meanings, not necessarily two different journal titles. It governs promotion to a reusable category, not whether a source-specific name may appear in Related Work. SQEB may remain in the manuscript’s source-specific terminology map.

**translation-object-collision**
**两篇“交叉注意力”论文不能验证当前 cross-attention 的中文模块名。** 它们对应的英文是 `Criss-Cross Attention`，定义的是沿图像行列收集信息；当前操作则由振动信号提供查询、电流信号提供键和值。中文同形和英文词根相近，都不能消除对象与操作的差别。

译名证据暂缺时，可保留英文并作操作性说明：**“采用 cross-attention，其中查询来自振动信号，键和值来自电流信号。”** 这是定义当前操作，不是宣布某个中文译名已获验证。Skill 中已有的 self-attention 译名记录，也不能替代这一核查。

通信来源支持的是其定义范围内的 **Age of Information → 信息年龄**，不能据此验证“信息年龄门控”或其他带 age 的完整模块名。若需描述 gate，应保留已有英文名称，并说明已经核实的输入与作用；本案例没有给出该 gate 的定义，不能补造机制。

**不应全面禁止“信息年龄”。** 当所指量与该来源的 AoI 定义一致时可以使用；是否适用于当前模型仍需核对定义。缺少匹配证据不等于词语本身错误。

**two-contexts-with-scope**
**Admitted general term: `feature fusion`.** Its scope is combining multiple feature representations at the feature level, with their sources and combination operation specified.

The supplied packet provides two distinct, substantively matched contexts:

- **D, Methods p.4:** temperature-sequence and spectral features are combined before quality regression.
- **E, Methods p.3:** two vibration-derived representations are combined before machinery classification.

These support the general combining operation despite different inputs and downstream tasks. Different sensing modalities are not required. They do not establish field-wide prevalence, a particular fusion operator, improved performance, or causal, topological, or reliability properties.

**Chinese status is separate.** D and E supply no Chinese translation evidence. Independently, the [Skill’s bilingual bank](../../references/engineering-application-terminology-bank_CN.md) already records `feature fusion / 特征融合` as verified through a Chinese scholarly source’s bilingual abstract and keywords. That existing record supports the base translation, not industrial prevalence or the expanded compound name; it is not a fresh online check.

Remove `causally reliable production-topology`, because the stated implementation contains none of the corresponding mechanisms or analyses. A concise method sentence is:

:::writing{variant="standard" id="83148"}
The model uses feature fusion to combine features from its two measured-signal paths.
:::

## Two Post-Freeze Requests

**same-word-different-operation**
**“跨域特征对齐模块”不适用于当前实现。** 当前只有测量的时间戳匹配，没有源域与目标域的隐特征学习或分布差异损失；该名称会暗示尚未实现的操作。

- **F**：对象是测量，操作是按时间戳接近程度进行匹配，与当前实现对应。
- **G**：对象是源域与目标域的隐特征，操作是通过分布差异损失学习表征，与当前实现不同。

两篇不同论文出现 `alignment`，不等于提供了两个语义匹配的证据。共享名称的准入需要核对**完整名称、对象及操作**，不能按共同词根累计。F 可支持当前操作的解释，G 不能为“跨域特征对齐”这一命名背书。

保留实际操作，改用普通功能描述；不将其包装成未经验证的通用模块名或通行译名：

:::writing{variant="standard" id="56201"}
该步骤将时间戳相近的测量匹配为同一组。
:::

**new-author-name-without-precedent**
**Retain Stage-Conditioned Projection Unit (SCPU) in Methods** as an author-defined, project-specific component, with its implemented operation clearly stated. An approved new component name does not require earlier papers using the same name.

**Do not classify SCPU as an established mechanism in the shared bank.** Keep its definition in the project’s terminology map. The absence of an exact-name precedent does not establish methodological novelty; that requires comparison with related operations, including differently named ones. The supplied evidence also does not support claims of improved accuracy, effectiveness, or superiority.

A concise method sentence is:

:::writing{variant="standard" id="56202"}
In this work, the Stage-Conditioned Projection Unit (SCPU) uses a known stage indicator to select a learned projection, applies it to the measured-variable feature vector, and passes the projected features to the quality regressor.
:::
