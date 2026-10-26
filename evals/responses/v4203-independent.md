# Fictional Observation-Problem Final Response

A fresh context answered the same A/B on frozen v4.2.3, changing only the reading root. Baseline science/prose already pass; this checks the explicit observation profile and retained boundaries, not general gains. Wrapper/path/link/line metadata and whitespace are normalized, and nonresearch live account-quota values are redacted; exact raw/dispatch remain private. Runtime orientation is not case evidence. This current-copy redaction does not rewrite Git history.

运行取向披露：采用当前仓库 **v4.2.3 中文入口的 problem-only 路由**；运行规则与旧记忆仅用于导航，不作为案例证据。已检查包含额度（账户用量数值已隐去）；未使用付费接口或重置额度。本轮只读，无编辑、浏览、原论文访问、实验或新代理。以下 A/B 数值均为虚构。

**A：规则多速率下的观测不可用**
这是**规则多速率采样，叠加永久丢失与报告延迟**，导致9 s决策时观测不完整。

| 计数项 | 快变量 | 慢变量 | 合计 |
|---|---:|---:|---:|
| 原生周期 | 1 s | 4 s | 不适用 |
| 原生频率 | 1 Hz | 0.25 Hz | 不适用 |
| 0至9 s预期采集值数 | 10 | 3 | **13** |
| 9 s实际可用值数 | 9 | 2 | **11** |

快变量可用时间为 `{0,1,2,3,4,5,7,8,9}`，慢变量为 `{0,4}`。快变量5 s的**实测零值计入观测**。

- **共同网格不可用比例：** `(7+1+1)/20 = 45%`。其中慢时钟未安排采样的位置为 `{1,2,3,5,6,7,9}`，占`7/20=35%`；永久丢失和晚发布各占`1/20=5%`。七个非采样位置不是七次采集故障。
- **预期采集值不可用比例：** `2/13≈15.38%`；永久丢失分量为`1/13≈7.69%`，晚发布分量为`1/13≈7.69%`。分母都是13个预期测量值，不是20个网格位置。

原生时钟均规则；快变量收到的测量时间间隔因6 s丢失而出现2 s间隔。慢变量原生采集时间为`0,4,8`，发布时间为`0,4,10`，后者间隔为4 s、6 s。**接收间隔不均不证明原生采样不规则**。8 s测量的报告延迟为2 s；物理过程滞后未知，也不能由掩码判定MCAR、MAR或MNAR。

等待10 s使用慢变量8 s值，可以形成**针对9 s的延迟估计**：目标时刻9 s，该输入采集于8 s、可用于计算始于10 s，输出实际发出于10 s或更晚。若10 s发出，则相对目标时刻延迟1 s；不能倒写为9 s决策已经取得该值。

英文问题描述（60词）：

Two process variables are scheduled every 1 s and 4 s over 0-9 s. At the 9 s decision, 11 of 13 scheduled measurements are available on a 20-position grid. The fast measurement at 6 s is permanently lost; the slow measurement acquired at 8 s is released at 10 s. The observed fast value at 5 s is zero.

**B：起点比例与实际缺失条目**
裁剪后的区间为`[0,10)`、`[5,15)`、`[98,100)`；并集为 **`[0,15) ∪ [98,100)`**。

| 项目 | 计算结果 |
|---|---:|
| 缺失段起点密度 | `3/100 = 3%` |
| 请求段长之和 | `10+10+10 = 30` |
| 裁剪后长度之和，尚未去重 | `10+10+2 = 22` |
| 实际缺失条目 | `22−5 = 17` |
| 受影响变量缺失比例 | `17/100 = 17%` |
| 全变量缺失比例 | `17/200 = 8.5%` |

因此，**“3%缺失数据”和“30%缺失值”都不能这样推出**。3%是起点密度；`30/100=30%`只是请求长度总和相对单变量长度的比例，包含重叠与越界。完整题设允许通过裁剪、取并集算出实际比例，而不能直接使用这两个生成参数代替。

**P37：单独处理**
依据题给来源说明及[本地来源记录第130至139行](../../references/published-evidence.md)，可以迁移的是定义：`R_f = 缺失段起点数 / 总序列长度`，段长另控；**它不是缺失测量条目比例**。未核原代码及实际掩码，不能认证P37受影响变量或全变量的实际缺失率，也不能假定其重叠、裁剪及变量覆盖规则，更不能移植本玩具的17%或8.5%。

**只读审计**
本次所需区别**已有规则足够支持，未发现必须新增的规则缺口**：

- **入口可达：** [中文入口第75行](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)直接导向问题优先分类；[采样专题第21至25行](../../references/topic-playbooks.md)也要求problem-only先走计数概况，无须进入方法或实验设计。
- **问题层已明确：** [问题优先分类第54至66行](../../references/problem-first-classification_CN.md)覆盖原生安排、预期次数、实测零、发布时刻、网格非事件、延迟估计、缺失机制未知，以及起点比例与实际比例的分母区别。
- **既有采样与掩码规则已足够：** [场景术语第125至127行及第256至260行](../../references/terminology-decisions_CN.md)分别确认实测零仍是观测，以及固定周期、接收时间、报告延迟、过程时滞与网格复用的区别。
- **评价边界已明确：** [评价参考第93至101行](../../references/experiment-evidence-design.md)区分原生观测与网格、目标与发出时刻；同文件[第198至204行](../../references/experiment-evidence-design.md)明确段长、重叠、裁剪及变量覆盖影响实际比例，并禁止推断未核代码行为。

这些区别已在问题优先入口提前呈现，并与既有参考衔接；没有数值算例本身，不构成规则缺失。
