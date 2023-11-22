<template>
    <div class="comment-box">
        <p>
            <router-link :to="{ name: 'profile', params: { nickname: comment.user_nickname } }">
                {{ comment.user_nickname }}
            </router-link> {{ comment.created_at }}<br>남긴 별점{{ comment.rating }} : {{ comment.content }}
        </p>
    </div>
</template>

<script setup>
const props = defineProps({
    comment: Object
})
</script>


<style scoped>
.comment-box select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: 'Nanum Gothic', sans-serif;
    background-color: white;
}

.comment-box textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: 'Nanum Gothic', sans-serif;
}

.comment-box button {
    padding: 10px 20px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 4px;
    color: #333;
    cursor: pointer;
}

.comments h3 {
    margin-bottom: 15px;
}

.comments p {
    background-color: #f8f8f8;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 10px;
}
</style>
