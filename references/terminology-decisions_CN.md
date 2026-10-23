# 按语义和场景选择术语

与[通用术语库](engineering-application-terminology-bank_CN.md)配合使用，不是机械替换词典。来源编号对应[已发表文献索引](published-evidence.md)。文献有用例只能说明这个词可以成立，不能证明它符合当前方法。作者偏好留在具体论文的术语表中。

## 决策顺序

1. 确定对象：物理量、观测、样本、隐特征、工况、状态，还是计算操作。
2. 核对上下句、定义、公式及输出去向，不能仅凭模块名推断功能。
3. 搜索相近工程任务中的具体搭配；排除参考文献标题，并辨别名词与动词。
4. 区分：正确、需定义、作者偏好、含义不清、科学含义不符、证据不足。
5. 必要时给出原句、位置、局部改句和理由，不做全篇自动替换。

没有搜到只表示“在本次检索语料中未发现”，不等于禁止使用。词频不证明科学正确性。配套脚本只产生待核查候选。

## 数据对象

| 术语 | 适用对象 | 必须区分 |
|---|---|---|
| process variable / measured variable | 温度、压力、流量等测量或控制量 | 隐空间特征不等于物理变量 |
| quality variable | 产品或过程质量的测量目标 | 类别标签不一定是连续质量量 |
| feature / feature representation | 输入描述量或编码后的特征 | 改进特征不等于改变测量变量 |
| channel | 已说明与变量、信号对应关系的模型轴 | 不默认所有模型一变量一通道 |
| sample | 窗口、钢板、批次、周期等学习或评价单位 | 数据库一行不一定是一个独立样本 |
| observation / measurement | 一个观测值、向量或观测事件 | 观测单位与样本单位可能不同 |
| record | 真正的数据库、日志记录或关联对象 | 不用来随意替代训练样本 |
| attribute | 故障语义属性、图节点属性、元数据字段 | 不作为过程测量变量的默认名称 |

训练和测试数量通常写 `training samples`、`test samples`。只有真实存在训练与模型选择的数据池时才写并解释 `development set`，不能用改名暗示做过验证集实验。将 records 改成 samples 前先确认二者是否同一单位。

P05、P06 和 P29 的 attributes 用于零样本故障语义，P20 用于图节点属性；P29 明确区分结构化故障描述、传感器测量及其文本化表示。这些合法用法不妨碍物理测量优先用 variables。动词 attribute 与此不是一回事。

## 状态、工况与模式

| 术语 | 合理含义 | 核查问题 |
|---|---|---|
| operating condition(s) | 负荷、设定值、速度、原料等运行条件 | 是否确实指可辨识的工况，而非隐向量？ |
| operating mode | 定义明确的离散运行模式 | 模式划分、标签从哪里来？ |
| operating state / operational state | 过程、系统或局部单元当前的运行表现或状态 | 是物理状态、推断状态还是编码？ |
| process state | 物理、监测或数学定义的过程状态 | 上下文是否给出明确对象？ |
| latent state / hidden state | 内部数学表示 | 是否误写成已验证的物理状态？ |
| prototype | 真正存在的代表向量、样例或中心 | 模型是否有原型机制？ |

P04 有 process state 的实际用例；P16 有 operational state；P10 研究 operating conditions。这不是常见程度排名。不能只为流畅把 state 换成 condition：连续变化的局部特征并不自动构成离散工况。`local operational state` 需要与真实的局部自适应机制相符，也不等于已识别物理状态。没有原型机制，不引入 `prototype state`。

学习得到的模糊状态（P07）、离散运行模式与状态空间中的物理状态各有定义，不能因为都有 state 就互换。process disturbance 是扰动过程行为的输入或事件，也不等于获取测量时的背景工况。

## 变量及其特征

| 表达 | 语义边界 |
|---|---|
| variable-wise encoding / features | 按变量分别组织的编码或特征；说明输出对象 |
| independently encoded variable features | 独立编码路径的输出；核对独立性的具体范围 |
| individual-variable features | 较中性的各变量特征描述 |
| variable-specific features | 强调各变量特有的内容，不等于独立编码 |
| variable-specific behavior | 变量之间存在不同表现；有时写清对扰动的不同响应更准确 |
| local variable features | 对某工序、单元、邻域而言的局部特征，不自动等于独立分支输出 |

