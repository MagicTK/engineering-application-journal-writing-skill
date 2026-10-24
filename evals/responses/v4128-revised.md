# Final Source-Identity Fictional Response

Actual response after self-contained-fixture clarification. Supplied identities and component names are fictional; private local links and terminal blank lines are normalized.

**I4128-A**
实际 helper 返回值：

```text
P01 → '10.1000/example(part)'
P02 → '10.1000/example(part)'
相等比较 → True
```

中文判断：两者是同一规范化 DOI 身份，不能计作两篇独立支持论文。编码形式、resolver 域名、查询参数和片段没有增加来源数；括号仍被保留。按重复来源计一次，也尚不能满足“两个不同已发表工作、机制语义匹配”的通用名称准入要求。

英文作者核查意见：

:::writing{variant="standard" id="41281"}
P01 and P02 share the same normalized DOI identity and cannot count as two independent supporting papers. Please count this source once; admission as a general mechanism still requires another distinct published work with a matching operational definition.
:::

**I4128-B**
按题目给定顺序，四个实际身份字符串为：

```text
%C3%81       → '10.1000/Á'
%C3%A1       → '10.1000/á'
part%23tail  → '10.1000/part#tail'
part#tail    → '10.1000/part'

第一对相等比较 → False
第二对相等比较 → False
```

中文判断：
- 第一对不能认定相同。helper 仅折叠 Basic Latin `A–Z`，不对整个 Unicode 字符串执行 `casefold()`。
- 第二对不能认定相同。`%23` 解码后属于 DOI 路径内容；原始 `#tail` 是 URL 片段，不属于路径。不能删掉身份字符串中的 `#tail` 来制造重复。
- 不同身份字符串也不自动证明是独立学术工作，或支持相同机制。
- 两篇不同主来源在正文注释中引用同一背景论文，不构成删除主来源的理由。应区分主来源身份与背景引文重合，也不必把所有机构链接强换为 DOI。

**I4128-C**
英文建议：

:::writing{variant="standard" id="41282"}
Use adaptive fusion as a broad descriptor, while distinguishing input-dependent scalar gating from query–key–value cross-modal attention. Attribute Condition-Aware Expert Fusion Module to the paper that defines it rather than presenting it as an established module family. Retain your clearly defined new module name as a proposal of this work, and treat its Chinese rendering as provisional until independently supported.
:::

中文判断：
- **自动身份检查**只能识别其覆盖范围内的 DOI URL 身份重复，不能证明出版真实性、工作独立性、操作等价性、名称通用性或译名可靠性。
- **基础词**可以保留。`fusion` 或宽泛的 `adaptive fusion` 不必禁用，但两种计算应分别说明；共享措辞不能证明它们是同一种具体机制。
- **完整模块名**目前只有单篇定义依据，可带归属引用，不应仅凭两个不同 DOI 就准入通用模块家族。
- **中文证据**仍缺可靠术语机构或中文学术来源中可对应英文名称、且定义匹配的正文依据，并记录 URL 与段落。个人博客机器翻译不足；核查前保留英文及描述性中文说明。
- **作者新名称无需删除**。明确标为本文提出并给出操作定义即可；这既不要求已有两篇同名论文，也不自动证明技术新颖性。

**执行证据**
使用指定运行时以 `Python -B` 导入当前 [validate_suite.py](../../scripts/validate_suite.py)，直接调用 `resolver_doi_identity` 六次；输出 `dont_write_bytecode=True`，进程退出码 `0`。未运行会遍历其他文件的整套验证入口。

判断依据为当前 v4.1.28 的[术语准入规则](../../references/engineering-application-terminology-bank.md)。未联网、编辑文件、安装或启动额外代理；未检索任务记忆、历史响应或评分文件，也未采用 README 中的既往评测结论。
