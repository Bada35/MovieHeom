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
23.11.21 3시 27분 수정

1. 유저 정보 조회 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:username>/
해당 url로 원하는 username과 함께 get 요청을 하게 되면
{
    "nickname": "test03_changed",
    "email": "test04@test.com",
    "birth_date": "2023-11-19",
    "reviews": [
        {
            "content": "test123",
            "rating": 3.4,
            "movie_id": 238,
            "user_id": 4
        }
    ],
    "liked_movies": [
        {
            "movie": {
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
        }
    ],
    "favorite_quote": "해치웠나?",
    "profile_picture": "/profile_pictures/response.jpeg"
}
와 같이 nickname, email, 작성한 리뷰 목록, 좋아요한 영화 목록, 명대사, 프로필 사진 url을 확인할 수 있다.

2. 회원 정보 수정 - PUT 요청
http://127.0.0.1:8000/accounts/profile/edit/
해당 url로 nickname, email, favorite_quote, profile_picture의 값을 담아 put 요청을 하게 되면
{
    "nickname": "test03_changed",
    "email": "test04@test.com",
    "favorite_quote": "해치웠나?",
    "profile_picture": "/profile_pictures/response.jpeg"
}
와 같이 현재 로그인한 유저의 nickname과 email, favorite_quote, profile_picture를 변경할 수 있다
# 만약 이전의 정보를 유지한 체 특정 항목만 변경을 원할 시,
값을 입력하지 않은 필드의 값을 전송하지 않으면 이전의 값들이 유지된 체로 특정 필드만 변경이 가능하다.

3. 비밀번호 수정 - POST 요청
http://127.0.0.1:8000/accounts/password/change/
해당 url로 변경할 new_password1, new_password2의 값을 담아 post 요청을 하게 되면
{"detail":"New password has been saved."}
와 같이 현재 로그인한 유저의 비밀번호가 변경되게 된다.
# 비밀번호 수정같은 경우, 현재 dj_rest_auth를 통해 회원가입과 로그인을 구현했기에
2 번과 같은 방법으로 비밀번호 수정을 하게 되면 password가 암호화되지 않아 변경한 password를 통해 로그인이 되지 않는다.
따라서 dj_rest_auth를 사용하기 위해 제공되는 password 변경을 사용한다.

4. 팔로우하기 - POST 요청
http://127.0.0.1:8000/accounts/follow/<str:username>/
해당 url로 원하는 상대의 username의 값을 담아 post 요청을 보내면
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
라는 메시지가 뜨게 된다.

5. 팔로워 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:username>/followers/
해당 url로 원하는 username의 팔로워 리스트를 사용할 때 get 요청을 보내면
만약 팔로워가 없다면 
[]
팔로워가 있다면
[
    {
        "nickname": "test02"
    }
]
현재는 이렇게 나타난다.

6. 팔로잉 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:username>/followings/
팔로우와 동일

7. 리뷰 작성 - POST 요청
http://127.0.0.1:8000/movies/reviews/
해당 url로 content(str), rating(float), movie_id의 값들을 post로 요청을 하면
{"content":"test2","rating":7.0,"movie_id":13}
형태로 나타남
db에 저장되어 있는 정보를 확인해보면 review_id, content, rating, created_At, updated_at들이 잘 저장되어 있고
movie_id와 user_id가 잘 연결되어 있는 것을 볼 수 있다.

8. 리뷰 검색 - GET 요청
# movie_id로 검색
http://127.0.0.1:8000/movies/reviews/?movie_id=<movie_id>
해당 url로 원하는 movie_id와 함께 get 요청을 하게 되면
해당 영화에 작성된 리뷰들을 불러올 수 있다.
만약 http://127.0.0.1:8000/movies/reviews/?movie_id=13으로 요청을 하게 되면
[{"content":"test2","rating":7.0,"movie_id":13},{"content":"test2","rating":7.0,"movie_id":13}]
형태로 넘어오는 것을 볼 수 있다.

# user_id로 검색
http://127.0.0.1:8000/movies/reviews/?user_id=<user_id>
해당 url로 원하는 user_id와 함께 get 요청을 하게 되면
해당 유저가 작성한 리뷰들을 불러올 수 있다.
반환 값은 위와 동일

9. 영화 좋아요 - POST 요청
http://127.0.0.1:8000/movies/<int:movie_id>/liked/
해당 url로 원하는 movie_id와 함께 post 요청을 하게 되면
현재 접속해 있는 ( header에 담긴 토큰 값의 주인 ) 사용자가 영화를 좋아요 하게 된다.
만약 해당 영화를 처음 좋아요 요청을 하게 된다면
{"status":"like added"}
이미 좋아요 요청이 되어 있는데 한 번 더 요청한다면 
{"status":"like removed"}
라는 메세지가 뜨게 된다.

10. 회원가입 - POST 요청
http://127.0.0.1:8000/accounts/signup/
해당 url로 username, password1, password2, email, nickname, birth_date, profile_picture, favorite_quote의 값과
함께 post 요청을 하게 되면 해당 정보의 user가 생성된다.

11. 로그인 - POST 요청
http://127.0.0.1:8000/accounts/auth/login/
해당 url로 username, password의 값과 함께 post 요청을 하게 되면
{
    "key": "1f85859018805f2406a40759073c2e9448d70ff8",
    "username": "test03"
}
의 형태로 Token 값과 로그인 하는 유저의 username이 넘어온다.

12. 방명록 작성 - POST 요청
http://127.0.0.1:8000/accounts/guestbook/
해당 url로 author( 작성자의 user_id ), target_user ( 피작성자의 user_id ), content와 함께 post 요청을 하게 되면
{
    "id": 1,
    "content": "test",
    "created_at": "2023-11-20T17:29:17.005080Z",
    "author": 1,
    "target_user": 2
}
의 형태로 guestbook DB에 방명록이 생성된다.
