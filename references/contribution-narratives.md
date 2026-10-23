# Contribution Routes For AI-for-Engineering Papers

Use when choosing an argument, structuring the Introduction/Related Work, or calibrating contribution claims. Keep the engineering object, operating conditions, information access, decision output, and evidence visible. The source of an idea may be a process observation or a method insight; the paper must establish why the resulting capability matters for the engineering task.

## Record Novelty On Separate Axes

Describe the contribution on problem formulation, method/mechanism, engineering adaptation/integration, and evidence/understanding. One axis can lead while others support it. A familiar task can carry a strong new mechanism; a newly formulated task can use established tools; a useful adaptation may contribute a well-evidenced capability under realistic constraints. Neither task familiarity nor a new task label establishes scientific value by itself.

The portfolio's A/B/C labels are coarse planning aids. They are separate from manuscript archetypes and the routes below. A new problem is not automatically A; a familiar problem is not automatically C. Quality follows significance, substance, comparison fairness, and evidence, not vocabulary or journal-tier labels.

## Select The Argument Route

| Route | What must be established | Main argument | Evidence that earns the claim |
|---|---|---|---|
| New problem or formulation | A consequential industrial condition or decision is inadequately represented in existing formulations | Engineering observation → mismatch with existing task/assumptions → precise formulation → suitable response | Source-grounded task differences, operational relevance, valid labels/measurement, and comparison under the new definition |
| Familiar problem, new mechanism | Existing work solves the task to a documented extent; a specific capability remains limited | Prior achievement → remaining capability under condition C → mechanism addressing it → observed effect | Closest-mechanism controls, fair inputs/budgets, isolating tests, and practical effect under C |
| Interacting constraints | Two or more conditions interact to change identifiability, supervision, information access, objectives, or feasible decisions | Individual conditions → demonstrated interaction → resulting requirement → response to the interaction | Single-condition controls plus joint-condition tests; assess interaction and failed simpler alternatives |
| Substantive engineering adaptation | A known method's assumptions or implementation do not meet an actual operating requirement | Established capability → actual engineering constraint → specific adaptation → engineering benefit and cost | Matched unadapted baseline, implementation/assumption accounting, robustness or utility tests relevant to the constraint |
| Focused comparative improvement | A limited change or comparison answers a useful, independent question | Relevant comparison target → precise modification → reproducible local gain/trade-off → supported scope | Competitive relevant baselines, uncertainty where it matters, effect size and resource cost; transparent cases where the method does not win |

Routes may combine when the argument requires it; name the dominant route to keep the manuscript coherent. Select cases from the claim and data, not from a fixed two-dataset template. Select venue fit only after clarifying the contribution and engineering relevance.

## Make Interactions Real

Combining “few labels” and “multi-label diagnosis” is initially a candidate setting. Determine whether limited labels leave particular label combinations unobserved, whether faults co-occur physically, and whether the available annotation supports the proposed output. Define the resulting learning/evaluation question and information boundary. Simply concatenating task names or adding a second loss is not evidence of a new problem.

Likewise, coupling operating-condition shift with fault propagation can matter if it changes the validity of transfer assumptions or the meaning of propagation evidence. That claim needs process/data support; an attention map alone does not establish propagation or root cause. Compare separate-condition and joint-condition alternatives when the interaction itself is the contribution.

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

Generalization, practicality, effectiveness, and efficiency are distinct outcomes. A plausible mechanism motivates a generalization test; it does not establish a gain before held-out conditions or other appropriate evidence are evaluated. An improvement in one metric can justify a focused claim, while costs, failure cases and task relevance determine its engineering significance.

## Turn Analysis Into Manuscript Prose

Maintain evidence states, missing-input flags, and reviewer-risk notes in internal artifacts. In the manuscript, state the supported contribution directly and place necessary information/scope conditions where they govern interpretation. Avoid turning the Introduction into repeated disclaimers about what the study does not prove.

Related Work should advance by capabilities, assumptions, and remaining needs: each group establishes what the next group addresses and why a remaining requirement matters here. Preserve useful conceptual contrasts; remove contrast that merely rehearses an imagined objection. Use [argument and prose craft](argument-and-prose-craft.md) for paragraph-level execution.

Before drafting a contribution sentence, answer: what changes, relative to what verified work, under which engineering conditions, through which operation, and with what evidence? The wording should expose those answers rather than invent significance.
