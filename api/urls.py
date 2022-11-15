from django.urls import path, include
from .auth import CustomAuthToken
urlpatterns = [
    path('auth/',CustomAuthToken.as_view()),
    path('tag/', include('Tag.urls')),
    path('user/', include('User.urls')),
    path('post/', include('PostApp.urls')),
]