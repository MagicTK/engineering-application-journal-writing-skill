# Figure Revision State / 图稿修订状态

Use one record per figure; a combined deck also needs a figure-to-slide map.
This record tracks cross-tool evidence, not external runtime state JSON.
未执行或未确认的项目保留 pending/untested，不复制示例验收结论。

## Identity and route / 身份与路径

| Field / 字段 | Value / 值 |
|---|---|
| Figure ID / 图号 | |
| Scientific contract / 科学契约 | |
| Paper source version/fingerprint / 论文源版本与指纹 | |
| Data-dependent / 是否依赖实测数据 | yes/no/mixed; identify panels / 混合图逐 panel 标明 |
| Route / 路径 | AstraDraw → editable PPT → human revision → paper; or verified data → reproducible plot → paper |
| Current stage / 当前阶段 | specification/design/reconstruction/human-review/reconciliation/approval/export/integration/compiled-QA |
| Intended paper dimensions / 纸面尺寸 | width, height, single/double column; source of constraint / 约束来源 |
| Protected objects/layout / 受保护对象与排版 | |
| Allowed claim; arrow/color semantics / 允许主张与箭头、颜色语义 | |

## Dependency discovery / 依赖发现

| Skill/runtime / 技能与运行时 | Installed version or fingerprint / 当前版本或指纹 | Consulted guidance / 已读指南 | Available/blocker / 可用性与阻塞 |
|---|---|---|---|
| astra-figure-workflow / AstraDraw | | | |
| image-to-editable-ppt / Image to Editable PPT | | | |
| Plotting/build/export tools / 数据绘图、编译与导出工具 | | | |

Resolve installed paths at execution time; keep shared packages portable. This
record alone does not authorize installation; suite maintenance does not execute
conversion prerequisites. For an authorized conversion, follow the current skill,
user constraints and existing authorization. / 执行时发现安装位置，交付包不写死本机路径；本表本身不授权安装，维护套件不执行转换前置；实际已授权转换按当前技能、用户约束及已有授权处理。

## Version and authority log / 版本与主件日志

| Revision | Role and path / 角色与路径 | Fingerprint | Derived from / 派生自 | Editor/date / 修改者与日期 | Current master? / 当前主件 | Source/map freshness / 源件及映射是否同步 |
|---|---|---|---|---|---|---|
| | candidate/scene/manifest/PPTX/human-PPTX/export/PDF | | | | | current/stale/unavailable |

- Current per-figure master and slide / 当前逐图主件与页号:
- Human review / 人工审阅: pending / edits received / reviewed with no changes; evidence / 依据:
- Human revision scope and protected regions / 人工改动与保护区域:
- Scene/manifest/object-map reconciliation / scene、manifest、对象映射对账:
- Preserved prior version / 保留的历史版本:
- Safe next edit source / 下次编辑使用的源件:

Manual PPT changes do not auto-sync into source JSON or old maps. Preserve the
human-revised PPTX as master until deliberate reconciliation succeeds. Never
overwrite it by rebuilding from stale input. / 人工 PPT 改动不会自动回写 JSON 或旧对象映射；对账完成前以人工修订 PPTX 为主件，不从旧输入重建覆盖。

## Decisions and permissions / 决策与授权

| Decision / 决策 | Exact version/fingerprint and scope / 版本、指纹与范围 | Who/date / 人员与日期 | Actual evidence / 实际依据 | Status / 状态 |
|---|---|---|---|---|
| Design selection/review / 设计选择与审阅 | | | | pending/accepted/rejected/delegated-choice |
| Scientific check / 科学核验 | | | | untested/pass/fail |
| Execution authorization / 执行授权 | | | | scope recorded / 已记录范围 |
| Current revision approval / 当前修订版批准 | | | | pending/approved/rejected |
| Publication/reference rights / 发布与参考素材权限 | | | | unknown/authorized/restricted |

Do not call delegated selection human confirmation. Existing explicit approval
within its version/scope needs no repeated request. One request may authorize
continuous stages; record the scope without inventing review. / 受托选择不写成用户亲自确认；同版本同范围已有明确确认不重复询问；当次可连续授权多阶段，但不能编造审阅。

