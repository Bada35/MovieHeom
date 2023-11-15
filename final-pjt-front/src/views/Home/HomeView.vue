<template>
  <div class="home">
    <h1>MovieHeeom</h1>
    <div class="search">
      <input type="text" placeholder="어떤 영화로 헤엄치고 싶으세요?" />
      <button>Search</button>
    </div>
    <div class="navigation">
      <button @click="selectCard('Netflix')">Netflix</button>
    <button @click="selectCard('Watcha')">Watcha</button>
    <button @click="selectCard('BoxOffice')">BoxOffice</button>
    </div>
    <NetflixCard v-if="selectedCard === 'Netflix'"/>
    <WatchaCard v-if="selectedCard === 'Watcha'"/>
    <BoxOfficeCard v-if="selectedCard === 'BoxOffice'"/>
    <div class="top-right-menu">
      <button class="auth-button" @click="toggleModal">로그인</button>
      <button class="auth-button" @click="signUp">회원가입</button>
    </div>
    <div class="modal-overlay" v-if="showModal" @click="toggleModal"></div>
    <LoginModal v-if="showModal" />
  </div>
</template>


<script>
import { ref } from 'vue';
import NetflixCard from '@/components/HomeCards/NetflixCard.vue';
import WatchaCard from '@/components/HomeCards/WatchaCard.vue';
import BoxOfficeCard from '@/components/HomeCards/BoxOfficeCard.vue';
import LoginModal from '@/components/Modal/LoginModal.vue';

export default {
  name: 'HomeView',
  components: {
    NetflixCard,
    WatchaCard,
    BoxOfficeCard,
    LoginModal,
  },
  setup() {
    const selectedCard = ref(null);
    const showModal = ref(false);

    function selectCard(card) {
      selectedCard.value = card;
    }

    function toggleModal() {
      showModal.value = !showModal.value;
    }

    return {
      selectedCard,
      selectCard,
      showModal,
      toggleModal,
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

.navigation button {
  margin-right: 10px;
  padding: 8px 16px;
  font-family: 'Eczar', serif;
  font-size: 1.1em;
  background-color: #f0f0f0;
  border: 2px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
}

.navigation button:hover {
  background-color: #e0e0e0;
}

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
}
</style>
