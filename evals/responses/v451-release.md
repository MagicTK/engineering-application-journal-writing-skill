### A. Fault alarm

**Manuscript prose**

The valve-wear estimator in [12] aligns asynchronous measurements in time to estimate wear. The proposed alarm uses a clock-aware mask for fault detection. We will evaluate how the alarm responds to changes in the mask threshold by comparing six settings.

**Planned threshold comparison**

| Factor | Comparison design |
|---|---|
| Quantity varied | Threshold of the clock-aware mask, evaluated at six settings |
| Conditions to hold fixed | Alarm model, input measurements, and fitting and calibration procedure |
| Basis for comparison | Evaluate all six settings on the same test records and compare missed faults and false alarms |

**Author note.** Supply the six threshold values. Check Fig. 1(a), Fig. 1(b), and Table 2 against their captions before assigning cross-references. The planned sweep tests sensitivity to one parameter.

### B. Semiconductor pass/fail prediction

**Manuscript prose**

The public UCI SECOM dataset pairs semiconductor manufacturing measurements with pass/fail outcomes. Some measurements are missing. We will compare a predictor that fills missing entries with training-set medians against the same predictor supplied with both the filled measurements and a binary mask marking which entries were observed. This comparison asks whether measurement availability adds information for pass/fail prediction.

**Minimum check.** Construct the mask from the original records before filling missing entries, using only availability information accessible at prediction time. Use identical training and test records for both predictors, fit the medians on the training records alone, and compare fail detection and false alarms on the same held-out records.

### C. Attribution, figure, and equation

**Manuscript prose**

The method of del Río and Grey [8] aligns asynchronous signals.

The observed bands appear in Fig. 2(a), and the alarm state for each window appears in Fig. 2(b).

The alarm weights each observed signal according to
\[
g_i = w_i x_i,
\]
where \(x_i\) is the observed signal indexed by \(i\), \(w_i\) is its learned coefficient, and \(g_i\) is the weighted signal.

**编辑备注。** 正文保留了复姓 del Río，并按期刊体例列出两位作者；图 2 的两处引用分别对应图注中的观测频带和逐窗报警状态。
