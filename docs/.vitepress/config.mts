import {defineConfig} from 'vitepress'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    base: process.env.VITE_BASE,
    lang: 'zh-CN',
    title: "UMTK | UOS AutoTest Method ToolKit",
    description: "UOS AutoTest Method ToolKit",
    head: [
        // ['meta', {name: 'referrer', content: 'no-referrer-when-downgrade'}],
        ['link', {rel: 'icon', href: `${process.env.VITE_BASE || '/'}favicon.ico`}],
    ],
    vite: {
        publicDir: "assets",
        plugins: [
            // https://vitepress-auto-sidebar-plugin.netlify.app/
            AutoSidebar({
                // You can also set options to adjust sidebar data
                // see option document below
                collapsed: true,
                deletePrefix: "1A",
            })
        ]
    },

    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        siteTitle: "UMTK",
        nav: [
            {text: '🏠首页', link: '/index'},
            {text: "UTMK", link: '/umtk/1A简介.md'},

            {text: "SIG", link: '/SIG.md'},
        ],
        search: {
            provider: 'local'
        },
        ignoreDeadLinks: true,
        // =========================================================
        logo: {src: '/logo.png', width: 25, height: 30},
        socialLinks: [
            {icon: 'github', link: 'https://github.com/linuxdeepin-QAeggs/uos-method-toolkit'}
        ],
        footer: {
            copyright: `版权所有 © 2024-${new Date().getFullYear()} 统信软件`
        },
        //大纲显示2-3级标题
        outline: [2, 4],
        //大纲顶部标题
        outlineTitle: '当前页大纲',

        docFooter: {
            prev: '上一页',
            next: '下一页'
        },

        lastUpdated: {
            text: '最后更新于',
            formatOptions: {
                dateStyle: 'short',
                timeStyle: 'medium'
            }
        },

        langMenuLabel: '多语言',
        returnToTopLabel: '回到顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '主题',
        lightModeSwitchTitle: '切换到浅色模式',
        darkModeSwitchTitle: '切换到深色模式'
    },
});
