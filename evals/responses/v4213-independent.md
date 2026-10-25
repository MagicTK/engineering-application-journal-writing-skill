# Active-Text Terminology Review: Actual Response

One fresh context answered one fictional request using frozen v4.2.13. The task answer and final scope statement below are unchanged; the intervening local-environment disclosure is omitted and summarized in the review. No feedback or correction was needed.

**正文范围**
启用正文为第 **6、7、9、11、16、21行**。第4、14行位于关闭分支；第19行位于注释环境，均不作为正文问题。关闭分支中的第3、13行不会开启有效注释环境；第18行的 `\else` 在注释中，不改变分支状态。

**术语核对**
已实际运行只读工具，共返回3类、5处候选，源起止行均为同一行。

| 源行号 | 原词或搭配 | 是否有充分理由修改 |
|---|---|---|
| 6 | `attributes`（`semantic attributes`） | **无，保留。** 指已知故障类别的语义描述，不是过程测量变量，不替换为 `variables`。 |
| 7 | `Operating conditions` | **无，保留。** 指两批数据的运行工况，与第16行的当前输入状态含义不同。 |
| 11 | `record` | **无，保留。** 是“记录测量”的动词，不是样本或记录条目的名词。 |
| 16 | `operating state` | **无，保留。** 当前输入状态决定门控系数，与模型参数固定并不矛盾，也不意味着在线更新参数。 |
| 21 | `records`（`Sensor records`） | **无，保留。** 指关联到学习样本标识的存储条目，不能机械替换为 `samples`。 |

人工补充：第9行的 `real-world dataset` 涉及数据来源。片段不足以核实这一来源描述；若需确认，应核对采集来源说明，不据此直接判错。`1200 samples` 按虚构设定保留，不核验或改动数值。

术语工具只列候选，不裁定语法、语义正误，也不能完整展开任意 TeX 宏或替代编译后的 PDF 核验。本次仅核对该虚构片段的正文范围与用词，不构成科学正确性认证。
