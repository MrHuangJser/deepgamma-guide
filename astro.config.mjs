import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  site: 'https://mrhuangjser.github.io',
  base: '/deepgamma-guide',
  trailingSlash: 'always',
  integrations: [starlight({
    title: 'DeepGamma 研究手册',
    description: '从期权结构到交易场景，读懂 DeepGamma 的每个指标。',
    defaultLocale: 'root',
    locales: { root: { label: '简体中文', lang: 'zh-CN' } },
    social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/MrHuangJser/deepgamma-guide' }],
    customCss: ['./src/styles/custom.css'],
    components: { Footer: './src/components/Footer.astro' },
    sidebar: [
      { label: '开始阅读', items: [
        { label: '阅读路线', slug: 'generated/guides/00-start-here' },
        { label: '做市商分析主线', slug: 'generated/guides/market-maker-framework' },
        { label: '通用配置词典', slug: 'generated/guides/00-common-settings' },
        { label: 'Web 平台操作', slug: 'generated/guides/web-platform' },
      ] },
      { label: '指标配置与场景', items: [{ autogenerate: { directory: 'generated/indicators' } }] },
      { label: 'Web 专属指标', items: [{ autogenerate: { directory: 'generated/web' } }] },
      { label: '交易基础与实践', items: [
        { label: '期权与期货基础', slug: 'generated/research/market-foundations' },
        { label: '组合使用与复盘', slug: 'generated/guides/15-workflows-and-risk' },
        { label: 'Web / 桌面配置差异', slug: 'generated/research/web-desktop-differences' },
      ] },
      { label: '来源与核验', items: [
        { label: '图像与媒体证据', slug: 'generated/research/evidence-and-media' },
        { label: '覆盖与未知项', slug: 'generated/research/coverage-and-unknowns' },
        { label: '做市商指标来源复核', slug: 'generated/research/market-maker-source-review' },
      ] },
    ],
  })],
});
