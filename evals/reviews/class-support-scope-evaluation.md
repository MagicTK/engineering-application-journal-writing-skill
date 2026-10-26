# Class Support And Problem-Only Guidance

Primary report: [current forward report](../forward-test-report.json).

## Source findings and scope

A source reviewer read the complete English/Chinese problem-classification and
abstract/contribution reference pairs on 4.2.37: four files, 985 lines. It found
one material ambiguity: the Chinese imbalance row said category count, rather
than sample counts within each class. Version 4.2.38 clarifies that object in
both languages. A same-context reread confirmed the corrected rows.

The maintainer also aligned both README first-use rows with the existing
problem-only mode: describe the problem, constraints and open facts; provide
candidate methods when requested. The same reviewer checked that local parity.
Neither the source review nor the local recheck is a whole-suite certificate.

No new source, generic mechanism name, taxonomy category or methodological
prescription was added. The existing abstract/contribution rules remain unchanged.

## Procedure and results

The fictional requests, criteria, 108 instruction/dependency hashes and both
README hashes were saved before a new responding context received the prompt.
It answered all three requests once without the criteria or prior answers.
The maintainer judged that first response against the saved criteria.

| Request | First-response result | Subsequent action |
|---|---|---|
| A | Correctly separates two classes from 900/100 versus 500/500 support; preserves product-level unit; no difficulty/performance inference | Optional local tightening of two accurate but repetitive English descriptions |
| B | Distinguishes one-per-class balanced support from extremely limited labels; no assumed episodes, unlabeled data or result | Optional local tightening of the accurate sentence |
| C | Requests missing problem/observation/annotation facts without inventing a target or selecting a method/experiment | None |

Independent exact arithmetic confirmed two classes in all three sample-count
examples, with respective majority/minority ratios 9:1, 1:1 and 1:1; the totals
are 1,000, 1,000 and 2 samples. These are synthetic descriptive counts, not
inference about independence, field prevalence, prediction difficulty or results.

The first answer was factually and scope-correct, but the three replacement
sentences repeated totals, binary status or one-per-class support. One local
prose refinement was requested in the same context, without giving replacement
text or changing the suite instructions. Its replacements retain the counts,
unit and scope more concisely. Both responses appear below. This is not three
independent repetitions, an independent second grader, a controlled baseline
comparison or evidence of general quality improvement.

The respondent disclosed an accidental truncated read of another installed
research suite and unsuccessful path guesses before using the specified source.
It also had preloaded history. This limits attribution to the candidate alone;
no default installed-client discovery or isolated-source test is claimed. The
source reviewer and functional respondent did different tasks. No real paper,
data, experiment or figure operation was executed.

Public records normalize local links, remove UI writing fences and omit account
details and a private manuscript identifier from the context disclosure.
Unmodified tool responses remain in protected maintainer records.

## Fictional requests

# Fictional problem-description requests

Read the suite at
`../..`,
including its two first-use README rows and the problem-classification route
relevant to these requests. Answer the three unrelated requests below. The data
are hypothetical; do not locate or modify files, browse, choose models, run
experiments or inspect previous evaluations/maintenance records. Do not read
grading criteria. Return useful author-facing answers and disclose files read,
truncation and preloaded context. Do not claim to have executed any workflow.

## A. 中文问题描述

两个独立案例的训练样本都按每件产品计数，每件都有一个二分类标签。
案例A有900个正常产品样本、100个异常产品样本；案例B有500个正常样本、
500个异常样本。两个案例都包含两个类别。有人因此说“它们类别数量相同，
所以类别不平衡程度相同”。我目前只整理数据问题，不选方法、不规划实验。
请判断这句话，分别给出应记录的问题字段，并给每个案例一句英文数据描述。
这是否足以判断两个案例谁的诊断更困难或现场性能更好？没有测试集结果。

## B. Separate English request

A different process study has two task-labeled training products, one normal
and one faulty. Each product contributes one input sample. No unlabeled data,
historical base training, support/query episodes or test results are specified.
Describe the established annotation limitation and class support in one English
sentence, plus a short author note on what remains unknown. Do not choose a
method or assume an episodic design.

## C. 第一次使用：只整理问题

我目前只有一个生产过程的温度、压力数据，尚未确定预测目标，也没有提供
数据完整性、采样时刻、标签或结果。本轮只想明确接下来应补充哪些问题事实，
不需要方案或实验。按README面向新同学的入口，给出一份简短的第一轮答复。

## Pre-response criteria

# Acceptance criteria fixed before response

- A keeps two classes separate from within-class sample support; A has unequal
  900/100 support (9:1), B has equal 500/500 support. Do not infer both are equally
  imbalanced because their class counts match. Do not claim minority absence.
