from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),

]