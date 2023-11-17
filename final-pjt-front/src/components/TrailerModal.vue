<template>
    <div class="modal-overlay" @click.self="close">
      <div class="modal-content">
        <h3>영화 줄거리</h3>
        <iframe :src="trailerUrl" width="560" height="315" frameborder="0" allowfullscreen></iframe>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    trailerUrl: String
  });
  
  const emit = defineEmits(['close']);
  
  const close = () => {
    emit('close');
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    width: 800px;
  }
  
  iframe {
    width: 100%;
    max-width: 800px;
    height: 450px;
  }
  </style>
  