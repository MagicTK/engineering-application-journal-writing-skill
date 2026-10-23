# AstraDraw → Editable PPT → Author Revision → Paper

## Scope and entry route

This is an optional tool-specific figure production route, not a requirement to install either tool. Existing PowerPoint, vector, TikZ or other suitable editable sources can follow the same scientific checks without raster generation or reconstruction. Use this route only when selected for the task, with the
[Figure/Table Contract](../assets/templates/figure-table-contract.md) and the
[Figure Revision State](../assets/templates/figure-revision-state.md). It records
the scientific source, current master, review evidence, and paper integration for
each figure; it does not replace an external skill's runtime state.

| Artifact | Route | Required evidence |
|---|---|---|
| Non-measured framework, algorithm flow, system structure, motivation or mechanism diagram, when this route is selected | AstraDraw design and iteration → design review → Image to Editable PPT object reconstruction → author/student review and revision → approval of the current revision → export/capture → local TeX or Overleaf file integration → compiled-paper inspection | Paper-grounded topology, verified labels, versioned editable source, review evidence, final-size checks |
| Measured comparison, ablation, sensitivity, robustness, signal, distribution, attention or other result-dependent view | Verified result data → reproducible plotting source → author review → export → paper integration and inspection | Real data, run/split/metric identifiers, transformation and plotting code; defined meaning of internal quantities |
| Mixed figure | Separate the schematic panels from data-dependent panels; use the appropriate route for each and record the assembly mapping | Both source chains; no generated panel presented as measured evidence |
| Existing editable diagram with a selected-object change | Resume the current master and edit the grounded objects; return to reconstruction only when the requested change requires it | Current file fingerprint, selected object identities, protected regions and attached connectors |

Image generation may explore a diagram's composition. It must not manufacture
measured curves, observations, error bars, confusion matrices, realistic signals,
or numerical evidence. A schematic quantity must be identified as schematic and
must not support a result claim. An image of a plot is not its underlying data;
converting it to paths does not make it a reproducible or data-linked plot.

## Discover dependencies at the point of use

Before invoking either external skill, discover its current installed location
through the current skill catalog or documented local discovery mechanism and read
that installed `SKILL.md`. Record the resolved skill name, available version or
file fingerprint, and consulted references in the project revision record. Do not
assume a version, a private home directory, model name, runtime path or command API.

- `astra-figure-workflow` is titled **AstraDraw**. Read its current session and
  local-editing guidance for ongoing/revised figures, and its design/reference
  guidance when planning a new design. Use its supported session mechanisms to
  preserve versions and scoped checks when available.
- `image-to-editable-ppt` is titled **Image to Editable PPT**. Read its current
  object-decision, manifest, QA and runtime guidance before conversion. Its current
  supported orchestration controls its own run/page state; do not forge or manually
  patch those states to satisfy this suite's checklist.

If a skill or required runtime is absent, name the missing dependency and the
stage it blocks. A request to update this suite is not permission to install
dependencies or execute drawing/conversion: do not auto-install or run those
stages during skill maintenance. Continue the independent scientific contract,
source inventory, label checks, data plotting plan and integration mapping that
remain possible. For a later user-authorized drawing/conversion task, follow the
installed skill's current runtime guidance and the user's current constraints;
carry forward existing authorization for necessary prerequisites. Ask only when
a missing user decision or actual environment permission boundary requires it,
not merely because a fixed workflow has another stage. Do not embed the external
skills, their private libraries, reference images or third-party material inside
this suite.

## 1. Lock the scientific specification

Identify the authoritative paper version, equations and method sections, input and
output, shared and separate modules, training/inference distinction, arrow meanings,
panel purpose, allowed labels and claims, and prohibited inferences. Record actual
paper width/height constraints from the journal class, source and author locks.
Do not inherit a case study's fonts, palette, width or page budget as defaults.

References can guide style or a scientifically compatible mechanism. Record which
role each reference has, its origin and permission status. They cannot silently add
architecture, results, causal claims or publication rights. Keep unknown-license
material private and reference-only. Aesthetic acceptance, scientific validation,
execution authorization, and permission to publish are separate records.

## 2. Iterate the AstraDraw design

