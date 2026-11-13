# 4.4.2: tool-assisted decisions and constrained delivery

Two independent fresh contexts, each with two new fictional problems, read the public guidance. Neither saw the evaluation files, the other context or private material. They produced the responses below. The four outcomes passed on this instruction snapshot; this is a scoped writing test, not a plant trial or a guarantee about arbitrary prompts. The runnable six-request guide example has different inputs from the evaluation.

- A: the same count of 12 appears in two different populations. The answer correctly identified procedure agreement, correctness among returned answers, coverage and timely correct delivery; it did not claim a plant test was executed.
- B: frozen numeric pretraining plus a fitted head is not zero-shot inference or agency. Future assays verified held-out predictions rather than supplying inputs. Whether the fitted head is useful is the experiment, not a given result.
- C: among 64 correct answers only 51 were confirmed timely, three were known late and ten could fall on either side. The tight bounds on all eligible requests are 51/80 and 61/80; neither a hard deadline guarantee nor a confidence interval follows. Any proposed breakdown applies only to components actually present.
- D: a synthesis report and training log cannot establish measured board power or console latency. Communication and compression received separate comparisons. The proposed target-board tests were not described as completed.

## Independent writing

**摘要结尾。** 在有参考检测程序的16单中，离线语言模型推荐的振动检测程序有12单与参考一致（75%）。以独立核实的最终故障类型为准，服务返回的15个自动诊断中有12个正确（80%）。在全部20个符合自动诊断条件的工单中，自动应答覆盖率为75%（15/20），按时获得正确诊断的比例为45%（9/20）：3个正确答案迟到，另有3单超时未答、2单转人工。

**讨论。** 不同检测程序可能得到同一正确诊断，因此，程序不一致不等于误诊；缺少参考程序的4单仍可评价最终诊断。80%描述的是已应答工单的准确率，不代表全部工单按时得到正确答案的机会。没有现场操作记录，不能据此认定推荐的检测已在现场执行。

**建议对照。** 在有参考程序的16单上做配对离线回放，分别用固定规则、模型推荐和参考程序选测，保持输入、可选程序、参数设置、诊断软件版本和时限相同。逐单核对最终类型：仅更换选测程序就能纠正的错误，提示选测影响；采用参考程序仍出错的，再区分程序执行与结果判读问题。另记迟到、超时和转人工，不把参考程序视为唯一正确选择。

**Introduction transition.** At discharge, the batch assay is still a day away. Can measurements available by discharge support an estimate of the eventual assay value? We study whether a numerical encoder pretrained on other plants provides useful features for this estimate. The encoder remains frozen; only a linear readout is fitted to labeled local batches. This is supervised transfer for quality estimation, not zero-shot or agentic diagnosis.

**Proposed test.** Hold out later batches intact and check for overlap with pretraining records. Compare the pretrained encoder against a frozen, randomly initialized encoder of identical architecture with the same fitted readout, and against a task-specific regression baseline. Match local label budgets, tuning access, and discharge-time inputs. Fit preprocessing on training batches only. Lock each held-out prediction at discharge; use the next day’s assay solely to score paired absolute errors in assay units.

**C｜结果。** 80 个符合条件且有标签的请求中，64 个得到了正确的自动答复：51 个在 70 ms 内（含 70 ms）送达操作台，3 个超时，10 个缺少操作台时间戳；因此，按时正确送达率的最紧区间为 **[51/80, 61/80]，即 [63.75%, 76.25%]**。两端分别对应这 10 个答复全部迟到或全部按时。37 ms 只是已答请求的模型执行时间 p95，不能判定端到端送达时间。

**前瞻试验。** 预先固定计时起点，以答复在操作台可见为终点。让网关方案与准确率相当的基线在同一硬件、网络条件和请求到达序列下成对测试，用同步时钟逐请求记录排队、推理、远程往返和重试。每个请求只计一次，分母保留全部合格请求；分别报告按时正确、迟到正确、错答、未答和转人工，缺失时间戳单列。

**D | Contribution boundary.** FPGA synthesis reports LUT and BRAM use; the workstation log shows shorter training there. Neither establishes board-level inference latency, power, or energy per request. The installed system sometimes uses a cloud specialist, so it is not fully offline.

**Communication.** Diagram the local and remote paths, marking payloads and the return to the console. Compare selective routing with local-only and always-remote baselines using the same models, requests, and link conditions. Report remote-call rate, bytes per eligible request, and timely correct delivery, including link failures.

**Model compression.** Plot task accuracy against model size for the uncompressed parent, the proposed compression, and a standard quantized baseline. Hold routing, test inputs, and target board fixed. Show synthesized LUT and BRAM counts separately; add latency or energy only after direct target measurements.
