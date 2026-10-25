# Candidate-Search Independent Review

One fresh context read the frozen v4.2.4 tool/guidance and actual synthetic CLI logs. The baseline is deterministic CLI behavior, not another agent; this is not a controlled science/writing gain. Only wrapper/path/link/line metadata and whitespace are normalized; exact raw/dispatch remain private. Runtime orientation is not evidence.

Runtime orientation, not evidence: Codex desktop, read-only review using the Chinese entrypoint and references. I did not rerun the CLI/tests, execute recorded commands, edit files, install packages, browse, or launch agents.

**A. CLI Verification**
The baseline is the recorded deterministic CLI behavior, not a baseline agent.

The old records (private local reference) confirm **returncodes `0/0`**: missing `pypdf` produced two failures yet wrote a report; the other run parsed a blank PDF, encountered a broken PDF, and still reported success. Parsing that blank PDF did not establish searchability.

The new records (private local reference) show:

| Case | Exit | Coverage | Report Outcome |
|---|---:|---|---|
| Missing `pypdf` | 2 | No new report | Dependency diagnostic; no report written |
| Mixed text/textless/broken | 1 | `partial` | 2 parsed, 1 searchable, 1 textless, 1 read failure; useful candidate retained |
| Text-bearing only | 0 | `complete` | 1 searchable file; candidate retained |
| Textless only | 1 | `failed` | 1 parsed but unsearchable file; no candidates |
| Unreadable only | 1 | `failed` | 0 parsed; 1 read failure recorded |
| Empty folder | 0 | `empty` | Explicit empty report, not a negative terminology finding |
| Missing dependency, existing report | 2 | No replacement | Record reports `preserved: true` and an existing-report SHA-256 |

**Current code boundaries:**
- Missing `pypdf` is specifically caught at [line 126](../../tools/extract_terminology_evidence.py) and returns `2` before the report-writing operations at line 180. That branch cannot overwrite an existing report. The preservation smoke record (private local reference) agrees.
- Other caught read/extraction errors accumulate in `failures`; parsed PDFs without nonblank extracted text enter `no_text_files`. Reports retain available candidates, then return `1` with an incomplete-coverage warning.
- Normal report-writing paths **can replace the specified report**. Dependency protection is not a general preservation or atomic-write guarantee. The import is lazy: an empty folder does not test whether `pypdf` is installed. Other missing-module names do not receive the special `pypdf` handling.

The [coverage calculation](../../tools/extract_terminology_evidence.py) means:
- `complete`: at least one parsed unique file, some extracted text in every such file, and no recorded failures/textless files.
- `partial`: some searchable files, plus failures or textless files.
- `failed`: no searchable files, with failures or textless files. Parsing may nevertheless have succeeded.
- `empty`: no parsed files and no recorded failures/textless files.

These are **file-processing/text-presence states**, not text-accuracy, all-pages-searchable, close-reading, scholarly-identity, definition, or translation certificates. Every written report remains `candidate_search_only`. Even a successful text-bearing parse is insufficient for terminology evidence: matching is lexical, reference-region detection is heuristic, and `unverified_body` is not semantic approval.

The JSON records document actual synthetic subprocess smoke runs, not mocked extraction tests. Separately, the [unit tests](../../tests/test_corpus_candidates.py) patch `pdf_pages` for dependency/failure scenarios. I inspected both kinds of evidence without rerunning them; fixture provenance and preservation were not freshly reproduced.

**Finding:** the old false-success behavior is demonstrated. I found no additional current defect in the requested paths; the implemented handling matches the supplied outcomes.

**B. Module-Q**
Under the existing [Chinese admission rules](../../references/engineering-application-terminology-bank_CN.md):

1. **Keep the attributed name.** The defined component is useful evidence for that paper’s own Module-Q. Preserve its name and source attribution; do not replace the method.
2. **Do not admit a generic mechanism yet.** The bibliography-only occurrence contributes no substantive definition. Two byte-distinct PDFs are not necessarily two scholarly works; bibliographic review must resolve versions. Generic admission requires at least two distinct relevant published works with matching objects and operations, with three to five preferred for ambiguous terms. Even that does not establish field-wide frequency.
3. **Keep Chinese verification separate.** Machine translation is not terminology evidence. Retain Module-Q in English and, where useful, clearly label a Chinese description as explanatory. An established Chinese name requires an appropriate original bilingual/terminology source; none was checked here.
4. **Do not count unavailable material as negative use.** Unsearched files are unchecked; failed/textless files are unsearchable or failed, not verified non-use. Even a searchable no-hit file establishes only no detected lexical match under that search.

Complete processing coverage removes **none** of those requirements. The existing [corpus-profile guidance](../../references/corpus-calibration-workflow.md) already separates inventory, searches, candidates, verified uses, scholarly identity, and Chinese verification.

Module-Q is a useful candidate with an explicit component definition in one source. Retain its attributed name and operational meaning. Next, resolve whether the PDFs represent distinct works, check substantive matching definitions in another relevant published work, and verify the Chinese wording independently.

**No additional Skill rules are warranted by this scoped check beyond the current fix.** Existing rules cover the fictional misuse. This supports a bounded CLI reliability conclusion, not general scientific or writing gains.
