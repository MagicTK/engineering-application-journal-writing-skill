# Actual candidate response

Only local link prefixes are normalized to repository-relative links. Response wording and formatting are preserved; self-reported word counts are not evaluation findings.

**A. Abstract And Class Vector**
:::writing{variant="standard" id="82461"}
For few-shot industrial classification, we average the embeddings of labeled support samples within each class to construct a class prototype. An MLP compares each query embedding with these prototypes to produce class scores, using query labels to supervise the training loss while predicting held-out queries without their labels.
:::

*49 words, counting hyphenated terms as one.*

The author should state:

- **Construction:** \(p_c=|S_c|^{-1}\sum_{x\in S_c}f_\theta(x)\), where \(S_c\) contains labeled support samples of class \(c\). Specify the embedding dimension, support count, and when prototypes are recomputed.
- **Parameter status:** Here, the prototype is a support-derived mean, not a separately optimized free parameter. If the encoder is trained, its changing embeddings can change the mean; that does not make the averaging rule learned.
- **Role and information access:** Each prototype represents a class in feature space and supplies the MLP’s query comparison. Support labels determine class membership; training-query labels supervise the loss. Held-out query labels must not enter prototype construction or prediction.
- **Meaning:** “Class prototype” accurately describes this defined representative. “Physical operating-state” requires an independently justified connection to physical states that the supplied specification does not establish.
- **Novelty:** Do not claim all constituents as newly proposed. Identify reused or adapted components and their sources, then explain any substantiated methodological difference. Trainability, naming, and combination alone do not establish novelty.

These statements describe **this construction**, not a rule that every prototype must be a mean or that every class must have exactly one prototype.

**B. Terminology And Translation**
**The full name is unsuitable as an established shared-library recommendation on the supplied evidence.**

Semantically, softmax normalization establishes nonnegative weights summing to one. It does not, by itself, establish fuzzy memberships, calibrated probabilities of physical modes, or correspondence between four reference vectors and four operating regimes. The absence of mode labels does not prohibit unsupervised mode discovery, but such an interpretation still needs evidence.

Bibliographically, one introducing paper supports an **attributed paper-specific name**. Three papers using only “gate” do not establish the complete compound or its qualifiers. Shared admission requires at least two distinct relevant published journal works defining the full name, or verified semantic equivalents, for matching objects and operations; three to five are preferable for ambiguous terms. Multiple versions of one work count once. Definitions and equations matter, not titles or citation mentions.

**Precise description:**

:::writing{variant="standard" id="82462"}
For each variable embedding, the model computes softmax-normalized weights over four learned reference vectors and uses their weighted sum to update that embedding.
:::

This describes the computation without inventing a replacement mechanism name. The manuscript must additionally define the score calculation and how the weighted sum enters the update; addition, concatenation, and replacement are not interchangeable.

**Independent Chinese evidence** would come from a terminology authority, standard, or reliable Chinese scholarly source explicitly connecting the complete English term to Chinese wording and a matching definition. Record the URL and inspected passage or section. Evidence for “gate” alone does not verify the compound. Machine translation, search snippets, and repeated blog wording are insufficient; competing translations warrant a second independent Chinese source. Translation verification and English-category admission remain separate. Without verification, retain the English identity with a descriptive Chinese explanation rather than claiming a standard translation. No external translation verification is claimed here.

**C. 作者建议**
可以保留“dual-reference scoring”作为本文明确定义的组件名称，无须先找到两篇使用完全相同名称的论文。共享术语库的准入条件不等于作者命名的前置条件，但仍须引用相关工作并说明实际差异。这里每类有两个经反向传播优化的自由参考向量，并非支持集均值，也不具有已验证的物理含义；强制改成每类一个均值会改变方法，而非纠正措辞。应明确向量维度、初始化、评分与聚合公式及训练和预测时的使用方式。名称、操作及结果的创新性均须另行论证；若需证明两个参考向量的必要性，应提供相应证据，不能预设优势。

:::writing{variant="standard" id="82463"}
The dual-reference scoring component learns two free reference vectors for each fault class through backpropagation. For each query embedding, it computes a score against each reference vector and aggregates the two scores within each class to obtain the class score.
:::

Guidance: [prototype distinctions](../../references/terminology-decisions.md) and [name-admission boundaries](../../references/engineering-application-terminology-bank.md).
