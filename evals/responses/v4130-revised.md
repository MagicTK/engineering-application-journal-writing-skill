# Fictional Few-Shot And Annotation-Budget Response

Actual response; counts, implementations and observations are fictional. Private local links and terminal blank lines are normalized.

已使用现行技能 v4.1.30。仅额外读取通用技能启动说明，未访问任务记忆、历史、评测、私有研究记录或原论文；未联网、修改文件或执行实验。

**M4130-A**
英文总览为78词，按空格计数；贡献仅作候选表述，不预设创新性。

:::writing{variant="document" id="41301"}
### Method Overview
The classifier learns an encoder and a matching function from 2,000 independently annotated base samples through supervised training episodes. The learned encoder maps support and query windows into a shared feature space, where the matching function relates each query to the labeled support examples. At evaluation, each task comprises four new classes with two labeled support windows per class. These support examples establish the current matching task, and the trained model predicts the classes of separate unlabeled queries.

### Contribution Draft
We connect supervised base-data learning to four-way, two-shot classification through a learned encoder and matching function that use the current task's labeled support windows to classify queries from new classes.
:::

中文核查：
- **原始当前支持标注：**4×2＝8个独立标注窗口。
- **另生成增强视图：**8×24＝192个；若原窗口也保留，则原始窗口与新增视图合计200个输入实例，仍只有8个原始支持标注。
- “整个模型仅需8个人工标注”不成立：基础学习使用2000个独立标注样本，单个当前任务另有8个支持标注。
- “192个增强视图就是192个新标注”不成立：它们派生自已有支持窗口，不是新增独立人工标注。
- “基础训练query有标签就是测试泄漏”不成立：训练query可用基础样本标签形成监督；关键是独立测试query的标签不进入学习、匹配或调参。
- **2-shot的准确范围：**已有基础监督学习之后，每个测试任务对4个新类别各提供2个支持窗口，仅用于当前匹配，不用于参数训练；不代表全部学习历史只使用8个标注。

**M4130-B**
:::writing{variant="document" id="41302"}
### Method Overview
We study wind turbine classification with eight independently annotated training windows for each of four known classes. The network extracts sequence and spectrogram features from each window and combines them using learned weights to classify windows from independent test runs.

### Contribution Draft
We investigate learned fusion of sequence and spectrogram features from the same window for wind turbine classification under a fixed budget of eight labeled training windows per class.
:::

中文判断：
- 学生的绝对判断不成立。可明确写为**固定训练标注预算下的few-shot classification**，或采用更直接的“classification with limited labeled data”；不必为此改做元学习或新类别评价。
- 设置为4×8＝**32个独立标注训练窗口**，派生为**总计320个训练视图**，不是新增320个标注，也不是352个视图；先按独立运行划分，再仅增强训练集。
- 两路特征来自同一窗口，是不同表示，不是独立传感器。该设置不支持通用数量阈值、普遍优越性、新类别适应或实际产线部署；贡献草稿也未宣称这些结果。

**M4130-C**
标注数量减少比例为 **(320−32)/320×100%＝90%**，即少288个独立人工标注训练窗口。

:::writing{variant="document" id="41303"}
Compared with the baseline's 320 independently annotated training windows, our method uses 32, a 90% reduction in training annotation count, with both models trained from scratch and evaluated on the same independent test set.
:::

**作者建议：**保留“训练标注数量减少90%”，待效果数值补齐后讨论性能取舍，不将其改写为“精度相同”或“总体人力成本下降90%”。

术语判断：
- **few-shot learning基础名称：可以支持。**现行词库以P47的“基础学习＋有限支持样本”和P69的“固定少量标注＋增强视图”提供两个不同工程语境，支持有限样本设置，而非统一算法、类别划分或数量门槛。[词库记录](../../references/engineering-application-terminology-bank.md)
- **完整SSFN特有融合模块名：不能因此升格为通用家族。**基础名称的证据不自动覆盖完整复合模块名；单篇定义可保留归属，不能据此宣称通用。
- **作者真正新提出并定义的模块：不必先有两篇同名论文。**应明确其为本研究提出的组件，交代操作与边界；多源门槛针对通用类别的入库，不是禁止新命名。[命名规则](../../references/engineering-application-terminology-bank.md)
- **中文来源角色：**按现行指南已有核查记录，《航空学报》（DOI：10.7527/S1000-6893.2019.23756）与《软件学报》（006958）的双语题名、摘要等支持“小样本学习”的译名；它们不是工程定义的第三、第四篇。本轮未打开原文或在线复核。[中文核查记录](../../references/engineering-application-terminology-bank.md)
