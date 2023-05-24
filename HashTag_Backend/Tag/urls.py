from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagView.as_view(), name="tagcreateview"),
    path('self/update/<int:id>', views.SelfTagView.as_view(), name = "SelfTagUpdateDeleteView"),
    path('self/', views.SelfTagGetView.as_view(), name = "SelfTagListView"),
    path('self/count', views.SelfTotalTag.as_view(), name = "SelfTagCountView"),
    
    path('list/', views.TagListAPIView.as_view(), name = "ListTagView"),
    path('detail/<str:title>', views.TagDetailAPIView.as_view(), name = "TagDetailView"),
    path('followers/<str:tagname>',views.GetTagFollowers.as_view(), name = "TagFollowers"),
    path('followtag/<str:title>', views.FollowTagView.as_view(), name='followtag'),
    path('trending/',views.TrendingTags.as_view(), name='trendingtags'),
    path('suggested/', views.SuggestedTags.as_view(), name='suggestedtags'),
    path('usertagfolowingsignal/<str:title>', views.TagUserFollowSignal.as_view(), name='taguserfollowingsignal'),
    path('recommend/', views.RecommendTags.as_view(), name='recommendtags'),
]