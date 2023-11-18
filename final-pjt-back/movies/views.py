from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters ,status
from .models import Movie, Genre, Review
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
# import operator
# from functools import reduce
# from django.db.models import Q
# Create your views here.


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
        movie_id = self.request.data.get('movie_id')
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(user=self.request.user, movie=movie)
    
    # 특정 영화의 리뷰만 찾고 싶을 때
    # movies/reviews/?movie_id=<movie_id>로 검색 가능
    def get_queryset(self):
        queryset = Review.objects.all()
        movie_id = self.request.query_params.get('movie_id')

        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)
        
        return queryset