from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsAPI.as_view(), name='PostsAPI'),
    path('<pk>', views.PostInfoAPI.as_view(), name='PostInfoAPI'),
    path('<pk>/modifypost/',views.ModifyPostAPI.as_view(), name='ModifyPostApi'),
    path('<pk>/deletepost/', views.DeletePostApi.as_view(), name='DeletePostApi'),
    # path('<pk>/commentView/', views.CommentView.as_view(), name='CommentView'),
    # path('<pk>/likeview/', views.LikeView.as_view(), name='LikeView'),
]