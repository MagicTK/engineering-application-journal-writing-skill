# Contribution Routes For AI-for-Engineering Papers

Use when choosing an argument, structuring the Introduction/Related Work, or calibrating contribution claims. Keep the engineering object, operating conditions, information access, decision output, and evidence visible. The source of an idea may be a process observation or a method insight; the paper must establish why the resulting capability matters for the engineering task.

## Record Novelty On Separate Axes

Describe the contribution on problem formulation, method/mechanism, engineering adaptation/integration, and evidence/understanding. One axis can lead while others support it. A familiar task can carry a strong new mechanism; a newly formulated task can use established tools; a useful adaptation may contribute a well-evidenced capability under realistic constraints. Neither task familiarity nor a new task label establishes scientific value by itself.

The portfolio's A/B/C labels are coarse planning aids. They are separate from manuscript archetypes and the routes below. A new problem is not automatically A; a familiar problem is not automatically C. Quality follows significance, substance, comparison fairness, and evidence, not vocabulary or journal-tier labels.

## Separate A Principle From Its Implementation

An overall-method contribution should name the principle or capability that organizes the design, not simply announce an acronym. Component contributions explain the particular advances that realize it. If the overall item and a component item make the same claim at two lengths, merge or redistribute them. If two operations form one advance, explain their dependency instead of splitting them to reach a conventional item count.

For each item, distinguish **what is new** from **what makes it work**. A standard encoder may supply features to a new relation mechanism without becoming a second novelty claim. An auxiliary objective may explain how a predictor learns from unlabeled measurements without existing in the inference graph. A contribution should remain technically recognizable after removing promotional adjectives and module acronyms.

Published organizations differ: P10 and P17 use two items, P06 presents three linked advances, and P08 includes problem analysis alongside a solution. Their checked locations are in [the passage analysis](published-evidence.md#passage-level-writing-analysis--段落级写作分析). Transfer the logic, not the count or a claim of theory that this work does not contain.

**Synthetic design, not a reported result:** a conventional encoder feeds a new mask-aware aggregation rule that accepts changing sensor subsets. A coherent candidate item is: "A mask-aware aggregation rule combines the available sensor features, allowing the diagnostic model to operate with varying sensor subsets." The standard encoder is supporting machinery, not another claimed advance. This describes a design capability only when the implementation supports it; any accuracy, robustness or novelty claim still needs its own comparison. The contribution should identify the distinguishing operation more specifically when known.

An empirical item must state the finding or new resource, not merely the effort: what engineering question does the comparison resolve, under which conditions, and with what evidence? A routine benchmark plus a real-world case usually validates the method; a demonstrated new operational capability or previously unresolved trade-off may itself warrant a contribution. Do not erase a legitimate empirical contribution because it mentions experiments.

## Select The Argument Route

| Route | What must be established | Main argument | Evidence that earns the claim |
|---|---|---|---|
| New problem or formulation | A consequential industrial condition or decision is inadequately represented in existing formulations | Engineering observation → mismatch with existing task/assumptions → precise formulation → suitable response | Source-grounded task differences, operational relevance, valid labels/measurement, and comparison under the new definition |
| Familiar problem, new mechanism | Existing work solves the task to a documented extent; a specific capability remains limited | Prior achievement → remaining capability under condition C → mechanism addressing it → observed effect | Closest-mechanism controls, fair inputs/budgets, isolating tests, and practical effect under C |
| Interacting constraints | Two or more conditions interact to change identifiability, supervision, information access, objectives, or feasible decisions | Individual conditions → demonstrated interaction → resulting requirement → response to the interaction | Valid single/joint-condition comparisons or analysis that distinguishes the interaction from separate effects; use meaningful simpler alternatives |
| Substantive engineering adaptation | A known method's assumptions or implementation do not meet an actual operating requirement | Established capability → actual engineering constraint → specific adaptation → engineering benefit and cost | Matched unadapted baseline, implementation/assumption accounting, robustness or utility tests relevant to the constraint |
| Focused comparative improvement | A limited change or comparison answers a useful, independent question | Relevant comparison target → precise modification → reproducible local gain/trade-off → supported scope | Competitive relevant baselines, uncertainty where it matters, effect size and resource cost; transparent cases where the method does not win |

Routes may combine when the argument requires it; name the dominant route to keep the manuscript coherent. Select cases from the claim and data, not from a fixed two-dataset template. Select venue fit only after clarifying the contribution and engineering relevance.

## Make Interactions Real

Combining “few labels” and “multi-label diagnosis” is initially a candidate setting. Determine whether limited labels leave particular label combinations unobserved, whether faults co-occur physically, and whether the available annotation supports the proposed output. Define the resulting learning/evaluation question and information boundary. Simply concatenating task names or adding a second loss is not evidence of a new problem.

Likewise, coupling operating-condition shift with fault propagation can matter if it changes the validity of transfer assumptions or the meaning of propagation evidence. That claim needs process/data support; an attention map alone does not establish propagation or root cause. When the interaction itself is the contribution, distinguish it from separate effects using valid comparisons or analysis. If removing one condition makes the task undefined or changes available information, do not invent an impossible control; state the changed comparison scope and use a justified alternative.

These are reasoning examples, not claims about any particular dataset or proof that the research direction is novel. Establish the nearest prior treatment of the joint setting before describing it as new.

## Position Prior Work Fairly

For the closest relevant work, record:

1. its actual achievement and conditions of evaluation;
2. the assumption, information access, or capability relevant to this study;
3. evidence that the current industrial setting changes what is required;
4. the proposed response and why that operation addresses the requirement;
5. the experiment that distinguishes this response from reuse or a simpler alternative.

Distinguish “outside the paper's evaluated scope,” “not represented in its formulation,” and “shown to fail under a matched test.” An untested setting is not proof that the prior method cannot work there. Avoid dismissing an entire field because a few selected papers omit one condition. Use representative and nearest competitors, not only convenient weak baselines.

A defensible argument is:

`documented prior capability → evidenced remaining requirement → concrete design response → discriminating test → measured engineering outcome`

For a new formulation, explain why existing task definitions miss a relevant condition. For a familiar problem, explain which capability improves and how. The same honest chain can support either paper.

## Choose Comparisons Proportional To Claims

A paper need not beat every published model. It must test the comparison that supports its stated advance using relevant, reasonably competitive alternatives and fair settings. Explain why each baseline is included and identify inaccessible implementations. A selected reference method can be an informative target without licensing a field-wide best-performance claim.

Generalization, practicality, effectiveness, and efficiency are distinct outcomes. A plausible mechanism motivates a generalization test; it does not establish a gain without independent held-out evidence for the stated target population. New samples from the same population and transfer to changed conditions or sites are different claims, each needing the corresponding separation and information boundary. An improvement in one metric can justify a focused claim, while costs, failure cases and task relevance determine its engineering significance.

## Turn Analysis Into Manuscript Prose

Maintain evidence states, missing-input flags, and reviewer-risk notes in internal artifacts. In the manuscript, state the supported contribution directly and place necessary information/scope conditions where they govern interpretation. Avoid turning the Introduction into repeated disclaimers about what the study does not prove.

Related Work should advance by capabilities, assumptions, and remaining needs: each group establishes what the next group addresses and why a remaining requirement matters here. Preserve useful conceptual contrasts; remove contrast that merely rehearses an imagined objection. Use [argument and prose craft](argument-and-prose-craft.md) for paragraph-level execution.

Before drafting a contribution sentence, answer: what changes, relative to what verified work, under which engineering conditions, through which operation, and with what evidence? The wording should expose those answers rather than invent significance.
