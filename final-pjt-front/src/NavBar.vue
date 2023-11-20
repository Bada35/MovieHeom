<template>
  <header>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link :to="{ name: 'movieDetail', params: { movie_id: 637 } }">Movie</router-link>
      <router-link to="/search">Search</router-link>
      <router-link to="/admin">Admin</router-link>
    </nav>
  </header>
</template>

<script setup>
</script>

<style scoped>
nav a {
  font-family: 'Gowun Dodum', sans-serif;
  margin-right: 15px;
  text-decoration: none;
  font-size: 1.2em;
  color: black;
  transition: color 0.3s ease;
}

nav a:hover {
  color: #3498db;
}
</style>
