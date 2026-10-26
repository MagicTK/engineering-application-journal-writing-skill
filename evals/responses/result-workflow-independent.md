# Result Workflow: Independent First Response

The following is the actual first response of one new responding context. Local
paths, temporary-output links, interpreter path and client writing-block wrappers
are normalized; account-status metadata is omitted. The substantive prose and
limitations are retained. Exact raw records remain with the maintainer. This was
not a memory-blank test or multiple independent respondents.

## Requests

Request A (Chinese novice user): 我想学怎样从同一份结果整理图表和结果文字。请找到套件中的可运行虚构例子并实际生成一次产物，读生成结果，给我一个简短中文解释、两句英文结果描述和英文图注。这个例子能否报告300个不同测试样本，或者Variant B在每一次运行均显著更好？解释要直接，不要只重复原则。
Request B (separate fictional author request): 我的真实稿结果已经确认，当前只提供两个宏平均F1均值81.2%和82.0%。我只想要一句英文比较，不改表、不重跑实验。能否把教学例子里的SD拿来给我的图加误差条？直接给一句英文及必要说明，不做整篇审查。

## First Response

**A：已实际生成并读取产物**
先从每张混淆矩阵计算指标，再按方法汇总均值和样本标准差，表格与图片使用同一组统计量；结果文字据此撰写。

| 虚构方法 | 宏平均 F1 均值 | 样本 SD |
|---|---:|---:|
| Reference A | 79.90% | 0.75 个百分点 |
| Variant B | 82.73% | 2.33 个百分点 |

两个问题的直接答案：
- **不能报告 300 个不同测试样本。** 示例约定三张结果表使用同一批 100 个虚构样本，每种方法合计是 300 次分类决策，不是 300 个不同样本；混淆矩阵本身也不能验证样本身份。
- **不能说 B 每次均显著更好。** 第二组中，B 为 80.06%，反而低于 A 的 80.74%。这些是构造结果，不是真实训练运行，也没有显著性检验；SD 仅描述构造数值的分散程度。

英文结果描述，两句：
In this fictional example, Variant B had a higher mean macro-F1 than Reference A (82.73% versus 79.90%), with sample SDs of 2.33 and 0.75 percentage points, respectively. However, in the second constructed outcome table, Reference A scored 80.74%, compared with 80.06% for Variant B.

英文图注：
Macro-F1 in a fictional teaching example. Open markers represent three constructed outcome tables per method; filled markers and error bars show the mean and ±1 sample standard deviation (ddof = 1). The vertical axis spans 75–90%. These constructed results are not repeated training runs.

**B：仅作一句比较**
The mean macro-F1 was 82.0%, compared with 81.2%, a difference of 0.8 percentage points.

**不能借用教学例子的 SD 添加误差条。** 它与真实稿件的结果无关，两个均值也无法确定 SD。当前可以只报告均值，不添加误差条、不声称统计显著；无需为完成这句话改表或重跑实验。

**执行与产物**
实际执行一次，退出码为 `0`；生成记录显示 Python `3.7.4`、Matplotlib `3.1.1`：
```bash
MPLCONFIGDIR=$WORKDIR/tester-mpl \
XDG_CACHE_HOME=$WORKDIR/tester-cache \
PYTHONDONTWRITEBYTECODE=1 \
$PYTHON_FOR_PLOT \
../../assets/examples/result-workflow/build.py \
--output $WORKDIR/tester-output
```

已完整读取生成的 表格 (`table.md`)、CSV (`summary.csv`)、证据记录 (`evidence.json`)，并打开检查了图片 (`macro-f1.png`)，未见文字遮挡或裁切。

本次完整读取的套件文件：
- [中文自动化入口](../../skills-zh/engineering-experiment-automation-zh/SKILL.md)、[实验证据设计](../../skills-zh/engineering-experiment-evidence-design-zh/SKILL.md)
- [执行指南](../../references/experiment-execution_CN.md)、[运行记录模板](../../assets/templates/experiment-run-manifest.md)
- [示例说明](../../assets/examples/result-workflow/README_CN.md)、[生成脚本](../../assets/examples/result-workflow/build.py)、[虚构输入](../../assets/examples/result-workflow/fixture.json)

**披露与可用性**
本轮已预载历史记忆摘要、技能目录和工作区规则，因此不是完全空白上下文；未使用历史内容作答，未另读记忆、`evals/`、`tests/`、其他项目、既往评测答案或维护记录。源文件读取无截断，命令无失败、无补救或指令修改；此路径未遇到可用性故障。

