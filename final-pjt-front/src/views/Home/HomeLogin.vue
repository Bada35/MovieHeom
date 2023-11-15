<template>
    <div class="top-right-menu">
        <button class="auth-button" @click="toggleLoginModal">로그인</button>
        <button class="auth-button" @click="toggleSignUpModal">회원가입</button>
    </div>
    <div class="modal-overlay" v-if="showLoginModal" @click="toggleLoginModal">
        <LoginModal @click.stop />
    </div>
    <div class="modal-overlay" v-if="showSignUpModal" @click="toggleSignUpModal">
        <SignUpModal @click.stop />
    </div>
</template>
  
  
<script>
import { ref } from 'vue';
import LoginModal from '@/components/Modal/LoginModal.vue';
import SignUpModal from '@/components/Modal/SignUpModal.vue';

export default {
    name: 'HomeLogin',
    components: {
        LoginModal,
        SignUpModal,
    },
    setup() {
        const showLoginModal = ref(false);
        const showSignUpModal = ref(false);

        function toggleLoginModal() {
            showLoginModal.value = !showLoginModal.value;
        }

        function toggleSignUpModal() {
            showSignUpModal.value = !showSignUpModal.value;
        }

        return {
            showLoginModal,
            toggleLoginModal,
            showSignUpModal,
            toggleSignUpModal,
        };
    }
};
</script>
  
  
<style scoped>
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
  