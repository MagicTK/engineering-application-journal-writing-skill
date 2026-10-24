# Fictional Soft-Sensor And Quality-Task Response

Actual response; implementations and timing facts are fictional. Private local links and terminal blank lines are normalized.

访问范围限于现行技能及相关参考、通用启动指引和只读额度查询。系统预置历史摘要未用作依据；未检索记忆或历史文件，未联网、读取原论文、修改文件或运行实验。

**M4131-A**
:::writing{variant="document" id="41311"}
Method Overview

The soft sensor estimates the current process concentration q(t), in mg/L, at time t using temperature and pressure windows available up to t and a released historical concentration measurement. An encoder represents the process windows, and its output is concatenated with the latest released concentration value and passed to a regressor. Laboratory results are released 60 minutes after their corresponding process times. Model fitting uses subsequently obtained laboratory values as targets for historical training samples; independent test estimates are evaluated against their corresponding laboratory values only after prediction.

Contribution Candidate

A soft-sensing approach combines encoded temperature and pressure windows with the latest released historical concentration measurement to estimate the current process concentration.
:::

中文核查：方法总览 **88 词**，按空白分词，`q(t)`、`mg/L`各计一词，不含标题和贡献候选。任务为 **T5 当前浓度估计**。

- **“目标量永远不能作为模型输入”：错误。** 同一物理量的已发布历史观测可以输入；不能据此输入尚未获得的当前目标值。
- **“旧时间戳就证明化验已可用”：错误。** 必须比较发布时间。`q(t−120 min)`在`t−60 min`发布，已可用；`q(t−15 min)`要到`t+45 min`才发布，不可用。题设未说明采样间隔，因此不能认定前者就是“最近一次”。
- **“这是60分钟未来浓度预报”：错误。** 输出对应`t`，预测时距为零；60分钟是化验发布延迟。
- **“训练用后来化验的历史目标就是泄漏”：错误。** 历史训练样本可用后来取得的化验值作监督目标；泄漏取决于是否把预测时不可得的信息用于该次预测，或把独立测试目标用于拟合、选择或调参。

**M4131-B**
:::writing{variant="document" id="41312"}
Method Overview

A process feature encoder is trained through a regression task to learn representations for product quality prediction. The final deployment candidate uses only these learned process features to assign products to one of three quality categories.

Contribution Candidate

A quality-category prediction approach uses process representations learned through regression to classify products into three quality categories.
:::

中文核查：

- **主任务路由为T3。** 最终输出是三个质量类别之一；回归是特征学习阶段的任务，不使最终候选自动变成T5，也不应把最终目标和评价指标全改成连续量。
- **不路由为T4。** 类别预测没有输出责任变量、定位结果或根因解释，不能据分类结果宣称找到了致缺陷原因。
- **标题不必强制改名。** 可保留`quality prediction`，在摘要和任务定义中明确其类别输出；内部路由码不要求重命名标题。没有控制动作，也不补写闭环能力。依据：[现行任务路由规则](../../references/industrial-ai-taxonomy.md)。

**M4131-C**
:::writing{variant="document" id="41313"}
Method Overview

At time t, the model forecasts the process concentration q(t + 120 min) using process measurement windows available up to t and historical concentration measurements already released by t. Training and test samples are separated chronologically, and forecasts for the independent test period are evaluated against laboratory measurements obtained later.

Contribution Candidate

A quality-forecasting approach combines available process measurements with released concentration history to estimate process concentration 120 minutes ahead.
:::

中文核查：这是明确的 **120分钟ahead预报**，可并用 **T5＋T6**：前者标识连续质量量预测，后者标识未来目标。未来化验值后来仅用于评分，且不进入当前输入或调参，不能仅因标签后来获得就判泄漏。

术语依据与核验边界：

- **确切用例与语义等价须分开。** 按[现行词库英文记录](../../references/engineering-application-terminology-bank.md)，P34第1页、P57第1–2页明确使用soft-sensing名称；P57的§2.1、式(1)涉及由过程测量及目标历史估计关键变量。P56第1–2页使用inferential-sensor名称，对应质量间接估计任务，因此是相对于soft sensing的**限定语义等价依据**，不是soft-sensing的另一字面命中。三项记录不证明所有virtual-sensing同义词或完整模型名称均已获准。
- **中文支持有明确范围。** [词库中文记录](../../references/engineering-application-terminology-bank.md)列有《自动化学报》c210035的双语标题，以及《信息与控制》2020.9311的双语标题和摘要，支持soft-sensor modeling与“软测量／软测量建模”的对应。本轮只读取该记录，未联网复核原页面。
- **不能扩张为primary/secondary中文定义已核验。** 当前术语决策将其解释为待估目标与输入测量的角色，而非重要性排序或第一、第二个实体传感器；这不是其中文标准译名的核验。可直接写“待估浓度”“可获得过程测量”，无需生造直译。

以上三条贡献均为题设所支持的表述候选，不代表已证明新颖性、性能收益或产线部署。
