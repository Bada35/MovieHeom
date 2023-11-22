<template>
    <div class="profile-container">
        <div class="profile-background">
            <!-- 사용자 배경 이미지 -->
            <img :src="coverImg" alt="User background" />
        </div>
        <div class="profile-content">
            <div v-if="isMyProfile">
                <button class="settings-button" @click="toggleSettingModal">
                    <img :src="gearImg" alt="Settings" />
                </button>
            </div>
            <div v-else>
                <p>팔로우 버튼</p>
            </div>
            <div class="modal-overlay" v-if="showSettingModal" @click="toggleSettingModal">
                <SettingModal @click.stop @update-successful="handleUpdateSuccess" />
            </div>
            <!-- 프로필 이미지 -->
            <div class="profile-image">
                <img :src="userProfileImg" alt="${username}의 프로필" />
            </div>
            <!-- 사용자 정보 -->
            <div class="user-info">

                <h2>{{ user.nickname }}의 바다</h2>
                <button @click="toggleFollowingModal">
                    <p>{{ followingCount }} Following </p>
                </button>
                <button @click="toggleFollowerModal">
                    <p>{{ followerCount }} Followers</p>
                </button>
                <div class="modal-overlay" v-if="showFollowingModal" @click="toggleFollowingModal">
                    <FollowingModal :nickname="user.nickname" @click.stop />
                </div>
                <div class="modal-overlay" v-if="showFollowerModal" @click="toggleFollowerModal">
                    <FollowerModal :nickname="user.nickname" @click.stop />
                </div>
            </div>
            <!-- 평가한 영화 -->
            <div class="rated-films">
                <h3>🎬{{ user.nickname }}님의 바다에 떠다니는 영화들</h3>
                <div class="comments-container">
                    <div v-if="user.liked_movies && user.liked_movies.length > 0" class="films-grid">
                        <!-- 영화 목록 -->
                        <div class="film" v-for="film in user.liked_movies" :key="film.liked_movies">
                            {{ film.movie.title }}
                        </div>

                    </div>
                    <div v-else>
                        <h2> 평가한 영화가 없어요ㅠㅠ</h2>
                    </div>
                </div>

            </div>
            <!-- 남긴 코멘트 -->
            <div class="user-comments">
                <h3>💬{{ user.nickname }}님이 남긴 코멘트</h3>
                <div class="comments-container">
                    <div v-if="user.reviews && user.reviews.length > 0" class="films-grid">
                        <!-- 영화 목록 -->
                        <div class="film" v-for="review in user.reviews" :key="review.movie_id">
                            {{ review.content }} {{ review.rating }}점 <br>작성일자 {{ review.created_at }}
                        </div>

                    </div>
                    <div v-else>
                        <h2> 남긴 코멘트가 없어요😥</h2>
                    </div>
                </div>
            </div>
            <div class="user-comments">
                <h3>🌠{{ user.nickname }}님의 명대사</h3>
                <div class="comments-container">
                    <p>{{ user.favorite_quote ? user.favorite_quote : '명대사를 설정해주세요!' }}</p>
                    <!-- <p v-html="defaultQuote" :style="{ 'font-family': '\'Nanum Gothic\', sans-serif' }"></p> -->
                </div>
            </div>
            <!-- 좋아하는 키워드 -->
            <div class="favourite-keywords">
                <h3>🏷️{{ user.nickname }}님이 좋아하는 키워드</h3>
                <div class="comments-container">
                    <div class="keywords-grid">
                        <!-- 키워드 목록 -->
                        <span class="keyword">드라마</span>
                        <span class="keyword">액션</span>
                        <!-- ... -->
                    </div>
                </div>
            </div>
            <!-- 방명록 -->
            <div class="rated-films">
                <h3>🎬{{ user.nickname }}님의 방명록</h3>
                <div class="comments-container">
                    <div v-if="GuestBooks && GuestBooks.length > 0" class="films-grid">
                        <!-- 영화 목록 -->
                        <div class="film" v-for="GuestBook in GuestBooks" :key="GuestBook.id">
                            {{ GuestBook.user }}
                            {{ GuestBook.content }}
                            {{ GuestBook.created_at }}
                        </div>

                    </div>
                    <div v-else>
                        <h2> 방명록을 남겨주세요🙄</h2>
                    </div>
                </div>
                <div v-if="!isMyProfile" class="guestbook-form">
        <h3>방명록 남기기</h3>
        <textarea v-model="guestbookContent" placeholder="방명록에 남길 메시지를 입력하세요."></textarea>
        <button @click="submitGuestbook">방명록 작성</button>
    </div>

            </div>
        </div>
    </div>
</template>
  

<script setup>

import { useRoute } from 'vue-router'
const route = useRoute();
import axios from 'axios'

import { ref, onMounted } from 'vue'
import coverImg from '@/assets/cover1.png'
import userProfileImg from '@/assets/userProfileImg.png'
import { useCounterStore } from '@/stores/counter.js'

import gearImg from '@/assets/gear.png'
import FollowingModal from '@/views/Profile/FollowingModal.vue'
import FollowerModal from '@/views/Profile/FollowerModal.vue'
import SettingModal from '@/views/Profile/SettingModal.vue'


const store = useCounterStore()
const nickname = ref(route.params.nickname)
const user = ref({})

const GuestBooks = ref([])
const guestbookContent = ref('');

