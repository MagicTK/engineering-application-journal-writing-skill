# Fictional Observation-Problem Baseline

One context answered A/B on immutable v4.2.2. Main science and positive prose already pass. Wrapper/path/link/line metadata and whitespace are normalized, and nonresearch live account-quota values are redacted; exact raw/dispatch remain private. Runtime orientation is disclosed, not case evidence. This current-copy redaction does not rewrite Git history.

运行定位（非案例证据）：从指定发布包 v4.2.2 中文入口进入 problem-only 路由，读取相关采样、掩码与评价参考；另读取通用运行时 Skill 并核对额度（账户用量数值已隐去）。以下 A、B 均按题设虚构条件计算，不是工业实测结果。

**A：观测口径**
这是**固定多速率观测，同时存在永久丢失和报告延迟**。共同网格中的空位不能统一解释为停机或采集故障。

| 项目 | 快变量 | 慢变量 |
|---|---|---|
| 原生周期、频率 | 1 s，1 Hz | 4 s，0.25 Hz |
| 0–9 s 内计划应得值 | 10 个 | 3 个 |
| 第 9 秒可用值的采集时刻 | 0、1、2、3、4、5、7、8、9 | 0、4 |
| 第 9 秒不可用的计划值 | 第 6 秒：永久丢失 | 第 8 秒：第 10 秒才释放 |

因此，**计划应得 13 个值，第 9 秒实际可用 11 个**；快变量第 5 秒的实测零值计入这 11 个。

- **共同网格不可用比例：**`9/20 = 45%`。其中慢变量非采样时刻占 `7/20 = 35%`，永久丢失占 `1/20 = 5%`，晚到占 `1/20 = 5%`。
- **原生计划应得值不可用比例：**`2/13 ≈ 15.38%`。永久丢失、晚到分别为 `1/13 ≈ 7.69%`。按各变量自身分母，分别是快变量 `1/10 = 10%`、慢变量 `1/3 ≈ 33.33%`。

慢变量在 1、2、3、5、6、7、9 秒**没有计划采样事件**，不是七次丢测。原生时钟仍然规则；快变量收到的记录在采集时间轴上出现 5→7 秒的两秒间隔，其余相邻间隔为一秒。慢变量的采集时刻为 0、4、8 秒，释放时刻为 0、4、10 秒：后者的间隔是 4、6 秒。**收到记录的间隔不均，不等于原生采样计划不规则。**

第 8 秒慢值的报告延迟为两秒；物理过程滞后没有给出，不能从采样周期或晚报推定。

允许等到第 10 秒再估计第 9 秒的目标。准确说法是：**目标时刻为 9 秒、使用截至第 10 秒可用信息的延迟估计**，实际输出不早于第 10 秒。该值仍代表第 8 秒的测量，但不能回写为第 9 秒决策时已经可用；这也不是第 9 秒之后才采集的测量。

掩码本身不能识别 MCAR、MAR 或 MNAR，也不能证明插补性质或时序因果关系。

英文问题描述，60 words：

In this fictional case, two measurements follow fixed schedules with periods of one and four seconds. Of thirteen scheduled values through second nine, eleven are available for the decision at second nine. One fast measurement is permanently lost, while the slow measurement acquired at second eight becomes available at second ten. The observed fast measurement at second five equals zero.

**B：遮蔽计数**
裁剪后的区间为 `[0,10)`、`[5,15)`、`[98,100)`；并集为 `[0,15) ∪ [98,100)`。

| 量 | 计算结果 |
|---|---|
| 起点密度 | `3/100 = 3%` |
| 请求长度之和 | `10+10+10 = 30` 个位置，含重复及越界请求 |
| 实际缺失项 | `15+2 = 17` 个 |
| 受影响变量缺失比例 | `17/100 = 17%` |
| 全变量缺失比例 | `17/(100×2) = 8.5%` |

也可核算为 `30−8（越界）−5（重叠）=17`。所以，“3% missing data”不能由起点密度推出；“30% missing values”也不能由请求总长度推出。3% 是起点密度，30 是请求长度总和，均不是最终缺失项比例。

**P37 与 B 分开：**仅按题供来源笔记，可迁移 `R_f = 缺失段起点数/序列总长度` 的定义，以及段长另行控制这一设置区别；不能把 `R_f` 直接改称缺失值比例。没有原代码或最终掩码，不能认证 P37 实际受影响变量或全变量的缺失比例，也不能把 B 的裁剪、重叠规则与 17%／8.5% 套给 P37。本轮读取的 [P37 发布包记录，第 570 行](../../references/published-evidence.md)未载该 `R_f` 定义，因此这里明确将其归为**题供来源笔记，而非本轮原文核验**。

**规则审计**
- **问题路由已有覆盖。**[中文入口第 75 行](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)明确进入问题优先分类；[分类表第 33–36 行](../../references/problem-first-classification_CN.md)已区分缺失、多速率、不规则间隔、报告可用时刻及过程滞后。这些现有规则足以支持 A 的基本分类。
- **零值、掩码角色和分母已有明确规则。**[术语参考第 125–129 行](../../references/terminology-decisions_CN.md)明确“测得的零仍是观测”，并要求说明计数与分母；[评价参考第 196–210 行](../../references/experiment-evidence-design.md)区分参考可用性、实际输入掩码及计分位置。不能把这些说成尚未覆盖。
- **采样与延迟说明也已可访问。**[采样参考第 21–45 行](../../references/topic-playbooks.md)区分原生观测、对齐生成值及释放延迟，并链接评价检查；[时序评价第 596 行](../../references/experiment-evidence-design.md)明确分开输入代表时刻、信息可用时刻和实际输出时刻，足以支持延迟分析的准确命名。
- **可确认的局部缺口是显式计数导航。**问题优先分类第 31–36 行没有直接列出“共同网格位置／原生计划事件／截至决策时刻可用值”三种计数，也没有直达既有掩码与分母规则的链接；上述采样、掩码和评价段落也未显式给出“段起点密度／请求长度和／裁剪去重后缺失项”的换算区别。这是局部说明与导航缺口，**不是整个 Skill 缺乏采样或分母原则**，更不需要因此引入预测器、插补方法或实验计划。
