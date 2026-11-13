# Crossed constraints: scope and response review

Two fresh readers each received two fictional tasks; after a substantive clarification, two different fresh readers repeated the same four prompts, rearranged across readers. The readers saw the public instructions but not the tests, manuscripts or each other’s answers. This is an open-guide writing test, not an estimate of field performance or an assessment of ten real papers. Verbatim response text below omits presentation markup.

The first round passed the four scoped writing decisions. One answer went further: keeping a second sensor as well as changing its time representation confounds the interpretation of the input factor. We added that distinction to the guide and repeated the test on the final instruction snapshot. In the final English batch answer, unit-only comparisons use less information; only pooled vs organized inputs can isolate organization, not the single-unit comparators. The proposed validation split is a design, not an existing split. The final Chinese crossed comparison names the missing cells and the paired difference between reductions; its positive outcome is not assumed. Neither numerical thresholds nor achieved gains were supplied in the other three cases.

## Initial reader 1

**batch**

The dryer and screen each record every lot, but the discharge record gives only one outcome for the lot: pass or reject. That outcome can be used to assess predictions from the two logs, but it cannot establish which unit, if either, caused a rejection.

**Candidate contribution:** Summarize each unit’s log separately, then combine the two summaries into one lot-level reject score trained against the discharge outcome. This would test whether preserving unit identity helps predict disposition without assigning the lot label to either unit.

**Evaluation figure:** Plot precision–recall curves for rejection on the same held-out lots. Compare the candidate with dryer-only, screen-only, and pooled-log models using the same information cutoff and tuning budget; show the reject fraction as a reference. Label any companion heat map “unit scores for lot disposition.” Calling it “fault localization” would require independently verified fault origins.

**synth**

**引言衔接：** 每个故障类虽可从三次独立采集中切出许多窗口，但增加窗口并不增加独立采集次数。因此，扩散增广值得检验的问题是：在真实采集次数不变时，生成窗口能否改善对另一次真实采集的诊断？

**方法贡献候选：** 拟按故障类生成训练窗口，与真实窗口混合训练分类器；测试时只使用分类器。

**划分与对照：** 先按采集划分，再切窗。做三折轮换，每折每类留一次完整采集作测试，其余两次用于训练；预处理和生成器均只用训练数据拟合。对照一仅用真实窗口，对照二用等量重复抽样替代生成窗口，以区分生成内容与重复呈现的作用。三组固定分类器和训练步数。

**图与报告：** 按故障类分面，对同一次留出采集，用线连接三种方案的窗口正确率。逐次列值，再对采集等权汇总；实测与生成窗口数分列。每类独立采集数仍为三，不据此推断跨设备效果。

## Initial reader 2

**Introduction.** A feed setting changed on Tuesday, raising the question of whether hourly soft-sensor estimates remained accurate after the change. The independent reference for each draw is released the next day, so it cannot inform the estimate issued for that draw.

**Proposed evaluation timeline.** Replay events in time order. At each hourly issue time, record the estimate using only information then available. When a reference is released the next day, match it to its draw, score the original estimate, and only then allow a supervised update for subsequent estimates. Compare frozen, one-update, and continually updated models on the same draws, with the same feedback delay and replay allowance. Plot error by draw time, marking Tuesday’s setting change and the first eligible post-change update. To assess forgetting, also score each model version on held-out pre-change draws.

**Discussion.** The histogram shift documents a distributional difference; it does not establish that the feed change caused it, that the input–property relationship changed, or that updating improves accuracy.

**摘要结果句。** 在相同的独立测试批次上，采用签发时已获得的两路原生读数和外部数值预训练的 B，平均误差低于仅用慢速读数、随机初始化的 A。

**贡献边界。** 结果支持 B 整套方案在此次比较中的优势，不能据此断言两项改动分别有效或相互增强。下游训练批次和标签相同，不等于预训练资源相同。

**图 1　最小补充设计**（同一签发时点）

