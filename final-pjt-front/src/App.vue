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
