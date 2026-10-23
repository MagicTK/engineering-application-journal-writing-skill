# 4.1.5 Revised-Source Writing Responses

The same respondent reread the frozen 4.1.5 instructions and answered the four original fictional requests. These are same-context responses, not a second fresh-context run. The returned prose is preserved below.

**sampling-clock-and-estimation-route**
:::writing{variant="document" id="58143"}
**Introduction Closing**
Process variables are measured every 5 s or every 20 s, while laboratory concentration assays are much less frequent. The complete-observation comparator retains only times when all variables are observed, discarding intervening measurements from the faster stream. To use these partial observations for concentration estimation, we restrict the probabilistic measurement equation and likelihood to the variables observed at each time. The resulting common latent state is linked to concentration through supervision at the available training assay times. Once trained, the soft sensor estimates concentration every 5 s from observations already received. In a held-out chronological comparison using the same source measurements and training labels, it achieves lower concentration RMSE than the complete-observation comparator.

**Contribution**
We adapt the probabilistic soft sensor through an observed-subset likelihood coupled to a supervised state-to-concentration relation. Measurements from each available variable subset inform a common latent state, which supplies the concentration estimate. This formulation retains partial observations from both acquisition streams for estimation at the 5 s decision interval.

**Methodology Opening**
The model operates directly on process measurements at their acquisition times. At each such time, the measurement equation and its likelihood include only the variables actually observed, allowing incomplete measurement vectors to inform the common latent state without constructing a filled measurement grid. During fitting, concentration supervision enters through the state-to-quality relation only at times with observed training targets. At each 5 s decision time, the trained predictor maps the state inferred from observations received up to that time to a concentration estimate, without access to the current laboratory assay.
:::
Author notes: The 20 s interval is four times as long as the 5 s interval, so its sampling rate is one-quarter as high. The contribution concerns the observed-subset likelihood and supervised output relation, not a new encoder. Lower concentration RMSE supports the estimation result, not recovery of all unobserved measurements.

**training-smoothing-and-online-filtering**
:::writing{variant="document" id="58144"}
**Abstract**
Concentration estimation from multirate process measurements requires using observations even when only some variables have been measured. Discarding incomplete observations removes information supplied between the slower sampling times. We adapt a joint observation model to the variable subset measured at each time, allowing fast and slow streams to contribute directly to state estimation. Two interacting latent components explain the measurements through the same equation. The quality-linked component has a direct concentration-output equation, while the auxiliary component represents other variation and remains involved in joint inference. During TRAIN fitting, forward-backward smoothing uses the complete training sequence, including concentration assays, to estimate latent-state moments for parameter learning. After fitting, parameters remain fixed: a forward filter uses only process observations available up to each prediction time, and the concentration head maps the estimated quality-linked state to concentration. Evaluation uses production runs disjoint from TRAIN, with TEST concentration values reserved for scoring. In this matched held-out production study, the observed-subset model achieves lower concentration RMSE than the complete-observation model, supporting its use for concentration estimation under the evaluated sampling conditions.

**Contribution**
We adapt the joint measurement equation to varying observed-variable subsets, so that partial observations from both sampling streams contribute to inference of the interacting latent states. The concentration estimate uses the quality-linked state, while the auxiliary state continues to account for other measurement variation within the same inference process. The matched held-out comparison demonstrates lower concentration RMSE relative to the complete-observation model.
:::
Author notes:
- The abstract contains 176 whitespace-delimited words, counting hyphenated compounds as one. Full-sequence TRAIN smoothing supports parameter learning; prediction uses fixed parameters and forward filtering without TEST assays.
- Novelty rests in the observed-subset adaptation. The auxiliary state remains active in inference, and the reported benefit is concentration estimation accuracy, not control or deployment performance.

**completed-batch-bidirectional-analysis**
:::writing{variant="document" id="58145"}
**Motivation**
Final quality classification is performed after a production batch has finished, when the measurement sequence from every temporal stage is available. The reference method uses only the batch-end measurement vector, so its input does not directly represent response changes across those stages. These changes motivate a representation that captures within-batch temporal variation while retaining its association with the known stages. The proposed aggregation scheme summarizes the encoded sequence according to this stage organization and fuses the resulting summaries for final batch quality classification.

**Methods Opening**
At batch completion, a standard bidirectional sequence encoder processes the full measurement sequence in both temporal directions. Its output representations are aggregated within the known temporal stages, and the resulting stage summaries are fused to predict one final quality class for the batch. Both encoding directions therefore operate on measurements already available when the classification is performed. Training and test sets contain independent complete batches, and final inspection labels for test batches are used only to score the predictions.
:::
作者说明：判定时点明确为批次结束，因此双向编码使用的是决策时已经完整采集的数据，无须删除反向编码器。贡献落在已知时间阶段与序列表示之间的聚合方式，现成编码器仅作为支撑组件；删除了因果预警和逐时刻报警的错误含义，未添加性能结论。

**trailing-window-attention**
> Unmasked attention integrates information across all positions in the completed trailing window, from \(t-L+1\) through \(t\), for window-level condition classification. The classifier maps the pooled representation to one condition label for the completed window.

No attention-mask change is required: the single prediction uses a window fully available by \(t\). It does not provide position-level fault localization, and computation latency is unspecified.

## Additional Post-Freeze Request

The following fictional completion-route request was authored after the instruction freeze and answered in the same context. It is not a fresh-context test. The response is preserved as returned.

**past-only-completion-with-age-aware-gating**
:::writing{variant="document" id="68219"}
**Method Overview**
At each 1 s decision time, the input grid carries forward each slower sensor’s most recently received measurement, accompanied by an observation indicator and the elapsed time since that measurement was acquired. A feature gate uses these measurement ages and observation indicators to modulate the features supplied to a regression head, which estimates the current concentration. Training and testing use the same input construction and gating operations, with prediction inputs restricted to information available by the decision time and excluding the current concentration assay.

**Contribution**
- We introduce feature gating conditioned on measurement age and observation indicators for concentration estimation from carried-forward measurements. An ablation using the same training and test data shows lower concentration error than gating that ignores measurement age, supporting the contribution of age information to the evaluated prediction task.
:::
Author note: The carried-forward input construction is preserved, and novelty is assigned to the gate. The ablation supports concentration estimation accuracy, not missing-value reconstruction; an observed-subset likelihood would misdescribe the implemented method.