不能将 specific 全部改成 wise：前者偏内容特有性，后者偏组织或计算方式。当前语料不能为表中每个完整搭配提供直接用例；这些是语义判断，最终仍要服从方法和作者已确认的术语。

`feature selection` 保留已定义描述量的子集，`feature extraction` 构造描述量，`sensor selection` 才涉及需要哪些物理测量。P40 返回所选特征的索引；保留的若干频谱或统计特征仍可能需要全部原始传感器及预处理。先说明减少的是哪种对象，再判断能否主张减少传感器、采集成本或推理时间。

## 标签对象

| 术语或对象 | 需要确定的含义 |
|---|---|
| missing annotation | 未知目标不等于已确认阴性；说明整条样本还是某些标签缺失 |
| candidate-label set | 多个可能目标；说明可能同时有几个为真、是否保证包含真实目标 |
| multilabel target | 同一样本可真实对应多个标签；多个正项本身不是标注歧义 |
| partial label space | 某分类器负责的局部标签集合，如 P39；不能从词面推断标注不完整 |
| label enhancement / soft training target | 人为构造的数值表示，应交代来源及学习作用；不自动是纠正后的观测、概率或实测严重程度 |
| noisy label / noisy measurement | 标注/目标有误与输入观测被扰动不同；确认受影响对象及评价所用参考 |

P39-P40 是相邻机械领域的用例，不代表流程工业监督形式统一。P40 的邻域生成标签值属于学习对象；要解释为物理严重程度，还需与损伤、强度或明确严重程度目标建立独立依据。定义合理的论文专用术语不必全局改名，也不能仅凭题目判断全领域用法。

## 结构与操作

- intra-stage 是工序内，inter-stage 是工序间，cross-stage 是跨工序。`inter-stage relationships` 与 `cross-stage fusion` 可以在一个摘要中并存，不必强制统一所有前缀，更不能颠倒 intra/inter。
- stage-wise 表示逐工序处理，stage-level 表示粒度，stage-structured 表示保留了已定义的工序结构，三者不互换。
- partition 可来自固定工艺划分；grouping 可预设或学习；clustering 需要实际聚类机制；软分组不一定输出硬簇。
- aggregation 对集合汇总；fusion 结合信息来源；interaction 建模相互作用。需对照操作选择，不靠“高级词”替换。
- relationship 范围较宽；dependency 不自动表示因果；correlation 需要相应统计量或合理定义。
- topology、prior、constraint 分别核查工程来源和数学作用；加性注意力偏置不是硬约束，也不自动是因果图。
- causal convolution 表示特定输出不读取未来输入；预测依赖表示信息对预测有用。二者本身均不识别物理干预效应或根因，不能只因出现 causal 就混同。
- spatial / spatiotemporal 应定义所指轴或关系：物理位置、工艺拓扑、图邻域或明确建模的变量间结构；时空表述还需说明时间轴。模型网格相邻不自动等于物理接近或工艺耦合。
- gate 调节贡献，attention 计算关系或加权聚合，fusion module 结合路径。核查形状与操作，不混淆分支和融合模块。
- unified / global / plant-wide 需说明表示范围，融合两条路径不证明普适泛化或完整全厂覆盖。

stage 先区分生产单元、一个批次中的时间阶段与学习阶段；local/global 先确认局部性的定义域，时间感受野不等于全厂区域；propagation 区分图上特征更新与真实扰动的传播。这些选择会改变科学含义，不只是风格问题。

mask、sparse、constraint 需核查作用位置：注意力边为零、logit 置零、类别被排除、专家不执行是不同结果。有限 logit 置零后仍可获得正的 softmax 概率；普通稠密 softmax 也不证明稀疏执行。同理，块对角图限制的是该次图运算，不一定限制后续特征混合，更不证明物理单元独立。摘要中的作用应落在完整计算实际支持的层面。

## 分方向加载

