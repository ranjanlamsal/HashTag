from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserAPI.as_view(), name='UserAPI'),
    path('<pk>', views.UserInfoAPI.as_view(), name='UserInfoAPI'),
    path('<pk>/followed', views.UserFollowedTagAPI.as_view(), name='UserFollowedTagAPI'),
]