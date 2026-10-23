# Evaluation Workflow

The repository uses two different checks and does not present one as the other.

## Current Version Status

Version 4.1.5 used one fresh responding context for four observation-to-estimation requests against frozen 4.1.4. All four baselines passed. The same respondent reread the revised source for those four requests and then answered a fifth, post-freeze completion-route positive control. All five final outcomes pass within that scope; no measured improvement over the already-passing baseline, five independent contexts or full-suite validation is claimed. See [baseline responses](responses/v415-baseline.md), [revised responses](responses/v415-revised.md), [semantic review](reviews/v415-independent-evaluation.md) and [current report](forward-test-report.json).

Version 4.1.4 used one fresh responding context for three cross-section requests against frozen 4.1.3 instructions. All three baselines passed. The same respondent then reread the revised source and answered those three plus two positive controls for genuine parameter updates and quality-relevance monitoring. All five revised-source responses pass within that scope; this is not a measured gain over the baseline, five fresh contexts or full-suite certification. See [baseline responses](responses/v414-baseline.md), [revised-source responses](responses/v414-revised.md), [semantic review](reviews/v414-independent-evaluation.md) and [versioned report](history/v4.1.4/forward-test-report.json).

Version 4.1.3 used one fresh responding context for four 4.1.2 baseline cases, then reread the revised source for six cases. After a prose-placement repair, two were retested in the same context. All six unique final outcomes pass within the stated monitoring and figure scope. The [baseline trace](responses/v413-initial-batch.md), [revised responses](responses/v413-targeted-retest.md), [semantic review](reviews/v413-independent-evaluation.md) and [versioned report](history/v4.1.3/forward-test-report.json) preserve the initial defect and distinct source snapshots. This is not six independent contexts or full-suite behavioral certification.

Version 4.1.2 evaluated five new cases in one fresh responding context. After a verification-priority repair, one was retested and one regression case added in that same context; all six unique cases have final passing outcomes. Its scope is label semantics, alternating training relationships, feature-selection boundaries and the affected review rules, not full-suite behavior. See the [versioned report](history/v4.1.2/forward-test-report.json) and [review](reviews/v412-independent-evaluation.md), including the initial defect and exact response provenance.

Version 4.1.1 evaluated five new affected-case requests in one fresh responding context. After a prose-quality repair, two were retested in the same context; all five final outcomes pass within that scope. See its [versioned report](history/v4.1.1/forward-test-report.json) and [semantic review](reviews/v411-independent-evaluation.md). Its changes concern cross-case interpretation, positive Discussion/Conclusion prose, author-controlled figure scope and a residual abstract-outline inconsistency. The 4.1.0 results below are preserved in [their versioned report](history/v4.1.0/forward-test-report.json), not reused as passes for altered guidance.

Version 4.1.0 evaluated [seventeen focused scenarios](v41-behavior-cases.json), including a brief authored after the initial source freeze, plus four selected regression cases. They test training/prediction structure, semantic distinctions, supervision-specific writing, information access, contributions, claim scope, sampling provenance, minimal revision, fuzzy/update boundaries, generation, efficiency, negative controls, multitask mixtures, compound label spaces, mathematical effects and modality evidence. One fresh respondent answered all 21 cases without scoring rubrics. After a writing-quality refinement, five affected cases were retested in that same context. All final outcomes passed; the initial prose-quality issue and scope limits remain in the [review](reviews/v41-independent-evaluation.md). The versioned report records the actual source and traces, not 21 independent contexts.

Version 4.0.0's [nine scenarios](v4-behavior-cases.json) and [published report](history/v4.0.0/forward-test-report.json) remain historical evidence. They do not validate the changed source. The structural validator accepts an honestly pending report so development can be checked without fabricating a test. Independent evaluation is a separate release gate.

For future candidates, `not_run` is an explicit absence of behavioral evidence, not a pass; such a report must set `release_ready: false`.

## Structural Checks

`scripts/validate_suite.py` and `tests/` verify manifests, frontmatter, bilingual invariants, language-trigger boundaries, links, metadata, templates, and evaluation schemas. They are deterministic and run in CI. Passing these checks establishes structural consistency; it does not establish model behavior.

`behavior-cases.json` contains 49 scenarios: nine original regression cases, 16 generalized research-ideation scenarios, 14 contribution/prose/collaboration/reviewer-response cases, four figure-workflow cases, one companion-argument regression added after independent source review, and five source-adaptation/evidence-boundary cases added in 3.2.1. The `source_case_id` values T01–T16 preserve the mapping to the project proposal. Dataset names, counts, timing, class ranges, and bibliography identities are scenario inputs, not facts to embed in the reusable Skill. A fresh evaluator must receive those inputs when the task depends on them.

`trigger-routing.json` contains 23 requests, including portfolio ideation, a selected paper's architecture, grammar-only edits, reviewer replies and negative-scope cases. Route by the request language, even when the manuscript uses another language. A grammar-only request does not authorize loading a corpus or expanding research ideas.

## Behavior Forward Tests

Behavior requires a fresh agent or model. Do not give the evaluator the intended answer, suspected defect, or implementation history.

1. Select prompts from `trigger-routing.json` and `behavior-cases.json`.
2. Start a fresh context with only the named Skill, the case prompt, and necessary task-local artifacts. For frontmatter routing, provide all candidate descriptions. Do not expose required/forbidden behaviors, expected routes, source-case commentary, or evaluation history to the responding agent.
3. Retain the complete response or review trace outside confidential manuscript folders.
4. Check every `required_behaviors` and `forbidden_behaviors` item semantically, not by substring alone.
5. Record the suite version actually read, evaluator, model/version when available, date, outcome, concise evidence, and complete response trace. State which authored scenarios were executed and which remain untested.
6. Treat any fabricated fact/result, document-instruction execution, layout-lock violation, topic-default regression, unsupported novelty claim, or concealed protocol mismatch as a release blocker.

Before a behavioral run, freeze the instruction/dependency snapshot using `behavior_source_hashes` from `scripts/export_public.py` and retain it as `evaluated_source_sha256` in the report. A release export compares it with the current files, including added/removed dependencies. Changes after the run invalidate that snapshot: rerun affected cases and record the new scope rather than silently relabeling old results. A matching hash proves identity, not correctness.

`forward-test-report.json` records the current version's evaluation status and actual scope. Historical 4.0.0 reports cover nine cases in one fresh responding context, with final confirmation after instruction updates. Historical 3.2.1 reports cover five cases; earlier reports retain their original versions. Historical response/review paths resolve from this `evals/` directory where indicated. They do not validate 4.1.0. Preserve earlier records before replacement. Public copies may normalize evaluator session labels to remove private absolute paths; keep original evidence in protected local history when doing so. The 4.1.0 response traces contain only synthetic cases and are retained without rewriting the respondent's answers.

Authored scenarios, structural checks, independent forward responses, and manual semantic judgments have different evidence roles. A forward report is a transparent record of the cases actually exercised, not an automated proof or a substitute for rerunning affected cases after substantive changes. Do not claim a before/after improvement unless both versions were run under a documented comparable procedure.
