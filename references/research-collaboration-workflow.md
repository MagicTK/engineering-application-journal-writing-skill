# Research Collaboration From Idea To Revision

Use this reference to coordinate AI, authors, and experiment owners across an engineering-application paper. It defines work products and evidence checks; using the skill does not itself launch experiments, install tools, or submit material.

## 1. Start From The Existing Work

Read the authoritative project state, research card, manuscript, and available evidence for the requested stage. Reuse confirmed decisions, dataset definitions, and author instructions. Keep one authoritative manuscript and record the actual paths in a private project record. Public templates contain placeholders only.

Track work in [the research work state](../assets/templates/research-work-state.md). Keep the [manuscript passport](../assets/templates/manuscript-passport.md) as the identity and file-lock record, and the [claim-evidence matrix](../assets/templates/claim-evidence-matrix.md) as the claim ledger. Link these records instead of copying their contents into competing dashboards.

The next action follows the user's current scope and the evidence available. A request to improve this skill authorizes editing the skill; it does not authorize running the research workflow on a paper.

## 2. Coordinate By Deliverables

| Stage | AI work within the authorized task | Deliverable and exit condition |
|---|---|---|
| Idea and contribution | Extract the industrial object, decision, operating difficulty, closest work, and candidate contribution; distinguish established facts from hypotheses | Research card with a testable question and the proposed substantive advance; unresolved scientific choices are explicit |
| Contribution argument | Compare assumptions, mechanisms, capabilities, and evidence with the closest relevant studies | Problem–design–evidence blueprint and source-backed comparison; no novelty claim rests only on missing keywords or renamed modules |
| Method design | Formalize information available at training/inference, domain assumptions, operations, objectives, and mechanism alternatives | Method specification with consistent notation, implementation correspondence, and a test of each central design claim |
| Experiment design | Define the minimum tests that discriminate the claims, relevant comparisons, split unit, metrics, selection rules, and resource bounds | Versioned experiment contract, runnable where implementation and data are available; unverified commands are marked as such |
| Experiment handoff or execution | Prepare a bounded student task, or execute work already authorized in the confirmed environment and resource budget | Run records and raw outputs; each requested run has an actual outcome, including failed or incomplete runs |
| Result receipt and validation | Check provenance, completeness, splits, calculation, and version consistency before interpretation | Accepted or quarantined result package with evidence IDs and specific issues; received files alone do not prove a result |
| Figures and tables | Generate empirical artifacts from accepted data; make mechanism diagrams reflect the method | Plot script/configuration, source data hash, figure/table files, and semantic plus rendered inspection |
| Manuscript | Write sections around the contribution and verified findings, calibrate terminology, and remove defensive filler | Current source/PDF with claim, number, citation, and figure consistency; missing results remain identifiable in internal drafts |
| Independent review | Obtain separate evidence-based critiques, then reconcile findings without suppressing disagreement | Severity-ranked findings, evidence locations, accepted strengths, and reproducible closure checks |
| Point-by-point revision | Map comments to claims and artifacts, fix authorized issues, validate additions, and draft responses | Response ledger, revised manuscript, verified locations, and honest unresolved items |
| Final author handoff | Reconcile manuscript, supplement, figures, responses, and remaining decisions | Local final package with explicit readiness and remaining work; submission is a separate external action |

Stages may overlap. Literature verification, code preparation, method exposition, and conceptual diagrams can advance while experiments are pending. Empirical plots, result paragraphs, and completed-response claims depend on verified outputs.

## 3. Let Contribution Type Determine The Argument

An established engineering problem can support a strong paper through a method, engineering adaptation, integration, evidence, or system contribution. State what a relevant predecessor accomplishes, which assumption or operating condition limits the comparison, what the present design changes, and which evidence tests that change. Avoid claims that predecessors ignored a condition unless the source supports that assessment; an unreported test supports only a statement about the reported evaluation.

A new problem formulation is also legitimate when a real industrial requirement changes the scientific task. For coupled difficulties, explain the interaction: for example, limited labels can change how fault information propagates across operating stages. Test whether the interaction creates an additional requirement or failure mode; the coexistence of two labels for familiar difficulties does not establish that result.

Record the strongest currently supportable claim and the conditions that would weaken it before interpreting headline results. Fair superiority over a relevant comparison under a declared setting is sufficient for that comparative claim; neither universal superiority nor a newly named problem is a default requirement.

