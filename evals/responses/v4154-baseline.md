# Fictional Mass-Combination Baseline

One task context answered two requests on the immutable v4.1.53 release. Core calculations and writing already passed; the response correctly reported the absent scoped rule/Chinese admission record. This is an evidence-coverage gap, not a demonstrated scientific reasoning failure. Wrappers, local links and whitespace only are normalized; raw records remain private.

**A. 中文核查**

冲突系数为
\[
K=0.6(0.5)+0.1(0.2)=0.32,\qquad 1-K=0.68.
\]
非空交集的未归一化质量为
\[
q(A)=0.12+0.18+0.06=0.36,\quad
q(B)=0.05+0.03+0.15=0.23,\quad q(\Theta)=0.09.
\]
标准归一化 Dempster 合成将这些质量除以 \(0.68\)。等分剩余质量时，\(\operatorname{BetP}(A)=m(A)+m(\Theta)/2\)，B 同理。

| 质量函数 | \(m(A)\) | \(m(B)\) | \(m(\Theta)\) | BetP(A) | BetP(B) |
|---|---:|---:|---:|---:|---:|
| \(m_1\) | 0.600000 | 0.100000 | 0.300000 | 0.750000 | 0.250000 |
| \(m_2\) | 0.200000 | 0.500000 | 0.300000 | 0.350000 | 0.650000 |
| Dempster 合成 | 0.529412 | 0.338235 | 0.132353 | 0.595588 | 0.404412 |
| 质量算术平均 | 0.400000 | 0.300000 | 0.300000 | 0.550000 | 0.450000 |

算术平均与 Dempster 合成不同。信念质量不能直接等同于已校准类别概率；pignistic 转换本身也不证明经验校准。

当 \(m_1(A)=1,m_2(B)=1\) 时，\(K=1\)，标准归一化规则因分母为零而未定义。B 的契约规定此时弃判；添加 epsilon 会改变操作，不能冒充标准规则。

同一观测上学习两个头**不能证明证据来源独立**。不同参数或分别训练也不构成独立性证明，共享观测可能造成相关支持和重复计数。

**词库记录：**
- Dempster's rule **没有已完成的双来源准入记录，也没有单独登记的已核验中文措辞**，因此不存在可据该库报出的完整来源对。P49 的记录明确仅支持输入相关的特征加权组合，不验证严格 Dempster 合成。[P49 记录](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/e1875a4c3753866f2c6edf7afe4740c7f3da913d/references/published-evidence.md#L434)
- 实际相邻来源对是 **P52 pp.2–3 与 P75 p.3**，对应原文条目 **“evidential neural network / evidential deep learning (checked Dirichlet classification form)”**，不是 Dempster 规则。[英文条目](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/e1875a4c3753866f2c6edf7afe4740c7f3da913d/references/engineering-application-terminology-bank.md#L351)
- 中文记录实际为 **“evidential deep learning / 证据深度学习; subjective logic / 主观逻辑”**，来源为 *Journal of Image and Graphics*, jig.250475；其中还记录“信念质量”和“不确定性质量”。这些不能替代 Dempster 规则的中文核验。[中文条目](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/e1875a4c3753866f2c6edf7afe4740c7f3da913d/references/engineering-application-terminology-bank.md#L398)
- 未收录不代表术语无效；同一工作的预印本、期刊版和镜像不能计为不同工作。**“Calibrated Causal Dempster Reliability Block”不能凭基础条目自动准入**：完整名称及其限定含义需要各自匹配，基础词获准不证明校准、因果性或可靠性。[完整名称规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/e1875a4c3753866f2c6edf7afe4740c7f3da913d/references/engineering-application-terminology-bank.md#L19)

**A. English Sentence**
22 words.

We apply softmax to the weighting scores and sum the feature vectors using the resulting coefficients to obtain a combined feature representation.

**B. English Abstract**
122 words.

Fault classification from two aligned sensor streams of an industrial process requires combining class support while representing uncertainty and disagreement. We propose MassLink for classification within a known class set. Each stream's head produces nonnegative class evidence that parameterizes a Dirichlet model and yields singleton belief masses with residual mass on the class frame. A coefficient learned from each stream's encoded features discounts its singleton masses and transfers the remaining mass to the frame. The discounted mass functions are combined by the standard normalized Dempster rule when conflict is below one; total conflict triggers abstention. Pignistic probabilities from the combined masses determine the final class decision. Two held-out industrial-process cases show improved balanced accuracy relative to the same two heads evaluated separately.

**B. English Contribution**
35 words.

We propose MassLink, which discounts each stream's Dirichlet-derived belief masses using its encoded features, combines the discounted masses through normalized Dempster combination, and derives known-class fault decisions from pignistic probabilities, with total conflict triggering abstention.

**B. 作者说明**
词数按空白分词，连字符词和所有格各计一词。MassLink 保留为已批准的拟议英文名；不补造中文全称，新颖性比较仍待完成。

契约中的对应关系为 \(\alpha_c=e_c+1,\ S=\sum_c\alpha_c,\ b_c=e_c/S,\ u=C/S\)。折扣系数 \(r\in[0,1]\) 对应 \(b'_c=rb_c,\ m'(\Theta)=1-r+ru\)。这是学习权重的质量折扣，不是已验证的准确率校准；\(\Theta\) 表示已知类别全集，不增设未知类别。

两案例结论仅按虚构契约陈述，比较对象是同样两个分别评估的头。本文本未加入延迟、部署、跨厂、校准、因果、独立来源或未知类能力声明；未修改文件、联网或运行实验。
