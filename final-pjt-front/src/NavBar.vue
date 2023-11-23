<template>
  <header>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link :to="{ name: 'movieDetail', params: { movie_id: 637 } }">Movie</router-link>
      <router-link to="/search">Search</router-link>
      <router-link to="/admin">Admin</router-link>
      <NavBarLoggedIn v-if="isLoggedIn"/>
      <NavBarLoggedOut v-if="!isLoggedIn"/>
    </nav>
  </header>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter.js'
import NavBarLoggedIn from '@/components/NavBarLoggedIn.vue'
import NavBarLoggedOut from '@/components/NavBarLoggedOut.vue'

const store = useCounterStore()
const isLoggedIn = ref(store.isLogin.value)

watch(() => store.isLogin, (newValue) => {
  isLoggedIn.value = !isLoggedIn.value
  console.log('바꼈어용')
})

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
