# Numerical Pretraining And Generated Categories: Initial Actual Response

One context used v4.2.21. Both cases passed the maintainer review without feedback. The request and actual response are preserved below; private local links and writing wrappers are normalized.

## Original Fictional Request

Use the Engineering Application Journal Writing Skill at SUITE_ROOT. This is a fictional writing and result-checking request, not authorization to change files or run research experiments. Read only the public entrypoints and relevant references there; do not read evals, tests, private maintenance records, actual manuscripts, other projects or memory files. Do not browse or delegate. Briefly disclose the public passages actually read and any inherited context or truncated outputs. Respect the existing account-usage policy; do not output account information.

We have two independent studies, not two branches of one model. Help a research-group student explain each study without treating every pretrained model as the same kind of language-model application. Do not invent novelty, mechanisms or results.

A. Current concentration estimation from industrial process measurements. A numeric encoder was pretrained by reconstructing deliberately masked values in an external multivariate time-series corpus. Corpus provenance and the absence of any downstream evaluation sequence from pretraining have already been checked. No text, tokenizer for language, class descriptions, language model, image conversion or chat service is used. At the downstream task, the pretrained encoder weights are frozen; additive low-rank weight updates and a regression head are trained jointly with measured concentration targets from 20 production batches. At prediction, each available measurement window passes through the encoder with those learned updates and the head, producing one current concentration estimate. Eight separate held-out production batches supply evaluation; no evaluation-time updates are made. A matched predictor using the same encoder architecture without pretraining, the same downstream fitting data and the same downstream update/head budget has MAE 0.16 g/L; the pretrained route has MAE 0.12 g/L. These are the only measured results; no hardware, prompt or language-output measurements exist.

B. Bearing diagnosis by generated category text. A pretrained general-audio encoder and language decoder are adapted using vibration/text training pairs. The training descriptions are filled from templates using the known training fault labels and training metadata; these descriptions are supervised training targets, not extra independently collected faults. Base weights remain frozen while low-rank updates are fitted. At prediction, a vibration window and a fixed instruction are supplied; the true fault label and its target description are not inputs. The generated answer is mapped to one of the three allowed categories by a predeclared rule: trim whitespace, lowercase, and match the exact category strings normal, inner-race or outer-race. No synonym mapping, retry, output filtering or abstention mechanism is implemented. All eight independent held-out decisions must be scored once. References, in order, are [normal, normal, inner-race, inner-race, outer-race, outer-race, inner-race, normal]. Generated answers, in the same order, are [normal, normal, inner-race, outer-race, outer-race, bearing issue, inner-race, uncertain]. No maintenance actions, human explanation ratings, unknown-class tests or hardware times were collected.

The student's shared draft says: 'Both models require no labeled training data because their backbones are pretrained and frozen. A improves prediction through language reasoning with no additional inference work. B obtains 83.33% diagnostic accuracy after keeping only valid labels, proving actionable fault explanations and reliable recognition of unknown faults.'

Please return: (1) a concise Chinese judgment of the learning/prediction roles and the draft's factual problems; (2) the exact result calculations and their denominators; (3) two separate short English method-overview paragraphs, one for each study, and two separate short English result paragraphs. Use positive, connected academic prose; keep checks and optional improvements outside the manuscript paragraphs. Finally identify only unknowns that would matter for a stronger claim the author actually wants to retain. Do not demand a universal suite of prompt, hallucination, deployment or new comparative experiments merely because pretraining is used.

## Actual Response

**阅读披露**
已读指定发布版的 [SKILL.md](../../SKILL.md) 全文，以及以下公开参考的相关段落：[topic-playbooks.md](../../references/topic-playbooks.md) 第2、8、9节；[experiment-evidence-design.md](../../references/experiment-evidence-design.md) 的划分、比较、指标与拒识部分；[argument-and-prose-craft.md](../../references/argument-and-prose-craft.md) 第1–6节。另查看了公开目录、标题和关键词命中；一次检索输出截断，结论所用段落随后已定点重读。

继承上下文包含系统提供的工作区记忆摘要，但未采用其中的项目事实，也未读取记忆文件或其他禁读内容。未修改文件、运行研究实验、浏览或委派；仅核算题给数字。

