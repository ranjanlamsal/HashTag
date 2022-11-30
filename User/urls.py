from django.urls import path
from . import auth

from . import views

urlpatterns = [
    path('', views.UserRecordView.as_view(), name="create"),
    path('list/', views.userlistview, name="userlist"),
    path('login/', auth.CustomAuthToken.as_view() , name="login"),
    # path('logout/', views.Logout.as_view(), name="logout"),
    path('<int:pk>/', views.user_detail_view, name='UserInfoAPI'),
    # path('followingtag/<str:username>',views.UserFollowedTags.as_view()),
    # path('<pk>/update', views.user_update_destroy_view, name = 'update'),
    # path('<pk>/delete', views.user_update_destroy_view, name = 'destroy'),
    
]