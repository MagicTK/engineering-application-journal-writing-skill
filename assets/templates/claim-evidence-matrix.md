# Claim-Evidence Matrix / 主张-证据矩阵

## Status Vocabulary

- `unverified`: claim or value has no traceable source.
- `source-confirmed`: background fact or definition is verified.
- `setting-confirmed`: experiment setup is verified.
- `result-verified`: result is traceable to data, code/log, and metric calculation.
- `text-synchronized`: all manuscript mentions use the verified result.
- `layout-verified`: final figure/table and PDF presentation are checked.

## Matrix

| Claim ID | Claim | Type | Required evidence | Source artifact | Status | Allowed wording | Manuscript locations | Owner |
|---|---|---|---|---|---|---|---|---|
| CL-01 | | problem/method/result/engineering/deployment | | | unverified | | | |

## Consistency Links

| Result ID | Main table | Ablation | Figure | Abstract | Results text | Conclusion | Run/split ID |
|---|---|---|---|---|---|---|---|
| R-01 | | | | | | | |

## Rule

Do not promote a result claim beyond `result-verified`. An online/deployment claim requires `EO` evidence; external generalization requires `EX`; measured operational benefit requires `EV`. None can substitute for another.
