# Fictional Wrapped-Phrase Integration Response

Repaired final-source response. Inputs and operations are synthetic. Only private local links and terminal blank lines are normalized.

已按当前 [Skill 4.1.32](../../SKILL.md)，用 `Python -B` 导入当前 [audit()](../../scripts/audit_terminology.py)，逐个检查了 10 个内嵌字符串。使用 `tex=True, min_count=1`，以显示单次搭配；返回模式均为 `review_candidates_only`。未写文件、联网、安装、运行科学实验或启动代理；未读取任务历史、私有记录或真实论文，无被迫历史访问。

**M4132-A**

| 候选规则 | 实测词组 | 次数 | 起止源行 |
|---|---|---:|---|
| `variable-feature` | variable-wise features | 1 | 3-4 |
| `exchange` | information exchange | 1 | 5-6 |
| `offline` | Offline | 1 | 9-9 |

`attribute`、`record` 均无候选：第1行注释和第10行引用键未被当作正文；标签中的 `offline` 也未额外计数。这些候选不是禁词。

局部原句 → 改句，仅第5-6行：

原句：`Unit summaries support information exchange before classification.`

:::writing{variant="standard" id="41321"}
The unit summaries are summed using learned weights to form the classifier input.
:::

中文理由：改句直接交代已确认的加权求和及分类用途。`variable-wise` 符合按变量分别编码的操作，保留；`offline assay` 确指实验室化验，也保留。

**M4132-B**

| 独立输入 | 完整 `exchange` 候选次数 | 完整 information exchange 搭配次数 | 实测说明 |
|---|---:|---:|---|
| B1：百分号后换行 | 0 | 0 | 输出单个连写词 `informationexchange`，次数1 |
| B2：真正空行 | 0 | 0 | 空段切断搭配，不拼接第1、3行 |
| B3：中间有标签 | 0 | 0 | 排除标签并保留短语边界；`attribute` 也无候选 |

正向控制：链接显示文字命中 `state-condition`，词组为 `operating conditions`，**1次，源第1-2行**；相同完整搭配也出现1次。网址目标中的 `records` 未生成 `record` 候选。

作者建议：先核对预期排版中的词间边界，再检查句法和含义；未命中不等于语言全部正确，连写串也不应被赋予科学含义。

**M4132-C**

不能从源文本命中三次，推出 PDF 出现三次，更不能推出通行方法或中文译名已经验证。

- **PDF 最小核查**：确认实际编译入口、宏定义与调用、包含文件及生效条件，再核对对应编译 PDF 中的可见位置和次数。脚本不展开任意宏、`\input` 或自定义条件；定义处、调用处与最终显示次数可能不同。本轮未执行这些核查。
- **名称最小核查**：若要推荐为通用类别，需至少两篇不同的相关已发表论文，在定义或实质说明中具有匹配的对象与操作；有歧义时宜检查3-5篇。同一论文的镜像仍只算一篇，熟悉的基础词也不能自动验证完整复合名称。
- **中文单独核查**：需可靠术语来源或中文学术来源中的英中对应及匹配定义。英文用法成立不等于中文译名成立，目前不能声称“顶刊已验证”。

可继续检查已提供文本的对象、操作、输入输出及下游用途，保留准确的作者新提模块名，并明确它是本研究提出的组件。证据未齐是“待核查”，不是一概禁用；上述要求也不是每个普通句子必须附两篇引用。依据：[现行名称准入规则](../../references/engineering-application-terminology-bank.md)。

**M4132-D**

以下均为实际调用结果，表中空格是脚本对普通源换行的归一化显示：

| 独立输入 | 候选规则 | 实测词组 | 次数 | 起止源行 |
|---|---|---|---:|---|
| root 换行 cause | `causality` | root cause | 1 | 1-2 |
| cross 换行 stage | `stage-scope` | cross stage | 1 | 1-2 |
| stage 换行 level | `stage-scope` | stage level | 1 | 1-2 |
| real 换行 time | `deployment` | real time | 1 | 1-2 |
| variable 换行 specific features | `variable-feature` | variable specific features | 1 | 1-2 |

检查判断：命中只证明脚本识别到了候选词组，不能证明物理根因或实时达标，后两者分别需要匹配的根因证据及规定条件下的时限证据。`stage-level` 指粒度，`stage-structured` 涉及保留并定义的结构，不能据此互换；`variable-specific` 与 `variable-wise` 的语义侧重不同，也不应一律替换。
