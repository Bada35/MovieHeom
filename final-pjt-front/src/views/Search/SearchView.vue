<template>
    <div class="search-view">
        <div class="search-box">
            <input type="text" placeholder="어떤 영화를 찾으시나요?" />
            <button @click="searchMovies">
                <img src="@/assets/MagnifyingGlass.png" alt="검색아이콘" />
            </button>
        </div>
        <div class="movie-cards">
            <MovieCard @click="startFlow(id)" v-for="id in movie_ids" :key="id" :movie-id="id" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'

const router = useRouter()

const route = useRoute();
const TMDB_ACCESS_TOKEN = import.meta.env.VITE_TMDB_ACCESS_TOKEN
const searchword = ref(route.params.searchword)
const movie_ids = ref([])

const searchMovies = async () => {
    const url = `https://api.themoviedb.org/3/search/movie?query=${searchword.value}&include_adult=false&language=ko-KR&page=1`;
    const options = {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${TMDB_ACCESS_TOKEN}`
        }
    };

    try {
        const response = await axios.get(url, options);
        console.log(response.data);
        movie_ids.value = response.data.results.map(movie => movie.id);
    } catch (error) {
        console.error(error);
    }
}

const startFlow = (movie_id) => {
    const isConfirmed = window.confirm("이 영화로 헤엄쳐볼까요?🏊🏻‍♀️");
    if (!isConfirmed) {
        return
    } 
}

onMounted(searchMovies)

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
    justify-content: flex-start; /* Align items to the start */
    align-items: flex-start; /* Align items to the top */
    width: 100%;
    padding: 0 20px; /* Add horizontal padding */
    padding-top: 50px;
}


.search-box button img {
    width: 40px;
    height: auto;
}
</style>
