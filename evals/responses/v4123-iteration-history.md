# Whole-Passage Iteration History

These are actual unedited fictional-case responses, not approved manuscript templates. No private manuscript was used.

## Initial v4.1.22 Response

**PROSE-A**
:::writing{variant="document" id="64183"}
**Introduction Closing**
Method [A] performs supervised regression on complete fixed time grids, while [B] uses measurement reconstruction to learn from unlabeled windows and supplies its predictor with an imputed complete grid. Both report favorable results in their respective settings. For the continuous crystallization process considered here, the requirement is to estimate product concentration from observations already available at prediction time while learning from infrequent, delayed assays. We investigate direct prediction from individual observations and their timing, together with shared-encoder training that uses measured values even when the corresponding concentration labels have not yet returned.

**Motivation and Formulation**
The process records 12 variables at sampling intervals of either one or five minutes. Laboratory assays correspond to samples taken approximately every two hours, with concentration labels available 40 minutes after sampling. Consequently, estimating concentration at sampling time \(t\) requires distinguishing when a measurement was acquired from when it became accessible. Define the available observation collection as
\[
\mathcal{O}_t=\{(i_j,v_j,s_j,a_j):t-10\,\mathrm{min}\leq s_j\leq t,\ a_j\leq t\},
\]
where \(i_j\), \(v_j\), \(s_j\), and \(a_j\) denote the variable identifier, measured value, acquisition time, and arrival time of observation \(j\). Multiple readings of the same variable remain separate observations, without completing a regular grid. The task is to estimate concentration \(y_t\) from \(\mathcal{O}_t\) at time \(t\); its assay label becomes available for learning only at \(t+40\,\mathrm{min}\).

**Method Overview**
A shared encoder represents each observation using its variable identifier, measured value, and elapsed time since acquisition. A learned weighting function uses these features to assign weights to the available observations. Their weighted aggregation supplies a regression head that predicts concentration. During training, an auxiliary decoder reconstructs actually measured values from encoded features, allowing windows without returned concentration labels to contribute to encoder learning. The regression loss uses only labels already available. The decoder and reconstruction loss are absent from the prediction path. At inference, all model parameters remain fixed, while aggregation weights vary with the input through the learned weighting function.

**Contributions**
1. We develop a concentration estimator that directly aggregates available observations with their variable identities, values, and acquisition-time intervals. This representation accommodates multiple readings per variable without requiring an imputed complete grid.
2. We combine concentration regression and measured-value reconstruction through a shared encoder. Returned assay labels supervise the regression task, while windows lacking those labels contribute through reconstruction, retaining a prediction path that requires only the encoder, weighting function, and regression head.

**Conclusion**
The proposed estimator combines direct use of available process observations with shared-encoder training for concentration estimation in continuous crystallization. Evaluation used 40 earlier production batches for training and 20 later, completely held-out batches from the same line, with all data-processing parameters fitted on training batches alone. Test replay respected observation availability, and subsequent assays were used only for scoring, without model updates. Across five independent training runs, mean concentration MAE was 0.54, compared with 0.68 for [A] and 0.61 for [B], in the same unit. Removing the acquisition-time interval increased MAE to 0.60, supporting the value of timing information within this estimator. These findings establish lower mean estimation error on the evaluated later batches from the studied production line.
:::

**PROSE-B**
:::writing{variant="document" id="90726"}
**Introduction Closing**
In the production system considered here, measurement distributions change over time, whereas operator-verified labels become available only 48 hours after the corresponding samples arrive. Source [C] reports diagnostic performance using a fixed historical classifier, and [D] studies incremental classification with promptly available labels. These studies provide reference settings for examining how diagnosis can retain a historical decision function while incorporating supervision that arrives after the measurements it describes. We combine a frozen historical classifier with a transformation and classifier updated from returned labels, and examine the resulting diagnostic performance and false-alarm rate under chronological replay.

**Problem Formulation**
Each arriving sample \(x_t\in\mathbb{R}^{20}\) contains 20 process measurements and belongs to one of six known classes. Its diagnosis must use the parameters available before updates at time \(t\), and the resulting output is permanently stored for scoring. Supervised learning can subsequently use older samples only when at least 48 hours have elapsed and their verified labels have returned. Samples awaiting labels are buffered without unsupervised updates. The resulting task is sequential six-class diagnosis under changing measurement distributions, with delayed supervision and a prediction-before-update ordering.

**Method Overview**
The historical classifier \(h_0\) is trained offline and then frozen. A second path applies a learnable transformation \(T\) before an updatable classifier \(h_1\). At time \(t\), their outputs are combined as
\[
p_t=0.4\,h_0(x_t)+0.6\,h_1(Tx_t),
\]
using the current parameters of \(T\) and \(h_1\) and fixed mixture weights. After saving \(p_t\), the method updates only \(T\) and \(h_1\) using eligible older samples whose labels have returned. The historical path therefore retains its original decision function, while the second path incorporates newly available supervision. Updates depend on label availability rather than each new measurement; there is no separate drift-detection step.

