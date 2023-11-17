from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]