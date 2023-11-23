from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, ReviewViewSet, movie_liked, LikedMoviesView, UserLikedMoviesView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('liked/', LikedMoviesView.as_view(), name='liked-movies-list'),
    path('<int:movie_id>/liked/', movie_liked, name='liked-movie'),
    path('liked/<str:nickname>/', UserLikedMoviesView.as_view(), name='user-liked-movies-list'),

]