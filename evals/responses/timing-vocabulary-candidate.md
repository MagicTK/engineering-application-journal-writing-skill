**读取说明**
仅读取了请求文件及以下 Skill 文件：
- 总控入口：[英文](../../SKILL.md)、[中文](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)。
- 术语润色入口：[英文](../../skills/engineering-terminology-polishing/SKILL.md)、[中文](../../skills-zh/engineering-terminology-polishing-zh/SKILL.md)。
- 术语决策参考：[英文](../../references/terminology-decisions.md)、[中文](../../references/terminology-decisions_CN.md)。

一次合并读取发生输出截断；本次使用的采样、时间及对齐小节随后已完整补读。上下文不可避免地预载了工作区指令、技能目录和历史记忆摘要，故不声称这是盲测；未读取记忆文件或将历史项目事实用于作答。套餐内额度已核实可用，未修改文件、联网或调用额度重置。

**1. Methods 术语核查**

| 原称呼 | 准确含义 | 建议词及单位 |
|---|---|---|
| “3 and 8 Hz” | 3、8是网格间距的倍数；对应周期为0.75、2 s，名义采样率为4/3、0.5 Hz | `interval multiplier`，无量纲；`nominal sampling period`，s；`nominal sampling rate`，Hz |
| “common 0.25-s acquisition clock” | 已知的是参考网格间距，不能据此确认硬件共用采集时钟 | `reference time grid`；`grid spacing`，0.25 s |
| 保持后的网格值视为新采样 | 网格每秒有4个位置，但保持已有测量不会新增采集 | `grid positions`；`held measurements`，保持原测量单位 |
| “changes the sampling period … to 1.5 s” | A的实际相邻存储观测间隔为0.75、0.75、1.50 s；名义周期仍为0.75 s | `interval between available observations`，s |
| “nine-sample input covers nine seconds” | 一个输入窗口含9个网格位置；首尾跨度为(9−1)×0.25＝2 s | `window length`，9 grid positions；`window time span`，2 s |
| “prediction every 0.25 s” | 0.25 s是网格间距；窗口步长为4个位置，即1 s；输出间隔未知 | `window stride`，4 grid positions / 1 s；`prediction output interval`，待核实 |
| “0.4-Hz process frequency … acquisition rate” | 0.4 Hz是A过程量的振荡峰频率，不是采集频率 | `process oscillation frequency`，Hz |

Methods 改句：
Starting at t = 0, measurements of A and B were scheduled every three and eight reference-grid spacings, respectively. The grid spacing was 0.25 s, giving nominal sampling periods of 0.75 s for A and 2 s for B, corresponding to nominal sampling rates of 4/3 Hz and 0.5 Hz. The stored measurement timestamps were 0, 0.75, 1.50, and 3.00 s for A and 0, 2, and 4 s for B. The scheduled measurement of A at 2.25 s was missing, leaving a 1.50-s gap between the available observations at 1.50 and 3.00 s. Preprocessing held the latest available measurement at each reference-grid position. Each input window contained nine grid positions spanning 2 s, including both endpoints, as in the window from 0 to 2 s. Successive windows were shifted by four grid positions, corresponding to 1 s. Independent spectral analysis reported an oscillation peak at 0.4 Hz in process variable A.

作者备注：需核实预测发出时刻、输出间隔及其与输入窗口的对应关系，不能由网格间距或窗口步长直接推出。若仍要使用“common acquisition clock”，还需确认实际硬件共钟或触发机制。

**2. Timing Input**

The feature encoder uses the measurements together with a 3-by-3 matrix of pairwise absolute time differences, defined by D_ij = |t_i - t_j|.

时间戳为(0, 1, 5) s，相邻间隔只有两个，即(1, 4) s；实际输入则包含所有观测对的绝对时间差：
\[
D=\begin{bmatrix}
0&1&5\\
1&0&4\\
5&4&0
\end{bmatrix}\ \mathrm{s}.
\]
因此，不能称为“三个相邻采样间隔”，也没有依据引入固定“sampling cycle”。使用该矩阵提供时间差信息，本身不构成观测同步；没有额外对齐操作，故删除同步保证。

两种统计的计算都正确，但含义不同：
- **Mean of reciprocal adjacent intervals**：\(\tfrac12(1/1+1/4)=0.625\ \mathrm{Hz}\)，即相邻间隔倒数的算术平均。
- **Reciprocal of the mean adjacent interval**：\(1/[(1+4)/2]=0.4\ \mathrm{Hz}\)，即平均相邻间隔的倒数，也等于0至5 s范围内的两个间隔除以5 s。

报告时应写明统计定义和观测范围，不能仅用未定义的“average sampling frequency”混指二者；两者都不证明存在等间隔采集计划。

**3. Grammar**

The process variables were measured at varying intervals.
