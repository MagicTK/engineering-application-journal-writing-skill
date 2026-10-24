**A. 术语判断**
可以称为 **physics-informed neural network（PINN）**：这里有明确的物料衡算，并通过输出构造在训练和推理中满足它；PINN基础类别并不限于PDE残差损失。“只能叫普通神经网络”的判断过严。

Skill中支持该基础名称的是**两篇不同作品**：
- **P59**：*Physics-informed neural networks with hard linear equality constraints*，2024；核验记录阅读的是作者版v1。
- **P60**：*Physics-informed neural networks with hard nonlinear equality and inequality constraints*，2026；核验记录阅读的是作者版v2。

每篇的预印本与期刊版只算一篇。P60沿用了P59的研究路线，因此是两篇作品中的基础术语使用，不能说成两次独立发明。中文基础译法**“物理信息神经网络”可以使用**，Skill已有独立中文学术摘要核验记录。

**KKT-hPINN是P59的完整专名**，不能因同样使用约束层便移植到当前方法，尤其当前层没有KKT推导。作者仍可为真正的新方法命名，但应明确是本文提出的名称，并给出准确的操作定义。

英文方法句：
> The physics-informed neural network enforces the specified linear mass-balance equations through a fixed output constraint layer during both training and inference.

依据：[术语库§0及PINN条目](../../references/engineering-application-terminology-bank.md)、[P59/P60版本与来源记录](../../references/published-evidence.md)。

**B. 训练内约束与训练后修正**
**甲的方法句：**
> During training, the network minimizes \(\|P(\hat y)-y\|^2\) with gradients propagated through the fixed differentiable operator \(P\), which is also applied at inference.

**乙的方法句：**
> The network is trained by minimizing \(\|\hat y-y\|^2\), and the fixed operator \(P\) is applied only to predictions made after training.

**甲的贡献表述：**
> We incorporate \(P\) into the training objective so that predictor updates account for errors in the corrected outputs used at deployment.

无可训练参数不等于无梯度作用。令 \(\hat y=f_\theta(x)\)，则
\[
\nabla_\theta L_{\甲}=2J_f^\top J_P^\top(P(\hat y)-y),\qquad
\nabla_\theta L_{\乙}=2J_f^\top(\hat y-y).
\]
甲的训练包含\(P\)的作用，乙没有，不能据“固定参数”断言训练等价；也不据此声称甲性能更好。`then`本身没有问题，但不能把**训练目标**写成**部署预测链中的下一模块**，这里用 *During training / At inference* 区分即可。

依据：[专题规则§6](../../references/topic-playbooks.md)、[术语润色companion](../../skills/engineering-terminology-polishing/SKILL.md)。

**C. 数值与物理约束**
第一句话错误。报告点对应
\[
(y_1,y_2)=(80,2),\qquad y_1+y_2=82\ne10,
\]
物料衡算残差为\(82-10=72\)。现有约束确实保证\(z_1+z_2=1\)，但正确的物料衡算约束应为
\[
100z_1+10z_2=10,\quad\text{等价于 }10z_1+z_2=1.
\]

第二个模型的物理坐标欧氏投影为
\[
y^*=(20,3)-\frac{20+3-10}{1^2+1^2}(1,1)
=(13.5,-3.5).
\]
它是该等式集合上的唯一最近点，且\(13.5-3.5=10\)；但第二路为负，**仅凭此等式投影不能保证物料流非负**。

两句英文：
> The normalization enforces \(z_1+z_2=1\), whereas mass conservation under the specified output scaling requires \(100z_1+10z_2=10\).

> The Euclidean projection yields \((13.5,-3.5)\), which exactly satisfies the total-flow equality while violating nonnegativity of the second flow.

依据：[物理约束与坐标核查](../../references/experiment-evidence-design.md)、[严谨性审阅companion§7](../../skills/engineering-journal-rigor-review/SKILL.md)。

**D. 五步非凸KKT迭代**
最关键的是请作者核对**实际优化目标和距离坐标、完整约束、第五步输出的约束/KKT残差及容差、未收敛时的处理**；“全局最近”还需相应最优性证明，“精度最高”还需明确指标、比较对象和实际比较结果。这些是审阅要求，不是启动实验的授权。

- **可行性：尚不能保证。** 固定五步只确认计算预算，不能确认收敛或返回点满足约束。
- **距离最优性：尚不能保证。** 非凸问题即使精确解出KKT方程，一般也不能仅据此认证局部最小，更不能认证全局最近点。
- **预测准确率：没有依据支持“最高”。** 可行性及距原预测最近，都不等于距真实目标最近。

简洁英文替换稿：
> The network prediction initializes a Newton-type solver for the KKT equations, and the output after five iterations is used as the corrected prediction.

若另有**满行秩线性等式下的解析欧氏投影证明**，应保留其假设范围内的等式可行性和唯一全局最近点保证；这不自动扩展为非负性或预测准确率保证。

依据：[约束证据边界](../../references/experiment-evidence-design.md)、[P59解析条件与P60 v2非凸范围记录](../../references/published-evidence.md)。四项均按[主Skill](../../SKILL.md)及[论证与行文规则](../../references/argument-and-prose-craft.md)限定主张与正文措辞。
