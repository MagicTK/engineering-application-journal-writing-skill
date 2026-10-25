# Batch-Phase Writing: One Fresh Context

Fictional input only; one initial answer and one same-context wording feedback. Local paths, display wrappers and private quota information are normalized; scientific content is preserved.

## Request

请只读使用 the current suite 的中文入口和必要参考，完成下面的虚构工程论文请求。不读取evals、其他项目、真实论文或网络；不修改文件，不运行科研训练或提出替代模型。可做简单只读算术。最后简要披露实际阅读的文件及范围。

作者先要把问题讲清楚，再按已经确认的实现撰写。以下是虚构输入，不对应任何真实论文：同一反应器分批生产，每个生产批次依次经历投料、反应、冷却三个操作时段，并非三个空间设备。实际总时长在80至130分钟之间，反应结束由运行中的事件触发，不是事先已知的固定时刻。不同批次的时段边界也不同。每分钟采集12个过程变量；每批结束后只化验一次最终产品浓度，没有运行中的浓度测量。数据共有40个生产批次，前28个用于模型开发，后12个按批完全留出评价，各种预处理、超参数与模型选择均未访问这12批。所有批次均超过30分钟。

任务一只整理问题，不推荐算法或新实验：给简洁的中英文问题表述与需要区分的对象。学生说“把每批变成许多窗口后就不再少样本；投料、反应、冷却是三个physical production units；把最终浓度复制到每个训练时刻就是实测浓度轨迹；都填充到130分钟就消除了时段不对齐”，请根据实际含义逐项判断，不只给禁用词。

任务二现在允许按已实现的模型写作，不允许换方案。模型只在各批开始后的第30分钟发出一次最终浓度预测，输入只含从开始到30分钟已经取得的测量和截至此时已经发生的操作事件。既定时段规则根据这些事件确定当前可见历史的分段；未发生的时段没有特征，不填入其未来测量。一个共享时间编码器编码可见历史，各已观测时段分别均值汇总；按事件顺序拼接这些表示，缺席位置使用声明的掩码，回归头输出一个最终浓度估计。当前研究不诊断故障、不改变控制器、不估计逐时浓度。训练时，可以用开发批次已测得的最终浓度作为这个30分钟输入的监督目标。预测时不输入当前批的实际最终浓度、实际总时长或未来事件。阶段分段与输入的可用时间已实现核对，不需重新发明网路。

12个留出批次上，采用同一30分钟信息边界的完整模型MAE为0.80 g/L，去掉分段、只对同一编码器输出全时域均值汇总的对照为1.10 g/L；数据划分与选择权限相同。只做了这项时间边界和这两个模型的比较，没有质量干预实验、部署或统计显著性结论。另一张附图采用完整轨迹和批次结束后才知道的实际总时长进行时间归一化，用于事后解释各批的时段位置，不进入模型预测、选择或指标计算。这个图是否必须删除？另有同学想把归一化时间t除以实际总时长作为30分钟预测的附加输入，认为它不涉及标签所以可以；这个建议尚未实现，也没有进入上述结果，请给一条核对意见，不擅自否定已确认结果。

请给约160—185词英文摘要、一个不超过70词的方法总览段、一条不超过40词的贡献候选句，以及一个不超过65词的Results/Discussion段。摘要说明困难、时间边界、编码到时段汇总再到最终目标的关联，保持积极清晰，不逐项堆砌内部审查声明。贡献不要把常规拼接称为首创，创新性比较未完成的提醒放作者注。Results可以报告指标但不得把最终浓度预测准确度写成成品质量已提升。用中文分别说明图和建议输入的判断、训练监督与预测输入的区别。不要为达到字数补造第二案例、真实部署、浓度轨迹标签或通用模块名。

## Initial Answer

**任务一：问题界定**
中文：同一反应器的生产批次依次经历投料、反应和冷却，但批次总时长为80–130分钟，操作时段边界随批次变化，反应结束由运行事件触发。每分钟记录12个过程变量，每批仅在结束后获得一次最终浓度化验值。问题是在批次级监督有限、运行进度不一致的条件下，依据预测时已经获得的过程信息，提前估计该批最终产品浓度。

English: A single reactor processes batches through feeding, reaction, and cooling. Batch durations range from 80 to 130 minutes, with varying stage boundaries and event-triggered reaction completion. Twelve process variables are recorded every minute, but concentration is assayed only once after each batch. The problem is to predict final product concentration from information already available during operation, with limited batch-level supervision and differing process progression.

需要区分的对象是：**反应器设备、生产批次、批内操作时段、采样点或窗口、实测终值，以及预测发出时刻**。40批对应40个实测终值；前28批用于开发，后12批完整留出。生产批次也不同于训练中的小批量。

| 学生说法 | 按实际含义判断 |
|---|---|
| “变成许多窗口后就不再少样本” | 不成立。窗口增加了输入片段数量，没有增加独立生产批次数或实测终值数量；同批窗口共享过程历史和监督来源。应分别报告窗口数、批次数和标签数。 |
| “三个 physical production units” | 对象错置。这里是同一设备内顺序发生的三个**操作时段**，可定义为 operating stages/phases；不是三个空间设备或生产单元。 |
| “复制最终浓度就是实测浓度轨迹” | 不成立。复制可以表达多个输入对应同一最终目标的监督关系，却没有产生任何运行中浓度测量。本实现只将30分钟输入与该批终值配对。 |
| “填充到130分钟消除了时段不对齐” | 不成立。填充统一的是数组长度，不是工艺进度或事件边界；同一分钟仍可能对应不同操作时段，填充值也不是过程测量。 |

