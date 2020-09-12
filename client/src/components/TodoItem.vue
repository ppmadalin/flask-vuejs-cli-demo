<template>
  <div class="todo-item" v-bind:class="{ 'is-completed':todo.completed }">
    <p>
        <input type="checkbox" v-on:change="markComplete">
        {{ todo.title }}
        <button v-on:click="$emit('del-todo', todo.id)" class="del">x</button>    
    </p>
        
  </div>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["todo"],
  methods: {
      markComplete() {
          this.todo.completed = !this.todo.completed;
      }
  }
};
</script>

<style scoped>

.todo-item {
    background: #f4f4f4;
    color: #333;
    padding: 10px;
    border-bottom: 1px #ccc dotted;
    width: 100%;
}

.del {
  background: #ff0000;
  color: #ffffff;
  border: none;
  padding: 5px 9px;
  border-radius: 50px;
  cursor: pointer;
  float: right;
}

.is-completed {
  text-decoration: line-through;
}

</style>