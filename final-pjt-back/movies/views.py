from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
import operator
from functools import reduce
from django.db.models import Q
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