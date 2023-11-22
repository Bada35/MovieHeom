# Django와 Vue 연동할 때, 사전작업
```
1. $ cd final-pjt-back을 통해 back 폴더로 이동
2. $ py -m venv venv를 통해 가상환경 생성
3. $ source venv/Scripts/acticate을 통해 가상환경 진입
4. $ pip install -r requirements.txt를 통해 필요한 프레임워크, 라이브러리 설치
5. $ py manage.py makemigrations -> $ py manage.py migrate로 마이그레이션 진행
6. $ py manage.py loaddata movie_data.json을 통해 db에 영화 데이터 저장
7. $ py manage.py runserver로 django 서버 가동
8. 이후 작업 진행
```
## url 목록과 사용 방법
### 기본적으로 axios 요청시 header에 로그인한 유저의 Token 값을 같이 보내야 함
```
오전 10:03 2023-11-22
23.11.22 10시 03분 수정

- 회원가입 - POST 요청
http://127.0.0.1:8000/accounts/signup/
해당 url로 username, password1, password2, email, nickname, birth_date, profile_picture, favorite_quote의 값과
함께 post 요청을 하게 되면 해당 정보의 user가 생성된다.

- 로그인 - POST 요청
http://127.0.0.1:8000/accounts/auth/login/
해당 url로 username, password의 값과 함께 post 요청을 하게 되면
{
    "key": "02b0920bb8487b5b7ddb497ece6e577210815bd6",
    "nickname": "test01_nick",
    "user_id": 1
}
형태로 넘어오는 것을 볼 수 있다.

- 회원 정보 수정 - PUT 요청
http://127.0.0.1:8000/accounts/profile/edit/
해당 url로 nickname, email, favorite_quote, profile_picture의 값을 담아 put 요청을 하게 되면
{
    "nickname": "test01_nick_changed",
    "email": "test04@test.com",
    "favorite_quote": "해치웠나?",
    "profile_picture": "/profile_pictures/response.jpeg"
}
와 같이 현재 로그인한 유저의 nickname과 email, favorite_quote, profile_picture를 변경할 수 있다
# 만약 이전의 정보를 유지한 체 특정 항목만 변경을 원할 시,
값을 입력하지 않은 필드의 값을 전송하지 않으면 이전의 값들이 유지된 체로 특정 필드만 변경이 가능하다.

- 비밀번호 수정 - POST 요청
http://127.0.0.1:8000/accounts/password/change/
해당 url로 변경할 new_password1, new_password2의 값을 담아 post 요청을 하게 되면
{"detail":"New password has been saved."}
와 같이 현재 로그인한 유저의 비밀번호가 변경되게 된다.
# 비밀번호 수정같은 경우, 현재 dj_rest_auth를 통해 회원가입과 로그인을 구현했기에
2 번과 같은 방법으로 비밀번호 수정을 하게 되면 password가 암호화되지 않아 변경한 password를 통해 로그인이 되지 않는다.
따라서 dj_rest_auth를 사용하기 위해 제공되는 password 변경을 사용한다.

- 특정 유저 정보 조회 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:nickname>/
해당 url로 원하는 유저의 nickname과 함께 get 요청을 하게 되면
{
    "id": 1,
    "nickname": "test01_nick",
    "email": "",
    "birth_date": "2023-11-19",
    "reviews": [        
        {
            "user_nickname": "test01_nick",
            "content": "test1234",
            "rating": 7.0,
            "movie_id": 14,
            "user_id": 1,
            "created_at": "2023-11-21T05:21:55.518190Z"
        }
    ],
    "liked_movies": [
        {
            "movie": {
                "id": 13,
                "movie_id": 13,
                "title": "포레스트 검프",
                "released_date": "1994-06-23",
                "vote_avg": 8.476,
                "poster_path": "/xdJxoq0dtkchOkUz5UVKuxn7a2V.jpg",
                "genres": [
                    18,
                    35,
                    10749
                ]
            }
        }
    ],
    "favorite_quote": "해치웠나?",
    "profile_picture": "/profile_pictures/response.jpeg"
}
와 같이 id( user_id ), nickname, email, 작성한 리뷰 목록, 좋아요한 영화 목록, 명대사, 프로필 사진 url을 확인할 수 있다.

- 팔로우하기 - POST 요청
http://127.0.0.1:8000/accounts/follow/<str:nickname>/
해당 url로 원하는 유저의 nickname의 값을 담아 post 요청을 보내면
만약 언팔로우 상태에서 요청을 보내면 
{
    "status": "followed"
}
팔로우 상태에서 요청을 보내면 
{
    "status": "unfollowed"
}
만약 자기 자신을 팔로우 요청하게 된다면
{
    "error": "You cannot follow yourself."
}
형태로 넘어오는 것을 볼 수 있다.

- 팔로워 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:nickname>/followers/
해당 url로 원하는 유저의 nickname과 함께 get 요청을 보내면
만약 팔로워가 없다면 
[]
팔로워가 있다면
[
    {
        "nickname": "test02_nick"
    }
]
형태로 넘어오는 것을 볼 수 있다.

- 팔로잉 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:nickname>/followings/
팔로우와 동일

- 방명록 작성 - POST 요청
http://127.0.0.1:8000/accounts/guestbook/
해당 url로 user ( 현재 로그인되어 있는 유저의 id ), target_user ( 현재 위치하고 있는 프로필의 주인 id ), content 값과 함께
post 요청을 하게 되면
{
    "id": 8,
    "user": 2,
    "target_user": 1,
    "target_user_nickname": "test01_nick",
    "content": "test1",
    "created_at": "2023-11-21T06:29:00.184353Z"
}
형태로 guestbook DB에 방명록이 생성된다.

- 특정 방명록 수정 - PUT 요청
http://127.0.0.1:8000/accounts/guestbook/<int:guestbook_id>/
해당 url로 user ( 해당 방명록 작성자의 id ), target_user ( 현재 위치하고 있는 프로필의 주인 id ), content 값과 함께 post 요청을 하게 되면
{
    "id": 2,
    "user": 1,
    "target_user": 2,
    "target_user_nickname": "test02_nick",
    "content": "test12_update22",
    "created_at": "2023-11-22T10:02:44.038628",
    "updated_at": "2023-11-22T10:05:54.266830"
}
형태로 수정된 값이 넘어오는 것을 볼 수 있다.
# 수정은 방명록의 작성자와 수정자가 같아야지만 수정이 가능하다.

- 특정 방명록 삭제 - DELETE 요청
http://127.0.0.1:8000/accounts/guestbook/<int:guestbook_id>/
해당 url로 원하는 리뷰의 id 값과 함께 delete 요청을 하게 되면
해당 방명록이 삭제되어 더 이상 나타나지 않는 것을 볼 수 있다.
# 삭제는 해당 프로필 주인과 방명록의 작성자만 가능하다.

- 특정 유저의 방명록 목록 조회 - GET 요청
http://127.0.0.1:8000/accounts/guestbook/?nickname=<str:nickname>
해당 url로 원하는 유저의 nickname과 함께 get 요청을 보내면
[
    {
        "id": 6,
        "user": 2,
        "target_user": 1,
        "target_user_nickname": "test01_nick",
        "content": "test123",
        "created_at": "2023-11-21T06:28:56.033407Z"
    },
    {
        "id": 7,
        "user": 2,
        "target_user": 1,
        "target_user_nickname": "test01_nick",
        "content": "test12",
        "created_at": "2023-11-21T06:28:57.848486Z"
    }
]
형태로 넘어오는 것을 볼 수 있다.

- 영화 좋아요 - POST 요청
http://127.0.0.1:8000/movies/<int:movie_id>/liked/
해당 url로 원하는 movie_id와 함께 post 요청을 하게 되면
현재 접속해 있는 ( header에 담긴 토큰 값의 주인 ) 사용자가 영화를 좋아요 하게 된다.
만약 해당 영화를 처음 좋아요 요청을 하게 된다면
{"status":"like added"}
이미 좋아요 요청이 되어 있는데 한 번 더 요청한다면 
{"status":"like removed"}
라는 메세지가 뜨게 된다.

- 특정 유저의 영화 좋아요 목록 조회 - GET 요청
http://127.0.0.1:8000/movies/liked/<str:nickname>/
해당 url로 원하는 유저의 nickname과 함께 get 요청을 하게 되면
해당 유저가 좋아요를 누른 영화 목록을 조회할 수 있다.
[
    {
        "id": 13,
        "movie_id": 13,
        "title": "포레스트 검프",
        "released_date": "1994-06-23",
        "vote_avg": 8.476,
        "poster_path": "/xdJxoq0dtkchOkUz5UVKuxn7a2V.jpg",
        "genres": [
            18,
            35,
            10749
        ]
    },
    {
        "id": 238,
        "movie_id": 238,
        "title": "대부",
        "released_date": "1972-03-14",
        "vote_avg": 8.71,
        "poster_path": "/I1fkNd5CeJGv56mhrTDoOeMc2r.jpg",
        "genres": [
            18,
            80
        ]
    }
]
형태로 넘어오는 것을 볼 수 있다.

- 리뷰 작성 - POST 요청
http://127.0.0.1:8000/movies/reviews/
해당 url로 content(str), rating(float), movie_id의 값들을 post로 요청을 하면
{
    "user_nickname": "test01_nick_changed",
    "content": "test123",
    "rating": 6.5,
    "movie_id": 238,
    "user_id": 1,
    "created_at": "2023-11-21T05:44:37.683240Z"
}
형태로 넘어오는 것을 볼 수 있다.

- 특정 영화 리뷰 수정 - PUT 요청
http://127.0.0.1:8000/movies/reviews/<int:review_id>/
해당 url로 content, rating와 함께 put 요청을 하게 되면
{
    "id": 3,
    "user_nickname": "test01_nick",
    "content": "test_update",
    "rating": 9.0,
    "movie_id": 238,
    "user_id": 1,
    "created_at": "2023-11-22T11:05:22.515910",
    "updated_at": "2023-11-22T11:05:53.799027"
}
형태로 수정된 값이 넘어오는 것을 볼 수 있다.
# 수정은 해당 리뷰 작성자와 요청자가 같아야지만 가능하다.

- 특정 영화 리뷰 삭제 - DELETE 요청
http://127.0.0.1:8000/movies/reviews/<int:review_id>/
해당 url로 원하는 리뷰의 id 값과 함께 delete 요청을 하게 되면
해당 영화 리뷰는 삭제되어 더 이상 나타나지 않는 것을 볼 수 있다.
# 삭제는 리뷰 작성자와 삭제 요청자가 같아야지만 가능하다.

- 리뷰 검색( 리뷰 리스트 확인 ) - GET 요청
# movie_id로 검색
http://127.0.0.1:8000/movies/reviews/?movie_id=<int:movie_id>
해당 url로 원하는 movie_id와 함께 get 요청을 하게 되면
해당 영화에 작성된 리뷰들을 조회할 수 있다.
만약 http://127.0.0.1:8000/movies/reviews/?movie_id=238으로 요청을 하게 되면
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
형태로 넘어오는 것을 볼 수 있다.

# nickname로 검색
http://127.0.0.1:8000/movies/reviews/?nickname=<str:nickname>
해당 url로 원하는 유저의 nickname와 함께 get 요청을 하게 되면
해당 유저가 작성한 리뷰들을 조회할 수 있다.
[
    {
        "user_nickname": "test01_nick",
        "content": "test1234",
        "rating": 7.0,
        "movie_id": 14,
        "user_id": 1,
        "created_at": "2023-11-21T05:21:55.518190Z"
    },
    {
        "user_nickname": "test01_nick_changed",
        "content": "test123",
        "rating": 6.5,
        "movie_id": 238,
        "user_id": 1,
        "created_at": "2023-11-21T05:44:37.683240Z"
    }
]
형태로 넘어오는 것을 볼 수 있다.
# 만약 유저가 nickname을 변경하게 되면 어떻게 되는지 고민하고 있었는데,
변경 전 / 후가 같이 검색되는 것을 보니 알아서 처리해주는 것 같다.