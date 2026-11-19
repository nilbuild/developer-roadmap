# API Calls

Vue doesn't ship its own HTTP client, so API calls are made with the browser's Fetch API or a library such as Axios. In a component, requests are typically started in the `onMounted` lifecycle hook (or `mounted` in the Options API) or in response to user actions, and the results are stored in reactive state such as a `ref` so the template updates automatically when the data arrives. It's good practice to track loading and error states alongside the data, and to move reusable request logic into composables or a dedicated API module. For caching, background refetching, and request deduplication, libraries such as TanStack Query for Vue can manage server state for you.

Visit the following resources to learn more:

- [@article@How To Make API calls in Vue.JS Applications](https://medium.com/bb-tutorials-and-thoughts/how-to-make-api-calls-in-vue-js-applications-43e017d4dc86)
- [@article@How to Use RapidAPI Client with Vue.js](https://rapidapi.com/guides/fetch-api-with-vue)