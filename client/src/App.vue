<template>
  <div id="app">
    <Navigation />
    <Content />
  </div>
</template>

<script>
import Navigation from "./components/layout/Navigation.vue";
import Content from "./components/layout/Content.vue";

export default {
  name: "App",
  components: {
    Navigation,
    Content
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Roboto", sans-serif;
  line-height: 1.4;
}

a {
  text-decoration: none;
}

ul {
  list-style: none;
}

/* Utils */

.l-heading {
  font-size: 2em;
}

</style>
