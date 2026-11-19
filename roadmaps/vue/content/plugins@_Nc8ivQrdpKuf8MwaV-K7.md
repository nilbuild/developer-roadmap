# Plugins

Plugins are self-contained pieces of code that add app-level functionality to Vue. A plugin is either an object with an `install()` method or a function that acts as the install function, and it is registered with `app.use(plugin, options)`. Inside `install`, a plugin can register global components and directives, make resources available to the whole app with `app.provide()`, or add global properties through `app.config.globalProperties`. Libraries such as Vue Router and Pinia are installed as plugins.

Visit the following resources to learn more:

- [@official@Plugins in Vue.js](https://vuejs.org/guide/reusability/plugins.html)
- [@article@How to Write Your Own Vue.js Plugin](https://www.linode.com/docs/guides/how-to-write-vue-js-plugins/)