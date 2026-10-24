# Final Frozen-Candidate Response

Actual response to three fictional requests. Numerical results and citations are supplied fictional facts; this is not scientific validation or an approved universal writing template.

**PROSE4123-A**

:::writing{variant="document" id="41231"}
**Introduction**

Methods [A] and [B] provide two useful starting points for concentration estimation: supervised regression on complete fixed time grids and learning from unlabeled windows through measurement reconstruction, respectively. Both report good results under their evaluated settings, while the predictor in [B] also receives an imputed complete grid. For continuous crystallization, the requirement examined here is to estimate product concentration directly from observations available at the prediction time, preserving their measurement times. We therefore combine observation-level features with shared-encoder training so that measured values in windows awaiting assay labels can also contribute to learning.

**Motivation and Problem Formulation**

Twelve process variables are sampled at intervals of either 1 or 5 min, whereas concentration assays correspond to sampling times approximately 2 h apart and become available for learning 40 min later. At prediction time \(t\), define \(\mathcal{O}_t=\{(j,v,s,a):t-10\,\mathrm{min}\leq s\leq t,\ a\leq t\}\), where \(j\), \(v\), \(s\), and \(a\) denote the variable identifier, measured value, acquisition time, and arrival time. The task is to estimate concentration \(y_t\) from \(\mathcal{O}_t\). Multiple observations of one variable are retained, without filling the window into a complete grid. During training, a concentration target becomes eligible for supervision only after its assay result has returned.

**Method Overview**

Each available observation is encoded using its variable identifier, value, and elapsed time \(t-s\). A learned weighting function uses these features to aggregate the encoded observations within the window, and a regression head maps the aggregate to concentration. The elapsed-time input distinguishes measurements acquired at different times even when they belong to the same variable. An auxiliary decoder uses the encoded features to reconstruct measured values. This reconstruction objective trains the shared encoder on windows whose concentration labels have not returned, while the regression loss uses only returned assay labels. The decoder is used only for training and does not complete unmeasured entries. Prediction uses the encoder, weighted aggregation, and regression head with fixed parameters; the aggregation weights nevertheless vary with the input observations.

**Contributions**

- Observation-level concentration estimation incorporates variable identity and measurement timing into a learned weighted summary of available readings, allowing unevenly sampled windows to be processed without constructing a complete input grid.
- Shared-encoder training couples concentration regression on returned assay labels with reconstruction of measured values in unlabeled windows, extending the training information available for the estimator without adding a reconstruction step to prediction.

**Conclusion**

The proposed approach estimates product concentration in continuous crystallization from available, time-stamped observations while using unlabeled measurement windows during training. In chronological replay of later, held-out batches from the same production line, its mean concentration MAE over five independent training runs was 0.54, compared with 0.68 for [A] and 0.61 for [B]. Removing elapsed time increased MAE to 0.60, supporting its contribution to estimation in this setting. The results show lower mean estimation error in this same-line evaluation; prospective validation is needed to assess performance during live operation.
:::

作者备注：实验设置节应保留“前40批训练、后20批完全留出、处理参数仅由训练批次拟合、测试化验仅计分且不更新模型”。未提供方差或显著性检验，不使用显著改善表述；[A][B]仅为虚构引文代号。

**PROSE4123-B**

:::writing{variant="document" id="41232"}
**Introduction**

Study [C] reports diagnostic performance with a classifier trained on historical data, whereas [D] investigates incremental classification when labels are promptly available. These approaches establish complementary reference points for retaining learned diagnostic information and incorporating new supervision. In the system considered here, operator-verified labels reach the model 48 h after their samples, so the newest measurements cannot immediately support supervised updates. This study combines a frozen historical classifier with a learnable transformation and an updatable classifier, examining whether their combination improves diagnosis under delayed feedback and how it affects false alarms.

**Problem Formulation**

The task is to assign each vector \(x_t\in\mathbb{R}^{20}\) to one of six known classes as it arrives, while the measurement distribution changes over time. Its prediction must use the parameters available before any updates at \(t\). Subsequent learning may use only earlier samples whose 48 h waiting period has elapsed and whose labels have returned. Each original prediction remains the scoring output after later model updates.

**Method Overview**

The historical classifier \(h_0\) is trained offline and then frozen. The second path applies a learnable transformation \(T\) to \(x_t\) before classification by \(h_1\). Their outputs are combined as \(p_t=0.4h_0(x_t)+0.6h_1(Tx_t)\), with fixed mixing weights. The prediction is saved before any update at \(t\). Eligible older labeled samples are then used to update \(T\) and \(h_1\). Samples awaiting labels are buffered without driving updates. Learning is therefore triggered by the availability of eligible labeled samples, rather than by measurement arrival alone.

**Contribution**

- We combine a frozen historical classifier with an updatable transformation and classifier under a prediction-before-update sequence. This design retains a fixed historical contribution to each six-class decision while allowing returned labels to change the second path under the 48 h feedback constraint.

**Results and Discussion**

In historical replay of the production line, the proposed method achieved a mean macro-F1 of 0.78, compared with 0.71 for the fixed historical baseline and 0.76 for the incremental control operating under the same 48 h label rule. The macro-F1 improvement was accompanied by a normal-sample false-alarm rate of 2.4%, exceeding the respective baseline rates of 1.6% and 2.0%. Thus, the gain in average class-wise diagnostic performance came at the cost of more false alarms on normal samples. Whether this trade-off is acceptable depends on the intended alarm-handling requirements. The process benchmark and production-line comparisons used separately fitted models and chronologically preserved predictions, so they examine the learning procedure in two settings rather than transfer of one fitted model between them. The available means do not establish the statistical significance of the differences.

**Conclusion**

Combining a retained historical classifier with updates from delayed labels supports fault diagnosis as measurement distributions change. Production-line replay yielded higher mean macro-F1 than the evaluated alternatives, together with a higher false-alarm rate. The retrospective findings support this combination as an option for diagnosis with 48 h feedback, with its suitability for live operation depending on prospective evaluation of the observed trade-off.
:::

作者备注：保留一个实质贡献条目，不将普通加权求和另列为创新。未给出基准数值，正文仅说明已完成比较，不推断其效果方向；[C][D]仅为虚构引文代号。

**PROSE4123-C**

:::writing{variant="document" id="41233"}
Using 19 normal production batches for training, the method detected 69 of 72 windows in the single fault batch evaluated. The window-level false-alarm rate was 2% across 480 windows from five normal test batches. These results support sliding-window anomaly detection in the evaluated records. The overlapping windows do not constitute independent batch-level repetitions, and the fault evidence comes from one batch. Additional fault batches and external-line evaluation are needed to assess broader applicability before field deployment.
:::

作者备注：原句应替换。它将窗口级异常检测扩大为批次级故障诊断，而单个故障批次也不足以支持全面可靠性的结论。
