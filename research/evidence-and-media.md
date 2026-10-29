# DeepGamma图像和多媒体识读记录

核验日期：2026-10-29。这个记录区分从图片直接看到的内容、官方文字默认值和金融原理推断。行情截图只用来识别界面，不用于证明预测效果。

## 1. 读取了什么

原始桌面目录14篇逐页提取正文、图片链接、video/audio/source/iframe。主资源清单另含产品页、数据源页、Changelog及v16发布说明，共18个页面。最初17页下载147个去重图片URL，补充v16后主清单共有156个不带查询参数的唯一图片地址；包含品牌图与装饰图，不能把这156全叫指标截图。

14篇桌面指标与产品页各生成图像联系表，并已逐表查看；分辨率、来源与本地路径保存在[source-manifest.json](source-manifest.json)。联系表覆盖总览、添加入口、参数、样式、示例；细小文字主要与正文互核，不能把缩略图阅读声称为每个像素都逐字辨认。

Web平台总览21幅操作截图及关键Delta、热图、Big Flows、Profile参数原图已识读，清单在[Web平台图像索引](../assets/web-platform/manifest.json)。Web五项额外指标识读34幅不同功能截图，重要4幅作原图放大核对，见[专用证据JSON](web-exclusive-sources.json)。Web各页的媒体元素另做扫描，见[web-media-scan.json](web-media-scan.json)。

最终补查覆盖了14篇共同指标的全部106处非装饰截图（97个不同资源），各有 `contact-<slug>.jpg` 联系表。Web索引221处资源记录均有可用本地副本；161处带alt的技术截图记录已标识读状态，包含平台21处、共同指标106处、额外指标34处的复用与交叉引用。这里的“处”按页面出现次数统计，不能将其写成161张互不重复的图片。logo和分隔线不作为功能证据。

## 2. 桌面各篇的直接视觉证据

| 页面 | 看到的关键内容 | 联系表 |
|---|---|---|
| Big Flows | 菱形/方形、买卖开平Tooltip、Generic/Open/Close三组、Size；不同示例已改色/填充 | [图片](../assets/contact-sheets/option-big-flows.jpg) |
| Delta | Revert与Cumulative独立开关，取反及累计前后形态，副图颜色/柱型 | [图片](../assets/contact-sheets/option-delta.jpg) |
| Envelopes | 三色随时间变化；General示例Carry开；Zero/Major/Minor分别可配置 | [图片](../assets/contact-sheets/option-levels-envelopes.jpg) |
| Envelopes Advanced | 0DTE、Carry开、OI-R源，三线阶梯与Line示例 | [图片](../assets/contact-sheets/option-envelopes-advanced-deepchart.jpg) |
| Expected Move | 区间填充、独立上/下界，Daily和1σ；示例打开边界Line | [图片](../assets/contact-sheets/option-expected-move.jpg) |
| Heatmap | 正负色块、GEX-H按钮、0DTE、Carry关，1/30/90强度设置 | [图片](../assets/contact-sheets/option-gex-heatmap.jpg) |
| GEX Profile | MM与MM C/P标签，General有正文未列字段，Peak/Rolling/Summary示例 | [图片](../assets/contact-sheets/option-gex-profile.jpg) |
| Hedging | Amplifying紫、Attenuating绿、Neutral橄榄黄；仅颜色与Plot组 | [图片](../assets/contact-sheets/option-gex-profile-hedging-de.jpg) |
| Levels | 三角数量排名、正负三角方向、Yellow Zero与延伸配置 | [图片](../assets/contact-sheets/option-levels.jpg) |
| Levels Advanced | GEX (MM)标签、排名、Carry关、Plot与综合图 | [图片](../assets/contact-sheets/option-levels-advanced.jpg) |
| Profile | 四源示例、Stack、Peak、历史Rolling截面及汇总 | [图片](../assets/contact-sheets/option-profile-deepchart.jpg) |
| Summary | 主图环境背景与副图、Marker、Bars与Auto Color | [图片](../assets/contact-sheets/option-summary.jpg) |
| Summary Gex | MM源、主图Marker，独立Regime显示参数，另有Line示例 | [图片](../assets/contact-sheets/option-summary-gex.jpg) |
| Volume | Call/Put柱、Total Hidden，参数示例Stacked与正文Splitted默认差别 | [图片](../assets/contact-sheets/option-volume.jpg) |

产品页联系表还显示回放日期、To futures price、Speed、Expirations与指标快捷栏，可核对Web版本界面差异。[产品页联系表](../assets/contact-sheets/features-deepgamma.jpg)。v16的[模板栏原图](../assets/images/iWXl8H1kbws7lHOtv0lI5ngYOvw.png)与[共享文件选择器](../assets/images/T9FbB9oR2J0RgXZhm4D5slHuc0.png)已单独查看，能看到Shared和DeepGamma Full示例；不能由模板名推断当前订阅权益。

