<template>
    <!-- <div class="parent-container">
        <div class="profile-container_left">
            <div class="user-img">
                <img :src="userProfileImg" alt="유저이미지">
            </div>
            <div class="user-info">
                <div class="bio-container">
                    <p>{{ user.bio }}</p>
                </div>
                <button class="edit-button">Edit</button>
            </div>
            <div class="user-contact">
                <div class="name-birthdate">
                    <p class="name">{{ user.name }}</p>
                    <p class="birthdate">{{ user.birthdate }}</p>
                </div>
                <p class="email">{{ user.email }}</p>
                <p>팔로잉{{ follower? follower : 0 }} | 팔로워{{ following? following : 0 }}</p>
            </div>
        </div>
        <div class="profile-container_right">
            <div class="user-nickname">
                <h2>{{ user.nickname }}의 섬</h2>
            </div>
            <div class="user-stats">
                <span>{{ user.reviews }} reviews</span>
                <span>{{ user.comments }} comments</span>
                <span>{{ user.likes }} likes</span>
            </div>
            <div class="user-actions">
                <input type="text" placeholder="Leave a guestbook~">
                <button>Enter</button>
            </div>

        </div>
    </div> -->
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import userProfileImg from '@/assets/userProfileImg.png'
import { useCounterStore } from '@/stores/counter'


// const user = ref({
//     nickname: 'YoungJun',
//     bio: '에블린을 수천 명 봤지만 당신 같은 사람은 없었어. 이루지 못한 목표와 버린 꿈이 너무 많아. 최악의 에블린으로 살고 있는 거야. 당신이 실패의 길을 택했기에 다른 에블린들이 성공한 거야. 당신은 무엇이든 할 수 있어',
//     reviews: 189,
//     comments: 23,
//     likes: 2,
//     name: '서지수',
//     birthdate: '1997.03.05',
//     email: 'ssafybada@gmail.com'
// })
const user = ref({
    username: '',
    nickname: '',
    email: '',
    birth_date: '',
    reviews: [],
    liked_movies: [],
    favorite_quotes: '',
    profile_picture: ''
})
const store = useCounterStore()
const follower = store.getFollowers(user.value.username)
const following = store.getFollowings(user.value.username)


const printUsername = () => {
    console.log(store.username)
}

onMounted(() => {
    // store.getUserInfo(store.username)
    printUsername()
    })
</script>
  
<style scoped>
.parent-container {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 20px;
    margin: 40px;
    padding: 20px;
}

.profile-container_left {
    display: grid;
    grid-template-areas:
        'user-img'
        'user-info'
        'user-contact';
    grid-template-columns: 1fr;
    grid-template-rows: 300px auto 1fr;
    width: 20vw;
    height: 80vh;
    gap: 20px;
    margin: 40px auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: rgb(238, 231, 231);
    align-items: start;
}

.profile-container_right {
    display: grid;
    grid-template-areas:
        'user-nickname'
        'user-stats'
        'user-actions';
    grid-template-columns: 1fr;
    grid-template-rows: 300px auto 1fr;
    width: 70vw;
    height: 80vh;
    gap: 20px;
    margin: 40px auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: rgb(238, 231, 231);
}

.user-img {
    width: 300px;
    height: 300px;
    overflow: hidden;
    border: 5px solid white;
    /* 프로필 이미지 테두리 */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    position: relative;
    /* 배경 이미지 위로 겹치도록 */
    z-index: 10;
    margin-top: 15px;
    margin-bottom: -80px;
    justify-self: center;
}

.user-info {
    grid-area: user-info;
    padding: 20px;
    border-bottom: 2px solid #d4d4d4;
    border-radius: 10px;
    background-color: #ffffff71;
    color: #555555;
    font-family: 'Nanum Gothic', sans-serif;
    height: 220px;
    line-height: 1.6;
    display: flex;
    /* Flex 컨테이너로 설정 */
    flex-direction: column;
    /* 요소들을 세로로 정렬 */
    justify-content: space-between;
    /* 내용을 상하로 분산 */
    position: relative;
    /* 자식 요소에 대한 위치 지정을 위함 */
}

.bio-container {
    text-align: center;
}

.user-stats {
    grid-area: user-stats;
    /* 추가 통계 섹션 스타일링 필요 */
}

.edit-button {
    align-self: flex-end;
    /* 버튼을 flex 컨테이너의 끝으로 정렬 */
    padding: 10px;
    margin-top: auto;
    /* 나머지 내용과 분리 */
    border: none;
    background-color: #3e444b;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.2);
    border-radius: 4px;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

.edit-button:hover {
    background-color: #0056b3;
}

.user-contact {
    grid-area: user-contact;
    padding: 20px;
    border-top: 1px solid transparent;
    color: #555555;
    font-family: 'Gowun Dodum', sans-serif;
    text-align: left;
    margin-top: -40px;
}

.user-nickname{
    grid-area: user-nickname;
    font-family: 'Gowun Dodum', sans-serif;
    text-align: left;
    font-size: 50px;
    color: #333;
    margin-bottom: 30px;
}
.name-birthdate {
    display: flex;
    justify-content: start;
    align-items: baseline;
}

.name-birthdate .name {
    font-size: 30px;
    font-weight: bold;
    margin-right: 20px;
}

.name-birthdate .birthdate {
    font-size: 20px;
}


.user-actions {
    grid-area: user-actions;
}

button {
    padding: 10px;
    border: none;
    background-color: #3e444b;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.2);
    border-radius: 4px;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #0056b3;
}

input[type="text"] {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.email {
    margin-top: -20px;
}</style>
  