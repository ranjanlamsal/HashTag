from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth/',obtain_auth_token),
    path('tag/', include('Tag.urls')),
    path('user/', include('User.urls')),
    path('post/', include('PostApp.urls')),
]