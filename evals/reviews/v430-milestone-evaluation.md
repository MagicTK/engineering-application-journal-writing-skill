# 4.3 Milestone: Capability And Evidence Review

Date: 2026-10-27. This is a consolidation of the 4.2 work, not a claim that
every reference, future manuscript or possible use has been validated.
The suite retains its existing Skill and template structure.

## Scope And Source Continuity

The maintainer reconciled the requested outcomes against current instructions
and actual prior records. A content comparison against the installed-writing
snapshot `afe03b7fa386a02569cc148dc81032ee0a58745a` covers 58 entry/reference
Markdown files: 21 are byte-identical, 28 differ only in their whole-line suite
version metadata, and nine contain substantive changes. Only version metadata
is normalized; prose and examples are not masked.

Those nine files have scoped follow-up evidence: terminology and published
notes in the branch-conversion, rate-conversion and fault/disturbance checks;
the two execution references' optional fictional-example links in the
result-workflow check; and the two static corrections below. File identity
preserves provenance, not the breadth of a historical test.

| Requested capability | Implemented guidance and actual evidence | Remaining boundary |
|---|---|---|
| Industrial problems before model families | [Problem-first classification](../../references/problem-first-classification.md) separates observations, annotation, operating conditions, resources, tasks and scales. Its conditional many-to-many navigation keeps time-series mechanism leads separate from engineering naming authority. [Installed narrow requests](suite-coverage-evaluation.md) and [class-support checks](class-support-scope-evaluation.md) exercise selected distinctions. | These are routes for the defined problem, not automatic method recommendations or exhaustive coverage of all industrial settings. |
| Connected abstract, contributions and body | [Abstract craft](../../references/abstract-and-contribution-craft.md), [contribution narratives](../../references/contribution-narratives.md) and the [section guide](../../references/section-writing-guide.md) preserve actual operations, interfaces and evidence. The [installed seven-section response](../responses/installed-writing-chain.md) retains its first answer and two same-context prose refinements. | A coherent description does not establish novelty, data validity or journal acceptance. Length and section choices remain author/task specific. |
| Context-sensitive English and Chinese | The [bank](../../references/engineering-application-terminology-bank.md) separates general names, attributed names, functional descriptions and pending entries; Chinese wording is checked separately. [Bilingual terminology review](bilingual-term-parity-evaluation.md), [branch conversion](branch-conversion-evaluation.md), [sampling operations](rate-conversion-evaluation.md) and [fault/disturbance](fault-disturbance-evaluation.md) retain their definition/read limits. | The ledger is partial. Two source IDs alone do not certify semantic matches, a complete compound name, all translations or field-wide prevalence. |
| Whole-workflow and narrow requests | The [collaboration workflow](../../references/research-collaboration-workflow.md), bilingual entries and [installed workflow check](suite-coverage-evaluation.md) support coordinated writing as well as grammar-only and problem-only requests. [Entry-pair review](figure-route-scope-evaluation.md) checked all 14 pairs with local repairs. | A local task does not authorize experiments, a new research program, manuscript upload or unrelated edits. |
| Experiments, results and figures | [Evidence design](../../references/experiment-evidence-design.md) separates information access, repeated runs and claims. The [optional executable example](../../assets/examples/result-workflow/README.md) was [actually run](result-workflow-evaluation.md) to produce a table, SD plot and provenance record from fictional counts. Figure routes preserve source/editability and author locks. | This is not a general training engine, a rerun of a real study or proof of every plotting/client environment. |
| Review and handoff | [Rigor/handoff](../../references/rigor-and-handoff.md) separates scientific findings, text corrections and unresolved implementation checks. The installed workflow case retains an honest response ledger and author-owned figure changes. | These checks do not independently authenticate raw data, perform journal peer review or predict an editorial decision. |
| Group installation and clear bilingual documentation | Both READMEs include complete-suite installation, task entry points and original diagrams. The [official-helper download](suite-coverage-evaluation.md) matched the pinned published payload; [local presentation checks](result-workflow-evaluation.md) inspected the fictional example in desktop/mobile rendering. | The download and rendering records retain their original versions; they are not new client-discovery, GitHub-UI or cloud-CI tests. |
| Privacy and maintainable reuse | MIT attribution, public-export filters, source/dependency fingerprints and narrow publication review preserve the public/private boundary. No real paper, result, figure or experiment was edited for this milestone. | Literal scans are bounded checks, not proof against all semantic disclosure or every external clone/cache. Keep private records outside the public payload. |

This review found two remaining wording problems. The collaboration example
could imply that fewer labels change physical fault propagation; it now places
the effect on learning diagnostic relationships. The rigor guide grouped all
robustness settings under "disturbance"; it now asks for the actual variation
or constraint. These are corrections to review guidance, not new methods.

## New Scoped Use Check

One new responding context received the two fictional requests below after the
114 instruction/dependency hashes and criteria were frozen. It was not given
prior answers or evaluation files. The maintainer reviewed the complete first
answer; no corrective feedback or retest was needed. The responder was closed.

