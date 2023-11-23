<template>
    <div class="movie-details">
        <img :src="getPosterImg(movieDetail.poster_path)" :alt="`${movieDetail.title}영화 포스터`">
        <img :src="getBackdropImg(movieDetail.backdrop_path)" alt="백드롭이미지">
        <div>
            <h1>{{ movieDetail.title }}</h1>
            <div class="buttons">
                <button class="YTbutton" @click="showTrailerModal">
                    <img src="@/assets/youtube.png" alt="유튜브 아이콘" />
                </button>
                <button class="like-button-liked" @click="toggleLike">{{ likeButtonText }}</button>
            </div>
        </div>
        <p>개봉일: {{ movieDetail.release_date }}</p>
        <p>TMDB 평점: {{ movieDetail.vote_average }}</p>
        <p>장르: {{ genreNames }}</p>
        <p>줄거리 <br>{{ movieDetail.overview }}</p>
        <p>코멘트 </p>
        <div class="comment-box">
            <textarea v-model="newComment" placeholder="코멘트 작성..."></textarea>
            <select v-model="newRating">
                <option disabled value="">평점을 선택해주세요</option>
                <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
            </select>
            <button @click="submitComment">제출</button>
        </div>
        <div class="comments">
            <h3>코멘트</h3>
            <div v-if="comments && comments.length > 0">
                <commentCard :comment="comment" v-for="comment in comments" :key="comment.id"/>
            </div>
            <div v-else>
                <p>첫 코멘트를 남겨보세요!!</p>
            </div>
        </div>
        <p>공식 예고편</p>
        <TrailerModal v-if="showModal" :trailerUrl="trailerUrl" @close="showModal = false" />
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router';
import axios from 'axios';
import TrailerModal from '@/views/Movie/TrailerModal.vue';

import commentCard from '@/views/Movie/commentCard.vue'


const { token, myInfo } = useCounterStore()
const route = useRoute();
const movieDetail = ref({});
const showModal = ref(false);
const trailerUrl = ref('');
const movie_id = ref(route.params.movie_id);  // Grave of the Fireflies (1988)
const newComment = ref('');
const comments = ref([]);
const newRating = ref('');


const isLiking = ref(false); // 첫상태
const likeButtonText = ref(isLiking.value ? '안좋아요' : '좋아요')


const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const YT_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY


const fetchMovieDetails = async () => {
    const url = `https://api.themoviedb.org/3/movie/${movie_id.value}?api_key=${TMDB_API_KEY}&language=ko-KR&append_to_response=credits`;
    console.log("Requesting URL:", url);

    try {
        const response = await axios.get(url);
        movieDetail.value = response.data
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

const fetchComments = async () => {
    const url = `http://127.0.0.1:8000/movies/reviews/?movie_id=${movie_id.value}`
    // 서버에서 코멘트 불러오는 로직
    try {
        const response = await axios.get(url);
        comments.value = response.data;
    } catch (error) {
        console.error(error);
    }
    // comments.value = fetchedComments;
};



// https://api.themoviedb.org/3/movie/12477?api_key=0c29fadf6f60100379e8867c18df1169&language=ko-KR&append_to_response=credits

onMounted(async () => {
    await fetchMovieDetails()
    await fetchComments()
});


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

.buttons {
    display: flex;
    align-items: center;
    /* Align the buttons vertically */
    justify-content: center;
    /* Center the buttons horizontally */
    width: 100%;
    /* Set the width to take full container width */
    gap: 10px;
}

.like-button {
    padding: 5px 10px;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 1em;
    /* Adjust font size to match YT button text height */
    line-height: 1;
    /* Ensures the button height matches the text size */
    background-color: #f0f0f0;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    /* Align the text vertically */
    justify-content: center;
    /* Center the text horizontally */
}

.like-button:hover {
    background-color: #e0e0e0;
    border-color: #ccc;
}

.like-button-liked {
    background-color: #007bff;
    color: white;
}

.comment-box select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: 'Nanum Gothic', sans-serif;
    background-color: white;
}

.comment-box textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: 'Nanum Gothic', sans-serif;
}

.comment-box button {
    padding: 10px 20px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 4px;
    color: #333;
    cursor: pointer;
}

.comments h3 {
    margin-bottom: 15px;
}

.comments p {
    background-color: #f8f8f8;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 10px;
}
</style>
