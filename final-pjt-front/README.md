# final-pjt-front

안녕하세요 프론트 입니다



### 🏔컴포넌트 구조

![image](https://github.com/Bada35/final-pjt/assets/139415935/d7536155-d903-4862-8200-2ea64bf93641)






# 3. Vue 구현

Date: 2023년 11월 23일
작성일시: 2023년 11월 23일 오전 10:01

<aside>
💡 < rest api 수정 필요한것 >
- 11번 에서 닉네임, 프로필 이미지도 넘어오게


- 8,9번에서 프로필 이미지, 인용구문도 넘어오게

- 16-1 가능하다면 해당 id영화를 좋아요 한 유저의 닉네임이나 id가  배열로 넘어오게
  [
    {
        "user_nickname": "test01_nick",
        "content": "test1234",
        "rating": 7.0,
        "movie_id": 238,
        "user_id": 1,
        "created_at": "2023-11-21T05:21:49.459942Z"
        **“liked_user_id” : [1, 42, 3]   <- 이런식?**
    },
    {
        "user_nickname": "test02_nick",
        "content": "test123",
        "rating": 6.5,
        "movie_id": 238,
        "user_id": 2,
        "created_at": "2023-11-21T05:22:11.594460Z"
    }
  ]
  아니면 현재 로그인한 유저가 특정 url에 movie_id와 함께 요청을 보내면 그 영화를 like하고 있는지 아닌지 true/false나 뭐 status:liked 이런식으로 돌아오는 url 하나 더 있었으면 좋겠음.

- 6번도 마찬가지. nickname으로 특정 유저를 조회했을 때 팔로우하고 있는 유저의 닉네임이나 id가 배열로 넘어와주게 하거나, 현재 로그인한 유저가 특정 유저를 팔로우하고 있는지 확인할 수 있는 url이 있었으면 좋겠음.

</aside>

### 1. 회원가입 - POST 요청

<aside>
📌 http://127.0.0.1:8000/accounts/signup/
해당 url로 username, password1, password2, email, nickname, birth_date, profile_picture, favorite_quote의 값과
함께 post 요청을 하게 되면 해당 정보의 user가 생성된다.


</aside>

- 관련 컴포넌트 : NavBar, NavBarLoggedout, SignUpModal
- axios 위치 : counter.js
- 전달 인자 : URL, payload(데이터값)
- 토근 전달 여부 : No
- 반환값 : 없음

```jsx
<!--SingUpModal.vue-->

const signUp = async function () {
    let payload = {};

    if (username.value) payload.username = username.value;
    if (email.value) payload.email = email.value;
    if (password1.value) payload.password1 = password1.value;
    if (password2.value) payload.password2 = password2.value;
    if (nickname.value) payload.nickname = nickname.value;
    if (birth_date.value) payload.birth_date = birth_date.value;
    if (profile_picture.value) payload.profile_picture = profile_picture.value;
    if (favorite_quote.value) payload.favorite_quote = favorite_quote.value;

    await store.signUp(payload)
    emit('signup-successful')
}
```

필수로 넘겨야 하는 값은 username(아이디), 비밀번호1, 비밀번호2, 닉네임
저렇게 처리를 안 하면 null값으로 넘어가는데, 그러면 axios 에러가 난다
없는 값은 아예 안 넘어가도록 해야함
필수값에 * 넣고 안 넣은채로 회원가입 누르면 필수 입력입니다 뜨게 하고싶다

```jsx
<!--counter.js-->

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
```

토큰을 굳이 저장해야하나?
여기서 좀 더 예외처리 해야할게 보임

### 2. 로그인 - POST 요청

<aside>
📌 http://127.0.0.1:8000/accounts/auth/login/
해당 url로 username, password의 값과 함께 post 요청을 하게 되면
{
    "key": "02b0920bb8487b5b7ddb497ece6e577210815bd6",
    "nickname": "test01_nick",
    "user_id": 1
}
형태로 넘어오는 것을 볼 수 있다.


</aside>

- 관련 컴포넌트: NavBar, NavBarLoggedout, LogInModal
- axios 위치 : counter.js
- 전달 인자 : URL, payload(username, password)
- 토근 전달 여부 : No
- 반환값 : {
  "key": "02b0920bb8487b5b7ddb497ece6e577210815bd6",
  "nickname": "test01_nick",
  "user_id": 1
  }

```jsx
<!--LogInModal.vue-->

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}
```

```jsx
<!--counter.js-->

const logIn = async (payload) => {
    try {
      const response = await axios.post(`${API_URL}/accounts/auth/login/`, payload);
      token.value = response.data.key
      nickname.value = response.data.nickname
      user_id.value = response.data.user_id
      myInfo.value = await getUserInfo(nickname.value)

      alert(`${nickname.value}님, 안녕하세요!🌊`)
      isLogin.value = true
    } catch (err) {
      console.error(err);
    }
  }
```

```jsx
pinia스토어인 counter.js에 로그인시 반환되는 token, nickname, id(pk)값을 저장함
= pinia 스토어에 저장된 저 세 값은 로그인된 유저의 값이다
  + getUserInfo을 통해 myInfo에 로그인된 유저의 다른 값도 다 저장한다
= 로그아웃 시 null로 초기화 (❔ref로 초기화시켜야하나?)

----------------------------------------------------

isLogin.value = ref(true)

처리를 통해 NavBar에서

const isLoggedIn = ref(store.isLogin.value)

watch(() => store.isLogin, (newValue) => {
  isLoggedIn.value = !isLoggedIn.value
})

로 isLoggedIn 값을 업데이트하고, 이를 통해 아래와 같이 NavBarLoggedout/In을 토글함

<NavBarLoggedIn v-if="isLoggedIn"/>
<NavBarLoggedOut v-if="!isLoggedIn"/>

이렇게 할 경우 로그인 성공 시 NavBar가 업데이트되면서 자동으로 Login 모달창이 꺼짐
```

- ref로 초기화시켜야하나?

  로그아웃될 때 **`token`**, **`nickname`**, **`myInfo`**, **`user_id`** 값을 **`null`**로 초기화하는 것이 올바른 방법입니다. **`ref(null)`**로 초기화할 필요는 없습니다. Vue 3의 Composition API에서 **`ref()`**는 반응형 참조를 생성하는 데 사용됩니다. 한 번 **`ref()`**를 사용하여 반응형 참조를 만든 후에는, 해당 참조의 **`.value`** 속성을 직접 수정하여 값을 변경할 수 있습니다.

### 3. 로그아웃 - POST 요청

<aside>
📌 [**http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/)**
해당 url로 post 요청을 하게 되면
{"detail":"Successfully logged out."}
형태로 로그아웃이 진행된다.


</aside>

- 관련 컴포넌트: NavBar, NavBarLoggedIn, LogInModal
- axios 위치 : counter.js
- 전달 인자 : URL, payload(username, password)
- 토근 전달 여부 : No
- 반환값 : {"detail" : "Successfully logged out."}

```jsx
<!--NavBarLoggedIn.vue-->

<template>
    <div class="top-right-menu">
        <button class="auth-button" @click="logOut">로그아웃</button>
        <!--생략--->
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter.js'

const { logOut } = useCounterStore()
</script>
```

```jsx
<!--counter.js-->

const logOut = async () => {
    try {
      await axios.post(`${API_URL}/accounts/logout/`);
      token.value = null
      nickname.value = ''
      user_id.value = null
      myInfo.value = null

      alert('잘 가요!🙋🏻‍♀️')
      isLogin.value = false
    } catch (err) {
      console.error(err);
    }
  };
```

```jsx
pinia 스토어에 저장된 로그인된 유저의 값 nickname, key, user_id, myinfo를 초기화시켜준다
NavBar 토글을 위해 isLogin 값 또한 false로 변경함
```

### 4. 회원 정보 수정 - PUT 요청

<aside>
📌 [**http://127.0.0.1:8000/accounts/profile/edit/](http://127.0.0.1:8000/accounts/profile/edit/)**
해당 url로 nickname, email, favorite_quote, profile_picture의 값을 담아 put 요청을 하게 되면
현재 로그인한 유저의 nickname과 email, favorite_quote, profile_picture를 변경할 수 있다
만약 이전의 정보를 유지한 체 특정 항목만 변경을 원할 시, 값을 입력하지 않은 필드의 값을 전송하지 않으면
이전의 값들이 유지된 체로 특정 필드만 변경이 가능하다.


**+ bgm_url - PUT 요청**
해당 url을 통해 bgm_url 값과 함께 put 요청을 하게 되면
현재 로그인한 유저의 bgm_url에 대한 링크가 저장된다.

</aside>

- 관련 컴포넌트: ProfileView, SettingModal
- axios 위치 : SettingModal
- 전달 인자 : URL, payload(nickname, email, favorite_quote, profile_picture, bgm_url 중 변경 원하는것만), token
- 토근 전달 여부 : Yes
- 반환값 : ? (필요없어서 돌아오는지 확인해보지 않음)

```jsx
<!--SettingModal.vue-->

const editProfile = async () => {
    const url = 'http://127.0.0.1:8000/accounts/profile/edit/';
    let data = {};

    if (nickname.value) data.nickname = nickname.value;
    if (email.value) data.email = email.value;
    if (favorite_quote.value) data.favorite_quote = favorite_quote.value;
    if (profile_picture.value) data.profile_picture = profile_picture.value;

    try {
        const response = await axios.put(url, data, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        alert('회원정보 수정 완료!:', response.data);
        emit('update-successful');
    } catch (error) {
        console.log('Error updating profile:', error);
        alert('수정하는 중 오류가 발생했어요😰')
    }
};
```

```jsx
<!--ProfileView.js-->

<div class="modal-overlay" v-if="showSettingModal" @click="toggleSettingModal">
    <SettingModal @click.stop @update-successful="handleUpdateSuccess" />
</div>

const showSettingModal = ref(false);

function toggleSettingModal() {
    showSettingModal.value = !showSettingModal.value;
}

const handleUpdateSuccess = async () => {
    user.value = await store.getUserInfo(nickname.value)
    toggleSettingModal() // 모달 닫기
};
```

모달에서 수정에 성공하면 에밋을 통해 `'update-successful'`을 보냄
`'update-successful'`을 받으면 `handleUpdateSuccess()`가 실행되고,
프로필에 띄우는 유저의 값을 수정된 값으로 다시 받아옴(❔애초에 store의 myInfo로 받아오면 getUserInfo가 필요 없을까그 후 `toggleSettingModal()`로 모달을 닫는다

### 5. 비밀번호 수정  - POST 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/accounts/password/change/](http://127.0.0.1:8000/accounts/password/change/)**
해당 url로 변경할 new_password1, new_password2의 값을 담아 post 요청을 하게 되면
{"detail":"New password has been saved."}
와 같이 현재 로그인한 유저의 비밀번호가 변경되게 된다.


비밀번호 수정같은 경우, 현재 dj_rest_auth를 통해 회원가입과 로그인을 구현했기에
2 번과 같은 방법으로 비밀번호 수정을 하게 되면 password가 암호화되지 않아 변경한 password를 통해 로그인이 되지 않는다.
따라서 dj_rest_auth를 사용하기 위해 제공되는 password 변경을 사용한다.

</aside>

### 6. 특정 유저 정보 조회 - GET 요청

<aside>
📌 [http://127.0.0.1:8000/accounts/users/](http://127.0.0.1:8000/accounts/users/)str:nickname/
해당 url로 원하는 유저의 nickname과 함께 get 요청을 하게 되면
id( user_id ), nickname, email, 작성한 리뷰 목록, 좋아요한 영화 목록, 명대사, 프로필 사진 url을 확인할 수 있다


</aside>

- 관련 컴포넌트: 많음
- axios 위치 : counter.js
- 전달 인자 : URL, payload(조회하고자 하는 유저의 nickname), token
- 토근 전달 여부 : Yes
- 반환값 :

![Untitled](3%20Vue%20%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB%2024a9949faad94460984ee0980281b474/Untitled.png)

```jsx
<!--counter.js-->

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
  }
```

전체 response.data를 반환함으로써 user 개개인 객체로 조회할 수 있도록 함

### 7. 팔로우하기 - POST 요청

<aside>
📌 [**http://127.0.0.1:8000/accounts/follow/](http://127.0.0.1:8000/accounts/follow/)str:nickname/**
해당 url로 원하는 유저의 nickname의 값을 담아 post 요청을 보내면 팔로우 여부가 토글링됨


</aside>

- 관련 컴포넌트: ProfileView

- axios 위치 : ProfileView

- 전달 인자 : URL, payload(nickname, email, favorite_quote, profile_picture, bgm_url 중 변경 원하는것만), token

- 토근 전달 여부 : Yes

- 반환값 :

  - 언팔로우 상태에서 요청을 보내면
    { "status": "followed" }
  - 팔로우 상태에서 요청을 보내면
    { "status": "unfollowed" }

- 내 프로필인지 확인하는 `rendValue`

  ```jsx
  const rendValue = ref(false)
  const isMyProfile = () => {
      console.log(store.nickname)
      console.log(nickname.value)
      if (store.nickname === nickname.value) {
          rendValue.value = true
      } else {
          rendValue.value = false
      }
  }
  ```

  store에 저장된 닉네임과 현재 방문한 profile의 nickname이 같으면 `rendValue`를 true, 다르면 false

  - rendValue = ture (방문한 프로필이 내 프로필)
    - v-if를 통해 팔로우버튼 렌더 X, setting(정보수정)버튼 렌더 O
    - 코멘트 작성창 렌더 X
  - rendValue = false (방문한 프로필이 남 프로필)
    - v-if를 통해 팔로우버튼 렌더 O, setting(정보수정)버튼 렌더 X
    - 코멘트 작성창 렌더 O

```jsx
<!--ProfileView.vue-->

<template>
	  <!--생략--->
	    <div v-if="rendValue">
	        <button class="settings-button" @click="toggleSettingModal">
	            <img :src="gearImg" alt="Settings" />
	        </button>
	    </div>
	    <div v-else>
	        <button class="settings-button" @click="toggleFollow">{{ followButtonText }}</button>
	    </div>
	  <!--생략--->
</template>
  

<script setup>

const isFollowing = ref(false); // 첫상태 => 이걸 처리 못하겠어
const followButtonText = ref(isFollowing.value ? 'Unfollow' : 'Follow')

const rendValue = ref(false)
const isMyProfile = () => {
    console.log(store.nickname)
    console.log(nickname.value)
    if (store.nickname === nickname.value) {
        rendValue.value = true
    } else {
        rendValue.value = false
    }
}

**const toggleFollow = async () => {
    const url = `http://127.0.0.1:8000/accounts/follow/${user.value.nickname}/`
    console.log(url)
    try {
        const response = await axios.post(url, {}, {
            headers: {
                Authorization: `Token ${store.token}`
            }
        });
        console.log(response.data);
        if (response.data.status === 'followed') {
            isFollowing.value = true;
            followButtonText.value = 'Unfollow';
        } else if (response.data.status === 'unfollowed') {
            isFollowing.value = false;
            followButtonText.value = 'Follow';
        }
    } catch (error) {
        console.error(error);
    }
}**

onMounted(async () => {
    user.value = await store.getUserInfo(nickname.value)
    isMyProfile()
})

</script>
```

`followButtonText` 에 isFollowing.value ? 'Unfollow' : 'Follow' 삼항연산자로 처리함

`toggleFollow()` 함수가 처리될 때 isFollowing.value 처리

### 8. 팔로워 리스트 확인 - GET 요청(url 수정된 후 작성)

<aside>
📌


</aside>

### 9. 팔로잉 리스트 확인 - GET 요청(url 수정된 후 작성)

<aside>
📌


</aside>

### 10. 방명록 작성(C) - POST 요청 (닉네임도 돌아오게 수정될것)

<aside>
📌 [**http://127.0.0.1:8000/accounts/guestbook/](http://127.0.0.1:8000/accounts/guestbook/)**
해당 url로 user ( 현재 로그인되어 있는 유저의 id ), target_user ( 현재 위치하고 있는 프로필의 주인 id ), content 값과 함께 post 요청


</aside>

- 관련 컴포넌트: ProfileView

- axios 위치 : ProfileView

- 전달 인자 : URL, payload(현재 로그인되어 있는 유저의 id, 현재 위치하고 있는 프로필의 유저 id, content), token

- 토근 전달 여부 : Yes

- 반환값 : {

  “nickname: (예정)”,
  "id": 8,
  "user": 2,
  "target_user": 1,
  "target_user_nickname": "test01_nick",
  "content": "test1",
  "created_at": "2023-11-21T06:29:00.184353Z"
  }

```jsx
<!--ProfileView.vue-->

<h3>방명록 남기기</h3>
<textarea v-model="guestbookContent" placeholder="방명록에 남길 메시지를 입력하세요."></textarea>
<button @click="submitGuestbook">방명록 작성</button>

const submitGuestbook = async () => {
    try {
        const payload = {
            user: store.user_id, // 현재 로그인된 유저 ID
            target_user: user.value.id, // 프로필 주인 ID
            content: guestbookContent.value
        }

        await axios.post('http://127.0.0.1:8000/accounts/guestbook/', payload, {
            headers: {
                Authorization: `Token ${store.token}`
            }
        });
        guestbookContent.value = '' // 입력 필드 초기화
        fetchGuestBook() // 방명록 다시 가져오기(해야지 재렌더됨)
    } catch (error) {
        console.error(error);
    }
}

```

방명록 프로필 사진을 누르면 그 유저의 프로필로 가게 해야함

but 유저 프로필로 가게 하려면 닉네임도 필요하고, 프로필 사진도 받아와야 하는데 id값만 넘어옴

id값으로 닉네임 알아내는 방법 아예 없음. 그래서 수정 필요함

### 11. 특정 유저의 방명록 목록 조회(R) - GET 요청

<aside>
📌 [**http://127.0.0.1:8000/accounts/guestbook/?nickname=](http://127.0.0.1:8000/accounts/guestbook/?nickname=)str:nickname**
해당 url로 원하는 유저의 nickname과 함께 get 요청을 보내면


</aside>

- 관련 컴포넌트: ProfileView
- axios 위치 : ProfileView
- 전달 인자 : URL
- 토근 전달 여부 : No ⇒ 왜인지 모르겠음
- 반환값 :

```
[
    {
        "id": 1,
        "user": 1,
        "target_user": 2,
        "target_user_nickname": "test02_nick",
        "content": "test",
        "created_at": "2023-11-22T16:23:16.427385",
        "updated_at": "2023-11-22T16:23:16.427385",
        "comments": [
            {
                "id": 1,
                "user": 1,
                "guestbook": 1,
                "user_nickname": "test01_nick",
                "content": "test",
                "created_at": "2023-11-22T16:34:19.906741",
                "updated_at": "2023-11-22T16:34:19.906741"
            }
        ]
    },
    {
        "id": 2,
        "user": 1,
        "target_user": 2,
        "target_user_nickname": "test02_nick",
        "content": "test",
        "created_at": "2023-11-22T16:23:27.412995",
        "updated_at": "2023-11-22T16:23:27.412995",
        "comments": []
    }
]
```

```jsx
<!--ProfileView.vue-->

const fetchGuestBook = async () => {
        const url = `http://127.0.0.1:8000/accounts/guestbook/?nickname=${nickname.value}`
        try {
            const response = await axios.get(url);
            GuestBooks.value = response.data;
        } catch (error) {
            console.error(error);
        }
    }

onMounted(async () => {
    fetchGuestBook()
})
```

onMounted로 미리 fetch해주지 않으면 GuestBooks의 value가 정해지기 전에 조회해서 undefined 나기도
난 템플릿에 <div v-if="GuestBooks && GuestBooks.length > 0"> 걸어나서 괜찮긴 한데,
10번 방명록 create에서 create 성공한 후 업데이트하는데 쓰기도 하고 혹시 몰라서 fetch로 onMounted에 걸어놓음

### 12. 특정 방명록 수정(U) - PUT 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/accounts/guestbook/](http://127.0.0.1:8000/accounts/guestbook/)int:guestbook_id/**
해당 url로 user ( 해당 방명록 작성자의 id ), target_user ( 현재 위치하고 있는 프로필의 주인 id ), content 값과 함께 post 요청을 하게 되면 수정된 값이 넘어오는 것을 볼 수 있다.
수정은 방명록의 작성자와 수정자가 같아야지만 수정이 가능하다.


</aside>

- 관련 컴포넌트: ProfileView
- axios 위치 : ProfileView
- 전달 인자 :
- 토근 전달 여부 :
- 반환값 : {
  "id": 2,
  "user": 1,
  "target_user": 2,
  "target_user_nickname": "test02_nick",
  "content": "test12_update22",
  "created_at": "2023-11-22T10:02:44.038628",
  "updated_at": "2023-11-22T10:05:54.266830"
  }

```jsx
<!--ProfileView.vue-->

```

### 13. 특정 방명록 삭제(D) - DELETE 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/accounts/guestbook/](http://127.0.0.1:8000/accounts/guestbook/)int:guestbook_id/**
해당 url로 원하는 방명록의 id 값과 함께 delete 요청을 하게 되면
해당 방명록이 삭제되어 더 이상 나타나지 않는 것을 볼 수 있다.
삭제는 해당 프로필 주인과 방명록의 작성자만 가능하다.


</aside>

- 관련 컴포넌트: ProfileView
- axios 위치 : ProfileView
- 전달 인자 :
- 토근 전달 여부 :
- 반환값 : ?

```jsx
<!--ProfileView.vue-->

```

### 14. 방명록에 대한 대댓글 작성 - POST 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/accounts/guestbook_comment/](http://127.0.0.1:8000/accounts/guestbook_comment/)**
해당 url로 guestbook( 원하는 방명록의 id ), user( 작성자의 id ), content 값과 함께 post 요청을 하게 되면
수정된 값이 돌아온다


</aside>

- 관련 컴포넌트: ProfileView,
- axios 위치 : ProfileView
- 전달 인자 :
- 토근 전달 여부 :
- 반환값 : {
  "id": 5,
  "user": 1,
  "guestbook": 1,
  "user_nickname": "test01_nick",
  "content": "test123",
  "created_at": "2023-11-22T16:39:04.610250",
  "updated_at": "2023-11-22T16:39:04.610250"
  }

```jsx
<!--ProfileView.vue-->

```

### 15. 리뷰 작성(C) - POST 요청

<aside>
📌 [**http://127.0.0.1:8000/movies/reviews/](http://127.0.0.1:8000/movies/reviews/)**
해당 url로 content(str), rating(float), movie_id의 값들을 post로 요청을 하면 작성된 리뷰값이 넘어오는 것을 볼 수 있다.


</aside>

- 관련 컴포넌트: MovieDetailView
- axios 위치 : MovieDetailView
- 전달 인자 : URL, payload(content(str), rating(float), movie_id), token
- 토근 전달 여부 : Yes
- 반환값 : {
  "user_nickname": "test01_nick_changed",
  "content": "test123",
  "rating": 6.5,
  "movie_id": 238,
  "user_id": 1,
  "created_at": "2023-11-21T05:44:37.683240Z"
  }

```jsx
<!--MovieDetailView.vue-->

const submitComment = async () => {
    const requestData = {
        content: newComment.value,
        rating: newRating.value,
        movie_id: movie_id.value // The ID of the movie being reviewed
    }
    const url = `http://127.0.0.1:8000/movies/reviews/`;
    try {
        await axios.post(url, requestData, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        alert('코멘트 입력 완!')
        await fetchComments()
        console.log(newComment.value);
        newComment.value = '';
        newRating.value = '';
    } catch (error) {
        console.error(error);
    }
};
```

코멘트 작성 성공 후 `fetchComments()` 로 업데이트

### 16-1. movie_id로 리뷰 목록 조회(R) - GET 요청

<aside>
📌 [**http://127.0.0.1:8000/movies/reviews/?movie_id=](http://127.0.0.1:8000/movies/reviews/?movie_id=)int:movie_id**
해당 url로 원하는 movie_id와 함께 get 요청을 하게 되면
해당 영화에 작성된 리뷰들을 조회할 수 있다.


</aside>

- 관련 컴포넌트: MovieDetailView,
- axios 위치 : MovieDetailView
- 전달 인자 : URL, payload(nickname, email, favorite_quote, profile_picture, bgm_url 중 변경 원하는것만), token
- 토근 전달 여부 : Yes
- 반환값 :

```jsx
[
    {
        "user_nickname": "test01_nick",
        "content": "test1234",
        "rating": 7.0,
        "movie_id": 238,
        "user_id": 1,
        "created_at": "2023-11-21T05:21:49.459942Z"
    },
    {
        "user_nickname": "test02_nick",
        "content": "test123",
        "rating": 6.5,
        "movie_id": 238,
        "user_id": 2,
        "created_at": "2023-11-21T05:22:11.594460Z"
    }
]
```

```jsx
<!--MovieDetailView.vue-->

const fetchComments = async () => {
    const url = `http://127.0.0.1:8000/movies/reviews/?movie_id=${movie_id.value}`
    try {
        const response = await axios.get(url);
        comments.value = response.data;
    } catch (error) {
        console.error(error);
    }

}
```

### 16-2. nickname로 리뷰 목록 조회(R) - GET 요청

<aside>
📌 [**http://127.0.0.1:8000/movies/reviews/?nickname=](http://127.0.0.1:8000/movies/reviews/?nickname=)str:nickname**
해당 url로 원하는 유저의 nickname와 함께 get 요청을 하게 되면
해당 유저가 작성한 리뷰들을 조회할 수 있다.


</aside>

쓸 이유가 없음
닉네임으로 목록 조회 할만한 곳이 profile 뿐인데
profile 들어갈때 닉네임으로 받아오는 userinfo에 이미 리뷰목록 들어있음

### 17. 특정 영화 리뷰 수정(U) - PUT 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/movies/reviews/](http://127.0.0.1:8000/movies/reviews/)int:review_id/**
해당 url로 content, rating와 함께 put 요청을 하게 되면 수정된 값이 넘어오는 것을 볼 수 있다.
수정은 해당 리뷰 작성자와 요청자가 같아야지만 가능하다.


</aside>

- 관련 컴포넌트: MovieDetailView
- axios 위치 :
- 전달 인자 :
- 토근 전달 여부 :
- 반환값 : {
  "id": 3,
  "user_nickname": "test01_nick",
  "content": "test_update",
  "rating": 9.0,
  "movie_id": 238,
  "user_id": 1,
  "created_at": "2023-11-22T11:05:22.515910",
  "updated_at": "2023-11-22T11:05:53.799027"
  }

### 18. 특정 영화 리뷰 삭제 - DELETE 요청(미구현)

<aside>
📌 [**http://127.0.0.1:8000/movies/reviews/](http://127.0.0.1:8000/movies/reviews/)int:review_id/**
해당 url로 원하는 리뷰의 id 값과 함께 delete 요청
삭제는 리뷰 작성자와 삭제 요청자가 같아야지만 가능하다.


</aside>

- 관련 컴포넌트: MovieDetailView
- axios 위치 :
- 전달 인자 :
- 토근 전달 여부 :
- 반환값 :

```jsx
<!--MovieDetailView.vue-->
```

### 19. 영화 좋아요 - POST 요청

<aside>
📌 [http://127.0.0.1:8000/movies/](http://127.0.0.1:8000/movies/)int:movie_id/liked/
해당 url로 원하는 movie_id와 함께 post 요청을 하게 되면
현재 접속해 있는 ( header에 담긴 토큰 값의 주인 ) 사용자가 영화를 좋아요 하게 된다.


</aside>

- 관련 컴포넌트: MovieDetailView
- axios 위치 : MovieDetailView
- 전달 인자 : URL, payload(빈값), token
- 토근 전달 여부 :
- 반환값 :
  - 안좋아요 상태에서 요청을 보내면
    {"status":"like added"}
  - 좋아요 상태에서 요청을 보내면
    {"status":"like removed"}

```jsx
<!--MovieDetailView.vue-->

<button class="like-button-liked" @click="toggleLike">{{ likeButtonText }}</button>

const isLiking = ref(false); // 첫상태
const likeButtonText = ref(isLiking.value ? '안좋아요' : '좋아요')

const toggleLike = async () => {
    const url = `http://127.0.0.1:8000/movies/${movie_id.value}/liked/`;
    console.log(token)
    try {
        const response = await axios.post(url, {}, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        console.log(response.data);
        if (response.data.status === 'like added') {
            isLiking.value = true;
            likeButtonText.value = '안좋아요';
        } else if (response.data.status === 'like removed') {
            isLiking.value = false;
            likeButtonText.value = '좋아요';
        }
    } catch (error) {
        console.error(error);
    }

```

아무것도 보낼 필요가 없는데 왜 자꾸 에러가 나나 보니까, post보낼때 보낼값이 없다고 하더라도 `{}`를 넣어야 했음

post는 무조건 저렇게인가? 첫상태 like만 처리하면됨