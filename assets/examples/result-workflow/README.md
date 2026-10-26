# Results, Figure And Prose From One Fixture

[中文](README_CN.md) | [Execution guidance](../../../references/experiment-execution.md)

**Original fictional teaching data. No models were trained and no measurements
were acquired.** This example shows how a confusion-matrix fixture can support
a consistent table, plot and result passage. It is not evidence that a method
works in an industrial process.

## Run It

Python 3.7+ and Matplotlib are needed to render the figure. If Matplotlib is not
available, install it in an environment you control (`python -m pip install
matplotlib`); installation is optional for reading the saved example. No API key,
GPU, network service or model training is used by the builder.

From the repository root:

```bash
python assets/examples/result-workflow/build.py --output demo-results
```

The destination must not exist. The command creates `table.md`, `summary.csv`,
`macro-f1.png` and `evidence.json`, without changing the fixture or manuscript.
The record includes input/builder hashes, table IDs, unrounded summaries,
environment versions and artifact hashes. These identify what produced the
outputs; they do not establish scientific validity. Font/rendering versions may
change image bytes without changing the metric values.

## Read The Outputs

![Fictional macro-F1 example: open markers show three constructed tables per method; filled markers show the mean with one sample SD.](macro-f1.png)

The [generated table](table.md) uses mean +/- sample standard deviation (ddof=1)
over three constructed outcome tables per method. Compute each metric separately
in each table, then summarize those values. The JSON and CSV use the 0-1 scale;
the displayed table and plot use percentages. The accompanying SD is therefore
in percentage points, not a relative percentage change or a confidence interval.

**Example result passage, limited to this fictional fixture:**

> In this constructed example, Variant B has a higher mean macro-F1 than Reference
> A (82.73% versus 79.90%), with a larger between-table standard deviation (2.33
> versus 0.75 percentage points). The second outcome table instead favors
> Reference A, with macro-F1 scores of 80.74% and 80.06% for Reference A and
> Variant B, respectively.

**Figure caption:** Macro-F1 in a fictional teaching example. Open markers show
the three constructed outcome tables for each method; filled markers and error
bars show their mean and one sample standard deviation (ddof=1). The vertical
axis spans 75-90% to make the variation visible. The tables are
constructed inputs, not repeated training runs.

The passage reports both the aggregate difference and the exception. It does not
turn a larger mean into an all-run win, a significance claim, or proof of model
stability. SD bars describe these constructed values; they do not measure an
unknown population's uncertainty.

## Adapt The Reasoning, Not The Numbers

The fixture stipulates the same 100 fictional test examples, including 80 normal
and 20 fault examples, for each table. Rows are reference classes and columns are
predictions. Pooling three tables per method yields 300 decisions, not 300 unique
test examples. Confusion matrices alone cannot verify shared sample identities.
Mean F1 and F1 from pooled counts are also different summaries.

For a real study, use authorized immutable outputs and specify the actual
repetition unit, sample identities, class order, split and metric definition.
Missing or failed runs need an explicit status and justified treatment; silently
dropping them or substituting zero changes the summary. This fixture-specific
builder refuses missing/duplicate tables, mismatched supports and existing
output paths; it is not a general research evaluator or a replacement for
experiment records.

Preserve an approved figure design when making a local correction. This example
does not prescribe three runs, macro-F1, error bars, this plotting library or
this sentence structure for every paper. The numerical output is reproducible;
the choice and scope of the scientific claim still require author judgment.
