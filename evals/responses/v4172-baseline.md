# Fictional Imputation-Interface Baseline

One context answered A/B on immutable v71. Science, arithmetic, prose and its finding of an existing P25/P33 admission already pass. This is not a missing-base-term repair. Wrappers, local links and whitespace are normalized; raw records remain private.

**Request A**
Completion uses the supplied input mask, not the reference mask:
\[
c=M\odot x_{\mathrm{input}}+(1-M)\odot z=(0,12,99,30).
\]
The finite placeholders at unavailable input positions do not affect this selection.

- Artificially withheld entries with known references: \(H=R\odot(1-M)=(0,1,0,0)\).
- Scoreable hidden-entry count: \(\sum_i H_i=1\).
- Missing-entry MSE: \(\displaystyle\frac{\sum_{i:H_i=1}(c_i-x_i^{\mathrm{ref}})^2}{1}=(12-10)^2=\mathbf{4}\).

Entry 1’s zero is a valid observation. Entry 3 genuinely lacks a reference, so it cannot enter reference-based recovery scoring; its estimate, 99, is not ground truth. There are two unavailable inputs but only one scoreable hidden reference.

Scoring all known entries after reinserting measurements gives \((0+4+0)/3=4/3\). This mixes copied observations with one estimated value and cannot establish accuracy at every missing entry.

An originally observed value deliberately hidden **inside TRAIN** may legitimately remain a training-supervision target. A held-out evaluation reference instead remains scoring-only and must not guide fitting, preprocessing, or selection. Neither observed-entry reconstruction loss nor prefill alone establishes unknown-entry accuracy. Derive each mask’s meaning from its definition, not its name. Replacing numerical candidates changes values; updating trained parameters changes the model. These are different operations.

**Terminology Check**
The local release **does contain a completed, scoped matched-definition record** for **missing-value imputation**: P25, p.4, §3.1, and P33, p.5, §IV-B, Eqs. (13)–(15). It separately records **缺失值插补**, supported by the bilingual title/abstracts of *Acta Automatica Sinica*, DOI `10.16383/j.aas.c230534`.

I checked those local records, not the cited publications anew. They support the base operation and wording, not every compound name or architecture. An absent record would indicate incomplete bank admission, not invalidity.

**Request B**
Counts use whitespace-separated words; hyphenated compounds and numerals count as one word. Labels and notes are excluded.

1. Abstract/method chain: **47 words, 3 sentences**.
An imputer learns from incomplete training measurements using observed-entry reconstruction targets and estimates missing auxiliary measurements. Merging these estimates with available original measurements provides completed inputs for a quality regressor trained on available quality labels. Both fitted components remain frozen when estimating quality from permitted test windows.

2. Candidate contribution: **29 words, 1 sentence**.
To support quality regression from incomplete auxiliary measurements, the framework preserves available measurements while completing missing inputs, enabling a quality regressor to learn from the available training quality labels.

3. Analytical result: **28 words, 1 sentence**.
In the supplied four-entry example, the sole artificially withheld entry with a known reference was estimated as 12 against 10, yielding a missing-entry mean squared error of 4.

**Author/Review Notes**
- **Block 1:** Observed-only reconstruction is legitimate imputer fitting without naturally unknown targets. Quality-label supervision trains the downstream regressor, not the imputer’s auxiliary-measurement output; the whole pipeline is therefore not unsupervised. Exact component construction and selection procedures remain unspecified. Preserve the supplied frozen-test and scoring-only-reference boundaries.
- **Block 2:** This states a requirement-to-learner connection, not verified novelty. A contribution claim still needs a distinguishing advance and matching evidence; routine imputation and merging alone do not certify one. This architecture is case-specific, not mandatory for missing-data papers.
- **Block 3:** This reports only Request A’s arithmetic fixture. It establishes neither industrial quality-prediction performance nor naturally unknown-entry recovery.

**Read Log**
Exact absolute paths are provided by the file links. Body sections read are listed below; heading/keyword scans also covered these same release references.

- [Release SKILL.md](../../SKILL.md): entire file, Mission through §9.
- [Abstract/contribution companion](../../skills/engineering-abstract-contributions/SKILL.md): entire file.
- [Terminology bank](../../references/engineering-application-terminology-bank.md): “Scope And Evidence Boundary,” §0, and §11 excerpts including the imputation definition, separate Chinese wording, and scope limitations.
- [Topic playbooks](../../references/topic-playbooks.md): §1; additionally read excerpts of §§2–3, lines 80–208.
- [Experiment evidence](../../references/experiment-evidence-design.md): §3, lines 77–101; §6 through the missing-value recovery/preservation paragraphs, lines 169–195.
- [Mechanism-linked abstracts](../../references/abstract-and-contribution-craft.md): opening and §§1–2; §§4–5.
- [Terminology decisions](../../references/terminology-decisions.md): opening/“Decision Procedure,” lines 1–19; “Topic-Specific Terms,” lines 533–559.
- [Argument and prose craft](../../references/argument-and-prose-craft.md): §§4–6.
- Runtime-required reads: using-superpowers (private local reference) and its Codex tooling reference (private local reference), both entire files.

No files changed, browsing, scientific experiments, external model calls, thread creation, or account-setting changes.
