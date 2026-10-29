# DeepGamma功能覆盖与证据边界

核验日期：2026-10-29。覆盖范围以官方公开目录、产品页及平台总览为准。共19个跨版本去重指标，桌面有14篇专页，Web有19篇；同一指标的数据源与显示功能也纳入指南，不把快捷按钮重复计数。

## 指标覆盖

全部19项与文件的一一映射在[总目录](../README.md)。14项共通指标每篇记录桌面添加步骤、全部公开参数组、默认值、含义、原创数值/情景和失效条件；Web新增字段、默认值与例子集中在[跨版本配置](web-desktop-differences.md)。五项Web额外指标各有独立篇。

| 组别 | 指标数量 | 配置覆盖 | 图像覆盖 |
|---|---:|---|---|
| 标准量/结构 | 6：Volume、Profile、Levels、Envelopes、Summary、Expected Move | 期限、数据源、Carry及该指标公开显示字段 | 每页已读取联系表 |
| SPX分类数据共通 | 8：Delta、Big Flows、GEX Profile、Hedging、Levels Advanced、Envelopes Advanced、Summary Gex、Heatmap | 各自源/Value、过滤、显示及其公开默认 | 每页已读取联系表，关键配置原图附文 |
| Web额外 | 5：Net Flow、Dynamic Walls、Pressure、Sentiment、Exhaustion | 全部专页公开Parameters/Series及模型边界 | 34幅独特功能截图，见专用manifest |

## 平台与交叉功能覆盖

| 功能 | 保存位置 | 确认程度 |
|---|---|---|
| 桌面Option Chart新建、四标的选择 | [开始使用](../guides/00-start-here.md) | 官方步骤与选择器截图 |
| 指标添加、启停与设置窗口 | [开始使用](../guides/00-start-here.md)、[通用参数](../guides/00-common-settings.md) | 官方步骤、截图可见外壳 |
| 桌面快捷模板与共享模板 | [开始使用](../guides/00-start-here.md) | v16说明及模板栏/文件选择器图 |
| Web账号入口、连接、菜单、主题 | [Web平台](../guides/web-platform.md) | 官方平台总览，未注册账号 |
| Web图表类型、周期、ETH/RTH、Price/Grid | 同上 | 已公开的项目与默认值 |
| 多图Layout、符号Sync、独立窗口与全屏 | 同上 | Sync仅确认符号同步，不扩写其它同步 |
| Template、Workspace、Save | 同上 | 官方描述范围，云冲突机制未公开 |
| 快捷键、绘图、右键菜单 | 同上 | 所有公开工具及快捷键 |
| 全局Expiration与单指标Override | 同上及[跨版本配置](web-desktop-differences.md) | Default继承；例外单列 |
| To Futures Price与换月 | 同上及[组合流程](../guides/15-workflows-and-risk.md) | 默认关、自动选月份、换月偏差已说明 |
| Session、Replay、历史范围 | 同上 | 操作步骤有说明；精确可选历史受账号约束 |
| Peak、Rolling M1/M5/M15/M30、Flip only | [参数词典](../guides/00-common-settings.md)、[跨版本配置](web-desktop-differences.md) | 默认、阈值和公开限制 |
| Profile Summary、Sizing、Strike grid | 同上 | 区分显示变换、数据聚合与统计量 |
| 市场含义与数学 | [基础研究](market-foundations.md) | 23项OIC/Cboe/CME等一手来源 |
| 教学布局、情景、单位、风险与复盘 | [组合流程](../guides/15-workflows-and-risk.md) | 原创研究方案，非经验证策略 |
| 做市商阅读主线、库存与流量、目标对冲与新增订单、冲突处理 | [做市商分析](../guides/market-maker-framework.md)、[来源复核](market-maker-source-review.md) | 产品定义与教学推导分开；Cboe具体数据产品不等同DeepGamma供应合同 |

## 没有把哪些东西写成已知

| 未公开/未验证问题 | 目前能确认什么 | 使用上的处理 |
|---|---|---|
| MM持仓、GEX、DEX精确后台公式 | 官方称SPX用CBOE参与者数据 | 不反向编造Greek曲面、符号和单位缩放 |
| OI-R清算一致性、初始种子与开平净额 | 平台按实时分类流构建 | 不叫交易所实时清算OI，不用买卖差定义全市场OI |
| Carry对每个源的精确算式 | 官文描述带入结转/持仓 | 配置记录，跨图统一；不再手加一份OI |
| Zero Gamma求根、无根/多根及非Gamma源关系 | 界面显示翻转参考 | 不断言永远唯一或上方永远为正 |
| 期货等价量转换 | 桌面Volume/Delta有Future contracts选项 | 未知乘数/Delta规则时不当真实成交张数 |
| Web Delta MM源与Revert联动 | 两者均在文档中存在 | 避免重复反号，名称标清视角 |
| Expected Move IV选择、时钟和锚点 | IV范围、Daily/Thirty minute和显示档 | 通用公式只作教学，不声称精确重现 |
| Hedging/动态墙/压力/情绪/衰竭内部模型 | 专页描述用途与公开控件 | 不猜Vanna/Charm、概率、训练或盈利率 |
| Flip only百分比分母与重绘 | Web公开筛选和阈值 | 不把它叫最大变化排行榜或确定开仓检测 |
| 实时端到端延迟和修订 | 约每分钟刷新/1分钟分辨率描述 | 记录数据时间，不当逐笔工具 |
| 回放是否逐点保留发布时状态 | 有Replay及历史访问描述 | 不承诺无重绘、无回填或自动无前视回测 |
| 声音/触碰提醒、API、导出、自动交易 | 当前研究目录无足够公开配置证据 | 不把功能缺文档说成确定不存在，也不声称可用 |
| Technical analysis分组的完整指标表 | 平台总览仅用ATR、Bollinger bands等作示例 | 已覆盖分组入口；未公开的完整清单和参数不编造，19项数量指专门的期权指标目录 |
| 桌面Protected、保存作用域 | 截图有相应控件 | 单列待核实，不猜成风控锁仓 |
| 完整套餐、订阅和行情权限 | Web有独立订阅及无需额外feed说明 | 未登录用户账号，具体权限以当前账户为准 |

## 访问与验证边界

免费Demo真实入口要求姓名、邮箱和条款确认，公开页限定Replay。未提交个人资料或注册，因此没有把付费后的真实界面、服务器数值或执行行为写成已经实测。当前资料足以编写公开功能配置与使用指南，以上未公开实现保留为明确边界，不通过猜测填补。

这份清单用于控制结论强度，而不是要求用户在阅读前另行确认。后续如提供实际版本截图或官方更新，可沿源清单增量修订，不必重新组织整套文档。
