from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagListCreateAPIView.as_view()),
    path('<pk>', views.TagDetailAPIView.as_view()),
    path('followers/<str:tagname>',views.GetTagFollowers.as_view()),
    
]
