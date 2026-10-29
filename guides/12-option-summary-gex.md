# Option Summary Gex：做市商总Gamma、Delta与净流

**适用**：SPX。**来源**：[官方专页](https://www.deepcharts.com/helpcenter/article/option-summary-gex)。核验日2026-10-29；[Web差异](../research/web-desktop-differences.md)。

![官方界面总览，行情仅作显示示例](../assets/images/rDieXPPgDBso88cwPCg9hRB4NzQ.png)

## 指标名字不决定你选中的数据

默认聚合做市商Gamma，但可切到DEX或净Delta流。这时读数仍可能显示Regime系列名，却不能继续叫“Gamma环境”。先看Data source，再看符号和颜色。

添加：**New → Option Chart → SPX → Indicator Add → Option Summary Gex → + → 齿轮**。它是总量随时间变化，GEX Profile则是各档分布，两者维度不同。

## 四个数据源

| Data source | 默认／解释 | 正负值应怎样读 |
|---|---|---|
| Gex (Market Maker) | 默认，跨行权价做市商Gamma合计 | 对价格变化的敏感度符号，非涨跌方向 |
| Gex (OI R.T.) | 实时OI作底的Gamma口径 | 与MM净仓模型保持区别 |
| Dex (Market Maker) | 做市商Delta合计 | 方向敞口；若中性化，对冲方向相反 |
| Market Maker Δ | 做市商交易的净Delta流 | 期间新增流，非既有仓位总风险 |

官方未公开各源的完整单位、初始持仓、乘数与净额流程。不要对不同源沿用同一个“超过1M就强”的阈值。

## 全部显示配置

General的Expiration默认All，可0DTE、≤1/7/31/91d；Carry默认关。Marker默认关，正绿负紫、Value=0、Opacity20。Regime Subgraph默认绿/紫、Bars、Auto Color=+/−、Solid、宽4，可Line/Ignore；Name Label与Name Background关，Value Label与Value Background开，Chart color for marker关、Auto Center开；还有Short Name、第二色和线型，详见[Summary配置表](11-option-summary.md)。

桌面Marker画在价格主图；Web画在指标背景。推荐名称直接注明MM-GEX、MM-DEX或MM-Flow；若图表左侧仍只显示Regime，极容易把DEX正值错当长Gamma。

## 假设例子：DEX与GEX并不矛盾

假设某组合做市商总Delta是−1,000美元/点，但Gamma是+200美元/点²；同一时点核对ES月份，并近似 `dF_ES/dS_SPX≈1`。若要立即中性化Delta，约需买20张ES（每点50美元），而若标的再涨1点，Gamma使期权Delta约增加200美元/点，中性化时可能相应卖4张ES。这是“先买”与“涨后卖”同时合理的例子。

因此DEX回答当前方向风险，GEX回答价格变化时风险如何变。教学推导忽略IV/时间/其他仓位，不能把产品显示数值直接当这些美元单位。

## 场景：0DTE与All方向相反

假设0DTE Gamma为−300，其他期限合计+500，那么All为+200。日内近月风险放大与整体较正可以共存。研究时保留两个实例，记下期限；决定研究短时价格还是跨日背景，再选择相关口径，不能平均两数或多数表决。

若0DTE符号频繁切换，先检查值是否一直很靠近零、是否刷新导致台阶、是否存在到期临近Gamma急变。公开文档没有“持续N分钟才有效”的官方规则；你可以设研究规则，但必须标自拟并做样本外验证。

## 场景：用环境限制假说

假设Levels在6000，Summary Gex持续负。价格向上突破6000时，负Gamma也可能放大上涨，不能把紫色当做空。若看多延续假说依赖负Gamma且后来转正，就应重新评估动量可能被削弱，而不是无条件认为已经反转。

数据刷新、外部消息、模型覆盖与真实对冲地点都会限制解释力。把它与Hedging、Profile组合，是补充时空维度；不是获得多份独立的胜率证明。

## 图像核验

已查看General默认、Marker、Regime Subgraph和运行图。[联系表](../assets/contact-sheets/option-summary-gex.jpg)。正文说Bars默认，但另有Line显示示例；显示曲线不说明数据已变成平滑平均。负值向上走仍是负值，先读坐标再读颜色。
