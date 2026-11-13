# 4.4.1: partial references and conditional comparisons

Four fictional cases were distributed across two fresh reading contexts. No actual manuscripts, evaluations or study records were available to the responders. The first A answer called a recorder gap a filter-press outage, which could be read as production downtime. The first C concluded that all crossed cells were necessary without first checking where the old recipe ran. B and D handled unverified exposure and unit-level findings. The reference guide was amended in both languages to preserve the identity of the object and to distinguish conditional contrasts from a full interaction. Both original exercises were rerun without extra hints in two new contexts. The report records the fingerprint of that revision.

A and B pass narrowly: only the overlapping probe samples are a natural-outage reference; workload and detection of verified events do not establish total sensitivity or false alarms. C and D pass: recipe comparisons depend on observed cells and target telemetry precludes a source-only claim; teardown supports unit-level evaluation only. Alarm time plotted below would need to be available. A question in a motivation sentence is a stylistic option, not a required or universally preferred format. The demonstration is not clinical validation, independent reproduction of a paper or evidence about every pair of method and task.

## Final responses

**Introduction transition.** An isolated missing vibration reading leaves nearby measurements on both sides; a prolonged filter-press recorder outage can conceal an entire transient. A reading taken after recording resumes may help reconstruct the trace, but it was unavailable when an operator needed an alarm. Retrospective recovery and alarm timeliness therefore require separate tests.

**Comparison design.** Split by press run before fitting or scaling. In intact held-out runs, hide random points and contiguous blocks of outage-like lengths at matched missing fractions. Compare the candidate with centered linear interpolation on identical masks, allowing both access to later readings. Report mean absolute error against withheld measurements in sensor units, separately by mask type and block length. For real outages, keep the independent probe out of all estimators; document alignment, calibration uncertainty and overlap duration. Score only overlapping samples in each of the two covered gaps, separately from artificial masks. For alarms, replay runs using only readings available by each decision deadline; compare with holding the last reading. Timeliness requires independently timed events and a stated deadline.

**Figure 1 (planned).** (a) Reconstruction error for withheld points and blocks. (b) Nine real outages: dashed estimates and independent probe readings only where available. The probe covers parts of two gaps on one shift; the remaining seven have no reference for estimating recovery error.

**给作者的修改建议。** 请将“具名故障诊断”改为“异常评分，用于筛选待复核时段”。未标注不等于正常。全档案拟合所得分数只能描述这批记录；可展示已核实事件附近的分数变化，不能据此声称能检出新事件或识别故障类型。

**最小公平评价。** 按时间将完整运行段分为训练、校准、盲测三部分，窗口不跨界。仅用训练段重新拟合预处理和评分模型；在独立校准段按预先约定的分位数定阈值并锁定，不在测试集上最大化 F1。该分位数只限定校准段的超阈比例，不是误报概率。预先规定连续报警的合并规则和事件匹配时间窗，在盲测段逐一匹配已核实事件，报告命中数、漏检数及每百运行小时的报警次数。未匹配报警不等于误报；缺少经核实的无事件时段，不能估计误报率。事件记录不全，命中比例也仅适用于已核实事件；具名诊断另需独立核实的故障类型标签。

**C. 研究动机**
源域运行记录封存后，新配方仅在新机组上运行，泵故障诊断首先需要回答的是：利用调参阶段可见的目标域遥测，能否改善已知故障在这一工况下的识别？
对于标为“不属于任何已知类”的运行片段，诊断目标是将其拒识；这些标记不提供未知故障的名称或属性，因而不能用于验证具体故障类型的零样本识别。

**拟议实验**
按独立运行批次划分目标域调参集与测试集。从同一源模型出发，比较冻结模型与仅用无标签目标遥测调参的模型；测试前锁定各自的拒识阈值，测试标签和未知标记仅用于评分。按“配方×机组×已知或未知”列出批次数，区分未观测与未核实。对有参考标签的已知类报告各类正确识别率和误拒率，对经核实的未知样本报告拒识率。若旧配方也在新机组运行，可在新机组内比较配方，并在旧配方下比较机组，前提是其余条件可比；若只有新旧两种配方与机组的成对组合，则只报告联合变化，不拆分增益。缺少交叉组合时不估计交互效应。

**D. Contribution boundary**
Both branches rank bearing temperature highly, making it a candidate for inspection. Their agreement is not independent evidence of fault origin. Teardowns identified the lubrication pump as the failed unit in three incidents; none established which sensor responded first. For late-starting records, the first visible change cannot establish the response order.

**Proposed figure.** Show both branches’ sensor ranks beside time-aligned traces for each incident. Mark recording start, alarm time and unavailable prehistory. In a separate column, show the teardown finding at unit resolution or “not verified,” without drawing a causal arrow from sensor to pump.

**Falsifiable comparison.** In held-out incidents, mask the jointly favored sensor and a control sensor matched for variability and missingness, using the same replacement rule and time window. A no-larger paired drop in alarm score would not support preferential model reliance; even a larger drop could reflect unrealistic masked inputs. Separately, prespecify a justified sensor-to-unit mapping and compare the combined ranking with each branch alone by the confirmed pump’s rank among eligible units. Report all three ranks, candidate counts and verification coverage; exclude unverified alarms from accuracy calculations.
