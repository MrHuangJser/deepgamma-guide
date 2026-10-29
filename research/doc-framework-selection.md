# DeepGamma 文档站框架选型

调研日期：2026-10-29。结论：**现阶段首选 Astro + Starlight；如果决定以 React 构建大量交互教学组件和更鲜明的产品界面，优先 Fumadocs；如果希望用最少配置把现有 Markdown 上线，选 VitePress。**

这次查阅官方文档、npm发布标签，并在浏览器实际查看了五家的官方文档页面。外观评价属于审美判断；性能部分依据渲染架构与资源处理能力，没有用同一套内容分别构建测速，不能作为实测快慢排行榜。

## 1. 本项目实际需要

现有内容以中文长文、19项指标配置、英文参数名、表格、图片与来源为主。开始本轮盘点时，分篇指南和研究正文约11.8万字符，另有内容重复的合订本；assets约36.7MB，包含图片、联系表和5.36秒视频。图片总大小不是单页传输量，但单个PNG约2MB，确实需要网页资源优化。

网站最有价值的功能是分组侧栏、页内目录、中英混合搜索、图片点击放大、手机可读参数表、桌面/Web版本对照、清楚的出处与更新日期。未来可加入Gamma符号演示、Expected Move计算器等交互。以上属于项目需求推导，不是现有网站已经实现的功能。

## 2. 五个候选怎么选

| 框架 | 官网实际外观的判断 | 性能与部署特点 | 内容迁移/维护成本判断 | 对本项目的定位 |
|---|---|---|---|---|
| **Astro + Starlight** | 三栏阅读清晰、留白充足，适合做精致的知识手册 | 静态内容与局部交互分开，默认Pagefind本地全文搜索；本地Markdown图片可经Astro优化 | 低到中；需加标题元数据及整理路由 | **综合首选** |
| **Fumadocs** | 圆角面板、细边框、导航和组件更接近现代产品文档 | 可静态化；当前官方文档支持多种宿主，性能取决于具体宿主与客户端组件 | 中；界面定制自由，MDX/宿主/搜索配置要一并管理 | **React交互与视觉定制首选** |
| **VitePress** | 干净、克制，默认风格偏开发者文档 | 静态首屏 + Vue客户端导航；内置MiniSearch，也可换搜索方案 | 低；现有Markdown复用直接，Vue增强交互 | **最省维护的实用选择** |
| **Nextra** | 简洁、规整，文档主题完成度高 | Next.js路线，可静态导出；Pagefind构建后索引 | 中；要处理MDX与Next配置 | 想用Next.js且偏好简洁文档主题时选 |
| **Docusaurus** | 传统技术文档风格，信息密度较高 | 预生成页面与React客户端导航；版本化/i18n等文档能力丰富 | 中；很多能力现成，精细改造主题需额外投入 | 未来长期保留多个文档版本时更有价值 |

