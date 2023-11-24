<template>
    <div class="flex">
        <!-- Poster Image -->
        <div class="relative">
            <img :src="getPosterImg(movieDetail.poster_path)" :alt="`${movieDetail.title}영화 포스터`"
                class="h-[60vh] object-cover object-left mt-[5vh]">
        </div>

        <!-- Backdrop Image and Content Overlay -->
        <div class="relative flex-grow">
            <img :src="getBackdropImg(movieDetail.backdrop_path)" alt="백드롭이미지"
                class="h-[60vh] object-cover object-right mt-[5vh] w-full">
            <div class="overlay"></div>

            <!-- Title and Like Button -->
            <div class="absolute top-[10vh] left-[4%] m-4 z-20">
                <h1 class="text-white text-4xl font-bold shadow-lg font-Gowun inline-block mr-2">{{ movieDetail.title }}
                </h1>
                <button @click="toggleLike"
                    class="text-white text-2xl font-semibold bg-Heum-Secondary hover:bg-Heum-Third transition-colors duration-300 py-1 px-3 rounded-lg shadow">{{
                        likeButtonText }}</button>
            </div>

            <div class="absolute top-[20vh] left-[5%] bottom-10 z-20">
                <div class="mb-4">
                    <button @click="showTrailerModal" class="YTbutton">
                        <img src="@/assets/youtube.png" alt="유튜브 아이콘" />
                    </button>
                </div>
                <p class="text-white mb-2">개봉일: {{ movieDetail.release_date }}</p>
                <p class="text-white mb-2">TMDB 평점: {{ movieDetail.vote_average }}</p>
                <p class="text-white mb-2">장르: {{ genreNames }}</p>
                <p class="text-white mb-2">줄거리 <br>{{ movieDetail.overview }}</p>
            </div>
        </div>
    </div>
    <div class="z-50">
        <TrailerModal v-if="showModal" :trailerUrl="trailerUrl" @close="showModal = false" />
    </div>
    <div class="mt-10 px-5">
        <h3 class="text-2xl font-bold mb-4 text-Heum-Fourth font-Gowun">다음은 어디로 헤엄칠까요?👀</h3>
        <div class="movie-cards grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            <MovieCard v-for="id in movieRecommendations" :key="id" :movie-id="id" class="transform hover:scale-105 transition duration-300 ease-in-out"/>
        </div>
    </div>
    <div class="mt-8 px-6">
        <h3 class="text-2xl font-semibold mb-4">코멘트</h3>
        <div class="comment-box bg-white shadow rounded-lg p-4 mb-6">
            <textarea v-model="newComment" class="w-full p-2 border border-gray-300 rounded-md mb-4" placeholder="코멘트 작성..."></textarea>
            <select v-model="newRating" class="w-full p-2 border border-gray-300 rounded-md mb-4">
                <option disabled value="">평점을 선택해주세요</option>
                <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
            </select>
            <button @click="submitComment" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">제출</button>
        </div>
        <div class="comments">
            <h3 class="text-2xl font-semibold mb-4">코멘트</h3>
            <div v-if="comments && comments.length > 0" class="bg-white shadow rounded-lg p-4">
                <commentCard 
                    :comment="comment" 
                    v-for="comment in comments" 
                    :key="comment.id"
                    @comment-edited="handleCommentEdited"
                    @comment-deleted="fetchComments" />
            </div>
            <div v-else class="text-center py-4">
                <p>첫 코멘트를 남겨보세요!!</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios';
import TrailerModal from '@/views/Movie/TrailerModal.vue';

import commentCard from '@/views/Movie/commentCard.vue'
import MovieCard from '@/components/MovieCard.vue'

const router = useRouter()


const { token, myInfo, nickname } = useCounterStore()
const route = useRoute();
const movieDetail = ref({});
const showModal = ref(false);
const trailerUrl = ref('');
const movie_id = ref(route.params.movie_id);  // Grave of the Fireflies (1988)
const newComment = ref('');
const comments = ref([]);
const newRating = ref('');
const movieRecommendations = ref([]);



const isLiking = ref(false); // 첫상태
const likeButtonText = ref(isLiking.value ? '안좋아요' : '좋아요')
const checkLike = async () => {
    console.log(comments.value.liked_users_nickname)
    console.log(nickname)
    if (comments.value.liked_users_nickname && comments.value.liked_users_nickname.includes(nickname)) {
        alert('좋아요 한 영화에요')
        return true
    } else {
        alert('좋아요 안 한 영화에요')
        return false
    }
}


