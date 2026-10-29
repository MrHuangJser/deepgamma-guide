# 通用参数词典：先统一口径，再调整画面

核验日期：2026-10-29。适用于各篇明确列出的桌面字段；Web字段以[差异表](../research/web-desktop-differences.md)及各Web指南为准。不是所有指标都有这里的全部开关。

## Expiration：期限桶不是时间周期

桌面较简期限集合是 **0 DTE、≤1d、≤7d、≤31d、≤91d、All expirations**；Volume、Delta、Big Flows、Heatmap还列有≤2/3/4/5/6d。0DTE只看当日到期；≤7d是“包括0DTE在内”的期限集合，不是只看第7天。日历日、交易日与交易所截止时间的精确实现没有公开，不自行假定。

Expiration不会把5分钟K线变成日线。切换它改变纳入的期权合约集合；改图表周期改变显示聚合。Web还有Default继承全局快栏，到期日默认0DTE；桌面多数指标默认All，但Big Flows、Heatmap和Envelopes Advanced默认0DTE。来源见每篇官方专页与[Web总览](https://www.deepcharts.com/helpcenter/deepgamma-web/article/deepgamma-web-platform-overview)。

## Data source：同一条柱可以代表完全不同的经济量

| 标签家族 | 在研究中的含义 | 不能推导什么 |
|---|---|---|
| Call/Put Σ | Call、Put原始成交量 | 主动买卖、净持仓、做市商符号 |
| Call Σ − Put Σ | 两类量的差 | 买盘减卖盘；Put多不等于所有人买Put |
| Gamma / Gex (Call − Put) | Gamma加权的传统Call减Put模型 | 做市商实际净Gamma已被直接观测 |
| OI (Eod)、OI-E | 最近发布的日终持仓 | 当天新流入或实时仓位 |
| Gamma (Call OI-E − Put OI-E) | 用EOD存量而非成交量作底的Gamma模型 | 参与者分类已经确定 |
| OI-R / OI (R.T.) | 平台构造的实时持仓统计 | 官方清算OI即时发布 |
| Gex (Market Maker) | 官方定义的做市商Gamma数据口径 | 所有对冲一定在期货市场按模型执行 |
| Gex (Market Maker C/P) | 做市商Gamma按Call/Put拆开 | 必然左右对称，或每个Put都是负Gamma |
| Dex (Market Maker) | Delta存量风险口径 | Gamma环境；正Delta不等于立刻买期货 |
| Market Maker Net Flow / Δ | 分类交易流的净Delta口径 | 与Delta存量完全等价 |

别名如classic、state、convexity ladder来自官方跨平台解释，不能保证另一家同名模型的分母、单位和覆盖范围相同。[官方数据源示例](https://www.deepcharts.com/helpcenter/article/option-gex-heatmap)。

## Include Carry or Open Interest

官方将其解释为是否纳入前期结转/持仓，关闭偏当前交易日，开启偏带入存量。**不要手工把开启结果再加上一份昨天OI**，否则可能重复计入。不同数据源下的种子、结转时点、到期剔除和负仓位处理未公开。

两个图的Carry不同，峰值和总量可以不同；这不是画线错误。做日内新增流研究可用关，做包含前期风险的情景研究可用开；这些是研究用途选择，并非哪一个永远更准。桌面Envelopes Advanced默认开，其余不少专页写关，截图有时已被改为开；Web多项默认开。

## Number of Strikes、Number of levels、Number of profile

三者不能互换：Strikes控制计算纳入的行权价范围，0表示不限；Levels控制从中绘制多少关键位；Profile控制显示多少交易日的剖面（数量是否包含当前日，以实际界面确认）。限制Strikes可能改变计算结果及Zero Gamma，不是仅隐藏远处图形。官方没有明确有限Strikes是双侧各N还是总N，需在版本中核对，不预设。

## 桌面Subgraphs全字段

以下是各指标重复出现的显示字段，默认值不同的部分写在各篇表里。来源：[Volume](https://www.deepcharts.com/helpcenter/article/option-volume)、[Delta](https://www.deepcharts.com/helpcenter/article/option-delta)、[Envelopes](https://www.deepcharts.com/helpcenter/article/option-levels-envelopes)。

| 字段 | 调什么 | 使用建议 |
|---|---|---|
| Color、2° Color | 主色、第二色 | 记录第二色由什么条件触发 |
| Line、Background、2° Line、2° Background | 区间线与填充及备用颜色 | 降低填充遮挡，保留边界 |
| Subgraph Style | Line / Bars / StackedBars / Range / Hidden / BrokerLine / Ignore，依指标可用项 | 只从本指标列出的选项选；Hidden不应被当作删掉算法 |
| Auto Color | None、Slope、+/− | Slope按变化方向上色；+/−按数值符号。符号与斜率是两件事 |
| Line Style | Solid、Dash；部分还有Dot、Dash dot、Dash dot dot | 不同期限用不同线型 |
| Line Width | 线或柱宽 | 加粗只影响画面，不增加数据权重 |
| Short Name | 自定义序列名 | 写入来源、期限、Carry、单位，如MM-GEX-0DTE-C1 |
| Name Label、Value Label | 名称、当前值显示 | 保留关键位数值便于映射 |
| Name Background、Value Background | 标签背景 | 图层拥挤时用背景提高对比 |
| Chart color for marker | 使用图表颜色画标记 | 属显示设定，不是Marker阈值 |
| Include on Auto Center | 本序列参与自动缩放/居中 | 远距离关键位把价格压扁时检查此项 |

BrokerLine的精确连接/断段规则，官方正文未解释；只能确认它是Major/Minor等序列可选样式，不能把它解释为“向经纪商发送订单”。有些截图演示Line，有些文字写BrokerLine默认，遇到冲突以新建实例和实际设置为准。

特别注意 **Auto Color=Slope**：负值从−10升到−5可以显示绿色，却仍然是负值。因此读Gamma状态先看零轴和数值。不能只凭绿色判断正Gamma。

## Profile类画面全字段

适用于Option Profile、GEX Profile、Hedging Profile，后者没有前两者全部Peak/Rolling/Summary分组。官方来源：[Profile](https://www.deepcharts.com/helpcenter/article/option-profile-deepchart)、[GEX Profile](https://www.deepcharts.com/helpcenter/article/option-gex-profile)、[Hedging](https://www.deepcharts.com/helpcenter/article/option-gex-profile-hedging-de)。

| 分组／字段 | 桌面公开默认／选项 | 配置含义 |
|---|---|---|
| Width type | Automatic；另有Percentual period、Window width、Fixed bars | 自动、按可见期间比例、窗口宽度、固定柱数；数值单位随模式而变 |
| Current Width / Offset | 10 / 0 | 当前交易日剖面宽度和横向偏移 |
| Previous Width / Offset | 15 / 0 | 历史剖面宽度和偏移 |
| Number of profile | 5 | 交易日剖面显示数量；非5分钟，是否含当前以界面确认 |
| Vbp opacity | 90 | 剖面不透明度 |
| Border width | 1.00 | 边框宽度 |
| Show above bars | 关 | 是否在价格柱上层绘制 |
| Visual style | Solid；可Hollow | 实心/空心条 |
| Align to the right | 关 | 靠右显示 |
| Always visible | 关 | 滚动离开原区间也保持可见 |
| Strike Ticks Height (%) | 75 | 每档条的垂直厚度，不是报价Tick价值 |

用Automatic时，缩放窗口会改变柱的视觉长度，不能据屏幕像素判断实际风险同比增长。比较历史截面要读数值并固定尺度。

Background/Text包含Call/Positive背景（绿）、Put/Negative背景（紫），Text Enabled（关）、Text size（11）、两类文本色（白）。官方某些界面将两种色控都标成Call/Positive，是标签重复，不代表两种都是Call。

Disputed有Highlight（关）及两类高亮色（绿/紫）。官方说用于重叠/争议区域，没有公开判定公式。因此它不证明交易所数据无效，也不等于套利机会。

Peak分正、负两组；每组有Enable、Highlight、Highlight Color、Show Line、Line Color、Line Width、Line Style。普通Profile两侧Enable默认开，GEX Profile默认关；两者Highlight默认关、Show Line默认开、线宽1、线型Dash。**Enable关时，仅Show Line开不保证会出现线。**

Rolling Values的M1/M5/M15/M30是1/5/15/30分钟前的截面，不是移动平均。正文默认全部关、线宽1，线型分别Dot/Dot/Dash/Solid，颜色自定；示例图中常已开启并改线宽，所以不要照图误认默认。Web可能额外提供Flip only，见差异表。

Summary：净值及Call/Put分项依当前Data source计算。GEX Profile明确列出Enable Summary关、文本白、正绿负红、字号12；普通Profile正文虽解释汇总，开关默认未完整列出，截图可见Enable Summary，故应手动确认。汇总不是独立新指标，也不是与Summary Gex完全不同的数据证据。

## 截图中的指标容器控件

桌面各指标窗口还有共用外壳：顶部指标启停；Chart area的Horizontal/Vertical及区域下拉；部分指标可见Use sec. axis；底部Indicator Template、Protected、Apply、Save。它们属于指标摆放、轴和保存的控件，不是新的期权统计模型。

可根据画面确认Horizontal/Vertical用于不同区域布置，区域数字用于选择显示区域；要把风险值放副图时核对轴单位，不能让统计值被误认成指数价格。Use sec. axis是二轴显示开关；具体与自动缩放、区域类型的联动未完整公开。Protected的精确保护对象、Indicator Template保存/加载作用域，以及Apply与Save在不同版本的持久化差别，官方指标正文未完整说明。应通过临时模板在自己的版本验证，不把Protected猜成锁仓、风控或数据加密功能。

## 推荐的配置核对记录

每次截图旁写：版本／日期／数据时间／时区／标的／期货月份／价格模式／Data source／Expiration／Carry／Strikes／图表周期／Auto Color／单位。用模板保存后重新打开核对一次。跨指标不一致时，先排查这张记录，再讨论市场解释。
