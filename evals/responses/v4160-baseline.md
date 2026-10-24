# Fictional Forecast/Life Baseline

One task context answered two requests on immutable v4.1.59. Core science, arithmetic and writing already passed. One private runtime-quota sentence is redacted; wrappers, local links/line suffixes and whitespace are normalized. Scientific content is unchanged; raw records remain private.

Preset context included summaries of earlier Skill releases and terminology reviews; I did not use them as evidence for v4.1.59. [Private runtime quota detail omitted.] No files were modified, and no browsing, training, delegation, reset, or credit action was performed.

**Package Reading**
Read the main entry and abstract companion; selectively read or searched the relevant passages in these package files:
- [SKILL.md](../../SKILL.md): routing, evidence boundaries, name admission.
- [Abstract companion](../../skills/engineering-abstract-contributions/SKILL.md): mechanism linkage and contribution scope.
- [Abstract craft](../../references/abstract-and-contribution-craft.md): connected prose, contribution calibration, mixed findings.
- [Terminology decisions](../../references/terminology-decisions.md): referents, information timing, forecasting and warning distinctions.
- [Terminology bank](../../references/engineering-application-terminology-bank.md) and [Chinese bank](../../references/engineering-application-terminology-bank_CN.md): admission rules and targeted RUL/causal-filter/distillation records.
- [Published evidence](../../references/published-evidence.md): P45/P46, P81/P82 and associated passage notes.
- [Evidence design](../../references/experiment-evidence-design.md): split integrity, preprocessing, issue-time access and event timing.
- [Taxonomy](../../references/industrial-ai-taxonomy.md) and [topic playbooks](../../references/topic-playbooks.md): targeted task-label and feature-combination checks.

**A. Outputs, Targets And Evidence**
**1. Capped-life predictor**

| Current cycle | Uncapped remaining life: `260 − t` | Supplied target: `min(100, 260 − t)` |
|---|---:|---:|
| `t = 40` | 220 cycles | 100 cycles |
| `t = 220` | 40 cycles | 40 cycles |

The plateau belongs to the **capped target**, not physical remaining life. Values above 100 cycles receive the same label even while uncapped remaining life decreases. Known historical failure times may define supervised training targets without becoming inference inputs. Sensor sampling frequency does not establish the physical duration of an operating cycle.

Method sentence, **36 words**:
A scalar predictor is trained on historical trajectories to estimate remaining life capped at 100 operating cycles, using targets defined as the minimum of 100 cycles and the recorded failure cycle minus the current operating cycle.

**2. Six-step temperature predictor**

Its output is six future temperatures, not failure time or RUL. A specified upper-limit rule can convert those predictions into prospective crossing indications within the forecast horizon. Lower trajectory RMSE alone establishes neither longer warning lead, fewer missed events, RUL accuracy, nor an implemented alarm.

Future indexing is not itself disqualifying: planned commands genuinely known at issue time may be declared exogenous inputs. Later realized sensor readings are unavailable inputs for that earlier forecast, although they may subsequently supply training or evaluation targets. B retains its narrower, supplied through-issue-time input specification.

**3. Split and preprocessing checks**

A chronological split can evaluate future prediction for known assets. Randomly splitting heavily overlapping windows from one asset does not provide unseen-asset evidence; fitting normalization on its full future trajectory also violates the stated prospective fitting boundary. Neither arrangement establishes physical causality.

Targeted author checks are to identify the intended population; recover asset/run IDs and each window’s input/target timestamps; inspect shared observations and future targets across partitions; distinguish legitimate available historical context from leakage; trace normalization and tuning fit sets; and verify entity-held-out evidence wherever unseen-asset performance is claimed. Preserve the data and task, and flag unsupported claims without silently redesigning the study.

**4. Maintained terminology evidence**

**No completed RUL-specific two-context admission record plus separate Chinese wording check was found in the permitted package references.** That is a maintained-record gap, not evidence that RUL is invalid.

| Actual record | Recorded passage and supported scope |
|---|---|
| **P45/P46: knowledge distillation** | Bank line 378 and published-evidence line 501 describe P45 pp.3-5 matching teacher hidden features/regression targets; P46 pp.3,5-6 supplies multisensor-to-single-sensor guidance. This is a distillation pair, not two matched RUL definitions. |
| **P81/P82: causal convolution** | Bank line 381 records P81 p.3, III-B/Eq.(1), using present and dilated historical positions; P82 p.3, §3.1/Fig.3, explains historical temporal extraction. This supports time-indexed filtering, not RUL definitions or physical causal identification. |
| **Separate Chinese checks** | Bank line 452 records **知识蒸馏**, JOS 006933, bilingual title/abstracts. Line 467 records **因果卷积**, AAS c230634 abstracts/Fig.2 and the electrical-engineering source §3.1.2. These concern those base terms, not RUL; equation-access limitations remain recorded. |
| **Task mentions** | Taxonomy **T6**, line 60, lists future trajectories, remaining useful life and degradation horizons. Chinese-bank line 130 lists 寿命预测. Neither is a matched definition pair or independent Chinese wording-verification record. |

P45’s RUL title and P81’s prognosis title cannot supply the missing definition checks. Likewise, one namesake source does not admit **Causal Life-Preserving Horizon Module** as a generic category through its familiar head words. Preserve source-attributed use where appropriate. An author may approve a genuinely new, operationally defined proposal, but its name cannot establish physical causality or life preservation.

**B. Synthetic Draft**
These are fictional writing artifacts, not experimental evidence. ProcessHorizonNet’s approved English name is retained; no Chinese name or established-novelty claim is added. Counts use whitespace-separated words, with hyphenated compounds counted once.

Abstract, **121 words**:
Operating changes complicate multistep process-temperature forecasting by altering future temperature behavior. ProcessHorizonNet addresses this task using measured process variables and recorded operating inputs available through each issue time. A temporal encoder produces sensor-feature and operating-input-feature histories. An input-dependent gate combines these histories, allowing their relative contributions to vary with the available inputs. A direct multi-output regression head maps the combined representation to six future temperatures. Evaluation on a simulated process benchmark and an independent recorded production case compares ProcessHorizonNet with the same network using fixed feature-combination weights under matched data, splits, and seeds. Average trajectory RMSE is lower in both cases. In the production case, however, sixth-step RMSE is higher, while alarm-event F1 under a separately specified limit-crossing evaluation is unchanged.

Contribution draft, **37 words; novelty pending**:
ProcessHorizonNet connects encoded sensor and operating-input histories through input-dependent combination to direct six-step temperature regression, yielding lower average trajectory RMSE than fixed combination weights in both cases, with higher sixth-step RMSE and unchanged alarm-event F1 in production.
