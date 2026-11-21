### A. Revised passage and comparison table

Asynchronous measurements serve different engineering decisions in the two studies. The valve-wear estimator in [12] aligns readings by time to estimate wear. The proposed fault alarm uses a clock-aware mask. A planned sensitivity analysis will compare six settings of the mask threshold to determine how the alarm responds to that choice.

| Approach | Engineering task | Treatment of timing |
|---|---|---|
| Prior study [12] | Estimate valve wear | Align asynchronous readings by time |
| Proposed method | Raise a fault alarm | Apply a clock-aware mask whose threshold will be varied |

**Editorial note.** Verify the contents of Fig. 1(a–b) and Table 2 before restoring their cross-references. The six settings vary one parameter. Establishing whether the mask itself is necessary would require a separate comparison with the mask removed.

### B. Prospective paragraph

The public UCI SECOM dataset pairs semiconductor manufacturing measurements with pass/fail outcomes. When a measurement is missing, median imputation supplies a numerical input, but that value alone cannot distinguish an imputed median from an observed value equal to it. We will compare a classifier trained on median-imputed inputs with the same classifier given an additional mask indicating which measurements were observed. The comparison will test whether explicit availability information helps predict failure.

**Minimum check.** Confirm that the availability mask can be constructed from information available at prediction time. Fit the medians on training data alone, use the same imputed values and train/test split in both conditions, and compare missed failures and false alarms on the same held-out cases.

### C. Manuscript prose

In their study of asynchronous signals, del Río and Grey [8] aligned the observations in time.

The observed bands in Fig. 2(a) can be read alongside the alarm state for each window in Fig. 2(b).

The alarm weights each observed signal according to
\[
g_i = w_i x_i,
\]
where \(x_i\) is the observed signal, \(w_i\) is its learned coefficient, and \(g_i\) is the resulting weighted signal.

**编辑备注。** 图 2 可用于对照观测频带与逐窗报警状态，若要解释某一频带是否触发报警，还需单独验证其贡献。