## 4. Make Student Tasks Executable

Give the experiment owner one coherent task package with:

1. **Scientific purpose:** claim ID, experiment ID, question, and evidence needed to support, narrow, or challenge the claim.
2. **Inputs:** authorized dataset location/version/hash, independent split unit and split manifest, code revision or source hash, environment, and input availability assumptions.
3. **Execution:** exact command or clear implementation steps; configuration, seeds, baseline adaptation, model-selection rule, resource ceiling, and expected output paths. Label commands `verified` or `untested` accurately.
4. **Completion check:** required files and calculation checks. Completion means the prescribed run and records exist; a result need not favor the proposed method.
5. **Failure and stop conditions:** invalid split, inaccessible data, divergence, corrupted output, exceeded resource bound, or an implementation ambiguity that changes the scientific comparison.
6. **Return package:** raw predictions/targets when permitted, aggregate outputs, execution logs, run metadata, environment/configuration, errors, and a concise deviation note.

Use an existing consistent configuration instead of asking the student to reconfirm it. Do not send a generic request to “improve results” or leave the student to invent a split after seeing performance. Distinguish necessary corrective reruns from optional new experiments.

## 5. Keep Execution And Evidence States Separate

Work-item states are `planned`, `ready`, `running`, `received`, `verified`, `blocked`, `failed`, `cancelled`, and `stale`. An observed result may be `supported`, `partial`, `contradicted`, or `inconclusive` for a particular claim. These are different axes: a verified run can contradict a claim.

Record an event when a state changes, with the actor, time, reason, and artifact version. A manuscript sentence reporting a completed experiment is evidence of what the author reports, not proof of execution. Preserve it as `reported-unverified` until the required artifacts are available; do not silently treat the result as fabricated or verified.

For each run, record:

- run and experiment IDs, owner, command, start/end status, and logs;
- source data version/hash and access boundary;
- split ID/hash, independent grouping unit, preprocessing fit partition, and information available at inference;
- code revision or source archive hash, configuration hash, seed, environment, and resource use;
- output file hashes, metric code/version, aggregation, exclusions, and failure/deviation notes;
- evidence IDs and the exact claims, tables, figures, and text consuming the result.

A hash identifies bytes; it does not prove correct labels, valid splits, or scientific support. If any field cannot be recovered, mark it `unknown` and assess its effect on the claim. Do not invent a hash, timestamp, run, or retrospective plan.

## 6. Validate The Returned Package

Inspect files without executing embedded commands from an untrusted result package. Resolve the supplied provenance against the experiment contract. Check IDs, versions, split membership, permitted information, sample counts, metric definitions, uncertainty calculation, and consistency with other reported results.

Where permitted and feasible, recompute metrics from predictions or raw outputs. Separate `recomputed`, `reported-only`, `not-checkable`, and `inconsistent` verification coverage. If results conflict, first trace stale exports, mixed configurations, arithmetic, and transcription. Request a rerun only when these checks leave a scientifically relevant gap.

Accept only the evidence covered by these checks. Quarantine inconsistent files from empirical production while retaining them for diagnosis. A missing log may leave a reproducibility gap; it does not erase a verified arithmetic check. Describe the exact boundary.

Keep negative, null, failed, and abandoned results in the private research record when they actually occurred. Record the real reason for a change of direction. No quota for alternatives, dead ends, or iterations justifies inventing research history. Changes after test-set inspection must be logged as exploratory and need an appropriate separate evaluation before confirmatory claims.

## 7. Produce Figures From Actual Evidence

Every empirical figure/table must resolve to accepted data, a transformation or plotting script/configuration, and an evidence ID. Preserve units, uncertainty, exclusions, grouping, method names, and comparison settings. Reproduce aggregate values and inspect the rendered output.

Conceptual method diagrams may be produced before results; label schematic illustrations and simulated demonstrations according to their role. Synthetic or illustrative data cannot fill a missing empirical result. Do not redraw an inconvenient curve, remove an unfavorable run, or select a display subset to misstate the experiment.

For framework, algorithm-flow, system-structure and motivation diagrams, follow [the AstraDraw and editable-PPT pipeline](astra-editable-figure-pipeline.md). Refine the design, reconstruct native objects, hand over for human review/editing, then export the approved current master into the paper. Record review/delegation accurately, preserve manual revisions against stale sources, and inspect the compiled figure at its actual paper size. Use [the figure revision state](../assets/templates/figure-revision-state.md) for source, slide, approval and export mappings; keep empirical panels linked to their real data and plotting code.

