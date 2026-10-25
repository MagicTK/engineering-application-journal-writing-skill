# Fictional Problem-Only Baseline

One response context answered A/B on immutable v4.1.76. Its science already passes; no controlled general gain is inferred. Only wrappers, private path/link metadata and whitespace are normalized; raw/dispatch remain private. Runtime lookups are disclosed.

说明：两例均为虚构记录。额外的运行定向仅包括额度检查及通用技能入口读取，不作案例证据；未联网复核译名。

**A．问题分类与用词**
- **问题轴C**：Missing Data对应 **missing process measurements／过程测量缺失**，本例由两次停机造成；Multi-Rate对应 **multi-rate observations／多速率观测**。但须核实“每小时”指取样还是结果生成周期。报告晚到另记 **assay reporting delay／化验报告延迟**，不等于过程时滞；跨流时间戳不重合也不自动构成不规则采样。这些属于C1。
- **监督不足C2**：可称 **scarce batch-quality labels／批次质量标签稀缺**。约30批中8批有连续终检质量值，其余约22批仅缺质量目标，并非没有过程数据，更不等于正常、阴性或质量为零。批次标签数与测量点、窗口数分开报告；目前无标签错误的证据。
- **运行变化**：暂写 **long-term operating variation／长期运行变化**。离散工况、连续漂移及两者共存尚待辨明；未明确哪个分布改变，不能统称concept drift。
- **任务轴T**：Anomaly Localization是“异常定位”任务线索，不是本研究既定输出。只有明确估计连续质量量，才归质量预测/软测量；A尚未指定最终任务。
- **尺度轴O与来源**：Plant-Wide Process是全厂/全流程尺度线索，须确认跨工序系统边界；批次是样本粒度。TSMC是发表来源缩写，具体分刊待核。
- **方法轴M**：Graph、Fuzzy分别是图建模、模糊方法线索；Weakly/Self/Unsupervised Learning是学习策略线索。文件夹不代表已经采用，M轴留空。

**B．监督信息与训练信号**
**设计1**：属于利用有、无质量标签批次的半监督回归；8批提供实测质量回归目标，全部批次的已观测测量经人为遮蔽后提供自监督重建目标，与回归联合训练。自然缺失位置没有实测重建真值。没有独立预训练阶段，也没有故障类别；不能称整个系统无监督，或仅凭8批判定few-shot。

英文问题句：How can batch quality be estimated when only some batches have measured quality labels?

**设计2**：所有窗都有人工二元标签；相对窗口分类，这是直接监督，相对拟研究的逐时刻检测，则是粗粒度弱监督，不是“无标签”。逐时刻输出机制及相应评价依据仍未知，实验未开始，不能说细粒度检测已实现。

英文问题句：Can point-level anomalies be detected using only window-level anomaly annotations?

**定义边界**：自监督描述信号如何从数据构造，不是弱监督与无监督的总称，可与监督任务共同训练。广义弱监督可能包含标注不完整，狭义常指粗粒度或不准确标注，因此与半监督并非永远互斥。正常数据建模还须说明正常性由谁确认、是否用标注筛选或调阈值；部分检测文献称已知正常数据训练为半监督，不能一概宣称完全无人标注。