Inspect the existing design and relevant references. Make meaningful composition
choices around the scientific argument, then refine labels, hierarchy and local
details. Preserve protected regions and accepted decisions within their recorded
scope. Save the actual candidate, prompt/reference provenance and source binding;
a prompt that mentions a filename is not evidence that the image was supplied.

For local feedback, ground the current slide and real object names/IDs, or inspect
the screenshot region before resolving objects. App annotation IDs, scene IDs,
PowerPoint shape IDs and screenshot coordinates are different identifiers. Change
only selected objects and necessary attached connector endpoints; account for any
change to a color that encodes scientific meaning.

Bind design review to an exact candidate/version. If human confirmation is pending,
say so; never mark it accepted to advance a workflow. Existing explicit acceptance
within the same scope remains valid and must not be requested again. If the user
explicitly delegates design choice and authorizes continued reconstruction in the
same request, proceed within that scope and record the delegated choice honestly,
without calling it human-confirmed. A source/mechanism change invalidates affected
scientific checks and any acceptance whose scope it changes.

## 3. Reconstruct objects with Image to Editable PPT

Use the selected design raster as a visual reconstruction reference and the paper
specification as scientific authority. Preserve the selected layout while rebuilding
readable diagram labels, structural boxes, arrows, lines and panels as appropriate
native objects. Follow the installed skill's object-source rules for imagery,
foreground assets, formulas and background handling.

A slide-sized image placed in PPT, even with native text overlaid, is not an
object-level editable diagram. Nor does a high shape count prove useful editing:
a continuous line split into hundreds of fragments is not an independently
manageable connector. Keep useful object names, grouping and connector granularity.

Declare editability by object class, based on the delivered file:

| Object class | Declare and check |
|---|---|
| Labels and ordinary text | Native editable text; exact content, fonts, glyph coverage, wrapping and position |
| Structure, arrows and lines | Native shape/line/path editability and useful selection granularity; connection semantics |
| Plotted quantities | Original data and plotting source; native paths alone do not provide data-linked editing |
| Formulas | Actual representation: Office-native equation, vector asset/path, raster asset, or other; attach LaTeX source and re-render route where applicable |
| Photos, textures, devices and other imagery | Separate assets with origin and permitted use; moving/resizing an image is not editing its internal objects |

Do not label a vector formula with LaTeX source as an Office-native editable
equation. Formula appearance, editable source and PowerPoint equation editability
are different properties. Do not infer the original font family or exact glyph
source from PNG appearance. Use the original editable file, explicit author choice,
document metadata or rendering configuration as evidence. If unavailable, label the
font choice as a reconstruction/substitution and check the actual rendering.

Preserve the run manifests, source image, actual editable deck, per-figure slide
mapping, formula source, external assets, previews and provenance needed to resume.
Deliver individual-figure decks and an aggregate deck when requested, with a stable
figure-to-slide map. An aggregate deck does not by itself identify the paper master.

## 4. Verify and hand over for human revision

Use the installed conversion skill's page-owner QA and final structural validation.
Reuse recorded successful checks; do not repeat unchanged page-level visual QA.
Add missing scientific and editing evidence needed by the paper contract:

- Open the actual delivered PPTX and compare its render with the selected design.
  Verify labels and formulas against the authoritative paper, then inspect at the
  intended printed size for missing glyphs, clipping, overlap and line readability.
- On a copy, actually edit a representative native label, structural object and
  connector present in the figure; render the trial, verify the intended change
  and protected surroundings, and record file, slide, object and result. Record
  absent classes as not applicable. Package inspection/counts support this test
  but do not substitute for it. If only structural inspection is available, state
  that editing is untested; do not claim it was verified.
- Record per-object exceptions and failed checks. A conversion runtime may accept
  a warning, such as a blocked formula render, while the paper figure remains
  incomplete. A structural pass cannot approve missing scientific content or
  grant scientific/visual acceptance.

Hand the author/student the editable source, readable preview, object/formula
limitations, protected elements and revision instructions. Record whether human
review is pending, edits were received, or review concluded with no edits. Do not
claim human revision occurred merely because an agent prepared the PPTX.

## 5. Make the human revision the current master

When a revised PPTX arrives, preserve it and the prior source as separate versions.
Register the revised file's fingerprint, author, date, slide mapping and change
scope. Compare its render and relevant objects with the prior version, then set
the revised PPTX as the current master for the affected figure(s). Mixed revisions
in one deck require a per-figure master map.

