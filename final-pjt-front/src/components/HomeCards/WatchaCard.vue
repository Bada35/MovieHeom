<template>
    <div class="rank-image">
    <img :src="rankimg" alt="랭크이미지">
  </div>
  <div class="movie-cards">
    <MovieCard v-for="id in movieIds" :key="id" :movie-id="id" />
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import watchaRank from '@/views/Home/watcha.json'
import MovieCard from '@/components/MovieCard.vue'
import rankimg from '@/assets/watcha.png'

const movieIds = computed(() => watchaRank.map(movie => movie.id));

</script>

<style scoped>
.movie-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  padding: 0 20px;
}
.content-wrapper {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.rank-image {
    display: inline-block;
    flex-wrap: wrap;
    justify-content: flex-start; /* Align items to the start */
    align-items: flex-start; /* Align items to the top */
    width: 100%;
    padding: 0 20px; /* Add horizontal padding */
    padding-top: 50px;
}
</style>
