<template>
    <div class="search-view">
        <div class="search-box">
            <input type="text" placeholder="어떤 영화를 찾으시나요?" />
            <button @click="searchMovies">
                <img src="@/assets/MagnifyingGlass.png" alt="검색아이콘" />
            </button>
        </div>
        <div class="movie-cards">
            <MovieCard v-for="id in movie_ids" :key="id" :movie-id="id" />
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import MovieCard from '@/components/MovieCard.vue';

const route = useRoute()
const router = useRouter()
const movie_ids = ref([])

// 검색 결과를 URL 쿼리에 저장
const searchMovies = () => {
  movie_ids.value = [545611, 19913, 313369, 122906]
  router.push({ name: 'search', query: { ids: movie_ids.value.join(',') } })
}

// 마운트 시 URL 쿼리에서 검색 결과를 불러오기
onMounted(() => {
  const ids = route.query.ids;
  if (ids) {
    movie_ids.value = ids.split(',').map(Number);
  }
})

// 라우터에서 쿼리 변경을 감시하여 검색 결과를 업데이트
watch(() => route.query.ids, (newIds) => {
  if (newIds) {
    movie_ids.value = newIds.split(',').map(Number);
  }
})

</script>
  
<style scoped>
.search-view {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.search-box {
    display: flex;
    width: 100%;
    max-width: 600px;
    margin: 20px 0;
    border: 1px solid #ccc;
    border-radius: 20px;
}

.search-box input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 20px 0 0 20px;
    outline: none;
}

.search-box button {
    padding: 10px;
    border: none;
    background: none;
    cursor: pointer;
    border-radius: 0 20px 20px 0;
}

.movie-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    padding: 0 20px; /* Add horizontal padding */
    padding-top: 50px;
}


.search-box button img {
    width: 40px;
    height: auto;
}
</style>
  