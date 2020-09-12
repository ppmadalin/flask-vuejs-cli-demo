<template>
  <div id="app">
    <Navigation />
    <AddTodo v-on:add-todo="addTodo"/>
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo"/>
  </div>
</template>

<script>
import Navigation from "./components/layout/Navigation.vue";
import AddTodo from "./components/AddTodo.vue";
import Todos from "./components/Todos.vue";

export default {
  name: "App",
  components: {
    Navigation,
    AddTodo,
    Todos
  },
  data() {
    return {
      todos: [
        {
          id: 1,
          title: "My first task",
          completed: false
        },
        {
          id: 2,
          title: "My second task",
          completed: true
        }

      ]
    }
  },
  methods: {
    deleteTodo(id) {
      this.todos = this.todos.filter(todo => todo.id !== id)
    },
    addTodo(newTodo){
      this.todos = [...this.todos, newTodo];
    }
  }
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
