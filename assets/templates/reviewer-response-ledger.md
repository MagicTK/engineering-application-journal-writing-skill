# Reviewer Response Ledger / 审稿回复台账

Working template. Preserve every original comment. Draft text, proposed experiments, and unverified edit locations are not completed revisions.

## Revision Identity / 修订身份

| Field / 字段 | Value / 值 |
|---|---|
| Manuscript/version/hash / 稿件版本及哈希 | |
| Review source and received date / 审稿来源及接收时间 | |
| Target journal and verified instructions / 目标期刊与已核验要求 | |
| Revision scope and existing authorization / 修订范围及已有授权 | |
| Authoritative source and rendered PDF / 权威源文件及PDF | |
| Research work state and claim ledger / 协作状态及主张矩阵 | |
| Response draft version/hash / 回复稿版本及哈希 | |

If the journal or formatting rules are unavailable, keep the draft generic and label the unresolved field. Do not invent editor requirements.

## Coverage Map / 意见覆盖表

Preserve reviewer IDs and comment order. Split a compound comment into child IDs (for example, `R2-C3a`) linked to its original comment.

| Comment ID | Original comment / 原始意见 | Type / 类型 | Affected claim/artifact / 涉及主张或文件 | Disposition / 处理选择 | Owner / 负责人 | State / 状态 | Detail record / 详单 |
|---|---|---|---|---|---|---|---|
| R1-C1 | | correction / evidence / scientific-choice / explanation | | agree / partial-agreement / reasoned-disagreement / pending-decision | | open | |

Revision states: `open`, `planned`, `in-progress`, `changed-unverified`, `verified`, `partial`, `deferred`, `unresolved`. Disagreement and accepted limitation are dispositions, not proof that a comment was resolved. A reasoned-disagreement response can be verified for accuracy without asserting reviewer agreement.

## Per-Comment Record / 逐条记录

### R1-C1

- **Original comment / 原始意见:**
- **Underlying scientific request / 科学诉求:**
- **Affected claims and evidence / 相关主张与证据:**
- **Disposition and reason / 处理选择与理由:**
- **Action already completed / 已完成动作:**
- **Action still proposed or pending / 尚拟议或待完成动作:**
- **Revised wording or concise diff / 修订原文或差异:**
- **Source location / 源文件位置:** file + section/label + line when verified
- **Rendered location / PDF位置:** page + line or section/table/figure + PDF version/hash; never guess line numbers
- **Evidence / 证据:** evidence IDs + run/split IDs + result paths/hashes + calculation/verification record
- **Verification performed / 已做验证:**
- **Verifier and snapshot / 核验者及版本:**
- **Remaining issue, owner, and recovery / 剩余项、负责人及恢复条件:**
- **Draft response / 回复草稿:**

## Response Shape / 回复结构

Address the scientific point directly. State the actual change, its evidence or rationale, and the verified manuscript location. Keep courtesy brief and specific. Do not repeat a formulaic thanks paragraph before every comment.

**Completed correction / 已完成修改**

> We corrected [specific definition/value] in [verified location]. The revised text now states [actual wording or precise summary]. [Evidence or consequence when needed.]

**New result, only after verification / 补充结果，核验后才使用**

> We evaluated [actual condition and comparison] using [actual split/setting]. [Verified result and its implication.] The experiment and result are reported in [verified location].

**Reasoned disagreement / 有据的合理不同意**

> [Requested change] would change [the scientific target or information available] in this study. [Specific rationale/evidence.] We [actual clarification or supported alternative, if made] in [verified location].

**Work pending in an internal draft / 内部稿的未完成项**

> [PENDING: action, owner, required evidence, and affected location.] Current evidence supports [bounded claim].

These are functional examples with placeholders, not prose to paste unfilled. A source's unreported evaluation does not establish that its method cannot work. An offline case does not establish deployment. A plausible rationale cannot stand in for a requested empirical result.

## Closure Checks / 关闭检查

- [ ] Every original comment and child item is represented.
- [ ] “We added/revised/evaluated” claims match actual files and verified results.
- [ ] Changed values agree in the response, tables, plots, abstract, and conclusion.
- [ ] Locations point to the latest source/PDF; unresolved locators remain marked.
- [ ] Added evidence supports the stated scope; null or adverse results are represented fairly.
- [ ] Disagreements address the request with reasons; no attack on reviewer competence or prior work.
- [ ] Each partial, deferred, or unresolved item has an owner and exact next requirement.
- [ ] Revised source builds and affected pages are inspected when compilation is in scope and available.
- [ ] The local delivery separates finished response text from internal pending notes.

Record checked items only after performing them. If a check is unavailable or outside scope, state that explicitly. Stop at local author handoff; sending, uploading, or submitting requires the user's applicable authorization.
