# Four fictional writing exercises: response and review

2026-11-13. A fresh responding context received only the public writing references and fictional facts, not the manuscript, private source notes or grading criteria. Responses below reproduce its final prose (presentation wrappers omitted). The maintainer checked meaning against the prompts. This is a scoped editorial review, not a benchmark of acceptance, writing speed or all journal topics.

## Iteration before the final check

An initial casting and sparse-reference exercise separated the measurement site from the possible fault source and did not name an unknown inspection actor. A subsequent transfer exercise correctly handed two pelletizer profiles to a classifier, but ended with “predict whether the fault is a clogged screen or a sticking feeder.” The two examples had not been declared an exhaustive label set. This **failed** the task-preservation check. The guide was amended to distinguish motivating scenarios from a label dictionary. A separate fresh response then predicted “fault type from the pattern of deviations across the two units” without defining new labels. The final four exercises below followed the addition of the source-located topic routes. There was no controlled comparison against a previous release.

## 1. Two units; illustrative faults

> A change in granulator drive current can follow either a clogged screen in the upstream crusher or a sticky feeder at the granulator itself. The granulator reading alone therefore leaves the fault type ambiguous.
>
> We organize diagnosis around the two physical units whose currents are recorded.
>
> We compute a separate residual profile for each drive, preserving which unit exhibited each deviation. The classifier uses the two profiles together, so its fault-type prediction can depend on whether a granulator deviation is accompanied by a change at the crusher.

Judgment: the opening illustrates ambiguity without turning the classifier into a two-class or root-cause model. The overview is brief; the two subsequent sentences introduce profiles and then their consumer. No performance finding or novelty priority was asserted.

## 2. Shift flags, new alloy, fixed text descriptions

> 铸造质量记录按班次标记是否出现缺陷，声学信号却记录到具体时刻。即使一个班次被标为阳性，记录也没有指出哪段声音与缺陷有关。检验手册提供了另一条线索：它按缺陷类型描述症状。
>
> 这些症状描述可以作为解读声学记录的参照，但不能直接给某个时间窗贴上标签。换用新合金牌号时，适配阶段又只能使用无标签运行数据。由此产生的挑战是：如何判断局部声学模式与某类症状是否相符，并据此预测可由检验记录核对的班次标记。
>
> 贡献：我们用大语言模型将手册中的症状整理为每类缺陷的一份固定描述，为不同时间窗提供共同的比对依据。以这些描述为参照，评分器将各窗与症状的匹配程度转化为班次判据，使局部声学证据能够用于班次级预测。
>
> 方法：将每个声学窗的编码与固定缺陷描述比对，取班次内最高的窗口匹配分数预测该班次的缺陷标记。
>
> 实验设计：可在目标牌号无标签数据、评分器和班次划分均相同的条件下，对比大模型整理的描述与人工从同一手册整理的描述，以留出班次的缺陷标记评价两种方案。
>
> 两条审稿建议均不采纳。新的是合金牌号，未说明缺陷类别在训练中未见；最高分窗口只是模型选出的窗口，没有独立的时间标注就不能验证定位。“没有用大模型”也不是挑战：即使已有大模型生成的描述，描述与声音如何对应、窗口证据如何支撑班次判断，仍是要解决的问题。

Judgment: both the physical decision and the mismatch of label and observation units survive. Manual descriptions are proposed as a future comparator, not reported as a completed experiment. The prompt supplied no nearest prior art: these are mechanism/contribution candidates, not proof of novelty.

## 3. Timing, actor and tested population

> At winding completion, a roll’s tension trace is available, but its later coating loss is not yet known. We use the trace to predict that loss for the roll. Subsequent peel tests provide reference measurements for assessing predictions on audit rolls only.
>
> “Technicians tested every roll.” Reject. The operator is unspecified, and “every roll” changes the tested population. Use “Peel tests provided reference measurements for audit rolls only.”
>
> “The predictor estimates the loss from the tension trace.” Accept in context. It preserves the input and target if “the loss” already refers to later coating loss. As a standalone sentence, keep the timing explicit: “At winding completion, the predictor estimates later coating loss from the roll’s tension trace.”

Judgment: timing and actor matter more than active/passive voice. The evidence-bounded abstract is short because no model details, comparator or numerical findings were supplied.

## 4. New tool conditions versus unseen classes

> New tool condition: Labeled support from the new condition rules out zero target-condition shots. Request the shot unit and count, which classes the support covers, and whether the model is fitted once or evaluated over episodes. Hold out whole query runs from support and tuning; windows from one run are not independent shots. For a small fixed support set, adaptation with limited labeled target data is the clearest name.
>
> Unseen diagnostic class: Class-level zero-shot diagnosis may fit. Request the seen/unseen class split, the descriptors available for unseen classes, and whether any of their measurements enter support, adaptation, or model selection. Evaluate on independent labeled examples of the held-out classes and state whether the predictor chooses among unseen classes only or among both seen and unseen classes. Hold out classes separately from tool conditions so the reader knows which kind of transfer was tested.

Judgment: correctly distinguishes the two axes without requiring episodic training for all few-shot settings or promising a result on a new plant. No production dataset, unpublished paper text or live author feedback was used in these exercises.
