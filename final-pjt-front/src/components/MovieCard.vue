<template>
    <div class="movie-card" @click="goToMovieDetail">
        <div class="movie-hashtags">
            <span v-for="genre in movieDetail.genres?.slice(0, 3)" :key="genre.id">
                #{{ genre.name }}
            </span>
        </div>
        <div class="movie-poster">
            <img :src="getPosterImg(movieDetail.poster_path)" alt="Poster img" />
        </div>
        <div class="movie-title">
            {{ movieDetail.title }}
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const props = defineProps({
  movieId: Number
})
const movieDetail = ref({})
const router = useRouter()

const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY

const fetchMovieDetails = async (id) => {
    const url = `https://api.themoviedb.org/3/movie/${id}?api_key=${TMDB_API_KEY}&language=ko-KR&append_to_response=credits`;
    console.log("Requesting URL:", url);

    try {
        const response = await axios.get(url);
        movieDetail.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

const getPosterImg = (backURL) => {
    return `https://image.tmdb.org/t/p/w500${backURL}`;
}

const goToMovieDetail = () => {
  router.push(`/movie/${props.movieId}`)
}

onMounted(() => fetchMovieDetails(props.movieId));
</script>
  
<style scoped>
.movie-card {
    max-width: 280px;
    border-radius: 10px;
    background-color: #fff;
    color: #333;
    text-align: center;
    margin: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-basis: calc(20% - 20px);
}

.movie-hashtags {
    margin-top: 10px;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 0.8rem;
    color: #333;
    text-align: left;
    margin-bottom: 5px;
}

.movie-poster img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    border-radius: 10px;
}


.movie-title {
    font-family: 'Gowun Dodum', sans-serif;
    font-weight: bold;
    font-size: 18px;
    margin: 5px 0;
    text-align: left;
}
</style>