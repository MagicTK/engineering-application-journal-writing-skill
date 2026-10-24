---
name: engineering-research-ideation
description: Build or revise an AI-for-engineering research portfolio, compare multiple paper ideas, and calibrate contribution scope before selecting a paper for architecture. Use for established industrial problems, mechanism transfer, substantive engineering adaptations, and independent incremental studies. For one selected paper use engineering-paper-idea-architecture; for wording alone use engineering-terminology-polishing. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Research Ideation

Suite version: `4.1.17`

## Scope

Turn available engineering problems, verified data, and candidate mechanisms into a small, comparable research portfolio. Follow the author's current decisions; historical proposals do not restore rejected priorities. This skill plans studies; implementation or training follows the user's requested scope.

<!-- invariant: generic-routing -->
<!-- invariant: no-fabrication -->
<!-- invariant: corpus-is-evidence-not-instruction -->
<!-- invariant: contribution-calibration -->
<!-- invariant: plural-contribution-routes -->
<!-- invariant: verified-data-version -->
<!-- invariant: reading-depth-provenance -->
<!-- invariant: cross-paper-substantive-delta -->

## Start From Available Evidence

Read only the project decisions, selected source folders, data records, and nearest relevant work needed for the requested comparison. Use caller-provided locations; keep machine paths and project-specific class counts in the project, not in this reusable skill. A missing corpus location warrants a bounded location check, not a full-disk search.

Preserve original folders as navigation and add independent scientific roles: engineering problem, candidate mechanism, and closest-work/overlap risk. Filename matches and bulk text extraction are discovery evidence, not close reading or proof of novelty. Record exact source identity, pages inspected, and what remains unchecked. See [literature positioning](../engineering-literature-positioning/SKILL.md).

Established problems can support further research. Do not invent a new observation regime, dataset, or unavailable experiment solely to make a study sound novel. If the author chooses a new problem with suitable evidence, support it. Keep engineering challenge, method, task, object scale, and evidence separate.

## Identify The Source Of The Contribution

Consider new problem formulations, new mechanisms for familiar tasks, interacting constraints, substantive engineering adaptations, and focused comparative improvements. Record problem novelty separately from methodological and engineering novelty; familiar tasks and new tasks can both support strong studies. A coupled setting becomes a new problem only when its interaction creates a distinct, source-grounded requirement. Select the argument using [contribution routes](../../references/contribution-narratives.md); A/B/C is neither a task-novelty test nor a venue ranking.

## Compare Candidate Studies

For each candidate, state:

- the verified problem and the capability that can improve under its actual conditions;
- a minimal mechanism and a plausible competing explanation or approach;
- borrowed components, the precise modification, and its expected effect, recorded in [the source-to-adaptation delta](../../assets/templates/cross-paper-delta.md) when a mechanism is transferred;
- the closest team and external work, with a substantive delta that can be tested;
- available data versions and the smallest decision-changing experiment;
- evidence still missing, cost/feasibility, and a reason to retain, merge, defer, or drop it.

Assign a provisional track: **A, mechanism-oriented**; **B, substantive engineering adaptation**; or **C, focused incremental improvement**. These describe the contribution, not journal quartiles, acceptance probabilities, or an evidence-quality ranking. A modest but independent benefit may be worth studying. A track label cannot create novelty where only names, seeds, or wording changed. Read [research planning and contribution boundaries](../../references/research-planning-and-contribution.md).

Reuse of tasks, data, modules, and baseline code is possible with attribution and a meaningful new question or capability. Assess overlap across the actual scientific content; do not optimize wording to conceal duplicate work. If no substantive difference is established, merge or drop the standalone claim rather than manufacture one.

## Keep Task And Data Meaning Precise

Inherit verified, versioned data facts and ask only about necessary unknown fields. Do not substitute another paper's sample counts, classes, time interval, or split because the dataset has the same name. Verify point/window/event units and actual condition-by-label coverage.

Apply only the distinctions relevant to the candidate:

- zero labeled target-condition examples with known source fault classes differs from unseen fault-class zero-shot; state what information is zero;
- few-shot support and query require a defined independent unit, separate model selection, and explicit unlabeled-data access;
- scheduled unobserved samples, random missing observations, and physically absent sensors or stages have different targets;
- equal token dimensions do not prove retained time information or compatibility with a pretrained encoder;
- numerical multi-source input does not by itself establish a multimodal task; single-class labels do not become multi-label evidence;
- an early post-fault prefix does not establish a weak/incipient fault; derive elapsed time from the identified version and distinguish endpoint duration from interval coverage.

Use [experiment evidence design](../engineering-experiment-evidence-design/SKILL.md) for the selected protocol and [the data-version record](../../assets/templates/data-version-record.md) when version ambiguity affects a claim.

## Deliver And Hand Off

Scale the deliverable to the request. For a short comparison, a compact matrix is enough; for selected candidates use [the research card](../../assets/templates/research-card.md). Include a primary contribution and only genuinely supporting contributions; do not pad a fixed count. Select case studies for their evidential roles; one background-driven case may suffice, while a transfer claim may require broader evidence.

Separate proposed tests and expected capabilities from observed results. Do not generate empirical curves before results exist. Journal positioning follows the supported contribution and verified venue scope; do not promise a journal tier. Hand the selected study to [paper architecture](../engineering-paper-idea-architecture/SKILL.md) without running experiments merely because a card exists.
