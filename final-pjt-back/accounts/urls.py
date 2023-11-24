from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from .views import FollowUserView, FollowersListView, FollowingsListView, UserProfileEditView, UserProfileTotalView, CustomLoginView, GuestbookViewSet, GuestbookCommentViewSet

router = DefaultRouter()
router.register(r'guestbook', GuestbookViewSet, basename='guestbook')
router.register(r'guestbook_comment', GuestbookCommentViewSet, basename='guestbook_comment')

urlpatterns = [
    path('', include(router.urls)),
    # 팔로우 url
    path('follow/<str:nickname>/', FollowUserView.as_view(), name='follow-user'),
    # 팔로워, 팔로잉 목록 반환 url
    path('users/<str:nickname>/followers/', FollowingsListView.as_view(), name='followings-list'),
    path('users/<str:nickname>/followings/', FollowersListView.as_view(), name='followers-list'),
    # path('profile/', UserProfileView.as_view(), name='user-profile'),
    # 회원정보 수정 url
    path('profile/edit/', UserProfileEditView.as_view(), name='user-profile-edit'),
    # 회원정보 요청하는 url
    path('users/<str:nickname>/', UserProfileTotalView.as_view(), name='user-profile-test'),
    # path('profile/img_edit/', UserProfileView.as_view(), name='user-profile-img-edit'),
    # 로그인할 때 토큰 값과 username이 같이 반환되는 로그인 url
    path('auth/login/', CustomLoginView.as_view(), name='custom_login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)