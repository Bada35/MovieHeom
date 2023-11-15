<template>
    <div class="signup-modal" @click.self="closeModal">
        <h2 class="modal-title">회원가입</h2>
        <div class="signup-form">
            <input type="text" placeholder="이름" />
            <input type="email" placeholder="이메일" />
            <input type="password" placeholder="비밀번호" />
            <button>회원가입</button>
            <div class="login-link">
                <span>이미 가입하셨나요?</span>
                <a href="#">로그인</a>
            </div>
        </div>
    </div>
</template>
  

<script setup>
import { defineEmits } from 'vue'
const emit = defineEmits(['closeModal'])

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
  