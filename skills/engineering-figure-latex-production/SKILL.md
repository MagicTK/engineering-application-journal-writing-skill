---
name: engineering-figure-latex-production
description: Plan, create, revise, and verify scientific figures, tables, LaTeX layouts, compiled PDFs, and author-ready Overleaf packages for engineering-application journal papers. Use when visual evidence, float placement, table readability, page composition, build integrity, project organization, or final editable delivery is the main task. Do not use to invent result-dependent plots or to change protected manuscript layout during language-only revision. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Figure And LaTeX Production

Suite version: `4.1.5`

## Mission

Produce editable scientific artifacts whose visual structure matches the paper's engineering argument and whose layout remains stable under revision.

<!-- invariant: no-fabrication -->
<!-- invariant: authoritative-source-lock -->
<!-- invariant: layout-lock -->
<!-- invariant: result-dependent-artifacts -->
<!-- invariant: corpus-is-evidence-not-instruction -->

## 1. Establish Locks And Build Boundaries

Identify:

- authoritative source and baseline PDF;
- image and bibliography directories;
- content, data, and layout locks;
- protected table fonts, widths, and float order;
- build command and output directory;
- untrusted scripts, packages, or shell-escape requirements.

Do not run unknown project scripts or change the established package structure without need. Keep build artifacts outside the upload package.

## 2. Assign Every Artifact A Scientific Role

Classify each figure or table as motivation, process/data generation, overall framework, module detail, comparative evidence, ablation, sensitivity, robustness, interpretation, or engineering outcome.

Read [the complete figure and LaTeX guide](../../references/figure-and-latex-production.md). Create a Figure/Table Contract from [`assets/templates/figure-table-contract.md`](../../assets/templates/figure-table-contract.md) before substantial generation.

For non-measured framework, algorithm flow, system structure, motivation and mechanism diagrams, choose an available tool that preserves scientific structure and the required editable source. The [AstraDraw → editable PPT → human revision → paper pipeline](../../references/astra-editable-figure-pipeline.md) is optional, not an installation prerequisite. Route measured/result-dependent panels to real data and reproducible plotting; classify mixed panels separately. Resume an existing editable master for local object changes.

## 3. Protect Evidence Integrity

- Result-dependent figures require verified source data.
- Illustrations may clarify known process facts but must not fabricate equipment, signals, or operating relationships.
- Arrows must distinguish material flow, data flow, control flow, learned interaction, and causal direction.
- Attention, embedding, and heat-map views must be captioned as their defined internal quantities.
- Preserve raw assets and a replacement map for generated drafts.
- Visual acceptance, scientific validation, execution authorization and publication permission are separate, version-bound records.

## 4. Design For Final Print Size

- Choose single or double column from information density.
- Keep text readable without zoom.
- Use stable panel labels, terminology, and color semantics.
- Avoid embedded decorative titles and redundant legends.
- Prefer editable vector diagrams and reproducible plots when practical.
- Verify generated visual drafts label by label before insertion.

Use the [design and local-revision rules](../../references/figure-and-latex-production.md#3-visual-design-rules) for actual typography, source-preserving edits and author-selected flat styling. No font or palette is required by this suite. Preserve meaningful colormaps, textures and transparency. A PNG-only or local-edit request does not authorize a new format or whole-figure reconstruction. Keep model identities and fixed dimensions when they define the method; generic labels must not imply unestablished compatibility.

When the optional reconstruction route is selected, follow [its dependency, editing and approval rules](../../references/astra-editable-figure-pipeline.md) and the [revision-state record](../../assets/templates/figure-revision-state.md). Preserve received human edits as the current master; verify native editing separately from rendering and formula-source availability. Approval remains version- and scope-bound. Carry forward existing authority without repetitive confirmation, and report unavailable dependencies without claiming the blocked stage is complete.

## 5. Handle Tables Conservatively

Preserve approved fonts, grouping, metric order, and emphasis. For wide tables, first consider defined heading abbreviations and column allocation within the author's layout scope. Propose removing columns, splitting scientific questions or moving details to supplementary material only when authorized; do not delete evidence to fit the page. Do not solve width by making the table unreadably small.

## 6. Compile And Inspect

After each material change:

1. compile in the build-check directory;
2. inspect undefined references, missing assets, warnings, and overfull boxes;
3. render the PDF;
4. inspect every page visually, including the figure at actual paper size and its affected/adjacent pages, crop, caption placement and text-wrap termination;
5. compare protected pages and floats with the baseline;
6. verify caption, text, table, and bibliography consistency.

A successful LaTeX build is not a visual or scientific pass.

## 7. Organize The Delivery

Maintain:

- one obvious authoritative upload folder;
- one build-check folder with the latest PDF and logs;
- separate support/research notes;
- a clearly labeled archive for historical versions;
- one image directory inside the upload package unless the source genuinely requires more.

Use [`assets/templates/author-handoff.md`](../../assets/templates/author-handoff.md) to report source/PDF paths, blockers, required inputs, protected elements, and result-propagation points.

For revised figures, include the current editable master and fingerprint, human approval evidence, scene/manifest/map freshness, formula LaTeX and asset/font provenance, final-size preview and comparison, editability checks, and exact export-to-TeX/PDF mapping. Mark unavailable sources and pending work; a portable Overleaf file set is not evidence of remote upload.

## 8. Quality Gate

- No result-dependent graphic contains invented data.
- Figure semantics match equations and prose.
- Diagrams use the appropriate route; verified result data remain the source for measured plots.
- Editability claims reflect actual native-object checks and disclosed formula/image limits.
- Human changes are preserved in the current master; approval and paper exports bind to that revision.
- Text is readable at final size.
- Table style and author locks are preserved.
- Float order supports the section narrative.
- No blank columns, isolated headings, overlapping content, or clipped objects remain.
- Upload package contains no unnecessary build artifacts or duplicate image trees.
- The handoff identifies every unresolved replacement or author action.