**Contributions**
1. We integrate a frozen historical diagnostic path with a transformation and classifier updated from delayed, verified labels. The integration retains the historical model’s contribution to each prediction while allowing the second path to learn under the 48-hour supervision constraint. The substantive adaptation concerns these complementary learning roles and their update timing; the output combination uses a fixed weighted sum.

**Results Discussion**
Chronological comparisons were conducted on a process benchmark and historical production-line measurements, with models fitted separately for each case. In the production-line replay, mean macro-F1 was 0.78 for the proposed method, 0.71 for the fixed historical baseline, and 0.76 for the incremental control following the same 48-hour label rule. Normal-sample false-alarm rates were 2.4%, 1.6%, and 2.0%, respectively. Thus, the 0.02 macro-F1 gain over the matched incremental control accompanied a 0.4-percentage-point increase in false alarms. Higher aggregate diagnostic performance therefore came with more normal samples being flagged. Scoring used the original stored predictions, preserving the information available when each diagnosis was made.

**Conclusion**
Combining a retained historical classifier with a path updated from delayed labels provides a way to incorporate new supervision without modifying the historical model. Production-line replay showed higher mean macro-F1 than the evaluated baselines, together with a higher false-alarm rate on normal samples. The findings support a specific trade-off between diagnostic performance and false alarms under delayed supervision. Prospective evaluation would need to determine whether that trade-off is acceptable when the predictions are used in production.
:::

**作者备注**
- 两组均为独立虚构案例写作；数值完全来自题设，本次未开展实证实验。[A]–[D] 均为虚构引用占位。
- A：浓度单位未提供，未自行补造；时间输入消融不等于单独验证了重构辅助训练的收益。
- B：基准具体数值缺失，因此未判断其性能排序；两组案例分别拟合，不表述为同一模型跨厂迁移。
- 两组均无显著性结论，正文未将均值差异写成统计显著改善，也未声称已上线部署或取得经济收益。

## First v4.1.23 Candidate Response

**PROSE4123-A**

:::writing{variant="document" id="41231"}
**Introduction**
Supervised regression on a complete, fixed temporal grid has produced good results in [A]. Method [B] also exploits unlabeled windows through measurement reconstruction, while supplying its predictor with an imputed complete grid. These achievements motivate a different input treatment for continuous crystallization, where concentration must be estimated from measurements available at the prediction time and assay supervision is infrequent. We investigate direct estimation from time-stamped observations, coupled with shared-encoder training that uses measured values when concentration labels are unavailable. Evaluation uses 40 earlier production batches for training and 20 later, fully held-out batches from the same line; all data-processing parameters are fitted using the training batches alone.

**Problem Formulation**
The crystallization process provides 12 variables sampled at intervals of one or five minutes. Laboratory samples are collected approximately every two hours, and their concentration labels become available for learning 40 minutes after collection. To estimate concentration at time \(t\), the input comprises measurements acquired within the preceding ten minutes and received by \(t\). Writing each observation as its variable identifier \(j_i\), value \(v_i\), acquisition time \(s_i\), and arrival time \(a_i\), the task is
\[
\widehat c_t=f_\theta(\mathcal O_t),\qquad
\mathcal O_t=\{(j_i,v_i,s_i,a_i):t-10\,\mathrm{min}\le s_i\le t,\ a_i\le t\}.
\]
Multiple observations of the same variable remain separate entries. This formulation retains the available measurement history without requiring a complete grid. The target is concentration at \(t\), although its assay label can supervise learning only after its subsequent return.

**Method Overview**
A shared encoder represents each available observation using its variable identifier, measured value, and elapsed time \(t-s_i\). The elapsed time locates the measurement relative to the concentration being estimated. A learned weighting function uses these features to assign observation weights, and their weighted aggregation supplies a regression head that predicts concentration. During training, an auxiliary decoder reconstructs actually measured values from encoded features, allowing windows without returned concentration labels to contribute to encoder learning. The regression loss uses only concentration labels already returned. Reconstruction supplies an additional training signal; it neither fills unmeasured entries nor participates in prediction. At prediction time, the encoder, weighting function, and regression head have fixed parameters, while the aggregation weights vary with the input observations.

**Contributions**
- A concentration estimator operates directly on the available observations within a recent window, combining variable identity, measured values, and elapsed acquisition times through learned weighted aggregation. It retains repeated measurements without first imposing a complete temporal grid.
- Shared-encoder training combines regression on returned assay labels with reconstruction of measured sensor values. This arrangement incorporates windows lacking available concentration labels into training while retaining an observation-to-concentration prediction path without the auxiliary decoder.

