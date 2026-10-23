---
name: engineering-figure-latex-production
description: Plan, create, revise, and verify scientific figures, tables, LaTeX layouts, compiled PDFs, and author-ready Overleaf packages for engineering-application journal papers. Use when visual evidence, float placement, table readability, page composition, build integrity, project organization, or final editable delivery is the main task. Do not use to invent result-dependent plots or to change protected manuscript layout during language-only revision. Use this canonical version for English-language requests; use the -zh mirror for Chinese-language requests.
---

# Engineering Figure And LaTeX Production

Suite version: `4.1.2`

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

### Optional flat diagram finish and font provenance

The following finish rules apply when the author selects a flat geometric diagram style. They are not journal-wide rules or grounds to replace approved artwork. Follow the venue and author for font, palette and format; no named font is required by this suite. Quantitative colormaps, observed textures and scientifically meaningful transparency require their own appropriate treatment.

- Use flat white or a single fixed-color fill per diagram canvas/card/cell and a single fixed ink per text run. Do not add watercolor, powdery texture, ink wash, gradients, shadows, glows, or white halos behind letters. Ordinary edge antialiasing is allowed; changing opacity across one object is not. If author-approved transparency is used, keep its opacity constant.
- Match labels, small annotations, borders, and local arrows to the relevant module's deep color family (or black); preserve explicitly defined data-identity colors. Avoid vivid/electric blue when the author specifies the mature deep-blue palette. Different heatmap values may have different colors, but each cell interior stays uniform.
- For newly typeset or author-requested replacement text, load the author's actual specified font files. A generated raster's look-alike letters are not verified typography. When the contract specifies Comic Sans MS regular and Cambria Math, check the actual font face, size, glyph coverage, and mathematical indices; do not substitute simulated handwriting or heavy bold headings.
- Keep the scientific information and established topology while correcting visual finish. Maintain one simple fill for each editable object in a later PPT reconstruction instead of stacking decorative layers to imitate raster shading.
- Carry all accepted visual constraints forward in the revision record. Inspect blank card interiors, cell interiors, letter interiors/edges, headings, formulas, and legends at native and intended reading size before passing the figure. A correct prompt alone is not evidence of compliance.

### Source-preserving local revision

When the author approves an existing diagram's structure and asks for color or typography repair, protect its coordinate system, aspect ratio, compact spacing, connector endpoints and routing, arrowhead proportions, annotations, operator symbols, and internal schematic geometry. Do not globally reconstruct the figure merely to standardize colors or increase editability. Cluster point clouds, sampling markers and guides, mini-plots, and frozen/trainable icons carry information; preserve their arrangement. With author authorization for raster editing, reuse source crops and apply local masks or recoloring when object reconstruction would degrade them. Raster reuse must be disclosed, not labeled native editability.

Use the accepted palette as color authority and the accepted source as geometry authority, while the current manuscript remains scientific authority. An older visual source may contain corrected scientific errors: migrate current formulas, masks, access rules and arrows locally instead of restoring those errors. A request to make arrows less heavy is not a request to make them barely visible; inspect shaft/head proportions in the supplied reference and at the intended reading size.

A font name alone does not determine mathematical appearance. Check regular versus bold and italic variable glyphs, upright operators, script sizes, summation scale, baseline, spacing and centering. Source files can establish actual typography; raster appearance alone cannot. When the author accepts original raster lettering, preserve it unless a local defect requires replacement, recording its font as unverified rather than mandating whole-figure retypesetting. Use the author's latest typography decision instead of an obsolete project default.

Revise the authoritative manuscript and assign motivation, overview and module-detail roles before redrawing during a coordinated paper/figure revision. Inspect localized before/after crops and the full composition, including pixel-level protected regions where practical. Keep real result plots pending until their data exist. PNG-only or crop-preservation requests override the optional editable-PPT route below; do not convert, redraw or add deliverable formats solely for workflow uniformity.

- Choose single or double column from information density.
- Keep text readable without zoom.
- Use stable panel labels, terminology, and color semantics.
- Avoid embedded decorative titles and redundant legends.
- Prefer editable vector diagrams and reproducible plots when practical.
- Verify generated visual drafts label by label before insertion.

