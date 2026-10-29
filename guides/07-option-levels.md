# Option Levels：把统计峰提炼为少量水平位

**适用**：SPX、SPY、NDX、QQQ。**来源**：[官方专页](https://www.deepcharts.com/helpcenter/article/option-levels)。核验日2026-10-29；Web默认有差异，见[对照表](../research/web-desktop-differences.md)。

![官方界面总览，行情仅作显示示例](../assets/images/adT8WNpn7EQ34x6GIdnz6hZNlZ0.png)

## 功能与读图

从所选统计中抽取关键行权价画水平线；三角形数量表达相对排名，越多代表在当前比较集合中更集中。绿色向下三角对应正侧，红色向上三角对应负侧；这不是向下/向上价格预测。黄色Zero Gamma另列，不受Number of levels控制。

添加：**New → Option Chart → 选标的 → Indicator Add → Option Levels → + → 齿轮**。模板C/P L可作快捷入口。要看完整分布而非只看头部几档，用Option Profile。

## 数据源选择

| 选项 | 默认／含义 | 场景 |
|---|---|---|
| Gamma (Call − Put) | 默认；按传统量×Gamma Call减Put | 看风险敏感的集中位 |
| Call/Put Σ | 原始Call/Put量 | 看当日活跃墙 |
| OI (Eod) | 以前次日终OI作底 | 看带入结构 |
| Gamma (Call OI-E − Put OI-E) | OI作底的Gamma模型 | 对比存量Gamma与当日活动 |

前三者和第四者的排序可能完全不同，不应沿用同一套“强度”解释。切到OI时，黄线的精确计算关系未公开；不要宣称原始量“自动知道”真实做市商Gamma翻转点。

## General与Plot完整表

| 字段 | 桌面默认／选项 | 使用含义 |
|---|---|---|
| Expiration | All；0DTE、≤1/7/31/91d | 固定期限才能横向比排名 |
| Include Carry or Open Interest | 关 | 是否带入前期存量 |
| Number of Strikes (0 - unlimited) | 0 | 计算行权价范围；不是画几条线 |
| Number of sessions | 1 | 历史交易日线延伸范围 |
| Number of levels | 2 | 绘制关键位数量；是否按正负两侧分别计数正文未精确定义，实际核对 |
| Extension mode | Till interaction默认；None / Till end window | 画当前；延伸到触碰；延伸到视窗末端 |
| Text size、Custom header | 11、可自定 | 名称标清源和期限 |
| Align previous/current values on right | 开／关 | 历史与当日标签位置 |
| Positive/Negative/Zero color | 绿／红／黄 | 只在此口径内解释正负 |
| Lines width、Lines style | 1、Dash | 还可Solid/Dot/Dash dot/Dash dot dot |

Till interaction是画线延伸规则，不是止损、自动成交或支撑失效检测。历史线仍可供复盘，但不保证其对应仓位仍存在。

## 假设例子：排名变化不等于新增仓位

假设6000统计值300、6020为200、6040为100；稍后6000降到150，6020仍200，则6020可能变成第一名。三角形增加但6020绝对值没增加。所以排名只表相对强度，必须回Profile核对绝对值与来源。

研究者建议先显示2到3个关键位，固定Strikes=0作为基准，记录Level、排名、值、时间。若范围太远影响画面，先调显示，研究有限Strikes前保存一套全范围对照。

## 假设例子：到达、拒绝与接受

现价6000，上方6020为强正侧线。价格首次触及6020停顿并回落，是“拒绝候选”；若随后在6020上方连续成交并回踩守住，则原先的阻力假设不成立。线上下方向不是最终结论，实际接受/拒绝才决定如何记录情景。

下方5980负侧线也不能默认“Put墙必支撑”。负Gamma对冲在下行中可能顺势卖出。先用Summary核对总环境，必要时看Hedging。Zero Gamma上方通常偏稳定、下方偏放大只是官方的简化启发式，详见[Envelopes](09-option-envelopes.md)的适用条件。

## 图像核验与排错

已检查默认参数图、三角数量放大图和Plot图；确认线色、三角方向和排名，而非推测箭头含义。[联系表](../assets/contact-sheets/option-levels.jpg)。线太多先查sessions和levels，黄线不出现先查坐标范围、计算数据及是否有可用翻转点；不能擅造“黄线等于零价格”。
