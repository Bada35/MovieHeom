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
    liked_users_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'user_nickname', 'content', 'rating', 'movie_id', 'user_id', 'created_at', 'updated_at','liked_users_nickname']
        read_only_fields = ['user_nickname']

    def get_liked_users_nickname(self, obj):
        movie_likes = MovieLike.objects.filter(movie=obj.movie)
        return [like.user.nickname for like in movie_likes]

class MovieLikeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieLike
        fields = ['movie',]