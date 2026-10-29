# DeepGamma 所需的期权与期货基础：经一手资料核验的研究底稿

核验日期：2026-10-29（Asia/Shanghai）。本文件是为 DeepGamma 使用指南提供的市场知识底稿，并不声称下列通用公式就是 DeepGamma 的内部实现。产品公式、数据时效、交易商持仓推断、颜色含义及筛选范围须由 DeepGamma 自己的文档另行确认。文中的价格、数量、波动率和交易过程除特别标明外均为教学假设，不是历史业绩、实时行情或收益承诺。

## 1. 从期权合约到 Greeks

### 1.1 Call、Put、买方、卖方是两组不同概念

Call 是看涨期权，Put 是看跌期权；买入或卖出决定持仓方向。不能把“Call=多头持仓”“Put=空头持仓”当成定义。对于普通香草期权，买入 Call 的 Delta 为正，买入 Put 的 Delta 为负，卖出持仓的方向则反转。Delta 描述期权理论价格对标的微小变动的敏感度，不是该交易一定盈利的概率。[OIC：Delta](https://www.optionseducation.org/advancedconcepts/delta)

| 普通香草期权持仓 | Delta 方向 | Gamma 方向 | 标的上涨时的主要局部影响 |
| --- | --- | --- | --- |
| 买入 Call | 正 | 正 | 期权价值通常上升，Delta 通常变得更正 |
| 卖出 Call | 负 | 负 | 负 Delta 通常扩大，卖方风险增加 |
| 买入 Put | 负 | 正 | 期权价值通常下降，Delta 向零靠近 |
| 卖出 Put | 正 | 负 | 正 Delta 通常缩小 |

Gamma 的正负来自期权持仓方向。OIC 明确指出普通买入 Call 和买入 Put 均为正 Gamma，卖出 Call 和卖出 Put 均为负 Gamma。[OIC：Gamma](https://www.optionseducation.org/advancedconcepts/gamma)

### 1.2 用同一套单位理解 Delta、Gamma

令期权报价为 `V`，标的价格或指数点位为 `S`：

```text
Delta = ∂V/∂S
Gamma = ∂Delta/∂S = ∂²V/∂S²
ΔDelta ≈ Gamma × ΔS
ΔV ≈ Delta × ΔS + 0.5 × Gamma × (ΔS)²
```

这些是数学定义和局部 Taylor 近似，适用于小幅移动、其他输入暂时不变的教学分析。它们没有把未来的 IV、时间、利率、分红或跳跃价格变化算成已知。OIC 对 Greeks 的定位也是理论估计，而非实际报价保证。[OIC：Understanding Options Greeks](https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks)

**自拟例子**：某指数 Call 报价为 15.00 点，Delta=0.50，Gamma=0.004/指数点。若指数上涨 10 点，局部近似为：

```text
新 Delta ≈ 0.50 + 0.004 × 10 = 0.54
期权报价变化 ≈ 0.50 × 10 + 0.5 × 0.004 × 100 = 5.20 点
```

若合约乘数为每报价点 100 美元，单张期权约增加 520 美元。这里的 `Gamma=0.004` 不是“标的每上涨 1%，Delta 上升 0.004”，而是“标的每上涨 1 个指数点，Delta 上升约 0.004”。把点数、百分比及美元混用会让 GEX 放大或缩小几个数量级。

### 1.3 为什么到期附近、平值附近更敏感

对于普通香草期权，Gamma 往往集中在接近到期的平值区域；远虚值和深实值期权的 Delta 更靠近边界，局部 Gamma 较低。Gamma 会随标的移动而改变，不能把当前 Gamma 外推到很远的价格。[OIC：Gamma](https://www.optionseducation.org/advancedconcepts/gamma)

**使用含义（由上述原理推导）**：一个看似很窄的高 Gamma 行权价区，在价格接近时可能变得重要；但价格远离后，该区影响可以降低。比较两个 Gamma 峰时应固定标的、到期范围、时间和单位。单看峰高无法回答价格下一步朝哪个方向走。

## 2. 做市商 Delta 对冲：必须满足哪些条件

### 2.1 正 Gamma、负 Gamma的条件性机制

Cboe 的解释是：净正 Gamma 的做市商若用期货维持 Delta 中性，标的上涨时通常卖出对冲、下跌时通常买入对冲；净负 Gamma 时则相反，可能形成顺势对冲。这是对冲流可能抑制或放大波动的机制，而不是市场必然均值回归或必然突破的定律。[Cboe：Much Ado About 0DTEs，2023-09-08](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)

**自拟推导**：设期权组合的标的等价 Delta 为 `D`，对冲头寸为 `H=-D`，组合 Gamma 为 `G`：

```text
ΔH ≈ -G × ΔS
```

因此：

| 已知条件 | 标的上涨 | 标的下跌 |
| --- | --- | --- |
| 交易商期权组合 G > 0 且持续 Delta 对冲 | 增加卖出对冲 | 增加买入对冲 |
| 交易商期权组合 G < 0 且持续 Delta 对冲 | 增加买入对冲 | 增加卖出对冲 |

使用这张表前，必须确实知道 `G` 是谁的净持仓、是否覆盖相关对冲工具、是否使用相同符号。仅知道市场存在大量期权不足以套用它。

### 2.2 为什么高期权成交量不等于大额对冲需求

Cboe 指出，成交总量和对冲风险之间并非等号关系；客户买入和卖出可以相互抵消。其研究之所以比公开链条推断更接近真实头寸，是因为交易所能识别交易身份、买卖及开平。该研究也说明交易商可能在别的到期日、SPY、E-mini 等产品上有抵消持仓。[Cboe：同上](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)

**使用含义（综合推断）**：看到“总 Gamma 很大”“某行权价成交十万张”时，先检查它是绝对量、带符号净量、客户量、交易商量还是由 OI 建模得到的代理量。没有这些信息，最多把它当成风险集中区，不能写成“做市商必须买入多少手期货”。

### 2.3 对冲机制的边界

以下是分析条件，不是已验证的 DeepGamma 行为：

- 交易商可采用阈值或离散对冲，真实流并非每次价格变化都立即出现。
- 持仓可在跨期、跨行权价、跨产品之间抵消。单一看涨/看跌链不是整个组合。
- 同时发生的现货资金流、宏观信息、流动性变化和波动率变动可能盖过 Gamma 对冲。
- 正 Gamma 环境仍可出现趋势；负 Gamma 环境也可出现盘整。Gamma 是条件变量，不是单独交易信号。

这些限制与期权模型的共同边界一致：理论价格取决于输入假设，实际成交价由市场决定。[OIC：Black-Scholes Formula](https://prd-web.optionseducation.org/advancedconcepts/black-scholes-formula)

## 3. GEX 的单位、符号和估算边界

### 3.1 一个可核算的通用定义，不冒充产品公式

设某期权 `i` 的长仓单位 Gamma 为 `Γᵢ`，合约乘数为 `mᵢ`，带符号净张数为 `qᵢ`（多头正、空头负）：

```text
组合 Gamma = Σ qᵢ × mᵢ × Γᵢ
```

如果 `S` 是指数点数、`V` 是期权报价点数、`m` 是美元/报价点，则组合 Gamma 的单位为“美元/指数点²”。指数上涨 `ΔS` 时，组合美元 Delta 对标的点数的敏感度约变化 `组合Gamma × ΔS`。

市场展示常将其进一步换算为“标的移动 1% 时的 Delta 对冲名义金额变化”：

```text
Dollar GEX for 1% move ≈ Σ qᵢ × mᵢ × Γᵢ × S² × 0.01
```

这一步额外乘一个 `S`，是把 Delta 等价数量换成标的名义金额；`0.01S` 是假设的 1% 价格变动。该公式是单位分析推导，并非 DeepGamma 的官方口径。Cboe 将市场做市商净 Gamma 解释为 SPX 移动 1% 时可能需要调整的对冲规模，为这种口径提供了交易含义背景。[Cboe：做市商 Gamma 分析](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)

**自拟算例**：`S=6000`，`Γ=0.001/点`，`m=100美元/点`，假设已知某主体净多 `q=1000张`：

```text
组合 Gamma = 1000 × 100 × 0.001 = 100 美元/点²
标的涨 1% = 60 点
美元 Delta 敏感度变化 ≈ 100 × 60 = 6000 美元/点
按 S=6000 换算的对冲名义量变化 ≈ 6000 × 6000 = 3600万美元
```

这个“3600万美元”不是期权权利金，不是该主体已经成交的期货金额，也不是固定未来买卖单。若用每点 50 美元的 ES 粗略对冲上述 Delta 变化，在 `dF/dS≈1` 的假设下，变化量约为 `6000/50=120手ES`。只用于解释单位，真实执行需考虑基差、组合其他风险与对冲工具。

### 3.2 Call GEX 为正、Put GEX 为负可能是模型约定

有些外部模型给 Call、Put 分别设置正负符号，用 OI 作为头寸规模近似。这样得到的是带假设的暴露代理，而不是由“Put 的 Gamma 天生为负”得来的结论。普通买入 Put 的 Gamma 与普通买入 Call 一样为正。[OIC：Gamma](https://www.optionseducation.org/advancedconcepts/gamma)

因此检查一个 GEX 工具，至少应知道：

| 要核对的项目 | 为什么影响解读 |
| --- | --- |
| 展示主体 | 客户净头寸与交易商净头寸方向可能相反 |
| 多空符号来源 | 来自真实净持仓、逐笔分类、经验假设还是仅按 Call/Put 分类 |
| 张数输入 | 昨日 OI、当日累计成交量或估算净流量的意义不同 |
| Gamma 单位 | 每点、每美元、每 1% 或合约级会影响数值 |
| 到期范围 | 只看 0DTE 与全到期聚合可以得出不同结论 |
| 场景再定价 | 曲线是否随假设价格、IV、剩余时间重新计算 |

### 3.3 Gamma Flip/Zero Gamma 是条件化的模型交点

若对每个假设价格 `S*` 重算 Gamma，再加总得到 `G(S*)`，某个 `G(S*)=0` 的价格可称为该模型、该持仓范围下的零 Gamma 交点。它不必等于当前价格下按行权价分组柱子的正负分界。

这是数学解释，不能据此认定任何产品的“Gamma Flip”具体公式。若模型换了 IV 曲面、到期范围、OI 日期或持仓符号，交点可能移动、消失或出现多个。产品若未公开计算法，应在指南里标明“名称已确认，精确算法未公开”。

## 4. OI、成交量和 0DTE

### 4.1 Open Interest 是存量，Volume 是期间流量

OI 是一个期权系列尚未平掉的合约数。一份未平仓合约同时对应多头与空头，不能把 OI 自身解释成方向。OCC 只有在收盘后的清算配对后，才能报告新的 OI。双方同时开仓，OI 增一；一方开一方平，OI 不变；双方同时平仓，OI 减一。[OIC：General Information](https://www.optionseducation.org/referencelibrary/faq/general-information)

| 一笔 1 张交易 | 当日成交量变化 | OI 变化 |
| --- | --- | --- |
| 买方开仓、卖方开仓 | +1 | +1 |
| 买方开仓、卖方平仓 | +1 | 0 |
| 买方平仓、卖方开仓 | +1 | 0 |
| 买方平仓、卖方平仓 | +1 | -1 |

**自拟例子**：某行权价早盘 OI=20,000，盘中累计 Volume=50,000。不能计算“新 OI=70,000”；这 50,000 张可能包含大量日内反复换手和平仓，也可能包含价差组合的一个腿。OI 的方向归属与交易商身份仍然未知。

### 4.2 0DTE 是剩余期限，不代表合约今天才新上市

0DTE 指在当个交易日到期的期权；该系列可能在更早已经挂牌。到期附近的平值期权对标的移动敏感，交易者用于短期对冲、事件或日内观点，但剩余反应时间极短。[Cboe：0DTE Trading Resources](https://www.cboe.com/tradable-products/0dte/)

**对 DeepGamma 筛选的意义（推导）**：

1. 只看 0DTE：更接近今天的短期结构，但忽略其他到期日的抵消。
2. 看全到期：覆盖较长持仓结构，但可能掩盖今日临近到期的局部集中。
3. 将两者并排：用于观察“整体环境”与“当日局部结构”是否一致。
4. 用昨日 OI 配合今日 Gamma：是“存量张数 × 当下敏感度”的混合时点估算，不能称为完整盘中真实持仓。

### 4.3 时间价值衰减不等于卖方稳定收入

Theta 是其他条件不变时，期权理论价格随时间流逝的变化；衰减通常不是线性的，不同模型对时间的处理也可能不同。临近到期并不意味着可以将一天的 Theta 均匀除成每分钟再作保证预测。[OIC：Theta](https://www.optionseducation.org/advancedconcepts/theta)

**自拟对照**：假设同一位置指数缓慢上行，买入短期 Call 仍可能因 IV 下跌和时间衰减而亏损。反过来，卖出期权即使起初赚取衰减，一次大幅移动也可使 Gamma 风险占主导。用 DeepGamma 判断标的交易环境，与判断某张期权是否值得买卖，是两个需要连接但不能混同的步骤。

## 5. IV、Vega、偏斜和期限结构

### 5.1 IV 是从期权价格倒推的模型输入

历史波动率来自过去价格，IV 从当前期权价格和定价模型反推，通常以年化百分比表示。不同的行权价、期限可有不同 IV。偏斜反映同一到期日不同位置的隐含波动率差异；它体现定价结构，不能直接等同于真实未来概率。[OIC：Technical Information](https://www.optionseducation.org/referencelibrary/faq/technical-information)

**自拟例子**：某标的同到期平值 IV=20%，下方虚值 Put IV=27%，上方虚值 Call IV=21%。可以说市场为下行期权收取更高波动率定价，不能只凭 27% 判定标的一定下跌。买方的需求、保险溢价和报价差异都可能参与形成这个价格。

### 5.2 Vega 与 Gamma 不同

Vega 衡量 IV 变化对权利金的敏感度。市场通常按 IV 上升一个百分点（例如 20%→21%）给出 Vega；较长期限的期权常有较高 Vega，IV 也能在标的几乎不动时改变。[OIC：Vega](https://www.optionseducation.org/advancedconcepts/vega)

**自拟例子**：期权 Delta=0.40、Vega=0.20报价点/波动率百分点。标的上涨1点贡献约+0.40，但 IV 从25%跌到22%贡献约-0.60，忽略其他项后净变化约-0.20点。对方向判断正确并不自动等于期权盈利。

### 5.3 期限结构需要保持可比口径

期限结构展示不同到期日的 IV，常用平值 IV 作为可比基准。CME 的工具明确展示一年内不同到期的平值波动率，并可与前一周比较。[CME：Volatility Term Structure Tool User Guide](https://www.cmegroup.com/tools-information/quikstrike/quikstrike-volatility-term-structure-tool-user-guide.html)

Cboe 的 SPX 隐含波动率期限结构用于观察不同未来期限的市场定价；其 VIX9D、VIX、VIX3M 等指标对应不同目标期限。VIX 本身不是任意一张期权的 IV，也不是某条 Gamma 曲线。[Cboe：VIX Term Structure](https://www.cboe.com/tradable-products/vix/term-structure)

**自拟场景**：本周存在重要公告，2DTE ATM IV=30%，30DTE=20%。可将其解释为近期风险被更高定价；不能用 30% 与 20% 的差直接说某一张期权“高估10%”。期限越短，少量事件方差对年化 IV 的放大越明显。

在同一时间基准与可加方差的简化假设下，两个期限间的远期方差可作教学计算：

```text
σ_forward² = (σ₂²T₂ - σ₁²T₁)/(T₂-T₁)
```

这是数学推导，不是 DeepGamma 参数公式。若得到负值，首先检查报价、期限单位、交易时间及是否使用一致的平值/远期平值口径，而不是把负方差解释成真实可交易波动率。

### 5.4 用 IV 估计波动量级的局限

在独立同分布、波动率不变等简化假设下：

```text
期间标准差量级 ≈ S × 年化IV × sqrt(T)
```

`T` 必须以与年化方式一致的年数表示。按252交易日口径，`S=6000、IV=20%` 的一日量级约为 `6000×0.20/√252≈75.6点`。这是量级演示；若采用日历日计时、含隔夜时段或0DTE剩余小时，结果会不同。它不是“今天必在上下75.6点内”，也不等同于保证覆盖率；跳跃和尾部风险并未消失。OIC 也将模型定位为条件性理论估值。[OIC：Black-Scholes Formula](https://prd-web.optionseducation.org/advancedconcepts/black-scholes-formula)

## 6. 从 SPX/NDX 期权结构映射到 ES/NQ

### 6.1 指数与期货具有关系，但不是相同价格

SPX 是 S&P 500 现金指数体系，ES/MES 是 CME 的相关期货；NDX 对应 Nasdaq-100 指数体系，NQ/MNQ 是相关期货。CME 明确把股指基差定义为期货价格减现货指数价格，基差受融资成本、分红和剩余期限影响，可能为正也可能为负。[CME：What is Equity Index Basis?](https://www.cmegroup.com/education/courses/introduction-to-equity-index-products/what-is-equity-index-basis)

```text
B(t,到期月) = F(t,到期月) - S(t)
期货观察位 L_F ≈ 指数观察位 L_S + 同步基差 B
```

以上第二式是把同步观察到的价差用于映射的简单推导。它不是跨时段固定常数。必须匹配指数与期货的时间戳、所交易月份、延迟与是否属于现金市场更新时段。

### 6.2 两个映射算例

**SPX→ES 自拟例子**：同一时刻 SPX=6000，所交易的12月 ES=6024，基差=+24。SPX 期权结构位6020可暂时映射为 ES 约6044。若后续基差变成+19，映射位随之约为6039。

**NDX→NQ 自拟例子**：同一时刻 NDX=21000，指定月份NQ=21070，基差=+70。NDX结构位21100约映射为NQ21170。不能因为两个产品都跟踪 Nasdaq-100 就原样使用21100作为NQ价位。

**ETF 的额外边界**：SPY、QQQ 与相应指数存在比例关系，但并非固定、永久不变的精确除数。映射ETF结构时还要考虑分红、跟踪差异、ETF自身期权持仓，不能把“SPY≈SPX/10”或“QQQ≈NDX/40”写成恒等式。

### 6.3 理论公允价解释了基差来源

CME 给出的简化股指期货公允价为：

```text
F_fair = S × [1+r × (天数/360)] - 到期前分红的指数点数
```

实际期货价可围绕理论价格波动，供需和套利参与使其关系并非每秒精确成立。[CME：Calculating Fair Value](https://www.cmegroup.com/trading/equity-index/fairvalue.html)

**自拟例子**：`S=6000、r=4%、30天、预计分红10点`，则 `F_fair≈6000×(1+0.04×30/360)-10=6010`。用该式解释价差来源即可；盘中映射更需要同步实际价格，因为利率、分红预测与供需条件会变。

### 6.4 换月与连续合约

Micro E-mini 按股指期货季度周期挂牌，季度月份为3、6、9、12月。[CME：Micro E-mini Equity Index Futures FAQ](https://www.cmegroup.com/articles/faqs/frequently-asked-questions-micro-e-mini-equity-index-futures.html)

**使用含义（推导）**：换月后新旧期货合约可以有不同基差。同一 SPX/NDX 结构位映射到近月和远月会不同；连续合约若经过回溯调整，历史图表中的绝对点位还可能变化。交易前需要确认所下单合约和图表引用合约一致，不能把一个连续合约图上的历史绝对水平不加核对地用于另一月份。

## 7. ES、MES、NQ、MNQ 合约规格与金额换算

下表针对普通单腿期货报价，不是期权报价或日历价差的最小跳动规则。产品规格可能调整，实际交易仍以交易所和经纪商当前规则为准。

| 合约 | 指数体系 | 每指数点价值 | 普通最小跳动 | 每跳价值 | 与 E-mini 大小关系 |
| --- | --- | ---: | ---: | ---: | --- |
| ES | S&P 500 | 50美元 | 0.25点 | 12.50美元 | 标准 E-mini |
| MES | S&P 500 | 5美元 | 0.25点 | 1.25美元 | ES的1/10 |
| NQ | Nasdaq-100 | 20美元 | 0.25点 | 5美元 | 标准 E-mini |
| MNQ | Nasdaq-100 | 2美元 | 0.25点 | 0.50美元 | NQ的1/10 |

ES 的乘数和跳动根据 CME 规则第358章的官方申报文件核对；NQ 根据 CME 产品规格核对；Micro 合约根据 CME 产品资料卡及FAQ核对。[CME Rulebook 第358章（CFTC保存的交易所申报）](https://www.cftc.gov/sites/default/files/filings/ptc/16/03/ptc030416cmedcm002.pdf)、[CME：NQ规格](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html)、[CME：Micro E-mini产品资料卡](https://www.cmegroup.com/trading/equity-index/files/cme-micro-e-mini-futures-fact-card.pdf)

```text
单笔期货盈亏 ≈ (退出价格 - 进入价格) × 每点价值 × 多头手数
空头持仓方向相反；费用及滑点另计。
名义金额 = 期货价格 × 每点价值 × 手数
```

**自拟金额比较**：

| 假设逆向移动 | 1手ES | 1手MES | 1手NQ | 1手MNQ |
| --- | ---: | ---: | ---: | ---: |
| 10点 | -500美元 | -50美元 | -200美元 | -20美元 |
| 30点 | -1500美元 | -150美元 | -600美元 | -60美元 |

ES和NQ的日常点数波动不同，所以这张表只比较相同点数，不表示 NQ 的风险必然低于 ES。某合约每点价值较低，也不意味着按相同手数交易就有相同风险。

### 7.1 将结构位距离转成风险预算

下面是仓位计算示例，不是建议用多少风险：

```text
计划风险金额 R
计划止损距离 d（点）
每点价值 M
每手预留费用和滑点 c
最大计划手数 n = floor[R/(d×M+c)]
```

自拟条件：`R=300美元，d=12点，c=10美元`。1手ES计划风险为610美元，超过预算；1手MES为70美元，算术上最多4手。这只是计划值，跳空、流动性不足及交易限制可能造成实际损失大于计划。DeepGamma 水平可以帮助决定观察区和失效条件，不能代替金额计算。

## 8. 保证金、结算和不同产品风险

### 8.1 保证金不是最大亏损

CME 将期货保证金解释为开仓及持仓需要保留的资金，并非购买标的的首付款。初始、维持保证金有不同作用；经纪商可收取额外资金，波动增加时保证金可能提高，余额不足时可能被要求补资或被平仓。[CME：Margin—Know What's Needed](https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed)

因此不宜在长期使用指南里写死一个“当前ES保证金”。合约的每点盈亏是规格问题；保证金门槛是随时间和账户规则变化的要求；计划止损又是第三件事。

### 8.2 指数期权、ETF期权、期货期权不能混用交割逻辑

SPX 期权的合约乘数为100美元，采用欧式行权和现金结算；传统 SPX 与 SPXW 的结算时点、最后交易时点存在差别，不能把所有SPX系列都认作“当天收盘结算”。[Cboe：SPX Product Specifications](https://www.cboe.com/tradable-products/sp-500/spx-options/spx-specifications)、[Cboe：SPX Fact Sheet](https://res-certification.cboe.com/resources/spx/spx-fact-sheet.pdf)

CME 的 Micro E-mini 期权与 E-mini 期权也存在行权、结算安排差异，必须逐产品、逐系列查看，不能从“名称都带S&P”推断相同交割结果。[CME：Micro E-mini S&P 500 and Nasdaq-100 Options FAQ](https://www.cmegroup.com/articles/faqs/faq-options-on-micro-e-mini-s-p-500-and-nasdaq-100-futures.html)

**与指南相关的边界**：DeepGamma 如展示的是指数期权结构、使用者交易的是期货，则分析对象和执行工具不同。若使用者改为直接交易期权，还需额外核对该具体期权的乘数、最后交易时间、行权方式、结算依据与经纪商截止时间。

## 9. 把这些知识转为可重复观察流程

以下为基于基础知识的教学流程，不代表 DeepGamma 原生提供这些按钮或自动化：

1. **确定对象**：记录标的是SPX、NDX、SPY、QQQ还是期货期权，明确最终下单工具。
2. **固定口径**：记录日期、时区、数据更新时间、OI日期、到期范围、Gamma符号和金额单位。
3. **分看期限**：分别观察全到期结构和0DTE结构，找一致与冲突。
4. **标注区域**：把明显集中位置当作待观察区域，写出可能反应和失效情形。
5. **映射工具**：若交易ES/NQ，用同步基差转换指数结构位，核对合约月份。
6. **观察确认**：记录价格是否接受、拒绝、突破后回测；不要把接近水平本身视为确认。
7. **计算金额**：由失效位置、执行工具点值与成本预算得到计划仓位。
8. **事后复盘**：将入场前保存的结构与后续结果比较，避免用事后更新图解释过去信号。

### 9.1 三个可写入产品指南的教学场景

**场景A：净正Gamma假设下的区间反应**。若某工具的符号确实代表交易商净正Gamma，且高Gamma区附近出现多次价格拒绝，可将“短期对冲流可能压制波动”作为解释之一。若价格持续接受在区域外，该情景已失效；不能因正Gamma标签不断逆势加仓。

**场景B：净负Gamma假设下的突破跟随**。若已确认净负Gamma口径，价格在事件后离开原区间且成交/流动性支持移动，可把顺势对冲作为可能的放大器。突破失败仍可能出现；负Gamma不提供方向，也不保证突破延续。

**场景C：0DTE与全到期冲突**。全到期净Gamma为正、0DTE为负时，可记录为“结构分歧”，关注当日期限在剩余时间和价格附近是否占主导。不可简单把两个不同单位、不同归一化的数字相加。若平台没有权重或单位说明，应保留为定性对比。

## 10. 官方来源索引与证据边界

以下均已在本次研究中通过网络检索或打开核验。官方材料支持通用市场知识；它们不背书 DeepGamma 的指标算法或策略效果。

| 编号 | 官方来源 | 支持的核心内容 |
| --- | --- | --- |
| M01 | [OIC：Delta](https://www.optionseducation.org/advancedconcepts/delta) | Delta定义、普通Call/Put及买卖方向 |
| M02 | [OIC：Gamma](https://www.optionseducation.org/advancedconcepts/gamma) | Gamma定义、长短持仓符号、平值及临近到期特征 |
| M03 | [OIC：Understanding Options Greeks](https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks) | Greeks为条件性理论估计 |
| M04 | [Cboe：Much Ado About 0DTEs](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/) | 对冲方向机制、净量与总量区别、头寸数据边界；文章日期2023-09-08，不能当作2026实时结果 |
| M05 | [OIC：General Information](https://www.optionseducation.org/referencelibrary/faq/general-information) | OI方向中性、开平配对及清算后更新 |
| M06 | [Cboe：0DTE Trading Resources](https://www.cboe.com/tradable-products/0dte/) | 0DTE含义和短期期权敏感度 |
| M07 | [OIC：Theta](https://www.optionseducation.org/advancedconcepts/theta) | 时间衰减非线性与模型时间处理差异 |
| M08 | [OIC：Technical Information](https://www.optionseducation.org/referencelibrary/faq/technical-information) | IV/历史波动率及偏斜 |
| M09 | [OIC：Vega](https://www.optionseducation.org/advancedconcepts/vega) | Vega与IV变化 |
| M10 | [CME：Volatility Term Structure Tool User Guide](https://www.cmegroup.com/tools-information/quikstrike/quikstrike-volatility-term-structure-tool-user-guide.html) | 不同到期平值IV比较 |
| M11 | [Cboe：VIX Term Structure](https://www.cboe.com/tradable-products/vix/term-structure) | SPX波动率期限结构和不同目标期限指标 |
| M12 | [OIC：Black-Scholes Formula](https://prd-web.optionseducation.org/advancedconcepts/black-scholes-formula) | 模型输入及实际市场定价边界 |
| M13 | [CME：What is Equity Index Basis?](https://www.cmegroup.com/education/courses/introduction-to-equity-index-products/what-is-equity-index-basis) | 基差定义与成因 |
| M14 | [CME：Calculating Fair Value](https://www.cmegroup.com/trading/equity-index/fairvalue.html) | 股指期货简化公允价值公式 |
| M15 | [CME：Micro E-mini FAQ](https://www.cmegroup.com/articles/faqs/frequently-asked-questions-micro-e-mini-equity-index-futures.html) | Micro合约、跳动与季度周期 |
| M16 | [CME：Micro E-mini产品资料卡](https://www.cmegroup.com/trading/equity-index/files/cme-micro-e-mini-futures-fact-card.pdf) | MES/MNQ乘数与单腿tick |
| M17 | [CME：E-mini Nasdaq-100规格](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html) | NQ乘数20美元、tick0.25点 |
| M18 | [CME：E-mini S&P 500规格入口](https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html) | ES规格入口；动态网页本次文本抽取没有完整规格表 |
| M19 | [CME第358章规则申报（CFTC保存）](https://www.cftc.gov/sites/default/files/filings/ptc/16/03/ptc030416cmedcm002.pdf) | ES50美元乘数及0.25点单腿tick；文件年代较早，用于交叉核对而非当前交易时段依据 |
| M20 | [CME：Margin—Know What's Needed](https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed) | 保证金定义及动态要求 |
| M21 | [Cboe：SPX规格](https://www.cboe.com/tradable-products/sp-500/spx-options/spx-specifications) | SPX/SPXW乘数与交易时段差异 |
| M22 | [Cboe：SPX资料卡](https://res-certification.cboe.com/resources/spx/spx-fact-sheet.pdf) | SPX欧式、现金结算与AM/PM差异 |
| M23 | [CME：Micro E-mini Options FAQ](https://www.cmegroup.com/articles/faqs/faq-options-on-micro-e-mini-s-p-500-and-nasdaq-100-futures.html) | 期货期权的结算安排不能一概而论 |

### 编辑时应保留的三项区别

- **官方事实**：出处明确的定义与合约规则。
- **数学推导/自拟例子**：为帮助理解而计算，假设已写明，不是交易所公布的某日实际流量。
- **产品待核实**：DeepGamma的实际GEX符号、头寸来源、场景再定价、数据延迟与指标内部公式。只有DeepGamma官方说明或实际界面证据才能确认。