**1. 中文判断**
- **A：自监督预训练，随后受监督回归。** 掩码数值重建用于预训练；20个生产批次的实测浓度用于联合训练低秩权重增量和回归头。冻结的是基础权重，不是所有可学习参数。预测时输出当前浓度，不是未来预测、语言推理或文本生成；评价期间不更新参数。
- **B：受监督适配，以文本生成实现三分类。** 训练描述由已知训练标签和元数据填入模板形成，是监督目标，不是新增独立故障样本。预测输入为振动窗口和固定指令，再按预定规则解析生成答案。训练目标含标签不等于测试标签泄漏，也不等于无需标签。
- **草稿的问题：** 两项“无需有标签训练数据”均错误；A没有语言推理过程，冻结权重也不能证明相对基线没有额外推理开销。B筛除无效答案改变了分母；类别正确率不能证明解释可指导维护。`uncertain` 是本规则下的无效输出，不是已实现的拒识机制，更不能证明未知故障识别可靠。

**2. 结果与分母**
**A**
- MAE绝对下降：\(0.16-0.12=0.04\ \mathrm{g/L}\)。
- MAE相对下降：\((0.16-0.12)/0.16=25\%\)，分母是基线MAE，不是准确率提高25个百分点。
- 评价来自8个独立留出批次。若按窗口汇总，\(\mathrm{MAE}=\sum_{i=1}^{N}|\hat y_i-y_i|/N\)；题述未给出窗口总数及聚合方式，不能自动把8当作MAE的平均分母。

**B**
正确的是第1、2、3、5、7次；第4次误分类，第6、8次无效。
- **总体诊断准确率：\(5/8=62.5\%\)**，八次决策全部计入一次。
- 类别有效输出率：\(6/8=75\%\)；无效输出率：\(2/8=25\%\)。
- 有效输出内的条件准确率：\(5/6=83.33\%\)。该数可明确标为补充统计，不能替代总体准确率，也不能追认一个未实现的筛选或弃权机制。

**3. English Paragraphs**
两项研究分别成文；以下段落不包含作者核查清单。

**Study A: Method Overview**

The study estimates current process concentration from industrial measurement windows. A numerical encoder is pretrained through self-supervised reconstruction of deliberately masked values in an external multivariate time-series corpus. Its pretrained base weights are then frozen while additive low-rank weight updates and a regression head are trained jointly using measured concentration targets from 20 production batches. At prediction, each available measurement window passes through the encoder with the learned updates and the head to produce one current concentration estimate. The fitted parameters remain fixed throughout evaluation.

**Study A: Results**

On eight held-out production batches, the pretrained route achieved an MAE of 0.12 g/L, compared with 0.16 g/L for the matched predictor using the same encoder architecture without pretraining. Both predictors used the same downstream fitting data and matched budgets for the weight updates and regression head. The observed improvement was an absolute MAE reduction of 0.04 g/L, corresponding to a 25% relative reduction.

**Study B: Method Overview**

Bearing diagnosis is formulated as category-text generation from vibration windows. A pretrained general-audio encoder and language decoder are adapted using vibration and text training pairs. The text targets are descriptions constructed from templates using known training fault labels and metadata, and adaptation trains low-rank updates while keeping the base weights frozen. At prediction, the model receives a vibration window and a fixed instruction. Each generated answer is normalized by trimming whitespace and lowercasing, then mapped by exact matching to normal, inner-race, or outer-race.

**Study B: Results**

Among eight independent held-out decisions, five generated answers matched the reference category, one selected an incorrect allowed category, and two fell outside the permitted category set. Scoring all eight decisions once, with unmatched outputs counted as incorrect, yielded an overall diagnostic accuracy of 62.5% (5/8). The category-valid output rate was 75% (6/8), and the invalid-output rate was 25% (2/8).

**4. 仅与保留强主张有关的未知**
- **若A保留“相对基线无额外推理开销”：** 需要明确开销指标、执行路径、低秩增量是否合并以及对应比较证据。只有声称硬件时延或实际运行效率时，才需要相应测量。
- **若B保留“解释可指导维护”：** 需要明确输出支持哪种维护判断，以及验证解释或行动有效性的依据；现有类别答案及准确率不能回答这一问题。
- **若B保留“可靠识别未知故障”：** 需要明确未知类、实际判别或拒识机制及相应已知/未知评价。当前流程没有这些实现与证据，不能靠重新解释两条无效答案保留该主张。

“无需标签”和“A通过语言推理”是已确定的事实错误，不是待补实验的未知。其余新增检查应随作者真正保留的主张选择，不因使用预训练而统一追加。
