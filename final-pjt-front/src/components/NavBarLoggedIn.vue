<template>
    <div class="top-right-menu">
        <button class="auth-button" @click="logOut">로그아웃</button>
        <router-link :to="{ name: 'profile', params: { nickname } }">
      <img :src="userProfileImg" alt="ProfileImg" class="profile-img"/>
    </router-link>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter.js'
import userProfileImg from '@/assets/userProfileImg.png' 


const { logOut, nickname, myInfo } = useCounterStore()

</script>

<style scoped>
.top-right-menu {
    position: absolute;
    top: 20px;
    right: 20px;
    display: flex;
    align-items: center;
}

.auth-button {
    padding: 5px 10px;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 0.8em;
    background-color: #f0f0f0;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px;
}

.auth-button:hover {
    background-color: #e0e0e0;
    border-color: #ccc;
}
.profile-img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  margin-left: 10px;
}
</style>
