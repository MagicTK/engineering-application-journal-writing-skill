# v4.4.0: problem-method evidence and manuscript boundaries

Six fictional scenarios were bundled into two independent fresh reading contexts in the final round (A-C and D-F). Readers had access to the public guidance, not tests, earlier answers, private manuscripts, the web or actual experiments. No new empirical results were requested. This is a scoped diagnostic, not a benchmark for journal acceptance or six independent replications.

## Failures that changed the guide

- Initial A introduced observation-age encoding as an implemented contribution without a model specification. The initial D answer did not reliably distinguish handling a missing identifier as a proposed safety check from implementing it. Both are useful designs; neither is a given fact.
- After the first abstract-reference edit, a new A reader again introduced retaining arrival time and age as the authors' contribution. Good comparison design did not cancel that failure. D-F covered the task and access distinctions, but the missing-identifier boundary needed an explicit retest.
- We moved the distinction between paste-ready factual prose and design proposals into both entry languages and the abstract module. Two new readers then took the original exercises. The test did not add a hint identifying the failed sentence.

## Final judgment

| Case | What the response actually distinguished |
| --- | --- |
| A | Deadline versus timestamp in the abstract; resampling, masking and age-based analysis confined to proposals. |
| B | Weight count and server training time versus measured board latency, bytes, memory, energy and missed deadlines. |
| C | Rejection, later class learning, and initiating cause require three different references. |
| D | Expert test choice versus final judgment; clarification for a missing instrument identifier explicitly a candidate design. |
| E | Lot-level evidence, unlabeled pretraining, synthetic augmentation, and new-recipe access are not interchangeable. |
| F | Input change does not establish conditional drift; old and new recipes need separate chronological evaluation. |

The responses below are retained for inspection, not as prescriptions. In particular, zero filling is a comparator paired with a mask here, not a universal recommendation. A match to an expert tool choice is not the same outcome as a correct physical diagnosis.

## Final independent answers

Kiln energy demand must be predicted at 14:00 from minute-sampled channels and an hourly sensor whose 14:00 reading arrives at 14:08. The forecast must therefore use only readings received by 14:00, even when a later arrival carries a 14:00 timestamp.

| Proposed comparison | Design |
|---|---|
| Input treatment | Hold the regression model fixed. Compare hourly summaries of available readings, a minute grid carrying the last received hourly value, and zero-fill with an observation mask that distinguishes a missing reading from a measured zero. |
| Predictor | Compare ridge regression with a native-rate predictor using the same sensors, lookback, and arrival cutoff. A minute-channel-only model tests the value of adding the hourly sensor. |
| Evaluation | Split runs chronologically before windowing; fit preprocessing on training runs only. Do not interpolate the whole file: interpolation using the 14:08 arrival is an offline reference only. Report MAE and RMSE against the same measured demand targets at identical issue times. |
| Figure | On one timeline, mark minute observations, the hourly sample, its arrival, and the forecast deadline. Pair it with held-out absolute error versus age of the latest available hourly reading. |

**已有结果：**该模型存储的权重个数更少，本次服务器训练耗时更短。前者不等于模型文件更小或运行内存更低；后者不能证明板上推理更快或满足实时期限。

**部署测试：**在同一块板上，以相同精度、运行时、线程数、功耗模式和批量大小（1），按相同顺序回放同一测试集。分别记录冷启动和预热后的表现；在相同任务质量要求下，报告实际任务得分、模型文件字节数、峰值内存和单次推理能耗。从输入到达计时至输出可用，报告中位数、P95、P99及超期比例，并单列预处理、排队和推理耗时。

**Introduction transitions**

1. Assigning an assembly fault to a known class answers a different question from deciding when none of the known classes fits; rejection flags a case for inspection without naming its fault type.
2. Once a technician labels some rejected cases, the question becomes whether updating the detector improves recognition of the newly labeled types while preserving recognition of previously known faults.

**Suggested contrasts.** Before updating, compare forced known-class assignment with rejection at a validation-selected threshold. Report known-class macro-F1, known cases falsely rejected, and unfamiliar cases rejected where binary status is verified; type-level accuracy is unscorable without identities. After labels arrive, compare frozen and updated models on untouched later runs. Match label and replay budgets across update methods; report newly labeled types’ recall, change in old-class performance, and rejection of still-unfamiliar faults separately.

**Interpretation.** Write “The vibration channel ranked first for this alarm and warrants inspection.” Reserve “root cause found” for independent evidence identifying the initiating fault, such as a verified teardown finding.

**D｜洁净室检测**

引言衔接：同一句“请检查设备”，可能指痕量污染，也可能指压力稳定性。手册列出了获准的检测项目，但选哪一项取决于请求意图；即使意图明确，缺少仪器编号也不能确定检测对象。

贡献：本文将“选什么检测”与“检测结果是什么”分开：语言模型从两项获准测试中选择一项，结果由专业程序给出。相比之下，时序模型在数值传感器历史上预训练，再用带标签的目标仪器运行记录适配，以测量序列预测目标；它不直接回答文字请求该调用哪项测试。

实验一：在相同请求、手册和候选项下，比较语言模型与手册关键词规则，按两类意图分别报告与专家选择的一致率。对缺编号请求，另测“先询问编号”的候选策略，记录误调用率，不把暂缓执行算作选错测试。

实验二：固定仪器记录与专业程序，仅替换模型选择或专家选择，对照独立留出的最终判定，报告判定一致率与完成率；专家选对后仍出现的错误应与选错测试分开。

图：`请求 → 语言模型选项 → 专业程序 → 结果`；专家选项对照第二节点，留出判定对照末节点。缺编号时的候选分支为 `执行前 → 询问编号`。

**E | Fabric lots**

A lot-level quality label tells us how the lot was judged, not which trace interval mattered. Unlabeled traces may teach recurring process patterns, while diffusion could add training variation without adding independent quality judgments.

Split real lots before windowing or fitting anything. Cross augmentation (none, simple perturbation, diffusion) with unlabeled pretraining (off/on); match labeled lots, classifier, pooling, tuning budget and augmentation counts where applicable. Declare the unlabeled pool and recipe access. Score lot-level predictions on untouched real lots, reporting each recipe separately.

Mask highly ranked intervals and compare the change in lot score with masking equal-length random intervals from the same trace. This tests model reliance, not defect localization or cause. Using new-recipe development traces tests adaptation to that recipe; with none, freeze all choices before testing unseen-recipe transfer. Neither setting establishes robustness across recipes generally.

**F | Monthly updates**

Predict each run before its defect label arrives. Compare frozen, update-once and monthly-update classifiers with identical label delays and no earlier-recipe replay; disclose retained parameters or summaries. Score logged predictions by month. After each update, have an evaluator score sealed lots from each recipe to distinguish new-recipe gains from earlier-recipe losses. Once labels arrive, compare defect rates within overlapping pressure ranges.

Limited conclusion: A pressure histogram shift establishes a change in measured inputs, not a change in defect risk at a given pressure or a benefit from updating.
