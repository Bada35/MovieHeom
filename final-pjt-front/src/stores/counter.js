import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'

  // state: 반응형 상태(데이터)
  const token = ref(null)
  const nickname = ref('')
  const user_id = ref(null)
  const isLogin = ref(false)
  const myInfo = ref(null)


  // getters: 계산된 값




  // actions: 메서드
  // 1. 특정 유저 정보 조회 - GET 요청
  const getUserInfo = async (nickname) => {
    try {
      const response = await axios.get(`${API_URL}/accounts/users/${nickname}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      return response.data;
    } catch (err) {
      console.error('유저 정보 조회 오류', err);
      return null;
    }
  };

  // 11. 회원가입 - POST 요청
  const signUp = async (payload) => {
    const { username, email, password1, password2, nickname, birth_date, profile_picture, favorite_quote } = payload;

    if (password1 !== password2) {
      alert('비밀번호가 일치하지 않습니다!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, {
        username, email, password1, password2, nickname, birth_date, profile_picture, favorite_quote
      });
      alert('회원가입 성공!');
      token.value = response.data.key;
      return true
    } catch (err) {
      console.error('회원가입 오류', err);
      return false
    }
  }

  // 12. 로그인 - POST 요청
  const logIn = async (payload) => {
    try {
      const response = await axios.post(`${API_URL}/accounts/auth/login/`, payload);
      token.value = response.data.key
      nickname.value = response.data.nickname
      user_id.value = response.data.user_id
      myInfo.value = await getUserInfo(nickname.value)
      alert(`${nickname.value}님, 안녕하세요!🌊`)
      isLogin.value = ref(true)
    } catch (err) {
      console.error(err);
    }
  }

  // 13. 로그아웃 - 구현?
  const logOut = async () => {
    try {
      await axios.post(`${API_URL}/accounts/logout/`);
      alert('잘 가요!🙋🏻‍♀️')
      token.value = null
      isLogin.value = ref(false)
      myInfo.value = null
    } catch (err) {
      console.error(err);
    }
  };



  return {
    token,
    nickname,
    user_id,
    isLogin,
    myInfo,
    getUserInfo,
    signUp,
    logIn,
    logOut
  }
}, { persist: true })