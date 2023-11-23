<template>
    <div class="signup-modal">
        <h2 class="modal-title">회원가입</h2>
        <div class="signup-form">
            <form @submit.prevent="signUp">
                <input type="text" v-model.trim="username" placeholder="아이디" />
                <input type="email" v-model.trim="email" placeholder="이메일" />
                <input type="text" v-model.trim="nickname" placeholder="닉네임" />
                <input type="date" v-model.trim="birth_date" placeholder="생년월일" />
                <input type="password" v-model.trim="password1" placeholder="비밀번호" />
                <input type="password" v-model.trim="password2" placeholder="비밀번호 확인" />
                <input type="text" v-model.trim="profile_picture" placeholder="프로필사진" />
                <input type="text" v-model.trim="favorite_quote" placeholder="좋아하는 명대사" />
                <button type="submit">회원가입</button>
            </form>
            <div class="login-link">
                <span>이미 가입하셨나요?</span>
                <a href="#" @click.prevent="toggleSignUpModal">로그인</a>
            </div>
        </div>
    </div>
</template>
  

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref('')
const email = ref('')
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const birth_date = ref('')
const profile_picture = ref('')
const favorite_quote = ref('')

const emit = defineEmits(['signup-successful'])

const showSignUpModal = ref(false)

function toggleSignUpModal() {
    showSignUpModal.value = !showSignUpModal.value
}

const signUp = async function () {
    // Optional Chaining과 삼항 연산자를 사용하여 null값 처리
    let payload = {};

    if (username.value) payload.username = username.value;
    if (email.value) payload.email = email.value;
    if (password1.value) payload.password1 = password1.value;
    if (password2.value) payload.password2 = password2.value;
    if (nickname.value) payload.nickname = nickname.value;
    if (birth_date.value) payload.birth_date = birth_date.value;
    if (profile_picture.value) payload.profile_picture = profile_picture.value;
    if (favorite_quote.value) payload.favorite_quote = favorite_quote.value;

    await store.signUp(payload)
    emit('signup-successful')
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

.signup-form input[type='date']::-webkit-datetime-edit-fields-wrapper {
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 0.9em;
    color: #333;
}
</style>
  