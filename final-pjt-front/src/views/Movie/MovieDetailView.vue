<template>
    <div class="movie-details">
        <img :src="getPosterImg(movieDetail.poster_path)" :alt="`${movieDetail.title}영화 포스터`">
        <img :src="getBackdropImg(movieDetail.backdrop_path)" alt="백드롭이미지">
        <h1>{{ movieDetail.title }}</h1>
        <p>개봉일: {{ movieDetail.release_date }}</p>
        <p>TMDB 평점: {{ movieDetail.vote_average }}</p>
        <p>장르: {{ genreNames }}</p>
        <p>줄거리 <br>{{ movieDetail.overview }}</p>
        <p>코멘트 {{  }}</p>
        <p>공식 예고편</p>
        <button @click="showTrailerModal">
            <img src="@/assets/youtube.png" alt="유튜브 아이콘" />
        </button>
        <TrailerModal v-if="showModal" :trailerUrl="trailerUrl" @close="showModal = false" />
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router';
import axios from 'axios';
import TrailerModal from '@/components/TrailerModal.vue';


const store = useCounterStore()
const route = useRoute();
const movieDetail = ref({});
const showModal = ref(false);
const trailerUrl = ref('');
const movie_id = ref(route.params.movie_id);  // Grave of the Fireflies (1988)

const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const YT_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY


const fetchMovieDetails = async () => {
    const url = `https://api.themoviedb.org/3/movie/${movie_id.value}?api_key=${TMDB_API_KEY}&language=ko-KR&append_to_response=credits`;
    console.log("Requesting URL:", url);

    try {
        const response = await axios.get(url);
        movieDetail.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

const showTrailerModal = async () => {
    try {
        const searchResponse = await axios.get(`https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(movieDetail.value.title)} official trailer&type=video&key=${YT_API_KEY}`);
        if (searchResponse.data.items.length > 0) {
            const videoId = searchResponse.data.items[0].id.videoId;
            trailerUrl.value = `https://www.youtube.com/embed/${videoId}`;
            showModal.value = true;
        }
    } catch (error) {
        console.error(error);
    }
};

const getPosterImg = (backURL) => {
    return backURL? `https://www.themoviedb.org/t/p/w220_and_h330_face${backURL}` : ''
}

const getBackdropImg = (backURL) => {
    return backURL? `https://www.themoviedb.org/t/p/w533_and_h300_bestv2${backURL}` : ''
}

const genreNames = computed(() => {
  return movieDetail.value.genres?.map(genre => genre.name).join(', ') || '';
})


store.getReviews(movie_id)

// https://api.themoviedb.org/3/movie/12477?api_key=0c29fadf6f60100379e8867c18df1169&language=ko-KR&append_to_response=credits

onMounted(fetchMovieDetails);


</script>

<style scoped>
.movie-details {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

.movie-details img {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px;
}

.movie-details h1 {
    margin-bottom: 10px;
    color: #333;
    font-family: 'Gowun Dodum', sans-serif;
    font-size: 2em;
}

.movie-details p {
    font-family: 'Nanum Gothic', sans-serif;
    margin-bottom: 10px;
    color: #666;
}

.movie-details button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
}

.movie-details button img {
    width: 40px;
    height: auto;
}

.movie-details button:hover {
    opacity: 0.8;
}
</style>
