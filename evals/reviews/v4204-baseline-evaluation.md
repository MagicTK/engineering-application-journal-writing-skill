# Candidate-Search Failure Baseline

This baseline is a deterministic CLI reproduction on synthetic PDF fixtures,
not an independent language-model response or a scientific experiment. Exact
commands/logs remain private. No original paper, manuscript or industrial data
was involved.

On v4.2.3 behavior, isolating Python from optional site packages leaves pypdf
unavailable. Both PDF reads fail, yet the helper writes a zero-candidate report
and exits0. With a parsed blank PDF and a broken PDF, it again exits0 despite
one failed read. The report does record failures; the defect is the success
signal and missing explicit text/processing coverage, not fabricated matches.
The old parsed-file count does not establish that the blank PDF contains
searchable text.

Five regression checks expose four wrong success statuses and one absent
coverage object. The revision preserves usable candidates, distinguishes a
missing optional dependency, failed reads, textless inputs and empty corpora,
and does not upgrade candidate matches into admitted terminology. A zero-hit
search with failed or empty input coverage cannot establish corpus absence.
Existing naming and Chinese-verification rules remain in force. This is a tool
and coverage clarification, not a model-science baseline failure or general
writing improvement claim.
