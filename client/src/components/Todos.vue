<template>
  <div id="todos">
    <div id="todo-item">
      <div class="item" v-for="todo in todos" v-bind:key="todo.id">
        <TodoItem v-bind:todo="todo" v-on:del-todo="$emit('del-todo', todo.id)"/>
      </div>
    </div>
  </div>
</template>

<script>
import TodoItem from "./TodoItem.vue";

export default {
  name: "Todos",
  components: {
    TodoItem
  },
  props: ["todos"],
};
</script>

<style scoped>
#todos {
  color: #ffffff;
  background-color: cadetblue;
  height: 100vh;
}
#todo-item {
  max-width: 1140px;
  margin: 0 auto;

  /* Flex */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.item {
    width: 50%;
}

</style>