# Engineering Application Journal Writing Skill

[English](README.md) | [中文总控](skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md) | [摘要与贡献](skills-zh/engineering-abstract-contributions-zh/SKILL.md) | [术语决策](references/terminology-decisions_CN.md) | [评估说明](evals/README.md)

**面向工业智能的证据驱动科研与写作工具集。** 将工程问题、实际方法和已有结果组织成逻辑连贯的期刊论文。支持单段润色，也支持选题、实验、图表、全文审查及交接。

**4.1.67：14 对中英文 Skill。** 重点面向流程工业中的智能模型研究；其他工程应用按任务和证据边界使用，不套统一论文模板。

本版补充部分方法名称的定义和译名证据。实际测试范围与未完成核查见[评估记录](evals/README.md)；术语库不是已经全面验证的白名单。

[当前评估记录](evals/README.md#current-version-status)列明实际测试版本、案例、修复过程和边界，独立写作响应与程序检查分别报告，不替所有论文或全部指令背书；具体修订见[版本记录](CHANGELOG.md)。

## 核心能力

- **摘要连通方法。** 先读输入输出、公式和图，再说明模块为何相接；贡献不重复模块清单。
- **术语按场景选择。** 区分变量、特征、样本、工况和状态，不把另一领域的合法用词全部列为禁词。
- **问题与方法分层。** 多速率是观测挑战，Transformer 是方法；图、模糊和大模型不成为默认故事。
- **实验可追踪。** 明确输入语义、数据隔离、模型选择、重复运行及图表来源。
- **尊重已确认稿件。** 讨论模式不修改文件；语言润色不改结果、公式、表格字号和认可的图。

本套件不保证接收，不补造证据，也不以语言质量替代科学判断。交付的是工作指引、参考、模板和本地检查工具，不是通用训练平台，也不替代领域专家。

## 从当前问题开始

| 当前需求 | 入口 |
|---|---|
| 摘要模块没有承接，贡献像罗列模块 | [摘要与贡献](skills-zh/engineering-abstract-contributions-zh/SKILL.md) |
| 有模型想法，尚不清楚工程问题 | [选题与贡献校准](skills-zh/engineering-research-ideation-zh/SKILL.md) |
| 规划章节及验证贡献的实验 | [论文架构](skills-zh/engineering-paper-idea-architecture-zh/SKILL.md) |
| 不确定 state、condition、attribute、variable-wise | [术语决策](references/terminology-decisions_CN.md) |
| 核对图表和论述，不改实验数值 | [实验证据设计](skills-zh/engineering-experiment-evidence-design-zh/SKILL.md) |
| 已授权跑实验，需要保存可复现记录 | [实验自动化](skills-zh/engineering-experiment-automation-zh/SKILL.md) |
| 接近投稿，只检查原则性问题 | [严谨性审稿](skills-zh/engineering-journal-rigor-review-zh/SKILL.md) |

示例请求：

> 使用 $engineering-abstract-contributions-zh。先读当前源码、PDF、方法公式和框架图，保留已确认开头，澄清模块承接，不新增能力。给出摘要建议，以及确实需要同步的正文原句、位置、改句和理由。本轮不要更新 LaTeX 或 Overleaf。

中文交流不要求论文改成中文。需要英文交互时使用对应不带 `-zh` 的 Skill。

## 安装

### 方式一：让 Codex 从链接安装

在 Codex 中发送下面这段请求即可。安装的是**完整套件**，不是单个 Markdown 文件：

> 请使用 $skill-installer，从 https://github.com/MagicTK/engineering-application-journal-writing-skill 安装整个仓库根目录，路径为 `.`，安装名为 `engineering-application-journal-writing-skill`。保留 `skills`、`skills-zh`、`references`、`assets` 和 `scripts` 等完整目录，不要把单个伴随 Skill 单独复制出去。已有安装时先报告版本和位置，不覆盖我的本地修改。安装后运行套件检查，告诉我如何调用中文总控。

无需 GitHub 插件、API 密钥或向仓库上传论文。下载需要网络；本机的安装权限由 Codex 正常申请。若使用环境没有 `$skill-installer`，采用下面的本地方式。

### 方式二：下载后安装

在 [GitHub 仓库](https://github.com/MagicTK/engineering-application-journal-writing-skill) 选择 **Code → Download ZIP** 并解压，或克隆完整仓库：

```bash
git clone https://github.com/MagicTK/engineering-application-journal-writing-skill.git
cd engineering-application-journal-writing-skill
```

在仓库根目录运行：

```bash
python3 scripts/install_suite.py --dry-run
python3 scripts/install_suite.py --copy
```

检查工具和安装器使用 Python 3.9+ 标准库，无第三方依赖。默认安装到 `$CODEX_HOME/skills/engineering-application-journal-writing-skill`，未设置时使用 `~/.codex/skills/engineering-application-journal-writing-skill`。`--target FINAL_DIRECTORY` 指定最终目录；不会覆盖已有目标。省略 `--copy` 则建立符号链接。

保留完整目录，因为伴随 Skill 使用共享参考的相对路径。支持嵌套发现的客户端可直接展示各 Skill；仅识别根入口的客户端由总控读取伴随文件。具体客户端能否发现需实际验证。其他助手可读取 Markdown，无需 Codex 界面元数据。浏览器、PDF 工具、LaTeX 编译器和训练后端由使用环境提供。

### 确认安装成功

在安装后的下一轮对话中，让 Codex 读取本地根 `SKILL.md`，确认版本与实际下载的来源一致，再运行 `scripts/validate_suite.py`；本套件包含 14 对中英文入口。开发候选与 GitHub 当前发布版本可能不同，应记录实际下载的版本或提交，不把差异误判为安装失败。若技能选择器没有显示中文入口，可直接要求读取套件内 `skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md`，不必重复安装。客户端未刷新时再重启客户端。

更新前记录旧版本并备份自己的改动；下载新版后先验证，再明确替换旧套件。安装器遇到已有目录会停止，不自动删除或覆盖。卸载时只移除对应安装目录或符号链接，不删除论文项目；不确定位置时先让 Codex 列出路径。

## 组内同学第一次使用

先给当前问题、目标期刊（如已确定）、已有材料和允许的操作范围，不必一次填完所有模板。没有结果时可以讨论设计，但不能生成看似真实的结果。

| 起点 | 建议提供 | 第一轮应得到 |
|---|---|---|
| 只有工程问题 | 对象、测量、实际困难、已有方法 | 问题与方法分离后的候选路线和待查证据 |
| 已有方法，摘要写不顺 | 当前摘要、方法公式和框架图 | 准确的模块承接、保留句与最小改句 |
| 准备实验 | 主张、数据单位、划分方式、可用资源 | 可执行实验计划和缺失信息，不是编造结果 |
| 已有实验结果 | 表格、图、运行记录及当前论述 | 数值一致性、证据边界与学生核实清单 |
| 准备投稿 | 最新源文件、PDF、参考文献、保护项 | 原则性问题、必要修改与可选润色分开 |

可直接使用的请求：

> 使用 $engineering-terminology-polishing-zh。只检查我提供段落中的工程术语和句间逻辑。列出原句、建议句、原因和是否必须修改；不改方法、结果或文件。不确定的术语给出上下文和文献依据，不建立一刀切禁词表。

> 使用 $engineering-experiment-evidence-design-zh。根据现有方法和结果核查实验主张。把已确认的算术错误、需要原始运行记录核实的问题、可选补充实验分开。不要改表格数值，不启动训练。

> 使用 $engineering-application-journal-writing-skill-zh。先读我的当前稿件，只处理引言到方法总览的逻辑。保留已确认段落，给出准确位置和最小修改建议；导师确认后再改源文件。

导师与学生分别保留“待确认”“已确认”“已实施”“已验证”的状态。一次润色通过不代表数据、实现或论文接收已获确认。模型服务的数据政策仍需团队自行核实，不能因为 Skill 安装在本机就认为文稿不会离开本机。

## 14 对技能

| 入口 | 职责 |
|---|---|
| [工程应用写作总控](skills-zh/engineering-application-journal-writing-skill-zh/SKILL.md) | 范围、路由、保护约束与交接 |
| [工业智能论文路由](skills-zh/industrial-ai-paper-router-zh/SKILL.md) | 挑战、方法、任务、尺度、证据五维分类 |
| [研究选题](skills-zh/engineering-research-ideation-zh/SKILL.md) | 候选问题、实际增量与贡献校准 |
| [文献定位](skills-zh/engineering-literature-positioning-zh/SKILL.md) | 文献证据、缺口与引用职责 |
| [论文架构](skills-zh/engineering-paper-idea-architecture-zh/SKILL.md) | 问题、设计与证据组织 |
| [摘要与贡献](skills-zh/engineering-abstract-contributions-zh/SKILL.md) | 模块关联、贡献表达与最小正文同步 |
| [基准与真实案例](skills-zh/general-method-benchmark-realworld-zh/SKILL.md) | 通用方法的不同验证职责 |
| [工业背景驱动](skills-zh/background-driven-industrial-application-zh/SKILL.md) | 从过程、测量和瓶颈推出研究要求 |
| [实验证据设计](skills-zh/engineering-experiment-evidence-design-zh/SKILL.md) | 比较、消融、统计、结果一致性 |
| [实验自动化](skills-zh/engineering-experiment-automation-zh/SKILL.md) | 授权运行、模型选择与来源记录 |
| [图表与 LaTeX](skills-zh/engineering-figure-latex-production-zh/SKILL.md) | 科学图、可编辑输出和版面核验 |
| [术语与润色](skills-zh/engineering-terminology-polishing-zh/SKILL.md) | 精确用词、段落与句间逻辑 |
| [严谨性审稿](skills-zh/engineering-journal-rigor-review-zh/SKILL.md) | 有证据的发现与未决核查 |
| [审稿回复](skills-zh/engineering-review-response-zh/SKILL.md) | 意见、修改与证据对应 |

英文入口在 [English README](README.md) 中列出。

## 文件怎样组织

4.1.67 包含 **28 个 Skill 入口 Markdown、26 份专题参考 Markdown、13 份工作模板 Markdown**；英文和中文入口合计为 14 对，不是 28 套不同方法。参考资料按任务加载，不会要求每次把整个库读完。

| 目录 | 内容 |
|---|---|
| `SKILL.md`、`skills/`、`skills-zh/` | 总控与中英文专用入口 |
| `references/` | 章节写作、术语、问题分类、专题、实验证据与绘图说明 |
| `assets/templates/` | 论文信息、贡献证据、数据版本、实验运行、图表及作者交接模板 |
| `scripts/`、`tests/` | 安装、结构检查、只读术语筛查和测试 |
| `evals/` | 合成场景、实际响应、评估范围及版本记录 |

术语库不是关键词堆积：先区分对象与任务，再区分适用语境、科学含义和作者偏好。论文专属词表仍留在论文项目，不混入通用库。

通用机制名称按[至少两篇独立论文语境及中文单独核查](references/engineering-application-terminology-bank_CN.md#零专业名称准入与译名核查)准入；单篇模块保留来源归属，普通功能描述不自动升级为通用类别。当前核心证据表是部分核验，不宣称整个词库全部通过。

## 通用核心与条件专题

[五维分类](references/industrial-ai-taxonomy.md)分开工程挑战、方法家族、任务、对象尺度与证据类型。[专题规则](references/topic-playbooks.md)按需加载：多速率/不规则观测、有限监督、非平稳、多源、全流程、图与知识及模糊、生成模型、大模型、效率、定位、专家路由、复合故障、时序表示、控制决策。

不是每篇都必须有两组数据、三个贡献、200 词摘要、混淆矩阵或全部消融。以实际主张所需证据为准。投稿规则核查当前官方说明；已发表论文提供参考，不构成强制格式。

## 常用资料与工具

- [摘要贡献写法](references/abstract-and-contribution-craft_CN.md)、[正文同步模板](assets/templates/abstract-body-sync.md)。
- [章节指南](references/section-writing-guide.md)、[论证与行文](references/argument-and-prose-craft.md)、[贡献论证路径](references/contribution-narratives.md)。
- [术语决策](references/terminology-decisions_CN.md)、[通用术语库](references/engineering-application-terminology-bank_CN.md)、[已发表文献证据](references/published-evidence.md)。
- [实验执行](references/experiment-execution_CN.md)、[运行清单](assets/templates/experiment-run-manifest.md)、[实验证据](references/experiment-evidence-design.md)。
- [图表规范](references/figure-and-latex-production.md)、[转刊完整性](references/journal-migration-and-completeness_CN.md)、[作者交接](assets/templates/author-handoff.md)。

只读术语筛查：

```bash
python3 scripts/audit_terminology.py manuscript.tex --min-count 3
```

工具排除百分号注释、字面 `iftrue`/`iffalse` 的非活动分支、comment 环境、常见引用键/交叉引用键、网址目标及字面 `thebibliography` 环境；保留源行号和超链接显示正文，输出待审候选和高频搭配。普通段落内的源文件换行可连接成同一搭配，`line` 与 `end_line` 标出起止行；空段、字面 `\par`、排除的元数据及条件/comment环境指令行保守地隔开搭配。识别字面百分号注释对换行的抑制，不一律把换行当空格。不展开任意 TeX 宏、不读取包含文件、不自动判错、不改原文。自定义/嵌套语法、verbatim及类别码变化仍需人工核查，最终对照活动正文和 PDF。

## 证据、隐私与来源

公开内容仅含通用指引、原创整理、书目链接和合成测试情境；不含文献 PDF、论文原文、工业数据、私有项目日志或模型权重。单篇论文的术语表和实验记录留在论文目录。

参见[文献索引](references/published-evidence.md)、[设计参考](references/design-sources.md)、[贡献说明](CONTRIBUTING.md)及[隐私安全](SECURITY.md)。参考项目的 star 数不证明质量，也不是本项目的传播承诺。第三方许可与本项目许可分开处理。

## 验证

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

结构测试检查包装与约束，不等于科学验证。[行为评估记录](evals/forward-test-report.json)单独说明版本、范围和实际测试状态；历史测试不验证新版本，自评不冒充独立测试。详见[评估流程](evals/README.md)与[更新记录](CHANGELOG.md)。

维护者可运行 `python3 scripts/export_public.py NEW_DIRECTORY --draft` 生成干净的本地候选包。不加 `--draft` 时还要求许可和独立行为测试完成。工具不上传文件，也不包含上级仓库的历史。

## 许可

采用 [MIT 许可证](LICENSE)，版权署名 2026 MagicTK。允许使用、修改及再分发本项目原创 Skill 内容，包括商业用途；需保留版权及许可声明。参考文献和外部项目仍适用其各自的权利与许可，不因被本项目引用而改为 MIT，也不随本项目分发。
