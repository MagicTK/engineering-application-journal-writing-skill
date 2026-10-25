# Multirate Quality-Prediction Writing: Actual Response

One fresh context answered the fictional request without feedback. The task answer below retains its wording. Display wrappers are removed, one local reference link is made relative, and the environment disclosure is omitted; reading and evaluation limits are recorded in the review.

**一、采样与术语核对**
三句初稿均有实质性错误。应区分原生采样安排、实际收到的观测、模型网格以及标签发布时间。

| 核对项 | 本题结论 |
|---|---|
| 压力采样 | 闭区间内计划采样11次，收到10次；按预期采样次数计，丢测率为 **1/11**。原生周期仍为1秒，即1 Hz；收到的观测中存在丢测造成的间隔增大。 |
| 温度采样 | 固定周期5秒，即0.2 Hz；计划2次、收到2次，预期测量丢失率为 **0/2**。因此不能称为 *irregularly sampled*。 |
| 温度的“9/11” | 只能表示11个每秒网格位置中，9个位置**没有新温度观测**，不能不加定义地称为测量缺失率。其中7个位置可沿用旧值，t=0、1则没有历史温度可用。 |
| 保持值与计数 | 两路输入共有12个原始收到的测量标量，模型网格有11行。保持值不增加真实观测数，也不能充当新增的真实重构目标；网格行数不等于独立训练样本数。 |
| 掩码与时间间隔 | 压力在t=6：掩码0、间隔1秒；t=7收到新值后：掩码1、间隔0秒。温度在t=10：沿用t=7值，掩码0、间隔3秒。这里的间隔不是相邻两次观测之间的间隔。 |
| 温度首次观测前 | t=0、1的“距最近已收到测量的采样时刻”尚无定义。初始输入及该间隔的表示规则未提供，不能擅自填成0，也不能使用t=2的未来观测回填。 |
| 化验可用性 | 两次结果均延迟25秒发布。t=10时，t=0和t=10的化验结果都不可用。“历史取样”不等于“历史已知”；而且题设明确化验不作预测输入。 |

**训练属于半监督质量预测，而不是整套无监督。** 已发布化验提供监督质量目标，无质量标签窗口通过观测重构参与共享编码器学习；重构可描述为由观测自身构造目标的自监督辅助任务。

历史批次的报告在拟合前全部发布，因此用它们监督历史取样时刻的质量估计，不等于回放预测读取未来标签。回放中保持参数固定、按发布时序取输入、固定预测后再评分，是另一条必须保留的信息边界。隐藏状态递推也不等于在线参数更新。

**二、英文摘要**
196词，按空白分词，连字符词计一词。

Industrial quality estimation must accommodate process variables measured at different fixed rates, occasional measurement loss, and delayed laboratory assays. We develop a semi-supervised quality predictor that uses available process measurements and their timing to estimate current quality. At each second, the input retains the latest received measurements, where available, alongside masks identifying new observations and elapsed times since each variable's latest received measurement was sampled. A shared encoder extracts variable features. Conditioned on the masks and elapsed times, a gate weights these features and the previous hidden state to form an updated state, from which a readout estimates quality. During historical training, an auxiliary reconstruction head and the quality readout share the encoder. Reconstruction error is evaluated only at original observed entries, whereas quality error uses released assay labels at their associated sampling times. Windows without quality labels also contribute through reconstruction, allowing their measurements to shape the representation used for quality prediction. Inference retains the encoder, gated state update, and quality readout with fixed parameters. Replay evaluation on a process simulation case and a real production dataset yields lower root mean square error than a baseline lacking elapsed-time information under the same measurement availability constraints.

**三、数据评价说明**
83词，计词方式同上，可直接放入实验部分。

Training and parameter selection used only earlier production batches whose assay reports had all been released before fitting. Later batches were held out in their entirety for replay evaluation. Each prediction used only information available according to the original release times, with model parameters fixed. Assays served as targets, not prediction inputs. Prediction files were fixed before comparison with subsequently released assay values. Quality RMSE was calculated only at the corresponding assay sampling times; assay values were not replicated as per-second ground-truth labels.

**四、模块替代句与命名**
A gate conditioned on observation masks and the time elapsed since each variable's latest received measurement was sampled combines the encoded variable features with the previous hidden state to produce the updated state used for current quality estimation.

原句的 *standard industrial mechanism* 缺少通用性依据；*recover all unobserved measurements* 则与实际输出不符。这里更新的是隐藏状态，最终输出是质量估计；训练中的观测重构不构成缺失测量恢复结果。

**目前不能把 “observation-age gate／观测年龄门控”作为已确立的通用术语收入组内词库。** 根据仓库的[名称准入规则](../../references/engineering-application-terminology-bank_CN.md)，完整英文名称需要至少两篇独立相关已发表论文的同义操作依据，中文译名还须独立核查。本轮没有这些核验。它可作为本论文专用词表中的待确认名称，但不能因此宣称标准机制或创新；未核实也不等于证明该名称从未被使用。

门控区别性公式和文献比较仍待作者提供。现有定性结果仅支持所述案例中相对该基线的质量RMSE改善，不支持缺失恢复精度、实测实时性或产线部署主张。
