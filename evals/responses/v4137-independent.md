# Fictional Origin And Causal-Scope Response

One fresh task context handled four final requests; source and request coverage changed, not a controlled source-only comparison.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. These are synthetic writing/arithmetic checks, not scientific experiments.

审计：四项共用本次一个上下文，并非四次独立运行。预置上下文含历史摘要，本次未据其作答或检索历史。实际访问了指定 Skill（v4.1.37）、下列四份现行参考、通用 bootstrap 及其 Codex 工具说明；两次调用只读配额服务，并核算词数与算术。未检索文献、评测、既往答复、私有记录、真实论文或其他项目；未改文件、安装、运行实验、发布或调用其他代理。

**M4137-A**

1. 相关工作收束／需求：

> [R1] learns a flat predictive relation graph over all variables and returns variable candidates. [R2] provides unit-level locations without defining within-unit localization. For the present three-unit process, the modeling requirement is to connect cross-unit relations with within-unit variable relations and carry that distinction into a unit-to-variable decision that returns the initiating variable.

2. 方法总览：

> Lagged measurements are encoded into variable representations to form a graph within each fixed process unit. Each unit’s graph is summarized into a unit representation, and the three representations form a unit graph. Prediction objectives fit both levels. During analysis, each unit node undergoes a computational attack under the prescribed graph-load redistribution rule. The resulting scores select one unit; variable scoring then operates only on that unit’s graph and returns the estimated initiating variable.

3. 一项贡献候选：

> A two-level relation model links within-unit variable dependencies and cross-unit relations to sequential localization: node-attack scores under graph-load redistribution select a unit, whose variable graph then supplies the initiating-variable candidate.

作者注：保持现有实现，不增分类头；普通编码器不另立创新。载荷是定义的图数值，攻击是计算操作。独立事件评价仅已规划，未声称验证成功。[R1][R2]均为虚构占位，未将未测设置写成实测失败或全领域缺陷。

**M4137-B**

不应仅因缺少真实干预实验而一概删除 **causal effect**。题设中 \(Z\) 阻断后门路径 \(X\leftarrow Z\rightarrow Y\)，且独立扰动保证：

\[
E[Y\mid X=x,Z=z]=0.5x+2z,\qquad
E[Y\mid do(X=x)]=0.5x.
\]

因此，单位总体总因果效应为 \(0.5(x+1)-0.5x=\mathbf{0.5}\)。这是给定模型的解析效应，不是未提供的样本估计。

> Under the specified causal model, we estimate the population total causal effect of increasing X by one unit from observational samples by adjusting for Z in the conditional mean E[Y|X,Z].

作者注：观测样本用于估计，给定图及结构假设用于识别；实测干预提供另一类实证证据，并非本题识别的必要前提。此判断不认证现实图假设，也不把总体效应转换为某次故障根因。

**M4137-C**

| 指标 | 对象与分母 | 核算 |
|---|---|---|
| 图 precision | 预测的6条有向边 | \(4/6=66.67\%\) |
| 图 recall | 真实的6条有向边 | \(4/6=66.67\%\) |
| 图 F1 | 边计数组合 \(2TP+FP+FN=12\)，不是事件数 | \(8/12=66.67\%\) |
| 事件 top-1 | 全部12次独立事件的最终变量排名 | \(9/12=75.0\%\) |
| 事件 top-3 | 同一批12次事件、同一最终排名 | \(11/12=91.67\%\) |
| class-F1 | 另一分类器的故障类别预测；样本数、平均方式及计算计数未给 | 仅知 \(0.92\) |

> Directed-edge precision, recall, and F1 were each 0.667, with four correct edges among six predictions and six true edges. Across 12 independent fault events with injection-record origins, the final variable rankings achieved top-1 and top-3 hit rates of 75.0% (9/12) and 91.7% (11/12). A separate fault-class classifier reported F1 = 0.92. These metrics evaluate graph recovery, origin localization, and fault classification, respectively.

作者注：图F1和class-F1均不能改称“root-cause accuracy 92%”。单起源且仅搜索所选单元时，端到端命中率＝选对单元概率×选对单元后的条件命中率；仅报后者会漏计选错单元的失败，题设最终事件评价已覆盖完整链条。若参考只是最早响应变量，应称“相对于最早响应参考的定位命中率”，不能认定找到了物理起始故障。

**M4137-D**

甲：原句 “The attention map proves the physical root cause.” →

> The attention map visualizes the weights assigned to process variables by the fault-class classifier.

理由：只描述权重可视化，不升级为预测归因或物理因果证明。

乙：原句 “Plant interventions verify the actual failure source.” →

> Attacking nodes of the fitted directed graph under the defined numerical rules produces a ranking of candidate source nodes.

理由：保留图上数值操作及候选排序，不虚构实体干预或独立起源验证。

丙：原句 “Real-plant trials establish the intervention effect across all operating conditions.” →

> Controlled flow-setting interventions in the known structural-equation simulator yield a mean quality-response contrast between two settings, estimated from repeated simulations with other inputs and disturbance distributions held constant under the tested conditions.

理由：保留仿真器内受控干预的有效证据；范围限定为已测条件，不冒充真实工厂试验或全工况结论。

现行参考：
- A：[contribution-narratives.md](../../references/contribution-narratives.md)、[argument-and-prose-craft.md](../../references/argument-and-prose-craft.md)。
- B／C／D：[experiment-evidence-design.md](../../references/experiment-evidence-design.md)；B／D另用 [terminology-decisions.md](../../references/terminology-decisions.md)。
