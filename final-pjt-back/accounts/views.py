from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserProfileSerializer, UserProfileEditSerializer

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
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    # 정보 조회
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
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
        serializer = UserProfileEditSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)