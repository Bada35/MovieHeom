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
