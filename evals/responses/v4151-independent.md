# Fictional Causal-Time Final Response

One fresh task context handled the same two requests on the final frozen source; only the read root changed. The prior response was already scientifically correct. The new record changes evidence availability, not a demonstrated general writing gain. Wrapper, local-reference links/line suffixes and whitespace only are normalized; raw records remain private.

本次是同一上下文中的两项请求，不是两次独立模型实验。已有预置历史摘要，不能声称“记忆空白”；本轮未检索历史记录，也不能提供完整内部服务轨迹。

**A**

方法句（28词）：

> A causal convolution combines the current input with twice the input two time steps earlier; its final valid output from the window ending at T supplies the regressor.

作者核查：

- **实际索引与系数。** \(z_t\)读取\(\{x_{t-2},x_t\}\)。展开后：
  \[
  q_t=\frac{(x_{t-1}+2x_{t-3})+(x_t+2x_{t-2})+(x_{t+1}+2x_{t-1})}{3}
  =\frac23x_{t-3}+\frac23x_{t-2}+x_{t-1}+\frac13x_t+\frac13x_{t+1}.
  \]
  因此实际索引为\(\{t-3,t-2,t-1,t,t+1\}\)，对应系数为\(\{2/3,2/3,1,1/3,1/3\}\)。展开以所需索引均有效为前提，不补造边界值。
- **层与整条路径。** \(z_t\)不读取\(t\)之后的输入，符合包含当前位置的时间因果滤波；\(q_t\)则明确依赖\(x_{t+1}\)。第一层的名称不能保证后续路径仍逐点因果。\(i=0\)的当前输入并不违规；“严格只用过去”需要另行规定滞后及目标对齐。
- **间隔与物理因果。** dilation=2改变模型网格上的抽头间距，不等于降低采集频率。若原始采样间隔为\(\Delta\)，这里两抽头相隔\(2\Delta\)，并未规定采样间隔改为\(2\Delta\)。这种信息访问限制也不证明物理因果或干预效应。
- **端点与即时输出。** 截至\(T\)的完整窗口用于端点回归，不会仅因内部采用全窗口注意力或双向编码就必然泄漏未来：对内部位置较晚、但不超过\(T\)的信息，在端点已可用。不过，这不证明内部各位置都满足即时输出条件。对于明确要求在每个\(t\)零延迟输出的任务，原式\(q_t\)与要求冲突，因为非零项\(\frac13x_{t+1}\)尚不可用；必须直接指出冲突，不能偷偷改成后向平均、预测未来值或删项。
- **当前词库状态。** [英文准入记录](../../references/engineering-application-terminology-bank.md)已有P81 p.3 III-B/Eq.(1)与P82 p.3 §3.1/Fig.3的配对，不是普通convolution或因果图题名替代。 [中文核查记录](../../references/engineering-application-terminology-bank_CN.md)列有《自动化学报》c230634原始双语摘要及图2图注、《电工技术学报》2022年第3.1.2节，支持“causal convolution／因果卷积”。[访问限制记录](../../references/published-evidence.md)注明前者HTML缺公式正文、PDF下载未完成，后者公式为图片。本轮仅核对库内记录，未重读原论文或在线复核。
- **命名边界。** 保留准确的常规描述或作者批准的新名；基础词完成核查，不使完整的Temporal-Causal Fusion等限定名称自动成为通用术语。

**B**

摘要（104词）：

> WindowCausalRUL estimates equipment remaining useful life from a sensor history window ending at the decision time. The model uses causal convolution to encode current and preceding temporal positions within that window. Temporal attention then aggregates the encoded positions throughout the available window, converting the sequence of temporal features into a summary for regression. The regressor uses this summary to estimate remaining useful life at the window endpoint. Evaluation uses two held-out equipment cases and identical training settings for the full model and its control. In both cases, WindowCausalRUL achieves lower root mean square error than a control using the same encoder without temporal attention.

贡献候选（35词）：

> WindowCausalRUL links causal temporal encoding with attention over an available history window for endpoint RUL regression, achieving lower RMSE than the same encoder without temporal attention in two held-out equipment cases under identical training settings.

作者说明：

- 输入可记为\(X\in\mathbb R^{L\times p}\)，行对应\(t=T-L+1,\ldots,T\)，列对应传感器；编码后的有效位置经注意力汇总，再回归标量\(\widehat{\mathrm{RUL}}_T\)。隐藏维数、padding及编码输出长度未给，不擅定。
- 全部输入在\(T\)已可用，因此窗口内部不加三角mask不构成题设中的未来泄漏；这也不意味着模型能够为每个内部时刻提前给出预测。训练及归一化仅用训练数据，按题设保留。
- 贡献候选强调组合路径及给定比较，不宣称普通卷积本身是新发明。保留作者批准的WindowCausalRUL，不擅造中文全名；独立新颖性未核查。
- 结果仅支持两个留出设备案例中的RMSE比较，不升级为显著性、跨厂、低延迟、物理因果或部署结论。本轮未核验代码、数据或实验记录。词数按空白分词，连字符词计一词，仅用于此次练习。
