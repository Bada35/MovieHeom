from rest_framework import serializers
from .models import Movie, Genre, Review, MovieLike

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_nickname', 'content', 'rating', 'movie_id', 'user_id', 'created_at', 'updated_at']
        read_only_fields = ['user_nickname']

class MovieLikeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieLike
        fields = ['movie',]