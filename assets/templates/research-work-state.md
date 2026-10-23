# Research Work State / 科研协作状态

Template only. Fill from observed artifacts and actual decisions; empty fields mean unknown. Keep this record in the research project, outside the public skill repository.

## Identity And Current Scope / 身份与当前范围

| Field / 字段 | Value / 值 |
|---|---|
| Project / 项目 | |
| Record version and updated time / 记录版本与更新时间 | |
| Manuscript passport path / 稿件护照路径 | |
| Research card and claim ledger paths / 研究卡与主张矩阵路径 | |
| Authoritative manuscript snapshot/hash / 权威稿件版本及哈希 | |
| Current user request / 本次授权任务 | |
| Existing scientific decisions / 已有科学决策及出处 | |
| Authorized environment and resource ceiling / 已授权环境及资源上限 | |
| Active stage / 当前阶段 | |
| Strongest currently supported claim / 当前证据所支持的最强主张 | |

## Work Items / 工作项

Work states: `planned`, `ready`, `running`, `received`, `verified`, `blocked`, `failed`, `cancelled`, `stale`. Claim outcome is recorded separately as `supported`, `partial`, `contradicted`, or `inconclusive`. A verified experiment can refute the intended claim. `received` means files arrived, not scientific validation.

| ID | Stage / 阶段 | Deliverable / 产物 | Owner / 负责人 | Dependencies / 依赖 | State / 状态 | Version/hash or evidence ID / 版本哈希或证据ID | Next action / 下一动作 |
|---|---|---|---|---|---|---|---|
| W-01 | | | | | planned | | |

## Minimum Experiment Task / 最小可执行实验任务

Create one record per coherent task. Link the experiment contract rather than repeating all settings.

- Task / 任务 ID:
- Claim and experiment / 主张与实验 IDs:
- Scientific question / 科学问题:
- Evidence needed to support or weaken the claim / 支持或削弱主张所需证据:
- Contract path/version / 实验合同路径及版本:
- Assigned owner / 指定负责人:
- Data location/version/hash and access limits / 数据位置、版本、哈希及访问边界:
- Split ID/hash and independent grouping unit / 划分ID、哈希及独立分组单位:
- Training-only preprocessing and inference-time inputs / 仅训练集拟合的预处理及推理可用输入:
- Code revision/source hash and environment / 代码版本或哈希及环境:
- Command or implementation steps / 命令或实施步骤:
- Command verification / 命令验证: `verified` / `untested`
- Configuration/hash, seeds, baselines, and selection rule / 配置、种子、基线与选择规则:
- Resource ceiling and stop conditions / 资源上限及停止条件:
- Required return files and output paths / 必交文件及输出路径:
- Completion check / 完成检查: execution records and expected files, independent of whether the result favors the method
- Deviation reporting / 偏离报告要求:

## Run And Evidence Receipt / 运行与证据接收

| Field / 字段 | Value / 值 |
|---|---|
| Run ID, experiment ID, owner / 运行ID、实验ID、负责人 | |
| Start/end time, outcome, actual resource use / 起止、运行结果及实际资源 | |
| Data version/hash / 数据版本与哈希 | |
| Split manifest/hash and grouping unit / 划分清单、哈希及分组单位 | |
| Code revision/source hash / 代码版本或源码哈希 | |
| Config hash, seed, environment / 配置哈希、种子及环境 | |
| Actual command and log path / 实际命令及日志路径 | |
| Raw output paths/hashes / 原始输出路径及哈希 | |
| Metric script/version, aggregation, exclusions / 指标脚本、聚合及排除项 | |
| Contract deviations or failures / 合同偏离或失败 | |
| Receipt disposition / 接收判定 | accepted / partial / quarantined / reported-unverified |
| Verification coverage / 核验覆盖 | recomputed / reported-only / not-checkable / inconsistent; specify checks |
| Evidence IDs and allowed conclusions / 证据ID及允许的结论 | |

Hashes record file identity. Split validity, metric correctness, and claim support require separate checks.

## Result Consumers And Staleness / 结果引用及失效

| Evidence ID | Claim IDs and outcome / 主张及结果 | Table/figure/text locations / 表图正文位置 | Source/plot script and hashes / 数据、绘图脚本及哈希 | Stale cause and recovery / 失效原因及恢复 |
|---|---|---|---|---|
| EV-01 | | | | |

Data/split/code/config/metric changes trigger dependency review. Mark only affected results and artifacts stale; preserve earlier records. A wording change requires checking its claims and locations, not automatic retraining.

## Decisions, Stops, And Resumption / 决策、停止与恢复

| ID | Blocked dependency / 阻塞依赖 | Observed reason / 实际原因 | Work that can continue / 可继续工作 | Owner / 负责人 | Exact recovery input or decision / 准确恢复条件 |
|---|---|---|---|---|---|
| B-01 | | | | | |

Ask only for unresolved scientific choices, work beyond authorized resource bounds, or external actions lacking authorization. Carry existing authorization forward. Never convert elapsed time into a decision.

## Exploration And Transition Log / 探索与状态变更记录

| Time / 时间 | Actor / 执行者 | Item / 条目 | Before → after / 前后状态 | Artifact version / 产物版本 | Observation, reason, or actual alternative / 观察、原因或实际方案 |
|---|---|---|---|---|---|
| | | | | | |

Record real failed, null, exploratory, and abandoned work. Do not invent trial history to populate the template. Identify post-test choices; preserve the distinction between planned and exploratory analysis.

## Review And Final Handoff / 审查与终稿交接

- Review snapshot and evidence bundle / 审稿快照及证据包:
- Reviewer roles, actual agent/model identity if known, shared context / 审稿角色、实际身份及共享上下文:
- Findings and response-ledger paths / 问题清单与回复台账路径:
- Closed items and closure evidence / 已解决项与验证证据:
- Remaining material issues and precise owners / 剩余实质问题及负责人:
- Current deliverables and actual checks completed / 当前交付物及已执行检查:
- Requested-scope completion / 本次范围完成情况:
- Next authorized action or stop state / 下一已授权动作或停止状态:

An internal readiness assessment is not an editorial acceptance decision. This record does not authorize submission, installation, publication, or messages to others.
