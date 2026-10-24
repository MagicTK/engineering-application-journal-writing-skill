# Mechanism-Linked Abstracts And Contributions

[中文](abstract-and-contribution-craft_CN.md)

Use this guide for revision, not as a sentence template. The transferable lesson from published papers is the relationship between engineering requirements, intermediate objects and evaluated outcomes. An accepted paper can still contain redundant or unsupported prose. Source-reading notes are in [the published evidence index](published-evidence.md).

## 1. Recover The Mechanism Before Improving The Sentence

Write an internal row for every operation that matters to the claim:

| Input and physical/model level | Operation | Output | Next consumer | Evidence | Uncertainty |
|---|---|---|---|---|---|
| Observed measurements | Actual encoder | Encoded measurements | A specified relation learner | Equation, figure, code if available | Unknown input axis must remain unknown |

Do not require all papers to have grouping, stages, gates or multiple branches. For a soft sensor, the chain may be measurements, an estimated state and a quality prediction; for weak supervision, instance features, bag aggregation and a bag-level objective. Where the source does not expose an interface, ask rather than inventing one.

For multistage fusion only, inspect whether a pooled stage vector is the final output or an intermediate context returned to variable-level features. Independently encoded features can share encoder weights; `independent` does not necessarily mean separately parameterized. A residual branch may preserve features while a different fusion module combines them. An attention prior added to scores is not automatically a causal model or a hard topology constraint.

When a feature bypass matters to the advance, explain its actual merger rather
than deriving the operation from the module title. P11/P15/P14 define additive
residual paths, including dimension matching where needed. For a verified design,
`The mapped input is added to the transformed features, which then supply the
classifier` states a positive connection. A different design may concatenate two
parallel feature sets; retain an approved proposed name and describe that actual
operation. Put shape checks in Methods and avoid claiming lossless information
retention or a generalization gain merely from either merger. A routine residual
connection is not automatically an independent contribution.

Mark each operation as prediction-time computation, training objective, pretraining, or test-time adaptation. These are different relationships, not successive boxes in one forward pass. An alignment loss can shape an encoder during training without receiving its output during deployment; a reconstruction decoder can be absent at inference. When this distinction is central, the abstract needs one clear training-to-prediction connection rather than a fictional sequence. Published examples P10, P17 and P21 illustrate different training interactions; P25 even uses different branch components for training and prediction.

For active label acquisition, connect the sample-selection principle to the
annotations obtained, the learner they update and the predictor retained for
the engineering task (P89-P91). This is a learning relationship, not a final
fusion of labels and sensor features. State the distinguishing acquisition
principle rather than treating a routine query loop as novelty. Put ordinary
pool-separation safeguards and detailed budget accounting in settings or author
notes; retain a simulated-annotation condition when needed to interpret a cost
claim. A result at equal label budgets is not already a result about less human
time or fewer labels at equal predictive performance.

For threshold-based feature processing, connect the threshold's input to the
transformed features and their next use. A verified design may compute thresholds
from encoded measurements, shrink the features and combine them with a bypass
before classification. That positive chain is clearer than claiming that a
threshold knows which components are noise. P87/P88 illustrate different
threshold generators and mergers, not a compulsory architecture. Select the
distinctive relationship for the contribution; routine thresholding alone is not
new, and a noisy-input classification gain is not a clean-signal recovery score.

A modified network copy is another possible training relationship. If a verified
design uses a parameter-masked copy to supply contrastive views, connect that
perturbation to the encoder it trains and then to the retained predictor. Explain
the distinctive pairing or learning rule where it matters, rather than presenting
the copy as a subsequent compressed classifier. Keep routine mask percentages
and implementation checks in Methods or author notes. A pruning operation can
support a representation-learning contribution without establishing deployment
compression; its name alone supplies neither novelty nor a measured benefit.

**Prepared models and runtime decisions, illustrated by P85:** when a system
selects among fixed model variants, connect available operating/network state to
that choice and the resulting engineering decision. For a verified design:
"A scheduler selects a prepared model using the current queue and link state.
The selected model classifies the incoming measurements." Add the distinguishing
selection principle or joint decision, not a fictional sequence of online weight
updates. If evidence uses a modeled execution cost, keep the simulation scope in
the result instead of rewriting it as measured device acceleration. One variant's
count is not the memory occupied by a resident collection of variants.

