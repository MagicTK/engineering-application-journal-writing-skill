# Branch Conversion Terminology Check

## Scope

On 2026-10-26, one new responding context used the frozen 4.2.42 suite for
three fictional terminology-and-writing requests. It received the raw cases and
the suite location, not the maintainer's predeclared criteria, previous answers
or private reading notes. The response disclosed preloaded workspace/history
context, no memory search, and a truncated terminology read followed by bounded
recovery. It did not inspect the original papers. This is not a memory-blank
trial, independent second grading or measured before/after improvement.

The source change admits compatible convolution-branch structural
reparameterization, supported by two scoped published engineering contexts and
separate Chinese wording evidence. It does not certify complete source networks
or convert the rest of the terminology bank into an automatic whitelist. The
existing pruning, distillation and latent-sampling records retain their scopes.

## Predeclared Checks And Observed First Answer

| Case | Required distinction | Observed outcome |
|---|---|---|
| Compatible branches | Preserve fixed normalization including epsilon, aligned convolutions, common post-sum activation and the retained inference graph; keep output checks separate from all-input proof and speed claims. | Names the scoped operation with traceable English/Chinese records. The 77-word Methods paragraph preserves the operations and no-retraining fact. Results retains the supplied 2e-6 output difference and slower 1.8-to-2.2 ms timing. |
| Nonlinear heads | Check the actual two maps; do not assume separately activated heads can be merged by averaging affine parameters. | Gives x=0 with outputs 0.5 and 0, rejects the all-input equality and supplies a small textual correction without changing the implementation. |
| Different training/structure roles | Separate Gaussian latent sampling, teacher-guided training and hidden-channel removal, while keeping full process inputs and student-only prediction. | Corrects the two-sentence description, does not invent sensor removal, runtime teacher fusion, a complete VAE or measured acceleration. |

All three first answers pass maintainer semantic review within the supplied facts.
No feedback or retest was needed, and no instruction changed after dispatch.
The Results tail restates the absence of speedup; it could be shortened, but is
not a factual defect or a reason to add a new universal writing rule.

Separate exact-rational arithmetic checked 300 constructed sequences and 4,650
positions for a compatible three-branch example, and reproduced the nonlinear
counterexample. These are synthetic operation checks, not the supplied 10,000
float32 measurements, source experiments, model training or hardware timing.
The request's numerical values are fictional inputs, not newly measured results.

The prior report is preserved at
[its original snapshot](../history/v4.2.42/pre-branch-conversion-report.json).
Program checks, source reading, matching hashes and semantic review have different
roles; none establishes publication acceptance or complete-suite correctness.

## Request And First Response

The following public transcript preserves the scientific wording. Machine-local
links are made repository-relative, client writing-block wrappers and quota
metadata are omitted, and Markdown trailing whitespace is normalized. Exact
tool output and the original prompt are retained privately. These presentation
changes do not constitute a revised answer.

### Raw Request

```text
Use the candidate suite at <suite root>, especially its Chinese terminology-polishing entry and relevant shared references. This is a fictional writing request, not a real experiment. Do not edit files, browse, search memory, inspect evals/history or private maintenance notes, run training or spawn agents. Answer the following, then state actual read ranges and any inherited context or truncated-read recovery; do not grade yourself.

A. 我在写冷却过程出口温度估计的英文论文。训练好的特征块有同一输入上的3点卷积、1点卷积和identity三个分支，各分支BN后相加，再共同经过一个ReLU。stride均为1、输入输出通道相同、各分支输出位置完全对齐。推理时BN用固定的训练统计量，包含epsilon。转换时折叠BN，把小卷积核居中补零，identity转为相应卷积，再相加核和bias，保留共同ReLU，不再训练。10000个合成输入上的float32最大输出绝对差为2e-6。在相同设备/批大小/测量边界下，转换前后平均推理耗时为1.8和2.2ms，其他部署数据没有。请先给这个操作的英中文基础名称及本套件内可核查的出处，再写50–85词Methods段落和一句Results。无需写整篇论文，不要补实验。

B. 另一个输出头实际是r(x)=0.5[ReLU(2x+1)+ReLU(-x-2)]。同学想替换成q(x)=ReLU(0.5x-0.5)，并写“The two heads are exactly merged by averaging their parameters, preserving the output for every input.” 请检查这一句能否保留，给一个明确检查及最小英文替换，不要改作者的模型实现。

C. 另一篇虚构论文训练时用z=mu+sigma*epsilon（epsilon为标准正态采样），以重构目标学习表示；固定教师提供额外的输出匹配目标。研究者另删除了一组隐层特征通道并重训学生，全部过程测量输入不变。预测时只用学生。草稿称“Structural reparameterization removes sensors and fuses teacher and student predictions for faster operation.” 请只修正这句话，可以拆两句，并简短解释三个训练/结构操作的不同角色。没有时延测量。
```