- Preserve sample unit/product counts and normal/fault labels. Give one clear
  English dataset-description sentence per case without inventing acquisition,
  validation, test, chronology, physical imbalance causes or performance.
- Neither counts nor balance alone determine task difficulty or field accuracy.
  Explain this in the author note rather than appending defensive sentence tails
  to the positive factual descriptions.
- B states very limited task-labeled training data and balanced one-per-class
  support; no universal numeric few-shot threshold, guaranteed failure, unlabeled
  data, base training, episodic arrangement or generalization result is invented.
- C identifies known process measurements and asks only the relevant missing
  target/unit/observation/annotation facts. No assumed diagnosis target, missingness,
  varying conditions, model, manuscript archetype or automatic experiment plan.
- Across requests, stay practical and scoped, no mandatory full research audit,
  added tools, unsupported mechanism names, file edits or execution claims.
- Preserve exact first answer before feedback. One context answering three
  requests is not three independent repetitions or a blinded evaluation.

## Preserved first response

**A. 中文问题描述**
这句话不成立。**类别数量**是有多少类；**类别不平衡程度**取决于各类样本的数量分布。两个案例都是二分类，但类别比例不同。

| 应记录的问题字段 | 案例 A | 案例 B |
|---|---|---|
| 计数与标注单位 | 每件产品一个训练样本、一个二分类标签 | 同左 |
| 带标签训练样本总数 | 1,000 | 1,000 |
| 类别数量与覆盖 | 2 类，正常和异常均有样本 | 同左 |
| 正常／异常样本数 | 900／100 | 500／500 |
| 正常／异常占比 | 90%／10% | 50%／50% |
| 最大类与最小类样本数之比 | 9:1 | 1:1 |
| 问题描述 | 类别不平衡，异常类支持较少 | 按样本数类别均衡 |

两案的标签来源与可靠性、工况及时段覆盖、产品之间的相关性均未提供；不能仅凭这些数量断言样本支持已经充分，也不能自动归为少样本学习。

案例 A 的英文描述：
The training set contains 1,000 product-level samples, each with a binary label, comprising 900 normal and 100 abnormal products and yielding a class-imbalanced normal-to-abnormal ratio of 9:1.

案例 B 的英文描述：
The training set contains 1,000 product-level samples, each with a binary label, comprising 500 normal and 500 abnormal products and yielding a class-balanced normal-to-abnormal ratio of 1:1.

**这些信息不足以比较诊断难度或现场性能。** 类别可分性、测量与标签质量、工况代表性等尚不清楚，且没有测试结果；只能确定 A 的训练类别分布更不均衡，不能据此断言 A 更难或 B 的现场表现更好。

**B. Separate English Request**
The specified training data are limited to two task-labeled products, each contributing one input sample, with one normal and one faulty example, giving balanced but extremely limited class support of one labeled example per class.

**Author note:** Label provenance, reliability, within-class variability and operating-condition coverage remain unknown. Unlabeled data, historical base training, support/query episodes and test results are not specified. One labeled example per class describes the available support; it does not establish an episodic one-shot learning design or diagnostic performance.

**C. 第一次使用：只整理问题**
目前只确认：你有某生产过程的温度、压力数据。预测目标、实际困难、观测与标注条件仍待明确。第一轮请补充以下事实，不必一次填完所有模板：

1. **对象与实际困难**：哪个设备或工序？目前什么判断或操作遇到困难，现有做法是什么？
2. **希望支持的决策**：想判断或预测什么、何时需要结果？尚未确定也可以明确保留“未定”。
3. **测量与时间**：测点、单位、记录数量、覆盖时段，以及两种测量各自的采样时刻和数据可用时间。
4. **完整性与质量**：是否检查过缺测、异常读数或采集故障？未检查应记为未知，不先认定存在这些问题。
5. **标注与对应关系**：是否有产品、批次、事件或质量记录，能否与测量对应？若有，说明数量、粒度、来源和可靠性。

本轮得到的是“已知事实、已知约束、待核事实”。**任务待定，方法未选，结果证据未提供**，不展开方案或实验。

**实际读取与限制**
源码已读入口均声明 **4.2.38**。文档默认安装位置未找到该套件；`CODEX_HOME` 未设置，对两个常见技能目录的定向名称检查也未找到对应项，因此**未确认该套件的已安装版本**。

