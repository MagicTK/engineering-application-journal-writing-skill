# 摘要与贡献：以机制关系组织表达

[English](abstract-and-contribution-craft.md)

本指南不是固定句式。借鉴已发表论文时，应提炼工程需求、前后模块对象及验证结论之间的关系；不能认为已发表论文每句话都值得照搬。参照[公开文献证据索引](published-evidence.md)。

## 1. 先查机制

对重要操作记录输入及尺度、操作、输出、下一步使用者、公式/图/实现依据和未知项。软测量可以是测量值到状态估计再到质量预测；弱监督可以是实例特征到包聚合及包级目标。不要强迫每篇论文都有分组、门控或多分支。

仅在多工序融合研究中，核查池化后的工序向量是最终输出，还是会回到变量特征的中间上下文。独立编码不等于各自参数独立；保留特征的残差分支不一定就是融合模块。先验加到注意力得分上，不自动等于因果发现或硬掩码。

特征旁路关系重要时，应解释真实汇合操作，不从模块名倒推运算。P11/P15/P14给出加性残差路径，并在需要时匹配维度。已核实设计可正面写：The mapped input is added to the transformed features, which then supply the classifier. 另一设计可能拼接两路特征，仍保留作者批准的自提名称并解释实际操作。形状细节放方法，不因任一种汇合就宣称信息无损或泛化提高，也不把普通残差连接自动单列为独立贡献。

给操作标注作用阶段：预测时计算、训练目标、预训练，还是测试时适应。它们不一定是前向路径中依次串联的模块。对齐损失可以在训练中约束编码器，重构解码器可以在预测时移除。若这一点是核心，应说明“训练机制如何支持最终预测”，不能虚构顺序流水线。P10、P17、P21 展示不同的训练关联；P25 的训练分支与预测时采用的组件也有区别。

主动获取标注时，把样本选择原则、新取得的标注、据此更新的学习器和最终工程预测器连起来（P89-P91），不是在最终特征中融合标签与传感数据。贡献写有区别的选择原则，不把普通查询循环本身当新颖性；常规训练池分离保障和预算明细放设置或作者说明。成本主张的解释需要时保留模拟标注条件；相同标签预算下的结果不直接等于人工时间更少，或相同精度所需标签更少。

采用阈值处理特征时，把阈值输入、变换后的特征及后续用途连起来。已核实设计可以从编码测量生成阈值、收缩特征，再与旁路结合供分类；正面解释这条链，不声称阈值天然识别了哪些分量是噪声。P87/P88展示不同生成及汇合方式，不规定统一架构。贡献保留有区别的关系，普通阈值化本身不是新发明；含噪输入的分类改善也不是干净信号恢复误差。

修改后的网络副本也可能服务于训练。若实际设计用参数掩码副本提供对比视图，应把这种扰动连接到它训练的编码器，再连接到保留的预测器；解释有区别性的配对或学习规则，不把副本写成随后部署的压缩分类器。常规掩码比例和实现核查放在方法或作者意见。剪枝可以支持表征学习推进，不因此证明部署压缩；名称本身既不提供新颖性，也不等于实测收益。

**预备模型与运行决策，参见P85：**系统若选择已固定的模型变体，应把可用运行/网络状态、选择及最终工程决策连起来。接口相符时可写：A scheduler selects a prepared model using the current queue and link state. The selected model classifies the incoming measurements. 再补真正有区别性的选择原则或联合决策，不虚构在线权重更新链条。证据采用计算成本模型时，结果保留模拟范围，不改写成实测设备加速；单个变体的数量也不是整个常驻模型集合的内存。

