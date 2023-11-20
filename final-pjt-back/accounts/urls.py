from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FollowUserView, FollowersListView, FollowingListView, UserProfileEditView, UserProfileTotalView, CustomLoginView

urlpatterns = [
    # 팔로우 관련 url
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    path('users/<str:username>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('users/<str:username>/followings/', FollowingListView.as_view(), name='followings-list'),
    # path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/', UserProfileEditView.as_view(), name='user-profile-edit'),
    path('users/<str:username>/', UserProfileTotalView.as_view(), name='user-profile-test'),
    # path('profile/img_edit/', UserProfileView.as_view(), name='user-profile-img-edit'),
    path('auth/login/', CustomLoginView.as_view(), name='custom_login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)