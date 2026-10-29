# Fumadocs 与 Nextra：本项目的 React 文档框架选型

核验日期：2026-10-29。仅调研当前官方文档，没有安装依赖、创建网站或运行性能基准。Fumadocs 使用主站 `www.fumadocs.dev` 的当前文档，不以 `v14.fumadocs.dev` 为依据；Nextra 使用主站当前 App Router 路线。文中“事实”是官方公开能力，“判断”是针对本项目的取舍。

发布版本另见同次调研的[npm官方registry快照](doc-framework-package-snapshot.json)：Fumadocs UI为16.17.9、Nextra为4.6.1。官网正文可能比已发布包先行，尤其下面的ZBSearch描述；本文不据主站文字保证16.17.9已包含相同实现。实施前须按选定包版本核对API、依赖及搜索后端，不能将文档主站、旧v14页面和不同发布包拼接使用。

## 结论

**判断：若希望做可持续扩展、较有设计自由度的 React 阅读站，优先 Fumadocs + Next.js 静态导出；若优先尽快采用标准文档布局、希望 Mermaid 少做集成，Nextra 很合适。** 本项目不需要按请求运行的服务器，也没有因中文而必须使用云搜索的理由。两者都能完成任务，中文搜索支持不是排除任何一方的依据。

本地只读盘点时有30个 Markdown 文件、约24.2万字符；其中《DeepGamma完整手册.md》约12.1万字符，是汇编副本。排除它后约12.2万字符，与“约11万”的内容规模接近；另有74处 Markdown 图片引用、1330行以竖线开始的表格内容、2处 Mermaid 围栏（汇编与拆分版含重复），没有 YAML frontmatter。网站应以拆分章节为主要内容源，汇编提供下载或排除搜索，避免结果一式两份。这是本地盘点，不是框架基准。

## 可核验的能力比较

