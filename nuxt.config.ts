import eslintPlugin from 'vite-plugin-eslint'
import StylelintPlugin from 'vite-plugin-stylelint'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  vite: {
    plugins: [
      eslintPlugin({
        overrideConfigFile: '.eslintrc.js',
      }),
      StylelintPlugin({
        configFile: 'stylelint.config.js',
      }),
    ],
  },
  nitro: {
    preset: 'node-server',
  },
  // https://tailwindcss.nuxtjs.org/options
  tailwindcss: {
    configPath: 'tailwind.config.js',
  },
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    notionClientSecret: 'overritten-by-dotenv',
    aesEncryptionKey: 'overritten-by-dotenv',
    public: {
      notionClientId: 'overritten-by-dotenv',
    },
  },
})
