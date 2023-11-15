<template>
  <div class="home">
    <h1>MovieHeeom</h1>
    <div class="search">
      <input type="text" placeholder="어떤 영화로 헤엄치고 싶으세요?" />
      <button>Search</button>
    </div>
    <HomeNavigation />
    <HomeLogin />
    </div>
</template>


<script>
import { ref } from 'vue';
import HomeNavigation from '@/views/Home/HomeNavigation.vue';
import HomeLogin from '@/views/Home/HomeLogin.vue';

export default {
  name: 'HomeView',
  components: {
    HomeNavigation,
    HomeLogin,
  },
  setup() {
    return {
    };
  }
};
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
