# 工程应用顶刊术语库与慎用词表

## 使用边界

本文件服务于工业过程、控制、自动化、制造与装备类工程应用论文。本版提供[38 篇已发表文献索引](published-evidence.md)及[按场景选择术语的规则](terminology-decisions_CN.md)。旧版私有语料词频无法在公开包中复现，因此不再作为公开频次证据。不以作者草稿为术语权威；计算机 Channel Strategy 文献仅用于相关方法讨论，不作为通用工程词库的默认来源。未检索到不等于禁用。

## 一、概念引入顺序

首次介绍陌生工程背景时，可按依赖关系组织：`物理过程 -> 过程测量 -> 工程结构 -> 模型对应关系 -> 模型操作 -> 实验证据`。这不是每段的固定顺序；对应关系已经明确后，方法段可以直接从模型对象开始，不必重复物理背景。

先介绍 measured/manipulated process variables，再说明其工序、设备、采样率或控制作用；若模型将每个变量视为一个输入通道，随后再明确定义 `one process variable corresponds to one input channel`。不要在工程问题尚未说明时直接使用 channel、token、embedding 或 routing。

## 二、高频工程术语审计

术语审校不能只检查作者主动指出的词。获得全文术语审计授权后，提取重复实义词和 2--4 词搭配，再重点审计承担工程叙事功能的部分。三次可作为可调整的起点，不应遗漏仅出现一次但影响科学含义的词，也不需要机械检查所有常用词。单句语法修改不要求建立全文频次账本。

优先范围包括摘要、引言、相关工作、讨论和结论，以及方法和实验中连接下列概念的句子：工业对象与工况；过程变量、工序、设备、生产路线和拓扑；领域/工艺/专家知识；工序内、工序间和生产全流程关系；模型操作对应的工程含义；benchmark、real-world、online 和 deployment 等证据层级。

标准数学算子、激活函数、element-wise 运算、普通张量操作、方法名和数据集标签若不存在一致性问题，不必投入同等审校强度。

每个审计项至少记录：稿件及分章节频次、外部独立论文覆盖数、典型语境、保留/澄清/替换/仅限方法层/慎用结论、推荐表达和全文传播位置。必须检查固定搭配而非孤立单词；正确修改往往需要重构整句。例如 `information exchange` 可按真实模型操作改为 feature interaction、context aggregation 或 cross-stage feature fusion。fault propagation 是关于扰动在物理过程传播的另一种主张，不能作为神经特征交换的润色同义词。

覆盖数仅指实际检索范围，不代表整个领域；未检索写“未核查”，不能记为零。

## 三、通用工程对象

| 含义 | 推荐术语 | 慎用 |
|---|---|---|
| 全厂或全流程对象 | plant-wide process, plant-wide industrial process | global system |
| 实际制造流程 | production process, production line, production route | pipeline, workflow |
| 工艺划分 | process unit, production stage, sub-process, process block | module 指代实体设备 |
| 采集量 | process variables, process measurements, measured/manipulated variables | 未定义模型对应关系前使用 channels |
| 工况 | operating condition；有定义的离散工况可用 operating mode | 用 domain 指代普通工况 |
| 过程扰动 | process disturbance；实际事件为负载或设定值变化时具体命名 | 将扰动与背景工况视为同义 |
| 物理或工艺结构 | process topology, material flow, equipment connection, control interaction, stage relationship | process link |

## 四、划分、分组与聚类

固定工艺归属用 `partition variables by process unit/stage` 或 `process-informed partition`；按设备或功能构建块用 `divide the process into blocks`；学习得到离散归属可称 learned grouping 或 hard assignment，只有定义了聚类机制时才用 clustering。具有分级权重或隶属度时可用 soft grouping/soft assignment，定义了软聚类时可用 soft clustering；归一化权重不自动等于校准概率。合并工序特征用 aggregate/integrate 或 feature fusion，并说明合并对象。

不要用 `organize/organization` 包办所有操作。应根据实际机制选择 partition、group、cluster、aggregate 或 integrate。

## 五、特征操作

| 操作 | 推荐术语 |
|---|---|
| 从测量中获得特征 | feature extraction |
| 编码到特征空间 | feature representation; representation learning |
| 建模表征间关系，不自动等于物理影响或因果 | feature/variable/inter-stage interaction |
| 合并多个特征源 | feature fusion; feature integration |
| 加权求和或形成上下文 | feature/context aggregation |
| 沿图边传递或更新表征 | feature propagation; message passing；说明图和更新操作 |
| 扰动沿物理过程传播 | fault propagation；需有工艺知识或传播方向与影响的证据 |

