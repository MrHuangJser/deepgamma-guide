# DeepGamma 中文配置与交易使用指南

核验日期：**2026-10-29**。覆盖官方帮助中心的 **14项桌面指标、19项Web指标**，以及平台配置、模板、回放、价格转换和交易研究流程。每个指标均有配置、含义、场景、教学例子与局限；19项按跨版本去重后计数，不是33种不同指标。

本目录以[原始桌面帮助中心](https://www.deepcharts.com/helpcenter/deepgamma)为起点，进一步核查[Web帮助中心](https://www.deepcharts.com/helpcenter/deepgamma-web/indicators)、官方截图与官网短视频，并检索OIC、Cboe、CME等一手资料。**这是公开资料与媒体核验，不是付费软件功能实测；所有交易数字例子均为教学假设。**

## 在线文档站

[打开 DeepGamma 中文研究手册](https://mrhuangjser.github.io/deepgamma-guide/)

站点采用 Astro + Starlight，支持中文全文搜索、分组导航、页内目录、明暗主题和图片放大。原始指南是内容真源，构建时由 `tools/prepare_site.py` 生成网页内容；合订本仅提供下载，不重复进入搜索。

本地运行：`npm ci` 后运行 `npm run dev`；生产构建为 `npm run build`，本地预览为 `npm run preview`。构建需要 Node.js 24 和 Python 3。推送 main 后由 GitHub Actions 自动发布到 GitHub Pages。

## 建议阅读顺序

1. [开始使用：数据、标的、添加指标、模板与布局](guides/00-start-here.md)
2. [期权与期货基础：Greeks、持仓、做市商对冲、IV、基差与合约规格](research/market-foundations.md)
3. [通用配置词典：期限、Carry、Subgraphs、Profile、Peak、Rolling与Summary](guides/00-common-settings.md)
4. 按下表选择指标；Web使用者同时读[Web平台操作](guides/web-platform.md)和[14项指标跨版本详细配置](research/web-desktop-differences.md)。
5. [组合使用、情景检验、ES映射、风险与回放复盘](guides/15-workflows-and-risk.md)

连续阅读可打开[DeepGamma完整手册](DeepGamma完整手册.md)。它由分篇合并生成，修改维护以各篇为准。

## 全部19项指标

“标准”组支持SPX、SPY、NDX、QQQ；“CBOE”组为SPX专用。这里的Web新增指帮助目录比桌面目录多列出，不能据此断言桌面软件绝无对应功能。

| 指标 | 数据/范围 | 详细指南 | 核心用途 |
|---|---|---|---|
| Option Volume | 标准 | [成交量](guides/01-option-volume.md) | 活跃度、Call/Put量与Premium |
| Option Delta | CBOE | [方向流量](guides/02-option-delta.md) | 客户/MM视角、逐柱与累计 |
| Option Big Flows | CBOE | [大额交易](guides/03-option-big-flows.md) | 权利金阈值、买卖、开平仓 |
| Option Profile | 标准 | [期权剖面](guides/04-option-profile.md) | 成交量、传统Gamma与EOD OI |
| Option GEX Profile | CBOE | [做市商风险剖面](guides/05-option-gex-profile.md) | 净Gamma、C/P拆分、DEX与OI-R |
| Option GEX Profile Hedging | CBOE | [对冲反应剖面](guides/06-option-gex-profile-hedging.md) | 放大、衰减、中性 |
| Option Levels | 标准 | [结构水平位](guides/07-option-levels.md) | 排名关键位与Zero Gamma |
| Option Levels Advanced | CBOE | [高级水平位](guides/08-option-levels-advanced.md) | MM风险与实时持仓集中 |
| Option Envelopes | 标准 | [Gamma参考线](guides/09-option-envelopes.md) | Zero、Major、Minor |
| Option Envelopes Advanced | CBOE | [实时OI参考线](guides/10-option-envelopes-advanced.md) | OI-R基础的结构变化 |
| Option Summary | 标准 | [传统Gamma汇总](guides/11-option-summary.md) | 总体模型状态随时间变化 |
| Option Summary Gex | CBOE | [MM风险汇总](guides/12-option-summary-gex.md) | Gamma、Delta、净流分别解读 |
| Option Expected Move | 标准 | [隐含波动范围](guides/13-option-expected-move.md) | Daily/30分钟、1σ/2σ |
| Option Gex Heatmap | CBOE | [风险热图](guides/14-option-gex-heatmap.md) | 风险区随价格和时间变化 |
| Option Net Flow | Web新增、CBOE | [净流量](guides/web-option-net-flow.md) | Call/Put/Difference累计 |
| Option Dynamic Walls | Web新增、CBOE | [动态墙](guides/web-dynamic-walls.md) | Walls/Overlap动态区域 |
| Option Market Maker Pressure | Web新增、CBOE | [做市商压力](guides/web-market-maker-pressure.md) | 累积压力与两条均线 |
| Option Market Maker Sentiment | Web新增、CBOE | [做市商情绪](guides/web-market-maker-sentiment.md) | 环境、方向、波幅状态 |
| Option Exhaustion Detector | Web新增、CBOE | [衰竭检测](guides/web-exhaustion.md) | 延伸后的衰竭候选标记 |

## 使用前最重要的区别

- **正负Gamma不是涨跌方向**。负Gamma也可能放大上涨；Put多头本身Gamma为正。
- **颜色语法依指标与版本变化**。Big Flows的Buy色、Hedging的紫色、Exhaustion的Hollow各自有不同含义。
- **OI-R不等于交易所实时清算OI**；成交量不等于净持仓；期权风险不等于已经发生的期货成交。
- **Web与桌面默认不同**。Web Delta有八种Value，热图默认过滤更宽，很多Carry默认开；迁移时逐项核对。
- **SPX结构用于ES需核对同步基差与月份**。Web期货价格转换自动选合约，换月可能短暂不一致。

## 图片、多媒体与核验证据

- [媒体识读与官方表述冲突清单](research/evidence-and-media.md)：哪些图被查看、视频画面支持什么、哪些说法不能直接照抄。
- [功能覆盖及未公开问题](research/coverage-and-unknowns.md)：所有功能与指南映射、仍未能核实的公式和产品能力。
- [桌面与产品资源清单](research/source-manifest.json)、[Web五项来源与识图清单](research/web-exclusive-sources.json)、[Web平台图像索引](assets/web-platform/manifest.json)、[Web媒体扫描](research/web-media-scan.json)。

官方图片保存在assets下，联系表便于逐页核对；图片、品牌和演示视频权利归原权利人。本地副本用于本次学习研究，文中保留官方原始来源；这些素材不表示获得再发布授权。

## 目录维护

`guides/`是操作与使用篇，`research/`是市场基础、版本差异与证据，`assets/`是来源图像和媒体。`tools/build_handbook.py`生成合订版并检查本地链接，`research/validation-report.json`记录最近检查结果。检索时使用官方英文指标名最方便。

资料描述了截至核验日可查到的公开能力。未公开算法、实时延迟、历史修正及完整账号权限不写成确定事实；具体边界已放在相应章节旁。
