from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User, Guestbook, GuestbookComment

from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.serializers import ReviewSerializer, MovieLikeSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=False, allow_blank=False)
    email = serializers.EmailField(max_length=50, required=False, allow_blank=True)
    birth_date = serializers.DateField(required=False, allow_null=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True, use_url=True)
    # favorite_quote = serializers.CharField(max_length=50, required=False, allow_null=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
            'birth_date': self.validated_data.get('birth_date', None),
            'profile_picture': self.validated_data.get('profile_picture', None),
            # 'favorite_quote': self.validated_data.get('favorite_quote', None),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname',]

# 프로필 조회용
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['nickname', 'email', 'password', 'username', 'birth_date',]

# 프로필 수정용
class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'favorite_quote', 'profile_picture', 'bgm_url']

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.email = validated_data.get('email', instance.email)
        instance.favorite_quote = validated_data.get('favorite_quote', instance.favorite_quote)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.bgm_url = validated_data.get('bgm_url', instance.bgm_url)

        instance.save()
        return instance


# 남의 프로필 구경가기
class UserProfileTotalSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    liked_movies = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'birth_date', 'favorite_quote', 'bgm_url', 'profile_picture', 'reviews', 'liked_movies']

    def get_reviews(self, obj):
        from movies.models import Review
        reviews = Review.objects.filter(user=obj)
        return ReviewSerializer(reviews, many=True).data
    
    def get_liked_movies(self, obj):
        from movies.models import MovieLike
        liked_movies = MovieLike.objects.filter(user=obj)
        return MovieLikeSerializer(liked_movies, many=True).data
    
# 영화 명대사와 프로필 이미지

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['favorite_quote', 'profile_image']

# 방명록
class GuestbookSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Guestbook
        fields = ['id', 'user', 'target_user', 'target_user_nickname', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['target_user_nickname']

    def get_comments(self, obj):
        # from .serializers import GuestbookCommentSerializer
        # comments = obj.take_guestbook.all()
        # return GuestbookCommentSerializer(comments, many=True).data
        from .models import GuestbookComment
        comments = GuestbookComment.objects.filter(guestbook=obj)
        return GuestbookCommentSerializer(comments, many=True).data

# 방명록 대댓글
class GuestbookCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestbookComment
        fields = ['id', 'user', 'guestbook', 'user_nickname', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user_nickname']