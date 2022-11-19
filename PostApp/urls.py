from django.urls import path

from . import views

urlpatterns = [
    path('', views.Post_create_view, name='PostsAPI'),
    path('list/', views.Post_list_view, name='PostList'),
    path('detail/<pk>', views.Post_detail_view, name='PostInfoAPI'),
    path('<pk>/updatepost/',views.Post_update_view, name='PostUpdaetAPI'),
    path('<pk>/deletepost/', views.Post_delete_view, name='PostDeleteAPI'),
]