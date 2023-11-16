<!-- ProfileView.vue -->

<template>
    <div class="profile-container">
        <div class="profile-background">
            <!-- 사용자 배경 이미지 -->
            <img :src="coverImg" alt="User background" />
        </div>
        <div class="profile-content">
            <!-- 프로필 이미지 -->
            <div class="profile-image">
                <img :src="userProfileImg" alt="${username}의 프로필" />
            </div>
            <!-- 사용자 정보 -->
            <div class="user-info">
                <h2>{{ username }}의 바다</h2>
                <p>{{ followingCount }} Following {{ followerCount }} Followers</p>
            </div>
            <!-- 평가한 영화 -->
            <div class="rated-films">
                <h3>Films you've rated</h3>
                <div class="comments-container">
                    <!-- 코멘트 목록 -->
                </div>
                <div class="films-grid">
                    <!-- 영화 목록 -->
                    <div class="film" v-for="film in ratedFilms" :key="film.id">filming</div>
                </div>
            </div>
            <!-- 남긴 코멘트 -->
            <div class="user-comments">
                <h3>Comments I've left</h3>
                <div class="comments-container">
                    <!-- 코멘트 목록 -->
                </div>
            </div>
            <!-- 좋아하는 키워드 -->
            <div class="favourite-keywords">
                <h3>My favourite keywords</h3>
                <div class="comments-container">
                    <div class="keywords-grid">
                    <!-- 키워드 목록 -->
                    <span class="keyword">드라마</span>
                    <span class="keyword">액션</span>
                    <!-- ... -->
                </div>
                </div>
                
            </div>
        </div>
    </div>
</template>
  

<script setup>

import { ref } from 'vue'
import coverImg from '@/assets/cover1.png'
import userProfileImg from '@/assets/userProfileImg.png'

const username = ref('박수빈')
const followingCount = ref(0)
const followerCount = ref(0)

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
    object-fit: cover; /* 전체 이미지가 보이도록 조정 */
    object-position: center; /* 이미지가 중앙에 위치하도록 */
}

.user-info h2 {
    color: #333;
    /* 글자색 */
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.user-info p {
    color: #666;
    /* 글자색 */
    font-size: 1rem;
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
}

.comments-container {
    /* 코멘트 목록 스타일 */
    border: 1px solid #ddd;
    /* 테두리 */
    border-radius: 10px;
    padding: 10px;
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
}</style>
  