# DeepGamma Web 新增五项指标：阅读入口

核验日期：2026-10-29。范围以[官方 Web 指标目录](https://www.deepcharts.com/helpcenter/deepgamma-web/indicators)为准：目录有 19 项；相对桌面帮助中心的 14 项，下面五项有额外的 Web 专页。这里的“新增”是文档目录的差异，不表示已验证桌面软件绝对不支持。

| 指标 | 主要问题 | 详细指南 |
|---|---|---|
| Option Dynamic Walls | 价格在动态参考带的上方、内部还是下方？ | [动态墙](web-dynamic-walls.md) |
| Option Exhaustion Detector | 当前延伸是否出现值得检查的衰竭点？ | [衰竭检测](web-exhaustion.md) |
| Option Market Maker Pressure | 期权来源的压力在持续累积还是开始回落？ | [做市商压力](web-market-maker-pressure.md) |
| Option Market Maker Sentiment | Gamma 环境、方向和波幅状态如何组合？ | [做市商情绪](web-market-maker-sentiment.md) |
| Option Net Flow | Call 与 Put 两侧的累计净流怎样变化？ | [期权净流](web-option-net-flow.md) |

五项均由官方标为 **CBOE 数据、SPX 专用**。统一添加路径为：打开 SPX 图 → `Indicators` → 绿色 `Add indicator` → `Options (Cboe)` → 搜索完整名称 → 在指标列表点齿轮修改 → `Apply`。前四项还可以通过右侧 `Settings` 快捷栏中的相应开关启停；Net Flow 专页未列出同名快捷开关。

下面的组合顺序是本文的研究用工作流，不是官方盈利策略：Sentiment 先看环境 → Dynamic Walls 确定价格所处区域 → GEX/OI 标出具体位置 → Pressure/Net Flow 检查累积变化 → Exhaustion 提醒观察触发点 → 最后验证实际价格反应。多个指标使用相关的期权数据，不能把同时变色当成多个独立证据。

本组指南区分官方功能事实、截图可见事实和原创教学情景。专有模型未公布公式、样本外胜率或信号重绘规则，不能从截图反推为确定的交易系统。资料截图来自官方页面，仅用于本地学习核对；[来源与识图记录](../research/web-exclusive-sources.json)列出原始 URL、本地文件和查阅状态。
