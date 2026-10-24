# Fictional State-Estimation Writing Response

Final-source response with two explicit actual-input timelines. One fresh task context handled four requests. Only private local reference links and terminal blank lines are normalized. No scientific experiments or real manuscript edits occurred.

边界说明：上下文预置了历史摘要，并非记忆空白；本轮未检索或援引任务历史。主动访问仅限通用引导、只读额度检查及当前 Skill 4.1.35 的必要参考；未联网、读取原论文、编辑或运行实验，不披露账户数值。

**M4135-A**
英文按空格计词，连字符词计一个：总览64词，贡献候选22词。

:::writing{variant="document" id="41351"}
Overview

A linear Gaussian state-space model represents measurements through two statistical latent states: u directly supplies the quality predictor, while v supports inference of u solely through their shared observation equation. Parameters are fitted only on historical training sequences using forward filtering, backward smoothing and EM. With parameters fixed, prediction recursively filters measurements permitted and available by issuance to infer u and estimate current quality.

Contribution Candidate

A dual-latent formulation uses u directly for quality estimation and v solely to support inference of u through their shared observation equation.
:::

中文审核：保留了直接输出与辅助推断的区别，未赋予潜坐标物理健康或工况含义。训练平滑没有进入预测路径，状态递推也未写成参数学习；贡献仍只是候选，尚无独特性或性能证据。

**M4135-B**
:::writing{variant="document" id="41352"}
1. With fixed transition and observation parameters, a mechanistic model explicitly defines reactant concentration and temperature as physical states and uses Kalman filtering to estimate them.

2. After each prediction is issued, online EM updates the transition matrix using permitted past data, and the updated matrix is used for the next prediction.
:::

第一项已有明确物理定义，不能一律改成不可解释潜变量；第二项确实改变转移矩阵，不能删去真实参数学习，也不能让更新反向进入已经发出的预测。

状态协方差表示模型下的状态估计不确定性，**不自动是故障概率**；故障事件定义、概率关联及校准证据均需另行建立。

**M4135-C**
C1为28词，C2为22词。

:::writing{variant="document" id="41353"}
C1

With prediction parameters fixed, the minute-100 state estimate was issued at minute 102 using observations newly measured and released at minute 102, within the permitted two-minute fixed lag.

C2

With prediction parameters fixed, the minute-100 state estimate used only observations released by minute 100; computation alone delayed issuance until minute 102.
:::

- **C1：**按102分钟发出报告，是允许的两分钟固定时滞估计。改报100分钟已发出，同时构成发出时间误报及该决策时点的信息访问违规，因为实际用了102分钟才发布的观测。
- **C2：**改报100分钟已发出属于计算延迟误报，零延迟主张不成立；但不能仅凭晚发判定未来信息泄漏。按给定实际输入，没有使用100分钟之后发布的观测。
- **共同边界：**101分钟只有模型状态传播，**不增加独立实测样本**。训练平滑仅作用于历史训练数据，不据此判定预测泄漏；预测参数也没有更新。

**M4135-D**
以下仅转述[当前术语记录](../../references/engineering-application-terminology-bank.md)及其[核验范围说明](../../references/published-evidence.md)，不是本轮重读原文。

- **基础名称支持：**P34与P73是两篇不同流程工业作品，支持限定的线性高斯潜状态 **state-space model**，以及相应状态预测、协方差预测和观测校正意义的 **Kalman filtering**；不表示两者实现完全相同。
- **重复副本：**P34的本地重复副本仍是同一学术作品，不能凑第三篇。
- **不能外推：**这些记录没有完成全部神经、非线性、自适应完整模块名的准入，也未独立复现全部矩阵公式、索引、阈值与最优性保证，更不认证故障概率校准或零延迟保证。

[中文审核记录](../../references/engineering-application-terminology-bank.md)分别记载：
- **AAS c230457：**核对到图5双语图注中深度变体内的 state-space 基础词对应，支持“状态空间模型”的限定用语核查，不是完整正文定义阅读。
- **AAS 2013.00043：**核对到双语题名、摘要、关键词，支持 Kalman filter/filtering 与“卡尔曼滤波”的基础对应，不声称完整正文已读。
- **《测绘通报》2017.0338：**核对到原始双语题名、摘要、关键词及第1—2节，支持滤波与固定时延平滑的用语区分。

缺失正文不能记为已读；上述译名核查不增加流程工业定义篇数。准确且有操作定义的作者新提名称应保留并标明归属，不要求先有两篇同名论文，也不因此把它升格为已准入的通用类别。
