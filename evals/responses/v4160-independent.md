# Fictional Forecast/Life Final Response

One fresh task context answered the same two requests on the frozen final source; only the read root changed. The earlier response already passed core science and writing. The new record changes maintained evidence availability, not a demonstrated general writing gain. Wrappers, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

Preset project summaries and writing preferences were available; this was not a memory-blank test. Release findings below come only from the permitted package. No files were changed, external sources opened, training or delegation performed, or credits/resets used.

**Actual Reading List**
Read the entrypoints and relevant passages in these eight files, all under the immutable root; the entrypoint reports version **4.1.60**:

- [SKILL.md](../../SKILL.md)
- [Abstract/contributions companion](../../skills/engineering-abstract-contributions/SKILL.md)
- [Evidence-design companion](../../skills/engineering-experiment-evidence-design/SKILL.md)
- [Abstract and contribution craft](../../references/abstract-and-contribution-craft.md)
- [Terminology decisions: forecast targets and life quantities](../../references/terminology-decisions.md)
- [Terminology bank: admission rule and matched records](../../references/engineering-application-terminology-bank.md)
- [Published-evidence index: forecast/life passage records](../../references/published-evidence.md)
- [Evidence guide: split integrity and forecast/life evaluation](../../references/experiment-evidence-design.md)

**A. Targets, Outputs, Evidence**
**1. Capped-life prediction**

| Reference cycle | Uncapped remaining life | Supplied training target |
|---|---:|---:|
| \(t=40\) | \(260-40=220\) cycles | \(100\) cycles |
| \(t=220\) | \(260-220=40\) cycles | \(40\) cycles |

The plateau belongs to the capped label, not physical remaining life, which continues decreasing. Known historical failure times may legitimately construct supervised targets without becoming inference inputs. Sensor sampling frequency does not establish a cycle’s physical duration.

**2. Temperature forecasting**

The output is a six-value future temperature trajectory, not RUL. A specified upper-limit rule can convert it into prospective crossing indications. Lower trajectory RMSE alone establishes neither longer warning lead, fewer missed events, RUL accuracy nor an implemented alarm. These require their own target, decision-rule, event/timing or implementation evidence.

Future-indexed planned commands genuinely known at issue time can be legitimate exogenous inputs. Later realized sensor readings are unavailable to that issue-time forecast; their index alone is not the deciding criterion.

**3. Split and access checks**

A chronological split can assess future prediction on known assets. Unseen-asset claims require corresponding entity-held-out evidence. Randomly separating heavily overlapping same-asset windows and fitting normalization on the full future trajectory are **not sufficient** for a causal unseen-asset claim.

Targeted author checks are:
- State the intended population, asset/run identifiers, issue times, input cutoffs and prediction horizons.
- Map raw input/target timestamps across partitions; distinguish legitimate shared historical context from leakage through overlapping windows or target periods.
- Verify entity-held-out separation for unseen-asset claims and training-only fitting of normalization and other selected preprocessing.
- Trace historical endpoint labels separately from prediction inputs, and check that model selection excludes held-out outcomes.

These are checks on the declared task, not instructions to delete data or substitute another task.

**4. Maintained terminology evidence**

**Yes**, the release maintains a dedicated RUL pair and a separate Chinese wording record:
- **P45, p.6, Section IV-A:** window-linked RUL labels constructed from completed run-to-failure trajectories, with a maximum RUL.
- **P81, p.3, Section III-A; p.6/Section V:** measurement-to-RUL regression, distinguishing engine-life labels and an etching-system TTF application.
- **Separate Chinese record:** paired titles/abstracts in Chinese Journal of Engineering DOI `10.13374/j.issn2095-9389.2019.10.10.005` and battery article ID `e8a2f2f8-f620-4dba-8882-355fe77d5255` support **剩余寿命** and **剩余使用寿命**. The recorded passages respectively define current-to-useful-end length and a battery endpoint convention.

These are maintained reading records, not fresh verification of the external sources. The shared engine convention is not independent invention; indexing, normalization, complete networks and performance remain uncertified. The Chinese HTML lacked complete method equations. **P95, pp.3–4, Section 2.1**, instead records trajectory forecasting followed by operating-limit alarms; its prognosis title does not establish RUL.

Neither the causal-convolution nor knowledge-distillation row admits **Causal Life-Preserving Horizon Module** as a complete generic name. One namesake source supports, at most, appropriately attributed source-specific use. An author-approved new proposal remains permissible with an operational definition, but its name supplies neither novelty nor physical causal/life-preservation evidence. An absent maintained record is not proof of invalidity.

Method sentence, **25 words**:
A scalar regressor is trained on historical run-to-failure trajectories to predict remaining useful life in operating cycles, with targets capped at 100 cycles as \(y(t)=\min(100,T_{\mathrm{failure}}-t)\).

**B. Synthetic Drafts**
These are fictional writing artifacts, not experimental evidence. ProcessHorizonNet retains its approved English name; Chinese naming and novelty remain unapproved/pending. Counts use whitespace-separated words, with hyphenated forms counted as one.

Abstract, **127 words**:
Operating changes alter future temperature behavior, complicating six-step process-temperature forecasting. ProcessHorizonNet addresses this task using measured process variables and recorded operating inputs available through each forecast issue time. A temporal encoder produces two feature histories representing sensor measurements and operating inputs. An input-dependent gate weights and combines these histories so that their relative contributions can vary across forecast issues. The combined representation supplies a direct multi-output regression head that predicts six future temperatures. Evaluations on a simulated process benchmark and an independent recorded production case compare this design with the same network using fixed feature-combination weights under matched data, splits, and seeds. Average trajectory RMSE is lower in both cases, although production-case sixth-step RMSE is higher. Alarm-event F1 remains unchanged under a separately specified production-case limit-crossing evaluation.

Contribution, **35 words**:
ProcessHorizonNet combines encoded sensor and operating-input histories through an input-dependent gate for direct six-step temperature regression; matched comparisons yield lower average trajectory RMSE in both cases, with higher production sixth-step RMSE and unchanged alarm-event F1.
