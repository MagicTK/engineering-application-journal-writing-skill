### A. Revised passage

An earlier study aligned asynchronous measurements by time to estimate valve wear [12]. The present study addresses a different decision: when to raise a fault alarm from readings collected on two sensor clocks. The proposed alarm uses a clock-aware mask. A planned sensitivity analysis will examine how the alarm responds to six settings of the mask threshold.

**Proposed threshold comparison**

| Factor varied | Proposed controls across settings | Comparison |
|---|---|---|
| Mask threshold, six settings | Use the same sensor readings, fitting and calibration procedure, and held-out cases | Compare alarm decisions on each case across the six settings |

**Author note.** Verify the contents of Fig. 1(a–b) and Table 2 before restoring their cross-references. Supply the six threshold values when reporting the design.

### B. Prospective paragraph

The UCI SECOM dataset pairs semiconductor manufacturing measurements with pass/fail outcomes. When a measurement is missing, median imputation supplies a numerical input, but the imputed value alone does not distinguish that entry from an observed value equal to the median. We will test whether supplying a measurement-availability mask alongside the imputed inputs changes pass/fail prediction.

**Minimum check.** Construct the mask from the original missing entries available at prediction time and fit the medians on training data only. Fit the same classifier with and without the mask under the same training conditions, then compare predictions on the same held-out cases using the same outcome metric.

### C. Manuscript prose

del Río and Grey [8] aligned asynchronous signals.

The observed bands in Fig. 2(a) can be read alongside the alarm state for each window in Fig. 2(b).

The alarm weights each observed signal according to
\[
g_i = w_i x_i,
\]
where \(x_i\) is the observed signal indexed by \(i\), \(w_i\) is its learned coefficient, and \(g_i\) is the resulting weighted signal.

**编辑备注。** 请保留复姓 del Río 的完整写法，并将文献 [8] 的贡献表述限定在异步信号对齐。