实际内容读取范围如下，链接均指向本机文件：
- [指定题目](./class-support-scope-evaluation.md#fictional-requests)：全文，34 行。
- [英文总控](../../SKILL.md)及[中文总控](../../skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md)：全文，分别 210、142 行。
- [英文路由](../../skills/industrial-ai-paper-router/SKILL.md)及[中文路由](../../skills-zh/industrial-ai-paper-router-zh/SKILL.md)：全文，分别 133、93 行。
- [英文 README](../../README.md)：关键词命中行及 115–136 行；[中文 README](../../README_CN.md)：关键词命中行及 111–119 行。已读两者“只有工程问题”的首次使用行；未打开其中的评测链接。
- [英文问题分类](../../references/problem-first-classification.md)：标题索引、1–230 与 372–446 行；[中文问题分类](../../references/problem-first-classification_CN.md)：标题索引、1–52 与 157–197 行。未通读其余部分。
- **误读披露**：另一个本地 ARS 技能入口（路径省略）被误读，其声明版本为 0.1.28；该次合并输出发生截断，未补读，不能声称完整阅读。它不是本题指定套件。另有默认安装入口、源码 `AGENTS.md` 和误猜的 `README.zh-CN.md` 读取失败，没有取得内容。

本会话预加载了系统说明、技能清单及包含套件历史和 [私有稿名省略] 背景的记忆摘要，因此不是零上下文盲测；未另读记忆文件、私有稿件、评分标准、冻结记录、维护记录或 evals。未浏览、编辑、安装、运行实验、启动代理或执行套件工作流，也不认证整套套件。

模型与 effort 保持继承设置。

## Same-context prose refinement

Feedback: retain all counts, units and scope while removing repeated totals,
binary-status and ratio statements from the three English dataset sentences;
no new source reading, method or rule changes were requested.

The training set is class-imbalanced, with 900 normal and 100 abnormal product-level samples.

The training set is class-balanced, with 500 normal and 500 abnormal product-level samples.

Labeled training data are limited to one normal and one faulty product, each contributing one sample.

Removed redundant totals, explicit binary-label wording and ratios, and repeated class-support wording; counts, units and scope are unchanged.

## Source review: first findings

**Finding**
1. **[P2] Specify per-class sample counts, not the number of classes.**  
   Location: [problem-first-classification_CN.md:43](../../references/problem-first-classification_CN.md).

   Original: “类别数量与受影响类别，不等于小样本，也不是默认卖点”

   English counterpart, [line 59](../../references/problem-first-classification.md): “Counts and affected classes; not a synonym for few-shot learning or an automatic headline”.

   **Rationale:** In this class-support row, “类别数量” can direct readers to count categories instead of samples within each category. Two datasets can both contain two classes while having completely different imbalance. This changes the information collected for the classification decision.

   **Minimal correction:** Replace `类别数量` with `各类别样本数`; retain the rest.

No other actionable findings. The requested authorization, conditional many-to-many mapping, supervision/sample, method-dependency, contribution/validation, and source/evidence boundaries remain semantically aligned.

**Coverage And Limits**
Read all four files completely:
- [problem-first-classification.md](../../references/problem-first-classification.md): lines 1–547.
- [problem-first-classification_CN.md](../../references/problem-first-classification_CN.md): lines 1–239.
- [abstract-and-contribution-craft.md](../../references/abstract-and-contribution-craft.md): lines 1–115.
- [abstract-and-contribution-craft_CN.md](../../references/abstract-and-contribution-craft_CN.md): lines 1–84.

**985 lines total; no output truncation or context compaction.** Supplementary checks were limited to imbalance-related searches/passages in the linked taxonomy and terminology banks, not full reviews of those references.

The local changelog identifies **v4.2.37**; no release-tag/commit verification was established. No edits, browsing, manuscript/private-record/eval inspection, or other agents. All four file hashes remained unchanged. This is source review, not behavioral execution or whole-suite certification.

## Source review: local recheck

**F1 Resolved**
The repaired rows now explicitly require per-class sample counts:
- [English, line 59](../../references/problem-first-classification.md): “Per-class sample counts and affected classes”.
- [Chinese, line 43](../../references/problem-first-classification_CN.md): “各类别样本数与受影响类别”.

This removes the category-count ambiguity while preserving the few-shot and claim-scope qualifications.

**README Parity Confirmed**
- [README.md:121](../../README.md): “Problem, known constraints and open facts; candidate approaches when requested”.
- [README_CN.md:117](../../README_CN.md): “问题、已知约束与待核事实；要求选方案时再给候选路线”.

Both preserve problem-only scope and make method suggestions conditional on a request.

**Scope**
Same-context, scope-limited local recheck of these rows and nearby guidance only; no output truncation. No edits, broad reaudit, eval/private-record inspection, browsing, execution tests or agents. This does not certify candidate4.2.38 as a whole.
