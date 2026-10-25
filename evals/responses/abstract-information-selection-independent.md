# Abstract Information Selection: Actual First Answer

Fictional input only; one fresh context and no corrective reply. Paths, display wrappers and environment-specific access disclosures are normalized; the scientific response content is preserved. See the accompanying review for access limitations.

## Request

Use the current Skill suite for a fictional industrial manuscript revision. Read only the public Skill and relevant references, not evals, tests, private maintenance files or actual manuscripts. Do not edit files, run scientific experiments, browse online or publish. Disclose inherited context access and truncated reading separately at the end.

We want a connected English abstract of about 160-200 words, one concise candidate design contribution and a short Methods explanation. Use only these facts. Explain necessary corrections and unresolved implementation checks afterwards, not as a string of caveats inside the abstract. Do not propose a new method or a catalogue of experiments.

The task is classifying four annotated operating conditions of a single zinc-roasting unit from contiguous 120-point windows sampled every second. Windows end at their prediction issue time. Training and test campaigns are disjoint. A historical linear SFA mapping is fitted only on training observations. Separately, another linear SFA mapping is recomputed from each available input window, including each test window without using its label. Both mappings minimize average squared first differences with zero-mean, unit-variance and decorrelation constraints. They produce four features per sample each. Their feature values and within-window first differences are concatenated on the common 119 valid time positions, yielding 16 channels. A one-dimensional CNN with a four-class softmax is trained using the window labels. At prediction, the historical mapping and CNN weights stay fixed, while the local mapping is recomputed from the current window. There is no cross-stage variable grouping, plant topology or quality target. The supplied implementation notes do not specify how local eigensolver signs, repeated eigenvalues or rank-deficient windows are handled.

With the same trained classifier architecture, replacing the local features with a second copy of the historical features gives macro-F1 0.87, while using the historical-plus-local features gives 0.91 on the same test campaigns. These are one aggregate comparison, with no confidence interval or device timing. State this result at its actual level; scientific novelty versus related SFA/CNN work has not been established. Do not assume that a measured process-condition classifier is a new benchmark resource.

Our draft says: 'An unsupervised, training-free global-local architecture fuses inter-stage and intra-stage independent dynamics to remove measurement noise. Because the two paths are whitened, their outputs are mutually statistically independent. The online local update makes the complete CNN a continually learned model. This improves process quality by 4% and supports real-time deployment.' Please keep the legitimate method idea without inheriting these claims solely from terminology.

Two technical checks belong after the manuscript passages. First, a coauthor rescales a feature sequence by 0.1 and reports that its average squared first difference fell from 0.02 to 0.0002, proving better physical dynamics. The unscaled sequence has unit variance and the scaled one has variance 0.01. Check what follows from those values. Second, a separate unimplemented network-expansion proposal for future labeled training data uses an old readout W, an added-block correction c and matrix D: the proposed readout is [W-D*c; c]. In the scalar illustration W=2, D=3, c=0.2. A colleague calls this 'only new weights update; original weights remain unchanged.' Check that statement, but do not insert the unimplemented proposal into the current abstract or claim that it already has timing/accuracy evidence. We do not have an automatic growth trigger or new labels available at test time.

Keep a source-specific complete model name attributed when appropriate; do not invent a new full module name. In Chinese notes, use established base terminology and distinguish process variable, feature, sample window and operating condition by their actual objects.

## Response

**Abstract**
This study examines whether combining historical and window-specific temporal representations improves recognition of four annotated operating conditions in a single zinc-roasting unit. Each prediction uses a contiguous 120-point window of measurements sampled every second and ending at the prediction issue time. A linear slow feature analysis (SFA) mapping fitted on training observations provides a historical representation, while a separate SFA mapping estimated from each input window describes its local temporal variation. Both mappings extract features by minimizing average squared first differences under normalization and decorrelation constraints. Their feature values and within-window differences are combined for a one-dimensional convolutional neural network trained with window labels to predict the operating condition. During prediction, only the local SFA mapping is re-estimated from the available unlabeled window; the historical mapping and classifier weights remain fixed. On test campaigns disjoint from training, the historical-plus-local representation achieves an aggregate macro-F1 of 0.91, compared with 0.87 when the local representation is replaced by a second copy of the historical representation using the same classifier architecture.

168 words, counting whitespace-separated tokens.

**Candidate Contribution**
A representation combining training-fitted and window-specific SFA features with their temporal differences supplies historical and current-window descriptors to a supervised classifier for zinc-roasting operating-condition recognition, while keeping the historical mapping and classifier weights fixed during prediction.

