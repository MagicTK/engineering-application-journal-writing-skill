---
name: engineering-experiment-automation
description: Plan or operate reproducible industrial-AI experiments with explicit data units, selection rules, run manifests, resource limits and result provenance. Use when the user requests experiment implementation, execution, reruns or result-to-figure synchronization; do not launch training for a writing-only request. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Experiment Automation

Suite version: `4.1.0`

<!-- invariant: execution-authorization -->
<!-- invariant: no-fabrication -->
<!-- invariant: selection-boundary -->
<!-- invariant: result-dependent-artifacts -->
<!-- invariant: resource-stop -->

This skill controls execution and provenance, not model invention. Use [evidence design](../engineering-experiment-evidence-design/SKILL.md) for what to test, then [the execution guide](../../references/experiment-execution.md) for how to run it. No training backend, GPU service or experiment runner is bundled. Use the repository's existing runner when available.

## Before Launch

Confirm the requested execution scope, data access, hardware and resource/credit limits. Writing permission is not training, cloud spending, dataset upload or publication permission. Do not launch a sweep because a paper would benefit from one.

Record the sample unit, temporal axis, train/test isolation unit, label availability, preprocessing fit population, code revision, configuration and model-selection rule. If there is no validation set, describe the actual training/selection procedure; do not invent one or repeatedly choose settings using the test set. Unknown input semantics block interpretation of the corresponding scientific claim, not unrelated writing work.

Check one representative batch, dimensions and objective before a smoke run. A smoke run verifies execution only. Define acceptance criteria and the run matrix before the full experiments; preserve negative results and failed runs.

## Run And Resume

Assign immutable run IDs with configuration, data/split fingerprint, seed, software environment, resource boundary and output directory. Keep raw predictions or sufficient statistics when permitted. Save selection history and distinguish last checkpoint, selected checkpoint and reported checkpoint.

Use bounded retries for transient failures. A changed algorithm, selection rule, data split or preprocessing step creates a new experimental version; it is not an invisible retry. Resume from an owned checkpoint after verifying compatibility. Never kill unrelated jobs or delete unique results to make room.

At the user's resource limit or quota stop condition, checkpoint and stop owned compute, save what completed, and report what remains. Do not buy credits or switch to paid fallback without explicit permission.

## Derive And Audit Results

Derive tables, uncertainty summaries and figures from the same identified runs. Record metric definition, support, run aggregation, standard-deviation convention and omitted/failed runs. Compute each run's F1 first; do not reconstruct mean F1 from mean precision and mean recall. A single-run confusion matrix cannot be asserted to reproduce a five-run mean table.

Update result-dependent prose and captions only within the user's editing authorization. Separate confirmed transcription errors from disagreements requiring raw predictions or code. Pair error bars with the actual repeated-unit definition, not decorative uncertainty. Follow [the result provenance checklist](../../assets/templates/experiment-run-manifest.md).

## Deliver

Return completed/planned/failed runs, reproducible configuration, verified numerical checks, remaining evidence questions and exact output locations. Separate scientific validation from successful execution, compilation and visual inspection. Report acceptance readiness as a bounded assessment, never as journal acceptance or a predicted probability.

Audit task-owned temporary storage at handoff. Preserve source, data, selected/final results, unique checkpoints and recovery materials. Delete only confirmed regenerable, unused intermediates within authorized scope; request approval before affecting history or another project.
