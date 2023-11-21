from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_username, user_field
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    favorite_quote = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # 팔로우
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')

    USERNAME_FIELD = 'username'



class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user_email(user, data.get('email'))
        user_username(user, data.get('username'))

        # 사용자 정의 필드
        user.nickname = data.get('nickname', '')
        user.birth_date = data.get('birth_date', None)
        user.profile_picture = data.get('profile_picture', None)
        user.favorite_quote = data.get('favorite_quote', None)

        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)

        if commit:
            user.save()
        return user

# 영화 명대사와 프로필 이미지 관리
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     favorite_quote = models.TextField(blank=True, null=True)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

# 방명록
class Guestbook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='guestbook')
    target_user_nickname = models.TextField(editable=False)
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_guestbook')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
