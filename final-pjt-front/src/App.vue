<template>
  <div>
    <RouterView />
    <foot-bar></foot-bar>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import FootBar from '@/FootBar.vue';

</script>

<style scoped></style>


<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap'); /* font-family: 'Gowun Dodum', sans-serif; */
@import url('https://fonts.googleapis.com/css2?family=Eczar:wght@400;500;800&display=swap'); /* font-family: 'Eczar', serif; */
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap'); /* font-family: 'Nanum Gothic', sans-serif */
</style>
