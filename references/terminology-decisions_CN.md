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

P05、P06 的 attributes 用于零样本故障语义，P20 用于图节点属性。这些合法用法不妨碍物理测量优先用 variables。动词 attribute 与此不是一回事。

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

## 结构与操作

- intra-stage 是工序内，inter-stage 是工序间，cross-stage 是跨工序。`inter-stage relationships` 与 `cross-stage fusion` 可以在一个摘要中并存，不必强制统一所有前缀，更不能颠倒 intra/inter。
- stage-wise 表示逐工序处理，stage-level 表示粒度，stage-structured 表示保留了已定义的工序结构，三者不互换。
- partition 可来自固定工艺划分；grouping 可预设或学习；clustering 需要实际聚类机制；软分组不一定输出硬簇。
- aggregation 对集合汇总；fusion 结合信息来源；interaction 建模相互作用。需对照操作选择，不靠“高级词”替换。
- relationship 范围较宽；dependency 不自动表示因果；correlation 需要相应统计量或合理定义。
- topology、prior、constraint 分别核查工程来源和数学作用；加性注意力偏置不是硬约束，也不自动是因果图。
- spatial / spatiotemporal 需定义物理、拓扑或图关系以及时间轴，张量列顺序不构成时空结构。
- gate 调节贡献，attention 计算关系或加权聚合，fusion module 结合路径。核查形状与操作，不混淆分支和融合模块。
- unified / global / plant-wide 需说明表示范围，融合两条路径不证明普适泛化或完整全厂覆盖。

## 分方向加载

- **多速率：** 区分采样率、间隔、异步与缺失，重复静态值不产生时间信号。参考 P08、P23-P26。
- **有限监督：** few-shot 说明有标签样本数；zero-shot 说明未见类别与可用语义；semi-supervised 区分有无标签数据；weak supervision 可能是包级或粗标签；self-supervision 解释目标生成。参考 P05-P06、P17-P22。
- **模糊：** 隶属度不自动等于校准概率；规则、隶属函数与聚合要有定义。证据不确定性也不是同一对象。参考 P07。
- **知识引导：** 区分专家规则、拓扑、物理定律与学习相似性，来源与进入模型的方式比形容词重要。参考 P04、P12-P14。
- **质量相关诊断：** 解释质量目标与过程行为的关系；不在摘要和实验总览中反复罗列缺陷。参考 P09、P16。

## 评价与边界

real-world 表示来源，不表示在线运行。不要习惯性加 offline；若回顾性与前瞻性评价区别影响结论，则应保留。类别不平衡通常在数据和指标分析中展开；只有它确实是研究问题或贡献时，才需要出现在摘要或贡献中。

普通实验章节可以用 experimental settings；若确实定义了可复现的评价程序，evaluation protocol 也不是错误。作者不喜欢某词，不应上升为整个领域禁令。

真正不可接受的是虚构结果和引用、编造输入语义、无依据的因果/部署/泛化结论及隐瞒选择泄漏。没有哪个普通单词本身足以证明这些问题。
