### A. Revised passage

The valve-wear estimator in [12] aligns asynchronous measurements by time before estimating wear. For fault detection, the proposed alarm uses a clock-aware mask. A planned sensitivity analysis will evaluate how the choice of mask threshold affects the alarm.

| Planned comparison | Quantity varied | Proposed controls | Outcome to compare |
|---|---|---|---|
| Six settings of the same mask | Mask threshold | Use the same sensor records, fitting and calibration procedure, and held-out observations at each setting. | Faults detected and false alarms at each setting |

**Author note.** Supply the six threshold values before running the comparison. Check Fig. 1(a), Fig. 1(b), and Table 2 against their captions before assigning cross-references.

### B. Prospective paragraph

The public UCI SECOM dataset pairs semiconductor manufacturing measurements with pass/fail outcomes. When a measurement is missing, median imputation supplies a value but leaves the classifier unable to tell from that value alone whether it was observed. We will compare a classifier given median-imputed measurements with one also given a binary indicator of availability for each measurement. This comparison asks whether knowing which measurements were available helps identify failed cases.

**Minimum check.** Fit the medians on the training data and use the same split, imputed values, classifier, and fitting procedure in both arms. Verify that the mask records availability at prediction time. On the same held-out cases, compare failure recall alongside the false-alarm rate among passing cases.

### C. Manuscript wording

Del Río and Grey [8] aligned asynchronous signals.

Figure 2 places the observed bands in panel (a) alongside the alarm state for each window in panel (b).

The alarm weights each observed signal according to
\[
g_i = w_i x_i,
\]
where \(x_i\) denotes the observed signal indexed by \(i\), \(w_i\) is its learned coefficient, and \(g_i\) is the resulting weighted signal.

**编辑备注**　连续行文可写作 “The signal alignment method of del Río and Grey [8] …”，以保留书目中复姓 del Río 的原有大小写。
