# 4.1.18 Full-Prose Baseline

One fresh context answered two fictional author requests using the unmodified 4.1.18 instructions. Its complete response follows without substantive editing. The cases do not report real research. A later maintainer review identified a contribution-organization defect in A; do not treat this initial response as approved guidance.

作者说明：以下均为虚构研究场景的写作稿。两篇摘要分别为203词、179词，按空格计词，连字符词计为一词。

**A. 浓度预测**
:::writing{variant="document" id="71843"}
### Abstract

Predicting product concentration in continuous chemical mixing requires learning from sensors sampled at different intervals and sparse concentration assays. A forward-filling reference places measurements on a common time grid for supervised prediction. We combine encoding at actual observation times with joint quality and reconstruction learning to use the available measurements directly. Within each window, the encoder represents each observed value together with its variable identity and elapsed time to the prediction instant, using only earlier measurements. A weighted readout combines these observation representations into a window representation for concentration prediction. During training, an auxiliary decoder reconstructs artificially masked observed values from labeled and unlabeled windows, while the quality loss uses only labeled windows. Both objectives train the shared encoder, allowing unlabeled measurements to inform the concentration predictor. Prediction uses neither the decoder nor a reconstructed time grid. Evaluation on a process simulation case and a production-data case uses independently held-out production periods, with test labels excluded from tuning. Under the tested native sampling settings, the model yields lower concentration prediction error than the forward-filling supervised reference. Removing either elapsed-time encoding or reconstruction learning from unlabeled windows increases prediction error, supporting the roles of observation timing and unlabeled-data learning in the evaluated prediction task.

### Contributions

- We combine encoding of measurement values, variable identities, and elapsed times with joint concentration prediction and masked-value reconstruction. This combination lets the shared encoder learn from labeled and unlabeled training windows while retaining observation timing in the representations aggregated for concentration prediction.
- Ablation comparisons show that elapsed-time encoding and reconstruction learning from unlabeled windows each contribute to concentration prediction under the tested native sampling settings: removing either increases error. Together with the lower error relative to the forward-filling supervised reference, these findings support the combined design in the simulation and production-data cases.
:::

**B. 零样本故障诊断**
:::writing{variant="document" id="92615"}
### Abstract

Process fault diagnosis is needed even for candidate fault classes with no available training samples. Engineers describe seen and candidate unseen classes in advance using a common set of semantic attributes, such as temperature rise and pressure drop. Building on attribute prediction followed by class-description matching, this study makes each attribute's contribution to zero-shot diagnosis depend on its prediction error on seen-class validation samples. An encoder and attribute prediction head are trained using only seen-class samples. A separate validation set from these classes provides attribute-wise errors, from which fixed matching weights are obtained, with larger weights assigned to attributes with smaller errors. At prediction time, the estimated attribute vector is compared with the predefined descriptions of candidate unseen classes using the resulting weighted distance. Selecting the class with the smallest distance gives greater influence to attributes predicted more accurately during validation. Evaluation uses a production-data case with fault classes held out and all their samples reserved for final testing. Compared with equal-weight matching using the same attribute predictor, the weighted distance increases diagnostic accuracy on the held-out class set.

### Contribution

- We introduce an attribute-weighted matching rule that derives fixed weights from prediction errors on separate seen-class validation samples. These weights give lower-error attributes greater influence when matching predicted attribute vectors to candidate unseen-class descriptions and selecting the nearest class. With the attribute predictor unchanged, this modification improves diagnostic accuracy over equal-weight matching on the evaluated held-out fault classes.
:::
