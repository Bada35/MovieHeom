사용하는 url들
- 기본적으로 axios 요청시 로그인한 유저의 토큰을 같이 보내야 함


1. 팔로우하기 - POST 요청
http://127.0.0.1:8000/accounts/follow/<str:username>/
원하는 상대의 username을 url에 넣어 post 요청을 보내면
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



2. 팔로워 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:username>/followers/
원하는 username의 팔로워 리스트를 사용할 때 get 요청을 보내면
만약 팔로워가 없다면 
[]
팔로워가 있다면
[{"id":1,"password":"pbkdf2_sha256$600000$qyqo786iyoonetbBLLvTwt$kfqcI+Cfj6g4pfKSTuZTA8Z1YtZlUFCYpLKXClnDc1A=","last_login":"2023-11-19T14:41:20.306637","first_name":"","last_name":"","username":"test01","nickname":"test01","email":"","birth_date":"2023-11-19","date_joined":"2023-11-19","is_active":true,"is_staff":false,"is_superuser":false,"groups":[],"user_permissions":[],"followers":[]}]
현재는 이렇게 나타난다.




3. 팔로잉 리스트 확인 - GET 요청
http://127.0.0.1:8000/accounts/users/<str:username>/followings/
팔로우와 동일




4. 본인 프로필 확인 - GET 요청
http://127.0.0.1:8000/accounts/profile/
로그인 상태에서 해당 url로 get 요청을 보내게 되면
{"nickname":"test01","email":"","password":"pbkdf2_sha256$600000$qyqo786iyoonetbBLLvTwt$kfqcI+Cfj6g4pfKSTuZTA8Z1YtZlUFCYpLKXClnDc1A=","username":"test01","birth_date":"2023-11-19"}
현재는 이렇게 나타남.



5. 회원 정보 수정 ( nickname, email ) - PUT 요청
http://127.0.0.1:8000/accounts/profile/edit/
해당 url로 'nickname'과 'email'을 put으로 요청하면
{"nickname":"change","email":"test@test.com"}
형태로 나타나고 실제 db의 accounts_user에 정상적으로 변경된 것을 볼 수 있다.



6. 리뷰 작성 - POST 요청
http://127.0.0.1:8000/movies/reviews/
해당 url로 content(str), rating(float), movie_id의 값들을 post로 요청을 하면
{"content":"test2","rating":7.0,"movie_id":13}
형태로 나타남
db에 저장되어 있는 정보를 확인해보면 review_id, content, rating, created_At, updated_at들이 잘 저장되어 있고 movie_id와 user_id가 잘 연결되어 있는 것을 볼 수 있다.



7. 리뷰 검색 - GET 요청
http://127.0.0.1:8000/movies/reviews/?movie_id=<movie_id>
해당 url로 원하는 movie_id와 함께 get 요청을 하게 되면
해당 영화에 작성된 리뷰들을 불러올 수 있다.
만약 http://127.0.0.1:8000/movies/reviews/?movie_id=13으로 요청을 하게 되면
[{"content":"test2","rating":7.0,"movie_id":13},{"content":"test2","rating":7.0,"movie_id":13}] 형태로 넘어오는 것을 볼 수 있다.

지금 적다가 생각해보니까 6, 7번은 요청 후 반환되는 데이터에 nickname 필드가 추가되어야 할 것 같음