| 维度 | Fumadocs 当前文档事实 | Nextra 当前文档事实 | 本项目取舍 |
|---|---|---|---|
| React 框架 | 官方集成 Next.js、React Router、TanStack Start、Waku；另有 Astro；Core、UI、内容层分离。[安装入口](https://www.fumadocs.dev/docs/manual-installation)、[Core](https://www.fumadocs.dev/docs/headless) | Next.js 插件；当前文档明确 Nextra 4 只支持 App Router，旧 Pages Router 是1/2/3路线。[介绍](https://nextra.site/docs) | 未有既定应用框架时，Fuma保留更多选择；Nextra的Next约束对本项目并非障碍 |
| 静态站 | 默认偏服务器方案，但官方支持静态导出；Next用 `output:'export'`，React Router/TanStack也有SPA及预渲染说明。[静态构建](https://www.fumadocs.dev/docs/deploying/static) | 官方支持静态导出到 `out`，示例使用 `output:'export'`、`images.unoptimized:true`。[静态导出](https://nextra.site/docs/guide/static-exports) | 两者都可部署在普通静态托管；构建时仍需Node工具链，线上不必常驻Node |
| 文档布局 | UI含侧栏、移动导航；页面组件有目录、面包屑等。可选Docs、Notebook、Flux、Glass、Spacious等布局。[布局](https://www.fumadocs.dev/docs/ui/layouts/docs)、[定制](https://www.fumadocs.dev/docs/guides/customize-ui) | Docs Theme已有导航、搜索、侧栏、TOC；官网自身使用该主题。[主题入门](https://nextra.site/docs/docs-theme/start) | 都满足指标目录＋章节阅读。选择应看中文正文宽度、长表和大截图，不看首页动画 |
| 主题扩展 | 当前UI只支持Tailwind CSS 4；有配色预设、CSS主题变量、组件props及CLI复制布局到本地；复制后的组件需自行维护。[主题](https://www.fumadocs.dev/docs/ui/theme)、[定制边界](https://www.fumadocs.dev/docs/guides/customize-ui) | 支持Next的CSS、CSS Modules与Sass；可配置主题组件、页面元数据，或自建主题。[CSS](https://nextra.site/docs/guide/custom-css)、[页面结构](https://nextra.site/docs/file-conventions/meta-file)、[自建主题](https://nextra.site/docs/custom-theme) | Fuma的分层与布局插槽更贴合长期定制；Nextra也能深改，不能说它“只能改颜色” |
| 普通Markdown | 官方内容层收集 `.md` 与 `.mdx`，提供TOC、结构化搜索数据等。[内容层](https://www.fumadocs.dev/docs/mdx) | `content`目录收集 `.md`、`.mdx`，不必每章改名为`page.mdx`；`_meta`控制导航排序。[文件约定](https://nextra.site/docs/file-conventions/meta-file) | 保留Markdown为内容真源，React组件按需添加，无需批量改成MDX |
| 表格与Mermaid | GFM受支持；Mermaid没有默认包装组件，官方给出渲染器与`remarkMdxMermaid`转换方案。[Markdown](https://www.fumadocs.dev/docs/markdown)、[Mermaid](https://www.fumadocs.dev/docs/markdown/mermaid) | GFM表格支持；Mermaid围栏内置转为组件。[Markdown](https://nextra.site/docs/guide/markdown)、[Mermaid](https://nextra.site/docs/advanced/mermaid) | Nextra在现有Mermaid围栏上集成更省事；两者都需检查中文节点、深浅色与窄屏横向阅读 |

审美判断：Fumadocs的多布局与分层适合塑造更克制的知识库界面；Nextra Docs Theme更适合直接采用熟悉的文档站结构。这里没有构建同一内容的双站视觉对照，不能把这种设计取向写成“某个必然更漂亮”。本项目真正的视觉工作是截图可放大、表格可横滑、正文行长适中和导航分组清楚。

## 搜索：两个过时印象需要纠正

**Fumadocs事实：** 当前主站的 Built-in Search 专页路径仍包含 `orama`，但正文已推荐 **ZBSearch**，默认 `multilingual` 使用 Unicode 分词，明确包括中文和日文。静态站使用 `staticGET`导出索引，并切换静态客户端/搜索UI；搜索由浏览器执行，不是把动态搜索API留在静态主机上。静态模式会下载导出的索引，大站需要评估成本。不能从旧版文章直接沿用“默认Orama且中文不支持”的结论。[当前搜索文档](https://www.fumadocs.dev/docs/headless/search/orama)

**Nextra事实：** 当前搜索是 **Pagefind**，构建之后索引HTML，并输出`_pagefind`资源；须显式完成`postbuild`，不能只看到搜索框就认为索引已经生成。官方静态导出示例为 `pagefind --site .next/server/app --output-path out/_pagefind`；路径是当前文档示例，应与最终锁定的Next版本产物核对。[搜索安装](https://nextra.site/docs/guide/search)

**Pagefind中文事实：** 依`<html lang>`选择语言索引；中日韩的非空格分词需要extended发行版，官方说明`npx pagefind`默认就是extended。它提供分词，不应误称中文词干还原；Nextra搜索框文案仍可单独本地化。[Pagefind多语言](https://pagefind.app/docs/multilingual/)、[Nextra Search组件](https://nextra.site/docs/built-ins/search)

**无基准推断：** 约30页、去重约12万字符的规模，优先本地静态搜索是合理起点；没有测量过索引压缩体积、首次查询时延或手机内存，不能声称任何一方“快几倍”。图片字节不需要进入正文索引，但截图上的字也不会自动变成可搜索内容；应保留现有正文中的字段解释和图片alt。

选型验证应覆盖至少：`未平仓`、`做市商对冲`、`衰竭`、`实时OI`、`0DTE`、`GEX`、`Include Carry`、`Put sell`、中文片段与中英混写。分别观察命中章节、结果排序及片段定位；没有这一步，不能把“支持中文”当成符合本项目需求的召回率证明。

## 本项目迁移时最容易漏的内容

1. **文章标题与导航名。** 当前每页已有一级标题、没有frontmatter。Fuma常用frontmatter title配合页面标题组件，若又保留正文H1可能重复；应选择统一标题策略，而不是为了框架先改写全部正文。Nextra可保留`content`文件名并用`_meta`设置中文标题与顺序；不要让`01-...`和研究笔记按字母混排。[Fuma标题约定](https://www.fumadocs.dev/docs/markdown)、[Nextra `_meta`](https://nextra.site/docs/file-conventions/meta-file)
2. **文件链接不等于网页路由。** 大量`07-option-levels.md`、`../research/...md`链接，不能只把文件复制进内容目录就认定最终URL正确。需要保留文件到路由的映射，统一处理扩展名、目录、锚点与部署子路径，并逐条检查。框架把链接转换成React/Next Link不等于自动保证本仓库的文件链接语义。[Nextra Link](https://nextra.site/docs/guide/link)、[Fuma链接](https://www.fumadocs.dev/docs/markdown)
3. **本地图片路径。** 当前多数`../assets/...`依赖源文件位置。Fuma的图片插件在启用导入时支持相对图路径，关闭导入则需确保资源实际可访问；Nextra支持Markdown静态图和相对导入。移动章节时应保持目录关系，或在构建适配层映射到`public`；不能只复制Markdown。[Fuma图片](https://www.fumadocs.dev/docs/headless/mdx/remark-image)、[Nextra图片](https://nextra.site/docs/guide/image)
4. **静态导出与图片优化。** Nextra示例明确关闭默认优化；Fuma若选Next也受Next相同限制。静态导出不提供默认按请求图片优化服务；可用未优化图片或自定义loader，但“静态图识别尺寸”不等于“部署后动态压缩”。本项目应保留原图可读性，再另做缩略图策略。[Next静态图片限制](https://nextjs.org/docs/app/guides/static-exports)
5. **MDX语法。** 不要无理由将所有`.md`改为`.mdx`。MDX中的未转义`<`、`{`、HTML注释及非闭合标签会触发不同语法；先检查普通Markdown编译路径，只为需要React组件的少数页面启用MDX。官方MDX说明可以通过格式或扩展名区分Markdown与MDX；两框架的具体处理以锁定版本验证。[MDX语法差异](https://mdxjs.com/docs/what-is-mdx/)、[Nextra格式配置](https://nextra.site/api/nextraconfig)
6. **内容去重与证据附件。** 汇编手册、源清单JSON、联系表和研究记录不宜全部进入同一导航与搜索。章节正文正常索引，证据附件可单独下载；这是本项目的信息架构决定，并非框架自动替你完成的功能。不要把源码、内部采集清单误做普通阅读章节。

## 推荐决策条件

选 **Fumadocs**：希望保留React框架选择、后续做更独特的章节导航或数据解释组件，并愿意补一层Mermaid和内容适配。建议从官方Next静态模板、标准Docs布局和本地静态搜索开始，暂不加入AI聊天或自建服务器。

选 **Nextra**：已经接受Next App Router，目标是用文档主题快速承载现有内容，喜欢默认导航，且希望Mermaid直接沿用。重点是Pagefind后构建流程、中文lang、图片静态输出和`_meta`目录整理。

两者都应先锁定实际版本，再用一篇长表页、一篇多图页和一篇Mermaid页做最小验证；当前文档变化较快，特别是Fuma搜索引擎与Tailwind配置，不能混用旧v14安装教程。本次不执行这一验证，也不据未经测量的构建速度或包体积决定胜负。
