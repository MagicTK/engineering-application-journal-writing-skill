# Measurement Roles: Actual Response

One fresh context answered two fictional requests using frozen v4.2.12. The task answer below is unchanged except for writing-block wrappers and trailing whitespace. Environment/local-path disclosure is omitted and summarized in the accompanying review. No feedback was needed.

**A. 问题分类**

1. **甲：输入测量偏差与目标测量不确定性并存的浓度预测。** 输入是过程测量，其中部分流量读数存在校验确认的偏差；目标是实验室测得的下游浓度，其测量不确定性属于目标侧。不能据此补设标签缺失、标签稀缺或目标存在系统偏差。
   **English:** Predict downstream product concentration from process measurements with calibration-confirmed bias in some flow readings, using laboratory concentration measurements with reported measurement uncertainty.

2. **乙：传感器状态诊断（三分类）。** 输入是原始传感器序列；目标是“正常、固定偏差、卡死”，类别依据是受控故障施加记录。偏差与卡死在这里是待识别状态，不能预先当作无关噪声去除。
   **English:** Identify normal, fixed-bias, and stuck sensor states from raw sensor sequences, using class labels provided by controlled fault-injection records.

3. **丙：含原因未明统计离群点的过程故障诊断。** 输入是历史过程序列；目标是过程故障判断。统计离群不等于测量错误，全部删除可能损失真实故障信息，不能直接称为“噪声消除”。**待核事实：这些离群点反映测量误差，还是真实过程响应？**
   **English:** Diagnose process faults from historical measurements containing a small number of statistical outliers of unknown origin, which may represent measurement errors or genuine process responses.

4. **丁：故障类别错标，即目标侧标注可靠性问题。** 输入测量已核对；已知错误发生在人工录入的故障类型标签，而不是输入测量。类别错标与甲的连续目标测量不确定性不同。
   **English:** Classify faults from checked process measurements when some fault-type labels have been incorrectly entered during manual annotation.

**监督性质：**甲、乙、丁都有外部任务目标，若用于拟合，分别属于有监督回归或分类；丁还具有不准确标注条件，可在明确采用的定义后归入弱监督。丙的故障标签条件未说明，缺少独立参照测量不等于缺少任务标签。四项均不能仅凭这些描述认定为无监督、自监督或半监督：无监督须明确哪个拟合阶段不用外部任务目标；自监督须有实际的数据自构造训练目标；半监督须有带标签和无标签样本共同参与学习的事实。

**B. 替换段落**

On the same independent test set, the classifier achieved 92% accuracy before additional noise injection and 86% after the specified zero-mean Gaussian noise was added to normalized inputs. The comparison model decreased from 90% to 78%. Both models used identical test samples, preprocessing, and noise realizations, with fault labels unchanged. The accuracy drops were therefore 6 and 12 percentage points, respectively. Under this perturbation, the classifier maintained higher diagnostic accuracy and exhibited a smaller performance decline than the comparison model.

**草稿处理：**原句应整句删除，用上述分析替换。未定义的“denoising module”不能保留或补造；类别输出及准确率不能证明恢复干净信号，更不能证明消除了真实工厂中的传感器故障。未额外加噪的基线也不能称为无噪数据。没有重复实验统计，不写统计显著性；结论限定于此次指定扰动，不扩展至其他干扰或现场部署。
