# Forward-Test Review Trace: General Method With Dual Evidence

- Evaluator: `01a00fcd-cc52-7b91-bb8f-56c4c703307e` (`Faraday`)
- Model: inherited session model; exact identifier was not exposed by the subagent tool
- Context: fresh, read-only
- Tested Skills: `skills/general-method-benchmark-realworld/SKILL.md`, `skills/engineering-experiment-evidence-design/SKILL.md`

## Prompt

你是独立前向测试员。只读，不修改任何文件。阅读上述两个 Skill。对下面原始请求执行技能，给出精炼论文结构与实验蓝图，并明确哪些内容必须保留占位符：

> 我提出了一个适用于复杂工业过程故障诊断的通用神经网络，准备在 TE benchmark 和一个真实化工装置上验证；部分参数和真实装置结果还没完成。请设计文章与实验。

## Response

The response below preserves the decisions and failure-mode checks used for scoring; formatting and repeated detail were condensed.

论文应采用“通用方法 + benchmark + 真实工业案例”范式。TE benchmark 提供受控、可复现的方法证据；真实装置提供实际过程条件下的工程相关性。两个案例不能证明普适性、在线运行或跨装置泛化。

建议结构为 Introduction、Problem Formulation and Motivation、Proposed Method、Experimental Evaluation、Discussion 和 Conclusion。实验部分先说明证据分工、公平设置和指标，再分别组织 TE benchmark 的主比较、消融、敏感性、扰动与类别分析，以及真实装置的过程来源、标签形成、主比较、精选消融和工程解释。跨案例综合只总结共同收益、条件差异和适用边界。

实验蓝图逐项覆盖：比较优势、模块贡献、合理扰动下的鲁棒性、工况或时间留出的条件泛化、可解释性、真实装置工程相关性，以及只有在具有指定硬件或在线证据时才能讨论的效率和部署。TE 运行序列构造窗口时必须按运行划分；真实装置优先按时间、批次、生产周期或设备划分。归一化、缺失处理和参数选择只能使用训练及验证信息。

必须保留的占位符包括：

- `[CORE-CHALLENGE]`：真正的共性工业挑战；
- `[METHOD-PRINCIPLE]`、`[MODULE-1/2/3]`：方法原则与模块定义；
- `[SCOPE]`：可主张的过程、工况和任务范围；
- `[TE-SOURCE]`：TE 版本、变量、故障、采样、运行、窗口和划分；
- `[PLANT-CONTEXT]`：装置边界、工艺路线、数据时期和匿名化；
- `[LABEL-PROVENANCE]`：标签来源、标注时点与不确定标签处理；
- `[SPLIT]`、`[PREPROCESSING]`、`[BASELINE-CONFIG]`；
- `[HYPERPARAMETERS]`、`[ROBUSTNESS-LEVELS]`；
- `[RESULT-*]`：均值、标准差、提升、显著性和所有图表结论；
- `[HARDWARE/RUNTIME]`、`[EXPERT-VALIDATION]`、`[EVIDENCE-STATUS]`。

在真实装置结果完成前，摘要和结论只能保留中性计划表述或明确结果占位，不能提前写“验证了工程有效性”。
