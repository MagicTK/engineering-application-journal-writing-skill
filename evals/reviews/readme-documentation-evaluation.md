# README Documentation And Figure Check

This is a documentation-only addition to 4.2.36, not a new Skill behavior
release. The previous 106 instruction/dependency files retain their evaluated
hashes. Two original synthetic SVG illustrations are added; the following
checks cover their meaning and readability, not new scientific performance.
The [sampling report](../history/v4.2.36-before-readme-assets/forward-test-report.json)
retains the earlier behavioral scope. The current report explicitly carries
that scope forward without claiming those cases were rerun on new illustrations.

Two newly spawned responding contexts used inherited model/effort settings.
The first read only the bilingual READMEs and checked interpretation, scope and
installation navigation. It found an ambiguous Chinese antecedent, corrected
before a same-context local recheck. The second read those READMEs, both SVG
assets and synthetic mobile previews; it found a line crossing an edge label.
Native SVG text and opaque label backgrounds were then checked in that same
context. These are two different documentation checks, not repeated independent
measurements of quality gain or whole-suite validation. Preloaded workspace
instructions and historical memory summaries prevent a context-blind claim.

The maintainer separately rendered desktop/mobile examples. Actual GitHub
mobile inspection exposed viewer controls obscuring a node in the first
interactive rendering, despite bounding-box checks passing. Static illustrations
replace that embed; editable Mermaid definitions remain collapsed as text.
The SVGs contain native text, no scripts, external assets or embedded HTML.
Renderer compatibility and actual hosted display remain distinct checks.

The complete responses below retain scientific wording. Local file links are
made repository-relative without source-line suffixes; application writing-block
wrappers are removed. Original responses remain in private maintenance records.


## README interpretation: first response

**1. Meaning Of The Example**
As a new group reader, I infer:

- **Labeled samples:** quality labels supervise the quality predictor and help train the shared encoder.
- **Unlabeled samples:** their measurements provide reconstruction targets, allowing the decoder and shared encoder to learn without quality labels.
- **Encoder:** produces the representation used by both training branches.
- **Decoder:** reconstructs measurements during training; it is not an input stage for the quality predictor.
- **Prediction:** measurements → encoder → quality predictor → quality estimate. The decoder is absent.

The decisive wording is: “Prediction on labeled samples and reconstruction of unlabeled measurements train a shared encoder” and “the reconstruction decoder is used only during training.” [English example](../../README.md)

**The diagram implies no different connection.** It shows `E --> P` and `E -. "Training only" .-> D`, with no decoder-to-predictor edge. Its caption explicitly says: “The diagram shows forward data paths, not optimization updates.” [Diagram and caption](../../README.md)

I cannot infer the loss formulas, weighting, training schedule, or whether labeled measurements also participate in reconstruction. The diagram alone does not distinguish labeled from unlabeled inputs; the prose supplies that information.

**2. Request And Installation**
For a near-final abstract, the task table’s “Review a near-final paper; essential issues only” points to **Rigor review**. Restricting that route to the abstract is straightforward. [Task navigation](../../README.md)

Use $engineering-journal-rigor-review. Review only the near-final abstract I provide, using only the supplied material. Report essential problems in meaning, internal consistency, method connections, or claim scope. For each finding, quote the exact text, explain the issue, and give a minimal proposed replacement only where justified. Preserve supported results and accepted wording; do not rewrite the whole abstract. Separate optional polish from necessary corrections. Mark anything requiring methods or results as unresolved, not verified. Do not edit files, inspect other manuscript sections, browse, or run experiments.

**Student installation route:** obtain the complete repository, then use **Download And Install Locally / 方式二：下载后安装**. From its root, the documented commands are:

```bash
python3 scripts/install_suite.py --dry-run
python3 scripts/install_suite.py --copy
```

The README specifies Python 3.9+, installation under `$CODEX_HOME/skills/engineering-application-journal-writing-skill` with a `~/.codex/skills/engineering-application-journal-writing-skill` fallback, and no overwriting of existing targets. Keep the whole suite, including shared directories. The alternative is the supplied `$skill-installer` request using repository path `.`. [Installation instructions](../../README.md)

If companions are not discovered, invoke the root orchestrator and ask it to read the relevant companion inside the suite; do not install isolated duplicates. These are documented routes, not installation behavior I tested.