| 输入方式 | 随机初始化 | 外部数值预训练 |
|---|---|---|
| 仅慢速读数 | A（已有） | C（待补） |
| 两路原生读数 | D（待补） | B（已有） |

只需补 C、D 即可检验这两个因素的交互。固定其余训练条件，核查预训练数据与测试批次无重叠。逐批配对计算预训练带来的误差降幅：慢速输入为 A−C，两路输入为 D−B；报告各降幅及其差值 `(D−B)−(A−C)` 的不确定性。只有该差值可靠地大于零，才支持正交互。要把收益进一步归于**多速率处理本身**，还需保留两路信息、仅改变采样时间处理方式的对照。

## Final reader 1

**Batch**

Introduction: Each lot passes through the dryer and then the screen, and both units log the lot, but only one outcome is recorded: pass or reject at discharge. These records can therefore support prediction of a lot’s disposition, but they do not identify which unit, if either, caused a rejection.

Candidate contribution: Test whether keeping the dryer and screen records distinct improves lot-level disposition prediction over pooling the same records without unit identity.

Proposed figure: For dryer-only, screen-only, pooled, and unit-aware predictions, plot the fraction of rejected lots predicted to pass alongside the fraction of passing lots predicted to be rejected. Use the same held-out lots, keep each lot intact, and select thresholds on validation lots by the same rule. Label any accompanying heat map “unit scores.” Calling it fault localization would require independent inspections establishing fault origin.

**Cross**

摘要结果句：在相同的独立测试批次上，使用签发前可用的两路原生采样并采用外部数值预训练的方案 B，其平均误差低于仅使用慢速读数、随机初始化的方案 A。

贡献边界：该结果支持 B 整体优于 A，不能说明两项改动各自有效或相互增强。增加一路读数也改变了可用信息，不能把输入收益直接归于采样率建模。

最少补两组：① 仅慢速读数＋预训练；② 两路原生采样＋随机初始化。四组使用相同的批次、标签、签发时点、预测头和调参预算；外部预训练数据不得包含测试批次。

建议图：横轴为输入方案，纵轴为平均误差，分别连接两种初始化下的结果。比较固定输入时预训练带来的误差降幅，并标出两种输入下降幅之差及按测试批次配对估计的置信区间，以检验增强效应。

## Final reader 2

**Introduction.** Tuesday’s feed-setting change provides a point at which to examine the soft sensor’s hourly property estimates. Each independent reference describes the property at the time of the draw but becomes available only the next day, so a histogram shift can be observed before any change in prediction error can be verified.

**Proposed evaluation.** Start the learner and a frozen baseline from the same pre-change model. On one timeline, mark the feed change, each hourly estimate, each reference release, and each update. Archive both models’ estimates using only information available at issue time. When a reference arrives, score the archived estimates for its draw; only then allow a supervised update for subsequent estimates. Report paired errors by draw time before and after the change, with pending references counted separately.

**Discussion.** The histogram shift documents a distributional difference. It does not establish that the feed change caused it, that the input–property relationship changed, or that updating would improve estimates.

**引言衔接：** 每类故障只有3次独立采集。切窗能提供更多训练片段，却不能增加独立采集次数。值得检验的是：在真实采集次数不变时，扩散增广能否改善对未见采集的诊断？

**候选贡献：** 拟仅用训练侧真实窗口拟合扩散模型，按故障类别生成补充窗口，检验其收益是否超过重复使用真实窗口。该方案尚未实施。

**划分与对照：** 先按采集划分，再切窗。每类轮流留出1次作测试，其余2次用于训练；测试仅用真实窗口。设两个对照：①仅用真实窗口；②用重复抽取的同类真实窗口等量替代生成窗口。三组使用相同分类器、批量大小和更新步数；生成器训练开销单列。

**图与报告：** 按故障类分面，横轴列三种方案，纵轴为每次留出采集的窗口诊断正确率，用线连接同一次采集的三个点。保留各次结果并等权汇总；分列真实采集数、真实窗口数和生成窗口数。结论限于未见采集，不外推至其他设备。
