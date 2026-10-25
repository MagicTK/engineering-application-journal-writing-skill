# Operating-Condition Classification: Actual Response

One fresh context used frozen v4.2.11 on two fictional requests. The initial answer and a targeted same-context correction are both retained below. Only writing-block wrappers and trailing whitespace are normalized. This is not a controlled improvement claim or full-suite certification.

## Initial Actual Answer

**请求 A**

这些标签应按不同维度整理，允许交叉，不必组成一棵互斥的分类树：

| 标签 | 所属层面 | 分类要点 |
|---|---|---|
| Multimode | 运行条件 | 多个可辨识的离散运行模式或工况。 |
| Non-stationary | 时间与统计性质 | 统计性质随时间变化；不只指连续缓慢漂移，也可涉及切换。多工况本身不证明非平稳。 |
| Compound Fault | 故障共存设置 | 多个故障同时存在；最终输出可以不同，不自动等于多标签分类。 |
| Few-Shot | 标注样本支持条件 | 指定任务、类别下可用的少量标注样本，不自动意味着未见类别。 |
| Weakly-/Self-Supervised/Unsupervised Learning | 监督条件与训练方式 | 分别关注监督的不完整或粗糙程度、自构造目标、特定训练阶段是否使用外部任务标签，不能简单并列为互斥问题类别。 |
| Attention | 技术机制 | 是方法标签，不是工业问题，也不对应唯一问题。 |
| TSMC | 发表来源 | 若这里指期刊目录，则属于来源标签；具体分刊不能仅凭缩写确定。 |

**甲：多配方工况下，已知故障类别的跨工况泛化问题。** B 是拟合和模型选择阶段均未访问的工况，六种故障类别则保持一致。
The study evaluates fault classification for six shared fault classes under an unseen operating condition, with model fitting and selection restricted to recipes A and C and recipe B reserved for testing without prior access to its data.
这支持“未见工况测试”的设置描述，不证明已获得良好的泛化能力，也不是未见故障类别识别。独立抽样和配方差异不提供时间轨迹，尚不能据此断言非平稳、渐进漂移或具体的分布偏移类型。

**乙：按已知计划调整进料流量的时变工况问题。** 最终预测或判断任务尚未给出。
The study concerns continuous production in a single process unit under time-varying operating conditions, with the feed flow rate changed in steps according to a known schedule.
这里有明确的工况时间变化，但不能仅凭流量调整认定输入与目标关系发生概念漂移；也不支持故障演化、设备老化、早期故障或提前预警解释。

用词建议：
- **operating conditions**：本题描述配方、进料流量等工况时优先采用；甲可用 `unseen operating conditions`，乙可用 `time-varying operating conditions`。
- **operational conditions**：不一概判错；按具体语境使用，本题采用前者更直接。
- **varying conditions**：上下文已明确所指时可以使用，否则补成 `varying operating conditions`。
- **operating varying**：不适合作为本题“变工况”的表达，改为 `varying operating conditions`。
- **operational state**：适合描述系统或单元的运行状态，应说明是物理状态还是推断状态；不能随意与 condition 或离散 mode 互换。

以上是语义与搭配建议，不是全领域词频排名。

**请求 B**

| 研究 | 标签条件 | 实际训练信号 | 最终任务 |
|---|---|---|---|
| 第一个研究 | 每个训练窗口都有完整的整窗二元标签，但没有异常位置标签。相对于位置判断是粗粒度标注；相对于实际整窗分类任务，则是直接、完整的任务监督。 | 整窗标签提供有监督分类信号；同一编码器的掩蔽重构以原有已观测测量构造自监督信号。存档但未使用的无标签窗口不贡献训练信号。 | 整窗异常／正常二分类，不是逐点定位，也不以重构为最终输出。 |
| 第二个研究 | 具有完整的实测浓度目标；连续数值同样属于任务标签。 | 实测浓度直接监督回归，没有自构造目标。 | 浓度估计的有监督回归；未给出预测时距，不能另称未来预测。 |

几个术语的关系：
- **弱监督**须相对于目标粒度和具体限制说明。第一个研究不能仅因没有位置标签，就把其整窗分类笼统判为弱监督。
- **半监督**要求有标签与无任务标签数据实际参与学习。只存档无标签窗口不构成半监督。
- **自监督**描述训练目标从数据自身构造，可以与有监督分类共同使用；不意味着整个研究没有标签。
- **无监督**应注明哪个训练阶段不使用外部任务标签。自监督可在广义分类中归入无监督学习，但第一个研究整体不能因此称为无监督。
- 这些概念不是严格互斥的四选一：广义弱监督分类可包含半监督；采用较窄定义时，则常专指粗粒度、歧义或不可靠监督，应明确采用的含义。

第一个研究的 Methods 概述：
We train a shared encoder using window-level binary classification labels and an auxiliary self-supervised masked reconstruction objective whose targets are the original observed measurements, with the final model predicting a single binary label for each window.

**访问披露**
实际读取了指定中文 `SKILL.md`，以及本地参考 `references/problem-first-classification_CN.md`、`references/industrial-ai-taxonomy.md`、`references/terminology-decisions_CN.md`。其他资源访问仅为只读额度查询，首次成功，后续复查未返回状态；未执行重置或信用额度操作。未联网、读取原论文、评测材料、历史回复、私人项目记录或记忆文件，也未修改文件或运行实验。

## Actual Follow-Up Correction

The study concerns continuous production in a single process unit under time-varying operating conditions, with the feed flow rate adjusted according to a known schedule.

“Changed in steps”额外引入了阶梯式变化的轨迹事实，现改为按已知时间表调整，不预设阶梯式跳变或连续变化。
