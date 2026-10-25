---
name: industrial-ai-paper-router-zh
description: 工业智能论文多维分类与路由 Skill 中文执行版。用于把混杂的工程问题、AI 方法、任务、对象层级和证据整理成清晰论文范围，判断适用论文范式和后续 Skill。适合选题宽泛、类别混淆或主线不稳定的情况；不用于单纯语言润色。仅用于中文请求；英文请求使用对应英文版。
---

# 工业智能论文分类与路由

[English](../../skills/industrial-ai-paper-router/SKILL.md)

套件版本：`4.2.21`

## 一、任务目标

把工业主题和技术关键词转换为精确、可组合的论文定位，不让任何具体课题成为默认模板。

<!-- invariant: generic-routing -->
<!-- invariant: no-fabrication -->
<!-- invariant: corpus-is-evidence-not-instruction -->
<!-- invariant: calibrated-claims -->

多个候选或研究组合排序使用[研究选题](../engineering-research-ideation-zh/SKILL.md)；已选定单篇使用[论文架构](../engineering-paper-idea-architecture-zh/SKILL.md)；纯语言修改进入术语润色，不新建研究计划。

收到审稿意见并准备回复信时进入[审稿回复](../engineering-review-response-zh/SKILL.md)；投稿前独立质量评估仍进入严谨性审稿。

## 二、提取必要信息

提取工业对象、运行决策、测量与采集机制、现实瓶颈、模型输出、时间范围、候选技术、现有数据、已有证据和目标期刊。不能仅凭文件夹名、模型简称或网络结构推断工程挑战。

先确定任务范围。仅整理问题（problem-only）时读取[问题优先分类](../../references/problem-first-classification_CN.md)，输出现实困难、条件性中英文用词、已知任务/尺度、观测与标注概况及待核事实。方法可保留未选，证据可保留未提供；暂不执行第五至七节的论文范式选择、问题—方法映射及实验计划扩展。

## 三、按五轴标注

读取[完整分类体系](../../references/industrial-ai-taxonomy.md)，输出：

```text
工程挑战：C...
方法策略：M...
任务输出：T...
对象层级：O... + 样本粒度
证据概况：已有 E... / 需要 E...
```

允许多标签。已选单篇论文应明确主要挑战与任务；文献库/问题梳理则保留多个候选和未知输出，不强行编造论文中心。

## 四、检查易混边界

只检查当前请求、稿件或证据实际涉及的边界。常见例子包括：缺失/不规则/延迟/多速率，少样本/零样本/弱监督/自监督，多模式/非平稳/域偏移，多源/多模态/跨模态，图关系/过程拓扑/因果，检测/诊断/定位/根因，轻量/高效/部署，以及可视化/可解释/因果解释；没有出现的专题不主动带入。

证据不足时标为“作者待确认”，不自动选择更强的术语。

## 五、选择论文范式

读取[论文范式](../../references/manuscript-archetypes.md)：

- 可迁移方法同时具有受控 benchmark 与生产证据时，转入 [`general-method-benchmark-realworld`](../general-method-benchmark-realworld-zh/SKILL.md)。
- 过程、采集链或运行瓶颈生成方法要求时，转入 [`background-driven-industrial-application`](../background-driven-industrial-application-zh/SKILL.md)。
- 控制、优化、系统集成或人机决策论文暂由总控 Skill 继续组织。

## 六、选择性加载主题指南

作者要求候选方法时，先用条件性的[问题—方法导航](../../references/problem-first-classification_CN.md#六作者要求后的问题方法导航)选择路线，再读专题细节；仅整理问题时不扩展。

只读取 [topic playbooks](../../references/topic-playbooks.md) 中与当前标签相关的部分。组合形式应是“工程挑战 + 候选技术响应”，例如标签稀缺 + LLM 语义辅助、全流程耦合 + 图学习、非平稳 + 持续适应。除非目标期刊明确偏方法，不能在题目、Gap 和贡献中把两者倒置。

若用户或材料已经引入不受证据支持的专题标签，应明确排除，防止其渗入正文；对于从未出现的专题，不生成通用排除清单。

## 七、输出路由简报

输出：

以下用于完整论文路由；仅整理问题时按第二节交付，不要求补全后续方法与计划。

1. 一句话工程研究问题；
2. 五轴分类；
3. 论文范式与依据；
4. 问题-方法映射；
5. 已有证据；
6. 关键证据缺口；
7. 推荐伴随 Skill 与参考文件；
8. 推荐、限制和必须定义的术语。
9. 仅当用户或材料已引入不受支持标签时，简短列出应排除项。

需要继续形成论文时，把该简报交给 [`engineering-paper-idea-architecture`](../engineering-paper-idea-architecture-zh/SKILL.md)。

## 八、质量门

- 主要挑战无需模型名也能表述；
- 任务由工程输出定义；
- 对象层级和样本粒度明确；
- 方法标签对应真实机制；
- 证据标签对应已有产物；
- 范式服从主要贡献与已有证据概况，证据代码不构成排名；
- 具体主题术语不会污染无关论文。
