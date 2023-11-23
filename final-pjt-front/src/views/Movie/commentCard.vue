<template>
    <div class="comment-box">
        <div v-if="isEditing">
            <textarea v-model="editedContent"></textarea>
            <select v-model="editedRating">
                <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
            </select>
            <button @click="submitEdit">OK</button>
        </div>
        <div v-else>
            <p>
                <router-link :to="{ name: 'profile', params: { nickname: comment.user_nickname } }">
                    {{ comment.user_nickname }}
                </router-link> {{ comment.created_at }}<br>남긴 별점{{ comment.rating }} : {{ comment.content }}
            </p>
            <button v-if="isAuthor" @click="enableEditing">수정</button>
            <button v-if="isAuthor" @click="deleteComment">삭제</button>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const props = defineProps({
    comment: Object
})

const { nickname, token } = useCounterStore()
const isAuthor = computed(() => nickname === props.comment.user_nickname)
const isEditing = ref(false)
const editedContent = ref(props.comment.content)
const editedRating = ref(props.comment.rating)

const emit = defineEmits(['comment-edited', 'comment-deleted']);



const enableEditing = () => {
    isEditing.value = true;
};


const submitEdit = async () => {
    try {
        const payload = {
            content: editedContent.value,
            rating: editedRating.value
        }

        await axios.put(`http://127.0.0.1:8000/movies/reviews/${props.comment.id}/`, payload, {
            headers: {
                Authorization: `Token ${token}`
            }
        })
        emit('comment-edited', { id: props.comment.id, content: editedContent.value, rating: editedRating.value })
        isEditing.value = false;
    } catch (error) {
        console.error(error)
    }
}


const deleteComment = async () => {
    if (confirm('정말로 삭제하시겠습니까?')) {
        try {
            await axios.delete(`http://127.0.0.1:8000/movies/reviews/${props.comment.id}`, {
            headers: {
                Authorization: `Token ${token}`
            }
        })
            emit('comment-deleted', props.comment.id);
        } catch (error) {
            console.error(error);
        }
    }
};
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
