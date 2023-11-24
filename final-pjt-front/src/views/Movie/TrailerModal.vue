<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal-content" @click.stop>
      <button class="close-button" @click="close">×</button>
      <h3>🎥공식 트레일러</h3>
      <iframe :src="trailerUrl" frameborder="0" allowfullscreen></iframe>
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
  opacity: 0;
  animation: fadeIn 0.3s forwards;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

.modal-content {
  position: relative;
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 80%;
  max-width: 800px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transform: scale(0.9);
  animation: scaleIn 0.3s forwards;
}

.modal-content>h3 {
  font-family: 'Gowun Dodum', sans-serif;
}

@keyframes scaleIn {
  to {
    transform: scale(1);
  }
}

.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  border: none;
  background: transparent;
  font-size: 24px;
  cursor: pointer;
}

iframe {
  width: 100%;
  height: 450px;
  border: none;
  border-radius: 4px;
}
</style>
  