const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const YT_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
const TMDB_ACCESS_TOKEN = import.meta.env.VITE_TMDB_ACCESS_TOKEN



const fetchMovieDetails = async () => {
    const url = `https://api.themoviedb.org/3/movie/${movie_id.value}?api_key=${TMDB_API_KEY}&language=ko-KR&append_to_response=credits`;
    console.log("Requesting URL:", url);

    try {
        const response = await axios.get(url);
        movieDetail.value = response.data
        await fetchComments()
    } catch (error) {
        console.error(error)
    }
}

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
    return backURL ? `https://www.themoviedb.org/t/p/w220_and_h330_face${backURL}` : ''
}

const getBackdropImg = (backURL) => {
    return backURL ? `https://www.themoviedb.org/t/p/w533_and_h300_bestv2${backURL}` : ''
}

const genreNames = computed(() => {
    return movieDetail.value.genres?.map(genre => genre.name).join(', ') || '';
})

const toggleLike = async () => {
    const url = `http://127.0.0.1:8000/movies/${movie_id.value}/liked/`;
    console.log(token)
    try {
        const response = await axios.post(url, {}, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        console.log(response.data);
        if (response.data.status === 'like added') {
            isLiking.value = true;
            likeButtonText.value = '안좋아요';
        } else if (response.data.status === 'like removed') {
            isLiking.value = false;
            likeButtonText.value = 'Follow';
        }
    } catch (error) {
        console.error(error);
    }

};

// const isLiked = computed(() => {
//     if (!myInfo.value || !myInfo.value.liked_movies) {
//     return false;
//   }
//     // 현재 영화의 ID가 myInfo.liked_movies 배열에 존재하는지 확인
//     const likedMovieIds = myInfo.value.liked_movies.map(movie => movie.movie.id);
//     return likedMovieIds.includes(movie_id.value);
// })


const submitComment = async () => {
    // 코멘트를 서버에 제출하는 로직
    const requestData = {
        content: newComment.value,
        rating: newRating.value,
        movie_id: movie_id.value // The ID of the movie being reviewed
    }
    const url = `http://127.0.0.1:8000/movies/reviews/`;
    try {
        await axios.post(url, requestData, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        alert('코멘트 입력 완!')
        await fetchComments()
        console.log(newComment.value);
        newComment.value = '';
        newRating.value = '';
    } catch (error) {
        console.error(error);
    }
};

const handleCommentEdited = (editedComment) => {
    const index = comments.value.findIndex(c => c.id === editedComment.id);
    if (index !== -1) {
        comments.value[index] = { ...comments.value[index], ...editedComment };
    }
}


const fetchComments = async () => {
    const url = `http://127.0.0.1:8000/movies/reviews/?movie_id=${movie_id.value}`
    // 서버에서 코멘트 불러오는 로직
    try {
        const response = await axios.get(url);
        comments.value = response.data
    } catch (error) {
        console.error(error);
        console.error(error);
    }
    // comments.value = fetchedComments;
};


const startFlow = (movie_id) => {
    const isConfirmed = window.confirm("이 영화로 헤엄쳐볼까요?🏊🏻‍♀️");
    if (!isConfirmed) {
        return
    } else {
        router.push(`/movie/${movie_id}`)
    }
}



const fetchMovieRecommendations = async () => {
    const url = `https://api.themoviedb.org/3/movie/${movie_id.value}/recommendations?language=ko-KR&page=1`;
    const options = {
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${TMDB_ACCESS_TOKEN}`
        }
    };

    try {
        const response = await axios.get(url, options);
        movieRecommendations.value = response.data.results.map(movie => movie.id).slice(0, 5);
    } catch (error) {
        console.error('Error fetching movie recommendations:', error);
    }
};



watch(() => route.params.movie_id, async (newMovieId) => {
    movie_id.value = newMovieId;
    await fetchMovieDetails();
    await fetchComments();
    await fetchMovieRecommendations();
}, { immediate: true });

</script>

<style scoped>
.overlay {
    position: absolute;
    top: 5vh;
    height: 60vh;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.8);
    z-index: 5;
    /* Lower z-index than the title and like button */
}

.YTbutton {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
    align-items: center;
}

.YTbutton img {
    width: 40px;
    height: auto;
}

.YTbutton:hover {
    opacity: 0.8;
}

.movie-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    padding: 0 20px; /* Add horizontal padding */
}

</style>
