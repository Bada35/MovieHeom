<template>
    <div class="login-modal">
        <h2 class="modal-title">로그인</h2>
        <div class="login-form">
            <input type="text" v-model.trim="username" placeholder="아이디" />
            <input type="password" v-model.trim="password" placeholder="비밀번호" />
            <button type="button" @click="logIn">로그인</button>
            <div class="signup-link">
                <span>비밀번호를 잊어버리셨나요?</span>
                <a href="#"><br>계정이 없으신가요? 회원가입</a>
            </div>
        </div>
    </div>
</template>
  

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>
  


<style scoped>

.modal-title {
    color: #333;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 1.5em;
    margin-bottom: 20px;
}
.login-modal {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    width: 300px;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1000;
}

.login-form input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
}

.login-form button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: rgba(30, 165, 255, 0.753);
    color: #fff;
    margin-top: 10px;
    cursor: pointer;
}

.login-form button:hover {
    background-color: dodgerblue;
}

.signup-link {
    text-align: center;
    margin-top: 10px;
}

.signup-link span {
    color: #333;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 0.9em;
}

.signup-link a {
    font-size: 0.9em;
    font-family: 'Nanum Gothic', sans-serif;
    text-decoration: none;
}

.signup-link a:hover {
    text-decoration: underline;
}
</style>
  