<template>
    <div class="login-modal">
        <h2 class="modal-title">팔로워</h2>
        <div v-if="followers && followers.length > 0">
            <p v-for="follower in followers" :key="follower.nickname">
                당신의 팔로워 {{ follower.nickname }}님
                {{ follower.profile_picture }}
            </p>
        </div>
        <div v-else>
            <p>팔로워가 아무도 없네요..😢</p>
        </div>
    </div>
</template>
  

<script setup>
import { ref, watchEffect } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter.js'

const { token } = useCounterStore()

const followers = ref([])

const props = defineProps({
    nickname: String
})

const fetchFollower = async () => {
    if (props.nickname) {
        const url = `http://127.0.0.1:8000/accounts/users/${props.nickname}/followers/`
        // 서버에서 팔로워 불러오는 로직
        try {
            const response = await axios.get(url, {
            headers: {
                Authorization: `Token ${token}`
            }});
            followers.value = response.data;
        } catch (error) {
            console.error(error);
        }
    }
};

// props.nickname이 변경될 때마다 fetchFollower 함수를 실행합니다.
watchEffect(fetchFollower);

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
  