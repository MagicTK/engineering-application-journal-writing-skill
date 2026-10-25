# Actual Aggregation-Check Baseline

This baseline is an inspection of existing guidance and exact synthetic arithmetic, not a baseline model response. The retained v4.2.7 repetition guide already states that mean run-wise F1 is not generally F1 computed from mean precision/recall, and distinguishes pooled predictions and representative runs. It was not missing that rule.

The candidate adds a bounded complementary check: fixed true-class support weights commute with the outer run average, and full single-label support-weighted recall equals accuracy under matched scoring definitions. Exact count fixtures demonstrate both valid nonlinear differences and genuinely inconsistent summary cells. Variable supports, selected classes and multilabel subset accuracy are separate cases. This is a scoped instruction improvement, not a claimed baseline reasoning failure or controlled general gain.
