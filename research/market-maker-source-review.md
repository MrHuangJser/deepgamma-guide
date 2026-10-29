# 做市商指标的独立来源复核

复核日期：2026-10-29。范围：GEX Profile、Hedging Profile、Levels Advanced、Envelopes Advanced、Summary Gex、GEX Heatmap、M.M. Pressure、M.M. Sentiment，以及通用配置与市场基础。

现有文档的核心方向关系和公开参数覆盖较完整。本次未发现“负 Gamma 等于看跌”“Put 天然负 Gamma”“Pressure 等于真实 ES 成交”等核心错误。需要补充的重点是把分散说明组织成一条可执行的做市商分析主线，并加强结转仓位、信息层级与数据时点的例子；不需要为了增加篇幅臆造后台公式。

## 1. 补充优先级与具体位置

| 优先级 | 当前缺口 | 建议补充位置与内容 |
|---|---|---|
| 高 | “真实 CBOE 数据”与平台指标之间的关系分散在多页，读者容易把真实参与者身份误认为完整对冲已经发生 | 新增做市商阅读主线；明确四层：参与者交易分类、头寸与 Greeks 聚合、条件对冲模型、实际价格及执行验证 |
| 高 | Carry 已说明开关用途，但缺少“日内净买入仍可能整体净空”的算例 | 通用参数、Summary Gex：用期初净仓加盘中净交易说明存量与增量；同一系列、同一单位下比较 |
| 高 | 环境／位置／变化的维度已经存在，未集中说明应如何选择最少的指标 | 做市商主线：Summary Gex 定量环境；Profile 或 Heatmap 定位；Hedging 条件反应；Pressure 盘中变化；Sentiment 提炼分类。不要要求全部同时开启 |
| 中 | OI-R 已正确标注平台构造，但一手数据规范可提供更扎实的边界 | 市场基础或证据说明：Cboe 1 分钟产品的 OI 字段为空；不能反向推断 DeepGamma 特定供应合同或后台实现 |
| 中 | 时间、覆盖、单位已有记录模板，但“指标冲突”的排查顺序可以更具体 | 组合流程：先核版本／Data source／Expiry／Carry／Strikes／时点，再区分局部与总量、存量与增量、数值与分类 |
| 中 | 缺少用同一条件比较“加了 MM 指标是否真的有帮助”的研究例子 | 复盘章节：固定价格规则与风险规则，分组比较有无某指标过滤的结果；同时记录机会减少、费用、最大不利移动，而非只看成功截图 |

## 2. 官方数据与平台派生结果应分层理解

