from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User, Guestbook, GuestbookComment
from .serializers import UserSerializer, UserProfileEditSerializer, UserProfileTotalSerializer, GuestbookSerializer, GuestbookCommentSerializer
from dj_rest_auth.views import LoginView
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

# 팔로우 기능
class FollowUserView(APIView):
    def post(self, request, nickname):
        target_user = get_object_or_404(User, nickname=nickname)
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.followers.filter(nickname=nickname).exists():
            request.user.followers.remove(target_user)
            return Response({"status": "unfollowed"})
        else:
            request.user.followers.add(target_user)
            return Response({"status": "followed"})

# 팔로워 목록        
class FollowingsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, nickname):
        user = get_object_or_404(User, nickname=nickname)
        followers = user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)

# 팔로잉 목록
class FollowersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, nickname):
        user = get_object_or_404(User, nickname=nickname)
        followings = user.followings.all()
        serializer = UserSerializer(followings, many=True)
        return Response(serializer.data)

# 프로필    
# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     # 정보 조회
#     def get(self, request):
#         serializer = UserProfileSerializer(request.user)
#         return Response(serializer.data)
    # 정보 수정
    # def put(self, request):
    #     serializer = UserSerializer(request.user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 프로필 수정
class UserProfileEditView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = UserProfileEditSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 프로필 요청시 필요 데이터 전부 전송   
class UserProfileTotalView(APIView):
    def get(self, request, nickname):
        user = get_object_or_404(User, nickname=nickname)
        serializer = UserProfileTotalSerializer(user)
        return Response(serializer.data)
    
# 영화 명대사와 프로필 이미지
# class UserProfileView(APIView):
#     def get(self, request):
#         user_profile = UserProfile.objects.get(user=request.user)  # 현재 로그인한 사용자의 프로필 정보를 조회
#         serializer = UserProfileSerializer(user_profile)  # 조회된 프로필 정보를 시리얼라이징
#         return Response(serializer.data)  # 시리얼라이즈된 데이터를 응답으로 반환

#     def post(self, request):
#         user_profile = UserProfile.objects.get(user=request.user)  # 현재 로그인한 사용자의 프로필 정보를 조회
#         serializer = UserProfileSerializer(user_profile, data=request.data)  # 요청 데이터로 시리얼라이저 초기화
#         if serializer.is_valid():  # 데이터 검증
#             serializer.save()  # 검증된 데이터를 사용하여 프로필 정보 업데이트
#             return Response(serializer.data)  # 업데이트된 데이터를 응답으로 반환
#         return Response(serializer.errors, status=400)  # 데이터 검증 실패 시 에러 응답 반환

# 로그인할 때 토큰 값과 username이 같이 넘어가도록
class CustomLoginView(LoginView):
    def get_response(self):
        original_response = super().get_response()
        mydata = {
            "nickname": self.user.nickname,
            "user_id": self.user.id,
            }
        original_response.data.update(mydata)
        return original_response
    
# 방명록 처리 view
class GuestbookViewSet(viewsets.ModelViewSet):
    queryset = Guestbook.objects.all()
    serializer_class = GuestbookSerializer
    # 인증된 사용자만 리뷰 작성
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 방명록 작성
    def perform_create(self, serializer):
        user = self.request.user
        target_user_id = self.request.data.get('target_user')
        target_user = User.objects.get(id=target_user_id)
        
        serializer.save(user=user, target_user=target_user, target_user_nickname=target_user.nickname)

    # 방명록 목록
    def get_queryset(self):
        queryset = Guestbook.objects.all()
        nickname = self.request.query_params.get('nickname')

        if nickname is not None:
            queryset = queryset.filter(target_user__nickname=nickname)

        return queryset
    
    # 방명록 수정
    def update(self, request, pk=None):
        guestbook = self.get_object()

        # 수정 권한 확인: 작성자만 수정 가능
        if guestbook.user != request.user:
            raise PermissionDenied("권한이 없습니다.")

        serializer = self.get_serializer(guestbook, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # 방명록 삭제
    def destroy(self, request, pk=None):
        guestbook = self.get_object()

        # 삭제 권한 확인: 작성자와 방명록 주인만 삭제 가능
        if guestbook.user != request.user and guestbook.target_user != request.user:
            raise PermissionDenied("권한이 없습니다.")

        self.perform_destroy(guestbook)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 방명록 대댓글 작성
class GuestbookCommentViewSet(viewsets.ModelViewSet):
    queryset = GuestbookComment.objects.all()
    serializer_class = GuestbookCommentSerializer
    # 인증된 사용자만 대댓글 작성
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 대댓글 작성
    def perform_create(self, serializer):
        user = self.request.user
        guestbook_id = self.request.data.get('guestbook')
        guestbook = get_object_or_404(Guestbook, pk=guestbook_id)
        serializer.save(user=user, guestbook=guestbook, user_nickname=user.nickname)
