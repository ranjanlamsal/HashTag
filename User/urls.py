from django.urls import path

from User.views import Login, Logout, User_Create_APIView

from . import views

urlpatterns = [
    path('addUser/', User_Create_APIView.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('', views.UserAPI.as_view(), name='UserAPI'),
    path('<pk>/', views.UserInfoAPI.as_view(), name='UserInfoAPI'),
    path('<pk>/followed', views.UserFollowedTagAPI.as_view(), name='UserFollowedTagAPI'),
    
]