**3. Concrete Friction**
- **Minor Chinese antecedent ambiguity:** “无标签测量数据的重构也参与训练二者共用的编码器” introduces “二者” without clearly naming a pair of branches or modules. The subsequent English passage and diagram resolve the meaning, so this is local wording ambiguity, not a method contradiction. “预测与重构共用的编码器” would identify the relationship directly. [Chinese example](../../README_CN.md)
- **Copyable-prompt scope caveat:** the existing abstract request says “Return a proposed abstract and only necessary body-sync edits with exact locations”; Chinese similarly requests “给出摘要建议，以及确实需要同步的正文原句、位置、改句和理由。” Both request revision proposals extending beyond an abstract-only check. They prohibit file updates, but are not ready-made *review-only, abstract-only* requests without narrowing. This is not an English/Chinese mismatch. [English request](../../README.md), [Chinese request](../../README_CN.md)

I found no substantive bilingual mismatch in the example’s architecture or installation route. Nor does the example present training-only reconstruction as a universal rule: it explicitly says “Hypothetical method, not a real manuscript” and “This is a short method passage, not an abstract template.”

**Read And Context**
I read only [README.md](../../README.md) and [README_CN.md](../../README_CN.md), with a focused line-numbered reread of task navigation, example, and installation sections. No linked files, maintainer records, manuscripts, or memory files were opened; no edits, experiments, installation tests, or web browsing occurred. A read-only quota check was performed as instructed.

Preloaded context included your request, workspace/AGENTS instructions, general assistant instructions, a skill catalog, and an automatically supplied prior-project memory summary. That summary was not used as evidence; this was not a context-blind reading. Conclusions concern README interpretation only, not full-Skill behavior or scientific validity.


## Chinese antecedent: same-context recheck

Confirmed: “预测与重构共用的编码器” now clearly identifies **prediction and reconstruction** as sharing the encoder. Its meaning remains consistent with the English example previously read: both learning objectives train the shared encoder; prediction retains only the encoder and quality predictor, without a decoder-to-predictor connection.

I reread only the [short Chinese example](../../README_CN.md). This is **same-context feedback on the local correction**, not a new independent review. The earlier prompt-scope caveat remains a usage distinction, not a bilingual error.


## Static diagrams: first response

**Findings**
Read both READMEs, both referenced SVGs, and both supplied mobile previews. No substantive training/prediction contradiction found.

- **Minor visual overlap:** in both [English SVG](../../assets/readme-training-prediction-en.svg) and [Chinese SVG](../../assets/readme-training-prediction-zh-CN.svg), the dotted decoder branch remains visible through “Training only” / “仅训练时使用”. Both labels remain readable. No clipped text, missing nodes, or unreadable passages are evident in the supplied 390-pixel previews.
- **Dependencies agree:** the premises, revised prose, diagram source, and SVGs consistently describe measurements → shared encoder → quality predictor → quality estimate, with a separate training-only encoder → decoder branch. Neither diagram introduces decoder → predictor.
- **The revision depends on the supplied premise:** the three-sentence “before” passage alone does **not** establish shared training or decoder removal. Those details are grounded in the preceding hypothetical facts, not inferred merely from module order. See [English example](../../README.md) and [Chinese example](../../README_CN.md).
- **Language scope:** the Chinese README retains the identical English before/after quotations; its Chinese framing and diagram labels agree with them. This is an English-writing example explained in Chinese, not two independently translated prose examples.
- **Unverified within scope:** “different verified designs” / “其他已核实的结构” at line 71 refers elsewhere. These four files do not establish that verification; the linked references were not inspected.

**What Follows**
Supervised prediction and unlabeled reconstruction both train the shared encoder; reconstruction can therefore influence the representation used for prediction. Prediction retains the encoder and predictor, without the decoder.

**What Does Not Follow**
This does not establish direct reconstruction-loss updates to the predictor head, a particular training schedule or loss weighting, improved accuracy, novelty, or scientific validity. The diagrams explicitly show forward paths, not optimization updates; omitted losses and training-data distinctions are therefore limitations of the schematic, not contradictions.

Nothing was edited. This is only the requested documentation-consistency check.


## Diagram readability: same-context recheck

Inspected both updated SVG assets and both supplied final mobile images.

- **Previous readability issue resolved:** the dotted branch no longer crosses “Training only” or “仅训练时使用”. Both backgrounds explicitly use opaque white. No unreadable labels, clipping, or unintended overlaps are visible in these previews.
- **Native SVG text confirmed:** labels use `<text>`/`<tspan>`, with no embedded HTML or `<foreignObject>`.
- **Meaning unchanged in both languages:** measurements → shared encoder → quality predictor → quality estimate; a separate encoder → reconstruction decoder branch remains training-only. No decoder → predictor dependency or optimization-update arrows have been introduced.

The earlier overlap finding remains applicable to the old previews but is closed for these updated assets. This targeted recheck does not establish universal renderer compatibility or add any scientific validation.
