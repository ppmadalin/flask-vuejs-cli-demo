<template>
  <div>
    <div class="container">
      <form v-on:submit="addTodo">
        <input type="text" v-model="title" name="title" placeholder="Add Todo..." />
        <input type="submit" value="Add" class="btn" />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddTodo",
  data() {
      return {
          title: ''
      }
  },
  methods: {
      addTodo(e) {
          e.preventDefault()
          const newTodo = {
              title: this.title,
              completed: false
          }

        //   Send up to parent
        this.$emit('add-todo', newTodo);

        this.title = '';
      }
  }
};
</script>

<style scoped>
div {
  background-color: cadetblue;
}

.container {
  max-width: 1140px;
  margin: 0rem auto;
  padding-top: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  display: flex;
  width: 50%;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 1rem;
}

input[type="text"] {
  flex: 10;
  padding: 1rem;
  border: 0;

}

input[type="submit"] {
  flex: 5;
  padding: 1rem;
  border: 0;
}

input[type="submit"]:hover {
    cursor: pointer;
    background-color: #f4f4f4;
}

</style>