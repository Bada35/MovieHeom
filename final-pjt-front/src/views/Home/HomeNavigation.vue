<template>
      <div class="navigation">
        <button @click="selectCard('Netflix')">Netflix</button>
        <button @click="selectCard('Watcha')">Watcha</button>
        <button @click="selectCard('BoxOffice')">BoxOffice</button>
      </div>
      <NetflixCard v-if="selectedCard === 'Netflix'" />
      <WatchaCard v-if="selectedCard === 'Watcha'" />
      <BoxOfficeCard v-if="selectedCard === 'BoxOffice'" />
  </template>
  
  
  <script>
  import { ref } from 'vue';
  import NetflixCard from '@/components/HomeCards/NetflixCard.vue';
  import WatchaCard from '@/components/HomeCards/WatchaCard.vue';
  import BoxOfficeCard from '@/components/HomeCards/BoxOfficeCard.vue';

  
  export default {
    name: 'HomeNavigation',
    components: {
      NetflixCard,
      WatchaCard,
      BoxOfficeCard,
    },
    setup() {
      const selectedCard = ref(null);
  
      function selectCard(card) {
        selectedCard.value = card;
      }
  
      return {
        selectedCard,
        selectCard,
      };
    }
  };
  </script>
  
  
  <style scoped>
  
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
  
  </style>
  