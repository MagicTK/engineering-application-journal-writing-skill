# Engineering Application Journal Writing Skill

[中文](README_CN.md) | [Start here](SKILL.md) | [Skills](#choose-a-skill) | [Terminology](references/terminology-decisions.md) | [Evaluation](evals/README.md)

**An evidence-led research and writing toolkit for industrial AI.** Turn an engineering problem, a model and its actual results into a coherent journal paper. Revise a single paragraph or work through research positioning, experiments, figures, manuscript review and handoff.

**Version 4.1.7: 14 English/Chinese skill pairs.** Primary focus: intelligent models for process-industry applications. Other engineering settings are supported through explicit task and evidence definitions, not a universal paper template.

This version adds scoped definition and translation evidence for selected method names. See the [evaluation record](evals/README.md) for the tested cases and remaining audit limits; the terminology bank is not a completed whitelist.

The [current evaluation record](evals/README.md#current-version-status) identifies the tested version, actual cases, repairs and limits. Independent writing responses and deterministic packaging checks are reported separately. They do not certify every manuscript or every instruction; [versioned changes](CHANGELOG.md) explain what has been updated.

## What It Does

- **Connects mechanisms to prose.** Abstracts explain how operations depend on each other; contributions identify the supported advance instead of repeating a module list.
- **Uses terminology in context.** Variables, features, samples, states and conditions retain their meanings. No blanket ban on words borrowed from another field.
- **Separates problems from methods.** Multi-rate observation is a data challenge; a transformer is a method. Graphs, fuzzy models and LLMs are not default narratives.
- **Keeps experiments traceable.** Input semantics, data isolation, model selection, repeated-run aggregation and result-to-figure provenance stay explicit.
- **Preserves the author's work.** Discussion-only requests do not edit files. Language revision does not change results, equations, table fonts or approved figures.

The suite does not guarantee acceptance, generate missing evidence or certify a study from its writing quality. It includes instructions, references, templates and local checks, not a universal training backend or a replacement for domain expertise.

## Start With Your Task

| Your task | Entry point |
|---|---|
| My abstract lists components but their connection is unclear | [Abstract and contributions](skills/engineering-abstract-contributions/SKILL.md) |
| Is this an industrial problem or only a model idea? | [Research ideation](skills/engineering-research-ideation/SKILL.md) |
| Which sections and experiments support this contribution? | [Paper architecture](skills/engineering-paper-idea-architecture/SKILL.md) |
| Is operational state, attribute or variable-wise appropriate? | [Terminology decisions](references/terminology-decisions.md) |
| Audit tables, figures and claims without changing results | [Evidence design](skills/engineering-experiment-evidence-design/SKILL.md) |
| Run approved experiments and retain reproducible results | [Experiment automation](skills/engineering-experiment-automation/SKILL.md) |
| Review a near-final paper; essential issues only | [Rigor review](skills/engineering-journal-rigor-review/SKILL.md) |

Example request:

> Use $engineering-abstract-contributions. Read my current source, PDF, method equations and framework figure. Preserve the accepted opening. Clarify the module connections without inventing capabilities. Return a proposed abstract and only necessary body-sync edits with exact locations. Do not update LaTeX or Overleaf yet.

For Chinese interaction, use the corresponding `-zh` skill or the [Chinese orchestrator](skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md). The manuscript can remain in English.

## Install

### Ask Codex To Install From The Link

Send this request in Codex. Install the **whole suite**, not a standalone Markdown file:

> Use $skill-installer to install https://github.com/MagicTK/engineering-application-journal-writing-skill from repository path `.` with the installation name `engineering-application-journal-writing-skill`. Preserve all shared directories, including `skills`, `skills-zh`, `references`, `assets` and `scripts`. Do not install an isolated companion. If an installation already exists, report its version and location without overwriting local changes. Run the suite validator and explain how to invoke the orchestrator.

No GitHub plugin, API key or manuscript upload is required. Downloading requires network access; Codex handles local permission requests normally. If your environment does not include `$skill-installer`, use the local method below.

### Download And Install Locally

Select **Code → Download ZIP** on the [repository page](https://github.com/MagicTK/engineering-application-journal-writing-skill) and extract it, or clone the complete repository:

```bash
git clone https://github.com/MagicTK/engineering-application-journal-writing-skill.git
cd engineering-application-journal-writing-skill
```

Then run from the repository root:

```bash
python3 scripts/install_suite.py --dry-run
python3 scripts/install_suite.py --copy
```

Python 3.9+ is sufficient for the bundled checks and installer; no third-party package is needed. The default destination is `$CODEX_HOME/skills/engineering-application-journal-writing-skill`, falling back to `~/.codex/skills/engineering-application-journal-writing-skill`. Use `--target FINAL_DIRECTORY` to choose another destination. Existing targets are never overwritten. Omit `--copy` to create a symlink.

Preserve the shared directory structure. Clients supporting nested skills may expose companions directly; otherwise invoke the root skill and let it read the requested companion. Client discovery varies and must be checked in that client. Other skill-capable assistants can read the Markdown without Codex UI metadata. Browser access, PDF tools, LaTeX compilers and experiment runners are optional capabilities supplied by your environment.

### Verify, Update And Remove

On your next Codex turn, ask it to read the installed root `SKILL.md`, confirm that its version matches the source you downloaded, and run `scripts/validate_suite.py`; this suite has 14 bilingual pairs. A development candidate's version can differ from the currently published GitHub version. Record the downloaded revision rather than treating that difference as an installation failure. If a companion does not appear in the selector, ask the orchestrator to read its file inside the suite. Do not install a duplicate just to expose the name. Restart the client if it has not refreshed its skill list.

Before updating, record the installed version and preserve local changes. Validate a new download before explicitly replacing the old suite. The installer stops at an existing destination; it never deletes or overwrites it. To uninstall, remove only the identified installation directory or symlink, not a manuscript project. Ask Codex to identify the path first when uncertain.

## First Use In A Research Group

Provide the immediate question, target venue if known, available materials and permitted actions. You do not need to complete every template. Missing results allow a design discussion, not plausible-looking invented findings.

| Starting point | Useful inputs | First output to expect |
|---|---|---|
| An engineering problem | Process, measurements, difficulty and existing approaches | Problem-led options and evidence to investigate |
| A method with an unclear abstract | Current text, method equations and framework figure | Accurate module linkage and minimal edits |
| Experiments to plan | Claims, sample unit, split and available resources | Executable plan and missing inputs, not fabricated results |
| Results to interpret | Tables, figures, run records and prose | Consistency findings and a verification handoff |
| A near-final paper | Current source, PDF, references and protected elements | Principle-level findings separated from optional polish |

Example requests:

> Use $engineering-terminology-polishing. Check only engineering terminology and sentence progression in the supplied paragraph. Give the original sentence, proposed sentence, rationale and whether the change is necessary. Do not change the method, results or files. For uncertain terms, provide context and published evidence instead of a universal blacklist.

> Use $engineering-experiment-evidence-design. Audit claims against the supplied method and results. Separate confirmed arithmetic errors, questions requiring original run records, and optional additional experiments. Do not replace table values or start training.

> Use $engineering-application-journal-writing-skill. Read my current draft and address only the progression from Introduction to method overview. Preserve approved passages. Give exact locations and minimal changes for supervisor approval before editing source files.

Keep proposed, approved, implemented and verified changes distinct. A polished paragraph does not certify data, implementation or acceptance. Check the hosting model service's data policy: installing a local Skill does not by itself keep manuscript content on your machine.

## Choose A Skill

| English skill | Purpose | Chinese |
|---|---|---|
| [Engineering application journal writing](SKILL.md) | Scope, routing, preservation and handoff | [中文](skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md) |
| [Industrial AI paper router](skills/industrial-ai-paper-router/SKILL.md) | Challenge, method, task, scale and evidence | [中文](skills-zh/industrial-ai-paper-router-zh/SKILL.md) |
| [Research ideation](skills/engineering-research-ideation/SKILL.md) | Candidate problems and contribution calibration | [中文](skills-zh/engineering-research-ideation-zh/SKILL.md) |
| [Literature positioning](skills/engineering-literature-positioning/SKILL.md) | Published evidence, gaps and citation roles | [中文](skills-zh/engineering-literature-positioning-zh/SKILL.md) |
| [Paper architecture](skills/engineering-paper-idea-architecture/SKILL.md) | Problem-design-evidence structure | [中文](skills-zh/engineering-paper-idea-architecture-zh/SKILL.md) |
| [Abstract and contributions](skills/engineering-abstract-contributions/SKILL.md) | Mechanism linkage and minimal body synchronization | [中文](skills-zh/engineering-abstract-contributions-zh/SKILL.md) |
| [Benchmark and real-world case](skills/general-method-benchmark-realworld/SKILL.md) | Distinct evidential roles for a general method | [中文](skills-zh/general-method-benchmark-realworld-zh/SKILL.md) |
| [Background-driven application](skills/background-driven-industrial-application/SKILL.md) | Derive requirements from the industrial setting | [中文](skills-zh/background-driven-industrial-application-zh/SKILL.md) |
| [Experiment evidence design](skills/engineering-experiment-evidence-design/SKILL.md) | Comparisons, controls, statistics and consistency | [中文](skills-zh/engineering-experiment-evidence-design-zh/SKILL.md) |
| [Experiment automation](skills/engineering-experiment-automation/SKILL.md) | Authorized runs, selection rules and provenance | [中文](skills-zh/engineering-experiment-automation-zh/SKILL.md) |
| [Figure and LaTeX production](skills/engineering-figure-latex-production/SKILL.md) | Scientific figures, editable outputs and layout | [中文](skills-zh/engineering-figure-latex-production-zh/SKILL.md) |
| [Terminology polishing](skills/engineering-terminology-polishing/SKILL.md) | Precise language and paragraph progression | [中文](skills-zh/engineering-terminology-polishing-zh/SKILL.md) |
| [Journal rigor review](skills/engineering-journal-rigor-review/SKILL.md) | Evidence-bound findings and unresolved checks | [中文](skills-zh/engineering-journal-rigor-review-zh/SKILL.md) |
| [Reviewer response](skills/engineering-review-response/SKILL.md) | Comment-to-change-to-evidence correspondence | [中文](skills-zh/engineering-review-response-zh/SKILL.md) |

## A Shared Core, Not One Paper Recipe

### Repository Map

Version 4.1.7 contains **28 Skill-entry Markdown files, 26 reference Markdown files and 13 working-template Markdown files**. The entries form 14 English/Chinese pairs, not 28 different methods. Load references by task rather than reading the whole library on every request.

| Location | Contents |
|---|---|
| `SKILL.md`, `skills/`, `skills-zh/` | Orchestrator and English/Chinese task entrypoints |
| `references/` | Section craft, terminology, taxonomy, topics, experiment evidence and figures |
| `assets/templates/` | Manuscript, claim/evidence, data-version, run, figure and handoff records |
| `scripts/`, `tests/` | Installation, structure checks, read-only terminology candidates and tests |
| `evals/` | Synthetic scenarios, actual responses, evaluation scope and versioned records |

Terminology guidance separates the object, task, context, scientific meaning and author preference. Paper-specific term decisions stay in that paper's project, not in a universal blacklist.

General mechanism names require [two distinct published-paper contexts and a separate Chinese-language check](references/engineering-application-terminology-bank.md#0-admit-names-not-search-counts). One-paper module names remain attributed; descriptive phrases do not become established categories merely by appearing here. The core evidence ledger is partial, with unresolved entries explicitly left unverified.

### Conditional Topics

The [five-axis taxonomy](references/industrial-ai-taxonomy.md) separates **engineering challenge, method family, task, object/scale and evidence profile**. Load only relevant [topic playbooks](references/topic-playbooks.md): multi-rate/irregular data, limited supervision, nonstationarity, multisource evidence, plant-wide systems, graphs/knowledge/fuzzy models, generative methods, LLMs, efficiency, localization, expert routing, compound faults, temporal representations or control/decision tasks.

A paper need not have two datasets, a fixed number of contributions, a 200-word abstract, a confusion matrix or every available ablation. Choose what establishes its actual claim. Venue rules must be checked from current official instructions; published examples establish writing options, not mandatory formatting rules.

## References And Tools

- [Abstract/contribution craft](references/abstract-and-contribution-craft.md) and [body-sync template](assets/templates/abstract-body-sync.md).
- [Section writing](references/section-writing-guide.md), [argument and prose craft](references/argument-and-prose-craft.md), [contribution narratives](references/contribution-narratives.md).
- [Terminology decisions](references/terminology-decisions.md), [terminology bank](references/engineering-application-terminology-bank.md), [40-paper evidence index](references/published-evidence.md).
- [Experiment execution](references/experiment-execution.md), [run manifest](assets/templates/experiment-run-manifest.md), [evidence design](references/experiment-evidence-design.md).
- [Figure production](references/figure-and-latex-production.md), [journal migration](references/journal-migration-and-completeness.md), [author handoff](assets/templates/author-handoff.md).

Read-only terminology candidates from a local source:

```bash
python3 scripts/audit_terminology.py manuscript.tex --min-count 3
```

The tool skips percent comments, inactive literal `iftrue`/`iffalse` branches, comment environments, common citation/reference keys, URL targets and literal `thebibliography` blocks. It preserves source line numbers and linked display prose. It does **not** expand arbitrary TeX macros, inspect included files, prove a phrase wrong or edit the manuscript. Verify active text against the compiled PDF; custom or nested syntax still needs manual review.

## Evidence, Privacy And Attribution

This repository distributes general instructions, original synthesis, bibliographic links and synthetic evaluation scenarios. It does not distribute reference PDFs, manuscript text, industrial data, private project logs or model weights. Keep manuscript-specific terminology and result records with the manuscript, outside the shared suite.

See [published sources](references/published-evidence.md), [design-source acknowledgments](references/design-sources.md), [contribution guidance](CONTRIBUTING.md) and [privacy/security guidance](SECURITY.md). Upstream popularity is not evidence of writing quality or a prediction of this project's adoption. Third-party licenses remain separate from this project's distribution terms.

## Check The Package

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

Structural checks test packaging and invariants, not scientific validity. Behavioral tests have a separate [evaluation record](evals/forward-test-report.json) with the version, scope and actual test status. Historical results do not validate this release; a self-review is not an independent test. See [evaluation procedure](evals/README.md) and [changes](CHANGELOG.md).

Maintainers can prepare a clean local candidate with `python3 scripts/export_public.py NEW_DIRECTORY --draft`. Without `--draft`, the exporter also requires a license and completed independent behavioral checks. It never uploads anything or includes the parent repository's history.

## License

[MIT](LICENSE), copyright 2026 MagicTK. Use, adapt and redistribute the original Skill content, including commercially, while retaining the copyright and license notice. Referenced publications and external projects retain their own rights and licenses; they are not relicensed or bundled here.