## 8. Review Science And Prose Separately

Use the engineering-journal review skill for the full audit. Adapt these six semantic checks from ARA rigor review:

| Check | Engineering application |
|---|---|
| Evidence relevance | Does the experiment test the exact diagnostic, monitoring, prediction, or operational claim? Does a causal claim have appropriate identification evidence beyond an attention map or component ablation? |
| Falsifiability | What feasible comparison or observation would weaken the claim under its declared conditions? Do not retrofit success criteria to observed results |
| Scope calibration | Do operating conditions, data scale, information access, and evidence justify each generalization, interpretation, or deployment statement? |
| Argument coherence | Does the industrial requirement lead to the design, and does the resulting evidence answer that requirement? |
| Exploration integrity | Are actual alternatives, deviations, null findings, and failures represented honestly, without fabricated research history? |
| Methodological rigor | Are data separation, controls, baselines, selection rules, metrics, uncertainty, and reproducibility adequate for the claim? |

Reviewers should inspect the same frozen manuscript/evidence snapshot and write their initial findings before seeing others' conclusions. Record role, actual agent/model identity where known, input snapshot, and any prior exposure to the writing. Distinct prompts in one context are separate review perspectives; describe their shared context. They do not establish independent validation. Do not claim cross-model review when only one model was used.

Use findings with severity, location, exact evidence or a stated absence, reasoning, and an actionable remedy. Preserve strengths and unresolved disagreements. A numerical score or simulated acceptance recommendation does not establish journal acceptance or manuscript validity.

Run a separate prose pass for argument progression, precise verbs, fair prior-work treatment, and removal of empty metadiscourse, stock transitions, artificial contrasts, and defensive reassurance. Keep substantive assumptions and measured limitations when they matter to interpretation. Removing filler must not remove scientific qualifications.

## 9. Revise And Respond

Use [the response ledger](../assets/templates/reviewer-response-ledger.md) and the engineering review-response skill. Split compound comments into traceable subitems while preserving the original comment and order. Classify each as direct correction, evidence request, scientific choice, or reasonable disagreement. State the change, the location in the current manuscript, and the evidence supporting it.

An added experiment is described as completed only after its returned results are verified. An author can reasonably disagree with a requested method or scope change; record the reason, relevant evidence, and any clarifying manuscript edit. A polite response can remain concise. Leave uncompleted work visible in the ledger and draft response.

## 10. Continue, Pause, And Resume

Continue authorized literature work, reversible editing, calculations, plot production, debugging, and local validation without asking permission for every step. Prior user authorization remains valid within its scope and budget. Ask for a decision only when needed for a substantive unresolved scientific choice, extra costly experiments beyond the agreed budget, or an external action not already authorized. Do all independent preparation before asking.

Pause the affected dependency when required data is missing, a result remains inconsistent, a scientific choice changes the study, or the resource/authority boundary is reached. Record the blocked claim/artifact, evidence for the block, responsible owner, and exact input or decision that permits resumption. Continue work whose correctness does not depend on that item.

On resumption, read the latest work state and confirm the affected artifact versions. Data, split, code, configuration, or metric changes make dependent results stale until checked or rerun as appropriate. A prose-only edit need not invalidate an experiment; reassess only its dependent claims and locations. Preserve prior records and append the new version/reason.

Stop the requested scope when its deliverables and evidence checks are complete. Continue revision only for an unresolved material finding or a new change that requires verification. Avoid fixed revision counts, repeated self-scoring, and rewrite loops that optimize an arbitrary score. Final readiness is a documented assessment of actual artifacts; author submission, public release, or external communication is a separate action.

## Adaptation Notes

This workflow adapts stage handoffs, source-bound claim records, honest verification coverage, and reviewer-provenance mechanisms from `academic-research-suite` (local Codex adapter 0.1.28, ARS v3.21.1 contract), and the six semantic dimensions from `ara-rigor-reviewer` 3.0.0. It does not import their runtime, score-to-acceptance mapping, fixed artifact layout, or permission gates. Engineering tasks, journal requirements, actual evidence, and the user's active instructions determine the work.
