from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.PostView.as_view(), name='UpdateSelfPostsAPI'),#
    path('update/<int:id>', views.SelfPostUpdateView.as_view(), name='SelfPostUpdateView'),
    # path('list/', views.Post_list_view, name='PostList'),#
    path('list/', views.PostRandomListView.as_view(), name='PostRandomListView'),
    path('detail/<int:pk>', views.Post_detail_view, name='PostInfoAPI'),#
    path('self/', views.SelfPostListCreateView.as_view(), name = 'SelfPostListcreateView'),
    path('self/count/', views.TotalPost.as_view(), name = 'TotalSelfPostView'),#
    
    path('list/<str:title>', views.TagPosts.as_view(), name = 'TagPosts'),
    path('totalposttag/', views.TotalPostTag.as_view(), name = 'TagPosts'),
    path('upvoted_by/', views.UserLikedPosts.as_view(), name = 'UserLikedPosts'),
    path('upvote/<int:id>', views.UpvotePost.as_view(), name = 'UpvotePost'),
    path('downvote/<int:id>', views.DownvotePost.as_view(), name = 'DownvotePost'),
    path('trending-date/', views.TrendingPostbyDate.as_view(), name = 'TrendingPostbyDate'),
    path('trending-upvotes/', views.TrendingPostByUpvoteCount.as_view(), name = 'TrendingPostbyUpvoteCount'),
    path('comment/<int:id>', views.CommentView.as_view(), name = 'CommentView'),
    path('reply/<int:id>', views.ReplyView.as_view(), name='ReplyView'),
    # path('posts/<int:post_id>/comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_comments'),
]