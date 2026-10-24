# Fictional Gating-Path Final Response

One fresh task context handled the same two requests on the frozen final snapshot. Only the prior-release read root differs. Baseline core judgments already passed; this is not controlled general writing improvement. Artifact wrapper, local-reference links if any and whitespace only are normalized; raw answers remain private.

测试边界：当前上下文含预设历史，不能称为“记忆空白”，也无法声称掌握完整内部服务轨迹。本轮是同一上下文处理 A、B，不是两次独立模型实验。

**A**

> Sigmoid-generated elementwise gates scale a feature branch, which is added to the original vector to form the residual output y = v + g ⊙ v.

作者说明：
- \(g\odot v=[0.4,-2.4]\)，故 \(y=[2.4,-5.4]\)。门控缩小了附加分支的幅值，但最终系数为 \(1+g=[1.2,1.8]\)，两个原特征的输出幅值均增大。
- 强制 \(g=0\)：关闭附加分支，得到 \(y=v=[2,-3]\)。强制 \(g=1\)：取消分支内的乘性调节，但保留相加，得到 \(y=2v=[4,-6]\)，并非仅保留原特征。
- 这里没有变量删除操作；即使门值为零，原特征仍经旁路进入输出。取值位于零与一之间，也不足以赋予门值故障概率含义。
- 原文的 attention 称谓可保留，同时明确实际门控与残差运算；不据名称改算式，也不要求所有门控采用同一种归一化或硬选择。

**B**

英文摘要：

> We propose Context-Gated Fusion for industrial classification by combining complementary variable history and neighborhood features. A local encoder produces history features x, while a relation encoder produces neighborhood features h. Both representations are fully computed before an MLP processes their concatenation and applies a sigmoid to generate elementwise gates g. The classifier receives r = x + g ⊙ h, retaining a direct local path and regulating the neighborhood contribution. After training, the MLP parameters remain fixed while gate values vary with the input. In each of two case studies, the model achieves higher classification accuracy than a fixed-gate control using g = 0.5, with all other model components and training settings matched.

贡献候选：

> Context-Gated Fusion computes sigmoid gates from concatenated history and neighborhood features, weights neighborhood features elementwise, and adds them to history features for classification, yielding higher accuracy than a matched fixed-gate control in both cases.

作者说明：
- 保留作者批准的 Context-Gated Fusion，作为本工作提出并定义的新组合；不要求前人已有同名，也不将其纳入通用术语库。中文可用“门控机制”作基础描述；完整中文名尚未批准、核实，不宣称标准译法，也不借用 Age-Aware State Gate 或“年龄门控”。
- 门值随输入变化，不等于持续参数学习；两路特征均完整计算，不支持专家稀疏调度或省算解释，也不是工况概率或采样控制。准确率结论限于两个给定案例及匹配固定门对照，不延伸至延迟、跨厂泛化或在线部署。
- 正式成稿时核对特征维度与逐元素对齐、评估划分、准确率记录及对照设置。题设未给具体增幅或统计检验，不补写数值或显著性。
