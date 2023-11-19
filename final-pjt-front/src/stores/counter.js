import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  // const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const username = ref('')

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
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

  const getUsername = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log(res);
      username.value = res.data.username; // 'username'은 응답의 실제 필드명에 따라 조정해야 할 수 있음
    })
    .catch((err) => {
      console.log(err);
    });
  };



  const signUp = async (payload) => {
    const { username, email, password1, password2, nickname, birth_date } = payload;

    if (password1 !== password2) {
      alert('비밀번호가 일치하지 않습니다!');
      return;
    }

    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, {
        username, email, password1, password2, nickname, birth_date
      });
      console.log('회원가입 성공', response.data);
      token.value = response.data.key;
    } catch (err) {
      console.error('회원가입 오류', err);
    }
  };

  const logIn = async (payload) => {
    try {
      const response = await axios.post(`${API_URL}/accounts/login/`, payload);
      console.log(response.data);
      token.value = response.data.key;
      // username.value = response.data.username;
      // console.log(response.data)
    } catch (err) {
      console.error(err);
    }
  };

  const logOut = async () => {
    try {
      await axios.post(`${API_URL}/accounts/logout/`);
      token.value = null;
      router.push({ name: 'ArticleView' });
    } catch (err) {
      console.error(err);
    }
  };
  return { API_URL, signUp, logIn, token, isLogin, logOut, username, getUsername }
}, { persist: true })
