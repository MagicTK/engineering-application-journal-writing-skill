# Fictional Selection-Case Response

Actual answer; supplied numbers and implementations are fictional. Local reference links are normalized for the repository.

**English Manuscript Prose**
:::writing{variant="document" id="64128"}
### S4124-A
Following FS-SCF [P62], a feature-selection layer rescales the four inputs using learned weights of 0.50, 0.30, 0.15, and 0.05. A penalty encourages the weights to sum to one, and all four weighted inputs are passed to the classifier.

### S4124-B
Training-set feature selection reduced the classifier input from 60 to six descriptors (90%), retaining two directly computable descriptors from each of the three sensors.

### S4124-C
Feature ranking and the choice of k used labels from both the training and final test sets, so the reported evaluation is not independent of feature selection.

### S4124-D
**Contribution:** We develop a diagnostic pipeline that selects two of five raw measurement channels during training and uses only those channels throughout preprocessing and prediction, reducing its required measurement inputs by 60%.

**Results:** On the same hardware and at the same batch size, complete-pipeline prediction latency decreased from 20 to 12 ms, a 40% reduction. Macro-F1 decreased from 0.900 to 0.898, indicating an absolute performance loss of 0.002 accompanying the latency improvement. The remaining three sensors continue to support process control.
:::

**中文作者说明**
**S4124-A**
学生的资源结论不成立；“没有硬子集就绝不能叫 FS 层”也过度。Skill 对 [P62 的定义核查](../../references/published-evidence.md)支持保留有归属的层名，但须说明实际是输入加权；P40/P61 的显式子集选择是不同操作，不构成统一禁名规则。

本例仍使用全部四个输入。该惩罚针对权重和的偏离，不强制产生稀疏子集，因此不能推出只需一个传感器或节省 75% 采集成本。权重大小也不是物理故障原因的证据。

**S4124-B**
90% 的描述量缩减成立，但三个传感器各保留两种描述量，仍全部需要；10 倍推理加速没有实测支持。可以直接计算所选六种描述量，无须一概保留原有 60 种计算。

必要作者核实只有两项：
1. 提交六个描述量的定义、传感器映射及预处理依赖，核对实际执行路径能否只计算这些描述量。
2. 若保留速度主张，补取相同硬件、批大小及计时范围下的完整预测耗时，覆盖所需预处理、描述量计算和分类输出，注明重复与汇总方式。无需为此安排重训练。

**S4124-C**
监督式排名及选择 k 都属于模型选择；分类器只在训练集优化，不能消除测试标签已经造成的信息泄漏。

应补取：数据划分与样本 ID、排名及相关标签变换脚本、k 的候选值和选择日志、各步骤访问的数据范围，以及最终子集对应的预测和指标记录。

可交接作者决定的修复路径：
1. **暂不重评：**保留原数值，明确标为测试标签参与选择的探索性结果，撤回“完全独立测试”的表述；同步更正方法、表注及相关结论。
2. **重新建立最终评估：**仅用训练数据完成选择，可预先固定 k，或在训练集内部交叉验证；交叉验证时各折内重新拟合归一化、排名及分类器。冻结流程后，在真正未参与既往选择的新留出数据上终评。
3. **没有新增数据时：**锁定流程后，按真实独立单位进行嵌套交叉验证，外层只评分，所有排名、标签变换和 k 选择限于外层训练数据；将其另列为新的内部重评结果。

不必每篇文章都设置独立验证集。原测试集也不会因重跑就恢复为“从未参与选择”；新评估完成前，不替换原数值或提前填写新结果。

**S4124-D**
可以同时保留诊断所需原始测量输入减少 60% 和完整预测耗时降低 40%，不能压缩成“仅特征数变化”。macro-F1 的绝对下降为 0.002，应明确作为性能代价；现有事实不支持精度等效、拆除传感器或维护费用减少。

B—D 的判断遵循 Skill 的[选择输出与资源声称边界](../../references/experiment-evidence-design.md)。以上仅使用题设虚构事实及本地参考，未执行实验或修改结果。