优先说明具体操作，避免笼统的 `information exchange`；若确实描述已定义实体之间的通信或交换，该词可以成立。

## 六、多工序、知识与案例

多工序优先使用 stage-wise feature extraction、stage-specific measurements、inter-stage relationships、cross-stage feature fusion、process-topology-guided integration。spatial/spatio-temporal 要说明所指结构与时间轴，不限于物理空间：例如 P11 在卷积语境使用 spatial，但这种模型用法本身不证明变量间存在物理邻近或工艺关系。当前研究若仅建模变量关系，可直接写 inter-variable relationships，避免添加未经支持的空间解释。

stage-level 表示尺度，例如每工序一个池化向量；stage-structured 表示保留了按工序组织的结构，二者不能互换。生产工序、同一批次的时间阶段、训练阶段也不是同一对象。local/global 可以指时间感受野、变量邻域或全厂范围，必须先明确指代，不能因为别的论文使用就照搬。

工艺流程、设备关系和控制结构用 process knowledge/process topology；现场工程师提供的信息用 expert knowledge；混合来源可统称 domain knowledge。prior knowledge/prior matrix/structural bias 应说明信息来源、构建方式及其支持哪一步推断，不能把所有预设量都称为先验知识。

公开仿真或标准过程使用 benchmark case study；来自实际生产过程的数据通常使用 real-world industrial case study、real-world production data 或 actual production conditions。只有当离线/在线状态本身影响研究设计或结论边界时才使用 `offline`，不能把它作为所有真实产线数据的默认标签。顺序回放或流式算法本身不等于实际部署；online/prospective evaluation 应与真实实施方式一致。deployment 需实际接入运行流程，并区分建议、影子运行与影响生产动作的闭环使用。

类别不平衡属于数据属性而不是默认的论文卖点。若它影响训练或评价，应在数据集小节给出类别数量，在实验设置中说明权重/采样策略，在指标小节解释 macro、weighted 或 class-wise 指标，并在结果中分析受影响类别。除非类别不平衡本身就是核心科学问题或贡献，否则不在摘要、贡献、实验总览和结论中突出。

## 七、慎用词

| 词语 | 风险 | 推荐替代 |
|---|---|---|
| information exchange | 可能没说清交互、聚合、传播还是融合 | 选择实际操作；确为交换且有定义时可保留 |
| process link / known process link | 实体与关系未定义时含义不清 | inter-stage relationship, equipment connection, process topology；定义图后可用 directed edge |
| organization / organize | 容易掩盖真实操作 | partition, group, cluster, structure, aggregate, integrate |
| experimental protocol | 仅罗列设置时不必使用；真实定义评价程序时可以成立 | experimental settings 等，或保留确有定义的 protocol |
| stage representation | 对象定义后可以使用，工程动机中偏抽象 | 明确是池化工序向量还是变量特征，不为流畅而改变尺度 |
| dependency | 需符合所建模的依赖，不自动暗示因果 | 说明具体关系；correlation 也需要适当定义 |
| deployment | 需要实际运行接入，单有在线计算不够 | practical relevance, real-world industrial evaluation |
| token / embedding / routing / adapter | 容易压过工程对象 | 工程对象和模型对应关系明确后再使用 |

## 八、后续扩展

词库按四层扩展：通用工程层、具体问题层、方法层、单篇论文专用层。多速率、多工况、小样本、缺失数据、非平稳、复合故障等问题应分别建子表；图模型、特征融合、迁移学习、轻量化、扩散、模糊、多模态和大模型等方法也应分别建子表。单篇论文的术语对照表放在该论文项目中，不进入通用库。新增词条必须有外部已发表论文证据，不能用作者草稿为自身背书。

建议按以下类别建立外部证据充分的子库：

| 层级 | 示例类别 |
|---|---|
| 工程问题 | 多工序/生产全流程、多速率、多工况、非平稳、数据缺失、小样本/弱监督、复合故障、异常定位 |
| 工程任务 | 故障检测、故障诊断、过程监控、质量预测、寿命预测、控制、优化、决策支持 |
| 方法家族 | 特征融合、图建模、注意力、迁移/适应、轻量化、自/弱监督、扩散、模糊、多模态、大模型 |
| 证据类型 | 仅 benchmark、benchmark 加真实案例、背景驱动应用、在线/影子验证、实际部署 |

通用核心应保持稳定；专题词条必须同时说明其对应的工程问题，以及允许使用的方法与证据语境。