功能依据：[Starlight](https://starlight.astro.build/)、[Fumadocs](https://www.fumadocs.dev/docs)、[VitePress](https://vitepress.dev/guide/what-is-vitepress)、[Nextra](https://nextra.site/docs)、[Docusaurus](https://docusaurus.io/docs)。官网可能使用定制布局，不能保证安装后不配置就与截图完全一致。

## 3. 为什么综合首选Starlight

当前任务主要是阅读与查找，Astro的静态HTML与按需交互方式很适合：文字不需要整体变成一个交互应用，计算器、图表演示可独立加载。**Starlight仍会为搜索、导航等功能使用JavaScript，并非整个网站零JS。**[Astro Islands架构](https://docs.astro.build/en/concepts/islands/)

Starlight直接支持Markdown，也能扩展MDX及React/Vue等组件。迁移时每页至少需要title元数据；图片可沿相对路径交给Astro的资源处理。它具备侧栏、目录、明暗模式、国际化等文档基础能力，适合把精力放在中文排版与图片可读性上。[内容与图片处理](https://starlight.astro.build/guides/authoring-content/)

其默认全文搜索使用Pagefind，构建时建立索引，不需要先购买或申请外部搜索服务。[Starlight搜索](https://starlight.astro.build/guides/site-search/)

Starlight官网有自身页面大小与碳排估算对比，但不是本项目的统一Lighthouse测试；本报告不据此断言它在所有场景快于其他框架。[官方性能说明的适用范围](https://starlight.astro.build/environmental-impact/)

## 4. 什么时候应改选Fumadocs

如果网站将从“手册”扩展为“可操作的交易学习平台”，需要更多React组件、互动图表、参数实验、卡片式学习路线，Fumadocs的组件和主题定制更有吸引力。其Core、UI、内容源分层可以组合；当前官方脚手架文档还列出多个宿主，不能沿用旧教程把它说成仅支持Next.js。[当前快速开始](https://www.fumadocs.dev/docs)

这并不意味着它必然需要常驻服务器，也不意味着React就一定慢。选择静态导出并控制客户端组件后，仍可作为静态文档部署；搜索、图片和动态功能需要按宿主分别配置。两种React方案的具体事实、中文搜索与迁移注意见[React框架核验笔记](react-doc-frameworks-notes.md)。

我的外观偏好是Fumadocs更适合做带品牌感的产品文档；Starlight更容易保持长文阅读的轻盈。这个判断不应替代用户对实际页面风格的选择。

## 5. 中文搜索不能只看“支持中文界面”

| 方案 | 已确认的事实 | 本项目需要验收什么 |
|---|---|---|
| Starlight / Nextra的Pagefind | Pagefind按HTML语言建索引；中文分词属于extended发行版能力，官方说npx默认用extended | 确保实际集成版本具备相应分词，页面语言为zh-CN；测连续中文与英文术语 |
| VitePress 1.6稳定版 | 有内置MiniSearch及自定义tokenize入口；界面翻译和分词是两件事 | 必须用真实中文查询测试，必要时自定义分词或换Pagefind |
| VitePress 2预览文档 | 主站明确写Intl.Segmenter进行中日文分词 | 不把预览版能力写成1.6稳定版保证 |
| Fumadocs | 当前主站内置搜索说明已更新，不能照旧教程固定认定为Orama | 按选定包版本核对搜索实现/API，验证静态部署与中文组合查询 |
| Docusaurus | 官方优先集成Algolia，文档也列社区本地搜索 | 不假设免费托管搜索自动获批；本地方案检查维护状况与中文效果 |

来源：[Pagefind中日韩分词](https://pagefind.app/docs/multilingual/)、[VitePress稳定版搜索](https://vuejs.github.io/vitepress/v1/reference/default-theme-search)、[VitePress预览版搜索](https://vitepress.dev/reference/default-theme-search)、[Docusaurus搜索](https://docusaurus.io/docs/search)。Fumadocs当前搜索源和静态模式见附属核验笔记。

建议验收查询：`负Gamma`、`做市商对冲`、`实时持仓量`、`平仓`、`Carry`、`OI-R`、`0DTE`、`Expected Move`、`Delta Revert`。标题命中优先，正文可定位到小节。给“负Gamma/负伽马”“实时持仓量/OI-R”等词建立别名是内容设计，不是仅靠搜索库会自动解决的问题。

## 6. 性能工作的重点

以下是根据现有资源推导的实施重点，没有声称已经完成优化：

1. **按分篇建站**。完整手册与章节重复，搜索默认不索引完整手册，合订本作为下载入口或排除索引的独立页面。
2. **图片分辨率分级**。正文用清晰的适中尺寸、点击放大再取原图；编码选择以文字截图清晰度与体积测试决定，不能为了AVIF/WebP把细字压糊。
3. **图片预留尺寸与懒加载**。首屏主要图优先，屏幕外图片延后，减少排版跳动。
4. **联系表放证据附录**。逐项指标页主要展示对应截图，避免一页加载全部媒体；5.8MiB视频点击后再加载。
5. **互动按需加载**。Mermaid可预渲染或按需加载；未来Greek演示、计算器无需让每一篇都带上图表库。
6. **字体尽量轻**。中文优先系统字体或精简自托管字体，避免首屏等待完整大字体或国外第三方字体服务。

这些工作通常比在宣传页比较一个分数更影响此项目体验。最终仍应拿同一篇含长表格和多图的指南，测首屏资源、LCP、CLS、INP和搜索首次响应；开发服务器的快慢不能代表生产站性能。

## 7. 迁移时保留哪些内容

保留现有Markdown为内容源，统一生成站点路由、标题与分组，转换本地.md链接并保持可追溯性。不要把汇编后的整册当唯一网页。图片原始来源、核验日期、假设标记与未公开算法边界都应继续保留。

当前正文有表格、1个分篇Mermaid流程图、很多中英文参数，以及少量未放在代码里的比较符号。MDX会把尖括号和大括号视为语法，不能仅把扩展名批量改成.mdx。选定框架后应逐页编译并检查相对图像路径、标题层级和锚点；Starlight添加frontmatter标题时，也要避免重复渲染原H1。

手机参数表需要水平滚动，图片支持放大与键盘关闭；左侧按“入门、指标、Web差异、交易基础、案例、证据”分组，右侧保留页内目录。桌面与Web对照适合用页签或并排卡片，内容以单一来源维护，避免复制后发生版本漂移。

## 8. 建议视觉方向

以可长时间阅读的浅色正文为默认，提供深色模式；使用石墨灰、青绿强调色，减少装饰渐变。保留指标截图自身的红绿紫语义，网页强调色不复用成新的交易信号。首页用“按指标查配置”和“按交易问题查场景”两条入口，而不是把所有章节堆成一个长目录。

这套视觉用Starlight和Fumadocs都能实现。选择差异主要在于希望有多少定制交互、偏好React还是Astro/Vue，以及后续维护者熟悉哪套工具。

## 9. 版本快照与结论边界

本次直接读取npm包注册元数据，`latest`快照为Starlight 0.42.7、VitePress 1.6.4、Fumadocs UI 16.17.9、Nextra 4.6.1、Docusaurus 3.10.2；VitePress的`next`为2.0.0-alpha.21。[包标签与兼容信息快照](doc-framework-package-snapshot.json)

这里是选型时点记录，不是安装锁文件。主站可能先于稳定包更新示例；实际实施必须固定兼容依赖并核对所选版本的API。没有安装依赖、构建五套站点或给出虚构跑分，也没有创建或发布网站。