## Sources and editability / 源件与可编辑边界

| Object/source class / 对象或源件 | Path/object IDs / 路径与对象 ID | Actual format/editability / 实际格式与编辑范围 | Provenance/limitation / 来源与限制 |
|---|---|---|---|
| Raw result data + plotting code / 真实结果与绘图代码 | | | run/split/metric; no generated data / 不生成伪数据 |
| Reference/candidate + prompt / 参考图、候选图与提示词 | | | origin, inspected role, usage rights / 来源、已检查用途与权限 |
| Labels / 文本标签 | | native text or exception / 原生文本或例外 | font evidence; substitutions / 字体依据与替代 |
| Structure/connectors / 结构与连线 | | native shapes/lines/paths or exception / 原生对象或例外 | named selection, useful granularity / 可定位且粒度合理 |
| Formula / 公式 | | Office-native equation / vector / raster | LaTeX source + renderer/font; do not equate vector with native equation / 不把矢量公式当 Office 原生公式 |
| Imagery / 图片资产 | | independent image; internal pixels not object-editable / 独立图片内部不按对象可编 | origin and rights / 来源与权限 |
| PPTX + scene/manifest + map / 可编辑主件与构建源及映射 | | | freshness and per-figure slide map / 同步状态与逐图页号 |

Font/glyph origins require source evidence; PNG appearance is insufficient.
字体和字形来源须有源件依据，不能仅凭 PNG 外观认定。

## Verification evidence / 核验依据

| Check / 检查 | Exact file/version, slide/object/page / 实际文件版本、页与对象 | Action and result / 操作与结果 | Status / 状态 |
|---|---|---|---|
| Openable PPTX + structural QA / 可打开与结构 QA | | | untested/pass/fail |
| Source-versus-render / 原图与渲染对照 | | | untested/pass/fail |
| Scientific labels/equations/arrows / 标签、公式、箭头科学含义 | | | untested/pass/fail |
| Native text edit trial / 原生文字编辑实测 | | copied file, changed object, rendered result / 副本、对象与渲染 | untested/pass/fail/N/A |
| Native structural object edit trial / 原生图形编辑实测 | | | untested/pass/fail/N/A |
| Connector edit trial + protected regions / 连线编辑与保护区域实测 | | | untested/pass/fail/N/A |
| Actual print-size readability / 实际纸面大小可读性 | | dimensions, glyphs, clipping, strokes / 尺寸、字形、裁切、线条 | untested/pass/fail |
| Compiled figure and affected/adjacent pages / 编译图页及相邻页 | | figure, caption, float order, wrap end / 图、caption、浮动体与绕排终止 | untested/pass/fail |

Counts or a passing package validator do not prove native editing, scientific
accuracy, human acceptance or paper readiness. / 数量或结构通过不替代编辑实测、科学核验、人工确认及纸面验收。

## Paper mapping and delivery / 论文映射与交付

| Figure/slide/panel | Approved master fingerprint / 已批准主件指纹 | Export path/fingerprint / 导出路径与指纹 | Export/capture settings / 导出或截图参数 | TeX include/label/caption/width / TeX 映射 | Compiled PDF/pages / 编译 PDF 与页面 |
|---|---|---|---|---|---|
| | | | format, crop, aspect ratio, resolution / 格式、裁切、比例、分辨率 | | |

- Editable source and formula source / 可编辑源件与公式源:
- Final-size preview and source/render comparison / 纸面大小预览与原图对照:
- Authoritative local TeX/Overleaf file set / 当前权威 TeX 或 Overleaf 文件集:
- Build command/log/PDF / 编译命令、日志与 PDF:
- Completed stage and evidence / 已完成阶段与依据:
- Pending review, missing dependency or unresolved check / 待确认、缺失依赖或未完成检查:
- Next authorized action / 下一步已授权工作:

A preview or screenshot may be produced for review before approval; it is not an
approved paper export. Keep the master bound to each derivative. / 可先生成审阅预览或截图，但不能称为已批准论文图；每份派生图都绑定实际主件。
