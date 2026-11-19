# v-else-if

The `v-else-if` directive denotes an "else if" block for `v-if`. It must immediately follow an element with `v-if` or another `v-else-if`, and it can be chained multiple times. Vue evaluates the conditions in order and renders only the first block whose expression is truthy, falling back to a `v-else` block if one is present. Like `v-if`, it can be used on a `<template>` element to conditionally render a group of elements without adding an extra wrapper element to the DOM.

Visit the following resources to learn more:

- [@official@v-else-if Documentation](https://vuejs.org/api/built-in-directives.html#v-else-if)