Manual PowerPoint edits do not automatically update an AstraDraw scene, JSON
manifest, generator or old object map. Mark those bindings stale. Before later
source-driven editing, reconcile/import the human changes into a new source and
verify a matching render, or continue from the revised native PPTX with a supported
editor. If reconciliation is unavailable, preserve that PPTX as master and disclose
the limitation. Never regenerate from an old image/scene/manifest and overwrite
the author's corrections. Do not run conversion finalization on stale manifests
and treat its regenerated deck as the human revision.

Bind approval to the current revision, fingerprint and scope, including any
scientific changes. Evidence must come from actual review or explicit authority
for the current selection. A prior PNG approval does not automatically approve a
reconstructed or manually changed PPTX. Approval still applicable to unchanged
scope need not be sought again. The user may explicitly authorize both stages or
the full pipeline in one request; advance the authorized work continuously and
record which decisions were delegated, which were human-confirmed, and which
remain pending. Authorization to proceed must not be reported as a review that
never occurred.

## 6. Export the approved current revision and integrate

Export from the current approved master, not an older canonical PNG. Prefer a
vector format supported by the existing TeX build and rendering stack. When a
raster export or screenshot is requested/needed, capture the approved version and
record crop, aspect ratio, resolution and intended print dimensions; inspect that
its resulting text and strokes remain readable. Keep the editable master beside
the export history. A screenshot is a paper derivative, not the editable source.

Map each export to its exact figure ID, slide/panel, target image path, TeX include,
label, caption, column width and affected sections/pages. Replace only authorized
assets in the existing local TeX/Overleaf file set, preserving class settings,
captions/labels, bibliography and protected layout unless the change requires an
authorized update. Overleaf-ready files are a deliverable; actual remote upload
or publication is a separate action governed by the user's authorization.

Compile through the project's established reviewed build route into the build-check
directory. Inspect missing assets, undefined references and overflow. Render the
PDF and inspect the figure at its actual paper size plus its affected and adjacent
pages, including caption placement, float order, crop, wrapping and where wrapped
text ends. Follow the [main guide](figure-and-latex-production.md) for full manuscript
page inspection. Log the exact export/master hashes and PDF version checked.
Recheck changed objects and affected layout after repairs; do not report that the
PPT-to-paper loop passed if only the deck or only an earlier PNG was inspected.

## Source inventory and completion

For each figure, retain or explicitly mark unavailable/not applicable:

1. scientific contract, paper/source version, raw result data and plotting code
   where data-dependent;
2. inspected reference origins and usage rights; candidate images, prompts and
   design review/selection evidence;
3. editable PPTX, current master/version/fingerprint, native object map where
   current, reconstructible scene/manifests where available, and slide mapping;
4. formula LaTeX plus actual rendered assets, font/glyph provenance and known
   substitutions, independent image assets and their licenses;
5. human revision files, change log, reconciliation/stale-binding state, and
   approval evidence for the current version;
6. paper export and final-size preview, reconstruction comparison, editing/QA
   evidence, TeX target mapping, compiled PDF and build/adjacent-page checks.

Use stable project-relative paths in a portable package. Keep working/build
artifacts and historical drafts outside the authoritative upload set. Report the
completed stage and exact remaining dependency, pending review or unresolved check.
Do not describe a review-ready draft as approved, a vector as fully editable, or
a file package as remotely published.

## Lessons from a reviewed diagram handoff

The reviewed workflow integrated canonical raster diagrams into a manuscript,
then separately delivered an object-level PPT reconstruction with formula sources
and rendering comparisons. An earlier image-placeholder deck did not provide
object-level editing. The reconstruction used native text and structural shapes,
vector formulas backed by LaTeX, and separate raster imagery. These observations
support per-class editability declarations and source-version tracking; shape
counts and a particular case's typography are not quality thresholds or defaults.

The later conversion did not itself revise the manuscript. Human-revised PPT →
export → TeX reintegration and paper inspection is the continuation required by
this contract, not an already verified outcome of that case. Task identity,
artifact fingerprints, measured counts and historical versus current inspection
coverage remain in the calling project's audit record.