若推进点在对齐，应明确对应的是样本时刻、维度、特征分布还是配对表征，以及采用何种判据；再连接到学得的预测器或后续计算，不能直接声称全部诊断信息已保留。方法句可以表达目标所鼓励的性质，结果句则需证据说明该性质或下游收益已获得。参见[对齐区别](terminology-decisions_CN.md#对齐明确对象和判据)，摘要只保留其中核心关系。

对保留的机制提取三项：**改变了哪个对象、进行了什么操作、改变后为何有助于下一步任务**。摘要保留有区别性的操作及用途，维度细节放在方法。变量特征、池化后的组特征和工序摘要不能都模糊成可随意互换的 feature，尤其当下一模块只接收其中一种时。

区分中间对象的变化与模型更新：门控或分组分配随当前输入重新计算，可以在训练参数固定时实现自适应，不必涉及在线参数学习。各节也应保留真实输出目标，不能把产品缺陷分类、质量估计和根因识别互换。[术语决策](terminology-decisions_CN.md)给出相应区别，不要求为此增加模块或实验。

## 2. 逐句检查职责与承接

按研究实际选用背景及关键属性、未解决能力、方法及目的、主要机制、最终表征/决策、验证认识等功能，不规定句数。对相邻两句问：读者已知什么，新增加什么，关系是顺序、并行、条件、因果还是证据？不能靠加 then 或 these features 补救缺失的逻辑。

内部机制核查应比替换稿更详细。正文选取理解推进所必需的关系，不把全部采样细节、组件清单和排除说明塞进同一个方法句。已交代清楚的条件，不必在句尾再用 with ... and ... 重述。次要实现事实可留在修改理由或相应章节，但避免误导所必需的信息访问条件不能省掉。对仅在训练中使用的辅助分支，通常正面说明预测时保留的路径，不另加一句罗列不执行哪些组件。“测试标签不用于调参”等常规保障放在实验设置，除非该信息边界正是研究主张的区别性条件；真正定义任务或消除歧义的排除与对照仍须保留。一句承担一个主要解释任务及其必要依赖，指代清楚的从句可以保留；不设单句词数上限，也不为追求短句拆散完整操作。

within each unit 与 across units 表示不同尺度时，句首结构相似不是语法错误；同一作用域不必反复交代。intra- 是内部，inter- 是之间。cross-stage fusion 与 inter-stage relationships 可以分别表达操作与关系，不必为形式统一机械替换。

一个指代清楚的从句，可能比连续两句重复主语更顺。根据独立信息和修饰层数决定是否拆句；First、then、finally 均为可选连接，不是模板必需品。

| 真实关系 | 应交代什么 | 常见误写 |
|---|---|---|
| 顺序变换 | 哪个输出成为下一步输入，新操作解决什么 | 前文有多个不同输出，却只写 these features |
| 并行互补 | 各路径保留/估计什么、在哪里汇合 | 用 then 暗示后一支由前一支产生 |
| 训练约束 | 何种监督作用于哪些参数或表征 | 把损失写成预测阶段的融合模块 |
| 更新控制 | 哪个事件触发学习变化，所需反馈何时可用 | 把更新触发写成采样控制或故障报警 |
| 知识引导计算 | 已知信息在哪个运算中起作用 | 实际只加得分偏置，却写知识与特征拼接 |
| 跨学习阶段适应 | 何时得到新信息、据此改变什么 | 将学习阶段与生产工序混为一谈 |
| 交替细化 | 拟合中哪两个对象相互更新，预测时保留什么 | 把双向训练循环写成两个无关模块或单向预测流水线 |
| 一个输出头、不同决策输出 | 哪个量用于类别估计，哪个量提供已定义的不确定性或拒绝决策 | 将证据、belief mass、类别概率互换，或只因报告不确定性就虚构拒绝机制 |

最后一句方法描述应从“做了什么”推进到“对任务形成什么”，例如兼顾局部测量与系统信息，或利用无标签数据形成质量预测所需表征。不要再列一遍模块，也不能把融合本身拔高为已经验证的泛化提升。清楚的短句优于含两个指代不明 which 的长句。

多头处理是核心时，连清输入对象、头输出及预测器，不将头数写成新增物理传感器或独立发现的关系。P11/P82区分合并后的头特征与注意力系数的单独用途，总览保留真实区别，摘要只选理解实际推进所需的关联。普通并行头本身不成为新贡献，其归一化也不是最终任务决策。

预测不确定性主张应连清估计量、区间与实际用途，不把概率模型和可靠性保证列成互不相关的点。针对接口已核实的合成设计，可写：Process measurements condition a distribution for the quality variable. Its interval bounds feed the declared warning rule, linking the estimated output range to the monitoring decision. 若无告警规则，就止于真实的质量估计或区间。贡献说明有区别的估计或区间构造如何产生可评价的输出，结果保留重要的覆盖率、宽度与工况差异；普通抽样数和核查排除项留在设置或作者说明。P103/P104提供不同的输出到用途关系，不要求将两种方法融合，也不把一个分布或近似写成已经证实的工程收益。

生成反事实输入时，把候选连到真实使用者。对接口已核实的增强设计，可写：Candidate inputs are adjusted toward the requested diagnostic class and checked by a fixed model. The accepted candidates augment real training data for the classifier that diagnoses new measurements. 模型解释设计则可能在预测时返回原始预测、改动后的输入及其模型响应（P62/P94用途不同），不能一律移除生成路径。贡献需说明有区别的生成或学习原则，普通类别引导本身不构成创新；结果保留重要类别权衡，不把模型内改动写成已验证的工艺动作。参见[按输出选择证据](experiment-evidence-design.md#counterfactual-outputs)，不将这些替代关系堆成固定模块清单。

## 3. 合成例子

已知设计：共享编码器产生各传感器特征，关系模块更新这些特征，分类器融合更新后与原始编码特征；没有跨域验证。

原表达：An encoder is designed. A relation module is introduced. A fusion module improves generalization.

可用的逻辑修复：A shared encoder first extracts features from individual sensor signals. A relation module uses these features to model dependencies between sensors. The classifier combines the updated features with the original encoder outputs, retaining both relational context and individual-sensor information.

修复建立输入输出关系、去掉未验证的泛化提升，但没有因此证明创新。真实论文仍需写出自身有依据的区别性机制，不直接复制此例。

另一组合成事实：软测量模型的质量预测器和重构解码器共享编码器；无标签测量参与重构训练，推理时仅用编码器和预测器。

可用表达：A shared encoder learns from labeled and unlabeled process measurements through prediction and reconstruction objectives. The quality predictor uses this representation to estimate the target from available process measurements.

无需虚构“先重构、再融合、再预测”的路径。两个例子均未自行提供创新或实验收益，必须加入原研究真实的区别性设计和证据。P03 的较短摘要也说明，机制与输出的关联不依赖固定字数。

**P36 展示另一种关联：** 各任务的门控将共享专家输出组合成对应质量目标所需的特征，梯度平衡则调节这些任务怎样训练共享参数。两种作用通过共同的多任务目标关联，不应写成融合特征在预测时又进入梯度平衡模块。这是训练关系，不必套用第一个例子的串行特征融合写法。

**P40 展示交替关联：** 标签表示引导特征筛选，筛选后的特征又改变下一轮标签更新所用的样本邻域。双向依赖各说明一次，再交代返回的特征子集。合成写法为：During fitting, label weights guide feature selection, while the selected features refine the sample neighborhoods used to update those weights. The resulting subset supplies the inputs to the diagnostic predictor. 只有这些接口与原方法相符时才采用；标签权重不自动是实测故障严重程度，筛选特征也不自动减少传感器。这种相互作用可以组织成一项关联贡献，但本身不证明收敛、创新或性能改善。

**P45-P46 展示教师指导的学习：** 说明传递对象及使用它的学习者，再关联训练后预测器与工程输出，不把训练损失写成师生特征的最终融合。针对已核实的回归设计，合成两句为：Teacher features and predictions guide the student during training. The trained student estimates product quality from the available process measurements. 真实论文应补充具有区别性的传递操作，此通用描述不是创新贡献。若预测还使用独立退出控制器或保留教师调用，应说明真实关系，不能归功于蒸馏本身。贡献可连接特定指导规则与其训练的学生能力，但仍需各自的创新和结果依据。

**P21 展示类别指导的表征学习：** 将估计类别信息与它在训练中指导的表征关系连接，不把时间模块和图模块列成互不相关的创新。对接口已核实设计的合成表达为：Temporal contrastive learning trains the encoder to associate contexts with later features across augmented views. Class estimates guide relationships between training samples, linking this representation objective to the diagnostic task. 预测时使用的编码器/分类器应在总览交代；只有为区分预测路径确有必要时才补入摘要。这里是训练关联，不是物理量预测或工艺拓扑学习。创新应在真实的耦合或目标构造及其证据，而不只是使用两种标准目标；其他对比设计仍需分别说明对象与配对依据。

**P13/P16展示关系建模到原因分析的承接：** 说明传给决策规则的对象，不只再列一个模块名。P13将学习图用于随后自上而下的节点评分，P16在检测后分析异常关系。摘要连清关系表征与实际排序或解释输出；贡献应交代有区别的“关系到决策”设计，不能把预测损失本身写成根因识别，或将同一图学习重复算两项推进。来源特有步骤保留归属，不为凑完整流水线而虚构分类器、物理干预或新贡献。

**节点更新到任务使用的承接：** 先连清表示对象，不只排列图相关名字。对接口已核实的分类器，可用两句合成表达：Neighbor-weighted updates combine features over expert-specified variable connections. Unit-wise means summarize the updated features, and the concatenated unit vectors supply the fault classifier. 按需补充真实编码器及有区别的权重设计，常规操作本身不构成贡献。P07的变量-时间节点与P13的生产单元层级不同；分别说明实际轴、固定/学习连接和输出层级，不借用完整层级或因果名字拔高摘要。

**门控贡献及其使用者：** 连清由什么决定门、门调节什么、调节后的贡献用在哪里。对接口已核实的双路径分类器，可写：Local and neighborhood features jointly determine a gate that scales the neighborhood contribution. Adding that contribution to the local features forms the classifier input. 其他设计可能门控专家或注意力输出，不强套这一路径。有区别的门控设计应连接真实任务证据，不把基础门本身单列为发明；残差旁路改变“抑制”的含义，稠密输入相关门也不等于稀疏执行或在线学习。除非影响正文保留主张的解释，这些核查意见放作者说明，不堆入摘要。

**源侧泛化学习，参见P50/P99：**连接训练操作及保留的诊断预测器，不虚构最终融合阶段。对接口已核实的虚构设计可写：Source-derived feature perturbations and a consistency objective jointly train the diagnostic representation. The trained encoder and classifier diagnose measurements from held-out operating conditions. 主张贡献前，将泛称目标替换为真正有区别的学习规则；不为串句新增目标拟合，不将不变性目标写成物理因果，也不将不同工况上的有升有降改写为总体收益。常规选择细节放设置或作者意见，除非它定义了所提推进。

**源模型迁移，参见P78/P79：**这是学习阶段之间的关系，不必是源/目标特征融合。连清工程访问限制、保留的源知识及用于训练目标预测器的指导。已核实设计可参照这一合成承接：A source-trained model initializes the target predictor. Target-derived class guidance then trains its representation from the available measurements, and the adapted model performs fault classification. 应把泛称guidance换成真实有区别性的选择规则或目标，必要时说明更新哪些组件。已有source-free条件可形成动机，但不使目标学习设计自动新颖。保留批次/数据流范围及观察到的类别权衡，不把审查排除条款填进摘要。

冻结骨干的预测也可与经目标信息调整的校正相结合。连清变化对象与校正后的预测/决策，分开先前校准和评价期更新；摘要保留有区别的适应原则，常规缓冲/优化器细节放方法，不再列成若干独立贡献。

**规则预测，参见P27/P77：**区分输入匹配、规则加权的数值输出及最终任务决策，不能只写高斯函数名而不说明下一步怎样使用。对已核实的回归设计，可直接表达为：Membership degrees determine rule weights, which combine local quality estimates into the final prediction. 再补本研究真正有区别性的学习或规则设计，不另列一串常规层。规则决策若在训练中指导编码器，应写受训表征及保留的预测器，不虚构最终特征融合模块。量的核对及解释边界放作者意见，正文保留受支持的任务意义及结果权衡。

**语义迁移，参见P05/P06/P80：**写清类别描述实际使什么成为可能，不将文本模型与传感模型并列罗列。语义匹配应由预测属性承接预给候选描述及故障名；特征生成应将描述条件生成器及训练约束接到生成特征、分类器拟合和保留的预测路径。合成承接为：Class descriptions condition feature generation. The synthesized unseen-class features train a classifier that diagnoses real process measurements. 再补本研究有区别性的约束或匹配规则，已有零样本设置及常规验证不单独成为推进。P80等设计保留训练组件的某些表征时应照实说明，不能默认全部丢弃。摘要保留真实候选集合和已见/未见表现权衡，不照搬完整资源账目或每类数量。

**证据合成：**将编码输出、真实组合对象及最终诊断决策连起来。特征加权结果送入分类器；明确的质量合成规则输出质量，还需按自己的决策规则使用。接口相符时可简写：Each stream supplies class-support masses. Their combination yields the support used for the final fault decision. 再补实际有区别性的权重或冲突处理，不笼统声称组合保证可靠性。后备处理不必每次进入摘要，但若它定义了所评价的输出，就应保留。按需查[合成与决策核查](terminology-decisions_CN.md#信念质量的合成与决策)。

**观测时间，参见P08/P24/P73：**将已采对象接到它实际提供输入的表征或估计器。摘要可由不同原生采样计划，引出利用现有测量或真实间隔的操作，再接质量量、图或报警。对已核实的间隔加权预测器，可写：Each stream is encoded at its native observation times. Measured intervals weight these representations before fusion for quality estimation. 再加入实际有区别的设计，不新造时间模块名。贡献可落在预测器怎样利用这些观测；用了中间观测不等于恢复全部未观测值。结果保留有据收益及仍存在的速率/间隔敏感性。

**训练损失加权：**将权重作用、受训学习器及工程决策连起来。接口相符时可写：Class-dependent weights scale the training errors of the temporal classifier. The fitted model assigns fault classes to new process measurements. 再补真实有区别性的权重规则，不把常规加权本身写成创新。训练系数不自动是预测时门控、特征融合模块或额外分数乘子。P93说明加权拟合，P92/P94则对增强前的选样加权，不能凭名称替代接口核对。结果落到实报指标及相关类别权衡；加权平均提高不单独证明稀有故障改善。权重和采样的详细运算放设置，不逐项塞进摘要。正文写保留的分类器如何预测，而不是在每句补排除条款。

若核实为特征加权的训练设计，应保留另一接口：Class counts from target pseudo-labels determine how target features are scaled before a nonlinear alignment mapping. The learned encoder supplies features to the fault classifier. 这指非线性对齐映射之前的特征操作；P98只为系数位置提供例子，不认证此合成映射是其具体核实现。再补真实有区别的规则及其与分类训练的关联，不虚构保留预测器中的门控。贡献需要具体推进及证据，而非weighted这个词；映射等价性检查放作者说明或方法。

同样的正面承接可用于已核实的训练logit调整，但须保留不同运算：Class-prior offsets modify the logits used to train the classifier. The trained network assigns fault classes to new process measurements. 再补真正有区别的偏置或更新规则，此功能描述本身不是新模块。P18分别调整训练logit和伪标签构造，P96则同时使用损失系数与间隔；应写清实际训练预测器的操作，不把所有不平衡策略写成特征融合或预测门控。来源冲突及分母核查放作者说明或方法，除非会改变摘要保留主张的解释。

**未来量预测与寿命估计：**先明确模型的保留输出，再写其收益。接口核实后可写：Encoded process histories supply a regression head that predicts the future temperature trajectory. 再补实际有区别性的运行信息使用方式，不罗列常规层。明确规则若将轨迹转为报警，要有相应事件和时序评价；P95将这些作用分开，P45/P81则使用寿命目标。寿命估计器不必预测每条传感轨迹，也不必增加故障分类器。标签截断或尺度若影响主张解释就保留，结尾落到实测预测/寿命结果和重要步长权衡，不把误差下降改成预警更早或维修成本下降。常规预测或回归本身不另算贡献。

若系数求导是核心且实现已核实，可直接连接训练作用：Joint differentiation through the probability-derived weights and classification loss trains the diagnostic encoder. The trained classifier diagnoses new measurements from this representation. 再补真正有区别的加权规则，普通乘法求导本身不构成新颖性；若实际停止因子梯度，则照实描述。常规计算图核查放方法或作者说明，不把另一个模块名或整套求导排除项塞进摘要。

有意扰动的诊断输入若用于训练，应连接该构造与保留的预测器，而非补造生成器/判别器或预测时攻击分支。对接口已核实的虚构设计可写：Bounded perturbations of labeled measurements train a temporal diagnostic model. Its trained encoder and classifier assign fault categories to incoming measurements. 再补真正有区别的构造，常规训练策略本身不自动成为贡献。坐标/预算细节一般放设置，除非它定义了推进；结果落到已测输入变化范围，不直接改成物理安全或全局鲁棒保证。这是功能写法，不准入完整防御机制名称。

**超边分组到诊断输出：** 先说明节点和超边的对象，再连接传播与真实预测。对已核实的变量节点设计，可写：An encoder supplies variable features. Node-to-hyperedge-to-node propagation combines them over expert-derived groups, and a graph-level summary supplies the fault classifier. 实际有区别的构造或学习设计才进入贡献，常规链条本身不是新颖性。固定归属、训练学习权重与依输入变化的特征可以同时存在；P96等样本节点设计须写自身的样本/批次接口，不能套工艺变量故事。归一化与访问细节按重要性放方法，不强造最终融合或物理因果意义。

## 4. 贡献写推进，不写工作日志

内部逐项记录最近前作已达到的能力、剩余需求、本次实际变化、能区分变化的证据和范围。不能未经充分检索就写唯一或首次。

可组织为总体原理加相互关联的机制，也可组织为问题建模、分析及方案，或必要工程适配及新的实证认识。没有固定三条要求。标准编码器为新分组机制提供输入时可以合写，第二句应说明联系，不能重新起一个不相干的贡献。

检查后项是否重复总框架，是否只是多列模块。普通两组案例通常属于验证；原创数据资源、部署能力或新的工程发现有依据时可以成为贡献，不能一概删除实验贡献。

对消融结论也作同样判断：若一项只说删去所提部件后任务指标变差，通常是设计贡献的支持证据，不是又一项推进。可接在设计项中，或移入验证总结。若实验回答独立提出的工程问题、建立新资源/能力，或获得超出“证明本设计有效”的有据发现，才可单列实证贡献。结果准确不等于可独立算贡献；一条充分支持的推进优于第二条重复其验证的条目。

总体框架项应有不被后续重复的组织原理或新能力；组件项再说明实现该原理的具体操作。两个操作共同完成一个推进时，可通过输入输出或共同目标合写。常规编码器不能仅因贡献列表需要平衡就单列为创新。

“句子接得顺”与“确实有创新”分别检查。P10、P17 各列两条，P06 组织三项关联推进，P08 包含问题分析，说明结构可灵活选择，并不提供数量模板。具体用[贡献路线](contribution-narratives.md)判断可主张的推进。

P38 将模型操作与新的跨模态 benchmark 资源分开。资源贡献应说明新增了什么数据、标注或评价能力，并核实范围和获取状态；它不同于“开展了实验”，数据规模与计划发布也不能单独证明创新或已经公开可用。

小样本贡献应连接具体机制与已声明的有限标签下学习/预测能力，问题设置本身不等于新机制。主张降低标注需求前，区分当前任务标签少与整个学习历史标签少；详细资源账目放实验设置，不逐项塞进摘要。[稀缺标签专题](topic-playbooks.md#2-scarce-labels-few-shot-zero-shot-weak-or-self-supervised-learning)保留合法基础数据学习、固定低数据训练及分任务训练等不同安排。

## 5. 实验收束

两个过程可以并列，两个数据集也可以并列，但不能混淆物理对象与数据集合。仿真基准与生产数据提供不同证据；real-world 不等于在线部署。offline 只有当区分评价方式确有意义时才需出现。

先核对研究输出再决定结句：生成保真度、质量预测误差与故障分类准确率不是同一结果。生成研究可以收束到生成质量及实测下游用途（P32），增强诊断的研究则收束到实际诊断评价（P35）。若生产测量中叠加人工故障，不能把全部测试故障都写成产线真实事件。摘要只保留避免误导所需的区别，详细构造在方法与实验中展开。

effectiveness 需要任务证据。engineering applicability 应说明适用对象及已验证范围：有工程依据的仿真可以支持所建模条件下的相关性或可行性，实际产线适用性则需要来自该场景且具有代表性的证据，两者都不自动证明已经部署。generalization 先明确目标总体：独立且无泄漏的留出样本可评价同一总体的新样本预测，跨工况、站点或时间范围迁移则需对应的留出证据。verified 和 demonstrated 都可以用于经验性验证，均不能替代证明或部署验证。

结尾一句可以同时交代案例及支持的结论；第二句应增加实际发现、权衡、评价条件或实质工程意义，不再说明做过实验或换句话重复同一指标收益。前句若已报告组合优于匹配的单路径对照，再说“这些比较支持组合的好处”通常没有新增信息；保留真正推进解释的句子，不以重复验证结论凑字数。两个物理过程可以直接并列为 case studies on process A and process B，不必为了形式把其中一个改成 dataset。其他研究也不必套两组案例。

修正夸大的结句时，正文直接写实际评价层级支持的发现，不要在句尾又把删除的主张以“尚未证明”带回摘要。例如调整后与原始检测分数的反向结果本身就是有效信息；为何删去无依据预警主张，可放在作者说明中。若边界会改变读者对保留结论的理解，例如计分规则或允许访问的目标数据，则摘要仍须保留。这里区分信息位置，不禁用负结果或必要限定。

类别不平衡、所有故障类别和硬件细节不必机械放进摘要；若它们正是研究问题或影响结论解释，则可以保留，否则在数据分析、指标及实现设置展开。实验数字是否出现由证据、作者和期刊要求决定，不设通用禁令。

## 6. 同步含义，不要求全文同句

引言核查缺口是否支撑机制；贡献核查推进与职责；动机/问题核查输入、标签和假设；总览与模块首尾核查顺序、串并联与输出去向；图和公式核查尺度、维度、箭头；实验核查新增作用是否确已评价；讨论/结论核查证据强度。

摘要改写不意味着所有章节都要改。保留正确句，科学疑点与可选润色分开。交付使用[摘要正文同步表](../assets/templates/abstract-body-sync.md)。字数约 200 词可以是作者目标，不是质量门槛；清楚完整且不过度重复，比凑字数重要。
