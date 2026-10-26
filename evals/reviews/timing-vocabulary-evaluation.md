# Sampling And Timing Vocabulary Review

## Change And Source Scope

The existing guide already distinguished reciprocal period/frequency, mean-rate
statistics, acquired measurements and model grids. This revision makes those
related concepts directly searchable in the English/Chinese decision guides,
adds adjacent-versus-pairwise endpoints, and removes an overgeneral suggestion
to begin irregular-observation prose with a sampling cycle. It introduces no
generic mechanism name, new industrial-work ID or real research result.

The maintainer reread P34 pp.4-5, P73 p.3, P24 pp.3-4 and the accepted P23
pp.1-2 for their observation definitions. P73 p.3 and P24 p.4 were also visually
inspected. These are selected passages, not complete implementation or result
audits. Separate Chinese base-word checks retain their actual indexed-title,
keyword or abstract scope in the terminology bank. No unpublished manuscript
content is used as public terminology evidence.

## Fictional Requests And First Answer

One newly spawned responding context received three requests with the frozen
Skill, not a scoring rubric or prior conclusions. It used inherited model and
effort settings. This was one context, not three independent replications.

1. Correct Methods terminology for a 0.25-s reference grid, streams scheduled
   every three/eight grid spacings, and one lost scheduled acquisition. The
   input supplied A timestamps 0/0.75/1.50/3.00 s, missing 2.25 s, and B
   timestamps 0/2/4 s. A nine-position window runs from 0 to 2 s inclusively,
   with a four-position stride and unknown prediction issuance. A separate
   0.4-Hz oscillation peak was supplied. The draft confused the multipliers
   with Hz, the grid with a shared acquisition clock, an observed gap with a
   new period, the window with nine seconds, and the peak with acquisition.
2. Correct a claim of a fixed sampling-cycle embedding and synchronization
   for observations at 0/1/5 s, whose actual timing input is
   `D_ij = abs(t_i - t_j)`. Calculate the matrix and two declared mean-rate
   statistics without inventing a new operation.
3. Correct grammar only in `The process variables was measured at varying intervals.`

The first answer was saved without feedback or retest. It reported preloaded
workspace instructions, a skill directory and a historical memory summary,
but no memory-file lookup or real-paper use. A combined read was truncated and
the relevant sections were reread. This is not a memory-blank or blind trial.
Public response formatting replaces local Skill links with repository-relative
links and removes application writing-block fences; the wording is unchanged.

## Maintainer Findings

| Request | Observed behavior | Outcome |
|---|---|---|
| Acquisition and model grid | Separates 0.75/2-s nominal periods, 4/3 and 0.5-Hz rates, the 1.50-s observed gap, held values, two-second endpoint span and one-second window stride. Keeps unknown prediction timing in an author note. | Pass |
| Pairwise timing | Gives the actual symmetric 3-by-3 differences and two adjacent gaps, preserves the measurement/timing input, and removes unsupported cycle and synchronization claims without inventing a named module. | Pass |
| Grammar only | Changes only `was` to `were` in the requested sentence. | Pass |

A separate exact-arithmetic check confirms the periods/rates, window span and
stride, `D = [[0,1,5],[1,0,4],[5,4,0]]`, adjacent gaps `[1,4]`, mean reciprocal
`5/8 Hz` and reciprocal mean `2/5 Hz`. This checks fictional arithmetic, not
measurements, source-paper algorithms or an experiment.

The Methods paragraph retains all supplied acquisition facts and could be
shortened for a manuscript that already tabulates them. That is an optional
editorial choice, not a failed technical requirement or a reason to impose a
word-count rule. No baseline comparison or independent second grader was used;
the result does not establish a measured writing-quality gain or certify the
entire terminology bank.

See the [actual first answer](../responses/timing-vocabulary-candidate.md),
[sampling-review report](../history/v4.2.36-before-readme-assets/forward-test-report.json) and
[preceding report](../history/v4.2.35/forward-test-report.json). Program tests,
bilingual structure, export fingerprints and behavior are separate checks.
