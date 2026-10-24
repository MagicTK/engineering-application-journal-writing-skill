# 4.1.14 Fresh-Context Response

One responding context; five fictional requests. The response is retained below. Only two local Skill-reference link targets were normalized to portable relative links; substantive text and writing blocks are unchanged. The exact dispatch and response remain in the maintainer's private record.

已读取指定入口及相关中英文指导，**Skill 版本为 4.1.14**。以下仅依据题设和 Skill 现有公开来源记录；未编辑文件、运行实验或新增文献检索。

**A**
:::writing{variant="standard" id="74101"}
A shared encoder processes the zero-filled measurement tensor together with its observation mask and is trained using available quality labels and a decoder's reconstruction loss on observed measurements. At inference, only the encoder and quality predictor are retained, and the predictor maps the learned representation to a quality estimate.
:::

中文理由：这是对计算路径的事实纠正。零值是占位符，解码器通过训练目标约束共享编码器，并不先补全测量再供预测器使用。缺少质量标签的样本仍可利用已观测测量参与重构训练；这里不主张未经验证的恢复或预测性能。

**B**
:::writing{variant="standard" id="74102"}
The proposed imputation scheme preserves observed measurements by construction and fills only unobserved positions with model estimates, producing a completed input for downstream classification.
:::

**两者可以讨论，但依据不同。** 观测值不变由合成式保证：当 \(M=1\) 时，\(x_{\mathrm{complete}}=x_{\mathrm{input}}\)。测试时人为隐藏的条目应在输入掩码中标为未观测，其参考值仅用于评分。

题设的独立生产运行留出、训练侧固定预处理与模型选择，以及隐藏条目参考值，支持评价**该 10% 随机遮蔽设置下的插补误差**；报告时需明确评分条目、分母和数值尺度。它不验证自然缺失值的恢复准确性，也不能直接外推至连续停测、其他缺失比例或其他工况。观测位置的训练重构损失不能替代这项测试；分类收益也需要独立的下游评价。尚未给出误差结果，因此不能宣称插补准确或优于其他方法。

**C**
原句不成立。计算如下：

| 指标 | Run A | Run B |
|---|---:|---:|
| 原定义 \(L=\mathrm{SSE}/N_{\mathrm{sequences}}\) | \(10/10=1\) | \(2/10=0.2\) |
| 每个评分条目的 MSE | \(10/100=0.10\) | \(2/10=0.20\) |

\(L\) 降至原来的五分之一，不等于准确率提高五倍。条目级 MSE 虽然变大，但评分对象不同，也不能据此认定缺失率导致精度下降。

英文替换：
> The sequence-normalized reconstruction loss decreased from 1.0 to 0.2, whereas the mean squared error per scored entry was 0.10 in run A and 0.20 in run B. Because the scored entries differ, these results do not establish improved reconstruction accuracy with increasing missingness.

最小交接：保留现有 SSE、计分条目数及 \(L\)，补列条目级 MSE，并同步修正相关正文和图注中的“五倍改善”。若保留缺失率影响的比较主张，需另行安排同一留出总体、共同隐藏评分条目、受控输入缺失设置的比较；本轮不执行重跑。

**D**
:::writing{variant="standard" id="74103"}
At each timestamp, the model estimates a latent process state using the likelihood of the sensor measurements available under the multirate sampling pattern. A separate quality equation maps this estimated state to a concentration estimate.
:::

中文建议：**不必要求缺失值重构测试。** 该方法没有定义补全测量输出，目标是利用可用测量估计状态，再预测浓度。浓度预测有效性的证据应来自独立留出数据上的浓度参考值，并明确采样模式、预测时的信息边界及对照方法的信息条件。结论限定于已测试采样模式下的浓度预测，不扩大为缺失值恢复能力；无需为此新增解码器或插补环节。

**E**
依据当前 Skill 的[名称准入规则](../../references/engineering-application-terminology-bank_CN.md)及[已核验记录](../../references/engineering-application-terminology-bank_CN.md)：

- **missing-value imputation：可以作为限定语义下的通用推荐名称。** 英文依据为 P25 的 PDF p.4、第 3.1 节，以及 P33 的 p.5、第 IV-B 节、式(13)–(15)，共同涉及估计未观测值。中文“**缺失值插补**”已有[《自动化学报》c230534](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c230534?viewType=HTML)双语题名及摘要的核验记录。数值占位、潜在表征对齐不自动属于插补；这组记录也不证明流程工业中的普遍使用程度。

- **reconstruction loss：可以作为限定语义下的通用推荐名称。** 英文依据为 P17 的 PDF pp.4–5、式(6)、(14)，以及 P33 的 p.6、式(18)。中文“**重构损失**”已有[《工程科学与技术》2022，54(5):240–248](https://scuaes.ijournals.cn/html/2022/5/202100675.html)双语摘要及对应关键词的核验记录。具体目标、掩码、范数和分母仍须逐文定义；名称本身不保证推理时执行插补，也不证明未知测量恢复准确。

- **Masked Quality Recovery Gate：按题设属于单篇来源专名，不能据此列为通用推荐名称。** 介绍该来源时可保留名称并明确归属；基础词 `gate` 的通用性不能替整个组合名称完成准入。这不是判定该名称错误。

- **作者真正提出的新模块不必因缺少两篇同名先例而删除。** 可以保留为“本文提出”的名称，说明实际操作、输入输出及使用边界，并以相应证据支持效果。双来源要求约束的是共享术语库的通用推荐，不是新模块的命名资格；数据库未列出也不等于术语无效。

上述中文依据均复用 Skill 已保存的核验记录，本轮未重新联网核查。
