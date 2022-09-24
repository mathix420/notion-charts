<script lang="ts" setup>
useHead({
  link: [
    {
      rel: 'stylesheet',
      href: 'https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css',
    },
  ],
})
</script>

<template>
  <div id="__wrapper">
    <Head>
      <Html class="dark bg-gray-900 text-white px-5" />
    </Head>

    <NuxtPage class="container mx-auto -mt-10" />
  </div>
</template>
