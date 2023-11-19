from django.urls import path
from .views import FollowUserView, FollowersListView, FollowingListView, UserProfileView, UserProfileEditView, UserProfileTestView

urlpatterns = [
    # 팔로우 관련 url
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    path('users/<str:username>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('users/<str:username>/followings/', FollowingListView.as_view(), name='followings-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/', UserProfileEditView.as_view(), name='user-profile-edit'),
    path('users/<str:username>/', UserProfileTestView.as_view(), name='user-profile-test'),
]