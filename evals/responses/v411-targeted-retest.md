本文件是同一上下文中的定向复测，不是 fresh-context test。已重读当前 `section-writing-guide.md` 和原请求指定的 Skills；以下两项重新作答仍只使用各自原有的合成事实。`responses.md` 保持不变。

## v411-cross-case-reversal

**可讨论的英文综合分析**

With parameters fitted separately for each case, the same weighting mechanism produced opposite changes in the reported mean performance under matched comparison settings. In fault classification, the full method achieved a mean macro-F1 of 84%, compared with 81% after removing the mechanism, a gain of 3 percentage points. In concentration soft sensing, the full method instead had a higher mean MAE of 0.44 g/L, compared with 0.40 g/L without the mechanism. The cross-case finding is therefore a boundary on the design's observed benefit: weighting favors classification in Case A, whereas its removal favors concentration estimation in Case B. This makes inclusion of the mechanism a case-specific modeling choice to be judged against the prediction target. Reusing the design across tasks preserves a common methodological principle, but the measured advantage does not carry over uniformly.

**简短理由：** 综合结论落在“设计收益的案例边界”，既保留 A 的增益，也保留 B 增加 0.04 g/L 的误差。macro-F1 与 MAE 的目标、单位和优劣方向不同，不能平均成一个有共同工程含义的 overall improvement。均值未给出运行间稳定性或显著性，B 的劣势也没有受控原因分析支持“噪声更大”的解释；这些属于解释边界，不必全部塞进英文结果段落。分别训练说明复用了方法，而非迁移了同一个已训练模型。

## v411-positive-discussion

**可讨论的英文 Results/Discussion（两段）**

On independent held-out batches, the new model's predictive advantage was concentrated in the low-flow condition, where mean MAE decreased from the comparator's 0.55 g/L to 0.42 g/L. Under routine flow, the ordering reversed: the new model had a mean MAE of 0.39 g/L, compared with 0.37 g/L for the comparator. The engineering trade-off is thus a 0.13 g/L reduction in observed mean error at low flow alongside a 0.02 g/L increase under routine flow. Model choice depends on the relative importance of these operating conditions for concentration prediction, with the reported means favoring the new model specifically when low-flow estimation is the priority.

Offline timing measurements on historical data, without production-line integration, recorded 12 ms for the new model and 5 ms for the comparator on the same target CPU, including preprocessing. Both reported times fall below the 20 ms decision deadline, leaving measured margins of 8 and 15 ms, respectively. The additional 7 ms of computation therefore fits within the stated budget in this measurement, making the low-flow error reduction available at the expense of timing headroom. Under routine flow, the comparator combines lower observed mean error with faster inference. The resulting choice is between a low-flow prediction advantage and greater computational margin, rather than a uniform improvement in accuracy and speed.

## v411-generalization-and-refitting

**对原答复的影响：无需修改。** 新增说明要求区分论文段落与随附审阅意见，并未改变泛化证据的含义。原答复的最小替换已直接写明同一总体内的独立批次测试和分别拟合；后续解释是在回答用户明确提出的“建立了什么、未建立什么”，不是向 Results 段落追加缺失实验清单。有效的随机批次留出支持评价总体内预测泛化，分别拟合不等于单个模型跨厂迁移，这两项判断保持成立。

## v411-approved-figure-scope

**对原答复的影响：无需修改。** 这是文字判断与授权范围检查，不是需要压缩的 Results/Discussion 草稿。原答复保留没有明确问题的句子，说明混淆矩阵与逐类 F1 的信息差异，并遵守已确认的图表与版式边界。未查看图、PDF 或源码的说明是必要的核验范围披露；新增写作说明既不取消这一边界，也不授权删图或调整流程图位置。

## v411-single-requirement-conclusion

**Effect on the original response: no change is required.** The new guidance separates manuscript prose from accompanying review; it does not change what constitutes an independent contribution. The original response is organizational advice, not a drafted Results paragraph. Its one-requirement, one-combined-advance structure remains appropriate, and its evidence checklist answers the explicit request for what is still needed to judge candidate novelty. That checklist should remain advice to the author, not be appended to the accurate abstract or conclusion. Neither a second challenge nor a fashionable future-work paragraph is needed.
