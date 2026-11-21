# Evidence in passage revision

Five independent fresh respondents each read one snapshot of the same English section-writing guide. They received the same three prompts together in the same order, a 450-word overall limit and no answer key or additional source. Each respondent answered once. The prompts are in the [current forward report](../forward-test-report.json). The baseline is the published main-branch guide at revision 8f9260a. This is a small, qualitative guide-level test. There was one reader per snapshot and the intermediate revisions responded to observed failures; between-reader variation precludes a causal performance estimate.

One earlier developmental example supplied all six threshold values in the draft. A reader repeated those values and inferred what an unseen panel showed. The new A brief deliberately withholds both the values and captions. The proposed alarm, source estimator and documents are fictional. In B, the public source confirms semiconductor manufacturing pass/fail labels and missing measurements. Median substitution and the observation-mask comparison are proposed here; they are not published SECOM results. B was a separately constructed transfer brief, not the example used to draft the new instruction. The [UCI SECOM dataset description](https://archive.ics.uci.edu/dataset/179/secom) is by McCann and Johnston. Case C is a positive control with supplied author names, caption contents and an equation.

| Guide | A. Source scope, missing evidence, prospective control | B. SECOM transfer | C. Verified names, figure and formula |
|---|---|---|---|
| [Baseline](../responses/v451-baseline.md) | Correctly left thresholds and panels open. The table compared two studies rather than the six planned arms. | Passed | Passed |
| [First revision](../responses/v451-candidate.md) | Specified a matched comparison but introduced one run per setting. The brief supplies no replication count. | Passed | Preserved the supplied family-name spelling in the editorial alternative. |
| [Second revision](../responses/v451-retest.md) | Correct on thresholds and repeats. Assigned the earlier study's two clocks to the new alarm without source evidence. | Passed | Passed |
| [Third revision](../responses/v451-validation.md) | Passed | Passed | Panel contents were correct but the first mention made the figure the subject, contrary to the requested content-first style. |
| [Final snapshot](../responses/v451-release.md) | Left all six values, repetitions and panel assignments unspecified. Named the varied parameter, shared fitting conditions and common test records. | Preserved prediction-time availability, training-only medians and matched records. | Retained the verified compound surname and citation, led with the observed bands and continued the equation with definitions. |

All three final responses met the scoped criteria. Earlier rows remain available to show what the successive instructions missed.

A result in the table is a judgment on the stated writing task. No classifier, dataset evaluation, or assessment of manuscript acceptance was carried out. The SECOM answers specify a proposed training split and comparison, not an already verified division of that dataset.

## Evaluated guide fingerprints

- baseline: 6fe9932252bf488c92d4bcc1241ebfb2aec48444e674e8388fd189c302d04d9f
- revised: 2f4f644f11aeb96d938ae00c90af3ff19c7f3b05136a46aba1b527420c60e879
- retest: 81b3c91e7b62d3153c93f1a2c2a58f79f56943dcec394702a2c4e4ab19319599
- validation: ede01669202a677ffdc1611253901b2c2122a84d1009219f7d7ca3b7cbf041f5
- release: 5389f1dcb53e67b07073f76914f0cb9649178fd6681f1b791779ebab0e5bde73
