from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User, Guestbook
from .serializers import UserSerializer, UserProfileEditSerializer, UserProfileTotalSerializer, GuestbookSerializer
from dj_rest_auth.views import LoginView

# 팔로우 기능
class FollowUserView(APIView):
    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.followers.filter(username=username).exists():
            request.user.followers.remove(target_user)
            return Response({"status": "unfollowed"})
        else:
            request.user.followers.add(target_user)
            return Response({"status": "followed"})

# 팔로워 목록        
class FollowersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        followers = user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)

# 팔로잉 목록
class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
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
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
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
        mydata = {"username": self.user.username}
        original_response.data.update(mydata)
        return original_response
    
# 방명록 처리 view
class GuestbookViewSet(viewsets.ModelViewSet):
    queryset = Guestbook.objects.all()
    serializer_class = GuestbookSerializer