DeepCharts 将 SPX 描述为使用 CBOE 参与者数据，其他标的使用 OPRA 及专有估计；GEX Profile 专页进一步区分 MM 净值、MM C/P、DEX、净流和 OI-R。应保留这一来源差异，但不要把产品的“无假设”宣传扩展为“Greek 估值、聚合、风险抵消和对冲行为均无需模型”。[DeepGamma 产品页](https://www.deepcharts.com/features/deepgamma)、[GEX Profile 数据源](https://www.deepcharts.com/helpcenter/deepgamma-web/article/option-gex-profile-deepgamma-web)

Cboe 自己的研究使用交易主体、买卖及开平资料来分析净头寸；它强调买卖抵消后的净风险和规模，而非总成交量。研究中的 Gamma 对冲是潜在买卖需求，并非已逐笔观测的期货成交；其 2023 年样本结论也不能替代 2026 年某个交易日的判断。[Cboe：SPX 0DTE 的市场影响](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)

建议在指南中明确以下证据边界：

| 层次 | 可以确认或研究的内容 | 不应直接跨越的结论 |
|---|---|---|
| 来源分类 | 官方称 SPX 可区分 MM；与仅用 Call/Put 符号假设有区别 | 看到了每家机构全部资产负债表 |
| 风险聚合 | MM GEX／DEX、按行权价分布、指定期限和 Carry | 横条数值就是未来必成交的 ES 手数 |
| 模型解释 | Hedging 的放大／衰减、Sentiment 的环境／方向分类 | 确定的预测概率或固定胜率 |
| 市场验证 | 同步价格、期货成交和盘口反应 | 同时发生就证明是期权做市商造成 |

后两行是研究方法上的推论。Hedging 官方明确使用 IV 与 Greeks 估计反应，Sentiment 官方明确由 DeepChart 计算；Pressure 官方只以期权数据构造的累计压力类比 CVD，没有给可换算为 ES 张数的单位。[Hedging](https://www.deepcharts.com/helpcenter/article/option-gex-profile-hedging-de)、[Sentiment](https://helpdesk.deepcharts.com/portal/en/kb/articles/option-market-maker-sentiment)、[Pressure](https://helpdesk.deepcharts.com/portal/en/kb/articles/option-market-maker-pressure-deepgamma-web)

## 3. 可直接纳入指南的 Carry 算例

以下是净头寸的教学恒等式，不是 DeepGamma 公布的算法。只考虑同一个期权系列，忽略到期、行权、转仓和更正：

```text
期末净仓 = 期初净仓 + 期间买入张数 − 期间卖出张数
```

假设期初 MM 净空 100 张，盘中买入 30、卖出 10：期间净买入为 20，期末仍净空 80。买入可能是在平空，不能自动解释为新增多仓。若该系列每张多头 Gamma 为正，期间净交易对 Gamma 的贡献可以为正，而含期初库存的组合 Gamma 仍为负。这就解释了为什么“日内新增活动”和“含结转风险”的符号可能不同。

DeepGamma 的 Summary Gex 官方说明 Carry 开启会纳入前期持仓，关闭只考虑当前会话；精确种子、结转算法和调整项未披露，因此不能声称上面算式可以精确复刻平台。[Summary Gex：General](https://www.deepcharts.com/helpcenter/article/option-summary-gex)

## 4. 新核对的 Cboe 数据规范：有帮助，但不能替平台补公式

Cboe Open-Close 产品提供参与者分类的买卖等统计，有 EOD、1 分钟及 10 分钟版本。产品页明确盘中版本不含 EOD 的 OI 等字段。[Cboe Open-Close 产品说明](https://datashop.cboe.com/cboe-options-open-close-volume-summary)

进一步读取 **1 分钟规范 v1.5（2026-03-27）** 得到：

- 字段 16、17 的 `open_interest`、`previous_open_interest` 在该盘中版本中为空。
- 字段 35—38 为 MM 买卖的笔数与成交量；没有单独列出 MM 开仓／平仓字段。客户和 firm 等字段另有开平拆分，不能把商品概述扩写为所有身份都有相同字段。
- 这些桶是日内累计快照，并非只包含最近一分钟增量。

这些结论来自该数据产品规范，**并不证明 DeepGamma 订阅或直接使用了这一具体文件**，也不证明平台不能获取其他来源。[Cboe 1 分钟规范，PDF 第 2—3 页](https://datashop.cboe.com/documents/Open_Close_1m_Spec_v1.5.pdf)

EOD 规范则区分 preliminary 与 final 文件，最终 OI 来自 OCC，数值可能修订。这进一步支持将 OI-R 称为平台实时统计，而非官方实时清算 OI。[Cboe EOD 规范 v1.3，PDF 第 3 页](https://datashop.cboe.com/documents/Open_Close_EOD_Spec_v1.3.pdf)

## 5. 时间与修订的当前边界

DeepGamma Web 官方写约每分钟刷新，明确不是 tick-by-tick。指南应区分数据分辨率、发布间隔和实际端到端延迟；不能由“一分钟数据”推出延迟恒定 60 秒或永远同步于价格。[Web 平台总览](https://helpdesk.deepcharts.com/portal/en/kb/articles/deepgamma-web-platform-overview)

Cboe 产品页公布 **2026-11-08** 起的盘中数据改进，包括 1 分钟快照处理交易撤销与更正。相对本次复核日 2026-10-29，这是尚未生效的公告；不能写成当前行为，更不能据此宣布 DeepGamma 的历史回放已经无回填。该信息宜留在来源复核记录，用户主指南继续保留“平台修订策略未公开”的表述。[Cboe 数据改进公告](https://datashop.cboe.com/cboe-options-open-close-volume-summary)

## 6. 本次无需改写的正确内容

现有各篇已经正确区分了：正负 Gamma 与涨跌方向、DEX 与 GEX、整体与局部、净值与 C/P 拆分、热图归一化与真实数值、Pressure 水平与斜率、Sentiment 空白与零值，以及共源指标并非独立证据。Hedging 与 Summary 不一致时，现有文档也未武断认定某一个错误。继续保留这些说明，并通过新增主线与互链提高可发现性即可。

未核实付费账户实时输出、完整 feed 合同、生产模型公式、单位、Carry 种子、修订政策、预测阈值及交易绩效。本次审阅不能把这些未知项转换为已确认的产品能力。

## 7. 本次补充处理记录

本次发现已落实到以下文档；上表保留审阅时的缺口，便于追溯。

| 处理项 | 已更新位置 |
|---|---|
| 数据层级、学习顺序、冲突表、完整观察例子 | [新增做市商分析主线](../guides/market-maker-framework.md)；首页和阅读导航增加入口 |
| 目标对冲不等于新增订单；已有对冲须扣除 | [Summary Gex](../guides/12-option-summary-gex.md)修订原20张ES算例 |
| 日内净买入仍可整体净空；Carry影响范围 | [通用配置](../guides/00-common-settings.md)、Summary Gex及新主线 |
| 累计Greek加权流不等于当前库存风险 | [Delta](../guides/02-option-delta.md)与[Web差异](web-desktop-differences.md) |
| 行权价贡献不等于全簿假设价格扫描 | [GEX Profile](../guides/05-option-gex-profile.md)与新主线 |
| Pressure／Sentiment不强求与其他读数恒等；未公开继承关系不补造 | [Pressure](../guides/web-market-maker-pressure.md)、[Sentiment](../guides/web-market-maker-sentiment.md) |
| 比较加入MM条件前后的增量价值 | [组合使用与复盘](../guides/15-workflows-and-risk.md) |
| OI-R的一手来源边界 | 本报告及[市场基础](market-foundations.md)互链 |

本次另复看本地保存的官方GEX Profile联系表：可见MM数据源、Carry与分价位横条，但这些画面不能确认后台初始库存、对冲订单或场景再定价。[图像证据](../assets/contact-sheets/option-gex-profile.jpg)
