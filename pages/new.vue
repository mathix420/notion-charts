<script lang="ts" setup>
const token = useCookie('nct-v1')?.value || undefined
const { data, pending, error, refresh } = await useLazyFetch('/api/notion/databases', {
  query: { token },
})

const database = ref(undefined)
const selectedDb = computed(() => {
  const res = unref(data)
  if (!res) return {}
  return res?.results?.find?.((x) => x.id === unref(database))
})

function parseTitle(db) {
  return [db?.icon?.emoji]
    .concat(db.title.map((x) => x?.text?.content))
    .filter(Boolean)
    .join(' ')
}
</script>

<template>
  <main class="flex flex-col items-center justify-center h-full">
    <h1 class="text-3xl font-black my-5 text-center">New chart</h1>

    <!-- Loading -->
    <div v-if="pending" role="status">
      <svg
        aria-hidden="true"
        class="mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
      <span class="sr-only">Loading...</span>
    </div>
    <!-- Error -->
    <div
      v-else-if="error"
      class="flex p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
      role="alert"
    >
      <svg
        aria-hidden="true"
        class="flex-shrink-0 inline w-5 h-5 mr-3"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
          clip-rule="evenodd"
        ></path>
      </svg>
      <span class="sr-only">Error</span>
      <div>
        <span class="font-medium">An error occurred!</span> You may want to try again in some time.
      </div>
    </div>
    <!-- Databases -->
    <div v-else class="w-full sm:w-96">
      <label for="database" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400">
        Select a database
      </label>
      <div class="flex">
        <select
          id="database"
          v-model="database"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        >
          <option selected :value="undefined">Choose a database</option>
          <option v-for="res in data.results" :key="res.id" :value="res.id">
            {{ parseTitle(res) }}
          </option>
        </select>
        <button class="ml-3" aria-label="Refresh databases" @click="refresh">
          <i class="fi fi-br-refresh" />
        </button>
      </div>
    </div>
    <div v-if="database && selectedDb" class="w-full sm:w-96 mt-5">
      <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400">
        Select fields
      </label>
      <div class="flex">
        <input
          type="text"
          class="rounded-none rounded-l-md bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Field name"
        />
        <span
          class="inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border border-gray-300 dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600"
        >
          :
        </span>
        <select
          class="rounded-none bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        >
          <option v-for="prop in selectedDb.properties" :key="prop.id" :value="prop.id">
            {{ prop.name }}
          </option>
        </select>
        <span
          class="inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border border-gray-300 dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600"
        >
          :
        </span>
        <select
          class="rounded-none bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        >
          <option value="value">Value</option>
          <option value="count">Count</option>
          <option value="average">Average</option>
          <option value="sum">Sum</option>
        </select>
        <button
          type="button"
          class="py-2 px-2 text-sm font-medium text-gray-900 bg-white rounded-r-md border border-l-0 border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
        >
          <i class="fi fi-br-trash"></i>
        </button>
      </div>
    </div>
    <!-- Button continue -->
    <!-- <button
      v-if="database"
      type="button"
      class="absolute bottom-10 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Continue
      <svg
        aria-hidden="true"
        class="ml-2 -mr-1 w-5 h-5"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
          clip-rule="evenodd"
        ></path>
      </svg>
    </button> -->
  </main>
</template>

<style lang="scss" scoped>
i.fi {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
}
</style>