**Methods**
Each sample window contains 120 consecutive measurement vectors from times \(t-119\) through \(t\), sampled at one-second intervals. Training and test campaigns are disjoint. The historical linear SFA mapping is fitted exclusively on training observations; the local linear SFA mapping is fitted separately within each training or test window without using its label. Each mapping produces four feature coordinates by minimizing average squared first differences under zero-mean, unit-variance and decorrelation constraints on its respective fitting data. Let \(g_i,\ell_i\in\mathbb{R}^{4}\) denote the historical and local feature vectors. Indexing each difference by its later endpoint gives
\[
z_i=\operatorname{concat}(g_i,\ell_i,g_i-g_{i-1},\ell_i-\ell_{i-1}),\qquad i=2,\ldots,120.
\]
The resulting sequence has 119 time positions and 16 channels. A one-dimensional CNN with a four-class softmax is trained using window labels. Prediction retains the historical mapping and CNN weights and recomputes the local mapping from the current available window.

**Necessary Corrections**
- **“Unsupervised, training-free” → supervised classification with label-free SFA fitting.** Neither SFA fitting nor labeled CNN training disappears because the feature objectives are unsupervised.
- **“Inter-stage and intra-stage” → historical-data and current-window scopes.** No production-stage grouping or plant topology is supplied.
- **“Mutually statistically independent” → separately constrained, decorrelated features.** Whitening does not generally establish statistical independence, either within a branch or between branches. Historical fitting constraints also need not hold on test-window outputs.
- **“Remove measurement noise” → minimize scale-constrained temporal variation.** This objective alone establishes neither noise removal nor physically meaningful dynamics.
- **“Continually learned CNN” → prediction-time local SFA re-estimation with a fixed CNN.** A changing local projection is a genuine fitting operation, but it does not update the classifier.
- **“Improves process quality by 4% and supports real-time deployment” → the reported aggregate classification comparison.** The difference is **0.04 macro-F1**, not measured quality improvement. One aggregate comparison without a confidence interval establishes no statistical significance; absent device timing, real-time deployment is unverified. Neither scientific novelty nor a new benchmark resource is established.

The candidate contribution describes the design, not proven novelty. The public Skill identifies closely related work in its [P54 record, *Abnormal Operating Condition Identification of Industrial Processes Based on Deep Learning With Global-Local Slow Feature Analysis*](../../references/published-evidence.md). Source-specific complete model names should remain attributed to their source; none was supplied here, so no new full model or module name is invented.

**Technical Checks**
1. **Rescaling does not improve normalized slowness.** For \(y'=0.1y\), both squared differences and variance scale by \(0.1^2=0.01\):
   \[
   \Delta(y')=0.0002,\qquad
   \frac{\Delta(y)}{\operatorname{Var}(y)}=\frac{0.02}{1}
   =\frac{0.0002}{0.01}=0.02.
   \]
   The reported decrease is entirely explained by amplitude scaling. The scaled sequence violates the unit-variance constraint; restoring unit variance restores the original difference energy. These values provide no evidence of better physical dynamics.

2. **The proposed readout changes old weights.**
   \[
   \begin{bmatrix}W-Dc\\c\end{bmatrix}
   =\begin{bmatrix}2-3(0.2)\\0.2\end{bmatrix}
   =\begin{bmatrix}1.4\\0.2\end{bmatrix}.
   \]
   The old readout block changes from \(2\) to \(1.4\). Even if only \(c\) is independently optimized, the effective old coefficients change through \(-Dc\); they remain unchanged only when \(Dc=0\). This unimplemented future labeled-training proposal supplies no current accuracy or timing evidence. No automatic growth trigger or test-time labels are available, and the proposal is excluded from the manuscript passages.

**Implementation Checks**
The local solver’s sign conventions and treatment of repeated eigenvalues remain unspecified. Sign flips and rotations within a repeated-eigenvalue subspace preserve SFA constraints but can change the channels presented to the fixed CNN. Channel ordering and orientation therefore require implementation clarification, not an assumption of invariance.

Rank-deficient windows also require clarification: singular covariance prevents ordinary full-rank whitening, and centered rank below four cannot support four mutually decorrelated, unit-variance linear features. The actual handling is unknown. Confirm that preprocessing and difference alignment match the Methods description; these checks do not imply that failures have already been observed.

中文术语说明：使用“慢特征分析”“一维卷积神经网络”“工况分类”。“过程变量”指实际测量量；“特征”指映射得到的坐标；“样本窗口”指连续120个采样时刻构成的分类输入；“工况”指四类标注对象。16个特征通道不等于16个过程变量；“历史/局部”也不等于“工序间/工序内”。
