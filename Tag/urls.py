from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagView.as_view(), name="tagcreateview"),
    path('self/<int:id>', views.SelfTagView.as_view(), name = "SelfTagListUpdateDeleteView"),
    path('list/', views.TagListAPIView.as_view(), name = "ListTagView"),
    path('detail/<int:pk>/', views.TagDetailAPIView.as_view(), name = "TagDetailView"),
    path('followers/<str:tagname>/',views.GetTagFollowers.as_view(), name = "TagFollowers"),
    # path('followtag/<int:id>/', views.FollowTagView.as_view(), name='followtag'),
    
]
