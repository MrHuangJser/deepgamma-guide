# 做市商分析主线：从数据、持仓到对冲与价格验证

核验日期：2026-10-29。本篇把分散的指标串成学习与研究流程；排序、配置组合和数字算例是研究者设计，不是官方交易系统或胜率排名。若主要研究 SPX／ES 日内行情，建议先读本篇，再查各指标参数。

## 1. 做市商视角为什么值得优先学习

期权成交量告诉你活动规模；参与者分类有助于区分谁在买卖；带符号头寸与 Greeks 则帮助分析这些活动如何影响风险。做市商若调整对冲，可能给标的带来买卖需求。分析价值来自这条机制链，不能由“MM”“Advanced”这样的名称推导预测优势。

Cboe 的研究强调买卖净额、Gamma 的符号与规模，并指出大量交易可以相互抵消。因此，学习重点应是净风险及其变化，而不是寻找最大的成交数字。[Cboe：SPX 0DTE 与做市商对冲研究](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)

对于期权组合交易，还需要研究 IV、期限结构、Theta、执行价格与结算制度；做市商指标并不能独自回答某张期权是否便宜。相关基础见[期权与期货基础](../research/market-foundations.md)。

## 2. 一条不能跳步的数据链

| 层次 | 能提供的信息 | 在 DeepGamma 中如何辨认 | 不能直接推出什么 |
|---|---|---|---|
| 参与者分类活动 | 某类主体的买卖与交易量 | 官方称基于 CBOE 数据的 MM 流量源 | 该主体完整跨市场持仓、最终交易意图 |
| 头寸与风险聚合 | 净数量、Delta、Gamma，受期限和结转范围影响 | GEX／DEX MM、OI-R 等不同源 | 已发生的期货成交 |
| 平台派生结果 | 压力序列、环境分类、放大／衰减类别 | Pressure、Sentiment、Hedging | 校准后的上涨概率或确定执行数量 |
| 实际市场反应 | 价格是否突破、成交是否延续、流动性是否变化 | 结合对应执行市场的价格与订单流观察 | 这些交易一定由某个做市商发起 |

