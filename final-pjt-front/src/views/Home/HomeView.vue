<template>
  <div class="home font-eczar text-center text-gray-800 relative">
    <video class="absolute right-0 bottom-0 min-w-full min-h-full -z-10" autoplay loop muted>
      <source :src="OceanBackground" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <h1 class="text-5xl mb-5">MovieHeum</h1>
    <div class="search mb-5">
      <input type="text" v-model="searchword" 
             class="mr-2 font-gowun py-2 px-3 w-72 border-2 border-gray-300 rounded-md text-lg" 
             placeholder="어떤 영화로 헤엄치고 싶으세요?" />
      <button @click="goToSearch" 
              class="py-2 px-5 font-eczar text-lg bg-purple-300 text-white border-none rounded-md cursor-pointer hover:bg-purple-400">Search</button>
    </div>
    <HomeNavigation />
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import HomeNavigation from '@/views/Home/HomeRank.vue'
import OceanBackground from '@/assets/ocean.mp4'

const router = useRouter()
const searchword = ref('')

const goToSearch = () => {
  if (searchword.value) {
    router.push(`/search/${searchword.value}`);
  } else {
    alert('검색어를 입력해주세요!');
  }
}


</script>

<style scoped></style>

