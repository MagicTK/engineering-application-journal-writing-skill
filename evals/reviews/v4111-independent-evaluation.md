# 4.1.11 Independent Fictional-Case Review

## Scope

One fresh respondent read the frozen 4.1.11 entrypoint and its terminology references, then answered four fictional requests. The maintainer reviewed the actual responses against the predefined behaviors. There was no separate grading agent or baseline run, so these results do not measure improvement over 4.1.10 or certify all skills, translations or scientific methods. No private manuscript, data or experiment was used by the respondent.

## Results

| Case | Outcome | Observed behavior |
|---|---|---|
| A: pooling scope and prose | Pass | Two connected sentences retain temporal encoding, within-unit averaging, concatenation and classification. The explanation rejects unsupported causal/noise claims and distinguishes encoded-position symmetry from raw-input order invariance. |
| B: assignments and hard decisions | Pass | Keeps sample-to-cluster weights separate from variable grouping, physical modes and fuzzy truth. Preserves both soft training assignments and the subsequent hard output without changing the algorithm. |
| C: compound names and Chinese | Pass | Does not admit a complete paper-specific module name from partial max-pooling matches. Requires independent translation evidence, and permits an accurately defined author-proposed name without pretending it is established. The invented translation remains a rejected test stimulus, not a recommended term. |
| D: genuine global readout | Pass | Preserves the whole-plant graph, averages across the supplied node-time axes and connects the readout to its classifier. Does not impose per-unit pooling or invent a separate fusion module. |

The actual response is retained in [v4111-revised.md](../responses/v4111-revised.md). Minor stylistic choices in explanatory Chinese are not editorial prescriptions; passing concerns the stated scientific and writing boundaries. No retest was needed for these cases. The current report stores the exact tested instruction/dependency hashes.

## Deterministic Checks

The first pending report omitted the required explanation for unrun cases and was correctly rejected by the existing validator. Adding that report field resolved the schema failure; no validation rule was relaxed. All 43 unit tests, 14 bilingual-pair checks and 28 official entrypoint checks then passed. Release/export and clean-install verification are separate from this behavioral result.
