# Initial Source-Identity Diagnostic Response

Actual fictional-case response. This pass disclosed additional historical-index access and is not recorded as an isolation-compliant evaluation. Private local links and terminal blank lines are normalized.

**I4128-A**
实际 helper 返回值：

```text
P01: '10.1000/example(part)'
P02: '10.1000/example(part)'
P01 == P02: True
```

中文判断：两个 URL 被归为同一 DOI 身份，不能因编号不同而计作两篇独立支持论文。括号得到保留；resolver、URL 编码及 ASCII 大小写差异不产生新身份。本次未验证注册、出版状态或机制支持。

英文作者意见：
:::writing{variant="standard" id="41281"}
P01 and P02 normalize to the same DOI name, so they should not be counted as two independent supporting papers. Please check the bibliographic records and the source’s mechanism definition before treating this item as evidence for a general mechanism.
:::

**I4128-B**
按题目顺序，四个实际身份字符串为：

```text
%C3%81:     '10.1000/Á'
%C3%A1:     '10.1000/á'
part%23tail: '10.1000/part#tail'
part#tail:   '10.1000/part'
```

中文判断：
- 两组比较结果均为 `False`，四个返回身份均不同。helper 只折叠 Basic Latin `A–Z`，不把 `Á` 与 `á` 合并；不能对整个 Unicode 字符串做 `casefold()`。
- `%23` 解码后属于 DOI 路径内容；原始 `#tail` 则是 URL fragment，不属于该路径。不能为了去重任意删除符号。
- 两篇主来源若确属不同作品，仅正文注释共同引用一篇背景论文，不应删除主来源。背景引文重复不等于主作品重复。
- 此检查不要求把可靠机构链接全部替换为 DOI，也不能据此否定非 DOI 来源。

**I4128-C**
英文建议：
:::writing{variant="standard" id="41282"}
Use adaptive fusion as a broad description where appropriate, while distinguishing input-dependent scalar gating from query–key–value cross-modal attention. Attribute Condition-Aware Expert Fusion Module to the paper that defines it rather than presenting it as an established module family. Retain your own clearly defined module name as a proposal of this work, and leave its Chinese terminology unverified until reliable bilingual evidence is available.
:::

中文判断：
- **自动检查的边界：**只能比较支持范围内的 DOI 身份。题设已说明两篇作品不同，但“DOI 不同”本身不能证明作品独立、已经发表、操作语义一致或完整名称获得多源支持。
- **基础词：**不全面禁用 `fusion`、`gate`、`attention` 或准确使用的 `adaptive fusion`。两篇共享宽泛词语，不代表标量门控与跨模态注意力是同一种具体机制。
- **完整名称：**`Condition-Aware Expert Fusion Module` 目前只有单篇定义，可归属该论文引用，不能凭两篇不同 DOI 升格为通用模块家族。
- **中文证据：**个人博客机器翻译不足。还需术语权威、标准或可靠中文学术来源中的中英对应与匹配定义，并记录链接和段落；存在争议时再寻第二独立来源。本轮不联网，保持待核验。
- **作者新名称：**不必删除。定义清楚、明确属于本文新提出的组件即可保留，不要求先有两篇同名论文；名称本身也不证明技术新颖性。

**执行证据**
读取的入口标注版本为 `4.1.28`；已读相关 references、`evals/README.md` 与 [validate_suite.py](../../scripts/validate_suite.py)。使用指定 Python 运行时加 `-B` 导入现有模块，实际调用 helper **6 次**，进程退出码 **0**，输出 `dont_write_bytecode: True`。未运行整套验证器，未联网、编辑、安装、开展研究实验或启动额外代理，也未打开其他 eval 文件或实际论文。

读取隔离存在已说明的启动偏差：额外检索了记忆索引并读取通用流程 skill。因此，以上是实际执行结果，但不能登记为完全满足读取隔离的独立盲测。
