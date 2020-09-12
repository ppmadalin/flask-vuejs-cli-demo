<template>
    <nav id="navbar">
        <div class="navbar__inner">
            <h1 class="navbar__inner__logo">ToDo</h1>
            <ul class="navbar__inner__menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    </nav>
</template>

<script>
export default {
    name: "Navigation"
    
}
</script>

<style scoped>

#navbar {
    background-color: #333;
    color: #ffffff;
}

.navbar__inner {
    max-width: 1140px;
    margin: 0 auto;
    padding: 1rem 0;

    /* flex */
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar__inner__menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar__inner__menu li {
    margin-left: 1rem;
}

.navbar__inner__menu li a {
    color: #fff;
}
</style>