When the author selects that optional pipeline, use it and [`figure-revision-state.md`](../../assets/templates/figure-revision-state.md) for the full loop:

1. Discover and read the current installed `astra-figure-workflow` (AstraDraw); ground the design in the paper, iterate and record the actual design decision.
2. Discover and read the current installed `image-to-editable-ppt` (Image to Editable PPT); reconstruct the selected design at object level and preserve its source manifests, assets and slide mapping.
3. Verify the delivered render and actual native text, shape and connector editing on a copy. Declare image and formula exceptions: vector formulas plus LaTeX source are not Office-native editable equations. Font/glyph provenance requires source evidence, not a guess from PNG appearance.
4. Deliver editable sources for author/student review and revision. Register received human changes as the current master; reconcile stale scene/JSON/object maps before further source-driven editing. Never rebuild from old input over human corrections.
5. Bind approval to the current revision and scope, then export or capture that master, integrate the authorized local TeX/Overleaf files, compile and inspect at actual paper size and on affected/adjacent pages.

Pending human confirmation must remain pending. Do not ask again for existing explicit confirmation within its scope. A request may authorize continuous stages or delegate design selection; record that authority without claiming a human review occurred. Report a missing skill/runtime and continue independent contract work. A skill-maintenance request does not authorize installation or conversion; an actual authorized conversion follows the installed skill and current user/runtime constraints.

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


### Optional Flat-Style Refinements

Apply these refinements only to an author-selected flat geometric profile. Named fonts below are examples subject to availability, licensing and explicit author choice, not preferred fonts for every engineering paper.

A flat-color spot check is insufficient. Verify every salient object perimeter and connector as well as its interior. Cards have exact straight edges, regular square or rounded corners, one fixed border color and uniform width; dashed frames have regular dash lengths and gaps. Remove wobbly or faded source strokes rather than recoloring them. Keep the original geometry, endpoints and protected scientific mini-plots while repairing a registered border band. Reopen an intentional connector port only where the scientific path requires it. Circles, squares, triangles and axes need clean consistent outlines, with original centers, sampling distances and counts preserved.

Use one fixed fill, one fixed border ink and one fixed text ink per semantic run. Remove residual wash immediately behind letters and around frames, not just in empty card corners. No pencil, sketch, handwritten ink, watercolor, powder, chalk, shadows, glow, textured strokes, soft-focus border or variable opacity. Alpha-composite new labels/arrows from transparent layers against the exact underlying fill; never paste a white rectangular rim over a colored panel. Boundary antialiasing alone may vary coverage. Local data-flow arrows use their module's deep ink; neutral cross-module arrows may use black only when a colored semantic association would mislead.

For an author-requested formal alternative, prefer actual Gill Sans MT Regular without bold titles, subtitles or card labels when this clear-style profile is selected; use size, spacing and coordinated ink for hierarchy; Futura is an optional alternative when requested. Verify the loaded font face and keep math in a genuine mathematical face with italic variables and upright operators. Generated lettering is not evidence of the named font. Preserve the repaired current version, then make the formal white/pale alternative; do not use an obsolete Comic-style default. A plain white large panel with very pale small operation cards is a valid complete design. Reference images transfer topology or layout only within their declared role; reject inherited hand-drawn texture.

Method diagrams use the correct model category (time-series foundation model, large language model, or multimodal foundation model when actually used). Concrete pretrained model/checkpoint names and numerical instance dimensions belong to experimental settings. Define the compatible interface and symbolic dimensions in the method; changing the displayed name cannot establish arbitrary backbone compatibility or cross-model performance.

Before generation, remove positive style keywords that request sketch/comic/hand-drawn/brush/chalk/wash/gradient/shadow effects from the effective prompt or inherited template. State: formal engineering-journal diagram; exact straight or rounded geometric frames; uniform stroke width; one fixed fill/border/ink; white major panels; module-colored arrows; no decorative effects. Lock scientific mini-plot geometry and endpoints. Inspect the actual output object by object, including phase headings and arrow ports; repair a specific failure before calling a version ready. Do not regenerate the whole image repeatedly for exact labels that deterministic typography can fix.