It disclosed automatically supplied historical context, but no memory-file
lookup or use of that history to fill the case facts. It read five Skill/guide
files, **not the two corrected shared references directly**. Thus the first
answer supports the routed task behavior, not a measured effect of either
specific wording change. There is no controlled baseline, independent second
grader, memory-blank claim or universal quality score.

## Requests

Use the Chinese orchestrator and relevant guidance from SUITE. Read only needed
Skill files, not evaluation files, private maintenance records, real papers or
other tasks. Do not edit files, run experiments or browse. Report actual reading
and any inherited context. Keep author notes separate from reusable English prose.

A. The physical process, fault events and measured observations are unchanged.
Only fewer of the same training samples receive fault labels. Known production
stages are coupled, and the proposed study examines the effect of limited labels
on learning diagnostic relationships between stages. There are no results or
adequate prior-work search supporting a new problem. Revise this into two
Introduction sentences and explain the issue: "Limited labels change fault
propagation across production stages, creating a new industrial problem."

B. Verified fictional values on the same task/test set: full-label training gives
macro-F1 of 88.0% for A and 87.0% for B; 10% training labels gives 82.0% and 79.0%.
A separate input-window-length study for A gives 80.0%, 82.0% and 81.0%.
No noise injection or new-condition test was performed. Classify what is tested,
then write two concise Results sentences retaining the positive findings.
Author notes may identify limits, but do not demand new experiments or append a
catalogue of unperformed tests to paper prose. The original claim is:
"A is robust to industrial disturbances and generalizes to changing operating
conditions."

The above is a public translation of the original Chinese prompt; the exact
prompt and first response are retained privately. The response below preserves
the scientific wording. Local path prefixes and writing-block wrappers are
normalized; private quota metadata is omitted.

## First Response

**A. 引言**

可用于论文的英文：

The known coupling between production stages makes inter-stage relationships relevant to fault diagnosis. This study examines whether and how reducing the number of labeled training samples, with the underlying measurements held fixed, affects the learning of these diagnostic relationships.

给作者的说明：原句把**监督信息减少**错误地写成了**物理故障传播改变**。研究问题应落在标签不足对诊断关系学习的影响上；目前也没有充分的前作检索支持“new industrial problem”，但这不妨碍清楚提出值得研究的问题。

**B. 实验含义与 Results**

这些实验分别检验：

- **完整标签与 10% 标签比较**：训练标签可用量对诊断性能的影响，以及 A、B 在相应条件下的表现。A 下降 6.0 个百分点，B 下降 8.0 个百分点；A 的领先幅度从 1.0 扩大到 3.0 个百分点。
- **窗口长度实验**：A 对输入窗口长度这一配置的敏感性。三个设置的分数相差最多 2.0 个百分点，反映已测试设置内的性能变化。

可用于论文的英文：

With 10% of the training labels, A achieved a macro-F1 of 82.0% compared with 79.0% for B, with a smaller decline from full-label training (6.0 versus 8.0 percentage points). Across the three tested window lengths, A maintained macro-F1 scores between 80.0% and 82.0%.

给作者的说明：上述干预分别涉及训练监督与输入配置，不能统称为已验证的“工业扰动鲁棒性”，也不能据此推出变工况泛化。没有噪声注入或新工况测试，因此删除原句中的对应外推即可，不要求补做实验。现有记录未提供重复运行的不确定性，故保留数值比较，不写“统计显著”；若正式稿尚未交代，可从已有记录补充窗口长度取值、标签抽取规则及 A/B 是否使用相同标签子集，无需重新核对题目已确认的信息。

**实际读取范围**
仅读取指定 Skill 目录内以下五个文件：

- [根入口 SKILL.md](../../SKILL.md)：第 1–220 行，用于定位中文入口及路由。
- [中文总控](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)：全文。
- [中文术语与语言润色](../../skills-zh/engineering-terminology-polishing-zh/SKILL.md)：全文。
- [中文实验与证据设计](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)：全文。
- [论证与文字精修指南](../../references/argument-and-prose-craft.md)：全文。

未读取 evals、私人维护记录、真实论文或其他任务；未改文件、运行实验或访问网络。[Private usage metadata omitted.]

**自动带入的历史上下文：有。**运行环境提供了既往工作摘要与偏好；本次未主动读取历史记忆文件，也未用这些历史内容补充两个虚构案例的事实或结论。

## Maintainer Judgment

Both cases pass their pre-specified narrow criteria. A proposes a learning
question under fixed physical observations and does not invent novelty or a
physical intervention. B distinguishes label availability and window-length
sensitivity, retains A's positive numerical comparison, and puts unsupported
noise/transfer claims in an author note rather than the reusable Results text.
The 6/8-point declines, 1/3-point gaps and 2-point window range follow directly
from the fictional supplied values. They are not recomputed real experiments
or a significance test.

The phrase "maintained ... between" is bounded by the three tested window
lengths; it does not assert stability over untested settings. Neither request
is evidence that every wording generated by the suite will be ideal. The new
record closes these observed local issues while earlier evidence retains its
own prompts, revisions and limitations.

Program tests, structure checks, public-content inspection and publication
identity are separate release tasks. Passing the writing cases does not replace
them, and their success does not strengthen the scientific claims above.