**任务二：英文稿**
以下按已确认实现撰写。按空格计词，连字符词计为一词。

**Abstract · 174 words**

Predicting final product concentration during batch operation is difficult when durations vary, stage boundaries shift, and concentration is measured only after completion. We study batches processed in a single reactor through feeding, reaction, and cooling, with durations of 80-130 minutes and event-triggered reaction completion. The model issues one prediction at minute 30 using only measurements of 12 process variables and operation events available from batch start through that minute. A shared temporal encoder represents the observed history. Predefined event rules identify observed stage portions, within which encoded features are averaged to retain stage membership for final concentration prediction. These representations are concatenated in event order, with absent stages masked, and passed to a regression head. Model development uses 28 batches with final concentration assays as supervision. On 12 subsequent batches held out from development, the model achieves an MAE of 0.80 g/L, compared with 1.10 g/L for global mean aggregation using the same encoder and 30-minute input boundary. This comparison supports retaining observed stage structure for final concentration prediction at the specified information boundary.

**Method Overview · 61 words**

At minute 30, predefined rules use observed operation events to partition the available history. A shared temporal encoder maps the 12-variable measurements to time-indexed features. Features are averaged within each observed stage portion, concatenated in event order with absent-stage positions masked, and passed to a regression head that estimates final concentration. Training pairs each development input with its batch's final assay.

**Contribution Candidate · 29 words**

We retain observed operating-stage structure in minute-30 final concentration prediction through event-defined mean aggregation of shared temporal features, with a matched comparison supporting its value under limited batch-level supervision.

**Results/Discussion · 58 words**

At the 30-minute cutoff, the complete model achieved an MAE of 0.80 g/L on 12 held-out batches, versus 1.10 g/L for global mean aggregation, a reduction of 0.30 g/L (27.3%). Under matched information and development conditions, this supports stage-separated aggregation for the evaluated prediction task. The evidence concerns final concentration estimation, not demonstrated improvements in manufactured product quality.

**边界判断**
- **事后附图：不必删除。** 完整轨迹和实际总时长可以用于事后解释。图注应明确归一化采用批次结束后已知的总时长，图仅展示时段位置，不参与预测、选择或评分。统一归一化时间轴也不保证各批时段边界重合，不能将该图呈现为第30分钟已经掌握的全过程信息。
- **建议输入的一条核对意见：** 第30分钟的 `30/T实际` 依赖当时未知的实际总时长，因此不符合本任务的信息边界；“不含标签”不足以证明输入可用。这项建议尚未实现，**不能据此否定已确认的0.80和1.10 g/L结果**。
- **训练监督与预测输入：** 已完成开发批次的最终化验值可以监督其30分钟输入，这是学习“早期历史到最终结果”的映射，不是提供运行中浓度标签。预测当前批次时，只使用截至30分钟已取得的测量和事件；当前批终值、实际总时长及未来事件均不输入。留出批次终值仅用于评分。

**作者注：** 创新性比较尚未完成，上述贡献只是候选表述，不把共享编码器、均值汇总或常规拼接单独宣称为首创。证据限于这一预测时点和两个模型的比较，不支持故障诊断、逐时浓度估计、控制改进、部署或统计显著性主张。

**阅读披露**
实际读取、检索均限于指定目录：
- [中文总入口](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)：全文142行；[中文摘要与贡献入口](../../skills-zh/engineering-abstract-contributions-zh/SKILL.md)：全文53行。
- [问题优先分类](../../references/problem-first-classification_CN.md)：提取1–195行，返回有截断；采用其中批次、时段、计数与质量目标相关段。
- [术语裁定](../../references/terminology-decisions_CN.md)：标题及关键词检索，读取1–75、221–240行。
- [摘要与贡献写法](../../references/abstract-and-contribution-craft_CN.md)：全文82行。
- [论证与文字精修](../../references/argument-and-prose-craft.md)：标题及关键词检索，读取55–104行。
- [实验证据指南](../../references/experiment-evidence-design.md)：标题检索，读取77–102行的划分与时间边界规则。

未读取evals、记忆文件、其他项目、真实论文或网络；未修改文件、训练或更换模型。仅作词数与误差降幅计算及只读额度检查。

## Wording Feedback

首答的对象、训练监督、预测输入与证据判断均已核对。仅复核Results/Discussion最后一句的写作：目前用not demonstrated作结略显防御性。请保留准确指标及比较边界，把该段收束到比较所支持的正面工程含义；不新增干预、部署、显著性或其他结果。只返回修订的Results/Discussion段，仍不超过65词，不改摘要、贡献、事实或Skill。无需读取更多文件。这是同一上下文的一次措辞反馈，不是新的独立测试。

## Revised Results/Discussion

At the 30-minute cutoff, the complete model achieved an MAE of 0.80 g/L on 12 held-out batches, versus 1.10 g/L for global mean aggregation, a reduction of 0.30 g/L (27.3%). Under matched information and development conditions, this comparison supports retaining observed stage structure to improve early estimates of final product concentration in the evaluated batches.