官方把 GEX Profile 的 MM 源描述为真实做市商数据，同时提供净额、C/P、DEX、净流及 OI-R 模式。模式之间统计对象不同，不能仅因都来自 CBOE 就互换。[官方 GEX Profile 数据源](https://www.deepcharts.com/helpcenter/deepgamma-web/article/option-gex-profile-deepgamma-web)

**来源真实与计算完整是两个问题。** 公开资料未充分披露 DeepGamma 使用的具体数据产品、初始库存、完整单位及净额流程。Cboe 自身可获取的交易信息，也不能直接等同某个供应商获授权接收的全部字段。关于公开数据文件能确认什么，见[本次来源复核](../research/market-maker-source-review.md)。

## 3. 必须分开的四种量

| 类型 | 所回答的问题 | 相关工具 | 使用时最关键的区别 |
|---|---|---|---|
| 期间交易净流 | 这段时间增加或减少了什么活动？ | Delta 的 MM 源、Market Maker Net Flow | 日内净买入可能是在平此前空仓 |
| 当前范围内的风险 | 所选头寸在当前估值下有多少 Delta／Gamma？ | GEX Profile、Summary Gex 的对应源 | Carry、期限及估值时点影响含义，未必覆盖全簿 |
| 条件对冲需求 | 若价格变化或新增交易被中性化，目标对冲如何变化？ | Hedging，以及对 GEX／DEX 的机制解释 | 目标头寸与待执行订单不同 |
| 实际执行流 | 市场中真正成交了多少？ | 对应期货／现货市场的成交数据 | DeepGamma 的 MM 风险读数不能代替它 |

Pressure 是单独的派生压力序列。官方将其类比为期权数据构造的累计指标，但没有给出可与 DEX 或 Net Flow 直接相等的公式。[官方 Pressure 说明](https://www.deepcharts.com/helpcenter/deepgamma-web/article/option-market-maker-pressure-deepgamma-web)

### 算例：净买入与负 Gamma 可以同时存在

仅考虑同一普通 Call 期权系列，假设开盘做市商净空 100 张，随后买入 30 张、卖出 10 张，忽略到期、行权与其他调整：

```text
日内净数量变化 = +30 - 10 = +20 张
当前净头寸     = -100 + 20 = -80 张
```

日内活动偏买，当前头寸仍为净空。以正的长仓单位 Gamma 加权，日内买卖贡献可以为正，含初始库存的当前 Gamma 仍可为负。若这段交易的 Call Delta 近似不变，净 Delta 流也可以为正；因此正的 MM 净流不必与负的风险汇总矛盾。上述库存恒等式不是 DeepGamma 的 Carry 或 OI-R 公式。

同理，`0DTE` 只说明今天到期，不说明今天才开仓，不能因此自动忽略隔夜结转。[0DTE 与持仓基础](../research/market-foundations.md)

### 算例：目标对冲已经持有，就不需要再下一遍单

假设期权簿 Delta 为 −1,000 美元／SPX 点，ES 每点 50 美元，所选月份满足局部近似 `dF/dS≈1`。只用 ES 对冲时，目标为多 20 张。若已有多 20 张，当前新增需求为零；若已有多 15 张，才需要补买约 5 张。

若组合 Gamma 为 +200 美元／点²，SPX 再涨 1 点、其他输入暂不变，期权 Delta 变为约 −800，目标转为多 16 张。从已有多 20 张出发，调整是卖 4 张。由此可以同时出现“期权 Delta 为负、期货仍净多、最新调整为卖出”。规格与单位推导见[Summary Gex 算例](12-option-summary-gex.md)。

这是教学账本，平台显示的 M、Contracts 或 Premium 不能未经单位确认直接代入。

## 4. 先学哪些指标，怎样配置

以下是学习顺序。初期同时启用前两组即可，掌握后再增加其余组件；多个同源指标一致不会增加独立样本数。

| 顺序 | 组件与建议配置 | 本阶段要学会什么 |
|---|---|---|
| 1：环境 | Summary Gex 选择 Gex (Market Maker)，明确 0DTE，手动记录 Carry | 读符号、大小、变化，区别负值收敛与转正 |
| 2：位置 | GEX Profile 同源、同期限、同 Carry；先显示 1 个 Profile | 把总量拆到行权价；必要时另开 C/P 模式查看抵消 |
| 3：局部反应 | 添加 Hedging Profile，保留 Amplifying／Attenuating／Neutral | 把颜色解释为对既有价格方向的条件反应 |
| 4：盘中路径 | Web 加 Pressure：独立副图、EMA15、第二均线先关 | 分开记录零轴位置、斜率、相对均线位置 |
| 5：状态摘要 | Web 加 Sentiment，Regime 与 Direction 分别用 Strip | 分清 Gamma 环境、方向类别、波幅提示与空白 |
| 6：复核工具 | 需要时选 Heatmap、Levels Advanced 或 Delta MM 源 | 分别补时间轨迹、少量参考位或新增活动信息 |

参数逐项见 [Summary Gex](12-option-summary-gex.md)、[GEX Profile](05-option-gex-profile.md)、[Hedging](06-option-gex-profile-hedging.md)、[Pressure](web-market-maker-pressure.md)、[Sentiment](web-market-maker-sentiment.md)及[Web 配置差异](../research/web-desktop-differences.md)。

**必须对齐的是有公开控件的实例。** 不能假定 Pressure、Sentiment、Hedging 都继承了同一个 0DTE／Carry 范围；它们的公开专页没有给出足够信息来确认完整继承关系。没有字段时记录“模型范围未公开”，不要为了凑齐一致性自行补造设置。

同时保留一个 All expirations 的背景图有助于跨期观察；0DTE 属于 All 的一部分，不是两份独立证据。Advanced Envelopes 的默认是 OI-R 加权模式，也不应仅凭 Advanced 名称列入 MM 净 Gamma 组。

## 5. Gamma 的变化为何不等于新开仓

组合风险不仅由数量决定，还由每张合约当时的敏感度决定。OIC 说明 Gamma 会随价格和剩余期限变化，临近到期的平值区域尤其敏感。[OIC：Gamma](https://www.optionseducation.org/advancedconcepts/gamma)

下面是忽略乘数的教学算例：同一参与者持有 100 张，单位 Gamma 从 0.010 变成 0.015，即使没有新交易，总 Gamma 也从 1.0 变成 1.5。反之，新买入正 Gamma 合约，也可能不足以抵消其他头寸的负 Gamma 或估值变化。

这对两个常见操作有直接影响：

- **Rolling 截面相减**：可以记录风险变动，但不能把差值全部称为新开仓。
- **累计 Net MM x gamma**：首先是交易流按 Greek 加权的累计口径；没有起始持仓、历史头寸当前重估等信息，不能直接当成 Summary Gex 的当前净 Gamma。官方 Delta 专页定义了加权模式，但未充分解释历史权重是否重估。[官方 Delta 数据模式](https://www.deepcharts.com/helpcenter/deepgamma-web/article/option-delta-deepgamma-web)

对冲变化还可能受到 IV、时间及新增持仓影响。这里是通用风险分析，不意味着 Hedging／Pressure 已经公开输出了 Vanna 或 Charm。

## 6. 指标冲突时，先定位冲突属于哪一层

| 看到的组合 | 可能成立的解释 | 下一步应检查什么 |
|---|---|---|
| Summary 为正，现价附近有负 GEX 档 | 总体净额与局部贡献不同 | 负档规模、距离、期限；不要把总体符号贴给每个档 |
| 0DTE 为负，All 为正 | 较远期限的正贡献抵消了当日负贡献 | 同时间、同源、同 Carry；不要对嵌套范围多数表决 |
| MM 净流为正，含结转 GEX 仍负 | 买入可能只减少原有空仓；流与存量不同 | 初始库存与 Carry，另查 Greeks 是否变动 |
| Pressure 上升，Sentiment Direction 向下或空白 | 连续序列与分类状态定义不同 | 数值时点、更新、显示状态；内部模型未公开时不强行解释 |
| Summary 为正，局部 Hedging 放大 | 聚合范围不同，模型也可能使用不同风险因素 | 先排设置与时间差，不能仅凭两者颜色认定数据错误 |
| 热图色块消失，但 Profile 还有该档 | 归一化、Cutoff 或显示范围造成过滤 | 查看绝对读数和显示配置，不能直接判为全部平仓 |

**无法解释的差异可以保留为未知。** 记录原始读数比编造“主力诱多”更有用。逐项说明见[热图](14-option-gex-heatmap.md)与[组合排错](15-workflows-and-risk.md)。

行权价剖面还要与假设价格扫描区分：在当前现价下，6000 行权价的 Gamma 贡献，不等于“当现价变成 6000 时整个组合的 Gamma”。所以不能从两根正负柱之间直接画出全市场 Zero Gamma；涉及全簿场景再定价与求根的细节，产品未公开就保持未知。[Zero Gamma 的数学边界](../research/market-foundations.md)

## 7. 一个完整的观察例子

以下数字仅为教学，不设置通用阈值。

| 时间 | 当时可见事实 | 可记录的假说与处理 |
|---|---|---|
| 09:45 | SPX 5995；同口径 Summary 为负；6000 附近 Hedging 为放大；Pressure 仍在零下但抬升 | 上行若发生，可能处于放大环境；尚未形成突破，负 Pressure 余额也不等于最近正在恶化 |
| 09:50 | 价格到 6003；Pressure 最新数据继续抬升 | 可登记上行延续候选；若研究 ES，先核同步基差，不把 SPX 6000 直接当 ES 下单价 |
| 09:55 | 价格回到 5997；Pressure 新读数转为下降 | 原突破解释减弱；保留失败样本，不因仍负 Gamma 就宣称“必然再次上涨” |
| 10:00 | Sentiment 方向为空白 | 记录缺少分类支持；不沿用上一条 Up，也不把空白记为 Down |

“突破后站稳”的判定、观察时间和失效价必须在看后续行情前写下。价格确认来自市场行为，不是要求五个同源图标同时变绿。正 Gamma 环境同样可能被更强的外部流突破；相同 Gamma 规模在不同流动性下也未必造成相同价格影响。单位和时段不明时，不把 GEX 数字直接除以 ES 成交量来计算所谓对冲占比。

## 8. 做市商专题复盘记录

在[通用复盘表](15-workflows-and-risk.md)上补充以下字段即可：

```text
数据身份：客户／MM；直接分类源／取反展示／平台派生
统计类型：逐柱流／累计流／当前风险截面／分类状态
范围：期限、Carry、行权价；未公开的继承关系单列
实际数值：符号、绝对大小、最近增量；不只记颜色
对冲解释：目标头寸还是增量；既有对冲是否未知
同步情况：每个读数的数据时间；执行标的与合约月份
冲突：全局vs局部、存量vs流量，或尚未解释
验证：原假说、事先写下的确认/失效条件、后续结果
```

研究指标是否有用时，应比较同一套价格规则“加入 MM 条件前后”的样本表现，记录收益以外的回撤、错过的机会、费用与滑点；同时保留没有触发和判断失败的时段。公开说明与演示截图不足以得出某指标更准或增加几个指标就有更高胜率的结论。
