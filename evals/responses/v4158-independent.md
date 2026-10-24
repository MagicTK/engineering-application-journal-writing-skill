# Fictional Annotation-Acquisition Final Response

One fresh task context answered the same two requests on the frozen final source; only the read root changed. The earlier response already passed core science and writing. The new record changes maintained evidence availability, not a demonstrated general writing gain. Wrappers, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

**A. 信息角色**
不能把“query labels”当作统一禁用类别。当前 v4.1.58 的[实际规则](../../skills/engineering-experiment-evidence-design/SKILL.md)明确限定为：**保留作最终评价的标签不能参与模型选择**，训练查询监督与授权获取的训练标签应另行判断。

| 安排 | 信息角色与判断 | 能说明及不能说明的内容 |
|---|---|---|
| 1 | 从授权训练池获取外部真实标签，再监督拟合预测器，属于池式主动学习；题设没有最终评价标签泄漏。 | 建立“选样→获取标注→扩大标注集→重拟合”的学习路径；本身不证明性能提升、新颖性或人工节省。对无标签池评分也不自动构成半监督训练目标。 |
| 2 | 开发／训练episode中的query标签提供监督损失，是合法训练监督，不是最终评价query标签。 | 说明训练信号的用途；不自动证明未见类别、独立shot或全流程标注成本低。 |
| 3 | 用最终评价query标签选择嵌入宽度，属于超参数选择中的评价标签泄漏。 | 这些标签已经影响模型选择，该评价不能再支持独立最终评估的解释。 |
| 4 | 选择工厂物理激励以区分故障假设，属于题设指定的激励式主动诊断，不是请求样本标注。 | 说明实验输入的选择目的；不证明已经实现因果识别、现场效益或标注节省。 |

**标签计数：新增30个，累计获取12＋30＝42个。** 缓存后重复训练五个epoch不会增加独立标注数，不能报成新增150个或累计210个。这42个是外部真值；模型生成的伪标签等目标须另列，不能混入真实标注获取数。

benchmark oracle揭示已有标注，可以模拟获取过程、评价规定标签预算下的学习表现；**没有测量真实专家工时、标注难度或实际人工节省**。

以下三个英文成稿均按正文空白分词计数，连字符连接项计一词，标题不计。

方法句：**33词**
The selector requests true labels for samples chosen from the authorized unlabeled training pool, adds those samples to the labeled set, and refits the diagnostic predictor while independent final evaluation labels remain sealed.

**实际维护依据**
以下报告的是本轮读到的[套件阅读记录](../../references/published-evidence.md)，不是本轮联网重读原论文的结果；不以题名或转引替代操作定义。

- **P89**：TCST，2023，DOI `10.1109/TCST.2022.3200214`。记录阅读并目视检查PDF pp.1、3；p.3第II-B节连接无标签池选样、请求专家标签、获取预算和分类器更新。
- **P90**：Chemometrics and Intelligent Laboratory Systems，2023，DOI `10.1016/j.chemolab.2023.104821`。记录阅读并目视检查PDF pp.1、4–5；第3.1节、图4及表1定义化工过程分类中的选择、外部标注与分类器重拟合循环。
- **P91**：TASE，2024，DOI `10.1109/TASE.2023.3325271`。记录阅读并目视检查PDF pp.1、4；p.4第II-B节连接查询取得的专家标签与复合故障分类器重训。

因此，**P89＋P90构成两篇不同发表作品的基础操作配对，P91提供第三篇作品**。P89/P91共享作者及研究脉络，不能包装成三次独立发明。该记录支持“为学习选择性获取标注”的基础操作，不认证全部MCAL/DGMR/E-ECos名称、统一选择准则、预算单位、预测器架构、人工节省或现场部署。

中文完整基础对应 **active learning／主动学习** 有[单独维护记录](../../references/engineering-application-terminology-bank_CN.md)：
- 《软件学报》2024，35(3):1125–1139，原始双语摘要，记录号7073：多模态训练中的选择性标注语境。
- 《系统仿真学报》2021，33(6):1350–1357，原始双语题名及摘要，记录号20-0093／页面2630：软测量中的选择性标注语境。

这两项核验基础用词与角色，不是完整方法审查，不增加英文工业定义作品数，也不认证所有复合译名或成本主张。

**Expert-Causal Class-Preserving Query Module**缺少获批操作定义，应保持待定，不能靠拼入已核基础词获得准入。反过来，[名称规则](../../references/engineering-application-terminology-bank.md)允许作者批准且定义明确的新提名；未入库不等于无效。

**B. 英文成稿**
摘要：**121词**
QueryBudgetFD addresses known-class industrial fault classification when acquired labels are limited. A small labeled seed initializes a shared encoder-classifier. At each round, classifier uncertainty and feature-space coverage jointly score the remaining authorized unlabeled training pool. Selected samples receive oracle-provided true labels, leave the pool, and enlarge the labeled set used to refit the encoder-classifier. Acquisition proceeds within a predeclared query budget. The resulting encoder-classifier assigns known fault classes to new process measurements without consulting the oracle. Evaluation covers a simulated process benchmark and a held-out recorded-production case; annotation is simulated by revealing existing labels for selected training samples. With identical initial labeled seeds and equal numbers of newly acquired labels, QueryBudgetFD achieves higher weighted F1 than random acquisition in both cases.

候选贡献：**39词**
QueryBudgetFD links joint uncertainty and feature-space coverage scoring to training-label acquisition and encoder-classifier refitting, yielding a retained known-class predictor with higher weighted F1 than random acquisition at matched initial labeled seeds and newly acquired label counts in both cases.

**作者备注**
- 保留作者批准的英文名QueryBudgetFD，不擅定中文名。新颖性比较尚未完成，候选贡献不等于已确立创新。
- 两个案例的比较结果仅来自题设，不是本轮实测；没有具体分数、重复运行或显著性证据，故不补写。
- 所有选择均未使用最终评价标签；不引入伪标签、新类发现、强化策略或物理激励。
- 等初始标注、等新增标签数下weighted F1较高，不等于等F1所需标签更少；真实人工时间、跨厂迁移、因果识别和在线部署均未测量。
