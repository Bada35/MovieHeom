<template>
    <div class="home">
      <h1>MovieHeeom</h1>
      <div class="search">
        <input type="text" placeholder="Where do you want to Heeom?" />
        <button>Search</button>
      </div>
      <div class="navigation">
        <button>Netflix</button>
        <button>Watcha</button>
        <button>BoxOffice</button>
      </div>
      <NetflixCard/>
    </div>
  </template>
  
  <script>
  import NetflixCard from '@/components/HomeCards/NetflixCard.vue';
  
  export default {
    name: 'HomeView',
    components: {
      NetflixCard
    },
    // 필요한 데이터, 메소드 등 추가
  };
  </script>
  
  <style scoped>
  .home {
    text-align: center;
  }
  
  .search input {
    margin-right: 10px;
  }
  
  .navigation button {
    margin-right: 10px;
  }
  
  </style>
  