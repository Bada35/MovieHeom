from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters ,status
from .models import Movie, Genre, Review, MovieLike
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# import operator
# from functools import reduce
# from django.db.models import Q
# Create your views here.
User = get_user_model()

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    # movie_id로만 검색이 가능하도록
    search_fields = ['movie_id']

    # # 영화 데이터 검색 시, ','와 ' '을 통해 여러 데이터 한 번에 검색
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.query_params.get('search', None)
    #     if search:
    #         search_terms = search.replace(',', ' ').split()
    #         query = reduce(operator.or_, (Q(title__icontains=term) | Q(genres__name__icontains=term) for term in search_terms))
    #         queryset = queryset.filter(query).distinct()
    #     return queryset

# 영화 좋아요 기능
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_liked(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    like_obj, created = MovieLike.objects.get_or_create(user=request.user, movie=movie)

    if created:
        return Response({'status': 'like added'})
    else:
        like_obj.delete()
        return Response({'status': 'like removed'})
    
# 좋아요한 영화 목록
class LikedMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes = MovieLike.objects.filter(user=request.user)
        liked_movies = [like.movie for like in likes]
        serializer = MovieSerializer(liked_movies, many=True)
        return Response(serializer.data)
    
# 특정 유저가 좋아요한 영화 목록
class UserLikedMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, nickname):
        # user = get_object_or_404(User, username=username)
        # 커스텀 사용자 모델을 사용한다면 이 방법이 더 적절하다고 한다,,,
        # User = get_user_model()
        user = get_object_or_404(User, nickname=nickname)
        likes = MovieLike.objects.filter(user=user)
        liked_movies = [like.movie for like in likes]
        serializer = MovieSerializer(liked_movies, many=True)
        return Response(serializer.data)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # 인증된 사용자만 리뷰 작성
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 현재 로그인한 사용자를 리뷰 작성자로
    def perform_create(self, serializer):
        user=self.request.user
        movie_id = self.request.data.get('movie_id')
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=user, movie=movie, user_nickname=user.nickname)
    
    # 특정 영화의 리뷰만 찾고 싶을 때
    # movies/reviews/?movie_id=<movie_id>로 검색 가능
    # movies/reviews/?user_nickname=<nickname>로 검색 가능
    def get_queryset(self):
        queryset = Review.objects.all()
        movie_id = self.request.query_params.get('movie_id')
        nickname = self.request.query_params.get('nickname')

        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)

        if nickname is not None:
            queryset = queryset.filter(user__nickname=nickname)
        
        return queryset