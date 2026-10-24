# Fictional Origin And Causal-Scope Response

One pre-change request was answered correctly; this is not a demonstrated failure. The interrupted earlier attempt produced no completed answer.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. These are synthetic writing/arithmetic checks, not scientific experiments.

**判断**
审稿人要求一概删除 `causal effect`，在题设下不成立。当前 Skill 要求术语与主张、假设及证据匹配；其[因果建模条目](../../references/topic-playbooks.md)明确要求区分干预效应、结构识别和根因排序，不能将“没有真实干预实验”等同于“只能讨论关联”。

**效应计算**
给定图为 \(Z\to X\)、\(Z\to Y\)、\(X\to Y\)。调整 \(Z\) 阻断后门路径 \(X\leftarrow Z\to Y\)，且
\[
E[Y\mid X=x,Z=z]=0.5x+2z.
\]
在结构干预 \(do(X=x)\) 下，
\[
E[Y\mid do(X=x)]=0.5x,
\qquad
E[Y\mid do(X=x+1)]-E[Y\mid do(X=x)]
=\boxed{0.5}.
\]
没有经过其他变量的中介路径，因此这里的直接效应也就是总效应。

三种角色应分开：
- **观测数据**：用于拟合条件均值并调整 \(Z\)，估计效应；不自动发现或证明因果图。
- **已给因果假设**：赋予调整结果因果解释。本题接受这些设定，不是在认证现实产线的图假设。
- **实测干预**：提供直接的干预响应证据；本研究没有这种证据，但这不取消题设模型下已成立的条件性因果含义。

\(0.5\) 是模型中的精确总体效应，不是声称有限样本回归必然恰好得到该值，也不能自动解释某次故障的根因。

**英文方法表述**
:::writing{variant="standard" id="73519"}
Under the specified causal graph and independent-disturbance assumptions, we estimate the population-average total causal effect of a one-unit increase in X from observational data by fitting E[Y|X,Z] and standardizing over Z.
:::
