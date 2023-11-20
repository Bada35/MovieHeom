from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from .views import FollowUserView, FollowersListView, FollowingListView, UserProfileEditView, UserProfileTotalView, CustomLoginView, GuestbookViewSet

router = DefaultRouter()
router.register(r'guestbook', GuestbookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 팔로우 url
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-user'),
    # 팔로워, 팔로잉 목록 반환 url
    path('users/<str:username>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('users/<str:username>/followings/', FollowingListView.as_view(), name='followings-list'),
    # path('profile/', UserProfileView.as_view(), name='user-profile'),
    # 회원정보 수정 url
    path('profile/edit/', UserProfileEditView.as_view(), name='user-profile-edit'),
    # 회원정보 요청하는 url
    path('users/<str:username>/', UserProfileTotalView.as_view(), name='user-profile-test'),
    # path('profile/img_edit/', UserProfileView.as_view(), name='user-profile-img-edit'),
    # 로그인할 때 토큰 값과 username이 같이 반환되는 로그인 url
    path('auth/login/', CustomLoginView.as_view(), name='custom_login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)