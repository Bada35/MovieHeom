from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('movies/', include('movies.urls')),
]
