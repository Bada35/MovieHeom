<template>
    <div class="absolute top-5 right-5 flex items-center">
        <button class="auth-button" @click="toggleLoginModal">SignIn</button>
        <button class="auth-button" @click="toggleSignUpModal">SignUp</button>
    </div>
    <div class="modal-overlay" v-if="showLoginModal" @click="toggleLoginModal">
        <LoginModal @click.stop />
    </div>
    <div class="modal-overlay" v-if="showSignUpModal" @click="toggleSignUpModal">
        <SignUpModal @click.stop @signup-successful="toggleSignUpModal" />
    </div>
</template>
  
  
<script setup>
import { ref } from 'vue';
import LoginModal from '@/components/Modal/LoginModal.vue';
import SignUpModal from '@/components/Modal/SignUpModal.vue';

const showLoginModal = ref(false);
const showSignUpModal = ref(false);

function toggleLoginModal() {
    showLoginModal.value = !showLoginModal.value;
}

function toggleSignUpModal() {
    showSignUpModal.value = !showSignUpModal.value;
}
</script>
  
  
<style scoped>
.auth-button {
    @apply py-1 px-2 font-Gowun text-xl text-Heum-Primary bg-transparent cursor-pointer ml-4 hover:text-gray-300;
}

.modal-overlay {
    @apply fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-40;
}
</style>
  