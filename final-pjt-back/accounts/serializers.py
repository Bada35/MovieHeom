from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=False, allow_blank=False)
    email = serializers.EmailField(max_length=254, required=False, allow_blank=True)
    birth_date = serializers.DateField(required=False, allow_null=True)
    # profile_picture = serializers.ImageField(required=False, allow_null=True, use_url=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
            'birth_date': self.validated_data.get('birth_date', None),
            # 'profile_picture': self.validated_data.get('profile_picture', None),
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
        fields = '__all__'

# 프로필 조회용
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password', 'username', 'birth_date',]

# 프로필 수정용
class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email',]

class UserProfileTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email']