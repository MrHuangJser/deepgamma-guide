# Option Summary：传统Gamma模型的总量时间序列

**适用**：SPX、SPY、NDX、QQQ。**来源**：[官方专页](https://www.deepcharts.com/helpcenter/article/option-summary)。核验日2026-10-29；[Web差异](../research/web-desktop-differences.md)。

![官方界面总览，行情仅作显示示例](../assets/images/a0OBa037eI31t8aazVqwDrXDPvI.png)

## 它和Profile里的Summary不是同一操作入口

这是独立副图指标，把所选范围的传统净Gamma模型聚合为单一时间序列。Profile里的Summary只是当前剖面的汇总显示开关；两者口径一致时可能密切相关，不能当两份独立确认。

默认绿色正值、紫色负值，读的是模型净Gamma符号。正Gamma不等于看涨，负Gamma不等于看跌；方向来自实际价格与其他流量。普通版没有直接分类恢复做市商净头寸。

添加：**New → Option Chart → 选标的 → Indicator Add → Option Summary → + → 齿轮**。

## 全参数

| 分组 | 字段 | 桌面默认／选项 |
|---|---|---|
| General | Data source | 唯一Gex (Call − Put)，不能切MM源 |
| General | Expiration | All；0DTE、≤1/7/31/91d |
| General | Include Carry or Open Interest | 关 |
| Marker | Enable | 关 |
| Marker | Positive / Negative color | 绿 / 紫 |
| Marker | Value | 0，变色阈值 |
| Marker | Opacity | 20 |
| Regime (1) | Color / 2° Color | 绿 / 紫 |
| Regime (1) | Style / Auto Color / Line / Width | Bars / +/− / Solid / 4，可Line、Ignore |
| Regime (1) | Name Label / Background | 关 / 关 |
| Regime (1) | Value Label / Background | 开 / 开 |
| Regime (1) | Chart color for marker / Auto Center | 关 / 开 |

还有Short Name及备用色/线型设置，见[通用字段词典](00-common-settings.md)。Marker在桌面主价格图画环境背景；Web正文明确是指标面板背景，不按桌面截图找主图色带。

若Marker Value改成非零，背景划分不再严格等同Gamma正负。例如阈值+100时，值+50虽然数学上仍正，可能落在阈值另一侧。**这种阈值配色不要叫真实Gamma翻转**；研究者建议初始保留0。

## 假设数值：合计正值仍可能有局部风险

假设三个档贡献+300、+200、−400，总和+100。Summary为正，但−400所在价位可能有明显局部负敏感度。把全图“绿色”理解成每一档都抑制波动，会丢失重要信息。继续看Profile/Levels辨认局部区。

若+100降到+20，是正Gamma减弱，不是已经转负；若Auto Color改Slope，下降阶段可变成第二色，必须看零轴而不是颜色。跨日幅度比较需同期限、Carry、时点及单位。

## 场景：调整观察方式而不是直接押方向

假设模型持续正值，价格在5980—6020区间且多次冲出失败，可以研究均值回归候选。若出现重大消息并突破区间，正Gamma并不阻止趋势，原先区间研究失效。

假设Summary跨零变负，价格也脱离区间，可研究趋势延续候选；但如果负值状态下价格回到横盘，不能为了符合模型反复追单。研究重点是Gamma符号是否改变了条件分布，而不是事后给每段走势贴标签。

## 配置与排错

建议同时保留数值标签与零轴参照；Marker开时用低Opacity，别遮住价格。普通Summary不能切做市商数据，SPX需要该口径时另加Summary Gex。0DTE与All相反时，可能是不同期限贡献抵销；不要对两个统计做简单多数表决。

已看General、Marker、Subgraphs及总览。[图像联系表](../assets/contact-sheets/option-summary.jpg)。某截图在负值区出现绿色柱，可能与示例配色/斜率设置有关；默认判读应以所选Auto Color及实际值确认。
