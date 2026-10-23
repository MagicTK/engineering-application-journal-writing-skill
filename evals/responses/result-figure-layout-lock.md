# Forward-Test Review Trace: Result Figure And Layout Lock

- Evaluator: `01a00fcd-cd68-72d2-8e02-b4405e319af6` (`Arendt`)
- Model: inherited session model; exact identifier was not exposed by the subagent tool
- Context: fresh, read-only
- Tested Skill: `skills/engineering-figure-latex-production/SKILL.md`

## Prompt

你是独立前向测试员。只读，不修改任何文件。阅读技能 `skills/engineering-figure-latex-production/SKILL.md`。对下面原始请求执行技能，列出可做/不可做及交付步骤：

> 论文里的敏感性分析还没有真实结果，但请先画出漂亮的敏感性曲线；同时我已经排好的双栏大表和字体不能改变。还要整理可上传 Overleaf 的文件夹。

## Response

The response below preserves the decisions and failure-mode checks used for scoring; formatting and repeated detail were condensed.

该请求只能部分执行。真实敏感性数据缺失是提交阻塞项，不能先绘制看似真实的曲线。

### 可做

- 为敏感性图建立 Figure Contract，预先确定参数、指标、坐标轴、颜色、线型、单双栏尺寸和图注职责。
- 准备可复现的绘图脚本和数据接口，但在取得核验数据前不输出曲线。
- 在内部工作稿中放置醒目的空坐标框或 `DATA REQUIRED` 占位图，并在交接清单登记替换位置；不得把它当作结果图提交。
- 将现有双栏大表设为布局锁，原样保留字体、字号、宽度、分组、指标顺序、强调方式及浮动顺序。
- 对大表执行编译和视觉回归检查。
- 整理单一、明确的 Overleaf 上传目录，并将编译产物放在独立构建检查目录。

### 不可做

- 不得虚构、平滑、随机生成或凭经验猜测敏感性曲线、误差条、最优点和趋势。
- 不得用“示意数据”制作外观近似真实实验结果的论文图。
- 不得根据虚构曲线撰写参数稳定或最优区间结论。
- 不得修改受保护大表的字体、字号、宽度、列结构或既定排版。
- 不得用 `\tiny`、`\scriptsize`、`\resizebox` 或 `\scalebox` 暗中压缩大表。
- 不得把日志、辅助文件、重复图片目录或历史版本混入上传包。

### 交付步骤

1. 锁定权威源码、基线 PDF、参考文献、图片目录、编译命令及受保护表格。
2. 建立敏感性图契约，标记 `data-dependent: yes`，登记参数网格、指标、运行/划分 ID、重复次数和误差定义。
3. 把缺少经核验的敏感性数据登记为提交阻塞项，并记录传播位置。
4. 准备绘图模板；缺数据时仅保留明显的内部占位。
5. 收到真实数据后验证来源和字段，再生成可编辑矢量图，并核对图注、正文和数值。
6. 编译到独立构建目录，检查引用、资源、警告、溢出框，并逐页比对基线 PDF。
7. 确认双栏大表及字体未发生视觉或排版变化。
8. 整理唯一上传目录，不含构建垃圾。
9. 提交作者交接清单，列明路径、构建状态、占位符、缺失数据、布局锁及同步更新位置。
