<template>
  <div class="home">
    <h1>MovieHeeom</h1>
    <div class="search">
      <input type="text" placeholder="어떤 영화로 헤엄치고 싶으세요?" />
      <button>Search</button>
    </div>
    <HomeAuth v-if="!isLoggedIn"/>
    <HomeProfile v-if="isLoggedIn"/>
    <HomeNavigation />
    </div>
</template>


<script setup>
import { ref, watch } from 'vue';
import HomeAuth from '@/views/Home/HomeAuth.vue'
import HomeProfile from '@/views/Home/HomeProfile.vue'
import HomeNavigation from '@/views/Home/HomeNavigation.vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore();
const isLoggedIn = ref(store.isLogin.value);

watch(() => store.isLogin, (newValue) => {
  isLoggedIn.value = !isLoggedIn.value; // 로그인 상태가 변경될 때 isLoggedIn을 업데이트
});
</script>


<style scoped>
.home {
  font-family: 'Eczar', serif;
  text-align: center;
  color: #333;
  position: relative;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.search {
  margin-bottom: 20px;
}

.search input {
  margin-right: 10px;
  font-family: 'Gowun Dodum', sans-serif;
  font-size: 1.1em;
  padding: 10px;
  width: 300px;
  border: 2px solid #ddd;
  border-radius: 5px;
}

.search button {
  padding: 10px 20px;
  font-family: 'Eczar', serif;
  font-size: 1.1em;
  background-color: #9a9ae3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.search button:hover {
  background-color: #ba68ed;
}
</style>
