## v411-generalization-and-refitting

**Minimal replacement**

“Randomly held-out independent production batches assess predictive generalization to new batches from the stated population within each case. The same algorithm is fitted separately in the two plants, rather than transferring a single trained model between them.”

The original first sentence is too categorical. Given the stated batch independence and absence of overlap or selection leakage, these are valid out-of-sample evaluations of within-population generalization. Random allocation does not invalidate that evidence. Without numerical results, however, the evaluation design alone cannot establish how well either fitted model generalizes or whether it outperforms a comparator.

The original second sentence confuses reuse of a method with transfer of fitted parameters. What is established is that the same algorithm was fitted and independently evaluated in two cases. Neither transfer of one fitted model between plants nor performance under untested population shifts is established. Cross-site experiments are not needed to describe the existing tests accurately; they would be relevant only if the author retained a cross-site transfer claim.

## v411-cross-case-reversal

**可讨论的英文综合分析**

The matched comparisons show a reversal in the observed benefit of the weighting mechanism across the two separately trained cases. For fault classification in Case A, including the mechanism increases mean macro-F1 from 81% to 84%, a gain of 3 percentage points. For concentration soft sensing in Case B, it increases mean MAE from 0.40 to 0.44 g/L, a deterioration of 0.04 g/L. Together, these results identify a boundary to the mechanism's usefulness: the reported means favor its inclusion for the classification case and its removal for the concentration-estimation case. This makes the mechanism a case-specific design choice whose value must be judged against the engineering prediction target, rather than a uniformly beneficial addition. The two task metrics do not define a common overall improvement. The comparison concerns reuse of a method with separately fitted parameters, not transfer of one trained model; the available means establish neither the consistency of the differences across runs nor why their directions reverse.

**简短理由：** 综合结论应落在“同一设计在不同案例中的适用边界”，而不是强行统一成正收益。macro-F1 与 MAE 的目标、单位和优劣方向不同，不能直接平均，改成相对百分比也不会自动产生共同的工程效用尺度；均值不能证明运行间稳定性或显著性，B 的较高误差也不能证明产线噪声更大。

## v411-positive-discussion

**可讨论的英文 Results/Discussion（两段）**

On independent held-out batches, the new model's error advantage was confined to the low-flow condition: its mean MAE was 0.42 g/L, compared with 0.55 g/L for the comparator, a reduction of 0.13 g/L. Under routine flow, the ordering reversed, with mean MAEs of 0.39 and 0.37 g/L, respectively. The engineering significance is therefore condition-specific: the new model offers lower observed concentration-estimation error at low flow, while the comparator retains an error advantage under routine flow. These results make the relative importance of the two operating conditions central to model choice; they do not identify an overall winner without an application-specific weighting of those conditions. The available means describe this performance pattern, but do not establish its statistical reliability or attribute it to an isolated mechanism.

The low-flow error advantage comes with a computational cost. Including preprocessing, inference took 12 ms for the new model and 5 ms for the comparator on the same target CPU. Both reported times fall below the 20 ms decision deadline, leaving margins of 8 and 15 ms, respectively. Thus, the new model trades 7 ms of additional computation for its observed low-flow error reduction while remaining within the stated budget in this measurement; the comparator is faster and also has the lower reported error under routine flow. The extra computation may therefore be worthwhile when low-flow estimation is the priority, but it provides no measured accuracy advantage in routine flow. Because timing was measured offline on historical data without production-line integration, this supports timing feasibility for the measured preprocessing-and-inference workload, not a live deadline guarantee or demonstrated improvements in control, downtime, or profit.

## v411-approved-figure-scope

**这句话没有可据现有信息认定的明确问题，可以保留：**

“The confusion matrix shows the class-pair errors for the test samples.”

它描述的是混淆矩阵在分类评价中的正常用途，没有据此宣称机理、因果关系或未测性能。逐类 F1 表概括各类的预测表现，混淆矩阵则可呈现真实类别被误判为哪些其他类别及其方向；两者的信息粒度不同，存在逐类 F1 表并不自动构成重复证据。

**下一步不删混淆矩阵，也不移动流程图。** 作者已明确保留混淆矩阵、流程图、表格指标与字号；当前 12 页以及本轮文字检查都不是压页或调整图序的授权。所给句子也没有提供必须改变图序的理由。后续仍限定在文字层面，仅在出现具体不一致时核对术语、图号与评价对象，不为这一句扩大修改范围。

以上只是对句义和修改范围的判断。未提供图、PDF 或源码，因此不能判断图中数值、标注、可读性或实际排版是否正确，也没有核验这些内容。

## v411-single-requirement-conclusion

No. One engineering requirement can motivate several cooperating operations. The number of components does not determine the number of challenges or independent contributions, and a familiar prediction task can still support a substantive methodological advance. Keep the accurate short abstract and the conclusion; neither needs padding or a diffusion/LLM future-work paragraph.

**Concrete organization**

1. **Motivation:** State the single requirement: predict concentration from the sensors available at prediction time. Explain the closest existing capability and any evidenced remaining limitation within that requirement. Do not manufacture a second gap to match the architecture.
2. **Method and contribution:** Present one candidate advance: a combined mask-encoding and masked-pooling operation for concentration prediction from available sensor measurements. Explain how the two operations cooperate using their actual inputs, outputs, and dependency. They may have separate technical subsections for readability without becoming separate novelty claims. This description identifies the candidate's scope; its distinguishing operation still needs to be specified before novelty can be judged.
3. **Evaluation:** Place the independent held-out-batch comparison immediately alongside the claim it tests, stating the sensor-availability conditions and actual outcomes. Treat the comparison as supporting evidence, not automatically as another contribution. No outcome has been supplied here, so the organization must not imply that the candidate already wins.
4. **Closing:** Retain the abstract's concise requirement-to-method-to-evidence progression. Let the conclusion summarize the combined idea and what the reported evaluation establishes within its tested scope. It can end there, without a new challenge, deployment claim, causal explanation, or future-work paragraph.

**Evidence needed to judge the candidate advance**

- **Closest prior work and exact technical difference:** Supply verified comparisons with the nearest sensor-availability-aware prediction and masked-aggregation methods, together with the combined operation's equations or algorithm. Identify what changes beyond a routine combination of known operations. A smooth description or a new component name cannot establish novelty.
- **Evidence that the combination meets the requirement:** Define admissible sensor subsets, the actual mask semantics, and how encoding and pooling use available measurements. Show which availability patterns the held-out evaluation covers. “Whichever sensors are available” should not silently become a claim of reliable prediction for every possible subset, including cases with insufficient information.
- **A discriminating comparison and its results:** Establish whether the existing comparison includes the nearest relevant alternative and a meaningful simpler combination under matched information access, data splits, and selection conditions. Report actual differences and uncertainty appropriate to the claimed benefit. A component removal is useful only if it leaves a scientifically meaningful predictor; independent novelty for each component need not be demonstrated when the claim concerns their combined operation.

Independent held-out batches support an assessment of predictive generalization to the represented population. They do not by themselves establish originality, superiority, or the proposed explanation for an outcome. The missing evidence concerns the combined operation's technical distinction and demonstrated value, not a need to invent another task or expand the paper into plant deployment.
