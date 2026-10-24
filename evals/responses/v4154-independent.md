# Fictional Mass-Combination Final Response

One fresh task context answered the same two requests on the frozen final source; only the read root changed. The earlier response already passed core science and writing. The new record changes maintained evidence availability, not a demonstrated general writing gain. Wrappers, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

**A：中文核查**
标准规则先计算交集乘积，再以 \(1-K\) 归一化：

\[
K=0.6(0.5)+0.1(0.2)=0.32.
\]
\[
q(A)=0.12+0.18+0.06=0.36,\quad
q(B)=0.05+0.03+0.15=0.23,\quad q(\Theta)=0.09.
\]

因此 \(m(X)=q(X)/0.68\)，且 \(m(\varnothing)=0\)。Pignistic 转换为 \(\operatorname{BetP}(c)=m(\{c\})+m(\Theta)/2\)。

| 操作 | \(m(A)\) | \(m(B)\) | \(m(\Theta)\) | BetP(A) | BetP(B) |
|---|---:|---:|---:|---:|---:|
| Dempster 合成 | 36/68 ≈ 0.529412 | 23/68 ≈ 0.338235 | 9/68 ≈ 0.132353 | 81/136 ≈ 0.595588 | 55/136 ≈ 0.404412 |
| 质量算术平均 | 0.400000 | 0.300000 | 0.300000 | 0.550000 | 0.450000 |

两个输入各自的 pignistic 概率分别为 \((0.75,0.25)\) 和 \((0.35,0.65)\)。质量平均不是 Dempster 合成；信念质量也不是已校准类别概率，pignistic 转换本身同样不证明经验校准。

当 \(m_1(A)=1,m_2(B)=1\) 时，\(K=1\)，标准归一化规则无定义。B 的约定对此返回弃权；分母加 epsilon 会改变运算。在同一观测上训练两个头，也不能证明证据来源独立。

**当前库记录**
[术语库第340行](../../references/engineering-application-terminology-bank.md)已有基础完整名称 **Dempster's rule of combination (normalized conjunctive rule)** 的配对记录：

- **P49**，*SREFNet: A Spectral Residual-Based Evidence Fusion Network for Industrial Fault Diagnosis*，DOI `10.1061/AJRUA6.RUENG-2063`：PDF p.3，式(6)–(7)。
- **P84**，*Robust fault diagnosis of a high-voltage circuit breaker via an ensemble echo state network with evidence fusion*，DOI `10.1007/s40747-023-01025-3`：PDF p.8，式(8)–(11)。

这是两篇不同作品中匹配的**理论定义**，不是两个未经修改的规则实现。P49 pp.5–6 的实际网络运算是特征加权求和；P84 完整 IDS-ESN 设计仍保留来源归属。

[中文记录第399行](../../references/engineering-application-terminology-bank.md)分别记载：北京邮电大学学报 DOI `10.13190/j.jbupt.2018-094` 的双语摘要、关键词及第1节定义1、式(1)–(2)，支持 **Dempster合成规则**；自动化学报 `c190676` 的双语摘要及表3，支持 **Dempster组合规则**。后者未记为完整方法正文核验。这些是库内既有记录，本轮未联网复核，也未把预印本另计为第二篇作品。

**Calibrated Causal Dempster Reliability Block 没有完成整名准入记录，不能由基础规则自动获得准入。**附加限定需要对应定义和证据；未收录不等于名称无效。

**A：English Method**
计数按空白分词，连字符词计一词；下同。**23 words**。

The method normalizes weighting scores across feature vectors using softmax and forms a fused representation by summing the vectors with the resulting weights.

**B：English Abstract**
**125 words**。

Fault classification from two aligned sensor streams of an industrial process requires combining class support while retaining uncommitted evidence. We propose MassLink, which represents each stream's nonnegative class evidence as a unit-prior Dirichlet opinion with singleton belief masses and residual mass over the known class set. A coefficient learned from the corresponding stream's encoded features discounts singleton masses, transferring the removed support to the full class set. The discounted masses enter the standard normalized Dempster rule when conflict is below one, with declared abstention at total conflict. A pignistic transformation distributes the combined residual mass equally among known classes, yielding probabilities for the final class decision. Across two held-out industrial-process cases, MassLink improves balanced accuracy relative to each of the same two heads evaluated separately.

**B：English Contribution**
**34 words**。

We propose MassLink for industrial fault classification, linking stream-specific evidence discounting to normalized Dempster combination and pignistic decisions, with total-conflict abstention and improved balanced accuracy over its separately evaluated heads in two held-out cases.

**B：作者专用说明**
- 保留批准的英文拟名 **MassLink**；不补造中文全称，创新性比较仍待完成。
- 操作对应为 \(\alpha_c=e_c+1,\ S=\sum_c\alpha_c,\ b_c=e_c/S,\ u=C/S\)。折扣系数 \(r\in[0,1]\) 给出 \(\tilde b_c=rb_c,\ \tilde m(\Theta)=1-r+ru\)；合成后以 \(\operatorname{BetP}(c)=m(\{c\})+m(\Theta)/C\) 作决策。
- 学习折扣不代表准确率校准；全冲突弃权不代表未知类识别。结果仅采用题设两案例及相同双头比较，不扩展到其他未经测试的能力。实际稿件还需说明弃权样本如何计入 balanced accuracy。