const showFollowingModal = ref(false);
const showFollowerModal = ref(false);
const showSettingModal = ref(false);


function toggleFollowingModal() {
    showFollowingModal.value = !showFollowingModal.value;
}

function toggleFollowerModal() {
    showFollowerModal.value = !showFollowerModal.value;
}

function toggleSettingModal() {
    showSettingModal.value = !showSettingModal.value;
}

const followingCount = ref(0)
const followerCount = ref(0)

const defaultQuote = ref('에블린을 수천 명 봤지만 당신 같은 사람은 없었어.<br>이루지 못한 목표와 버린 꿈이 너무 많아. 최악의 에블린으로 살고 있는 거야.<br>당신이 실패의 길을 택했기에 다른 에블린들이 성공한 거야.<br>당신은 무엇이든 할 수 있어')

const handleUpdateSuccess = async () => {
    user.value = await store.getUserInfo(nickname.value)
    toggleSettingModal(); // This should close the modal
};

const isMyProfile = () => {
    if (store.nickname === nickname.value) {
        return true
    } else {
        return false
    }
}

const fetchGuestBook = async () => {
        const url = `http://127.0.0.1:8000/accounts/guestbook/?nickname=${nickname.value}`
        // 서버에서 팔로워 불러오는 로직
        try {
            const response = await axios.get(url);
            GuestBooks.value = response.data;
        } catch (error) {
            console.error(error);
        }
    }


    const submitGuestbook = async () => {
    try {
        const payload = {
            user: store.currentUserId, // 현재 로그인된 유저의 ID
            target_user: user.value.id, // 프로필 주인의 ID
            content: guestbookContent.value
        };

        await axios.post('http://127.0.0.1:8000/accounts/guestbook/', payload);
        guestbookContent.value = ''; // 입력 필드 초기화
        fetchGuestBook(); // 방명록 다시 가져오기
    } catch (error) {
        console.error(error);
    }
};


onMounted(async () => {
    user.value = await store.getUserInfo(nickname.value)
    defaultQuote.value = user.favorite_quote ? user.favorite_quote : defaultQuote.value
    isMyProfile
    fetchGuestBook()
})

</script>


<style scoped>
.profile-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    max-width: 640px;
    margin: auto;
}

.profile-background img {
    width: 100vw;
    height: 250px;
    object-fit: cover;
    object-position: center;
}

.profile-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background-color: rgb(255, 255, 255);
    width: 120%;
    max-width: 100vw;
    position: relative;
    top: -50px;
    border-radius: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    /* 그림자 효과 */
}

.profile-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid white;
    /* 프로필 이미지 테두리 */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    position: relative;
    top: -75px;
    /* 배경 이미지 위로 겹치도록 */
    z-index: 10;
    margin-bottom: -80px;
}

.profile-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    /* 전체 이미지가 보이도록 조정 */
    object-position: center;
    /* 이미지가 중앙에 위치하도록 */
}

.user-info h2 {
    color: #333;
    font-family: 'Gowun Dodum', sans-serif;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    text-align: center;
}

.user-info p {
    color: #666;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 1rem;
    text-align: center;
}

.rated-films,
.user-comments,
.favourite-keywords {
    width: 100%;
    margin-top: 20px;
}

.films-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /* 2열 그리드 */
    gap: 10px;
}

.film {
    background: #ececec;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    font-family: 'Gowun Dodum', sans-serif;
}

.comments-container {
    /* 코멘트 목록 스타일 */
    border: 1px solid #ddd;
    /* 테두리 */
    border-radius: 10px;
    padding: 10px;
    font-family: 'Nanum Gothic', sans-serif;
    min-height: 100px;
    /* 최소 높이 설정 */
}

.keywords-grid {
    display: flex;
    /* 키워드를 위한 flex 레이아웃 */
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}

.keyword {
    display: inline-block;
    margin: 5px;
    padding: 5px 15px;
    border-radius: 20px;
    background: #d0e0f0;
    color: #333;
    /* 글자색 */
    font-size: 1rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

h3 {
    color: #333;
    font-family: 'Gowun Dodum', sans-serif;
}

h2 {
    color: #333;
    font-family: 'Gowun Dodum', sans-serif;
}

.user-info button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: inline-flex;
    /* Use inline-flex to align items within the button */
    align-items: center;
    /* Align the text vertically */
    justify-content: center;
    /* Center the content horizontally */
    margin-right: 10px;
    /* Add space to the right of the button */
}

.user-info button:last-child {
    margin-right: 0;
    /* Remove the margin from the last button */
}

.user-info button p {
    margin: 0;
    /* Remove default margin */
    padding: 0;
    /* Remove default padding */
    color: #333;
    /* Set text color */
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 1rem;
    /* Set the font size as desired */
}

.settings-button {
    position: absolute;
    /* Position the button absolutely within the .profile-content */
    top: 10px;
    /* Adjust as needed */
    right: 10px;
    /* Adjust as needed */
    background: none;
    border: none;
    cursor: pointer;
    padding: 5px;
    /* Add padding as necessary */
}

.settings-button img {
    width: 48px;
    /* Adjust as needed */
    height: 48px;
    /* Adjust as needed */
}

.guestbook-form {
    margin-top: 20px;
    text-align: center;
}

.guestbook-form textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    resize: vertical; /* 사용자가 크기 조절 가능 */
}

.guestbook-form button {
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

.guestbook-form button:hover {
    background-color: #0056b3;
}
</style>
  