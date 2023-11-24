<template>
  <div class="home font-eczar text-center text-gray-800 relative h-screen"> 
    <video class="absolute right-0 bottom-0 min-w-full min-h-full -z-10" autoplay loop muted>
      <source :src="OceanBackground" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <h1 class="text-6xl mb-4 mt-10 font-PermanentMarker text-Heum-Primary text-opacity-80">MovieHeum</h1>
    <div class="search mt-4 mx-auto w-full max-w-4xl relative">
      <form @submit.prevent="goToSearch" class="relative">
      <input type="text" v-model="searchword" 
             class="font-Gowun py-4 pl-6 pr-20 w-full h-16 text-2xl placeholder-opacity-30 placeholder-Heum-Primary text-Heum-Primary bg-Heum-Fourth bg-opacity-60 rounded-full focus:border-none focus:ring-0" 
             placeholder="어떤 영화로 헤엄치고 싶으세요?" />
      <button type="submit"
            class="absolute right-0 top-0 py-4 px-8 text-xl bg-transparent font-Gowun font-thin text-Heum-Primary rounded-full cursor-pointer hover:bg-Heum-Third h-full">Search</button>
          </form>

          </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
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