### First Response

以下拟稿仅采用题设的虚构事实，不表示我实施了实验。

**A. 名称与拟稿**
基础名称是 **structural reparameterization（也写作 structural re-parameterization），结构重参数化**。这里限定指兼容卷积分支向单一推理卷积的参数转换。

套件内可核查的依据：
- **英文操作**：[术语库第207行](../../references/engineering-application-terminology-bank_CN.md#L207)记录 P45 的 PDF pp.4–5、式(3)–(4)、(21)，以及 P132 的 pp.5–6、§3.3.2、Fig.4；P45 属于经核对的语义等价用例，不是完整名称的逐字匹配。
- **中文译名**：[第347行](../../references/engineering-application-terminology-bank_CN.md#L347)另列北航学报配对题名及中国图象图形学报期次页摘要作为译名依据。
- **适用边界**：[场景决策第268–272行](../../references/terminology-decisions_CN.md#L268)要求检查固定BN、对齐与激活位置；[来源说明](../../references/published-evidence.md#L1302)还明确指出 P132 某转换式遗漏 epsilon，不能照搬。

按题设，仿射分支在共同 ReLU **之前**相加，支持实数算术下的等价转换；有限输入上的 float32 检查并非全输入证明。测得耗时增加，也不能写成加速。

**Methods**

For cooling-process outlet-temperature estimation, we applied structural reparameterization to the trained feature block. The aligned 3-point convolution, 1-point convolution, and identity branches shared the input, used unit stride and equal input/output channel counts, and were summed before a common ReLU. We folded batch normalization using fixed training statistics, including epsilon, represented identity as a convolution, centrally zero-padded smaller kernels, and summed the resulting kernels and biases. The resulting single 3-point convolution retained the common ReLU without retraining.

**Results**

Across 10,000 synthetic inputs, the maximum absolute output difference in float32 was 2 × 10⁻⁶, while mean inference time increased from 1.8 to 2.2 ms on the same device, with the same batch size and timing boundaries, indicating no measured speedup under these conditions.

Methods 为 **77词**。

**B. 明确检查**
原句**不能保留**。取 \(x=0\)：
\[
r(0)=\tfrac12[\operatorname{ReLU}(1)+\operatorname{ReLU}(-2)]=0.5,
\qquad q(0)=\operatorname{ReLU}(-0.5)=0.
\]
一个反例就否定了“对每个输入保持输出”。这里先分别激活再平均，不能交换为先平均仿射参数再激活；无需修改作者实现。

最小英文替换：
Averaging the parameters does not preserve the output for every input.

**C. 句子修正**
The student is trained with a reconstruction objective using Gaussian reparameterization, \(z=\mu+\sigma\epsilon\), where \(\epsilon\) is standard normal noise, and an additional output-matching objective supplied by a fixed teacher. Selected hidden feature channels are removed and the student is retrained; all process-measurement inputs remain unchanged, and prediction uses only the student.

三个操作的角色不同：
- **高斯重参数化**：用于潜变量采样及重构表征学习，不是推理分支合并；仅凭采样式与重构目标，也不足以认定完整 VAE。
- **知识蒸馏**：固定教师提供训练目标，不是预测时融合教师与学生输出。
- **隐层通道剪枝及重训**：改变学生内部结构，不是删除实体传感器。没有时延测量，删除“faster operation”。

**实际读取**
下表均为本次读取，原始链接指向绝对路径（公开副本已规范化）；“命中行”仅指关键词检索返回的单行，不表示通读周边内容。

| 文件 | 正文读取行号 | 额外命中行 |
|---|---|---|
| [主入口](../../SKILL.md) | 1–200 | 无 |
| [中文术语润色入口](../../skills-zh/engineering-terminology-polishing-zh/SKILL.md) | 1–179，全文 | 无 |
| [中文术语库](../../references/engineering-application-terminology-bank_CN.md) | 1–50、150–212、230–243、340–349 | 91、229、291、309、324 |
| [中文场景决策](../../references/terminology-decisions_CN.md) | 250–290 | 113 |
| [发表证据](../../references/published-evidence.md) | 59–60、146、1302–1325 | 90–91、99、124、137–138、476、578、589、654、656、679、826、871、876、893、971、973、981、1019、1021、1066、1079、1088–1089 |

另外列出了套件根目录及指定目录的文件名，并对 [terminology-and-style.md](../../references/terminology-and-style.md)作关键词检索，无命中，未读取正文。

**截断恢复**：首次术语库输出发生截断，随后分段完整补读177–189、190–208、209–212行；未把截断内容当作已完整读取。
**继承上下文**：对话自动提供了通用规则、项目约束、技能目录及记忆摘要；未搜索记忆，也未以旧项目记录作为本答依据。未读取评测、历史或私有维护笔记，未联网核验原论文。未改文件、训练或启动代理。
