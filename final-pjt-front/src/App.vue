<template>
  <div class="flex flex-col min-h-screen">
    <NavBar></NavBar>
    <RouterView class="flex-grow"></RouterView>
    <FootBar></FootBar>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/NavBar.vue';
import FootBar from '@/FootBar.vue';

</script>

<style scoped></style>


<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap'); /* font-family: 'Gowun Dodum', sans-serif; */
@import url('https://fonts.googleapis.com/css2?family=Eczar:wght@400;500;800&display=swap'); /* font-family: 'Eczar', serif; */
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap'); /* font-family: 'Nanum Gothic', sans-serif; */
</style>
