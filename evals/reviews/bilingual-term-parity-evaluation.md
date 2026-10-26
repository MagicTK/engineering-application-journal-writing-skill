# Chinese Terminology Meaning Preservation

Primary report: [current forward report](../forward-test-report.json).

## Scope And Repairs

A separate source reviewer compared the complete English/Chinese terminology
bank and decision guides on 4.2.39: 608, 348, 853 and 379 lines respectively
(2,188 total), in bounded untruncated reads. Two Chinese phrases changed the
English meaning: a conditional statement about additive attention bias became
an absolute denial of hard constraints, and ordinary prediction measurements
became normal-condition measurements in the domain-generalization record.

The maintainer checked the exact four rows and corrected only the two Chinese
phrases. The original reviewer reread those four rows in the same context and
confirmed the repairs. That follow-up is not a second independent full review.
No new generic name, translation admission or source ID is introduced; English
definitions and all paper-specific results are unchanged. The review checked
existing records, not every cited paper or Chinese authority page. Its supplied
version and task context were not an independent publication audit.

## Procedure And Findings

One new responding context used the frozen 4.2.40 source for the two fictional
requests below, without private criteria, previous responses or corrective
feedback. The complete first answer was retained. The maintainer judged both
answers against criteria saved before dispatch; no baseline behavior failure,
controlled gain, independent second grader or full-suite certification is claimed.

- Case A preserves the distinction between a finite preference and exact
  masking under the stated softmax assumptions. It correctly keeps process
  relation information separate from physical causal identification.
- Case B preserves fixed-model prediction on healthy and known-fault inputs.
  Reading a test sample is not target-data fitting, and an unseen plant need
  not introduce an unseen fault class.
- Both Methods passages preserve their stated interfaces without inventing
  results or module names. The two-sentence attention passage is detailed;
  this is not a claim of uniquely optimal prose or an abstract-length model.
- An independent 50-digit decimal check of an illustrative zero-score row
  gives approximately (0.786986, 0.106507, 0.106507) for biases (0, -2, -2);
  replacing the last two with negative infinity gives (1, 0, 0). This is a
  mathematical check, not a floating-point implementation or empirical result.

The respondent disclosed preloaded memory-summary/workspace context without
memory search. A keyword output was truncated, then relevant passages were
reread completely; unrelated hits were not claimed as read. Actual reading
and action limits are retained below. Source-root use does not test installed
client discovery. Public copies normalize local paths and writing wrappers;
exact records remain private. Historical cases keep their original snapshots.

## Actual Request

Use the suite at <suite root>, current version 4.2.40.
Read the Chinese terminology-polishing entry and its relevant terminology
references. Do not inspect evaluation/history or private maintenance records,
use memory search, browse, edit files, run research experiments or spawn agents.
Answer the following two fictional requests. For each, give a concise Chinese
judgment, two connected English Methods sentences and at most two short Chinese
author notes. Preserve the supplied facts; do not add results or a named module.
Disclose the actual files/sections read, truncation recovery and any inherited
context. These are standalone writing requests, not a whole-paper review.

A. A process-variable attention layer uses row-wise softmax over finite scores.
Design A adds finite penalties (0 on allowed pairs and -2 on discouraged pairs)
to the scores. Design B instead adds 0 on allowed pairs and negative infinity
on excluded pairs; each row retains at least one finite score. May the two
designs both be described as "soft process constraints" because the terms are
additive? Describe how each acts on aggregation. A source of process relations
is supplied, but there is no physical intervention or root-cause study.

B. A diagnostic model is trained and selected using source plants only. At a
previously unseen plant it uses each current measurement sample for prediction;
all learned parameters and source-derived preprocessing statistics remain fixed.
Test samples include healthy operation and fault classes already represented
in source training. Their labels are available only to the external evaluator.
The author wonders whether domain generalization permits only healthy target
samples, or whether reading a fault sample already counts as target adaptation.
Explain the setting and write its Methods description. The study has no new
class-discovery component and no measured result is supplied.

## First Answer

**A. 加性偏置与硬掩码**
不能仅因采用加法就都称为“软过程约束”。设计 A 的有限惩罚调整相对权重，所有配对仍参与聚合；设计 B 将被排除配对的权重精确置零，是该聚合操作中的硬约束，并在允许配对之间归一化。

Using the supplied process relations, Design A adds 0 to finite attention scores for allowed variable pairs and −2 for discouraged pairs before row-wise softmax, favoring allowed pairs in relative weighting while retaining a positive aggregation weight for every pair. By contrast, Design B adds 0 for allowed pairs and −∞ for excluded pairs, with at least one finite score retained in each row, so that row-wise softmax assigns zero weight to excluded pairs and normalizes the remaining weights over allowed pairs.

作者说明：
- 有限惩罚不保证被抑制配对的最终权重低于所有允许配对。
- 工艺关系来源可支持上述计算依据，但不能据此宣称识别了物理因果效应或故障根因。

**B. 未见工厂预测**
这是仅用源工厂训练、选模，在未见工厂预测的域泛化设置。目标测试样本不必仅为健康样本；固定模型读取故障样本进行预测，不等于利用目标数据进行适应。外部评价者持有标签，也不等于模型可访问标签。

The diagnostic model was trained and selected using source-plant data only and was applied to each current measurement sample from a previously unseen plant with all learned parameters and source-derived preprocessing statistics kept fixed. In this domain generalization setting, the test samples included healthy operation and fault classes already represented in source training, and their labels were available only to the external evaluator.

作者说明：
- 未见的是工厂，不是这些故障类别；不应改写为新类别发现或类别级零样本诊断。
- 该设置说明评价条件，本身不能证明泛化性能或性能提升。

**读取与边界**
已确认套件版本为 **4.2.40**。实际读取范围如下：
- suite-manifest.yaml：版本及入口映射。
- 中文术语润色入口：全文。
- 中文术语库：使用边界、名称准入、第六至七节、第九节导言及“任务目标与观测安排”“数据使用与学习阶段”，另读 DG 中文译名记录。
- 中文场景决策：决策顺序、数据对象、状态／工况／模式、变量及其特征、结构与操作。
- Terminology And Style：第 4 节；三个参考文件还做了标题及关键词定位。

一次关键词输出发生截断，随后分段重读上述相关条目，重读输出完整；未恢复无关命中，也未将参考文件宣称为全文通读。文献编号及译名依据仅按本地记录阅读，未核验原论文。

会话预载了项目记忆摘要和工作区规则，但未使用摘要中的历史事实作判断，也未搜索记忆。除只读额度检查和上述本地读取外，未查看评测、历史或私有维护记录，未联网、编辑、运行实验或派生代理；两题均仅按题设作独立写作处理。
