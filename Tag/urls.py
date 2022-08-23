from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTagsAPI.as_view()),
    path('<pk>', views.TagAPI.as_view()),
]
