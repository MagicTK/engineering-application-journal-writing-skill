# 4.1.19 Full-Prose Retest

A new fresh responding context answered the two unchanged fictional author requests and one added empirical-contribution control using the frozen 4.1.19 candidate. It did not receive the initial answers or scoring criteria. Its complete response follows without substantive editing or link normalization. These are fictional writing cases, not reported research.

作者说明：以下均为给定虚构场景的写作稿，不代表真实研究结论。摘要按空格计词，连字符词计为一词。

**A. 浓度预测**
:::writing{variant="document" id="53142"}
### Abstract

Product concentration prediction in continuous chemical mixing must accommodate unequal sensor sampling intervals and sparse laboratory labels. A supervised reference approach forward-fills measurements onto a common time grid. This study instead combines observation-time encoding with joint quality and reconstruction learning. Each available measurement is encoded with its variable identity and elapsed time to the prediction instant, using only earlier measurements. A weighted readout combines these observation representations into a window representation for concentration prediction. To learn from windows without concentration labels, an auxiliary decoder reconstructs observed values that are artificially masked during training. Reconstruction uses both labeled and unlabeled training windows, while the quality loss uses labeled windows only. Together, these objectives train the shared encoder used by the concentration predictor, which operates directly on available observations at prediction time. Evaluation on independently held-out periods in a process simulation case and an industrial production data case shows lower prediction error than the forward-filled supervised reference under the tested native sampling settings. Removing either elapsed-time encoding or the reconstruction objective on unlabeled windows increases prediction error, supporting the roles of observation timing and learning from unlabeled measurements in the combined design.

### Contribution

- We integrate encoding of actual observation timing with joint concentration prediction and masked-value reconstruction, enabling a continuous-mixing quality predictor to learn from labeled and unlabeled windows while operating directly on measurements available before prediction. Lower held-out error than the forward-filled supervised reference, together with increased error after removing either elapsed-time encoding or unlabeled-window reconstruction, supports the combined design under the tested native sampling settings.
:::

摘要为 190 词。贡献合为一项，突出时间编码与联合学习的结合，案例和消融作为支持证据。

**B. 零样本诊断**
:::writing{variant="document" id="53143"}
### Abstract

Process fault diagnosis may require identifying candidate faults for which no training samples are available. Engineer-defined semantic attributes, such as rising temperature and falling pressure, provide common descriptions of seen and candidate unseen fault classes. Attribute predictions learned from seen faults can therefore be matched to unseen class descriptions. This study uses attribute prediction errors on held-out seen-class validation samples to determine how strongly each attribute contributes to that match. An encoder and an attribute prediction head are trained using seen-class samples. The validation errors yield fixed attribute weights, assigning greater weight to attributes with smaller prediction errors. At prediction time, the model produces an attribute vector from process measurements. Weighted distances between this vector and the predefined descriptions of candidate unseen classes determine the diagnosis, with the nearest description supplying the fault label. Thus, attribute-specific validation errors shape how predicted attributes contribute to fault classification. In an industrial production data case, fault classes are held out, and all samples from these unseen classes are reserved for final testing. Using the same attribute predictor, weighted matching improves diagnostic accuracy over equal-weight matching on the held-out class set.

### Contribution

- We introduce a matching rule in which attribute prediction errors on held-out seen-class validation samples determine fixed distance weights for zero-shot process fault diagnosis. By giving greater weight to attributes with smaller validation errors, the rule assigns a fault label through the nearest candidate unseen-class description in the weighted attribute space. With the same attribute predictor, this weighting improves diagnostic accuracy over equal-weight matching on the evaluated held-out class set.
:::

摘要为 187 词。贡献落在由已见类别验证误差确定匹配权重这一具体改动上。

**C. 实证贡献**
可以写成一项实证贡献。它回答了预先提出的独立工程问题：在采集预算相同的条件下，采样时刻的分配是否影响扰动后的预测质量。固定预测器、训练信息等因素并完成重复比较，使贡献落在采样安排带来的工程认识上，无须以新网络模块为前提。

:::writing{variant="document" id="53144"}
- Repeated comparisons of two prespecified sampling schedules on independently held-out production periods show that, under the same acquisition budget, the schedule allocating sampling opportunities to post-disturbance periods yields lower peak prediction error within the tested disturbance windows, while average error during routine operation remains similar. With the data source, predictor, training information, and total observation count held fixed, this finding establishes the relevance of sampling-time allocation to post-disturbance prediction quality in the evaluated setting.
:::
