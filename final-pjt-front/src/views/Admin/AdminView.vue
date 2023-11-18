<template>
    <div class="movie-container">
        <h1 class="title">박찬욱 감독의 2015년 이후 영화</h1>
        <ul class="movie-list">
            <li v-for="movie in movies" :key="movie.movieId" class="movie-item">
                <h3 class="movie-title">{{ movie.title }}</h3>
                <p class="movie-title-eng">{{ movie.titleEng }}</p>
                <p class="movie-year">{{ movie.prodYear }}년도 영화</p>
                <p class="movie-nation">국가 : {{ movie.nation }}</p>
                <p class="movie-plot">줄거리 : {{ movie.plots.plot[0].plotText }}</p>
                <p class="movie-runtime">러닝타임 : {{ movie.runtime }}</p>
                <a :href="movie.kmdbUrl" class="movie-link">KMDB링크</a>
            </li>
        </ul>
    </div>
</template>
  
  
<script setup>
import { ref } from 'vue';
import axios from 'axios';

const movies = ref([]);

const fetchMovies = async () => {
    const KMDB_API_KEY = import.meta.env.VITE_KMDB_API_KEY;
    const url = `https://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&detail=N&director=%EB%B0%95%EC%B0%AC%EC%9A%B1&ServiceKey=${KMDB_API_KEY}`;

    try {
        const response = await axios.get(url);
        movies.value = response.data.Data[0].Result;
    } catch (error) {
        console.error('Axios error:', error);
        console.log(error.response);
    }
};

fetchMovies();
</script>

<style scoped>
.movie-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.title {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
}

.movie-list {
    list-style: none;
    padding: 0;
}

.movie-item {
    background-color: #f8f8f8;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.movie-title {
    color: #2a71d0;
    margin-top: 0;
}

.movie-title-eng {
    font-style: italic;
    color: #666;
}

.movie-year,
.movie-nation,
.movie-plot,
.movie-runtime {
    color: #333;
    margin: 10px 0;
}

.movie-link {
    display: inline-block;
    background-color: #2a71d0;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.movie-link:hover {
    background-color: #1a5090;
}
</style>

  