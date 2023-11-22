import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'

  // state: 반응형 상태(데이터)
  const token = ref(null)
  const nickname = ref('')
  const user_id = ref(null)


  // getters: 계산된 값
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })



  // actions: 메서드
  // 11. 회원가입 - POST 요청
  const signUp = async (payload) => {
    const { username, password1, password2, email, nickname, birth_date, profile_picture, favorite_quote } = payload;

    if (password1 !== password2) {
      alert('비밀번호가 일치하지 않습니다!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, {
        username, password1, password2, email, nickname, birth_date, profile_picture, favorite_quote
      });
      alert('회원가입 성공!');
    } catch (err) {
      console.error('회원가입 오류', err);
    }
  }

  // 12. 로그인 - POST 요청
  const logIn = async (payload) => {
    try {
      const response = await axios.post(`${API_URL}/accounts/auth/login/`, payload);
      token.value = response.data.key
      nickname.value = response.data.nickname
      user_id.value = response.data.user_id
    } catch (err) {
      console.error(err);
    }
  }

  // 13. 로그아웃 - 구현?
  const logOut = async () => {
    try {
      await axios.post(`${API_URL}/accounts/logout/`);
      token.value = null;
    } catch (err) {
      console.error(err);
    }
  };



  return {
    token,
    nickname,
    user_id,
    isLogin,
    signUp,
    logIn,
    logOut
  }
}, { persist: true })