from django.urls import path

from . import views

urlpatterns = [
    path('', views.userlistcreateview, name="listcreate`"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('<pk>/', views.user_detail_view, name='UserInfoAPI'),
    path('<pk>/update', views.user_update_destroy_view, name = 'update'),
    path('<pk>/delete', views.user_update_destroy_view, name = 'destroy'),
    
]