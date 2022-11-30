from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='UpdateSelfPostsAPI'),
    path('update/<int:id>', views.SelfPostUpdateView.as_view(), name='SelfPostUpdateView'),
    path('list/', views.Post_list_view, name='PostList'),
    path('detail/<int:pk>', views.Post_detail_view, name='PostInfoAPI'),
    path('self/', views.SelfPostListCreateView.as_view(), name = 'SelfPostListcreateView'),
    path('list/<int:id>', views.TagPosts.as_view(), name = 'TagPosts'),
    path('upvoted_by/<int:id>', views.UserLikedPosts.as_view(), name = 'UserLikedPosts'),
    path('upvote/<int:id>', views.UpvotePost.as_view(), name = 'UpvotePost'),
    path('downvote/<int:id>', views.DownvotePost.as_view(), name = 'DownvotePost'),
]