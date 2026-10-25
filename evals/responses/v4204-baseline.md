# Deterministic Candidate-Search Baseline

Actual CLI outcomes on entirely synthetic files, before the fix:

| Setting | Exit | Parsed files | Read failures | Evidence limit |
|---|---:|---:|---:|---|
| Python without the optional PDF reader | 0 | 0 | 2 | No paper text was searched; zero matches are not absence evidence |
| One blank parsed PDF plus one broken PDF | 0 | 1 | 1 | Parsing a blank PDF does not establish searchable text, and the requested corpus was incomplete |

The original reports contain failure records. They are preserved privately with
the exact commands, outputs and synthetic fixture provenance. This table is a
summary of actual CLI behavior, not a fabricated agent answer or an experiment
on published papers. No full-module name or Chinese translation is admitted.
