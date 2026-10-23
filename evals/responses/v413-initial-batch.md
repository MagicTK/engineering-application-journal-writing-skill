# Independent baseline responses

These four fictional cases were answered from the frozen 4.1.2 instructions in one fresh responding context. They are baseline evidence, not results for changed 4.1.3 instructions. The answers below are retained verbatim.

**Case A**

Results paragraph:
With thresholds fixed using TRAIN-only normal data, evaluation on identical held-out process trajectories yielded adjusted point F1 scores of 96.0% for A and 94.0% for B, under a rule that credits an entire anomaly interval whenever any timestamp within it triggers an alarm. Unadjusted pointwise F1 instead favored B (69.0% versus 61.0%), demonstrating a scoring-dependent ranking. In one long anomaly, A first alarmed 85 seconds after onset, compared with 9 seconds for B; aggregate event delays have not been calculated. Same-hardware forward times were 2.1 ms for A and 3.0 ms for B, indicating faster model computation for A, not faster fault warning.

Abstract closing sentence:
Compared with B, A achieves higher adjusted point F1 and shorter forward time but lower unadjusted pointwise F1, and the available evidence does not establish timely online fault warning.

Follow-up calculation:
Using the existing unadjusted alarm traces, calculate the fraction of all annotated events detected within \(\tau\) seconds of onset as a function of \(\tau\), retaining events without an in-interval alarm as misses rather than excluding them.

**Case B**

替代图注：
中心窗口异常评分流程：模型使用区间 \([t-30\,\mathrm{s},\,t+30\,\mathrm{s}]\) 内的测量，对时刻 \(t\) 进行事后异常评分，输入齐备后的计算耗时为5 ms。不计传输、预处理及排队开销，该评分最早于 \(t+30.005\,\mathrm{s}\) 可用。

最重要的待核实项：
核对图示和评价是否区分“评分对应时刻 \(t\)”与“报警实际可用时刻”，并用后者对齐故障起点；当前输入定义不能支持在 \(t\) 之前预警，5 ms也不是端到端预警时延。

**Case C**

Retain the identity and dimension: they define the method’s operation, unlike batch size and optimization schedule, which belong in experimental settings.

Recommended block: “Foundry-Encoder R2, frozen”  
Recommended interface: “Hidden interface \(\mathbb{R}^{64}\)”

Methods opening:
The proposed method modifies the positional-state update of Foundry-Encoder R2 while keeping its encoder parameters frozen. This operation is defined on the encoder’s 64-dimensional hidden interface, \(\mathbb{R}^{64}\), and is specific to that architecture and width.

**Case D**

替换结果句：
在“窗口内任一时刻存在异常即判为含故障”的真值定义下，模型对截至 \(t\) 的过去60秒窗口进行分类，窗口级F1为0.91。

给作者的两句话：
请核对每个输出对应的窗口起止采样点及端点包含约定，依据原始时间标注重建窗口真值，并与保存的输出逐窗对齐。分析报警时序时，应以窗口结束 \(t\) 并完成处理后的实际可用时刻对齐原始故障起点，核对首次报警及其延迟，不能把阳性窗口回填为逐点预测或据此认定起点定位准确；故障结束后，窗口仍可能因保留异常片段而为阳性。
