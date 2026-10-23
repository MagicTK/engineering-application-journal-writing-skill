# 4.1.4 Baseline: Observation And Prediction Writing

One fresh responding context used the frozen 4.1.4 instructions for four fictional author requests. The response below is preserved as returned. It is a writing trace, not a scientific finding or independent score.

**sampling-clock-and-estimation-route**
:::writing{variant="document" id="58143"}
**Introduction Closing**
Concentration estimation in this process must reconcile 5 s and 20 s measurement intervals with much less frequent laboratory assays. The complete-observation comparator uses only times at which all process variables are measured, leaving intermediate measurements unused. We adapt the observation likelihood to the variables actually measured at each time, allowing partial observations to contribute directly to a common latent state. Available training assays supervise the relation between this state and concentration. The trained predictor then estimates concentration every 5 s using observations received by each decision time. In a held-out chronological comparison using the same source measurements and training labels, this approach achieves lower concentration RMSE than the complete-observation comparator.

**Contribution**
We introduce an observed-subset likelihood coupled to a supervised state-to-concentration relation. The likelihood incorporates the variables measured at each time directly into estimation of a common latent state, retaining partial observations from both sampling streams for concentration estimation at 5 s decision times.

**Methodology Opening**
The soft sensor estimates concentration at each 5 s decision time from process observations received up to that time. At each observation time, the measurement equation is restricted to the variables actually measured, and their values contribute to the likelihood used to infer the common latent state. Fitting and prediction operate directly on these observed subsets, without first completing a measurement grid. During training, concentration targets supervise the state-to-concentration relation only at their observed times. During prediction, the trained relation maps the estimated state to concentration without access to the current laboratory assay.
:::
Author notes: The 20 s stream has a fourfold longer sampling interval and one-quarter of the 5 s stream’s sampling rate. The revision replaces unsupported sample-recovery claims with direct observed-subset inference and locates the contribution in the likelihood and supervised relation, not a new encoder or the act of conducting experiments.

**training-smoothing-and-online-filtering**
:::writing{variant="document" id="58144"}
**Abstract**
Industrial concentration estimation must use process measurements acquired at different rates, which leave different subsets of variables observed at successive times. Restricting estimation to complete observations excludes available measurements from faster streams. We adapt a joint latent-state observation model to the subset measured at each time, allowing both fast and slow streams to contribute directly to concentration estimation. Two interacting latent components jointly explain the process measurements: one has a direct concentration-output relation, while the auxiliary component represents other variation and participates in joint state inference. During training, forward-backward smoothing uses the complete TRAIN sequence, including its concentration assays, to estimate latent-state moments for parameter learning. With parameters fixed, a forward filter processes available process observations up to each prediction time, and the concentration head maps the estimated quality-linked state to concentration. Evaluation uses production runs disjoint from TRAIN; TEST concentration values enter only the subsequent scoring. A matched held-out production comparison yields lower concentration RMSE than the complete-observation model, supporting the observed-subset formulation for quality estimation under the evaluated acquisition conditions.

**Contribution**
An observed-subset formulation adapts the shared measurement equation to fast and slow sampling streams, allowing both to inform the interacting latent states without discarding incomplete observations. The quality-linked state supplies the concentration estimate, while the auxiliary state helps explain the same process measurements during joint inference. A matched held-out production comparison supports this adaptation through lower concentration RMSE than the complete-observation model.
:::
Author notes:
- The abstract contains 172 whitespace-delimited words, counting hyphenated compounds as one. Full-sequence smoothing is confined to TRAIN parameter learning; TEST predictions use fixed parameters and forward filtering.
- Novelty is confined to the observed-subset adaptation. The auxiliary state remains active, and the measured benefit concerns concentration RMSE, not control performance or deployment.

**completed-batch-bidirectional-analysis**
:::writing{variant="document" id="58145"}
**Motivation**
Final batch quality is assessed here after production has ended and the complete measurement sequence is available. The verified comparison approach classifies quality from the batch-end measurement vector, which does not directly represent response changes across the batch’s temporal stages. These changes motivate a representation that captures within-batch temporal variation and organizes it according to the known production stages. The proposed aggregation scheme summarizes the encoded sequence within each stage and fuses the stage summaries into a representation for final quality classification.

**Methods Opening**
Each input sample is the complete measurement sequence of one finished production batch. A standard bidirectional sequence encoder processes this sequence in both temporal directions. The resulting representations are aggregated according to the known temporal stages, and the stage summaries are fused to produce one final quality-class prediction for the batch. All measurements used by the encoder are available when this prediction is made. Training and testing are separated by complete, independent batches, and final inspection labels for test batches are used only to score the predicted classes.
:::
作者说明：任务恢复为批次结束后的最终质量分类。此时完整测量序列已可用，双向编码并未使用该决策时点之后的信息，无须删除反向编码器。贡献限定为按已知时间阶段聚合序列表示；删除了因果预警和逐时刻报警的错误含义，未新增性能结论。

**trailing-window-attention**
> Unmasked attention combines information across the completed trailing window, from \(t-L+1\) through \(t\), for window-level condition classification. The classifier maps the pooled representation to one condition label for the completed window.

No attention-mask change is required: all inputs are available by \(t\), and the output concerns the completed window. Position-level fault localization and instantaneous computation are unsupported.