**Conclusion**
This study addresses concentration estimation in continuous crystallization using available time-stamped measurements and shared-encoder training under sparse assay supervision. In time-availability replay, with subsequent assays used only for scoring and no model updates, mean MAE across five independent training runs was 0.54, compared with 0.68 for [A] and 0.61 for [B]. Removing elapsed-time inputs increased MAE to 0.60, supporting their contribution to estimation in this setting. The findings establish lower average error on later held-out batches from the studied line. Prospective evaluation and additional production sites remain necessary to assess performance beyond this setting.
:::

中文作者备注：[A]、[B]仅为虚构引用占位。未提供方差或显著性检验，也未提供重构项的独立消融，因此不将均值差异写成显著提升，不单独宣称重构训练带来了已验证的精度增益。

**PROSE4123-B**

:::writing{variant="document" id="41232"}
**Introduction**
The fixed historical classifier studied in [C] provides evidence for diagnosis using previously learned relationships, while [D] investigates incremental classification when labels are promptly available. In the production system considered here, measurement distributions change over time, but operator-verified labels reach the model only 48 hours after sample arrival. This delay separates the need to diagnose current measurements from the opportunity to learn from their outcomes. We therefore combine a frozen historical classifier with a transformation and classifier updated from returned labels. The historical path contributes to every prediction, while delayed feedback modifies the second path as supervision becomes available.

**Problem Formulation**
Each arriving sample \(x_t\in\mathbb R^{20}\) contains the process variables used to distinguish six known classes. Diagnosis must use the model state available at arrival; the sample's label becomes eligible for learning only after the 48-hour delay and its return. Samples awaiting labels are stored without driving unsupervised updates. The task is sequential classification under changing measurement distributions and delayed supervision, with performance assessed from the predictions originally issued for each sample rather than predictions regenerated by a later model.

**Method Overview**
The historical classifier \(h_0\) is trained offline and subsequently frozen. The second path applies a learnable transformation \(T\) before classification by \(h_1\). Using the parameters available when \(x_t\) arrives, the model computes
\[
p_t=0.4\,h_0(x_t)+0.6\,h_1(Tx_t).
\]
The mixing weights remain fixed. This prediction is permanently recorded before any update at time \(t\). Only then are \(T\) and \(h_1\) updated using older samples whose labels have returned after the required 48-hour wait, according to the objectives defined in the method subsections. The historical classifier remains unchanged. Learning is therefore triggered by the availability of eligible supervision, not by each new measurement, and it does not require a separate drift-detection decision.

**Contribution**
- A diagnostic model integrates a fixed historical prediction path with a learnable transformation and classifier updated under delayed supervision. The arrangement retains the historical classifier's contribution while allowing the second path to incorporate returned labels, with prediction and subsequent learning explicitly separated for each arriving sample.

**Results Discussion**
Evaluation used chronological replay of a process benchmark and historical production-line records, with models fitted separately for the two cases. On the production line, mean macro-F1 was 0.78 for the proposed method, compared with 0.71 for the fixed historical baseline and 0.76 for the incremental control operating under the same 48-hour label rule. The corresponding false-alarm rates on normal samples were 2.4%, 1.6%, and 2.0%. Thus, the higher macro-F1 was accompanied by more frequent incorrect alarms during normal operation. Comparison with the delayed-label incremental control supports an improvement in the reported classification metric under matched feedback timing, but also identifies an additional false-alarm cost. Whether this balance is acceptable depends on operational requirements that historical classification scores alone cannot resolve.

**Conclusion**
Combining a frozen historical classifier with a transformation and classifier updated from delayed labels provides a way to revise diagnosis while retaining a fixed historical contribution. Production-line replay showed higher mean macro-F1 than both evaluated controls, together with a higher false-alarm rate. These findings support the approach within the evaluated delayed-feedback setting and identify its principal measured trade-off. Prospective evaluation is needed to determine whether that balance is suitable for operational monitoring.
:::

中文作者备注：[C]、[D]仅为虚构引用占位；普通加权求和不单列为算法创新。基准具体数值及显著性结果未提供，正文不推定其比较结论；两组案例分别拟合，不能解释为同一组权重跨工厂迁移。

**PROSE4123-C**

:::writing{variant="document" id="41233"}
This study evaluated sliding-window anomaly detection using a model trained on 19 normal production batches. The detector flagged 69 of 72 windows in one fault batch, with a window-level false-alarm rate of 2% across 480 windows from five normal batches. These findings characterize performance on the evaluated records. Overlapping windows are not independent batch replicates, and the single fault batch limits conclusions about broader fault coverage. Additional fault batches, external production lines, and prospective evaluation are needed to assess wider applicability.
:::

中文作者备注：不采用学生原句。“Batch-level fault diagnosis”改变了任务与输出粒度；“reliable … in industrial production”超出了单故障批次、窗口级测试的证据范围。
