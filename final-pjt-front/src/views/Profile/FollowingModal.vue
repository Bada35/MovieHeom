<template>
    <div class="login-modal">
        <h2 class="modal-title">팔로잉</h2>
        <div v-if="followings && followings.length > 0">
            <p v-for="following in followings" :key="following.nickname">
                {{ following.nickname }}님 팔로잉 중
            </p>
        </div>
        <div v-else>
            <p>아무도 팔로잉하고 있지 않아요!</p>
        </div>
    </div>
</template>
  

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter.js'

const { username } = useCounterStore()
const followings = ref([])

const fetchFollowing = async () => {
    const url = `http://127.0.0.1:8000/accounts/users/${username}/followings/`
    // 서버에서 코멘트 불러오는 로직
    try {
        const response = await axios.get(url);
        followings.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

onMounted(fetchFollowing)

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
  