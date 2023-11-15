<template>
    <div class="signup-modal" @click.self="closeModal">
        <h2 class="modal-title">회원가입</h2>
        <div class="signup-form">
            <form @submit.prevent="signUp">
                <input type="text" v-model.trim="username" placeholder="이름" />
                <input type="password" v-model.trim="password1" placeholder="비밀번호" />
                <input type="password" v-model.trim="password2" placeholder="비밀번호 확인" />
                <button type="submit">회원가입</button>
            </form>
            <div class="login-link">
                <span>이미 가입하셨나요?</span>
                <a href="#" @click="toggleSignUpModal">로그인</a>
            </div>
        </div>
    </div>
</template>
  

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const emit = defineEmits(['closeModal'])

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const showSignUpModal = ref(false) // 회원가입 -> 로그인

function toggleSignUpModal() {
    showSignUpModal.value = !showSignUpModal.value
}

const signUp = function () {
    if (password1.value !== password2.value) {
        alert('패스워드가 일치하지 않아요!')
        return
    }
    const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value
    }
    store.signUp(payload)
}

function closeModal() {
    emit('close-modal')
}  
</script>
  

<style scoped>
.modal-title {
    color: #333;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 1.5em;
    margin-bottom: 20px;
}

.signup-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 32px;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
    width: 400px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.signup-form input {
    width: 100%;
    padding: 16px;
    margin-bottom: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1em;
    box-sizing: border-box;
}

.signup-form button {
    width: 100%;
    padding: 16px;
    margin-top: 8px;
    background-color: #ff4081;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-size: 1em;
    cursor: pointer;
}

.signup-form button:hover {
    background-color: #e03565;
}

.login-link {
    text-align: center;
    margin-top: 10px;
}

.login-link span {
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 0.8em;
    color: #333;
}

.login-link a {
    font-size: 0.8em;
    color: #ff4081;
    text-decoration: none;
    margin-left: 5px;
}

.login-link a:hover {
    text-decoration: underline;
}
</style>
  