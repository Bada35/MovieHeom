from django.urls import path
from .views import FollowUserView, FollowersListView, FollowingListView

urlpatterns = [
    # 팔로우 관련 url
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    path('users/<str:username>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('users/<str:username>/followings/', FollowingListView.as_view(), name='followings-list'),
]