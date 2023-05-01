from django.urls import path
from . import auth
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from . import views

urlpatterns = [
     path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
    # path('', views.UserRecordView.as_view(), name="create"),
    # path('login/', auth.CustomAuthToken.as_view() , name="login"),
    # path('logout/', views.Logout.as_view(), name="logout"),
    # path('self-info/', views.UserProfileInfoView.as_view(), name='UserInfoAPI'),
    # path('followingtag/<str:username>',views.UserFollowedTags.as_view()),
    # path('<pk>/update', views.user_update_destroy_view, name = 'update'),
    # path('<pk>/delete', views.user_update_destroy_view, name = 'destroy'),
    
