<template>
    <div id="content" class="content">
        <div class="content__inner">
            <h1 class="l-heading ">Welcome back</h1>
            <p>Manage your tasks like a boss. Here are your today tasks</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "Content"
}
</script>

<style scoped>

#content {
    background-color: cadetblue;
    color: #fff;
    height: 100vh;
}

.content__inner {
    max-width: 1140px;
    height: 100%;
    margin: 0 auto;
    padding: 2rem 0;

    /* flex */
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

</style>