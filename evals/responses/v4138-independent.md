# Fictional Aggregation And Uncertainty-Writing Response

One fresh task context handled four scoped requests on the final frozen source. Source, request coverage and tool-output instructions changed; no controlled improvement is claimed.

Only private local reference links, line-end spaces and terminal blank lines are normalized; raw responses remain private. Synthetic arithmetic and writing checks are not scientific experiments.

访问说明：本次在同一任务上下文中处理四题。预置上下文含历史摘要，但未检索或用于作答。实际访问仅为指定 Skill（4.1.38）、下列当前参考、通用启动文件和只读额度服务；未披露账户值，未打开真实论文、eval、私有记录或其他项目，未修改文件、安装、运行实验或调用其他代理。

**M4138-A**
按 \(F1_k=2TP_k/(2TP_k+FP_k+FN_k)\)：

| 汇总对象 | Macro-F1 | Accuracy |
|---|---:|---:|
| 运行1 | \(7/9=77.7778\%\) | \(10/12=83.3333\%\) |
| 运行2 | \(1/7=14.2857\%\) | \(2/12=16.6667\%\) |
| 逐运行指标均值 | \(29/63=46.0317\%\) | \(50.0000\%\) |
| 汇总矩阵 `[[10,10],[2,2]]` | \(7/16=43.7500\%\) | \(12/24=50.0000\%\) |

两种 F1 **均可在各自定义下成立**；非线性指标不必满足“先计算再平均”等于“先合并再计算”。原稿定义明确，不应仅为数值一致自动更换评价对象。两种 accuracy 相等源于两次运行的样本数相同。

测试集仍只有 **12个不同样本**；24是运行—样本预测条目，不是24个独立采集样本。若原12个相互独立，独立样本数就是12。

逐运行汇总：
> The mean of run-wise macro-F1 across the two training runs was 46.03%, with mean run-wise accuracy of 50.00%, evaluated on the same 12 test samples.

合并预测汇总：
> Macro-F1 from the pooled run-example predictions was 43.75%, with pooled accuracy of 50.00%; the 24 prediction records corresponded to the same 12 test samples.

**M4138-B**
配对差值为 `[1.0, 0.9, 1.1, 0.9, 1.1]`，以下单位均为百分点：

- 均值差：**1.0000**
- 样本SD：\(s_d=\sqrt{0.04/4}=\mathbf{0.1000}\)
- SEM：\(0.1/\sqrt5=\mathbf{0.044721}\)
- 预定区间：\(1\pm2.776(0.044721)=\mathbf{[0.875854,\ 1.124146]}\)

> Across five independent paired blocks on the fixed data split, A improved mean accuracy over B by 1.00 percentage point (95% paired t interval: 0.876 to 1.124), supporting a positive expected difference over training randomness under the stated normality assumption.

作者注：区间排除零，支持题设条件下的正均值差推断。边际SD重叠不能推翻它，差值方差取决于配对协方差。仅剩两组各自的 mean±SD，可以恢复均值差，**不能恢复同一区间**；不得独立排序重配对，也不能外推到新产线或新分布。

**M4138-C**
敏感性图注：
> Accuracy versus T on a fixed test set. Means at T = 20 and 40 are 80% and 82%; error bars show ±1 sample SD (2 and 1 percentage points) across four random-initialization training runs per setting.

作者说明：将误写的95% CI纠正为样本SD；不改实际数据、误差棒、字体或几何，也不把SD转换或伪装成CI。

效率图注：
> Performance versus total parameter count, using the same four-run performance summaries. Runs differ in random initialization and share a fixed test set. Architecture-specific totals are fixed at 20,000 and 30,000 parameters, with no horizontal variability bars.

作者说明：性能离散度须来自实际四次训练，不补造未知数值；固定参数量没有随意添加横向±5%误差棒的依据。

据当前指南中的 **P66记录**，“五折SD”不能改称“五次独立种子实验”。连接ACC/F1/AUC的线连接的是指标类别，不能解释为连续参数敏感性曲线。

**M4138-D**
结果讨论，88词：
> A yielded higher mean weighted-F1 on both the process benchmark (81.2 ± 1.0% versus 80.5 ± 0.9%) and the production case (93.3 ± 0.5% versus 93.1 ± 0.4%). Benchmark sample SDs reflect five random-initialization runs on one fixed test set; production sample SDs reflect variation across three cross-validation folds. The mean gains are 0.7 and 0.2 percentage points, respectively. A's slightly larger sample SD in both evaluations indicates no reduction in the reported variability. The observed gains favor A within the evaluated settings, without an observed stability advantage.

摘要实验收束，30词：
> A showed observed mean weighted-F1 gains over B of 0.7 percentage points on the process benchmark and 0.2 on the production case, with slightly larger reported variability in both evaluations.

结论句组，43词：
> The method achieved higher observed mean weighted-F1 than B on the process benchmark and production case. These gains were accompanied by slightly larger sample SDs across training initializations and cross-validation folds, respectively. The findings support its average predictive performance within the evaluated settings.

作者注：现有汇总不支持“significantly superior”；A的已报SD更大，不支持“more stable”；无跨站点评价，不能写“across all industrial conditions”。保留既有两项真正设计贡献，将普通统计验证作为支持证据，不新增第三贡献。三折不是三次种子实验，也不合并两数据集为新总分。

**当前参考**
- A/B：[journal-migration-and-completeness.md](../../references/journal-migration-and-completeness.md)、[experiment-evidence-design.md](../../references/experiment-evidence-design.md)。
- C：上述重复性指南及 [figure-and-latex-production.md](../../references/figure-and-latex-production.md)；P66仅依据指南记录，未另读原论文。
- D：[section-writing-guide.md](../../references/section-writing-guide.md)、[contribution-narratives.md](../../references/contribution-narratives.md)。
- 另对 [terminology-decisions.md](../../references/terminology-decisions.md) 作了定向检索。
