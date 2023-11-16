import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  // const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // // DRF에 article 조회 요청을 보내는 action
  // const getArticles = function () {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/api/v1/articles/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //     .then((res) =>{
  //       // console.log(res)
  //       articles.value = res.data
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload;
  
    // 비밀번호 일치 확인
    if (password1 !== password2) {
      alert('비밀번호가 일치하지 않습니다!');
      return;
    }
  
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, 
        password1, 
        password2
      }
    })
    .then((res) => {
      console.log('회원가입 성공', res.data);
      token.value = res.data.key; // API가 키를 토큰으로 반환한다고 가정
      // router.push({ name: 'Home' }); // 회원가입 후 홈이나 다른 페이지로 리다이렉트
    })
    .catch((err) => {
      console.error('회원가입 오류', err);
    });
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        // router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  } 
  return { API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true })
