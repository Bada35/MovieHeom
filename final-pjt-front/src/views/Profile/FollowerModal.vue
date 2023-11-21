<template>
    <div class="login-modal">
        <h2 class="modal-title">팔로워</h2>
        <div v-if="followers && followers.length > 0">
            <p v-for="follower in followers" :key="follower.nickname">
                당신의 팔로워 {{ follower.nickname }}님
            </p>
        </div>
        <div v-else>
            <p>팔로워가 아무도 없네요..😢</p>
        </div>
    </div>
</template>
  

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter.js'

const { username } = useCounterStore()
const followers = ref([])

const fetchFollower = async () => {
    const url = `http://127.0.0.1:8000/accounts/users/${username}/followers/`
    // 서버에서 코멘트 불러오는 로직
    try {
        const response = await axios.get(url);
        followers.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

onMounted(fetchFollower)

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
</style>
  