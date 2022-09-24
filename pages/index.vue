<script lang="ts" setup>
const config = useRuntimeConfig()
const clientId = config.public.notionClientId
</script>

<template>
  <main class="flex flex-col items-center justify-center h-full">
    <h1 class="text-3xl font-black mb-5 text-center">Notion Charts.</h1>
    <!-- Sign in with Notion -->
    <a
      role="button"
      :href="`https://api.notion.com/v1/oauth/authorize?owner=user&client_id=${clientId}&response_type=code`"
      class="text-white bg-[#000000] hover:bg-[#000000]/90 focus:ring-4 focus:outline-none focus:ring-[#000000]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#000000]/50 dark:hover:bg-[#000000]/30 mr-2 mb-2"
    >
      <svg
        role="img"
        class="mr-2 -ml-1 w-5 h-5"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
        fill="white"
      >
        <path
          d="M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0 .84-1.168.84l-3.222.186c-.093-.186 0-.653.327-.746l.84-.233V9.854L7.822 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764 7.279v-6.44l-1.215-.139c-.093-.514.28-.887.747-.933zM1.936 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54 1.447-1.632z"
        />
      </svg>
      Sign in with Notion
    </a>
    <!-- Learn more on GitHub -->
    <a
      href="https://github.com/mathix420/notion-charts"
      target="_blank"
      class="absolute bottom-10 inline-flex justify-center items-center px-5 py-4 mx-3 text-base font-medium text-gray-500 bg-gray-50 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white"
    >
      <svg
        class="mr-3 w-8 h-8 fill-gray-400"
        aria-hidden="true"
        role="img"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
        />
      </svg>
      <span class="w-full">Learn more about Notion Charts</span>
      <svg
        aria-hidden="true"
        class="ml-3 w-6 h-6"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
          clip-rule="evenodd"
        ></path>
      </svg>
    </a>
  </main>
</template>

<style lang="scss">
html,
body,
#__nuxt,
#__wrapper {
  height: 100%;
}
</style>
