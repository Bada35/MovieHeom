<template>
    <div class="login-modal">
        <h2 class="modal-title">회원정보 수정</h2>
        <div class="signup-form">
            <form @submit.prevent="editProfile">
                <input type="test" v-model.trim="nickname" placeholder="수정할 닉네임" />
                <input type="email" v-model.trim="email" placeholder="수정할 이메일" />
                <input type="text" v-model.trim="favorite_quote" placeholder="수정할 명대사" />
                <input type="test" v-model.trim="profile_picture" placeholder="수정할 이미지" />
                <button type="submit">수정</button>
            </form>
        </div>
    </div>
</template>
  

<script setup>
import { ref, defineEmits } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter.js'

const emit = defineEmits(['update-successful'])

const nickname = ref('')
const email = ref('')
const favorite_quote = ref('')
const profile_picture = ref('')
const { token } = useCounterStore()


const editProfile = async () => {
    const url = 'http://127.0.0.1:8000/accounts/profile/edit/';
    let data = {};

    // Conditionally add fields to the data object
    if (nickname.value) data.nickname = nickname.value;
    if (email.value) data.email = email.value;
    if (favorite_quote.value) data.favorite_quote = favorite_quote.value;
    if (profile_picture.value) data.profile_picture = profile_picture.value;
    console.log(data)

    try {
        const response = await axios.put(url, data, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        alert('회원정보 수정 완료!:', response.data);
        emit('update-successful');
        // Handle success (e.g., show a message)
    } catch (error) {
        console.log('Error updating profile:', error);
        // Handle error (e.g., show an error message)
    }
};
</script>
  


<style scoped>

.modal-title {
    color: #333;
    font-family: 'Gowun Dodum', sans-serif;
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
</style>
  