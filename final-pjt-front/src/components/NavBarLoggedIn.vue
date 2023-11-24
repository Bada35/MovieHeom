<template>
    <div class="absolute top-5 right-5 flex items-center">
        <button class="auth-button" @click="logOut">Logout</button>
      <router-link :to="{ name: 'profile', params: { nickname } }">
        <img :src="userProfileImg" alt="ProfileImg" class="w-10 h-10 rounded-full object-cover ml-2 opacity-75"/>
      </router-link>
    </div>
  </template>

<script setup>
import { useCounterStore } from '@/stores/counter.js'
import userProfileImg from '@/assets/userProfileImg.png' 


const { logOut, nickname, myInfo } = useCounterStore()

</script>

<style scoped>
.auth-button {
    @apply py-1 px-2 font-Gowun font-thin text-xl text-Heum-Secondary bg-transparent cursor-pointer ml-4 hover:text-gray-300 mr-2 text-opacity-90;
}
</style>