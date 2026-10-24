# Fictional Causal-Time Baseline

One task context handled two requests on the immutable v4.1.50 release. Its scientific judgments already passed and it correctly reported the incomplete base-name ledger. No baseline scientific failure or controlled general writing gain is claimed. Wrapper, links and whitespace only are normalized; raw records remain private.

**A**

英文方法句（30词）：

> The temporal convolution combines the current observation with twice the observation two steps earlier to form z_t; its final valid output z_T supplies the regression input at the window endpoint.

中文作者核查：

- **实际索引与系数**：\(z_t\) 读取 \(\{x_{t-2},x_t\}\)，对应系数为 \(2,1\)。展开后：
\[
q_t=\frac23x_{t-3}+\frac23x_{t-2}+x_{t-1}+\frac13x_t+\frac13x_{t+1}.
\]
因此，\(q_t\) 的实际输入索引为 \(\{t-3,t-2,t-1,t,t+1\}\)，不能仅凭第一层名称认定整条路径只读取过去。

- **层、整条路径与当前输入**：原式 \(z_t\) 不读取晚于 \(t\) 的输入；\(i=0\) 对应的当前输入允许使用，“不读取未来”不等于“严格只读取过去”。后续层可扩大最终输出的依赖范围，\(q_t\) 已明确依赖 \(x_{t+1}\)。

- **时间间隔与物理因果**：dilation \(=2\) 表示卷积抽头相隔两个输入位置。若原始等间隔为 \(\Delta\)，抽头间隔为 \(2\Delta\)，不表示采集频率减半，也不自动改变输出步长。时间访问约束不证明物理因果；物理因果主张需要相应识别假设与证据。

- **端点回归**：原式 \(z_T\) 只依赖 \(x_T,x_{T-2}\)。若实际加入全窗口注意力或双向编码，须重新追踪依赖，不能仍套用原式的支持范围；但只要输入均在 \(T\) 已可用、仅预测 \(T\) 处目标，内部位置访问其后但不晚于 \(T\) 的位置，并不必然泄漏端点未来。这不使需要 \(x_{T+1}\) 的 \(q_T\) 在 \(T\) 可得。

- **即时逐点任务**：原式 \(q_t\) 与“每个 \(t\) 即时输出且不允许延迟”冲突，因为 \(x_{t+1}\) 尚不可用。应明确报告公式与任务要求不相容，交由作者确认模型修改；不能偷偷改为后向平均、补造未来输入或把延迟输出写成即时输出。

- **词库状态**：本包英文词库、中文对应词库及公开证据索引中，未找到完成的 `causal convolution` 英文双来源定义配对，也未找到该词带原始中文来源及定位的完成核查记录。[现有判据](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/ccfad9dac559f27f9c7c25a09685ad2974b74b32/references/terminology-decisions.md#L152)提供概念区分，不等于完成准入。不能用普通 convolution、因果图或单篇专名补足；未完成也不等于术语无效。保留准确常规描述和作者批准新名，但 `Temporal-Causal Fusion` 等完整限定名不能因基础词已核验而自动通用化，见[名称准入规则](https://github.com/MagicTK/engineering-application-journal-writing-skill/blob/ccfad9dac559f27f9c7c25a09685ad2974b74b32/references/engineering-application-terminology-bank.md#L18)。

**B**

英文摘要（102词）：

> WindowCausalRUL estimates equipment remaining useful life (RUL) from a sensor history window ending at the prediction time. Its causal temporal convolutional encoder combines measurements at each position with preceding observations to produce a sequence of temporal features. Temporal attention uses all encoded positions within the available window to form a summary of the sensor history. A regressor maps this summary to a single RUL estimate at the window endpoint, when all window measurements are available. In two held-out equipment cases, WindowCausalRUL yields lower root mean square error than a control using the same encoder without temporal attention under the same training settings.

英文贡献候选（35词）：

> WindowCausalRUL combines causal temporal encoding with attention over the available sensor window for endpoint RUL regression, yielding lower RMSE than the same encoder without temporal attention in two held-out equipment cases under identical training settings.

中文作者说明：

- **索引与维度**：按“时间×传感器”记 \(X_T\in\mathbb R^{L\times C}\)，第 \(j\) 行对应 \(T-L+j\)，\(j=1,\ldots,L\)。编码后的有效长度、隐藏维、padding/stride 未给定，不假定形状不变；注意力汇总后，回归器输出 \(T\) 处的标量 RUL。
- **时间与命名**：全部窗口测量在 \(T\) 已可用，内部不加三角 mask 不构成该端点任务的未来信息违规，但不能据此声称每个内部时刻均能即时预测。保留作者批准的 `WindowCausalRUL`，不补中文全名；causal 仅描述卷积的时间访问约束。
- **证据边界**：训练及归一化仅用训练数据按题设接受。比较只支持两个给定留出设备案例中的较低 RMSE，不扩展为统计显著、低延迟、跨厂能力、物理因果或现场部署，也不把普通卷积单列为发明；整体新颖性未经文献核查。

字数按空白分词，仅适用于本次合成练习。本轮未读取评测、既往回答、私有审计、实际论文或其他项目，未作文件修改、安装、浏览、实验、发布或代理调用。上下文已有预置历史，不能声称记忆空白；以上也不是完整内部服务轨迹。