When alignment is the advance, identify what is brought into correspondence and by which criterion: sample times, dimensions, feature distributions or paired representations. Connect that operation to the learned predictor or next computation, not to an unverified claim that all diagnostic information is preserved. A method sentence can state that an objective encourages a property; a result sentence needs evidence that the property or downstream benefit was obtained. See the [alignment distinctions](terminology-decisions.md#alignment-state-the-object-and-criterion); keep only the central relationship in the abstract.

For each retained mechanism, recover three things: **the object changed, the operation, and the reason the changed object is useful to the next task**. The abstract should retain the distinguishing operation and its purpose, not every tensor name. The method section can carry exact dimensions. Never compress variable features, pooled group features and a stage summary into one interchangeable `feature` if the next operation consumes only one of them.

Keep a changing intermediate object distinct from a changed model. A gate or grouping assignment recomputed from the current input can be adaptive with fixed trained parameters; it need not involve online parameter learning. Likewise, retain the actual output target across sections: product-defect classification, quality estimation and root-cause identification are not interchangeable endpoints. The [terminology decisions](terminology-decisions.md) distinguish these cases without prescribing additional modules or tests.

## 2. Give Each Sentence A Job And A Connection

Use whichever functions the study needs:

- establish the engineering task and a consequential process property;
- identify a remaining capability, supported by prior-work evidence;
- introduce the method and the specific problem it addresses;
- explain the main mechanism through the objects it produces and consumes;
- connect the final representation, estimate or decision to the engineering task;
- state what the actual evaluation establishes.

Read consecutive sentences as a pair. Ask what the reader now knows, what the next sentence adds, and whether the link is causal, sequential, parallel, conditional or evidential. A conjunction cannot repair a missing relationship. Conversely, repeated object names can be useful for technical continuity; avoid synonym changes that obscure identity.

Keep the mechanism check more detailed than the replacement prose. Select the relationships needed to understand the advance; do not transfer every verified sampling detail, component inventory and exclusion into the same method sentence. A condition already established clearly need not be repeated in a trailing `with ... and ...` clause. Move secondary implementation facts to the explanation or the appropriate section, while retaining any information-access condition needed to prevent a misleading claim. For a training-only auxiliary path, normally describe the retained predictor positively instead of adding a sentence listing components it does not execute. Likewise, routine safeguards such as withholding test labels from tuning belong in experimental settings unless that information boundary distinguishes the research claim. Keep an explicit exclusion or contrast when it actually defines the task or resolves a likely ambiguity. Give a sentence one main explanatory job with its necessary dependencies; a clear relative clause is welcome. Do not impose a word cap or split a coherent operation merely to produce short sentences.

Use scope phrases such as `within each unit` and `across units` when they mark genuinely different operations. They are not redundant merely because both occur at sentence starts. Avoid restating the same scope twice in one short sequence. `Intra-` means within; `inter-` means between. `Cross-stage fusion` and `inter-stage relationships` can coexist if they denote an operation and a relation consistently.

Choose the connection from the actual dependency:

| Relationship | What the reader needs | Misleading shortcut |
|---|---|---|
| Sequential transformation | Which output becomes the next input and what new operation it enables | `These features` when several incompatible outputs precede it |
| Parallel complement | What each path retains or estimates and where the outputs meet | `Then` implying one path is computed from the other |
| Training constraint | Which representation or parameter is shaped, by which supervision | Describing a loss as another inference-time fusion module |
| Prior-guided computation | Where given knowledge enters a learned operation | Saying knowledge and features are concatenated when knowledge only biases scores |
| Adaptation across phases | What changes, using which newly available information | Calling a learning phase a production stage |
| Update control | Which event changes learning, and when the required feedback is available | Implying that an update trigger controls sensor acquisition or is itself a fault alarm |
| Alternating refinement | Which two objects update each other during fitting, and what is retained for prediction | Describing a reciprocal training cycle as two independent modules or a one-way inference pipeline |
| One head, different decision outputs | Which head quantity supplies the class estimate, and which supplies a defined uncertainty or rejection decision | Calling evidence, belief mass and class probability interchangeable, or inventing rejection because uncertainty is reported |

Make the final method sentence advance from operation to task meaning. It may explain that a representation combines local measurements with system-level context, or that a predictor uses information from unlabeled observations. It should not re-list all modules or promote combination itself to proven generalization. A verified short sentence is preferable to a long sentence containing two vague `which` clauses.

When multi-head processing is central, explain the represented inputs and how the
head outputs reach the predictor, rather than describing head count as additional
physical sensors or independently discovered relations. P11/P82 distinguish
combined head features from any separate use of attention coefficients. Preserve
that distinction in an overview; include only the connection needed to understand
the abstract's actual advance. Ordinary parallel heads alone are not a new
contribution, and their normalization is not the final task decision.

## 3. Illustrative Repair, Not Manuscript Text

**Synthetic specification:** a shared encoder yields per-sensor features; a relation module updates those features; the classifier combines the updated features with their unchanged counterparts. No domain-transfer experiment exists.

Weak description: "An encoder is designed. A relation module is introduced. A fusion module improves generalization."

Source-faithful alternative: "A shared encoder first extracts features from individual sensor signals. A relation module uses these features to model dependencies between sensors. The classifier combines the updated features with the original encoder outputs, retaining both relational context and individual-sensor information."

The repair establishes the interfaces and removes an untested outcome. It does not prove that the mechanism is novel. In a real abstract, add its actual differentiating principle and supported purpose; do not use this generic example verbatim.

For a sequential mechanism, one sentence with a well-attached relative clause may be clearer than two sentences repeating the same subject. Split only when independent claims or stacked modifiers impair reading. `First`, `then`, and `finally` are available, not required.

**Different synthetic specification:** a soft sensor shares an encoder between a quality predictor and a reconstruction decoder. Unlabeled measurements train the reconstruction path; only the encoder and predictor are used at inference.

Source-faithful alternative: "A shared encoder learns from labeled and unlabeled process measurements through prediction and reconstruction objectives. The quality predictor uses this representation to estimate the target from available process measurements."

The second example needs no fabricated sequence of `reconstruction, then fusion, then prediction`. Neither example supplies novelty or empirical benefit by itself. Attach the manuscript's actual distinguishing design and supported evaluation, leaving routine components in the background. P03 also illustrates that a concise abstract can connect mechanisms and output without approaching a fixed word count.

**Another relationship, illustrated by P36:** task-specific gates combine shared expert outputs for the respective quality targets, while gradient balancing changes how those tasks train the shared parameters. The writing should connect the two roles through their common multitask objective, not claim that the balancing module receives the fused features during prediction. This illustrates a shared training relationship, rather than the sequential feature-fusion story used in the first example.

**An alternating relationship, illustrated by P40:** a label representation guides feature selection, and the selected features change the neighborhoods used in the next label update. Describe both directions once, then name the returned feature subset. A synthetic writing pattern is: "During fitting, label weights guide feature selection, while the selected features refine the sample neighborhoods used to update those weights. The resulting subset supplies the inputs to the diagnostic predictor." Use this only when those interfaces are verified. Label weights are not automatically measured fault severity, and feature selection is not automatically sensor removal. Reciprocal design can motivate one linked contribution; it does not itself establish convergence, novelty or improved performance.

**Teacher-guided learning, illustrated by P45-P46:** name the transferred object and the learner that uses it, then connect the trained predictor to the engineering output. Do not write a training loss as a final fusion of teacher and student features. For a verified regression design, a synthetic two-sentence description could be: "Teacher features and predictions guide the student during training. The trained student estimates product quality from the available process measurements." Add the actual distinguishing transfer operation where it matters; this generic description is not a contribution. When a separate exit controller or retained teacher call defines inference, explain that relationship rather than attributing it to distillation itself. A contribution can connect a particular guidance rule to the student capability it trains, but needs its own novelty and outcome evidence.

**Class-guided representation learning, illustrated by P21:** connect the estimated class information to the representation relation it trains, rather than listing a temporal module and a graph module as unrelated advances. A synthetic description for a verified design is: "Temporal contrastive learning trains the encoder to associate contexts with later features across augmented views. Class estimates guide relationships between training samples, linking this representation objective to the diagnostic task." The associated test-time encoder/classifier belongs in the overview; add it to the abstract only when needed to distinguish the prediction path. This describes a training interaction, not physical forecasting or learned production topology. Novelty must reside in the actual coupling or target construction and its evidence, not in merely using two standard objectives. Other contrastive designs need their own object and pairing descriptions.

**Relationship modeling followed by origin analysis, illustrated by P13/P16:** identify the object passed to the decision rule, not merely a second module name. P13 uses learned graphs in a subsequent top-down node-scoring procedure; P16 analyzes abnormal links after detection. An abstract can connect the relationship representation to its actual ranking or interpretation output. A contribution should expose the distinguishing relation-to-decision design, rather than equating a prediction loss with root identification or repeating the graph learner as two advances. Keep a source's particular procedure attributed; do not invent a classifier, a physical intervention or a new contribution merely to complete a familiar pipeline.

**Node updates followed by task-level use:** connect the represented objects,
not just graph-related names. For a verified classifier design, two synthetic
sentences are: "Neighbor-weighted updates combine features over expert-specified
variable connections. Unit-wise means summarize the updated features, and the
concatenated unit vectors supply the fault classifier." Add the actual encoder
and distinctive weighting design where needed; these ordinary operations alone
are not a contribution. A graph whose nodes are variable-time pairs (P07) differs
from a production-unit hierarchy (P13). Preserve the actual axes, fixed versus
learned connections and output level instead of borrowing a hierarchical or
causal name to make the abstract sound stronger.

**Gated contributions and their recipient:** describe what determines the gate,
what it scales and where that contribution is used. For a verified two-path
classifier: "Local and neighborhood features jointly determine a gate that
scales the neighborhood contribution. Adding that contribution to the local
features forms the classifier input." Other designs may gate different objects;
do not force this structure onto expert mixing or attention-output gating.
Connect any distinguishing gate design to its actual task evidence rather than
presenting the base gate as a separate invention. A residual bypass changes the
meaning of suppression, and a dense input-dependent gate need not be sparse
execution or online learning. Keep those audit judgments in the author note
unless needed to interpret a retained manuscript claim.

**Source-model transfer, illustrated by P78/P79:** this is a relationship across
learning phases, not necessarily fusion of source and target features. Explain
the engineering access restriction, the retained source knowledge and the
target-side guidance that shapes the predictor. For a verified design, a
synthetic connection is: "A source-trained model initializes the target
predictor. Target-derived class guidance then trains its representation from
the available measurements, and the adapted model performs fault
classification." Replace the generic guidance with the actual distinguishing
selection or objective; state which components change where that matters.
An existing source-free setting motivates a contribution but does not itself
make the target-learning design novel. Preserve batch/stream scope and observed
class-level trade-offs without turning audit exclusions into abstract padding.

A frozen backbone's prediction may instead be combined with a target-adjusted
correction. Connect the changed object to the corrected prediction or
decision, separating prior calibration from updates during evaluation. Keep the
distinctive adaptation principle in the abstract; routine buffer and optimizer
details belong in Methods, not another list of independent contributions.

**Semantic transfer, illustrated by P05/P06/P80:** state what the class
descriptions enable rather than listing a text model beside a sensor model.
For verified semantic matching, connect predicted attributes to the supplied
candidate descriptions and fault identity. For verified feature generation,
connect the descriptor-conditioned generator and its training constraint to
the generated features, classifier fitting and retained prediction path. A
synthetic connection is: "Class descriptions condition feature generation.
The synthesized unseen-class features train a classifier that diagnoses real
process measurements." Add the actual distinguishing constraint or matching
rule; the existing zero-shot setting and ordinary validation are not themselves
that advance. Keep any representation retained from a training component (as
in P80), rather than assuming it vanishes at prediction. Preserve the actual
candidate pool and observed seen/unseen trade-off without copying the resource
ledger or every class count into the abstract.

**Observation timing, illustrated by P08/P24/P73:** connect the acquired object
to the specific representation or estimator it supplies. An abstract can move
from different native sampling schedules to the operation that uses available
measurements or actual intervals, then to the quality estimate, graph or alarm.
For a verified interval-weighted predictor: "Each stream is encoded at its native
observation times. Measured intervals weight these representations before fusion
for quality estimation." Add the real distinguishing design, not a new timing
module name. A contribution may concern how the predictor uses those observations;
using intermediate measurements is not proof of recovering every unobserved value.
State the supported benefit and remaining rate/interval sensitivity in the result.

**Rule-based prediction, illustrated by P27/P77:** distinguish input matching,
rule-weighted numerical outputs and a final task decision. A Gaussian function
name alone does not explain how a predictor uses the result. For a verified
regression design, the connection can be stated directly: "Membership degrees
determine rule weights, which combine local quality estimates into the final
prediction." Add the actual distinguishing learning or rule-design principle,
not another list of ordinary layers. When rule decisions guide an encoder during
training, name the trained representation and retained predictor rather than
inventing a final feature-fusion module. Place quantity/interpretation checks in
the author note; keep supported task meaning and empirical trade-offs in prose.

**Training-loss weighting:** connect the factors to the learner, then the
retained classifier to the engineering decision. If verified: "Class-dependent
weights scale the training errors of the temporal classifier. The fitted model
assigns fault classes to new process measurements." Supply the actual
distinguishing rule rather than claiming routine weighting as an advance. Do not
turn a training coefficient into an inference-time gate, feature-fusion module or
additional score multiplier. P93 illustrates weighted fitting, whereas P92/P94
weight augmentation selection; those names cannot substitute for this interface
check. Close on the reported metric and relevant class trade-off. A weighted
aggregate gain alone does not substantiate rare-fault improvement; explain the
weight/sampler arithmetic in the settings, not in every abstract.

**Evidence combination:** connect the encoded outputs to the kind of combination
actually performed and to the final diagnostic decision. A feature sum feeds a
classifier; a defined mass-combination rule produces masses that need their own
decision rule. When implemented, a concise connection is: "Each stream supplies
class-support masses. Their combination yields the support used for the final
fault decision." Add the actual differentiating weighting or conflict treatment,
not a generic claim that combination guarantees reliability. A fallback need not
appear in every abstract, but retain it when it defines the evaluated output.
See [the mass-to-decision check](terminology-decisions.md#combining-belief-masses).

## 4. Contributions Are Advances, Not An Execution Log

For each candidate contribution, privately record: closest prior capability; remaining requirement; actual change; evidence that discriminates the change; scope. Do not state "the first" without a defensible literature search.

Common organizations include an overall principle plus linked mechanisms, a problem formulation plus analysis and solution, or a necessary engineering adaptation plus a new validated finding. Select the structure supported by the work. A standard encoder and a proposed relation learner can belong in one item when the encoder supplies the latter's inputs. The second sentence should explain that dependence instead of starting another unrelated mini-contribution.

Two checks catch padding: Does item 3 merely repeat item 1 at greater length? Would deleting a module name leave the claimed advance unchanged? Case studies normally belong in the evaluation summary unless the cases establish an original dataset, operational capability or scientific finding. Do not universally delete an experiment contribution from other papers.

Apply the same test to ablation claims. If an item only says that removing the proposed components worsens the task metric, it normally supports the design contribution rather than adding another advance. Attach that evidence to the design item or place it in the evaluation summary. Keep a separate empirical contribution when it answers an independently stated engineering question, establishes a new resource/capability, or yields a supported finding beyond confirming the proposed design. An accurate result is not automatically a separate contribution; one well-supported item is preferable to a second item that restates its verification.

An overall-framework item is useful when it states an organizing principle or new capability not repeated by the component items. A component item should then expose the specific operation that realizes part of that principle. When two operations are inseparable, connect them through their input/output or shared objective in one item. Do not claim an off-the-shelf encoder as an independent advance merely to balance the list.

Check novelty and sentence linkage separately: a logically smooth item can still contain no new contribution. P10 and P17 use two contribution items; P06 organizes three linked advances; P08 includes problem analysis. These observed structures support flexibility, not an item-count prescription. Use [contribution routes](contribution-narratives.md) for deciding what warrants a claim.

P38 separates model operations from a new cross-modal benchmark resource. A resource item should identify what data, annotations or evaluation capability it adds, with verified scope and access status. It is not equivalent to an item saying that the authors ran experiments; neither dataset size nor a promised release alone proves novelty or public availability.

For a few-shot contribution, link the particular mechanism to learning or prediction with the declared limited labels. The setting itself is not a new mechanism. Distinguish few current-task labels from few labels across the full learning history before claiming reduced annotation requirements; put detailed resource accounting in experimental settings. The [scarce-label playbook](topic-playbooks.md#2-scarce-labels-few-shot-zero-shot-weak-or-self-supervised-learning) preserves legitimate base-data learning, fixed low-data training and episodic alternatives.

## 5. Close On Evidence At The Correct Level

Parallel case phrasing can name two processes, or two datasets, but should not confuse a physical process with a data object. A simulator-derived benchmark and production data supply different evidence. `Real-world` describes provenance, not online deployment. Use `offline` only when the evaluation distinction matters.

Check the claimed output before choosing the ending: generation fidelity, quality-prediction error and diagnostic accuracy are not interchangeable. A generation study may close on generation and measured downstream usefulness (P32), while an augmentation study closes on the actual diagnostic evaluation (P35). Where production measurements are combined with injected faults, avoid calling all tested faults real plant events. Include this distinction in the abstract only as needed to keep its case/evidence claim accurate; place the full construction in Methods.

`Effectiveness`, `engineering applicability`, and `generalization` are different claims. The first needs relevant task evidence. For the second, identify the engineering setting and what the evaluation establishes: an engineering-grounded simulation can support relevance or feasibility under its modeled conditions, whereas applicability to an actual production setting needs representative evidence from that setting. Neither alone proves deployment. For generalization, specify the target population: a valid independent held-out split can assess prediction on new samples from that population, but transfer across conditions, sites or time regimes needs corresponding held-out evidence. `Verified` and `demonstrated` are both available for empirical evidence; neither creates proof or certifies deployment. Avoid empty superiority endings when a bounded finding is clearer.

One closing sentence can name the cases and supported outcome. Use two when the second adds an actual finding, trade-off, evaluated condition or substantive engineering consequence, not a second statement that experiments were performed or a paraphrase of the same metric gain. A sentence saying the comparison supports the benefit of a combination adds little when the preceding result already states that the combination outperforms its matched single-path control. Keep a genuinely new interpretation; do not fill a word target with a validation restatement. Preserve parallel objects: `case studies on process A and process B` is coherent without turning one process into a dataset for grammatical symmetry. A two-case pattern is not mandatory for other studies.

When correcting an overclaimed ending, write the supported finding at its actual evaluation level. Do not carry the deleted claim back into the abstract as a trailing statement that it was not established. For example, a contrast between adjusted and raw detection scores is itself an informative result; the reason for deleting an unsupported warning claim belongs in the author note. Retain a limitation in the abstract when it changes how the retained claim must be interpreted, such as the scoring rule or permitted target-data access. This is a placement decision, not a ban on negative findings or necessary qualifications.

Do not introduce class imbalance, every fault label or hardware detail in the abstract merely because it occurs in the dataset. Include such a fact when central to the problem or necessary to interpret the result; otherwise develop it in data analysis, metrics or implementation details. Quantitative results may be useful when supported and permitted by the author and venue.

## 6. Synchronize Meaning, Not Identical Wording

| Section | Synchronization question |
|---|---|
| Introduction | Does the claimed gap motivate this mechanism, without repeating another paragraph's gap? |
| Contributions | Are advances, their inputs and their roles aligned with the new abstract? |
| Motivation/problem | Are information access, prediction target and assumptions unchanged? |
| Overview | Is the operation order and parallel-path structure correct? |
| Module opening/closing | Is the received output named, and does the closing output feed the stated recipient? |
| Diagram/formula | Do granularity, dimensions, gate placement and arrows match? |
| Experiments | Is the new purpose actually measured? Do not invent a new result to match prose. |
| Discussion/conclusion | Is the interpretation at the same evidential level? |

An abstract rewrite does not automatically require editing every section. Preserve correct text; list technical ambiguities separately from optional prose. Use [the synchronization ledger](../assets/templates/abstract-body-sync.md).
