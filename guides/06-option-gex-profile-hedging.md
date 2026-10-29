# Option GEX Profile Hedging：价格移动时的对冲放大与衰减

**适用**：SPX。**来源**：[官方专页](https://www.deepcharts.com/helpcenter/article/option-gex-profile-hedging-de)。核验日2026-10-29；[Web差异](../research/web-desktop-differences.md)。

![官方界面总览，行情仅作显示示例](../assets/images/bWhuPB8uAqZCYh2VPTp0pm4qc.png)

## 它与GEX Profile的区别

GEX Profile告诉你风险在哪；Hedging Profile评估价格向某档移动时，对冲反应更可能**放大Amplifying**还是**衰减Attenuating**。官方称结合IV与Greeks，不只Gamma；没有公开详细Greek清单、权重和预测期限，因此不能声称它已分别输出Vanna或Charm，也不能推导出保证成交的期货张数。

添加：**New → Option Chart → SPX → Indicator Add → Option Gex Profile Hedging → + → 齿轮**。

## 三种颜色的条件含义

| 状态 | 默认色 | 价格上行抵达该档 | 价格下行抵达该档 |
|---|---|---|---|
| Amplifying | 紫 | 对冲可能进一步买入，放大上涨 | 对冲可能进一步卖出，放大下跌 |
| Attenuating | 绿 | 可能卖出，削弱上涨 | 可能买入，削弱下跌 |
| Neutral | 橄榄黄 | 模型没有清楚放大/衰减分类 | 同左 |

**紫色不等于看跌，绿色不等于看涨**。它表示对价格既有移动的反应方式。Neutral也不表示市场不会动，只表示这个模型不给明确的对冲放大/衰减判断。

## 全参数与推荐布局

Colors只有三项：Color amplifying紫、Color attenuating绿、Color neutral橄榄黄。Plot Settings有：

| 字段 | 桌面默认／选项 | 对画面的影响 |
|---|---|---|
| Width type | Automatic；Percentual period / Window width / Fixed bars | 宽度参照方式 |
| Current Width、Current Offset | 10、0 | 当前剖面宽及偏移 |
| Previous Width、Previous Offset | 15、0 | 历史剖面宽及偏移 |
| Number of profile | 5 | 显示几个交易日 |
| Vbp opacity、Border width | 90、1.00 | 不透明度及边框 |
| Show above bars | 关 | 是否覆盖价格柱 |
| Visual style | Solid；可Hollow | 实心/空心条 |
| Align to the right、Always visible | 均关 | 对齐与滚动时可见性 |
| Strike Ticks Height (%) | 75 | 每个行权价条的厚度 |

正文未提供Expiration、Carry、阈值或Data source调整项，不能照GEX Profile补出来。它可能受平台上下文影响，但未公开的继承关系不当作事实。Web可用字段看对照表。

研究者建议只显示当前一个Profile并与GEX Profile错开位置，保留三种默认色。缩小宽度解决遮挡，不通过隐藏Neutral把模型表现美化。宽度数值不代表胜率或概率。

## 场景一：放大上涨

假设价格从6000向6020上涨，6020附近Hedging为紫。研究假说是：“若价格获得上行接受，对冲可能顺势加速。”观察突破后回踩、成交和实际流量是否配合。若价格只短触6020后退回6000，并没有形成接受，放大上行的条件未发生。

同一个紫区域在6000下方，若价格正下跌抵达，含义是放大下跌，而不是此前“紫色上涨”判断突然失灵。这是条件模型，方向来自价格路径。

## 场景二：衰减区仍然被击穿

假设价格下行到5980绿色区域。对冲买压可能减缓下跌，但如果主动卖压更强，5980仍会失守。研究中可以先记录放缓是否出现，再等待价格重新接受5980上方；直接把绿区挂单买入没有体现该工具的条件性质。

若突破绿区后模型转紫，记录转换的实际时间，不能回放结束后把最终紫色套到此前绿色上。变化既可能来自仓位，也可能来自IV、时间及价格输入。

## 与其他指标组合

Summary Gex先判断整体Gamma环境；GEX Profile显示集中区；Levels Advanced提取少量水平位；Hedging解释接近时的反应方式。它们往往共享输入，四者一致不能解释成四个独立样本的“高胜率”。若GEX净值正而Hedging紫，先核数据时间和范围，再接受可能是模型考虑其他Greek的结果；公开公式不足以唯一解释差异。

## 媒体与验证范围

已查看总览、三色设置、Plot及综合图。[图像联系表](../assets/contact-sheets/option-gex-profile-hedging-de.jpg)。截图展示上下多档绿/紫，支持其是“分价位反应剖面”；不能通过截图推断具体买卖单、精确阈值或历史命中率。
