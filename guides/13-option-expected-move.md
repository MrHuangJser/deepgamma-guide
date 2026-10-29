# Option Expected Move：隐含波动范围与超预期移动

**适用**：SPX、SPY、NDX、QQQ。**来源**：[官方专页](https://www.deepcharts.com/helpcenter/article/option-expected-move)。核验日2026-10-29；[Web差异](../research/web-desktop-differences.md)。

![官方界面总览，行情仅作显示示例](../assets/images/km3AbuPelFQpX2uUQKoCgZ47Ntg.png)

## 区间意味着什么

把期权隐含波动信息转换为主图上的动态价格范围，Range是填充带，Range+是上边界，Range−是下边界。它回答“这一幅度相对定价的波动有多大”，不直接给方向，也不是Gamma墙。

官方用约70%/95%描述一倍/两倍标准差收盘范围。严谨地说，在特定分布和模型下，一倍约68.27%、两倍约95.45%；**这是条件化分布直觉，不是本指标已实现的历史覆盖率，更不是实盘收盘保证**。95%是更高覆盖率的宽区间，低概率的是落到区间外，不是“宽区间本身更不可能”。

添加：**New → Option Chart → 选标的 → Indicator Add → Option Expected Move → + → 齿轮**。

## 全参数配置

| 字段 | 桌面默认与选项 | 场景 |
|---|---|---|
| Interval | Daily默认；Thirty minute | 全交易日参考；滚动30分钟短时参考 |
| Value | One standard deviation默认；Average、Two standard deviation | 一般幅度、无指定概率的平均估计、较宽尾部参考 |

Web把Average称Normal，不能仅凭改名断言算法完全相同。该指标没有在正文给Expiration过滤，不要为了“与0DTE一致”编造不存在的菜单。

| 序列 | 桌面默认 | 其他显示字段 |
|---|---|---|
| Range (1) | Type=Range；可Hidden；None、Solid、宽1、Auto Center关 | Line/Background和第二套线/背景色，标签、背景、Short Name等 |
| Range+ (2) | 绿、Hidden；可Line/BrokerLine；None、Solid、宽1、Auto Center关 | Short Name默认0DTE R+ |
| Range− (3) | 紫、Hidden；可Line/BrokerLine；None、Solid、宽1、Auto Center关 | Short Name默认0DTE R− |

上下边界还各有2° Color、Name/Value Label、Name/Value Background、Chart color for marker，作用见[通用词典](00-common-settings.md)。截图显示边界被设为Line，正文默认却是Hidden：只看到填充带不一定是数据坏了，需在Subgraphs主动打开边界。

![Daily与一倍标准差配置](../assets/images/zihf8XmDBpT52fhbPdV5oT5B76A.png)

## 一个能复核的教学计算

常见的简单幅度近似为 `EM ≈ S × 年化IV × √T`。假设S=6000、IV=20%、T=1/252年，则一倍幅度约 `6000×0.20/√252=75.59点`，参考上下边界约5924.41与6075.59；两倍约151.19点。

这不是DeepGamma公开源码。它没有说明锚定现价、开盘或另一参考价的全部细节，也没有公开IV取哪条期权、如何插值、用252还是365日、如何处理隔夜和事件。截图显示带会随时间阶梯变化，不能将本教学的固定上下边界冒充产品精确输出。

若示范用390分钟交易日时钟，30分钟对应 `T=30/(390×252)`，同假设下幅度约20.97点。换日历时钟或加入隔夜风险会不同；**不要固定把平台Daily读数除以√13就当真实Thirty minute结果**。

## 场景一：接近上沿是否该卖

假设当前带为5925—6075，价格6068。它说明距上沿7点，剩余参考空间有限；不说明6075一定反转。若Summary正、Hedging衰减、价格在上沿外无法接受，可研究回归；若外部消息推动、IV上升、带扩张且价格接受上方，可研究趋势扩张。

将一次上破称为“低概率事件”也要先固定预测时点、区间和结束时点。动态带每分钟更新时，事后用最新宽带去评价早盘预测会造成前视偏差。

## 场景二：突破与波动重定价

假设价格从6000急升至6080，原上沿6075，但新的上沿变为6110。可能既有价格锚变化，也有IV变化；不能只看“最终仍在带内”就声称原范围预测成功。研究应保留10:00当时发布的范围，单独评价10:00到指定终点的结果。

期权买方还需比较实际波动、IV支付和Theta，看到价格大幅走动不保证买期权盈利；期权卖方也不能因95%区间宽就忽略尾部损失。基础关系见[IV与Greeks研究](../research/market-foundations.md)。

## 配置建议与复盘

先用Daily、一倍标准差、Range淡填充、两边界Line，名称写清Daily-1SD。想研究尾部另开两倍实例；比较不同周期时固定起点和终点，记录IV环境与数据刷新。

每个样本记：预测时刻、当时上下沿、后续最高/最低、终点收盘。**触碰概率与终点落在带内概率不同**；不能把“盘中越界过”与“收盘越界”混合统计。没有分布假设和样本外覆盖验证，不给该工具贴固定概率保证。

已识读总览、参数、Range/上下界设置及示例图。[联系表](../assets/contact-sheets/option-expected-move.jpg)。图支持动态带与独立边界可见性，不能确定IV精确源或计算时钟。
