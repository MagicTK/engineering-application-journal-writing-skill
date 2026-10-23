# Forward-Test Review Trace: Background-Driven Industrial Application

- Evaluator: `01a00fcd-ccdf-7ee3-9967-211afd6dacbc` (`Kuhn`)
- Model: inherited session model; exact identifier was not exposed by the subagent tool
- Context: fresh, read-only
- Tested Skill: `skills/background-driven-industrial-application/SKILL.md`

## Prompt

你是独立前向测试员。只读，不修改任何文件。阅读上述 Skill。对下面原始请求执行技能，输出问题提炼、论文主线与实验角色：

> 现场有电炉电流、温度、配料记录和视频，目标是降低能耗并识别异常运行状态。希望从应用背景出发写工程应用顶刊，不想写成算法排行榜。

## Response

The response below preserves the decisions and failure-mode checks used for scoring; formatting and repeated detail were condensed.

该课题应采用背景驱动型工业应用范式。论文的中心不是提出通用网络，而是解释配料、工艺阶段、能量输入、热响应和可视运行现象如何共同形成状态识别与能效判断问题。

建议研究问题为：在配料和工艺阶段持续变化的条件下，如何利用截至当前时刻可获得的电流、温度、配料及视频证据，区分正常工艺需求造成的高能耗与异常低效行为，并在可干预时间窗内为操作人员提供报警和节能依据？若数据没有可操作变量和干预结果，任务只能称为能耗预测、能效评估或节能机会识别，不能称为能耗优化。

推荐证据链：

```text
配料事件与物料条件
  -> 电流表征能量输入
  -> 温度表征热响应
  -> 视频表征可见运行现象
  -> 时间同步后的批次/阶段样本
  -> 状态判断与条件化能耗评估
  -> 报警或操作建议
```

论文应先补齐电炉类型、工艺阶段、批次边界、能耗指标、质量与产量约束、视频观测对象、同步误差、异常标签来源、当前报警方式、可操作变量和决策提前量。模型组件只能响应已经证实的阶段变化、异步对齐、多源证据或条件化评估要求。

实验角色包括：数据与任务有效性、当前实践比较、能耗主任务、异常主任务、联合任务验证、背景组件消融、跨工况泛化、信号受损鲁棒性、工程解释和在线价值。实际节能只能由影子运行、受控试验或在线干预支持；单现场历史数据最多支持现场相关性和离线工程价值。
