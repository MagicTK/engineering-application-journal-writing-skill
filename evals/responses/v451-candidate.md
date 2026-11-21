### A. Fault alarm

**Manuscript passage.** For valve-wear estimation, the method in [12] aligns asynchronous measurements by time. The proposed fault alarm uses a clock-aware mask. To assess how the mask threshold affects the alarm, we will compare six settings on the same held-out records.

**Planned threshold comparison**

| Experimental arms | Quantity varied | Conditions held in common | Proposed readout |
|---|---|---|---|
| One run per setting, six settings in total | Threshold of the clock-aware mask | Sensor inputs, fitting and calibration procedures, held-out records | Fault detection rate and false-alarm rate at each setting |

**Author note.** Verify the contents of Fig. 1(a) and (b) before assigning either panel to a sentence. Confirm the six threshold values and the intended contents of Table 2 before cross-referencing it. The table above describes a proposed sensitivity study.

### B. SECOM

**Manuscript passage.** The public UCI SECOM dataset pairs semiconductor manufacturing records with pass/fail outcomes. Some measurements are missing. We will compare two classifiers that receive the same median-imputed values. One will also receive a binary mask identifying which entries were observed. This comparison asks whether measurement availability adds information for pass/fail prediction.

**Minimum check.** Verify that both arms use the same records, splits, classifier and fitting procedure, with medians estimated on training records alone. Construct the mask from availability at prediction time and compare errors on the same held-out pass and fail records. This isolates the effect of supplying the mask.

### C. Citation, figure and equation

Del Río and Grey [8] aligned asynchronous signals.

The observed bands in Fig. 2(a) can be read alongside the alarm state for each window in Fig. 2(b).

The alarm computes a weighted signal \(g_i\) as
\[
g_i=w_i x_i,
\]
where \(x_i\) denotes the observed signal and \(w_i\) denotes its learned coefficient.

**编辑说明。** 若书目保留小写姓氏前缀 *del*，可将引文句改为 “Asynchronous signals were aligned by del Río and Grey [8].” 以保留原拼写。