## 3. 官网视频读取

[官方产品页](https://www.deepcharts.com/features/deepgamma)嵌入的原始媒体为[5.36秒MP4](https://framerusercontent.com/assets/xvNlJ0HIfb4IGyaa3z1y6POboM.mp4)，1920×1080、25fps、134帧。已下载到[本地视频](../assets/video/deepgamma-official-demo.mp4)，每秒抽样并查看首帧及末帧；[抽样联系表](../assets/video/contact-sheet.jpg)可复核。

画面为带景深/模糊效果的图表展示：价格路径、上下横向色带、左/中风险剖面、右侧空心/实心剖面、下方柱状统计。它支持“多个图层可以组合展示”的外观判断；**没有可读的完整参数步骤，不能据此反推数据源、净Gamma符号、入场点或未来订单**。这是产品视觉短片，不是完整讲解教程。

媒体包含AAC音轨，没有内嵌字幕流；音频检测均值约−64.8dB、峰值约−51.6dB。未取得可用旁白转录，不从音轨增添产品事实；“音轨存在”也不被写成“有一段已听懂的教学”。桌面指标页扫描所见iframe主要为Google Tag Manager，不把它当教学视频。Web扫描结果按实际元素记录，未遍历页脚整个YouTube频道的所有外链内容。

## 4. 官方文字、截图和金融机制的冲突处理

| 项目 | 证据差异 | 指南采用的处理 |
|---|---|---|
| Big Flows Put买开颜色 | 默认Buy绿/Sell红，但例子写红Put买开 | 仅在改Put配色后成立；读Tooltip和配置 |
| Big Flows开仓填充 | 默认开仓实心，但某BUY TO OPEN图是空心 | 样式可改；Tooltip优先，不用图片恢复默认 |
| Volume Display mode | 正文默认Splitted，参数截图Stacked | 两者并列记录，以文字默认为来源，不抹平差异 |
| 普通Envelopes Carry | 正文默认关，General图开 | 区分官方默认和示例状态 |
| Advanced Envelopes主次样式 | 正文BrokerLine，示例Line | 保留两种证据，不假定版本一致 |
| GEX Profile General | 正文没列Expiration/Carry/Stack，图里有 | 记录可见字段与示例值，不编默认 |
| Profile左右方向 | 普通/净值/拆分/堆叠形态不同 | 用图例、数值和Data source识别 |
| Heatmap橙区 | 原理说负Gamma放大，下方示例又说支撑 | 条件化处理，不把橙块一律当买压 |
| Call正/Put负 | 界面标签和传统模型把两者并写 | 多头Put本身正Gamma；净仓与模型约定决定符号 |
| “2卖1买”OI-R例 | 官网把净流简化为实时持仓说明 | 不沿用为全市场清算OI算式 |
| “100%”及“最准确” | 产品页营销数据主张 | 保留来源归属，不作为独立验证或预测保证 |
| Expected Move“70/95%” | 文案近似，未给完整分布及覆盖回测 | 写模型条件、68.27/95.45近似及终点/触碰区别 |
| Web Pressure overlay | 平台总览说叠加线，专页默认副图 | 以专页的Overlay开关和截图为准 |
| Web Net Flow Difference | 文字Bars/width1/+−/Diff，截图Hidden/3/None/Call | 在Net Flow篇列出矛盾，不照图误认默认 |
| Web平台“Only CBOE ... SPX” | 一句话语序与全文标准组支持SPX不一致 | 解释为CBOE组仅SPX，非SPX只能用CBOE组 |
| Web Rolling、Strike grid | 示例开，文字默认关 | 示例是修改后画面，不覆盖默认 |
| Web Levels Advanced示例 | 例图选OI源、三类线都改为黄 | 不把例图当MM GEX默认配色或默认数据源 |
| Web Expected Move与Volume示例 | 边界Line、总量线开启，正文默认Hidden | 区分用户开启的序列与初始默认 |

## 5. 可追溯性和验证层级

**文字事实**引用官方专页；**截图事实**给本地原图/联系表和原URL清单；**金融解释**引OIC/Cboe/CME；**数学与情景**明确假设；**未公开实现**不补造。各篇写“已识读”表示查看了这些图片，不表示登录付费软件或运行过其后台。

本地资源与Markdown链接由构建检查核对；检查报告仅验证文件和引用可达，不代表外部网站未来不改版、模型算法正确或交易有效。

另检查了正文引用的67个唯一外部URL：58个普通请求返回200，9个CME地址普通请求超时、经Web读取均成功取得对应页面/PDF。超时没有被误判成失效链接；[外部引用检查记录](external-link-check.json)保留两种结果。这里的可达验证仍不替代正文逐项事实核对。
