from django.urls import path

from . import views

urlpatterns = [
    path('', views.Post_list_create_view, name='PostsAPI'),
    path('<pk>', views.Post_detail_view, name='PostInfoAPI'),
    path('<pk>/updatepost/',views.Post_update_view, name='PostUpdaetAPI'),
    path('<pk>/deletepost/', views.Post_delete_view, name='PostDeleteAPI'),
]