- **多速率：** 区分采样率、间隔、异步与缺失，重复静态值不产生时间信号。参考 P08、P23-P26。
- **有限监督：** few-shot 说明有标签样本数；zero-shot 说明未见类别与可用语义；semi-supervised 区分有无标签数据；weak supervision 可能是包级或粗标签；self-supervision 解释目标生成。参考 P05-P06、P17-P22。
- **模糊：** 隶属度不自动等于校准概率；定义实际的隶属函数与聚合，模糊聚类层不一定具有语言规则。证据不确定性也不是同一对象。参考 P07、P27-P29、P33。
- **知识引导：** 区分专家规则、拓扑、物理定律与学习相似性，来源与进入模型的方式比形容词重要。参考 P04、P12-P14。
- **质量相关诊断：** 解释质量目标与过程行为的关系；不在摘要和实验总览中反复罗列缺陷。参考 P09、P16。

| 分方向术语 | 必须保留的含义 | 修改前核查 |
|---|---|---|
| conditional drift / concept drift | 某个明确分布的变化，不是统一的漂移定义 | `P(X)`、`P(Y)`、`P(X|Y)`、`P(Y|X)` 哪个改变、哪个保持？P30 使用特定的类条件分布定义。 |
| event-triggered learning / sampling / alarm | 分别是学习更新、采集事件或诊断输出 | 什么触发什么，所需测量或标签当时是否可用？P27 讨论学习更新。 |
| generation condition / operating condition | 生成条件可为故障类别或健康指标，运行工况则描述运行条件 | 先看条件变量，不把所有 conditional generation 都改写为工况条件生成。参考 P32。 |
| diffusion step / acquisition time | 模型加噪去噪迭代与实际测量时间 | 不默认扩散步代表物理时间演化，也不默认去除实际传感器噪声。参考 P32、P35。 |
| reservoir state / process state | 循环模型内部状态与有定义的过程状态 | P28 的 reservoir 是计算对象，不是物理储罐。 |
| slow feature / quality-related feature | 时间变化速度与目标相关性是两个性质 | 什么目标函数或方程建立了与质量的关联？参考 P34。 |
| efficiency / real time | 某种资源比较与满足决策时限 | 区分训练、生成、预测成本及计时范围；参数少不证明时延低。 |
| task balancing / load balancing | 任务训练影响与工作负载/专家使用的分配 | P36 平衡任务梯度，不因此证明稀疏路由或设备负载平衡。 |
| cross-modal alignment / synchronization | 学习的表征兼容性与采集时刻的配对 | P38 区分同步采集、token 构造与跨模态注意力；特征维度相等不证明时间已配对。 |
| local outside-class / unknown fault | 子分类器标签集之外与整个系统未知 | P37 的成对子分类器 OOD 类本身不构成系统级新故障检测。 |

## 评价与边界

real-world 表示来源，不表示在线运行。不要习惯性加 offline；若回顾性与前瞻性评价区别影响结论，则应保留。类别不平衡通常在数据和指标分析中展开；只有它确实是研究问题或贡献时，才需要出现在摘要或贡献中。

offline assay 可以准确表示实验室检测或迟到的质量标签，不等于给所有工业数据加 offline 前缀。online 可以指顺序计算，也可以指现场在线评价，必须说清；deployment 需要运行接入，影子评价不能证明闭环收益。

任务名称也需看定义。detection 可能指报警，diagnosis 可能识别类别、位置或原因；文献用法有差异（P02），先看目标与评价再改名。quality prediction 可能输出连续量，也可能预测质量类别（P09），不能为了表面统一把类别标签改成连续质量变量。

连续监测中，window-level、pointwise、point-adjusted、event-level 对应不同评价对象或计分规则。阳性窗口不定位窗口内的异常时刻；命中一次后填满真实异常区间只改变评分，不改变实际报警时间，P07 与 P22 的选择不同。inference time 描述明确范围内的计算耗时；detection delay 需要对齐真实报警、参考起点以及所需信息的可用时刻。early warning 还需要定义提前预警目标，计算快不能代替这些时序证据。按需阅读[连续监测评价](experiment-evidence-design.md#continuous-monitoring-what-is-scored-and-when)。

普通实验章节可以用 experimental settings；若确实定义了可复现的评价程序，evaluation protocol 也不是错误。作者不喜欢某词，不应上升为整个领域禁令。

真正不可接受的是虚构结果和引用、编造输入语义、无依据的因果/部署/泛化结论及隐瞒选择泄漏。没有哪个普通单词本身足以证明这些问题。
